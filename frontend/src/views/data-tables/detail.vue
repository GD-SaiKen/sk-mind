<template>
  <div class="page-layout detail-page">
    <PageHeader
      :title="table?.displayName || table?.tableName || '数据表详情'"
      :breadcrumb="[
        { label: '首页', to: '/' },
        { label: '数据表', to: '/tables' },
        { label: table?.tableName || '...' },
      ]"
    >
      <template #tags>
        <el-tag
          v-if="table"
          effect="plain"
          :type="layerTagType(table.layer)"
        >{{ table.layer }}</el-tag>
        <el-tag
          v-if="table"
          :type="table.agentEnabled ? 'success' : 'info'"
          effect="plain"
        >
          {{ table.agentEnabled ? 'Agent 已开放' : 'Agent 未开放' }}
        </el-tag>
      </template>
      <template #actions>
        <el-button plain @click="router.push('/tables')">返回列表</el-button>
      </template>
    </PageHeader>

    <div class="summary-row">
      <div
        v-for="s in summary"
        :key="s.label"
        class="sum-item"
      >
        <div class="sum-label">{{ s.label }}</div>
        <div class="sum-value">{{ s.value }}</div>
      </div>
    </div>

    <el-tabs v-model="activeTab">
      <el-tab-pane
        label="样例数据"
        name="sample"
      >
        <el-card shadow="never">
          <h3>样例数据（前 10 行）</h3>
          <el-table
            v-if="sampleData.length > 0"
            :data="sampleData"
            stripe
            max-height="400"
          >
            <el-table-column
              v-for="col in sampleColumns"
              :key="col"
              :prop="col"
              :label="col"
              min-width="120"
              show-overflow-tooltip
            />
          </el-table>
          <el-empty
            v-else
            description="暂无样例数据"
            :image-size="60"
          />
        </el-card>
      </el-tab-pane>

      <el-tab-pane
        label="字段列表"
        name="fields"
      >
        <Crud :pagination="fieldsPagination">
          <template #table>
            <!-- T4: 批量操作工具栏 -->
            <div v-if="selectedFields.length > 0" class="batch-toolbar">
              <span class="batch-hint">已选 {{ selectedFields.length }} 个字段</span>
              <el-button size="small" type="warning" plain @click="batchMarkSensitive">
                批量标记为敏感
              </el-button>
              <el-button size="small" plain @click="batchMarkInternal">
                批量标记为内部
              </el-button>
              <el-button size="small" plain @click="clearSelection">取消选择</el-button>
            </div>
            <Table
              ref="fieldTableRef"
              :columns="fieldColumns"
              :data="pagedFields"
              row-key="id"
              @selection-change="onFieldSelectionChange"
            >
              <template #col-nullRate="{ row }">
                <span :style="{ color: row.nullRate > 0.1 ? '#dc2626' : row.nullRate > 0.01 ? '#ca8a04' : '' }">
                  {{ (row.nullRate * 100).toFixed(1) }}%
                </span>
              </template>
              <template #col-isPk="{ row }">
                <el-tag
                  v-if="row.isPk"
                  type="warning"
                  effect="plain"
                  size="small"
                >主键</el-tag>
                <span v-else>-</span>
              </template>
              <template #col-sensitive="{ row }">
                <el-tag
                  v-if="row.sensitive"
                  type="danger"
                  effect="plain"
                  size="small"
                >{{ row.sensitiveType }}</el-tag>
                <span v-else>-</span>
              </template>
              <template #col-agentEnabled="{ row }">
                <el-tag
                  :type="row.agentEnabled ? 'success' : 'info'"
                  effect="plain"
                  size="small"
                >
                  {{ row.agentEnabled ? '可用' : '禁用' }}
                </el-tag>
              </template>
              <template #col-mapped="{ row }">
                <el-tag
                  v-if="row.mappedField"
                  type="success"
                  effect="plain"
                  size="small"
                >{{ row.mappedField }}</el-tag>
                <span v-else>未映射</span>
              </template>
            </Table>
          </template>
          <template #extra>
            <el-button plain size="small" @click="computeNullRates">
              计算空值率
            </el-button>
          </template>
        </Crud>

        <!-- T4: 字段编辑对话框 -->
        <el-dialog
          v-model="editDialogVisible"
          title="编辑字段"
          width="440px"
          :close-on-click-modal="false"
        >
          <el-form
            v-if="editingField"
            label-width="80px"
            label-position="left"
          >
            <el-form-item label="字段名">
              <span class="text-muted">{{ editingField.name }}</span>
            </el-form-item>
            <el-form-item label="显示名">
              <el-input
                v-model="editForm.displayName"
                placeholder="输入字段别名"
                maxlength="200"
                show-word-limit
              />
            </el-form-item>
            <el-form-item label="字段说明">
              <el-input
                v-model="editForm.description"
                type="textarea"
                :rows="3"
                placeholder="字段的业务含义和用途"
                maxlength="500"
                show-word-limit
              />
            </el-form-item>
            <el-form-item label="敏感级别">
              <el-select v-model="editForm.sensitivityLevel" style="width: 100%">
                <el-option label="公开（public）" value="public" />
                <el-option label="内部（internal）" value="internal" />
                <el-option label="敏感（sensitive）" value="sensitive" />
                <el-option label="高敏感（high_sensitive）" value="high_sensitive" />
              </el-select>
            </el-form-item>
          </el-form>
          <template #footer>
            <el-button @click="editDialogVisible = false">取消</el-button>
            <el-button type="primary" :loading="editSaving" @click="saveFieldEdit">保存</el-button>
          </template>
        </el-dialog>
      </el-tab-pane>

      <el-tab-pane
        label="来源和批次"
        name="source"
      >
        <el-card shadow="never">
          <h3>数据链路</h3>
          <div class="link-chain">
            <div class="chain-node">
              <div class="node-dot" />
              <div class="node-label">数据源</div>
              <div class="node-value">{{ table?.sourceName || '-' }}</div>
            </div>
            <div class="chain-arrow">&rarr;</div>
            <div class="chain-node">
              <div class="node-dot active" />
              <div class="node-label">接入任务</div>
              <div class="node-value">{{ table?.taskName || '-' }}</div>
            </div>
            <div class="chain-arrow">&rarr;</div>
            <div class="chain-node">
              <div class="node-dot" />
              <div class="node-label">数据表</div>
              <div class="node-value">{{ table?.tableName || '-' }}</div>
            </div>
          </div>
        </el-card>
      </el-tab-pane>

      <el-tab-pane
        label="质量结果"
        name="quality"
      >
        <el-card shadow="never">
          <h3>质量检查结果</h3>
          <el-empty
            v-if="qualityRecords.length === 0"
            description="暂无质量检查记录"
            :image-size="60"
          />
          <el-table
            v-else
            :data="qualityRecords"
            stripe
          >
            <el-table-column
              prop="rule"
              label="规则"
              min-width="160"
            />
            <el-table-column
              prop="time"
              label="执行时间"
              width="170"
            />
            <el-table-column
              label="结果"
              width="100"
            >
              <template #default="{ row }">
                <el-tag
                  :type="row.result === '通过' ? 'success' : 'warning'"
                  effect="plain"
                >{{ row.result }}</el-tag>
              </template>
            </el-table-column>
            <el-table-column
              prop="issues"
              label="问题数"
              width="80"
              align="center"
            />
          </el-table>
        </el-card>
      </el-tab-pane>

      <el-tab-pane
        label="权限"
        name="permission"
      >
        <el-card shadow="never">
          <h3>访问权限</h3>
          <el-descriptions
            :column="2"
            border
            style="max-width: 600px"
          >
            <el-descriptions-item label="访问级别">受控访问</el-descriptions-item>
            <el-descriptions-item label="Agent 可用">{{ table?.agentEnabled ? '已开放' : '未开放' }}</el-descriptions-item>
            <el-descriptions-item label="可访问角色">管理员, 销售部门</el-descriptions-item>
            <el-descriptions-item label="字段限制">2 个字段受限</el-descriptions-item>
          </el-descriptions>

          <!-- T6: Agent 可用性检查 -->
          <div style="margin-top: 20px">
            <el-button
              type="primary"
              :loading="agentCheckLoading"
              @click="checkAgent"
            >
              检查 Agent 可用性
            </el-button>
            <div v-if="agentCheckResult" style="margin-top: 12px">
              <el-alert
                :title="agentCheckResult.passed ? '检查通过 — 可以开放给 Agent' : '检查未通过'"
                :type="agentCheckResult.passed ? 'success' : 'error'"
                :closable="false"
              >
                <template v-if="!agentCheckResult.passed">
                  <ul style="margin: 4px 0; padding-left: 20px">
                    <li v-for="reason in agentCheckResult.reasons" :key="reason">{{ reason }}</li>
                  </ul>
                </template>
              </el-alert>
              <div style="margin-top: 8px; font-size: 13px; color: #6b7280">
                字段说明覆盖率：{{ (agentCheckResult.fieldDescriptionCoverage * 100).toFixed(0) }}%
                &nbsp;·&nbsp;
                未标记敏感字段：{{ agentCheckResult.unmarkedSensitiveCount }} 个
              </div>
            </div>
          </div>
        </el-card>
      </el-tab-pane>

      <el-tab-pane
        label="语义映射"
        name="semantic"
      >
        <el-card shadow="never">
          <h3>语义映射</h3>
          <el-empty
            v-if="semanticMappings.length === 0"
            description="暂无语义映射"
            :image-size="60"
          />
          <el-table
            v-else
            :data="semanticMappings"
            stripe
          >
            <el-table-column
              prop="field"
              label="字段"
              width="160"
            />
            <el-table-column
              prop="semantic"
              label="语义对象/属性"
              min-width="180"
            />
            <el-table-column
              prop="confidence"
              label="可信度"
              width="100"
              align="center"
            />
          </el-table>
        </el-card>
      </el-tab-pane>

      <el-tab-pane
        label="使用记录"
        name="usage"
      >
        <el-card shadow="never">
          <h3>最近使用记录</h3>
          <el-empty
            v-if="usageRecords.length === 0"
            description="暂无使用记录"
            :image-size="60"
          />
          <el-table
            v-else
            :data="usageRecords"
            stripe
          >
            <el-table-column
              prop="time"
              label="时间"
              width="170"
            />
            <el-table-column
              prop="user"
              label="用户"
              width="100"
            />
            <el-table-column
              prop="operation"
              label="操作"
              min-width="120"
            />
            <el-table-column
              prop="detail"
              label="详情"
              min-width="180"
            />
          </el-table>
        </el-card>
      </el-tab-pane>
    </el-tabs>
  </div>
</template>

<script setup lang="ts">
import type { ColumnSchema } from '@/components/crud'
import { computed, onMounted, reactive, ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { View, Edit } from '@element-plus/icons-vue'
import PageHeader from '@/components/page-header/index.vue'
import { Crud, Table } from '@/components/crud'
import { datasetService } from '@/api/services/dataset'
import { qualityService } from '@/api/services/quality'
import type { DatasetResponse, DatasetFieldResponse, QualityRun, AgentCheckResponse } from '@/api/types'

const route = useRoute()
const router = useRouter()
const id = route.params.id as string
const activeTab = ref('fields')
const loading = ref(false)

interface DataTableDetail {
  id: string
  tableName: string
  displayName: string
  layer: string
  sourceName: string
  taskName: string
  recordCount: number
  fieldCount: number
  qualityStatus: string
  agentEnabled: boolean
  updatedAt: string
}

interface FieldRow {
  id: string
  name: string
  displayName: string
  type: string
  nullRate: number
  sampleValue: string
  description: string
  sensitive: boolean
  sensitiveType: string
  sensitivityLevel: string
  isPk: boolean
  agentEnabled: boolean
  mappedField: string
}

function mapFieldToRow(f: DatasetFieldResponse): FieldRow {
  let sensitive = false
  let sensitiveType = ''
  if (f.sensitivityLevel && f.sensitivityLevel !== 'internal' && f.sensitivityLevel !== 'public') {
    sensitive = true
    sensitiveType = f.sensitivityLevel === 'sensitive' ? 'PII' : f.sensitivityLevel
  }
  return {
    id: f.id,
    name: f.fieldName,
    displayName: f.fieldAlias || f.fieldName,
    type: f.dataType + (f.fieldLength ? `(${f.fieldLength})` : ''),
    nullRate: f.nullRate ?? 0,              // T5: real null rate from API
    sampleValue: f.sampleValues || '-',
    description: f.description || '',
    sensitive,
    sensitiveType,
    sensitivityLevel: f.sensitivityLevel || 'internal',
    isPk: f.isPrimaryKey,                  // T1: real pk from API
    agentEnabled: true,
    mappedField: f.sourceColumn || '',
  }
}

interface QualityRecord {
  rule: string
  time: string
  result: string
  issues: number
}

function mapRunToQuality(r: QualityRun): QualityRecord {
  return {
    rule: r.ruleIds || '质量检查',
    time: r.createdAt,
    result: r.status === 'completed' ? '通过' : '执行中',
    issues: r.totalIssues,
  }
}

const table = ref<DataTableDetail>({
  id,
  tableName: '',
  displayName: '',
  layer: '',
  sourceName: '',
  taskName: '',
  recordCount: 0,
  fieldCount: 0,
  qualityStatus: 'pass',
  agentEnabled: false,
  updatedAt: '',
})

const summary = computed(() => [
  { label: '来源', value: table.value?.sourceName || '-' },
  { label: '记录数', value: (table.value?.recordCount ?? 0).toLocaleString() },
  { label: '字段数', value: table.value?.fieldCount ?? 0 },
  { label: '更新时间', value: table.value?.updatedAt || '-' },
])

function layerTagType(layer: string) {
  if (layer === 'serving' || layer === 'Serving') return 'success'
  if (layer === 'clean' || layer === 'Clean') return 'warning'
  return ''
}

function mapDatasetToDetail(ds: DatasetResponse): DataTableDetail {
  return {
    id: ds.id,
    tableName: ds.code,
    displayName: ds.name,
    layer: ds.dataLayer,
    sourceName: ds.dataSourceId || '-',
    taskName: ds.generatedByTaskId || '-',
    recordCount: ds.recordCount ?? 0,
    fieldCount: ds.fieldCount ?? 0,
    qualityStatus: 'pass',
    agentEnabled: ds.isAgentAccessible,
    updatedAt: ds.updatedAt,
  }
}

const sampleColumns = ref<string[]>([])
const sampleData = ref<Record<string, unknown>[]>([])

const fieldData = ref<FieldRow[]>([])
const fieldsPagination = reactive({
  page: 1,
  pageSize: 20,
  total: 0,
  onPageChange() {},
  onSizeChange() {},
})

const pagedFields = computed(() => fieldData.value.slice(
  (fieldsPagination.page - 1) * fieldsPagination.pageSize,
  fieldsPagination.page * fieldsPagination.pageSize,
))

const fieldColumns: ColumnSchema[] = [
  { type: 'selection', width: 50 },
  { type: 'text', prop: 'name', label: '字段名', width: 160, showOverflowTooltip: true },
  { type: 'text', prop: 'displayName', label: '显示名', width: 120 },
  { type: 'text', prop: 'type', label: '类型', width: 130 },
  { type: 'custom', prop: 'nullRate', label: '空值率', width: 90, align: 'center' },
  { type: 'text', prop: 'sampleValue', label: '样例值', minWidth: 130, showOverflowTooltip: true },
  { type: 'text', prop: 'description', label: '字段说明', minWidth: 150, formatter: (v: string) => v || '-' },
  { type: 'custom', prop: 'sensitive', label: '敏感', width: 90, align: 'center' },
  { type: 'custom', prop: 'isPk', label: '主键', width: 70, align: 'center' },
  { type: 'custom', prop: 'agentEnabled', label: 'Agent可用', width: 90, align: 'center' },
  { type: 'custom', prop: 'mapped', label: '已映射', width: 130 },
  {
    type: 'action', label: '操作', width: 80,
    buttons: [
      { label: '编辑', type: 'primary', onClick: (row) => openFieldEdit(row as FieldRow) },
    ],
  },
]

const qualityRecords = ref<QualityRecord[]>([])

// ── T4: 字段批量选择状态 ──
const selectedFields = ref<FieldRow[]>([])
const fieldTableRef = ref()

function onFieldSelectionChange(rows: FieldRow[]) {
  selectedFields.value = rows
}

function clearSelection() {
  selectedFields.value = []
  fieldTableRef.value?.clearSelection()
}

async function batchMarkSensitive() {
  if (!id || selectedFields.value.length === 0) return
  try {
    await datasetService.batchUpdateFields(id, {
      fieldIds: selectedFields.value.map(f => f.id),
      sensitivityLevel: 'sensitive',
    })
    await reloadFields()
    clearSelection()
  } catch { /* ignore */ }
}

async function batchMarkInternal() {
  if (!id || selectedFields.value.length === 0) return
  try {
    await datasetService.batchUpdateFields(id, {
      fieldIds: selectedFields.value.map(f => f.id),
      sensitivityLevel: 'internal',
    })
    await reloadFields()
    clearSelection()
  } catch { /* ignore */ }
}

// ── T4: 字段编辑对话框状态 ──
const editDialogVisible = ref(false)
const editingField = ref<FieldRow | null>(null)
const editSaving = ref(false)
const editForm = reactive({
  displayName: '',
  description: '',
  sensitivityLevel: 'internal',
})

function openFieldEdit(row: FieldRow) {
  editingField.value = row
  editForm.displayName = row.displayName
  editForm.description = row.description
  editForm.sensitivityLevel = row.sensitivityLevel
  editDialogVisible.value = true
}

async function saveFieldEdit() {
  if (!id || !editingField.value) return
  editSaving.value = true
  try {
    await datasetService.updateField(id, editingField.value.id, {
      fieldAlias: editForm.displayName || undefined,
      description: editForm.description || undefined,
      sensitivityLevel: editForm.sensitivityLevel,
    })
    editDialogVisible.value = false
    await reloadFields()
    clearSelection()
  } catch { /* ignore */ } finally {
    editSaving.value = false
  }
}

async function reloadFields() {
  if (!id) return
  try {
    const fieldsRes = await datasetService.getFields(id)
    fieldData.value = fieldsRes.items.map(mapFieldToRow)
    fieldsPagination.total = fieldsRes.total
  } catch { /* ignore */ }
}

// T6: Agent check state
const agentCheckResult = ref<AgentCheckResponse | null>(null)
const agentCheckLoading = ref(false)

async function checkAgent() {
  if (!id) return
  agentCheckLoading.value = true
  try {
    agentCheckResult.value = await datasetService.checkAgent(id)
  } finally {
    agentCheckLoading.value = false
  }
}

// T5: null rate computation
async function computeNullRates() {
  if (!id) return
  try {
    await datasetService.computeNullRates(id)
    await reloadFields()
  } catch { /* ignore */ }
}

const semanticMappings = [
  { field: 'order_id', semantic: '订单.订单ID', confidence: '高' },
  { field: 'customer_name', semantic: '客户.客户名称', confidence: '高' },
  { field: 'amount', semantic: '订单.订单金额', confidence: '高' },
]

const usageRecords = [
  { time: '2026-06-29 10:15', user: '张三', operation: 'Agent 查询', detail: '查询上月销售额前10客户' },
  { time: '2026-06-28 14:20', user: '李四', operation: '数据浏览', detail: '浏览订单表样例数据' },
]

async function loadData() {
  if (!id) return
  loading.value = true
  try {
    const ds = await datasetService.get(id)
    table.value = mapDatasetToDetail(ds)

    // Load fields
    try {
      const fieldsRes = await datasetService.getFields(id)
      fieldData.value = fieldsRes.items.map(mapFieldToRow)
      fieldsPagination.total = fieldsRes.total
    } catch { /* fields optional */ }

    // T4: Load sample data
    try {
      const sample = await datasetService.getSampleData(id, 10)
      sampleColumns.value = sample.columns
      sampleData.value = sample.rows.map(row => {
        const obj: Record<string, unknown> = {}
        sample.columns.forEach((col, i) => { obj[col] = row[i] })
        return obj
      })
    } catch { /* sample optional */ }

    // Load quality records
    try {
      const runsRes = await qualityService.getRuns({ page: 1, pageSize: 100 })
      qualityRecords.value = runsRes.items.map(mapRunToQuality)
    } catch { /* quality optional */ }
  } catch {
    // dataset load failed
  } finally {
    loading.value = false
  }
}

onMounted(() => { loadData() })
</script>

<style lang="scss" scoped>
.summary-row {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 12px;
  margin-bottom: 16px;
}

.sum-item {
  display: flex;
  flex-direction: column;
  gap: 4px;
  padding: 14px 16px;
  border: 1px solid #e5e7eb;
  border-radius: 6px;
}

.sum-label {
  font-size: 12px;
  color: #9ca3af;
}

.sum-value {
  font-size: 16px;
  font-weight: 600;
  color: #1f2937;
}

h3 {
  font-size: 16px;
  margin: 0 0 16px;
  color: #1f2937;
}

.link-chain {
  display: flex;
  align-items: center;
  gap: 20px;
  padding: 20px 0;
}

.chain-node {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 6px;
}

.node-dot {
  width: 12px;
  height: 12px;
  border-radius: 50%;
  background: #d1d5db;

  &.active {
    background: #2563eb;
  }
}

.node-label {
  font-size: 12px;
  color: #9ca3af;
}

.node-value {
  font-size: 14px;
  font-weight: 500;
  color: #1f2937;
}

.chain-arrow {
  font-size: 18px;
  color: #d1d5db;
}

// T4: 批量操作工具栏
.batch-toolbar {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 10px 14px;
  margin-bottom: 8px;
  background: #fef3c7;
  border: 1px solid #fcd34d;
  border-radius: 6px;
}

.batch-hint {
  font-size: 13px;
  color: #92400e;
  font-weight: 500;
}

.text-muted {
  color: #6b7280;
  font-size: 13px;
}
</style>
