<template>
  <div class="page-layout">
    <Index
      title="语义模型"
      :breadcrumb="[{ label: '首页', to: '/' }, { label: '语义模型' }]"
      description="维护业务对象、属性、语义关系和数据映射，为 Agent 提供业务语义理解能力。"
    />

    <div class="tab-bar">
      <button v-for="tab in tabs" :key="tab" class="tab-btn" :class="{ active: activeTab === tab }" @click="activeTab = tab">
        {{ tab }}
      </button>
    </div>

    <el-row :gutter="16" class="stat-row">
      <el-col :span="6">
        <el-card shadow="never" class="info-card">
          <div class="info-card-header">
            <div class="info-card-icon bg-indigo"><el-icon :size="16"><Service /></el-icon></div>
            <span class="info-card-label">业务对象</span>
            <span class="subtag">已建模</span>
          </div>
          <div class="val-row"><span class="val">3</span><span class="badge neutral">较昨日持平</span></div>
          <div class="foot">订单 · 客户 · 产品</div>
        </el-card>
      </el-col>
      <el-col :span="6">
        <el-card shadow="never" class="info-card">
          <div class="info-card-header">
            <div class="info-card-icon bg-blue"><el-icon :size="16"><Collection /></el-icon></div>
            <span class="info-card-label">对象属性</span>
            <span class="subtag">已定义</span>
          </div>
          <div class="val-row"><span class="val">28</span><span class="badge neutral">较昨日持平</span></div>
          <div class="foot">全部已映射</div>
        </el-card>
      </el-col>
      <el-col :span="6">
        <el-card shadow="never" class="info-card">
          <div class="info-card-header">
            <div class="info-card-icon bg-green"><el-icon :size="16"><Connection /></el-icon></div>
            <span class="info-card-label">语义关系</span>
            <span class="subtag green">健康</span>
          </div>
          <div class="val-row"><span class="val green">56</span><span class="badge neutral">较昨日持平</span></div>
          <div class="foot">已确认</div>
        </el-card>
      </el-col>
      <el-col :span="6">
        <el-card shadow="never" class="info-card">
          <div class="info-card-header">
            <div class="info-card-icon bg-purple"><el-icon :size="16"><Link /></el-icon></div>
            <span class="info-card-label">数据映射</span>
            <span class="subtag">待确认</span>
          </div>
          <div class="val-row"><span class="val">3</span><span class="badge neutral">较昨日持平</span></div>
          <div class="foot">1 个待确认</div>
        </el-card>
      </el-col>
    </el-row>

    <Crud v-if="activeTab === '业务对象'" :filter-items="searchFilterItems" v-model:filter-values="searchValues" :pagination="soPagination">
      <template #filters-actions>
        <el-button type="primary" :icon="Plus">创建业务对象</el-button>
      </template>
      <template #table><Table :columns="soColumns" :data="pagedObjects" /></template>
    </Crud>

    <Crud v-if="activeTab === '语义关系'" :filter-items="searchFilterItems" v-model:filter-values="searchValues" :pagination="srPagination">
      <template #filters-actions>
        <el-button type="primary" :icon="Plus">创建关系</el-button>
      </template>
      <template #table><Table :columns="srColumns" :data="pagedRelations" /></template>
    </Crud>

    <Crud v-if="activeTab === '数据映射'" :filter-items="searchFilterItems" v-model:filter-values="searchValues" :pagination="dmPagination">
      <template #filters-actions>
        <el-button type="primary" :icon="Plus">创建映射</el-button>
      </template>
      <template #table><Table :columns="dmColumns" :data="pagedMappings" /></template>
    </Crud>

    <Crud v-if="activeTab === '行动策略'" :filter-items="searchFilterItems" v-model:filter-values="searchValues" :pagination="apPagination">
      <template #filters-actions>
        <el-button type="primary" :icon="Plus">配置策略</el-button>
      </template>
      <template #table>
        <Table :columns="apColumns" :data="pagedPolicies">
          <template #col-forbiddenActions="{ row }"><span class="text-danger">{{ row.forbiddenActions }}</span></template>
        </Table>
      </template>
    </Crud>

    <el-card v-if="activeTab === '对象属性'" shadow="never">
      <el-empty description="对象属性管理功能即将上线" />
    </el-card>
  </div>
</template>

<script setup lang="ts">
import { computed, reactive, ref, watch } from 'vue'
import { Search, Plus, Edit, Service, Collection, Connection, Link, Select } from '@element-plus/icons-vue'
import Index from '@/components/page-header/index.vue'
import { Crud, Table } from '@/components/crud'
import type { ColumnSchema, FilterItem } from '@/components/crud'

const activeTab = ref('业务对象')
const searchFilterItems: FilterItem[] = [{ key: 'keyword', placeholder: '搜索...', width: '260px' }]
const searchValues = ref<Record<string, any>>({})
const tabs = ['业务对象', '对象属性', '语义关系', '数据映射', '行动策略']

const semanticObjects = [
  { code: 'ORDER', name: '订单', description: '销售订单业务对象', attrCount: 8, relCount: 12 },
  { code: 'CUSTOMER', name: '客户', description: '客户信息业务对象', attrCount: 10, relCount: 8 },
  { code: 'PRODUCT', name: '产品', description: '产品信息业务对象', attrCount: 10, relCount: 6 },
]

const semanticRelations = [
  { name: '下单', subject: '客户', object: '订单', direction: '单向', type: '创建', agentEnabled: true },
  { name: '包含', subject: '订单', object: '产品', direction: '多对多', type: '关联', agentEnabled: true },
  { name: '属于', subject: '产品', object: '分类', direction: '多对一', type: '归属', agentEnabled: false },
]

const dataMappings = [
  { semantic: '订单.订单ID', sourceTable: 'sales_orders', sourceField: 'order_id', transform: '直接映射', confidence: '高', status: '已确认' },
  { semantic: '订单.订单金额', sourceTable: 'sales_orders', sourceField: 'amount', transform: '直接映射', confidence: '高', status: '已确认' },
  { semantic: '客户.客户名称', sourceTable: 'customer_info', sourceField: 'name', transform: 'TRIM函数', confidence: '中', status: '待确认' },
]

const actionPolicies = [
  { objectType: '订单', allowedActions: '查询, 创建', forbiddenActions: '删除', riskLevel: '中', requireConfirm: false },
  { objectType: '客户', allowedActions: '查询', forbiddenActions: '修改, 删除', riskLevel: '高', requireConfirm: true },
  { objectType: '产品', allowedActions: '查询', forbiddenActions: '修改, 删除, 创建', riskLevel: '低', requireConfirm: false },
]

function filterBySearch<T extends Record<string, any>>(items: T[], fields: string[]): T[] {
  if (!searchValues.value.keyword || '') return items
  return items.filter(item => fields.some(f => String(item[f] ?? '').includes(searchValues.value.keyword || '')))
}

const filteredObjects = computed(() => filterBySearch(semanticObjects, ['code', 'name', 'description']))
const filteredRelations = computed(() => filterBySearch(semanticRelations, ['name', 'subject', 'object']))
const filteredMappings = computed(() => filterBySearch(dataMappings, ['semantic', 'sourceTable', 'sourceField']))
const filteredPolicies = computed(() => filterBySearch(actionPolicies, ['objectType', 'allowedActions', 'forbiddenActions']))

function slicePage<T>(data: T[], page: number, size: number) { return data.slice((page - 1) * size, page * size) }
function usePage() { return reactive({ page: 1, pageSize: 20, total: 0, onPageChange() {}, onSizeChange() {} }) }

const soPagination = usePage()
const pagedObjects = computed(() => slicePage(filteredObjects.value, soPagination.page, soPagination.pageSize))
watch([filteredObjects, () => soPagination.pageSize], () => { soPagination.total = filteredObjects.value.length })

const srPagination = usePage()
const pagedRelations = computed(() => slicePage(filteredRelations.value, srPagination.page, srPagination.pageSize))
watch([filteredRelations, () => srPagination.pageSize], () => { srPagination.total = filteredRelations.value.length })

const dmPagination = usePage()
const pagedMappings = computed(() => slicePage(filteredMappings.value, dmPagination.page, dmPagination.pageSize))
watch([filteredMappings, () => dmPagination.pageSize], () => { dmPagination.total = filteredMappings.value.length })

const apPagination = usePage()
const pagedPolicies = computed(() => slicePage(filteredPolicies.value, apPagination.page, apPagination.pageSize))
watch([filteredPolicies, () => apPagination.pageSize], () => { apPagination.total = filteredPolicies.value.length })

const soColumns: ColumnSchema[] = [
  { type: 'text', prop: 'code', label: '对象编码', width: 130 },
  { type: 'text', prop: 'name', label: '对象名称', minWidth: 120 },
  { type: 'text', prop: 'description', label: '描述', minWidth: 200 },
  { type: 'text', prop: 'attrCount', label: '属性数', width: 80, align: 'center' },
  { type: 'text', prop: 'relCount', label: '关系数', width: 80, align: 'center' },
  { type: 'action', label: '操作', width: 80, buttons: [{ label: '', icon: Edit, onClick: () => {} }] },
]

const srColumns: ColumnSchema[] = [
  { type: 'text', prop: 'name', label: '关系名称', minWidth: 100 },
  { type: 'tag', prop: 'subject', label: '主体对象', width: 100 },
  { type: 'tag', prop: 'object', label: '客体对象', width: 100 },
  { type: 'text', prop: 'direction', label: '方向', width: 80 },
  { type: 'text', prop: 'type', label: '类型', width: 80 },
  { type: 'tag', prop: 'agentEnabled', label: 'Agent可用', width: 100, formatter: (v: boolean) => v ? '是' : '否', tagMap: { true: 'success', false: 'info' } } as ColumnSchema,
  { type: 'action', label: '操作', width: 80, buttons: [{ label: '', icon: Edit, onClick: () => {} }] },
]

const dmColumns: ColumnSchema[] = [
  { type: 'text', prop: 'semantic', label: '语义对象/属性', minWidth: 160 },
  { type: 'text', prop: 'sourceTable', label: '来源表', width: 140 },
  { type: 'text', prop: 'sourceField', label: '来源字段', width: 140 },
  { type: 'text', prop: 'transform', label: '转换', width: 100 },
  { type: 'tag', prop: 'confidence', label: '可信度', width: 90, tagMap: { '高': 'success', '中': 'warning' } },
  { type: 'tag', prop: 'status', label: '状态', width: 90, tagMap: { '已确认': 'success', '待确认': 'warning' } },
  { type: 'action', label: '操作', width: 120, buttons: [{ label: '确认', icon: Select, onClick: () => {} }, { label: '编辑', icon: Edit, onClick: () => {} }] },
]

const apColumns: ColumnSchema[] = [
  { type: 'tag', prop: 'objectType', label: '对象类型', width: 100 },
  { type: 'text', prop: 'allowedActions', label: '允许行动', minWidth: 140 },
  { type: 'custom', prop: 'forbiddenActions', label: '禁止行动', minWidth: 140 },
  { type: 'tag', prop: 'riskLevel', label: '风险等级', width: 100, tagMap: { '高': 'danger', '中': 'warning', '低': 'success' } },
  { type: 'tag', prop: 'requireConfirm', label: '需确认', width: 100, formatter: (v: boolean) => v ? '是' : '否', tagMap: { true: 'warning', false: 'info' } } as ColumnSchema,
  { type: 'action', label: '操作', width: 80, buttons: [{ label: '', icon: Edit, onClick: () => {} }] },
]
</script>

<style lang="scss" scoped>
.tab-bar { display: flex; gap: 0; border-bottom: 1px solid $color-border; }
.tab-btn { padding: 10px 16px; border: none; background: none; font-size: $font-size-base; color: $color-text-secondary; cursor: pointer; border-bottom: 2px solid transparent; &:hover { color: $color-text-primary; } &.active { color: $color-primary; border-bottom-color: $color-primary; font-weight: $font-weight-medium; } }
.stat-row { margin: 0 !important; :deep(.el-col) { padding-left: 8px !important; padding-right: 8px !important; } :deep(.el-col:first-child) { padding-left: 0 !important; } :deep(.el-col:last-child) { padding-right: 0 !important; } }
.info-card { :deep(.el-card__body) { display: flex; flex-direction: column; gap: 8px; padding: 20px; } }
.info-card-header { display: flex; align-items: center; gap: 6px; }
.info-card-icon { display: flex; align-items: center; justify-content: center; width: 32px; height: 32px; border-radius: 8px; &.bg-indigo { background: #e0e7ff; color: #4f46e5; } &.bg-blue { background: #dbeafe; color: $color-primary; } &.bg-green { background: #dcfce7; color: $color-success; } &.bg-purple { background: #ede9fe; color: #7c3aed; } }
.info-card-label { font-size: $font-size-base; color: $color-text-secondary; }
.subtag { font-size: $font-size-xs; padding: 1px 6px; border-radius: 4px; margin-left: auto; white-space: nowrap; background: #f3f4f6; color: $color-text-placeholder; &.green { color: $color-success; background: #f0fdf4; } }
.val-row { display: flex; align-items: baseline; gap: 8px; }
.val { font-size: 28px; font-weight: $font-weight-bold; color: $color-text-primary; &.green { color: $color-success; } }
.badge { font-size: $font-size-xs; padding: 1px 6px; border-radius: 4px; &.neutral { color: $color-text-placeholder; background: #f3f4f6; } }
.foot { font-size: $font-size-xs; color: $color-text-placeholder; }
.text-danger { color: $color-danger; }
</style>
