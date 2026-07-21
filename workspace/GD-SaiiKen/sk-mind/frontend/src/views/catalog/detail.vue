<template>
  <div class="page-layout detail-page">
    <Index
      :title="datasetName"
      :breadcrumb="[{ label: '首页', to: '/' }, { label: '数据目录', to: '/catalog' }, { label: datasetName }]"
    >
      <template #tags>
        <el-tag :type="ds.quality === 'pass' ? 'success' : ds.quality === 'warning' ? 'warning' : 'danger'" effect="plain">{{ qualityLabel }}</el-tag>
        <el-tag v-if="ds.agentEnabled" type="success" effect="plain">Agent 可用</el-tag>
      </template>
      <template #actions>
        <el-button :icon="Edit" plain>编辑说明</el-button>
        <router-link :to="`/tables/${datasetId}`"><el-button :icon="View" plain>查看数据表</el-button></router-link>
      </template>
    </Index>

    <el-row class="summary-row" :gutter="16">
      <el-col :span="6"><div class="summary-card"><div class="summary-label">来源</div><div class="summary-value">{{ ds.source }}</div></div></el-col>
      <el-col :span="6"><div class="summary-card"><div class="summary-label">记录数</div><div class="summary-value">{{ ds.records?.toLocaleString() }}</div></div></el-col>
      <el-col :span="6"><div class="summary-card"><div class="summary-label">字段数</div><div class="summary-value">{{ ds.fields }}</div></div></el-col>
      <el-col :span="6"><div class="summary-card"><div class="summary-label">更新时间</div><div class="summary-value">{{ ds.updatedAt }}</div></div></el-col>
    </el-row>

    <TabNav v-model="activeTab" :tabs="tabs" />

    <div v-if="activeTab === 'desc'" class="tab-content">
      <el-descriptions :column="2" border>
        <el-descriptions-item label="数据集名称">{{ ds.displayName }}</el-descriptions-item>
        <el-descriptions-item label="技术表名">{{ ds.name }}</el-descriptions-item>
        <el-descriptions-item label="来源">{{ ds.source }}</el-descriptions-item>
        <el-descriptions-item label="层级">{{ ds.layer }}</el-descriptions-item>
        <el-descriptions-item label="质量状态">
          <el-tag :type="ds.quality === 'pass' ? 'success' : ds.quality === 'warning' ? 'warning' : 'danger'" effect="plain">{{ qualityLabel }}</el-tag>
        </el-descriptions-item>
        <el-descriptions-item label="Agent 可用">
          <el-tag :type="ds.agentEnabled ? 'success' : 'info'" effect="plain">{{ ds.agentEnabled ? '是' : '否' }}</el-tag>
        </el-descriptions-item>
        <el-descriptions-item label="业务说明" :span="2">{{ ds.description }}</el-descriptions-item>
      </el-descriptions>
    </div>

    <div v-if="activeTab === 'fields'" class="tab-content">
      <Table :columns="fieldColumns" :data="fieldCatalogData">
        <template #col-fieldName="{ row }"><span class="mono">{{ row.fieldName }}</span></template>
        <template #col-meaning="{ row }"><span :class="{ 'text-muted': !row.meaning }">{{ row.meaning || '未填写说明' }}</span></template>
        <template #col-sensitive="{ row }">
          <el-tag v-if="row.sensitive" type="danger" effect="plain" size="small">{{ row.sensitiveType }}</el-tag>
          <span v-else>—</span>
        </template>
      </Table>
    </div>

    <div v-if="activeTab === 'lineage'" class="tab-content">
      <div class="lineage-chain">
        <div class="lineage-node">
          <span class="lineage-label">数据源</span>
          <el-tag effect="plain">{{ ds.source }}</el-tag>
        </div>
        <span class="lineage-arrow">→</span>
        <div class="lineage-node">
          <span class="lineage-label">Raw 层</span>
          <el-tag effect="plain">{{ ds.name }}_raw</el-tag>
        </div>
        <span class="lineage-arrow">→</span>
        <div class="lineage-node">
          <span class="lineage-label">Clean 层</span>
          <el-tag effect="plain">{{ ds.name }}_clean</el-tag>
        </div>
        <span class="lineage-arrow">→</span>
        <div class="lineage-node">
          <span class="lineage-label">Serving 层</span>
          <el-tag effect="plain">{{ ds.name }}</el-tag>
        </div>
      </div>
    </div>

    <div v-if="activeTab === 'quality'" class="tab-content">
      <el-descriptions :column="2" border>
        <el-descriptions-item label="总体质量">正常</el-descriptions-item>
        <el-descriptions-item label="检查规则">3 条规则</el-descriptions-item>
        <el-descriptions-item label="通过">2 条</el-descriptions-item>
        <el-descriptions-item label="警告">1 条</el-descriptions-item>
        <el-descriptions-item label="最近检查">2026-07-10 09:35</el-descriptions-item>
        <el-descriptions-item label="影响 Agent">不影响使用</el-descriptions-item>
      </el-descriptions>
    </div>

    <div v-if="activeTab === 'permission'" class="tab-content">
      <el-descriptions :column="2" border>
        <el-descriptions-item label="可访问角色">管理员、财务部门、销售部门</el-descriptions-item>
        <el-descriptions-item label="可访问部门">财务部、销售部</el-descriptions-item>
        <el-descriptions-item label="字段级限制">phone_number（仅管理员）</el-descriptions-item>
        <el-descriptions-item label="Agent 继承用户权限">是</el-descriptions-item>
      </el-descriptions>
    </div>

    <div v-if="activeTab === 'agent'" class="tab-content">
      <el-descriptions :column="2" border>
        <el-descriptions-item label="Agent 可查询">是</el-descriptions-item>
        <el-descriptions-item label="查询限制">每次最多 10000 行</el-descriptions-item>
        <el-descriptions-item label="敏感字段限制">phone_number 需额外权限</el-descriptions-item>
        <el-descriptions-item label="最近更新">2026-07-10 09:30</el-descriptions-item>
      </el-descriptions>
    </div>

    <div v-if="activeTab === 'semantic'" class="tab-content">
      <Table :columns="semanticColumns" :data="semanticObjects" />
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { useRoute } from 'vue-router'
import { Edit, View } from '@element-plus/icons-vue'
import Index from '@/components/page-header/index.vue'
import TabNav from '@/components/tab-nav/index.vue'
import type { TabItem } from '@/components/tab-nav/index.vue'
import { Table } from '@/components/crud'
import type { ColumnSchema } from '@/components/crud'

const route = useRoute()

const datasetId = route.params.id as string
const datasetName = ref(String(route.params.id || '-'))
const activeTab = ref('desc')

const ds = {
  name: 'sap_sales_orders',
  displayName: '销售订单表',
  source: 'SAP ERP',
  layer: 'Serving',
  records: 1250,
  fields: 24,
  quality: 'pass' as const,
  agentEnabled: true,
  updatedAt: '2026-07-10 09:30',
  description: '来自 SAP ERP 系统的销售订单数据，经过清洗和标准化后进入 Serving 层。包含订单基本信息、金额、客户信息和状态等字段。',
}

const qualityLabel = ({ pass: '质量正常', warning: '质量警告', error: '质量异常' }[ds.quality] ?? ds.quality)

const tabs: TabItem[] = [
  { key: 'desc', label: '数据集说明' },
  { key: 'fields', label: '字段目录' },
  { key: 'lineage', label: '来源和血缘' },
  { key: 'quality', label: '质量状态' },
  { key: 'permission', label: '权限和敏感字段' },
  { key: 'agent', label: 'Agent 使用限制' },
  { key: 'semantic', label: '关联语义对象' },
]

const fieldCatalogData = [
  { fieldName: 'order_id', displayName: '订单编号', type: 'VARCHAR(32)', sensitive: false, sensitiveType: '', quality: 'pass', semanticMapping: '订单.订单编号' },
  { fieldName: 'customer_name', displayName: '客户名称', type: 'VARCHAR(128)', sensitive: false, sensitiveType: '', quality: 'pass', semanticMapping: '客户.客户名称' },
  { fieldName: 'amount', displayName: '订单金额', type: 'DECIMAL(12,2)', sensitive: false, sensitiveType: '', quality: 'pass', semanticMapping: '订单.订单金额' },
  { fieldName: 'phone_number', displayName: '联系电话', type: 'VARCHAR(20)', sensitive: true, sensitiveType: 'PII', quality: 'pass', semanticMapping: '' },
]

const fieldColumns: ColumnSchema[] = [
  { type: 'custom', prop: 'fieldName', label: '字段名', width: 160 },
  { type: 'text', prop: 'displayName', label: '显示名', width: 120 },
  { type: 'text', prop: 'type', label: '类型', width: 120 },
  { type: 'custom', prop: 'sensitive', label: '敏感', width: 80, align: 'center' },
  { type: 'tag', prop: 'quality', label: '质量', width: 80, tagMap: { pass: 'success', warning: 'warning' }, formatter: (v: string) => ({ pass: '正常', warning: '警告' }[v] ?? v) },
  { type: 'text', prop: 'semanticMapping', label: '语义映射', width: 140, formatter: (v: string) => v || '-' },
]

const semanticObjects = [
  { objectName: '订单', relation: '包含', attrCount: 6 },
  { objectName: '客户', relation: '关联', attrCount: 3 },
]

const semanticColumns: ColumnSchema[] = [
  { type: 'text', prop: 'objectName', label: '语义对象', minWidth: 130 },
  { type: 'text', prop: 'relation', label: '关联方式', width: 100 },
  { type: 'text', prop: 'attrCount', label: '关联属性数', width: 110, align: 'center' },
]
</script>

<style lang="scss" scoped>
.summary-row { margin: 0 0 16px; }
.summary-card { padding: 16px; background: #f9fafb; border: 1px solid #e5e7eb; border-radius: 8px; }
.summary-label { font-size: 13px; color: #6b7280; margin-bottom: 4px; }
.summary-value { font-size: 16px; color: #1f2937; font-weight: 500; }
.tab-content { padding-top: 16px; }
.mono { font-family: $font-family-mono; font-size: 13px; color: $color-text-primary; }
.text-muted { color: $color-text-placeholder; font-style: italic; }
.lineage-chain { display: flex; align-items: center; gap: 12px; flex-wrap: wrap; padding: 20px; background: #f9fafb; border: 1px solid $color-border; border-radius: 8px; }
.lineage-node { display: flex; flex-direction: column; align-items: center; gap: 6px; }
.lineage-label { font-size: $font-size-xs; color: $color-text-placeholder; }
.lineage-arrow { font-size: 18px; color: $color-text-placeholder;; font-weight: $font-weight-bold; }
</style>
