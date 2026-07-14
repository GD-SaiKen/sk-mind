<template>
  <div class="page" v-if="task">
    <div class="title-row">
      <h1>{{ task.name }}</h1>
      <el-tag type="success" size="small" effect="plain">正常</el-tag>
      <el-tag type="info" size="small" effect="plain">{{ task.code }}</el-tag>
      <div class="spacer" />
      <el-button type="primary" :icon="VideoPlay" :loading="executing" size="small" @click="handleExecute">立即执行</el-button>
      <el-dropdown trigger="click" size="small">
        <el-button :icon="Clock" size="small">补拉数据</el-button>
        <template #dropdown>
          <el-dropdown-menu>
            <el-dropdown-item @click="handleQuickFill(1)">补拉昨天</el-dropdown-item>
            <el-dropdown-item @click="handleQuickFill(7)">补拉最近 7 天</el-dropdown-item>
            <el-dropdown-item @click="handleQuickFill(30)">补拉最近 30 天</el-dropdown-item>
            <el-dropdown-item divided @click="handleBackfill">全量回溯（从上线日期至今）</el-dropdown-item>
          </el-dropdown-menu>
        </template>
      </el-dropdown>
      <el-button size="small">编辑</el-button>
    </div>

    <div class="summary-row">
      <div v-for="s in summary" :key="s.label" class="sum-item">
        <span class="sum-label">{{ s.label }}</span>
        <span class="sum-val">{{ s.value }}</span>
      </div>
    </div>

    <el-tabs v-model="activeTab">
      <el-tab-pane label="当前配置" name="config">
        <el-descriptions :column="2" border size="small" style="max-width: 600px">
          <el-descriptions-item label="名称">{{ task.name }}</el-descriptions-item>
          <el-descriptions-item label="编码">{{ task.code }}</el-descriptions-item>
          <el-descriptions-item label="同步模式">{{ task.syncMode === 'incremental' ? '增量同步' : '全量同步' }}</el-descriptions-item>
          <el-descriptions-item label="调度">{{ task.scheduleType === 'cron' ? `定时 (${task.cronExpression})` : task.scheduleType }}</el-descriptions-item>
          <el-descriptions-item label="最近同步">{{ task.lastSyncAt?.slice(0, 19) || '未同步过' }}</el-descriptions-item>
          <el-descriptions-item label="上次结果">{{ task.lastSyncStatus || '-' }}</el-descriptions-item>
          <el-descriptions-item label="创建时间">{{ task.createdAt?.slice(0, 19) }}</el-descriptions-item>
        </el-descriptions>
      </el-tab-pane>

      <el-tab-pane :label="`执行记录 (${batches.length})`" name="batches">
        <Index :pagination="batchesPagination">
          <template #table>
            <Table :columns="batchesColumns" :data="batches" size="small">
              <!-- 时间 -->
              <template #col-createdAt="{ row }">
                {{ row.createdAt?.slice(0, 19).replace('T', ' ') }}
              </template>
              <!-- 触发 -->
              <template #col-triggerType="{ row }">
                <span class="trigger-text">{{ triggerLabel[row.triggerType] ?? row.triggerType }}</span>
              </template>
              <!-- 状态/进度 -->
              <template #col-status="{ row }">
                <div class="status-cell">
                  <el-tag :type="batchType[row.status]" size="small" effect="plain">
                    {{ batchLabel[row.status] ?? row.status }}
                  </el-tag>
                  <template v-if="row.status === 'running'">
                    <el-progress
                      :percentage="row._pct >= 0 ? row._pct : 0"
                      :indeterminate="row._pct < 0"
                      :stroke-width="5"
                      :show-text="false"
                      style="width: 100%"
                    />
                    <span v-if="row._step" class="step-text">{{ row._step }}</span>
                  </template>
                  <span v-if="row.errorSummary" class="err-text">{{ row.errorSummary }}</span>
                </div>
              </template>
              <!-- 数据量 -->
              <template #col-successCount="{ row }">
                <template v-if="row.status === 'success' || row.status === 'partial_success'">
                  <span class="count-ok">{{ row.successCount?.toLocaleString() }} 行</span>
                  <span v-if="row.failCount > 0" class="count-err"> · {{ row.failCount }} 跳过</span>
                </template>
                <span v-else-if="row.status === 'running'">—</span>
                <span v-else class="count-dim">-</span>
              </template>
              <!-- 耗时 -->
              <template #col-duration="{ row }">
                <span v-if="row.startedAt && row.finishedAt" class="dur-text">
                  {{ duration(row.startedAt, row.finishedAt) }}
                </span>
                <span v-else-if="row.status === 'running' && row.startedAt" class="dur-text">
                  {{ elapsed(row.startedAt) }}
                </span>
                <span v-else>-</span>
              </template>
              <!-- 操作 -->
              <template #col-actions="{ row }">
                <div class="action-btns">
                  <el-button v-if="row.status === 'running'" size="small" text type="danger" @click="handleCancel(row.id)">停止</el-button>
                  <template v-else>
                    <el-button size="small" text @click="showLog(row)">日志</el-button>
                    <el-button
                      v-if="row.status === 'failed' || row.status === 'cancelled'"
                      size="small" text type="warning"
                      @click="handleRetry(row.id)"
                    >重试</el-button>
                  </template>
                </div>
              </template>
            </Table>
          </template>
        </Index>
        <div v-if="batches.length === 0" class="empty">暂无执行记录，点击「立即执行」开始</div>
      </el-tab-pane>
    </el-tabs>

    <!-- 日志弹窗 -->
    <el-dialog v-model="logDialog" title="批次日志" width="700px" destroy-on-close>
      <div class="log-detail">
        <div class="log-meta">
          <span>批次: {{ logBatch?.id?.slice(0, 12) }}...</span>
          <span>触发: {{ triggerLabel[logBatch?.triggerType ?? ''] ?? logBatch?.triggerType }}</span>
          <span v-if="logBatch?.startedAt && logBatch?.finishedAt">耗时: {{ duration(logBatch.startedAt, logBatch.finishedAt) }}</span>
          <span v-if="logBatch?.errorSummary" class="log-err-summary">{{ logBatch.errorSummary }}</span>
        </div>
        <el-table v-if="errorList.length > 0" :data="errorList" stripe size="small" style="margin-top: 12px">
          <el-table-column prop="errorType" label="类型" width="100" />
          <el-table-column prop="errorMessage" label="错误信息" min-width="250" />
          <el-table-column label="位置" width="100">
            <template #default="{ row: e }">{{ e.fieldName || (e.rowNumber ? '行 ' + e.rowNumber : '-') }}</template>
          </el-table-column>
          <el-table-column prop="createdAt" label="时间" width="160">
            <template #default="{ row: e }">{{ e.createdAt?.slice(0, 19).replace('T', ' ') }}</template>
          </el-table-column>
        </el-table>
        <div v-if="errorList.length === 0 && logBatch" class="log-ok">
          {{ logBatch.status === 'success' ? '本次同步无错误' : logBatch.status === 'running' ? '同步进行中...' : '无错误记录' }}
        </div>
      </div>
    </el-dialog>
  </div>
</template>

<script setup lang="ts">
import { computed, onMounted, onUnmounted, reactive, ref } from 'vue'
import { useRoute } from 'vue-router'
import { Clock, VideoPlay } from '@element-plus/icons-vue'
import { ElMessage } from 'element-plus'
import { ingestionService, type IngestionBatch, type ImportError, type IngestionTask } from '@/api'
import { Index, Table } from '@/components/crud'
import type { ColumnSchema } from '@/components/crud'

const route = useRoute()
const taskId = route.params.id as string
const task = ref<IngestionTask | null>(null)
const batches = ref<(IngestionBatch & { _pct?: number; _step?: string })[]>([])
const activeTab = ref('batches')
const executing = ref(false)
const backfilling = ref(false)
const logDialog = ref(false)
const logBatch = ref<IngestionBatch | null>(null)
const errorList = ref<ImportError[]>([])
let _esList: EventSource[] = []

const batchLabel: Record<string, string> = {
  pending: '等待中', running: '运行中', success: '成功', partial_success: '部分成功', failed: '失败', cancelled: '已取消',
}
const batchType: Record<string, '' | 'success' | 'warning' | 'danger' | 'info'> = {
  pending: 'info', running: '', success: 'success', partial_success: 'warning', failed: 'danger', cancelled: 'info',
}
const triggerLabel: Record<string, string> = {
  manual: '手动', scheduled: '定时', retry: '重试', backfill: '全量回溯', quick_fill: '快补',
}

const summary = computed(() => [
  { label: '调度', value: task.value?.scheduleType === 'cron' ? `定时 ${task.value?.cronExpression}` : task.value?.scheduleType ?? '-' },
  { label: '同步模式', value: task.value?.syncMode === 'incremental' ? '增量' : '全量' },
  { label: '最近同步', value: task.value?.lastSyncAt?.slice(0, 16) ?? '未同步过' },
  { label: '上次结果', value: task.value?.lastSyncStatus || '-' },
])

// ---- 分页 ----
const batchesPagination = reactive({ page: 1, pageSize: 20, total: 0, onPageChange() {}, onSizeChange() {} })

// ---- 批次列表列配置 ----
const batchesColumns: ColumnSchema[] = [
  { type: 'custom', prop: 'createdAt', label: '时间', width: 170 },
  { type: 'custom', prop: 'triggerType', label: '触发', width: 90 },
  { type: 'custom', prop: 'status', label: '状态 / 进度', width: 200 },
  { type: 'custom', prop: 'successCount', label: '数据量', width: 160 },
  { type: 'custom', prop: 'duration', label: '耗时', width: 80 },
  { type: 'custom', prop: 'actions', label: '操作', width: 160 },
]

// ---- 工具函数 ----
function duration(start: string, end: string): string {
  const s = (new Date(end).getTime() - new Date(start).getTime()) / 1000
  if (s < 60) return `${s.toFixed(0)}s`
  return `${Math.floor(s / 60)}m${(s % 60).toFixed(0)}s`
}
function elapsed(start: string): string {
  const s = (Date.now() - new Date(start).getTime()) / 1000
  if (s < 60) return `${s.toFixed(0)}s`
  return `${Math.floor(s / 60)}m${(s % 60).toFixed(0)}s`
}

// ---- 数据加载 ----
async function load() {
  task.value = await ingestionService.get(taskId)
  const b = await ingestionService.getBatches(taskId, { pageSize: 50 })
  batches.value = b.items
}

async function handleExecute() {
  executing.value = true
  try {
    const { batchId } = await ingestionService.execute(taskId)
    ElMessage.success('已提交')
    const placeholder: any = { id: batchId, triggerType: 'manual', status: 'pending', recordCount: 0, successCount: 0, failCount: 0, createdAt: new Date().toISOString(), _pct: -1, _step: '等待 Worker...' }
    batches.value.unshift(placeholder)
    const es = ingestionService.streamProgress(batchId,
      (d) => {
        const b = batches.value.find(x => x.id === batchId)
        if (b) { b._pct = d.pct; b._step = d.step; if (d.status !== 'running') b.status = d.status === 'success' ? 'success' : d.status === 'cancelled' ? 'cancelled' : 'failed' }
      },
      () => load(),
    )
    _esList.push(es)
  } catch { /* */ }
  finally { executing.value = false }
}

async function handleRetry(bid: string) {
  try { await ingestionService.retryBatch(bid); ElMessage.success('重试已提交'); await load() } catch { /* */ }
}
async function handleCancel(bid: string) {
  try { await ingestionService.cancelBatch(bid); ElMessage.success('已停止') } catch { /* */ }
}
async function showLog(row: IngestionBatch) {
  logBatch.value = row
  const e = await ingestionService.getBatchErrors(row.id, { pageSize: 50 })
  errorList.value = e.items
  logDialog.value = true
}
async function handleBackfill() {
  backfilling.value = true
  try { await ingestionService.backfill(taskId); ElMessage.success('全量回溯已提交'); await load() } finally { backfilling.value = false }
}
async function handleQuickFill(days: number) {
  const end = new Date(); end.setHours(0, 0, 0, 0)
  const start = new Date(end); start.setDate(start.getDate() - days)
  try { await ingestionService.quickFill(taskId, start.toISOString(), end.toISOString()); ElMessage.success(`快补 ${days} 天已提交`); await load() } catch { /* */ }
}

onMounted(load)
onUnmounted(() => _esList.forEach(es => es.close()))
</script>

<style lang="scss" scoped>
.page { }
.title-row { display: flex; align-items: center; gap: 10px; margin-bottom: 16px; }
.title-row h1 { margin: 0; font-size: $font-size-xl; font-weight: $font-weight-semibold; }
.spacer { flex: 1; }
.summary-row { display: grid; grid-template-columns: repeat(4, 1fr); gap: 12px; margin-bottom: 16px; }
.sum-item { display: flex; flex-direction: column; gap: 4px; padding: 14px 16px; border: 1px solid $color-border-light; border-radius: 6px; }
.sum-label { font-size: $font-size-xs; color: $color-text-placeholder; }
.sum-val { font-size: $font-size-lg; font-weight: $font-weight-semibold; }
.empty { text-align: center; padding: 60px; color: $color-text-placeholder; }

.status-cell { display: flex; flex-direction: column; gap: 4px; }
.step-text { font-size: 11px; color: $color-primary; }
.err-text { font-size: 11px; color: $color-danger; }
.count-ok { font-weight: $font-weight-semibold; color: $color-success; }
.count-err { color: $color-danger; font-size: $font-size-xs; }
.count-dim { color: $color-text-placeholder; }
.dur-text { color: $color-text-secondary; font-size: $font-size-sm; }
.trigger-text { color: $color-text-secondary; font-size: $font-size-sm; }
.action-btns { display: flex; align-items: center; gap: 4px; }

.log-detail { }
.log-meta { display: flex; flex-wrap: wrap; gap: 12px; font-size: $font-size-sm; color: $color-text-secondary; }
.log-err-summary { color: $color-danger; font-weight: $font-weight-semibold; }
.log-ok { text-align: center; padding: 20px; color: $color-text-placeholder; }
</style>
