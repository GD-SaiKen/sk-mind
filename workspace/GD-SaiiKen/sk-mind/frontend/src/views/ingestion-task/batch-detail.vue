<template>
  <div class="page-layout detail-page">
    <Index
      title="批次详情"
      :breadcrumb="[
        { label: '首页', to: '/' },
        { label: '接入任务', to: '/ingestion' },
        { label: taskName, to: `/ingestion/${taskId}` },
        { label: '批次详情' },
      ]"
    >
      <template #tags>
        <el-tag v-if="batch" :type="batchTagType" effect="plain">{{ batchLabel }}</el-tag>
      </template>
    </Index>

    <div v-if="loading" class="loading-wrap"><el-skeleton :rows="5" /></div>

    <template v-else-if="batch">
      <el-row class="summary-row" :gutter="16">
        <el-col :span="6">
          <div class="summary-card"><div class="summary-label">触发方式</div><div class="summary-value">{{ triggerLabel }}</div></div>
        </el-col>
        <el-col :span="6">
          <div class="summary-card"><div class="summary-label">开始时间</div><div class="summary-value">{{ batch.startedAt ?? '-' }}</div></div>
        </el-col>
        <el-col :span="6">
          <div class="summary-card"><div class="summary-label">结束时间</div><div class="summary-value">{{ batch.finishedAt ?? '-' }}</div></div>
        </el-col>
        <el-col :span="6">
          <div class="summary-card"><div class="summary-label">耗时</div><div class="summary-value">{{ duration }}</div></div>
        </el-col>
      </el-row>

      <TabNav v-model="activeTab" :tabs="tabs" />

      <!-- 批次概要 -->
      <div v-if="activeTab === 'summary'" class="tab-content">
        <div class="stat-grid">
          <StatCard :icon="Grid" icon-bg="bg-blue" label="总记录数" :value="batch.recordCount?.toLocaleString() ?? '-'" footer-text="本次批次处理记录" />
          <StatCard :icon="CircleCheckFilled" icon-bg="bg-green" label="成功数量" :value="batch.successCount?.toLocaleString() ?? '-'" value-class="green" footer-text="已入库记录" />
          <StatCard :icon="WarningFilled" icon-bg="bg-yellow" label="失败数量" :value="batch.failCount?.toLocaleString() ?? '-'" :value-class="batch.failCount > 0 ? 'yellow' : ''" :footer-text="batch.failCount > 0 ? '有待处理的错误' : '暂无错误'" />
          <StatCard :icon="CircleCloseFilled" icon-bg="bg-gray" label="跳过数量" :value="batch.skipCount?.toLocaleString() ?? '0'" footer-text="因过滤规则跳过" />
        </div>
        <el-descriptions :column="2" border style="margin-top: 16px">
          <el-descriptions-item label="批次号">{{ batch.id }}</el-descriptions-item>
          <el-descriptions-item label="状态">{{ batchLabel }}</el-descriptions-item>
          <el-descriptions-item label="触发方式">{{ triggerLabel }}</el-descriptions-item>
          <el-descriptions-item label="创建时间">{{ batch.createdAt?.slice(0, 19) }}</el-descriptions-item>
        </el-descriptions>
      </div>

      <!-- 错误清单 -->
      <div v-if="activeTab === 'errors'" class="tab-content">
        <Table
          :columns="errorColumns"
          :data="errors"
          :loading="errorsLoading"
        >
          <template #col-errorType="{ row }">
            <el-tag :type="errorTypeMap[row.errorType] ?? 'info'" effect="plain">{{ row.errorType }}</el-tag>
          </template>
          <template #col-errorMessage="{ row }">
            <span class="err-msg">{{ row.errorMessage }}</span>
          </template>
          <template #col-location="{ row }">
            <span v-if="row.fieldName">{{ row.fieldName }}</span>
            <span v-else-if="row.rowNumber">行 {{ row.rowNumber }}</span>
            <span v-else>-</span>
          </template>
          <template #col-createdAt="{ row }">{{ row.createdAt?.slice(0, 19) }}</template>
        </Table>
        <div v-if="!errorsLoading && errors.length === 0" class="empty">本批次无错误记录</div>
      </div>

      <!-- 产出数据表 -->
      <div v-if="activeTab === 'tables'" class="tab-content">
        <Table
          :columns="outputTableColumns"
          :data="outputTables"
          :loading="tablesLoading"
        >
          <template #col-tableName="{ row }">
            <el-link type="primary" :underline="false" @click="router.push(`/tables/${row.id}`)">{{ row.tableName }}</el-link>
          </template>
          <template #col-layer="{ row }">
            <el-tag effect="plain" :type="row.layer === 'Serving' ? 'success' : row.layer === 'Clean' ? 'warning' : ''">{{ row.layer }}</el-tag>
          </template>
        </Table>
        <div v-if="!tablesLoading && outputTables.length === 0" class="empty">暂无产出数据表</div>
      </div>

      <!-- 日志 -->
      <div v-if="activeTab === 'logs'" class="tab-content">
        <div class="log-list">
          <div v-for="(log, li) in logs" :key="li" class="log-item">
            <span class="log-time">{{ log.time }}</span>
            <el-tag :type="log.level === 'error' ? 'danger' : log.level === 'warning' ? 'warning' : 'info'" effect="plain" size="small">{{ log.level.toUpperCase() }}</el-tag>
            <span class="log-msg">{{ log.message }}</span>
          </div>
        </div>
        <div v-if="logs.length === 0" class="empty">暂无日志</div>
      </div>
    </template>

    <el-empty v-else description="批次不存在" />
  </div>
</template>

<script setup lang="ts">
import { computed, onMounted, ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { CircleCheckFilled, CircleCloseFilled, Collection, Grid, WarningFilled } from '@element-plus/icons-vue'
import { ingestionService } from '@/api'
import type { IngestionBatch, ImportError } from '@/api'
import Index from '@/components/page-header/index.vue'
import TabNav from '@/components/tab-nav/index.vue'
import type { TabItem } from '@/components/tab-nav/index.vue'
import StatCard from '@/components/stat-card/index.vue'
import { Table } from '@/components/crud'
import type { ColumnSchema } from '@/components/crud'

const route = useRoute()
const router = useRouter()

const taskId = route.params.taskId as string
const batchId = route.params.batchId as string
const taskName = (route.query.task as string) || '-'

const activeTab = ref('summary')
const loading = ref(true)
const errorsLoading = ref(false)
const tablesLoading = ref(false)

const batch = ref<IngestionBatch | null>(null)
const errors = ref<ImportError[]>([])
const outputTables = ref<any[]>([])
const logs = ref<{ time: string; level: string; message: string }[]>([])

const tabs: TabItem[] = [
  { key: 'summary', label: '批次概要' },
  { key: 'errors', label: '错误清单', count: 0 },
  { key: 'tables', label: '产出数据表' },
  { key: 'logs', label: '日志' },
]

const batchLabelMap: Record<string, string> = {
  pending: '等待中', running: '运行中', success: '成功',
  partial_success: '部分成功', failed: '失败', cancelled: '已取消',
}
const batchTagMap: Record<string, '' | 'success' | 'warning' | 'danger' | 'info'> = {
  pending: 'info', running: '', success: 'success',
  partial_success: 'warning', failed: 'danger', cancelled: 'info',
}
const triggerLabelMap: Record<string, string> = {
  manual: '手动触发', scheduled: '定时触发', retry: '重试',
  backfill: '全量回溯', quick_fill: '快补',
}
const errorTypeMap: Record<string, '' | 'success' | 'warning' | 'danger' | 'info'> = {
  parse_error: 'danger', type_error: 'danger', missing_required: 'warning',
  duplicate: 'warning', constraint: 'danger', unknown: 'info',
}

const batchLabel = computed(() => batchLabelMap[batch.value?.status ?? ''] ?? batch.value?.status ?? '-')
const batchTagType = computed(() => batchTagMap[batch.value?.status ?? ''] ?? 'info')
const triggerLabel = computed(() => triggerLabelMap[batch.value?.triggerType ?? ''] ?? batch.value?.triggerType ?? '-')
const duration = computed(() => {
  if (!batch.value?.startedAt || !batch.value?.finishedAt) return '-'
  const s = (new Date(batch.value.finishedAt).getTime() - new Date(batch.value.startedAt).getTime()) / 1000
  if (s < 60) return `${s.toFixed(0)}s`
  return `${Math.floor(s / 60)}m${(s % 60).toFixed(0)}s`
})

const errorColumns: ColumnSchema[] = [
  { type: 'custom', prop: 'errorType', label: '错误类型', width: 110 },
  { type: 'custom', prop: 'errorMessage', label: '错误信息', minWidth: 220 },
  { type: 'custom', prop: 'location', label: '位置', width: 100 },
  { type: 'custom', prop: 'createdAt', label: '时间', width: 160 },
]

const outputTableColumns: ColumnSchema[] = [
  { type: 'custom', prop: 'tableName', label: '表名', minWidth: 180 },
  { type: 'text', prop: 'displayName', label: '显示名', minWidth: 140 },
  { type: 'custom', prop: 'layer', label: '层级', width: 90 },
  { type: 'text', prop: 'recordCount', label: '记录数', width: 100, align: 'right', formatter: (v: number) => v?.toLocaleString() ?? '-' },
  { type: 'text', prop: 'fieldCount', label: '字段数', width: 80, align: 'center' },
]

async function loadBatch() {
  loading.value = true
  try {
    batch.value = await ingestionService.getBatch(batchId)
    tabs[1].count = batch.value?.failCount ?? 0
  } finally {
    loading.value = false
  }
}

async function loadErrors() {
  errorsLoading.value = true
  try {
    const r = await ingestionService.getBatchErrors(batchId, { pageSize: 100 })
    errors.value = r.items ?? []
  } finally {
    errorsLoading.value = false
  }
}

async function loadTables() {
  tablesLoading.value = true
  try {
    outputTables.value = []
  } finally {
    tablesLoading.value = false
  }
}

function genLogs() {
  if (!batch.value) return
  const entries: typeof logs.value = []
  if (batch.value.startedAt) entries.push({ time: batch.value.startedAt.slice(0, 19), level: 'info', message: `批次 ${batchId.slice(0, 12)}... 开始执行` })
  if (batch.value.successCount > 0) entries.push({ time: batch.value.finishedAt?.slice(0, 19) ?? '-', level: 'info', message: `成功处理 ${batch.value.successCount} 条记录` })
  if (batch.value.failCount > 0) entries.push({ time: batch.value.finishedAt?.slice(0, 19) ?? '-', level: 'warning', message: `处理失败 ${batch.value.failCount} 条记录` })
  if (batch.value.skipCount > 0) entries.push({ time: batch.value.finishedAt?.slice(0, 19) ?? '-', level: 'info', message: `跳过 ${batch.value.skipCount} 条记录` })
  if (batch.value.status === 'failed') entries.push({ time: batch.value.finishedAt?.slice(0, 19) ?? '-', level: 'error', message: '批次执行失败' })
  if (batch.value.status === 'success') entries.push({ time: batch.value.finishedAt?.slice(0, 19) ?? '-', level: 'info', message: '批次执行成功' })
  logs.value = entries
}

onMounted(async () => {
  await loadBatch()
  genLogs()
})

// Watch tab changes for lazy loading
import { watch } from 'vue'
watch(activeTab, (tab) => {
  if (tab === 'errors' && errors.value.length === 0) loadErrors()
  if (tab === 'tables' && outputTables.value.length === 0) loadTables()
})
</script>

<style lang="scss" scoped>
.loading-wrap { padding: 40px; }

.summary-row { margin: 0 0 16px; }

.summary-card {
  padding: 16px; background: #f9fafb; border: 1px solid #e5e7eb; border-radius: 8px;
}
.summary-label { font-size: 13px; color: #6b7280; margin-bottom: 4px; }
.summary-value { font-size: 16px; color: #1f2937; font-weight: 500; }

.tab-content { padding-top: 16px; }

.stat-grid {
  display: grid; grid-template-columns: repeat(4, 1fr); gap: 16px;
}

:deep(.bg-blue) { background: #dbeafe; color: $color-primary; }
:deep(.bg-green) { background: #dcfce7; color: $color-success; }
:deep(.bg-yellow) { background: #fef3c7; color: $color-warning; }
:deep(.bg-gray) { background: #f3f4f6; color: #6b7280; }

.green { color: $color-success; }
.yellow { color: $color-warning; }

.err-msg { color: $color-text-secondary; font-size: 13px; }

.empty {
  text-align: center; padding: 60px; color: $color-text-placeholder; font-size: 14px;
}

.log-list { display: flex; flex-direction: column; border: 1px solid $color-border; border-radius: 6px; overflow: hidden; }
.log-item {
  display: flex; align-items: flex-start; gap: 12px; padding: 10px 14px;
  border-bottom: 1px solid $color-border-light; font-size: 13px;
  &:last-child { border-bottom: 0; }
  &:hover { background: #f9fafb; }
}
.log-time { color: $color-text-placeholder; white-space: nowrap; font-family: monospace; flex-shrink: 0; }
.log-msg { color: $color-text-regular; flex: 1; }
</style>
