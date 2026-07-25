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
      <el-tab-pane name="config">
        <template #label>
          <el-badge :value="schemaChangeCount" :hidden="schemaChangeCount === 0" :max="99">
            <span>当前配置</span>
          </el-badge>
        </template>
        <template v-if="!isEditing">
          <el-descriptions :column="2" border style="max-width: 600px">
            <el-descriptions-item label="名称">{{ task.name }}</el-descriptions-item>
            <el-descriptions-item label="编码">{{ task.code }}</el-descriptions-item>
            <el-descriptions-item label="调度">{{ task.scheduleType === 'cron' ? `定时 (${task.cronExpression})` : task.scheduleType }}</el-descriptions-item>
            <el-descriptions-item label="最近同步">{{ fmtDateTime(task.lastSyncAt) || '未同步过' }}</el-descriptions-item>
            <el-descriptions-item label="上次结果">{{ task.lastSyncStatus || '-' }}</el-descriptions-item>
            <el-descriptions-item label="创建时间">{{ fmtDateTime(task.createdAt) }}</el-descriptions-item>
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

        <!-- F1.2 — Schema 变更审计 -->
        <el-divider />
        <el-collapse>
          <el-collapse-item name="schema">
            <template #title>
              <span>Schema 变更审计</span>
              <el-tag v-if="schemaChangeCount > 0" type="warning" size="small" style="margin-left: 8px">
                {{ schemaChangeCount }}
              </el-tag>
            </template>
            <div v-loading="schemaChangeLoading">
              <el-table :data="schemaChanges" empty-text="暂无 Schema 变更" style="width: 100%">
                <el-table-column prop="tableName" label="数据表" min-width="180" />
                <el-table-column label="变更类型" width="120">
                  <template #default="{ row }">
                    <el-tag :type="schemaChangeTagType(row.changeType)" size="small">
                      {{ SCHEMA_CHANGE_LABELS[row.changeType] ?? row.changeType }}
                    </el-tag>
                  </template>
                </el-table-column>
                <el-table-column prop="columnName" label="列名" min-width="160" />
                <el-table-column label="检测时间" width="180">
                  <template #default="{ row }">{{ fmtDateTime(row.detectedAt) }}</template>
                </el-table-column>
              </el-table>
            </div>
          </el-collapse-item>
        </el-collapse>
      </el-tab-pane>

      <el-tab-pane :label="`执行记录 (${batches.length})`" name="batches">
        <Crud :pagination="batchesPagination">
          <template #table>
            <Table :columns="batchesColumns" :data="batches">
              <template #col-createdAt="{ row }">{{ fmtDateTime(row.createdAt) }}</template>
              <template #col-sourceSignature="{ row }">
                <span
                  v-if="(row.sourceSignature || '').startsWith('(')"
                  class="iface-tag iface-tag-agg"
                >{{ row.sourceSignature }}</span>
                <span v-else class="iface-tag">{{ ifaceLabel(row) }}</span>
              </template>
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
                  <span class="count-ok">{{ row.successCount?.toLocaleString() }} 行写入</span>
                  <span v-if="row.skipCount > 0" class="count-warn"> · {{ row.skipCount }} 跳过</span>
                  <span v-if="row.failCount > 0" class="count-err"> · {{ row.failCount }} 拒绝</span>
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

      <!-- F1.3 — 数据对账 -->
      <el-tab-pane name="recon">
        <template #label>
          <span>数据对账</span>
          <el-badge v-if="reconSummary.toRepair > 0" :value="reconSummary.toRepair" type="danger" :max="99" style="margin-left: 4px" />
        </template>
        <div v-loading="reconLoading">
          <!-- 概览卡片 -->
          <div class="recon-cards">
            <div class="recon-card">
              <span class="recon-card-label">最近对账</span>
              <span class="recon-card-val">{{ reconSummary.lastCheck ? fmtDateTime(reconSummary.lastCheck) : '—' }}</span>
            </div>
            <div class="recon-card">
              <span class="recon-card-label">数据一致</span>
              <span class="recon-card-val" style="color: var(--el-color-success)">{{ reconSummary.consistent }}</span>
            </div>
            <div class="recon-card">
              <span class="recon-card-label">存在差异</span>
              <span class="recon-card-val" style="color: #ca8a04">{{ reconSummary.diff }}</span>
            </div>
            <div class="recon-card">
              <span class="recon-card-label">待修复</span>
              <span class="recon-card-val" :class="{ 'recon-card-err': reconSummary.toRepair > 0 }">{{ reconSummary.toRepair }}</span>
            </div>
          </div>

          <!-- 对账记录表格 -->
          <el-table :data="reconciliations" empty-text="暂无对账记录" style="width: 100%; margin-top: 16px">
            <el-table-column prop="interfaceName" label="接口" min-width="170" />
            <el-table-column label="级别" width="90">
              <template #default="{ row }">
                <el-tag :type="row.checkLevel === 'L1' ? 'info' : row.checkLevel === 'L2' ? 'warning' : 'danger'" size="small" effect="plain">{{ CHECK_LEVEL_LABELS[row.checkLevel] ?? row.checkLevel }}</el-tag>
              </template>
            </el-table-column>
            <el-table-column label="模式" width="80">
              <template #default="{ row }">
                <el-tag :type="row.syncMode === 'incremental' ? 'warning' : 'success'" size="small" effect="plain">
                  {{ SYNC_MODE_LABELS[row.syncMode] ?? row.syncMode ?? '全量' }}
                </el-tag>
              </template>
            </el-table-column>
            <el-table-column prop="apiTotal" label="API 总量" width="100" align="right" />
            <el-table-column label="对比基准" width="110" align="right">
              <template #default="{ row }">
                <el-tooltip
                  :content="row.syncMode === 'incremental'
                    ? '增量模式：与「本批拉取行数」对比（窗口内是否拉全）'
                    : '全量模式：与「整表行数」对比'"
                  placement="top"
                >
                  <span>{{ row.syncMode === 'incremental' ? (row.pulledCount ?? 0).toLocaleString() : (row.dbCount ?? 0).toLocaleString() }}</span>
                </el-tooltip>
              </template>
            </el-table-column>
            <el-table-column label="差异" width="90" align="right">
              <template #default="{ row }">
                <span :class="{ 'diff-ok': row.status === 'pass', 'diff-warn': row.status === 'warning', 'diff-err': row.status === 'failed' }">
                  {{ (row.diffCount ?? 0) > 0 ? `+${row.diffCount}` : '0' }}
                </span>
              </template>
            </el-table-column>
            <el-table-column label="差异率" width="100" align="right">
              <template #default="{ row }">
                <span :class="{ 'diff-ok': row.status === 'pass', 'diff-warn': row.status === 'warning', 'diff-err': row.status === 'failed' }">
                  {{ ((row.diffRatio ?? 0) * 100).toFixed(2) }}%
                </span>
              </template>
            </el-table-column>
            <el-table-column label="状态" width="100">
              <template #default="{ row }">
                <el-tag :type="row.status === 'pass' ? 'success' : row.status === 'warning' ? 'warning' : row.status === 'failed' ? 'danger' : 'info'" size="small">{{ RECON_STATUS_LABELS[row.status] ?? row.status }}</el-tag>
              </template>
            </el-table-column>
            <el-table-column prop="checkedAt" label="检查时间" width="180">
              <template #default="{ row }">{{ fmtDateTime(row.checkedAt) }}</template>
            </el-table-column>
            <el-table-column label="操作" width="200" align="center">
              <template #default="{ row }">
                <div class="action-btns">
                  <el-button text @click="showReconDetail(row)">查看详情</el-button>
                  <el-button v-if="row.status === 'warning' || row.status === 'failed'" text type="warning" @click="handleTriggerRecon('L2')">触发深度对账</el-button>
                  <el-button v-if="row.status === 'failed'" text type="danger" @click="handleRepair(row.id)">修复</el-button>
                </div>
              </template>
            </el-table-column>
          </el-table>
        </div>

        <!-- 对账详情弹窗 -->
        <el-dialog v-model="reconDialog" title="对账详情" width="800px" destroy-on-close>
          <div v-loading="reconDetailLoading">
            <template v-if="reconDetail">
              <div class="recon-summary-grid">
                <div class="recon-sum-item">
                  <span class="recon-label">API 总量</span>
                  <span class="recon-val">{{ reconDetail.apiTotal?.toLocaleString() }}</span>
                </div>
                <div class="recon-sum-item">
                  <span class="recon-label">
                    对比基准
                    <el-tag
                      :type="reconDetail.syncMode === 'incremental' ? 'warning' : 'success'"
                      size="small" effect="plain" style="margin-left: 4px"
                    >{{ SYNC_MODE_LABELS[reconDetail.syncMode ?? 'full'] ?? '全量' }}</el-tag>
                  </span>
                  <span class="recon-val">
                    {{ (reconDetail.syncMode === 'incremental' ? reconDetail.pulledCount : reconDetail.dbCount)?.toLocaleString() }}
                    <span class="recon-sub">{{ reconDetail.syncMode === 'incremental' ? '（本批拉取）' : '（整表行数）' }}</span>
                  </span>
                </div>
                <div class="recon-sum-item">
                  <span class="recon-label">差异行数</span>
                  <span class="recon-val" :class="{ 'diff-err': (reconDetail.diffCount ?? 0) > 0 }">{{ reconDetail.diffCount?.toLocaleString() }}</span>
                </div>
                <div class="recon-sum-item">
                  <span class="recon-label">差异率</span>
                  <span class="recon-val" :class="{ 'diff-err': reconDetail.status === 'failed', 'diff-warn': reconDetail.status === 'warning' }">
                    {{ ((reconDetail.diffRatio ?? 0) * 100).toFixed(2) }}%
                  </span>
                </div>
              </div>
              <el-divider>分段明细（L2 深度对账）</el-divider>
              <el-table v-if="reconDetail.detail && reconDetail.detail.length" :data="reconDetail.detail" stripe style="margin-top: 8px">
                <el-table-column prop="dateRange" label="日期段" min-width="200" />
                <el-table-column prop="apiCount" label="API 行数" width="100" align="right" />
                <el-table-column prop="dbCount" label="DB 行数" width="100" align="right" />
                <el-table-column label="差异" width="80" align="right">
                  <template #default="{ row }">
                    <span :class="{ 'diff-err': row.diff !== 0 }">{{ row.diff > 0 ? `+${row.diff}` : row.diff }}</span>
                  </template>
                </el-table-column>
                <el-table-column label="状态" width="100">
                  <template #default="{ row }">
                    <el-tag :type="row.diff === 0 ? 'success' : 'danger'" size="small">{{ row.diff === 0 ? '一致' : '需修复' }}</el-tag>
                  </template>
                </el-table-column>
              </el-table>
              <el-empty v-else description="暂无分段明细（L2 深度对账尚未实现）" :image-size="80" />
            </template>
          </div>
        </el-dialog>
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
          <div class="log-sum-item" v-if="logBatch.sourceSignature">
            <span class="log-sum-label">接口</span>
            <span class="log-sum-val"><span class="iface-tag">{{ logBatch.sourceSignature }}</span></span>
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
            <span class="log-sum-label">写入行数<small class="log-sub">（实际变更）</small></span>
            <span class="log-sum-val log-ok-val">{{ logBatch.successCount?.toLocaleString() ?? 0 }}</span>
          </div>
          <div class="log-sum-item">
            <span class="log-sum-label">跳过行数<small class="log-sub">（已存在未变）</small></span>
            <span class="log-sum-val" :class="{ 'log-warn-val': (logBatch.skipCount ?? 0) > 0 }">{{ logBatch.skipCount?.toLocaleString() ?? 0 }}</span>
          </div>
          <div class="log-sum-item">
            <span class="log-sum-label">拒绝行数</span>
            <span class="log-sum-val" :class="{ 'log-err-val': (logBatch.failCount ?? 0) > 0 }">{{ logBatch.failCount?.toLocaleString() ?? 0 }}</span>
          </div>
        </div>

        <!-- 时间范围 -->
        <div class="log-time-row" v-if="logBatch.startedAt">
          <span class="log-sum-label">执行时间</span>
          <span class="log-sum-val">{{ fmtDateTime(logBatch.startedAt) }} → {{ fmtDateTime(logBatch.finishedAt) || '进行中' }}</span>
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
            <template #default="{ row: e }">{{ fmtDateTime(e.createdAt) }}</template>
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
import { ingestionService, type IngestionBatch, type ImportError, type IngestionTask, type SchemaChange, type Reconciliation } from '@/api'
import { SCHEMA_CHANGE_LABELS, RECON_STATUS_LABELS, CHECK_LEVEL_LABELS, SYNC_MODE_LABELS } from '@/constants/ingestion'
import { fmtDateTime } from '@/utils/datetime'
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
// F1.2 — Schema 变更审计
const schemaChanges = ref<SchemaChange[]>([])
const schemaChangeLoading = ref(false)
const schemaChangeCount = computed(() => schemaChanges.value.length)

// F1.3 — 数据对账
const reconciliations = ref<Reconciliation[]>([])
const reconLoading = ref(false)
const reconDialog = ref(false)
const reconDetail = ref<Reconciliation | null>(null)
const reconDetailLoading = ref(false)

// 概览卡片：最近对账时间 / 数据一致 / 存在差异 / 待修复
const reconSummary = computed(() => {
  const list = reconciliations.value
  const lastCheck = list.length
    ? list.reduce((m, r) => (r.checkedAt > m ? r.checkedAt : m), list[0].checkedAt)
    : null
  const consistent = list.filter(r => r.status === 'pass' || r.status === 'repaired').length
  const diff = list.filter(r => r.status === 'warning').length
  const toRepair = list.filter(r => r.status === 'failed').length
  return { lastCheck, consistent, diff, toRepair }
})
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
  { label: '最近同步', value: fmtDateTime(task.value?.lastSyncAt, false) || '未同步过' },
  { label: '上次结果', value: task.value?.lastSyncStatus || '-' },
])
const batchesPagination = reactive({ page: 1, pageSize: 20, total: 0, onPageChange() {}, onSizeChange() {} })

const batchesColumns: ColumnSchema[] = [
  { type: 'custom', prop: 'createdAt', label: '时间', width: 170 },
  { type: 'custom', prop: 'sourceSignature', label: '接口', width: 130 },
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
function ifaceLabel(row: any): string {
  if (row.sourceSignature) return row.sourceSignature
  const ps = row.progressStep || ''
  const m = ps.match(/([A-Za-z][A-Za-z0-9_]*)/)
  return m ? m[1] : '—'
}

// F1.2 — Schema 变更审计：后端接口（B1.4）未实现时静默失败，不阻塞页面
function schemaChangeTagType(t: string): '' | 'success' | 'warning' | 'danger' | 'info' {
  if (t === 'added') return 'warning'
  if (t === 'removed') return 'danger'
  if (t === 'type_changed') return 'info'
  return 'info'
}

async function loadSchemaChanges() {
  schemaChangeLoading.value = true
  try {
    const res = await ingestionService.getSchemaChanges(taskId)
    const list = res && Array.isArray((res as any).items)
      ? (res as any).items
      : Array.isArray(res) ? res : []
    schemaChanges.value = list as SchemaChange[]
  } catch (e) {
    console.error('加载 Schema 变更失败:', e)
    schemaChanges.value = []
  } finally {
    schemaChangeLoading.value = false
  }
}

// F1.3 — 数据对账：后端接口（B1.4）未实现时静默失败，不阻塞页面
async function loadReconciliations() {
  reconLoading.value = true
  try {
    const res = await ingestionService.getReconciliations(taskId, { pageSize: 50 })
    const list = res && Array.isArray((res as any).items)
      ? (res as any).items
      : Array.isArray(res) ? res : []
    reconciliations.value = list as Reconciliation[]
  } catch (e) {
    console.error('加载对账记录失败:', e)
    reconciliations.value = []
  } finally {
    reconLoading.value = false
  }
}

async function showReconDetail(row: Reconciliation) {
  reconDetailLoading.value = true
  reconDialog.value = true
  try {
    reconDetail.value = await ingestionService.getReconciliation(row.id)
  } catch (e) {
    console.error('加载对账详情失败:', e)
    reconDetail.value = null
  } finally {
    reconDetailLoading.value = false
  }
}

async function handleTriggerRecon(level: 'L1' | 'L2' | 'L3') {
  try {
    await ingestionService.triggerReconciliation(taskId, level)
    ElMessage.success(`${level} 对账已触发`)
    await loadReconciliations()
  } catch { /* handled */ }
}

async function handleRepair(reconId: string) {
  try {
    await ingestionService.repairReconciliation(reconId)
    ElMessage.success('修复已提交')
    await loadReconciliations()
  } catch { /* handled */ }
}

async function load() {
  task.value = await ingestionService.get(taskId)
  const b = await ingestionService.getBatches(taskId, { pageSize: 50 })
  batches.value = b.items
  // Start/stop tick + polling timers based on whether any batch is running
  const hasRunning = b.items.some((x: any) => x.status === 'running' || x.status === 'pending')
  if (hasRunning) { startTick(); startPolling() }
  else { stopTick(); stopPolling() }
  // F1.2 — Schema 变更审计列表
  await loadSchemaChanges()
  // F1.3 — 数据对账记录
  await loadReconciliations()
}

async function handleExecute() {
  executing.value = true
  try {
    const { batchId } = await ingestionService.execute(taskId)
    ElMessage.success('已提交')
    const placeholder: any = {
      id: batchId, triggerType: 'manual', status: 'pending',
      recordCount: 0, successCount: 0, failCount: 0,
      sourceSignature: undefined,
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
          if (d.skipCount !== undefined) (b as any).skipCount = d.skipCount
          if (d.sourceSignature !== undefined && d.sourceSignature) (b as any).sourceSignature = d.sourceSignature
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
.count-warn { color: #ca8a04; font-size: $font-size-xs; }
.count-dim { color: $color-text-placeholder; }
.dur-text { color: $color-text-secondary; font-size: $font-size-sm; }
.trigger-text { color: $color-text-secondary; font-size: $font-size-sm; }
.iface-tag { display: inline-block; padding: 1px 8px; border-radius: 4px; background: rgba(0,0,0,0.04); color: $color-text-secondary; font-size: 11px; font-family: monospace; }
.iface-tag-agg { background: rgba(64,158,255,0.12); color: #2563eb; font-weight: 600; }
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
.log-warn-val { color: #ca8a04; }
.log-sub { font-size: 11px; color: $color-text-placeholder; margin-left: 2px; font-weight: normal; }
.log-time-row, .log-step-row {
  display: flex; align-items: flex-start; gap: 8px;
  padding: 8px 0; font-size: 13px;
}
.log-step-code {
  font-size: 12px; color: $color-primary;
  background: rgba(0,0,0,0.04); padding: 2px 8px; border-radius: 4px;
  word-break: break-all; flex: 1;
}
/* F1.3 — 数据对账 */
.recon-cards {
  display: grid; grid-template-columns: repeat(4, 1fr); gap: 12px; margin-bottom: 4px;
}
.recon-card { display: flex; flex-direction: column; gap: 6px; padding: 14px 16px; border: 1px solid $color-border-light; border-radius: 6px; }
.recon-card-label { font-size: $font-size-xs; color: $color-text-placeholder; }
.recon-card-val { font-size: $font-size-lg; font-weight: $font-weight-semibold; color: $color-text-primary; }
.recon-card-err { color: $color-danger; }
.recon-summary-grid {
  display: grid; grid-template-columns: repeat(4, 1fr); gap: 12px;
  padding: 12px 0; border-bottom: 1px solid $color-border-light;
}
.recon-sum-item { display: flex; flex-direction: column; gap: 4px; }
.recon-label { font-size: 12px; color: $color-text-placeholder; }
.recon-val { font-size: 14px; font-weight: $font-weight-semibold; color: $color-text-primary; }
.recon-sub { font-size: 12px; font-weight: $font-weight-normal; color: $color-text-placeholder; }
.diff-ok { color: $color-success; font-weight: $font-weight-semibold; }
.diff-warn { color: #ca8a04; font-weight: $font-weight-semibold; }
.diff-err { color: $color-danger; font-weight: $font-weight-semibold; }
</style>