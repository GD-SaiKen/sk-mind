<template>
  <div class="page-layout">
    <Index
      title="接入任务"
      :breadcrumb="[{ label: '首页', to: '/' }, { label: '接入任务' }]"
      description="管理数据接入任务，配置同步策略，跟踪执行状态和结果。"
    >
      <template #actions>
        <el-button type="primary" :icon="Plus" @click="router.push('/ingestion/create')">创建任务</el-button>
      </template>
    </Index>

    <!-- 统计卡片 -->
    <div class="stat-grid">
      <div v-for="card in statCards" :key="card.label" class="stat-card">
        <div class="sc-top">
          <div :class="['sc-icon', card.iconBg]">
            <el-icon :size="16"><component :is="card.icon" /></el-icon>
          </div>
          <span class="sc-label">{{ card.label }}</span>
          <el-tag v-if="card.badge" :type="card.badgeType" effect="plain">{{ card.badge }}</el-tag>
        </div>
        <div :class="['sc-value', card.color]">{{ card.value }}</div>
        <div class="sc-foot">{{ card.footer }}</div>
      </div>
    </div>

    <!-- CRUD 表格区 -->
    <Crud :filter-items="filterItems" v-model:filter-values="filterValues" :pagination="paginationConfig" @filter-change="loadTasks">
      <template #table>
        <Table ref="tableRef" :columns="columns" :data="tasks" :loading="loading">
          <template #col-name="{ row }">
            <el-link type="primary" :underline="false" @click="router.push(`/ingestion/${row.id}`)">
              {{ row.name }}
            </el-link>
          </template>
          <template #col-lastSyncAt="{ row }">
            <span v-if="row.lastSyncAt" :style="{ color: syncFreshColor(row.lastSyncAt) }">
              {{ fmtDateTime(row.lastSyncAt, false) }}
            </span>
            <span v-else class="never-sync">未同步过</span>
          </template>
          <template #col-actions="{ row }">
            <template v-if="running[row.id]">
              <div class="inline-progress">
                <span class="ip-step">{{ running[row.id].step }}</span>
                <div class="ip-row">
                  <el-progress
                    :percentage="running[row.id].pct >= 0 ? running[row.id].pct : 0"
                    :indeterminate="running[row.id].pct < 0"
                    :stroke-width="6"
                    :show-text="false"
                    style="width: 100px"
                  />
                  <el-tooltip content="停止" placement="top">
                    <el-button type="danger" :icon="VideoPause" circle @click="handleCancel(row.id, running[row.id].batchId)" />
                  </el-tooltip>
                </div>
              </div>
            </template>
            <template v-else>
              <div class="action-btns">
                <el-tooltip content="详情" placement="top">
                  <el-button :icon="View" circle @click="router.push(`/ingestion/${row.id}`)" />
                </el-tooltip>
                <el-tooltip content="编辑" placement="top">
                  <el-button :icon="Edit" circle @click="router.push(`/ingestion/${row.id}/edit`)" />
                </el-tooltip>
                <el-tooltip content="执行同步" placement="top">
                  <el-button type="success" :icon="VideoPlay" circle @click="handleExecute(row)" />
                </el-tooltip>
                <el-tooltip v-if="row.status === 'active'" content="停用" placement="top">
                  <el-button type="danger" :icon="CircleCloseFilled" circle @click="handleDisable(row)" />
                </el-tooltip>
                <el-tooltip v-else content="启用" placement="top">
                  <el-button type="primary" :icon="CircleCheck" circle @click="handleEnable(row)" />
                </el-tooltip>
              </div>
            </template>
          </template>
        </Table>
      </template>
    </Crud>
  </div>
</template>

<script setup lang="ts">
import { computed, onMounted, onUnmounted, reactive, ref } from 'vue'
import { useRouter } from 'vue-router'
import {
  CircleCheck, CircleCloseFilled, Clock, Collection, DataAnalysis, Edit, Plus, Search, VideoPause, VideoPlay, View, WarningFilled,
} from '@element-plus/icons-vue'
import { ElMessage, ElMessageBox } from 'element-plus'
import { dataSourceService, ingestionService, type IngestionTask, type DataSource } from '@/api'
import Index from '@/components/page-header/index.vue'
import { Crud, Table } from '@/components/crud'
import type { ColumnSchema, FilterItem } from '@/components/crud'
import { fmtDateTime } from '@/utils/datetime'

const router = useRouter()
const tableRef = ref()
const tasks = ref<IngestionTask[]>([])
const loading = ref(false)

// 动态数据源筛选选项
const dataSourceOptions = ref<{ label: string; value: string }[]>([{ label: '全部', value: '' }])
const dataSources = ref<DataSource[]>([])

const filterItems: FilterItem[] = [
  { key: 'keyword', placeholder: '搜索任务名称...', width: '240px' },
  { key: 'sourceId', type: 'select', placeholder: '数据源', width: '140px',
    options: dataSourceOptions.value },
  { key: 'status', type: 'select', placeholder: '状态', width: '110px',
    options: [
      { label: '全部', value: '' }, { label: '正常', value: 'active' },
      { label: '草稿', value: 'draft' }, { label: '停用', value: 'paused' },
    ] },
]
const filterValues = ref<Record<string, any>>({})
const running = reactive<Record<string, { pct: number; step: string; batchId: string }>>({})
let _pollEss: EventSource[] = []

const page = ref(1)
const pageSize = ref(20)
const total = ref(0)

const paginationConfig = reactive({
  get page() { return page.value }, set page(v: number) { page.value = v },
  get pageSize() { return pageSize.value }, set pageSize(v: number) { pageSize.value = v },
  get total() { return total.value },
  onPageChange() { loadTasks() },
  onSizeChange() { page.value = 1; loadTasks() },
})

const statusMap: Record<string, { text: string; type: '' | 'success' | 'warning' | 'danger' | 'info' }> = {
  draft: { text: '草稿', type: 'info' }, active: { text: '正常', type: 'success' },
  paused: { text: '停用', type: 'warning' }, disabled: { text: '已禁用', type: 'danger' },
}

const columns: ColumnSchema[] = [
  { type: 'custom', prop: 'name', label: '任务名称', minWidth: 180 },
  { type: 'text', prop: 'code', label: '编码', width: 150 },
  { type: 'text', prop: 'scheduleType', label: '调度频率', width: 110, formatter: (v: string) => v === 'cron' ? '定时' : v === 'manual' ? '手动触发' : v === 'interval' ? '每小时' : v || '手动触发' },
  { type: 'custom', prop: 'lastSyncAt', label: '最近同步', width: 170 },
  { type: 'tag', prop: 'status', label: '状态', width: 90, formatter: (v: string) => statusMap[v]?.text ?? v, tagMap: { active: 'success', draft: 'info', paused: 'warning', disabled: 'danger' } },
  { type: 'text', prop: 'createdAt', label: '创建时间', width: 170 },
  { type: 'custom', prop: 'actions', label: '操作', width: 280, align: 'center' },
]

const statCards = computed(() => {
  const activeTasks = tasks.value.filter(t => t.status === 'active')
  const staleTasks = activeTasks.filter(t => {
    if (!t.lastSyncAt) return true
    return Date.now() - new Date(t.lastSyncAt).getTime() > 24 * 3600000
  })
  const lastSync = activeTasks.map(t => t.lastSyncAt).filter(Boolean).sort().pop()
  type Card = { label: string; value: number; icon: any; iconBg: string; footer: string; color?: string; badge?: string; badgeType?: string }
  return [
    { label: '活跃任务', value: activeTasks.length, icon: Collection, iconBg: 'sc-icon-blue', footer: lastSync ? `最近同步: ${fmtDateTime(lastSync, false)}` : '暂无同步记录' },
    { label: '数据新鲜', value: activeTasks.length - staleTasks.length, icon: CircleCheck, iconBg: 'sc-icon-green', color: 'green', footer: '24h 内有同步' },
    { label: '数据过期', value: staleTasks.length, icon: WarningFilled, iconBg: 'sc-icon-yellow', color: 'yellow', footer: '超过 24h 未更新' },
    { label: '停用', value: tasks.value.filter(t => t.status === 'paused' || t.status === 'disabled').length, icon: CircleCloseFilled, iconBg: 'sc-icon-red', color: 'red', footer: '已停用的任务' },
  ] as Card[]
})

async function loadDataSources() {
  try {
    const result = await dataSourceService.getList({ page: 1, pageSize: 100 })
    const items = (result.items ?? []) as DataSource[]
    dataSources.value = items
    dataSourceOptions.value = [
      { label: '全部', value: '' },
      ...items.map(ds => ({ label: `${ds.name} (${ds.code})`, value: ds.id })),
    ]
  } catch { /* ignore */ }
}

async function loadTasks() {
  loading.value = true
  try {
    const res = await ingestionService.getList({
      keyword: filterValues.value.keyword || undefined,
      status: filterValues.value.status || undefined,
      dataSourceId: filterValues.value.sourceId || undefined,
      page: page.value, pageSize: pageSize.value,
    })
    tasks.value = res.items
    total.value = res.total
  } finally { loading.value = false }
}

async function handleExecute(task: IngestionTask) {
  try {
    const { batchId } = await ingestionService.execute(task.id)
    ElMessage.success('已提交')
    startPoll(task.id, batchId)
  } catch { /* handled */ }
}

function startPoll(taskId: string, batchId: string) {
  running[taskId] = { pct: -1, step: '等待 Worker...', batchId }
  const es = ingestionService.streamProgress(
    batchId,
    (d) => { running[taskId] = { pct: d.pct, step: d.step, batchId } },
    () => { setTimeout(() => delete running[taskId], 3000); loadTasks() },
  )
  _pollEss.push(es)
}

async function handleCancel(taskId: string, batchId: string) {
  try { await ingestionService.cancelBatch(batchId); ElMessage.success('取消信号已发送') } catch { /* handled */ }
}

async function handleEnable(task: IngestionTask) {
  try {
    await ingestionService.enable(task.id)
    ElMessage.success('已启用')
    await loadTasks()
  } catch { /* handled */ }
}

async function handleDisable(task: IngestionTask) {
  try {
    await ElMessageBox.confirm('确定停用该任务？', '确认')
    await ingestionService.disable(task.id)
    ElMessage.success('已停用')
    await loadTasks()
  } catch { /* handled */ }
}

onMounted(() => { loadDataSources(); loadTasks() })
onUnmounted(() => _pollEss.forEach(es => es.close()))

function syncFreshColor(lastSyncAt: string | null): string {
  if (!lastSyncAt) return '#909399'
  const ms = Date.now() - new Date(lastSyncAt).getTime()
  const hours = ms / 3600000
  if (hours < 6) return '#67c23a'
  if (hours < 24) return '#e6a23c'
  return '#f56c6c'
}
</script>

<style lang="scss" scoped>
.page { }

.stat-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 16px;
  margin-bottom: 16px;
}

.stat-card {
  display: flex; flex-direction: column; justify-content: space-between;
  height: 160px; padding: 20px;
  border: 1px solid $color-border-light; border-radius: $radius-base;
  background: $color-bg-white;
}

.sc-top { display: flex; align-items: center; gap: 8px; }
.sc-icon {
  display: flex; align-items: center; justify-content: center;
  width: 32px; height: 32px; border-radius: $radius-base;
  &-blue { background: #dbeafe; color: $color-primary; }
  &-green { background: #dcfce7; color: $color-success; }
  &-yellow { background: #fef9c3; color: $color-warning; }
  &-red { background: #fee2e2; color: $color-danger; }
}
.sc-label { font-size: $font-size-base; color: $color-text-secondary; flex: 1; }
.sc-value {
  font-size: $font-size-3xl; font-weight: $font-weight-bold;
  color: $color-text-primary; margin: 6px 0 2px;
  &.green { color: $color-success; }
  &.yellow { color: $color-warning; }
  &.red { color: $color-danger; }
}
.sc-foot { font-size: $font-size-xs; color: $color-text-placeholder; }

.never-sync { color: $color-text-placeholder; font-size: $font-size-xs; }
.action-btns { display: flex; align-items: center; justify-content: center; gap: 4px; }
.inline-progress { display: flex; flex-direction: column; gap: 4px; }
.ip-step { font-size: 11px; color: $color-primary; }
.ip-row { display: flex; align-items: center; gap: 6px; }
</style>
