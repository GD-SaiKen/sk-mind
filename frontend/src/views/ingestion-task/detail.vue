<template>
  <div class="page-layout" v-if="task">
    <Index
      :title="task.name"
      :breadcrumb="[{ label: '首页', to: '/' }, { label: '接入任务', to: '/ingestion' }, { label: task.name }]"
    >
      <template #tags>
        <el-tag type="success" effect="plain">正常</el-tag>
        <el-tag type="info" effect="plain">{{ task.code }}</el-tag>
      </template>
      <template #actions>
        <el-button type="primary" :icon="VideoPlay" :loading="executing" @click="handleExecute">立即执行</el-button>
        <template v-if="!isEditing">
          <el-button :icon="Edit" @click="toggleEdit">编辑</el-button>
        </template>
        <template v-else>
          <el-button type="primary" :loading="saving" @click="handleSave">保存</el-button>
          <el-button @click="handleCancelEdit">取消</el-button>
        </template>
      </template>
    </Index>

    <div class="summary-row">
      <div v-for="s in summary" :key="s.label" class="sum-item">
        <span class="sum-label">{{ s.label }}</span>
        <span class="sum-val">{{ s.value }}</span>
      </div>
    </div>

    <el-tabs v-model="activeTab">
      <el-tab-pane label="当前配置" name="config">
        <template v-if="!isEditing">
          <el-descriptions :column="2" border style="max-width: 600px">
            <el-descriptions-item label="名称">{{ task.name }}</el-descriptions-item>
            <el-descriptions-item label="编码">{{ task.code }}</el-descriptions-item>
            <el-descriptions-item label="调度">{{ task.scheduleType === 'cron' ? `定时 (${task.cronExpression})` : task.scheduleType }}</el-descriptions-item>
            <el-descriptions-item label="最近同步">{{ task.lastSyncAt?.slice(0, 19) || '未同步过' }}</el-descriptions-item>
            <el-descriptions-item label="上次结果">{{ task.lastSyncStatus || '-' }}</el-descriptions-item>
            <el-descriptions-item label="创建时间">{{ task.createdAt?.slice(0, 19) }}</el-descriptions-item>
          </el-descriptions>
        </template>
        <template v-else>
          <el-form :model="editForm" label-width="100px" style="max-width: 500px">
            <el-form-item label="名称">
              <el-input v-model="editForm.name" />
            </el-form-item>
            <el-form-item label="编码">
              <el-input :model-value="task.code" disabled />
            </el-form-item>
            <el-form-item label="调度方式">
              <el-select v-model="editForm.scheduleType" style="width: 100%">
                <el-option label="手动触发" value="manual" />
                <el-option label="定时" value="cron" />
              </el-select>
            </el-form-item>
            <el-form-item v-if="editForm.scheduleType === 'cron'" label="Cron 表达式">
              <el-input v-model="editForm.cronExpression" placeholder="0 0 */30 * * ?" />
            </el-form-item>
            <el-form-item label="描述">
              <el-input v-model="editForm.description" type="textarea" :rows="3" />
            </el-form-item>
          </el-form>
        </template>
      </el-tab-pane>

      <el-tab-pane :label="`执行记录 (${batches.length})`" name="batches">
        <Crud :pagination="batchesPagination">
          <template #table>
            <Table :columns="batchesColumns" :data="batches">
              <template #col-createdAt="{ row }">{{ row.createdAt?.slice(0, 19).replace('T', ' ') }}</template>
              <template #col-triggerType="{ row }"><span class="trigger-text">{{ triggerLabel[row.triggerType] ?? row.triggerType }}</span></template>
              <template #col-status="{ row }">
                <div class="status-cell">
                  <el-tag :type="batchType[row.status]" effect="plain">{{ batchLabel[row.status] ?? row.status }}</el-tag>
                  <template v-if="row.status === 'running'">
                    <el-progress :percentage="row._pct >= 0 ? row._pct : 0" :indeterminate="row._pct < 0" :stroke-width="5" :show-text="false" style="width: 100%" />
                    <span v-if="row._step" class="step-text">{{ row._step }}</span>
                  </template>
                  <span v-if="row.errorSummary" class="err-text">{{ row.errorSummary }}</span>
                </div>
              </template>
              <template #col-successCount="{ row }">
                <template v-if="row.status === 'success' || row.status === 'partial_success'">
                  <span class="count-ok">{{ row.successCount?.toLocaleString() }} 行</span>
                  <span v-if="row.failCount > 0" class="count-err"> · {{ row.failCount }} 跳过</span>
                </template>
                <span v-else-if="row.status === 'running'">—</span>
                <span v-else class="count-dim">-</span>
              </template>
              <template #col-duration="{ row }">
                <span v-if="row.startedAt && row.finishedAt" class="dur-text">{{ duration(row.startedAt, row.finishedAt) }}</span>
                <span v-else-if="row.status === 'running' && row.startedAt" class="dur-text">{{ elapsed(row.startedAt) }}</span>
                <span v-else>-</span>
              </template>
              <template #col-actions="{ row }">
                <div class="action-btns">
                  <el-button v-if="row.status === 'running'" text type="danger" @click="handleCancel(row.id)">停止</el-button>
                  <template v-else>
                    <el-button text @click="showLog(row)">日志</el-button>
                    <el-button v-if="row.status === 'failed' || row.status === 'cancelled'" text type="warning" @click="handleRetry(row.id)">重试</el-button>
                  </template>
                </div>
              </template>
            </Table>
          </template>
        </Crud>
        <div v-if="batches.length === 0" class="empty">暂无执行记录，点击「立即执行」开始</div>
      </el-tab-pane>
    </el-tabs>

    <!-- 日志弹窗 -->
    <el-dialog v-model="logDialog" title="同步详情" width="680px" destroy-on-close>
      <div class="log-detail" v-if="logBatch">
        <!-- 同步摘要 -->
        <div class="log-summary-grid">
          <div class="log-sum-item">
            <span class="log-sum-label">状态</span>
            <el-tag :type="batchType[logBatch.status]" effect="plain" size="small">{{ batchLabel[logBatch.status] ?? logBatch.status }}</el-tag>
          </div>
          <div class="log-sum-item">
            <span class="log-sum-label">触发方式</span>
            <span class="log-sum-val">{{ triggerLabel[logBatch.triggerType] ?? logBatch.triggerType }}</span>
          </div>
          <div class="log-sum-item">
            <span class="log-sum-label">耗时</span>
            <span class="log-sum-val" v-if="logBatch.startedAt && logBatch.finishedAt">{{ duration(logBatch.startedAt, logBatch.finishedAt) }}</span>
            <span class="log-sum-val" v-else>-</span>
          </div>
          <div class="log-sum-item">
            <span class="log-sum-label">拉取行数</span>
            <span class="log-sum-val">{{ logBatch.recordCount?.toLocaleString() ?? 0 }}</span>
          </div>
          <div class="log-sum-item">
            <span class="log-sum-label">写入行数</span>
            <span class="log-sum-val log-ok-val">{{ logBatch.successCount?.toLocaleString() ?? 0 }}</span>
          </div>
          <div class="log-sum-item">
            <span class="log-sum-label">拒绝行数</span>
            <span class="log-sum-val" :class="{ 'log-err-val': (logBatch.failCount ?? 0) > 0 }">{{ logBatch.failCount?.toLocaleString() ?? 0 }}</span>
          </div>
        </div>

        <!-- 时间范围 -->
        <div class="log-time-row" v-if="logBatch.startedAt">
          <span class="log-sum-label">执行时间</span>
          <span class="log-sum-val">{{ logBatch.startedAt?.slice(0, 19).replace('T', ' ') }} → {{ logBatch.finishedAt?.slice(0, 19).replace('T', ' ') || '进行中' }}</span>
        </div>

        <!-- 最后步骤 -->
        <div class="log-step-row" v-if="logBatch.progressStep">
          <span class="log-sum-label">最后步骤</span>
          <code class="log-step-code">{{ logBatch.progressStep }}</code>
        </div>

        <!-- 错误摘要 -->
        <el-alert
          v-if="logBatch.errorSummary"
          :title="logBatch.errorSummary"
          type="error"
          :closable="false"
          show-icon
          style="margin-top: 12px"
        />

        <!-- 错误清单 -->
        <el-table v-if="errorList.length > 0" :data="errorList" stripe style="margin-top: 12px">
          <el-table-column prop="errorType" label="类型" width="100" />
          <el-table-column prop="errorMessage" label="错误信息" min-width="250" />
          <el-table-column label="位置" width="100">
            <template #default="{ row: e }">{{ e.fieldName || (e.rowNumber ? '行 ' + e.rowNumber : '-') }}</template>
          </el-table-column>
          <el-table-column prop="createdAt" label="时间" width="160">
            <template #default="{ row: e }">{{ e.createdAt?.slice(0, 19).replace('T', ' ') }}</template>
          </el-table-column>
        </el-table>
      </div>
    </el-dialog>
  </div>
</template>

<script setup lang="ts">
import { computed, onMounted, onUnmounted, reactive, ref } from 'vue'
import { useRoute } from 'vue-router'
import { Edit, VideoPlay } from '@element-plus/icons-vue'
import { ElMessage } from 'element-plus'
import { ingestionService, type IngestionBatch, type ImportError, type IngestionTask } from '@/api'
import Index from '@/components/page-header/index.vue'
import { Crud, Table } from '@/components/crud'
import type { ColumnSchema } from '@/components/crud'

const route = useRoute()
const taskId = route.params.id as string
const task = ref<IngestionTask | null>(null)
const batches = ref<(IngestionBatch & { _pct?: number; _step?: string })[]>([])
const activeTab = ref('batches')
const executing = ref(false)
const logDialog = ref(false)
const isEditing = ref(route.query.edit === '1')
const editForm = reactive({ name: '', scheduleType: 'manual', cronExpression: '', description: '' })
const saving = ref(false)
const logBatch = ref<IngestionBatch | null>(null)
const errorList = ref<ImportError[]>([])
let _esList: EventSource[] = []
let _tickTimer: ReturnType<typeof setInterval> | null = null
let _pollTimer: ReturnType<typeof setInterval> | null = null

function startTick() {
  if (_tickTimer) return
  _tickTimer = setInterval(() => {
    // Force re-render so elapsed() timer updates every second
    batches.value = [...batches.value]
  }, 1000)
}
function stopTick() {
  if (_tickTimer) { clearInterval(_tickTimer); _tickTimer = null }
}

// Re-fetch batches periodically while any are still running.
// The engine creates one batch per interface for a multi-interface task, but the
// SSE progress stream is only opened for the first batch. Secondary batches (e.g.
// OEE) have no SSE stream of their own, so without this poll their status would
// stay "running" forever even after they finished on the backend.
async function pollRunning() {
  try {
    const b = await ingestionService.getBatches(taskId, { pageSize: 50 })
    batches.value = b.items
    const hasRunning = b.items.some((x: any) => x.status === 'running' || x.status === 'pending')
    if (!hasRunning) stopPolling()
  } catch { /* ignore transient poll errors */ }
}
function startPolling() {
  if (_pollTimer) return
  _pollTimer = setInterval(pollRunning, 3000)
}
function stopPolling() {
  if (_pollTimer) { clearInterval(_pollTimer); _pollTimer = null }
}

const batchLabel: Record<string, string> = { pending: '等待中', running: '运行中', success: '成功', partial_success: '部分成功', failed: '失败', cancelled: '已取消' }
const batchType: Record<string, '' | 'success' | 'warning' | 'danger' | 'info'> = { pending: 'info', running: '', success: 'success', partial_success: 'warning', failed: 'danger', cancelled: 'info' }
const triggerLabel: Record<string, string> = { manual: '手动', scheduled: '定时', retry: '重试', backfill: '全量回溯', quick_fill: '快补' }

const summary = computed(() => [
  { label: '调度', value: task.value?.scheduleType === 'cron' ? `定时 ${task.value?.cronExpression}` : task.value?.scheduleType ?? '-' },
  { label: '最近同步', value: task.value?.lastSyncAt?.slice(0, 16) ?? '未同步过' },
  { label: '上次结果', value: task.value?.lastSyncStatus || '-' },
])
const batchesPagination = reactive({ page: 1, pageSize: 20, total: 0, onPageChange() {}, onSizeChange() {} })

const batchesColumns: ColumnSchema[] = [
  { type: 'custom', prop: 'createdAt', label: '时间', width: 170 },
  { type: 'custom', prop: 'triggerType', label: '触发', width: 90 },
  { type: 'custom', prop: 'status', label: '状态 / 进度', width: 200 },
  { type: 'custom', prop: 'successCount', label: '数据量', width: 160 },
  { type: 'custom', prop: 'duration', label: '耗时', width: 80 },
  { type: 'custom', prop: 'actions', label: '操作', width: 160 },
]

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

async function load() {
  task.value = await ingestionService.get(taskId)
  const b = await ingestionService.getBatches(taskId, { pageSize: 50 })
  batches.value = b.items
  // Start/stop tick + polling timers based on whether any batch is running
  const hasRunning = b.items.some((x: any) => x.status === 'running' || x.status === 'pending')
  if (hasRunning) { startTick(); startPolling() }
  else { stopTick(); stopPolling() }
}

async function handleExecute() {
  executing.value = true
  try {
    const { batchId } = await ingestionService.execute(taskId)
    ElMessage.success('已提交')
    const placeholder: any = {
      id: batchId, triggerType: 'manual', status: 'pending',
      recordCount: 0, successCount: 0, failCount: 0,
      createdAt: new Date().toISOString(),
      _pct: -1, _step: '等待 Worker...',
    }
    batches.value.unshift(placeholder)
    startTick()
    const es = ingestionService.streamProgress(batchId,
      (d) => {
        const b = batches.value.find(x => x.id === batchId)
        if (b) {
          b._pct = d.pct
          b._step = d.step
          if (d.status === 'running') {
            b.status = 'running'
            if (d.startedAt) (b as any).startedAt = d.startedAt
          } else if (d.status !== 'pending') {
            b.status = d.status === 'success' ? 'success' : d.status === 'cancelled' ? 'cancelled' : 'failed'
          }
          if (d.recordCount !== undefined) (b as any).recordCount = d.recordCount
          if (d.successCount !== undefined) (b as any).successCount = d.successCount
          if (d.failCount !== undefined) (b as any).failCount = d.failCount
        }
      },
      () => { stopTick(); load() },
    )
    _esList.push(es)
  } catch { /* */ } finally { executing.value = false }
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

function toggleEdit() {
  isEditing.value = true
  activeTab.value = 'config'
  if (task.value) {
    editForm.name = task.value.name
    editForm.scheduleType = task.value.scheduleType
    editForm.cronExpression = task.value.cronExpression || ''
    editForm.description = task.value.description || ''
  }
}

function handleCancelEdit() {
  isEditing.value = false
}

async function handleSave() {
  if (!task.value) return
  saving.value = true
  try {
    const data: Record<string, unknown> = {}
    if (editForm.name !== task.value.name) data.name = editForm.name
    if (editForm.scheduleType !== task.value.scheduleType) {
      data.scheduleType = editForm.scheduleType
      data.cronExpression = editForm.scheduleType === 'cron' ? editForm.cronExpression || undefined : undefined
    } else if (editForm.scheduleType === 'cron' && editForm.cronExpression !== (task.value.cronExpression || '')) {
      data.cronExpression = editForm.cronExpression || undefined
    }
    if (editForm.description !== (task.value.description || '')) data.description = editForm.description || undefined

    if (Object.keys(data).length === 0) {
      ElMessage.info('无变更')
      isEditing.value = false
      return
    }

    await ingestionService.update(taskId, data)
    ElMessage.success('已更新')
    isEditing.value = false
    await load()
  } catch { /* handled */ } finally { saving.value = false }
}

onMounted(load)
onUnmounted(() => { _esList.forEach(es => es.close()); stopTick(); stopPolling() })
</script>

<style lang="scss" scoped>
.page { }
.summary-row { display: grid; grid-template-columns: repeat(3, 1fr); gap: 12px; margin-bottom: 16px; }
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
.log-summary-grid {
  display: grid; grid-template-columns: repeat(3, 1fr); gap: 12px;
  padding: 12px 0; border-bottom: 1px solid $color-border-light;
}
.log-sum-item { display: flex; flex-direction: column; gap: 4px; }
.log-sum-label { font-size: 12px; color: $color-text-placeholder; }
.log-sum-val { font-size: 14px; font-weight: $font-weight-semibold; color: $color-text-primary; }
.log-ok-val { color: $color-success; }
.log-err-val { color: $color-danger; }
.log-time-row, .log-step-row {
  display: flex; align-items: flex-start; gap: 8px;
  padding: 8px 0; font-size: 13px;
}
.log-step-code {
  font-size: 12px; color: $color-primary;
  background: rgba(0,0,0,0.04); padding: 2px 8px; border-radius: 4px;
  word-break: break-all; flex: 1;
}
</style>