﻿<template>
  <div class="rg-page">
    <div class="tab-bar">
      <button v-for="tab in tabs" :key="tab" class="tab-btn" :class="{ active: activeTab === tab }" @click="activeTab = tab">{{ tab }}<span v-if="tab === '待确认关系'" class="tab-count">{{ pendingCount }}</span></button>
    </div>

    <!-- 统计卡片 -->
    <el-row :gutter="16" class="stat-row">
      <el-col :span="6"><el-card shadow="never" class="info-card"><div class="info-card-header"><div class="info-card-icon bg-blue"><el-icon :size="16"><Connection /></el-icon></div><span class="info-card-label">关系边总数</span><span class="subtag">图谱边</span></div><div class="val-row"><span class="val">{{ relationEdges.length }}</span><span class="badge green-bg">↑ 2 较昨日</span></div><div class="foot">全部关系边</div></el-card></el-col>
      <el-col :span="6"><el-card shadow="never" class="info-card"><div class="info-card-header"><div class="info-card-icon bg-green"><el-icon :size="16"><CircleCheckFilled /></el-icon></div><span class="info-card-label">已确认</span><span class="subtag green">可信</span></div><div class="val-row"><span class="val green">{{ confirmedCount }}</span><span class="badge neutral">较昨日持平</span></div><div class="foot"><span>确认率</span><div class="health-bar"><div class="health-bar-fill" :style="{ width: confirmRate + '%' }" /></div><span>{{ confirmRate }}%</span></div></el-card></el-col>
      <el-col :span="6"><el-card shadow="never" class="info-card"><div class="info-card-header"><div class="info-card-icon bg-purple"><el-icon :size="16"><Link /></el-icon></div><span class="info-card-label">AI 生成</span><span class="subtag">智能推理</span></div><div class="val-row"><span class="val">3</span><span class="badge neutral">较昨日持平</span></div><div class="foot">由 AI 自动生成</div></el-card></el-col>
      <el-col :span="6"><el-card shadow="never" class="info-card"><div class="info-card-header"><div class="info-card-icon bg-yellow"><el-icon :size="16"><WarningFilled /></el-icon></div><span class="info-card-label">待确认</span><span class="subtag danger-tag">需审核</span></div><div class="val-row"><span class="val yellow">{{ pendingCount }}</span><span class="badge neutral">较昨日持平</span></div><div class="foot">{{ pendingCount > 0 ? '请及时确认' : '暂无待确认' }}</div></el-card></el-col>
    </el-row>

    <!-- 关系边列表 -->
    <Index v-if="activeTab === '关系边列表'" :pagination="edgesPagination">
      <template #filters>
        <el-input v-model="searchTerm" placeholder="搜索关系..." :prefix-icon="Search" class="search-input" clearable />
      </template>
      <template #actions>
        <el-button type="primary" :icon="Plus">创建关系边</el-button>
      </template>
      <template #table>
        <Table :columns="edgesColumns" :data="pagedEdges">
          <template #col-fromEntity="{ row }">
            <el-tag effect="plain">{{ row.fromEntity }}</el-tag>
            <span class="mono">{{ row.fromId }}</span>
          </template>
          <template #col-toEntity="{ row }">
            <el-tag effect="plain">{{ row.toEntity }}</el-tag>
            <span class="mono">{{ row.toId }}</span>
          </template>
        </Table>
      </template>
    </Index>

    <!-- 关系查询 -->
    <el-card v-if="activeTab === '关系查询'" shadow="never">
      <div class="query-form">
        <el-row :gutter="16">
          <el-col :span="8"><label>对象类型</label><el-select v-model="queryType" class="w-full"><el-option label="客户" value="customer" /><el-option label="订单" value="order" /><el-option label="产品" value="product" /></el-select></el-col>
          <el-col :span="8"><label>对象ID</label><el-input v-model="queryId" placeholder="如: CUST-8856" /></el-col>
          <el-col :span="8"><label>跳数范围</label><el-select v-model="queryHops" class="w-full"><el-option label="1 跳" value="1" /><el-option label="2 跳" value="2" /><el-option label="3 跳" value="3" /></el-select></el-col>
        </el-row>
        <el-button type="primary" class="query-btn" @click="showResult = true"><el-icon :size="16"><Search /></el-icon>查询关系路径</el-button>
      </div>
      <div v-if="showResult" class="result-section">
        <h4>查询结果示例</h4>
        <div class="result-path">
          <el-tag effect="plain">客户 CUST-8856</el-tag><span class="arrow">→ 下单 →</span>
          <el-tag effect="plain">订单 SO-2026-001234</el-tag><span class="arrow">→ 包含 →</span>
          <el-tag effect="plain">产品 PROD-5678</el-tag>
          <span class="result-meta">可信度: 93% · 已确认</span>
        </div>
      </div>
    </el-card>

    <!-- 待确认关系（卡片布局） -->
    <div v-if="activeTab === '待确认关系'" class="pending-list">
      <div v-for="edge in pendingEdges" :key="edge.id" class="pending-card">
        <div class="pending-header">
          <div class="pending-path">
            <el-tag effect="plain">{{ edge.fromEntity }}</el-tag><span class="mono">{{ edge.fromId }}</span>
            <span class="arrow">→ {{ edge.relation }} →</span>
            <el-tag effect="plain">{{ edge.toEntity }}</el-tag><span class="mono">{{ edge.toId }}</span>
          </div>
          <el-tag type="warning" effect="plain">待确认</el-tag>
        </div>
        <div class="pending-meta">来源: {{ edge.source }} · 生成方式: {{ edge.generatedBy }} · 可信度: {{ (edge.confidence * 100).toFixed(0) }}%</div>
        <div class="pending-actions">
          <el-button plain>查看证据</el-button>
          <el-button type="primary">确认关系</el-button>
          <el-button plain type="danger">拒绝</el-button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed, reactive, ref, watch } from 'vue'
import { Search, Plus, Edit, Connection, CircleCheckFilled, Link, WarningFilled } from '@element-plus/icons-vue'
import { Index, Table } from '@/components/crud'
import type { ColumnSchema } from '@/components/crud'

const activeTab = ref('关系边列表')
const searchTerm = ref('')
const queryType = ref('customer')
const queryId = ref('')
const queryHops = ref('2')
const showResult = ref(false)
const tabs = ['关系边列表', '关系查询', '待确认关系']

interface Edge { id: string; fromEntity: string; fromId: string; relation: string; toEntity: string; toId: string; source: string; generatedBy: string; confidence: number; confirmed: boolean }

const relationEdges: Edge[] = [
  { id: '1', fromEntity: '客户', fromId: 'CUST-8856', relation: '下单', toEntity: '订单', toId: 'SO-2026-001234', source: '销售订单表', generatedBy: '数据映射', confidence: 0.95, confirmed: true },
  { id: '2', fromEntity: '订单', fromId: 'SO-2026-001234', relation: '包含', toEntity: '产品', toId: 'PROD-5678', source: '订单明细表', generatedBy: '数据映射', confidence: 0.98, confirmed: true },
  { id: '3', fromEntity: '客户', fromId: 'CUST-8856', relation: '可能关联', toEntity: '客户', toId: 'CUST-7745', source: 'AI推理', generatedBy: 'AI生成', confidence: 0.65, confirmed: false },
]

const filteredEdges = computed(() =>
  relationEdges.filter(e => {
    const s = searchTerm.value
    return !s || e.fromEntity.includes(s) || e.toEntity.includes(s) || e.relation.includes(s) || e.source.includes(s)
  })
)

function slicePage<T>(data: T[], page: number, size: number) {
  return data.slice((page - 1) * size, page * size)
}

const edgesPagination = reactive({ page: 1, pageSize: 20, total: 0, onPageChange() {}, onSizeChange() {} })
const pagedEdges = computed(() => slicePage(filteredEdges.value, edgesPagination.page, edgesPagination.pageSize))
watch([filteredEdges, () => edgesPagination.pageSize], () => { edgesPagination.total = filteredEdges.value.length })

const pendingEdges = computed(() => relationEdges.filter(e => !e.confirmed))
const pendingCount = computed(() => pendingEdges.value.length)
const confirmedCount = computed(() => relationEdges.filter(e => e.confirmed).length)
const confirmRate = computed(() => relationEdges.length > 0 ? Math.round(confirmedCount.value / relationEdges.length * 100) : 0)

const edgesColumns: ColumnSchema[] = [
  { type: 'custom', prop: 'fromEntity', label: '源实体', minWidth: 160 },
  {
    type: 'tag', prop: 'relation', label: '关系', width: 120,
    tagType: 'warning',
  },
  { type: 'custom', prop: 'toEntity', label: '目标实体', minWidth: 160 },
  { type: 'text', prop: 'source', label: '来源', width: 140 },
  {
    type: 'tag', prop: 'generatedBy', label: '生成方式', width: 100,
    tagMap: { 'AI生成': 'warning' },
  },
  {
    type: 'text', prop: 'confidence', label: '可信度', width: 90, align: 'center',
    formatter: (v: number) => (v * 100).toFixed(0) + '%',
  },
  {
    type: 'tag', prop: 'confirmed', label: '状态', width: 90,
    formatter: (v: boolean) => v ? '已确认' : '待确认',
    tagMap: { true: 'success', false: 'warning' },
  } as ColumnSchema,
  { type: 'action', label: '操作', width: 80, buttons: [{ label: '', icon: 'Edit', onClick: () => {} }] },
]
</script>

<style lang="scss" scoped>
.rg-page { display: flex; flex-direction: column; gap: 20px; }
.tab-bar { display: flex; gap: 0; border-bottom: 1px solid $color-border; }
.tab-btn { padding: 10px 16px; border: none; background: none; font-size: $font-size-base; color: $color-text-secondary; cursor: pointer; border-bottom: 2px solid transparent; &:hover { color: $color-text-primary; } &.active { color: $color-primary; border-bottom-color: $color-primary; font-weight: $font-weight-medium; } }
.tab-count { font-size: $font-size-xs; color: $color-text-placeholder; margin-left: 4px; }
.search-input { width: 280px; }

.stat-row { margin: 0 !important; :deep(.el-col) { padding-left: 8px !important; padding-right: 8px !important; } :deep(.el-col:first-child) { padding-left: 0 !important; } :deep(.el-col:last-child) { padding-right: 0 !important; } }
.info-card { :deep(.el-card__body) { padding: 20px; display: flex; flex-direction: column; gap: 8px; } }
.info-card-header { display: flex; align-items: center; gap: 6px; }
.info-card-icon { width: 32px; height: 32px; border-radius: 8px; display: flex; align-items: center; justify-content: center; &.bg-blue { background: #dbeafe; color: $color-primary; } &.bg-green { background: #dcfce7; color: $color-success; } &.bg-purple { background: #ede9fe; color: #7c3aed; } &.bg-yellow { background: #fef3c7; color: $color-warning; } }
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
.w-full { width: 100%; }
.query-btn { align-self: flex-start; }
.result-section { border-top: 1px solid $color-border; padding-top: 16px; margin-top: 16px; h4 { font-size: $font-size-base; margin-bottom: 12px; } }
.result-path { display: flex; align-items: center; gap: 8px; flex-wrap: wrap; padding: 16px; background: #eff6ff; border: 1px solid #bfdbfe; border-radius: $radius-base; }
.arrow { color: $color-text-secondary; font-size: $font-size-sm; }
.result-meta { font-size: $font-size-xs; color: $color-text-secondary; width: 100%; margin-top: 8px; }

.pending-list { display: flex; flex-direction: column; gap: 12px; }
.pending-card { padding: 16px; background: #fefce8; border: 1px solid #fef08a; border-radius: $radius-base; }
.pending-header { display: flex; align-items: center; justify-content: space-between; margin-bottom: 8px; }
.pending-path { display: flex; align-items: center; gap: 4px; }
.pending-meta { font-size: $font-size-xs; color: $color-text-secondary; margin-bottom: 12px; }
.pending-actions { display: flex; gap: 8px; }
</style>
