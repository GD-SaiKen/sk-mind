<template>
  <div class="page-layout">
    <Index
      title="关系图谱"
      :breadcrumb="[{ label: '首页', to: '/' }, { label: '关系图谱' }]"
      description="管理业务对象实例之间的语义关系边，查询关系路径，确认规则或 AI 生成的关系，构建企业知识图谱。"
    />

    <TabNav v-model="activeTab" :tabs="tabs" />

    <el-row :gutter="16" class="stat-row">
      <el-col :span="6">
        <el-card shadow="never" class="info-card">
          <div class="info-card-header">
            <div class="info-card-icon bg-blue"><el-icon :size="16"><Connection /></el-icon></div>
            <span class="info-card-label">关系边总数</span>
            <span class="subtag">图谱边</span>
          </div>
          <div class="val-row"><span class="val">{{ stats?.totalEdges ?? 0 }}</span><span class="badge neutral">全部关系边</span></div>
          <div class="foot">全部关系边</div>
        </el-card>
      </el-col>
      <el-col :span="6">
        <el-card shadow="never" class="info-card">
          <div class="info-card-header">
            <div class="info-card-icon bg-green"><el-icon :size="16"><CircleCheckFilled /></el-icon></div>
            <span class="info-card-label">已确认</span>
            <span class="subtag green">可信</span>
          </div>
          <div class="val-row">
            <span class="val green">{{ stats?.confirmedCount ?? 0 }}</span>
            <span class="badge neutral">确认率</span>
          </div>
          <div class="foot"><span>确认率</span><div class="health-bar"><div class="health-bar-fill" :style="{ width: (stats?.confirmRate ?? 0) + '%' }" /></div><span>{{ stats?.confirmRate ?? 0 }}%</span></div>
        </el-card>
      </el-col>
      <el-col :span="6">
        <el-card shadow="never" class="info-card">
          <div class="info-card-header">
            <div class="info-card-icon bg-purple"><el-icon :size="16"><Link /></el-icon></div>
            <span class="info-card-label">AI 生成</span>
            <span class="subtag">智能推理</span>
          </div>
          <div class="val-row"><span class="val">{{ stats?.aiGeneratedCount ?? 0 }}</span><span class="badge neutral">智能推理</span></div>
          <div class="foot">由 AI 自动生成</div>
        </el-card>
      </el-col>
      <el-col :span="6">
        <el-card shadow="never" class="info-card">
          <div class="info-card-header">
            <div class="info-card-icon bg-yellow"><el-icon :size="16"><WarningFilled /></el-icon></div>
            <span class="info-card-label">待确认</span>
            <span class="subtag danger-tag">需审核</span>
          </div>
          <div class="val-row"><span class="val yellow">{{ stats?.pendingCount ?? 0 }}</span><span class="badge neutral">待确认</span></div>
          <div class="foot">{{ (stats?.pendingCount ?? 0) > 0 ? '请及时确认' : '暂无待确认' }}</div>
        </el-card>
      </el-col>
    </el-row>

    <!-- ====== 关系边列表 ====== -->
    <Crud v-if="activeTab === '关系边列表'" :filter-items="edgeFilterItems" v-model:filter-values="edgeFilterValues" :pagination="edgesPagination" @filter-change="loadEdges">
      <template #filters-actions>
        <el-tag
          v-if="activeRelationCode"
          closable
          type="warning"
          effect="plain"
          @close="clearRelationFilter"
        >
          关系过滤：{{ activeRelationCode }}
        </el-tag>
        <el-button type="primary" :icon="Refresh" @click="loadEdges">刷新</el-button>
      </template>
      <template #table>
        <Table :columns="edgesColumns" :data="edges" :loading="edgeLoading">
          <template #col-from="{ row }">
            <el-tag effect="plain">{{ row.fromObjectName }}</el-tag>
            <span class="mono">{{ row.fromEntityId }}</span>
          </template>
          <template #col-to="{ row }">
            <el-tag effect="plain">{{ row.toObjectName }}</el-tag>
            <span class="mono">{{ row.toEntityId }}</span>
          </template>
        </Table>
      </template>
    </Crud>

    <!-- ====== 关系查询 ====== -->
    <el-card v-if="activeTab === '关系查询'" shadow="never">
      <div class="query-form">
        <el-row :gutter="16">
          <el-col :span="6">
            <label>对象类型</label>
            <el-select v-model="queryType" class="w-full" clearable filterable>
              <el-option v-for="o in objectOptions" :key="o.value" :label="o.label" :value="o.value" />
            </el-select>
          </el-col>
          <el-col :span="6">
            <label>对象 ID</label>
            <el-input v-model="queryId" placeholder="如 WO001，不填查全部" />
          </el-col>
          <el-col :span="4">
            <label>关系类型</label>
            <el-select v-model="queryRelationCode" class="w-full" clearable filterable>
              <el-option v-for="r in relationOptions" :key="r.value" :label="r.label" :value="r.value" />
            </el-select>
          </el-col>
          <el-col :span="4">
            <label>跳数范围</label>
            <el-select v-model="queryHops" class="w-full">
              <el-option label="1 跳" :value="1" />
              <el-option label="2 跳" :value="2" />
              <el-option label="3 跳" :value="3" />
            </el-select>
          </el-col>
          <el-col :span="4">
            <label>仅已确认</label>
            <el-switch v-model="queryConfirmedOnly" active-text="是" inactive-text="否" />
          </el-col>
        </el-row>
        <el-row :gutter="16" class="conf-row">
          <el-col :span="12">
            <label>可信度范围（下限）</label>
            <el-slider
              v-model="queryMinConfidence"
              :min="0"
              :max="1"
              :step="0.05"
              show-input
              :show-input-controls="false"
            />
          </el-col>
          <el-col :span="12" class="conf-hint">
            <span>仅展示可信度 ≥ {{ queryMinConfidence.toFixed(2) }} 的关系</span>
          </el-col>
        </el-row>
        <el-button type="primary" class="query-btn" :icon="Search" :loading="queryLoading" @click="handleQuery">查询关系路径</el-button>
      </div>
      <div v-if="showResult" class="result-section">
        <h4>查询结果（{{ queryResult?.total ?? 0 }} 条路径）</h4>
        <div v-if="queryResult && queryResult.paths.length > 0" class="path-list">
          <div v-for="(path, idx) in queryResult.paths" :key="idx" class="path-card">
            <div v-for="(edge, eidx) in path.edges" :key="eidx" class="path-segment">
              <template v-if="eidx === 0">
                <el-tag effect="plain">{{ edge.fromType }}</el-tag>
                <span class="mono">{{ edge.fromId }}</span>
              </template>
              <span class="arrow">→ {{ edge.relationName }} →</span>
              <el-tag effect="plain">{{ edge.toType }}</el-tag>
              <span class="mono">{{ edge.toId }}</span>
              <span class="path-meta">可信度 {{ (edge.confidence * 100).toFixed(0) }}% · {{ edge.status === 'confirmed' ? '已确认' : edge.status }}</span>
            </div>
          </div>
        </div>
        <el-empty v-else description="未找到匹配的关系路径" :image-size="60" />
      </div>
    </el-card>

    <!-- ====== 待确认关系 ====== -->
    <div v-if="activeTab === '待确认关系'" class="pending-list">
      <el-alert v-if="pendingEdges.length === 0" title="暂无待确认关系" type="success" :closable="false" />
      <div v-for="edge in pendingEdges" :key="edge.id" class="pending-card">
        <div class="pending-header">
          <div class="pending-path">
            <el-tag effect="plain">{{ edge.fromObjectName }}</el-tag>
            <span class="mono">{{ edge.fromEntityId }}</span>
            <span class="arrow">→ {{ edge.relationName }} →</span>
            <el-tag effect="plain">{{ edge.toObjectName }}</el-tag>
            <span class="mono">{{ edge.toEntityId }}</span>
          </div>
          <el-tag type="warning" effect="plain">待确认</el-tag>
        </div>
        <div class="pending-meta">
          来源: {{ edge.sourceDataset || '-' }} · 生成方式: {{ edge.generatedBy }} · 可信度: {{ (edge.confidence * 100).toFixed(0) }}%
        </div>
        <div class="pending-actions">
          <el-button type="primary" :disabled="actionLoading" @click="confirmEdge(edge)">确认关系</el-button>
          <el-button plain type="danger" :disabled="actionLoading" @click="rejectEdge(edge)">拒绝</el-button>
          <el-button plain :disabled="actionLoading" @click="markInsufficient(edge)">信息不足</el-button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed, onMounted, reactive, ref, watch } from 'vue'
import { useRoute } from 'vue-router'
import { ElMessage } from 'element-plus'
import { Search, Refresh, Connection, CircleCheckFilled, Link, WarningFilled } from '@element-plus/icons-vue'
import TabNav from '@/components/tab-nav/index.vue'
import type { TabItem } from '@/components/tab-nav/types'
import Index from '@/components/page-header/index.vue'
import { Crud, Table } from '@/components/crud'
import type { ColumnSchema, FilterItem } from '@/components/crud'
import { graphService } from '@/api/services/graph'
import { semanticService } from '@/api/services/semantic'
import type { GraphEdge, GraphStats, GraphQueryResult, SemanticObject, SemanticRelation } from '@/api/types'

const activeTab = ref('关系边列表')
const route = useRoute()
const tabs: TabItem[] = [
  { key: '关系边列表', label: '关系边列表' },
  { key: '关系查询', label: '关系查询' },
  { key: '待确认关系', label: '待确认关系' },
]

const edgeFilterItems: FilterItem[] = [
  { key: 'keyword', placeholder: '搜索实体 ID...', width: '200px' },
]
const edgeFilterValues = ref<Record<string, any>>({})

// ── Data ──
const edges = ref<GraphEdge[]>([])
const stats = ref<GraphStats | null>(null)
const edgeLoading = ref(false)
const actionLoading = ref(false)
const queryLoading = ref(false)

const edgePage = ref(1)
const edgePageSize = ref(20)
const edgeTotal = ref(0)
const edgesPagination = reactive({
  get page() { return edgePage.value },
  set page(v) { edgePage.value = v },
  get pageSize() { return edgePageSize.value },
  set pageSize(v) { edgePageSize.value = v },
  get total() { return edgeTotal.value },
  set total(v) { edgeTotal.value = v },
  onPageChange() { loadEdges() },
  onSizeChange() { edgePage.value = 1; loadEdges() },
})

const pendingEdges = computed(() => edges.value.filter(e => e.status === 'pending'))

// ── 查询表单 ──
const queryType = ref('')
const queryId = ref('')
const queryRelationCode = ref('')
const queryHops = ref(2)
const queryMinConfidence = ref(0.7)
const queryConfirmedOnly = ref(true)
const showResult = ref(false)
const queryResult = ref<GraphQueryResult | null>(null)

// 从语义模型页「查看边」跳转带入的关系编码过滤
const activeRelationCode = ref<string | undefined>(undefined)

const objectOptions = ref<{ label: string; value: string }[]>([])
const relationOptions = ref<{ label: string; value: string }[]>([])

// ── 列定义 ──
const edgesColumns: ColumnSchema[] = [
  { type: 'custom', prop: 'from', label: '起点对象', minWidth: 170, slotName: 'col-from' },
  { type: 'tag', prop: 'relationName', label: '关系', width: 130, tagType: 'warning' },
  { type: 'custom', prop: 'to', label: '终点对象', minWidth: 170, slotName: 'col-to' },
  { type: 'text', prop: 'sourceDataset', label: '来源', width: 140 },
  { type: 'tag', prop: 'generatedBy', label: '生成方式', width: 110, tagMap: { system: 'success', mapping_rule: '', ai: 'warning', manual: 'info' } },
  { type: 'text', prop: 'confidence', label: '可信度', width: 90, align: 'center', formatter: (v: number) => (v * 100).toFixed(0) + '%' },
  { type: 'tag', prop: 'status', label: '状态', width: 90,
    formatter: (v: string) => ({ confirmed: '已确认', pending: '待确认', rejected: '已拒绝', insufficient: '信息不足' }[v] ?? v),
    tagMap: { confirmed: 'success', pending: 'warning', rejected: 'danger', insufficient: 'info' } },
  { type: 'action', label: '操作', width: 170, buttons: [
    { label: '确认', type: 'success', onClick: (row: any) => confirmEdge(row as GraphEdge), hidden: (row: any) => (row as GraphEdge).status === 'confirmed' },
    { label: '拒绝', type: 'danger', onClick: (row: any) => rejectEdge(row as GraphEdge), hidden: (row: any) => ['confirmed', 'rejected'].includes((row as GraphEdge).status) },
    { label: '信息不足', onClick: (row: any) => markInsufficient(row as GraphEdge), hidden: (row: any) => ['confirmed', 'rejected'].includes((row as GraphEdge).status) },
  ] },
]

// ── 数据加载 ──
async function loadEdges() {
  edgeLoading.value = true
  try {
    const res = await graphService.getEdges({
      keyword: edgeFilterValues.value.keyword || undefined,
      relationCode: activeRelationCode.value || undefined,
      page: edgePage.value,
      pageSize: edgePageSize.value,
    })
    edges.value = res.items
    edgeTotal.value = res.total
  } catch { edges.value = [] }
  finally { edgeLoading.value = false }
}

async function loadStats() {
  try { stats.value = await graphService.getStats() } catch { /* ignore */ }
}

function clearRelationFilter() {
  activeRelationCode.value = undefined
  edgePage.value = 1
  loadEdges()
}

async function loadOptions() {
  try {
    const objRes = await semanticService.getObjects({ pageSize: 100 })
    objectOptions.value = objRes.items
      .filter(o => o.status === 'active')
      .map((o: SemanticObject) => ({
        label: `${o.name} (${o.code.split('.').pop()})`,
        value: o.code.split('.').pop() || o.code,
      }))
  } catch { /* ignore */ }
  try {
    const relRes = await semanticService.getRelations({ pageSize: 100 })
    relationOptions.value = relRes.items
      .filter(r => r.status === 'active')
      .map((r: SemanticRelation) => ({ label: `${r.name} (${r.code})`, value: r.code }))
  } catch { /* ignore */ }
}

// ── 路径查询 ──
async function handleQuery() {
  queryLoading.value = true
  showResult.value = true
  try {
    const res = await graphService.queryGraph({
      type: queryType.value || undefined,
      id: queryId.value || undefined,
      relationCode: queryRelationCode.value || undefined,
      hops: queryHops.value,
      minConfidence: queryMinConfidence.value,
      confirmedOnly: queryConfirmedOnly.value,
    })
    queryResult.value = res
  } catch {
    queryResult.value = null
  } finally {
    queryLoading.value = false
  }
}

// ── 状态流转 ──
async function confirmEdge(edge: GraphEdge) {
  actionLoading.value = true
  try {
    await graphService.confirmEdge(edge.id)
    ElMessage.success('已确认')
    loadEdges(); loadStats()
  } catch { /* 错误提示由 axios 拦截器统一处理 */ }
  finally { actionLoading.value = false }
}

async function rejectEdge(edge: GraphEdge) {
  actionLoading.value = true
  try {
    await graphService.rejectEdge(edge.id)
    ElMessage.success('已拒绝')
    loadEdges(); loadStats()
  } catch { /* 错误提示由 axios 拦截器统一处理 */ }
  finally { actionLoading.value = false }
}

async function markInsufficient(edge: GraphEdge) {
  actionLoading.value = true
  try {
    await graphService.markInsufficient(edge.id)
    ElMessage.success('已标记信息不足')
    loadEdges(); loadStats()
  } catch { /* 错误提示由 axios 拦截器统一处理 */ }
  finally { actionLoading.value = false }
}

watch(activeTab, () => { edgePage.value = 1 })

onMounted(() => {
  const relCode = typeof route.query.relationCode === 'string'
    ? route.query.relationCode
    : undefined
  activeRelationCode.value = relCode
  queryRelationCode.value = relCode || ''
  loadEdges()
  loadStats()
  loadOptions()
})
</script>

<style lang="scss" scoped>
.tab-btn { padding: 10px 16px; border: none; background: none; font-size: $font-size-base; color: $color-text-secondary; cursor: pointer; border-bottom: 2px solid transparent; &:hover { color: $color-text-primary; } &.active { color: $color-primary; border-bottom-color: $color-primary; font-weight: $font-weight-medium; } }
.stat-row { margin: 0 !important; :deep(.el-col) { padding-left: 8px !important; padding-right: 8px !important; } :deep(.el-col:first-child) { padding-left: 0 !important; } :deep(.el-col:last-child) { padding-right: 0 !important; } }
.info-card { :deep(.el-card__body) { display: flex; flex-direction: column; gap: 8px; padding: 20px; } }
.info-card-header { display: flex; align-items: center; gap: 6px; }
.info-card-icon { display: flex; align-items: center; justify-content: center; width: 32px; height: 32px; border-radius: 8px; &.bg-blue { background: #dbeafe; color: $color-primary; } &.bg-green { background: #dcfce7; color: $color-success; } &.bg-purple { background: #ede9fe; color: #7c3aed; } &.bg-yellow { background: #fef3c7; color: $color-warning; } }
.info-card-label { font-size: $font-size-base; color: $color-text-secondary; }
.subtag { font-size: $font-size-xs; padding: 1px 6px; border-radius: 4px; margin-left: auto; white-space: nowrap; background: #f3f4f6; color: $color-text-placeholder; &.green { color: $color-success; background: #f0fdf4; } &.danger-tag { color: $color-danger; background: #fee2e2; border: 1px solid #fecaca; } }
.val-row { display: flex; align-items: baseline; gap: 8px; }
.val { font-size: 28px; font-weight: $font-weight-bold; color: $color-text-primary; &.green { color: $color-success; } &.yellow { color: $color-warning; } }
.badge { font-size: $font-size-xs; padding: 1px 6px; border-radius: 4px; &.green-bg { color: $color-success; background: #f0fdf4; } &.neutral { color: $color-text-placeholder; background: #f3f4f6; } }
.foot { display: flex; align-items: center; gap: 6px; font-size: $font-size-xs; color: $color-text-placeholder; }
.health-bar { flex: 1; height: 4px; background: #f3f4f6; border-radius: 2px; overflow: hidden; }
.health-bar-fill { height: 100%; background: $color-success; border-radius: 2px; }
.mono { font-family: $font-family-mono; font-size: $font-size-xs; color: $color-text-secondary; margin-left: 4px; }
.query-form { display: flex; flex-direction: column; gap: 16px; label { display: block; font-size: $font-size-sm; color: $color-text-secondary; margin-bottom: 4px; } }
.conf-row { align-items: center; }
.conf-hint { display: flex; align-items: center; font-size: $font-size-sm; color: $color-text-secondary; }
.w-full { width: 100%; }
.query-btn { align-self: flex-start; }
.result-section { border-top: 1px solid $color-border; padding-top: 16px; margin-top: 16px; h4 { font-size: $font-size-base; margin-bottom: 12px; } }
.path-list { display: flex; flex-direction: column; gap: 12px; }
.path-card { padding: 14px 16px; background: #eff6ff; border: 1px solid #bfdbfe; border-radius: $radius-base; display: flex; flex-direction: column; gap: 8px; }
.path-segment { display: flex; align-items: center; gap: 8px; flex-wrap: wrap; }
.path-meta { font-size: $font-size-xs; color: $color-text-secondary; }
.arrow { color: $color-text-secondary; font-size: $font-size-sm; }
.pending-list { display: flex; flex-direction: column; gap: 12px; }
.pending-card { padding: 16px; background: #fefce8; border: 1px solid #fef08a; border-radius: $radius-base; }
.pending-header { display: flex; align-items: center; justify-content: space-between; margin-bottom: 8px; }
.pending-path { display: flex; align-items: center; gap: 4px; flex-wrap: wrap; }
.pending-meta { font-size: $font-size-xs; color: $color-text-secondary; margin-bottom: 12px; }
.pending-actions { display: flex; gap: 8px; }
</style>
