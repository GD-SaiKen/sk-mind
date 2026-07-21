<template>
  <div class="page-layout detail-page">
    <Index
      :title="tableName"
      :breadcrumb="[{ label: '首页', to: '/' }, { label: '数据表', to: '/tables' }, { label: tableName }]"
    >
      <template #tags>
        <el-tag effect="plain" :type="table.layer === 'Serving' ? 'success' : table.layer === 'Clean' ? 'warning' : ''">{{ table.layer }}</el-tag>
        <el-tag :type="qualityTagType" effect="plain">{{ qualityLabel }}</el-tag>
        <el-tag :type="table.agentEnabled ? 'success' : 'info'" effect="plain">{{ table.agentEnabled ? 'Agent 可用' : '未开放' }}</el-tag>
      </template>
      <template #actions>
        <el-button :icon="Edit" plain @click="router.push(`/tables/${tableId}/field` + '?table=' + tableName)">编辑说明</el-button>
        <el-button :icon="Connection" plain>建立映射</el-button>
      </template>
    </Index>

    <el-row class="summary-row" :gutter="16">
      <el-col :span="6"><div class="summary-card"><div class="summary-label">来源数据源</div><div class="summary-value">{{ table.sourceName }}</div></div></el-col>
      <el-col :span="6"><div class="summary-card"><div class="summary-label">记录数</div><div class="summary-value">{{ table.recordCount?.toLocaleString() ?? '-' }}</div></div></el-col>
      <el-col :span="6"><div class="summary-card"><div class="summary-label">字段数</div><div class="summary-value">{{ table.fieldCount }}</div></div></el-col>
      <el-col :span="6"><div class="summary-card"><div class="summary-label">更新时间</div><div class="summary-value">{{ table.updatedAt }}</div></div></el-col>
    </el-row>

    <TabNav v-model="activeTab" :tabs="tabs" />

    <!-- 样例数据 -->
    <div v-if="activeTab === 'sample'" class="tab-content">
      <Table v-if="sampleData.length > 0" :columns="sampleColumns" :data="sampleData" />
      <div v-else class="empty">暂无样例数据</div>
    </div>

    <!-- 字段列表 -->
    <div v-if="activeTab === 'fields'" class="tab-content">
      <div class="toolbar">
        <el-input v-model="fieldSearch" placeholder="搜索字段名或说明..." :prefix-icon="Search" style="width:240px" clearable />
        <div class="spacer" />
        <el-button :icon="Plus">批量补充说明</el-button>
        <el-button :icon="Delete">批量标记敏感</el-button>
      </div>
      <Table :columns="fieldColumns" :data="filteredFields">
        <template #col-fieldName="{ row }">
          <span class="mono">{{ row.fieldName }}</span>
        </template>
        <template #col-fieldDisplayName="{ row }">
          <div>{{ row.fieldDisplayName }}</div>
          <div v-if="row.fieldComment" class="row-sub">{{ row.fieldComment }}</div>
          <div v-else class="row-sub-muted">未填写字段说明</div>
        </template>
        <template #col-nullRate="{ row }">
          <div class="null-cell">
            <el-progress :percentage="row.nullRate" :stroke-width="4" :show-text="false" :color="row.nullRate > 30 ? '#dc2626' : row.nullRate > 10 ? '#ca8a04' : '#16a34a'" />
            <span class="null-text" :class="row.nullRate > 30 ? 'text-danger' : row.nullRate > 10 ? 'text-warning' : ''">{{ row.nullRate }}%</span>
          </div>
        </template>
        <template #col-sensitive="{ row }">
          <el-tag v-if="row.sensitive" type="danger" effect="plain" size="small">{{ row.sensitiveType }}</el-tag>
          <span v-else>—</span>
        </template>
        <template #col-actions="{ row }">
          <div class="action-btns">
            <el-button link type="primary" @click="router.push(`/tables/${tableId}/field/${row.fieldName}?table=${tableName}`)">详情</el-button>
          </div>
        </template>
      </Table>
    </div>

    <!-- 来源和批次 -->
    <div v-if="activeTab === 'source'" class="tab-content">
      <el-descriptions :column="2" border>
        <el-descriptions-item label="来源数据源">{{ table.sourceName }}</el-descriptions-item>
        <el-descriptions-item label="最近批次">BATCH-20260710-0001</el-descriptions-item>
        <el-descriptions-item label="层级">{{ table.layer }}</el-descriptions-item>
        <el-descriptions-item label="接入方式">数据库同步</el-descriptions-item>
        <el-descriptions-item label="创建时间">2026-06-01 10:00</el-descriptions-item>
        <el-descriptions-item label="最近更新">{{ table.updatedAt }}</el-descriptions-item>
      </el-descriptions>
    </div>

    <!-- 质量结果 -->
    <div v-if="activeTab === 'quality'" class="tab-content">
      <div class="stat-grid">
        <StatCard :icon="CircleCheckFilled" icon-bg="bg-green" label="通过" :value="passRules" value-class="green" footer-text="已通过的质量规则" />
        <StatCard :icon="WarningFilled" icon-bg="bg-yellow" label="警告" :value="warnRules" value-class="yellow" footer-text="待处理的质量问题" />
        <StatCard :icon="CircleCloseFilled" icon-bg="bg-red" label="异常" :value="errRules" value-class="red" footer-text="需立即修复" />
        <StatCard :icon="Setting" icon-bg="bg-blue" label="规则总数" :value="qualityChecks.length" footer-text="已配置的质量规则" />
      </div>
      <Table :columns="qualityColumns" :data="qualityChecks" style="margin-top: 16px">
        <template #col-ruleName="{ row }">
          <router-link :to="`/quality`" class="link">{{ row.ruleName }}</router-link>
        </template>
      </Table>
    </div>

    <!-- 权限 -->
    <div v-if="activeTab === 'permission'" class="tab-content">
      <el-descriptions :column="2" border>
        <el-descriptions-item label="可访问角色">管理员、财务部门、销售部门</el-descriptions-item>
        <el-descriptions-item label="Agent 继承权限">是</el-descriptions-item>
        <el-descriptions-item label="字段级限制">
          <el-tag v-for="f in ['phone_number', 'bank_account']" :key="f" type="danger" effect="plain" size="small" style="margin-right:4px">{{ f }}</el-tag>
        </el-descriptions-item>
        <el-descriptions-item label="最近变更">管理员 · 2026-06-15</el-descriptions-item>
      </el-descriptions>
    </div>

    <!-- 语义映射 -->
    <div v-if="activeTab === 'mapping'" class="tab-content">
      <Table :columns="mappingColumns" :data="semanticMappings" />
    </div>

    <!-- 使用记录 -->
    <div v-if="activeTab === 'usage'" class="tab-content">
      <Table :columns="usageColumns" :data="usageRecords" />
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed, ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { CircleCheckFilled, CircleCloseFilled, Connection, Delete, Edit, Grid, Plus, Search, Setting, WarningFilled } from '@element-plus/icons-vue'
import Index from '@/components/page-header/index.vue'
import TabNav from '@/components/tab-nav/index.vue'
import type { TabItem } from '@/components/tab-nav/index.vue'
import StatCard from '@/components/stat-card/index.vue'
import { Table } from '@/components/crud'
import type { ColumnSchema } from '@/components/crud'

const route = useRoute()
const router = useRouter()

const tableId = route.params.id as string
const tableName = ref(String(route.params.id || '-'))
const activeTab = ref('fields')
const fieldSearch = ref('')

const table = reactive({
  layer: 'Serving',
  sourceName: 'SAP ERP',
  recordCount: 1250,
  fieldCount: 24,
  agentEnabled: true,
  updatedAt: '2026-07-10 09:30',
  qualityStatus: 'pass',
})

import { reactive } from 'vue'

const qualityTagType = computed(() => {
  const m: Record<string, '' | 'success' | 'warning' | 'danger'> = { pass: 'success', warning: 'warning', error: 'danger' }
  return m[table.qualityStatus] ?? 'info'
})
const qualityLabel = computed(() => ({ pass: '质量正常', warning: '质量警告', error: '质量异常' }[table.qualityStatus] ?? table.qualityStatus))

const tabs: TabItem[] = [
  { key: 'sample', label: '样例数据' },
  { key: 'fields', label: '字段列表' },
  { key: 'source', label: '来源和批次' },
  { key: 'quality', label: '质量结果' },
  { key: 'permission', label: '权限' },
  { key: 'mapping', label: '语义映射' },
  { key: 'usage', label: '使用记录' },
]

const sampleData = [
  { order_id: 'SO-2026-001234', customer_name: '先锋科技', amount: '756,200', order_date: '2026-06-15', status: '已发货' },
  { order_id: 'SO-2026-001235', customer_name: '深圳创新材料', amount: '623,500', order_date: '2026-06-16', status: '生产中' },
  { order_id: 'SO-2026-001236', customer_name: '上海精密仪器', amount: '498,800', order_date: '2026-06-17', status: '待审批' },
]

const sampleColumns: ColumnSchema[] = [
  { type: 'text', prop: 'order_id', label: '订单编号', minWidth: 160 },
  { type: 'text', prop: 'customer_name', label: '客户名称', minWidth: 130 },
  { type: 'text', prop: 'amount', label: '金额', width: 100 },
  { type: 'text', prop: 'order_date', label: '日期', width: 110 },
  { type: 'tag', prop: 'status', label: '状态', width: 80, tagMap: { '已发货': 'success', '生产中': 'warning', '待审批': 'info' } },
]

interface TableField {
  fieldName: string; fieldDisplayName: string; dataType: string; nullRate: number
  sampleValue: string; fieldComment: string; sensitive: boolean; sensitiveType: string
  isPK: boolean; allowQuery: boolean; mappedTo: string
}

const fields: TableField[] = [
  { fieldName: 'order_id', fieldDisplayName: '订单编号', dataType: 'VARCHAR(32)', nullRate: 0, sampleValue: 'SO-2026-001234', fieldComment: '销售订单唯一标识，格式 SO-年份-序号', sensitive: false, sensitiveType: '', isPK: true, allowQuery: true, mappedTo: '订单.订单编号' },
  { fieldName: 'customer_name', fieldDisplayName: '客户名称', dataType: 'VARCHAR(128)', nullRate: 0, sampleValue: '先锋科技股份有限公司', fieldComment: '下单客户企业全称', sensitive: false, sensitiveType: '', isPK: false, allowQuery: true, mappedTo: '客户.客户名称' },
  { fieldName: 'amount', fieldDisplayName: '订单金额', dataType: 'DECIMAL(12,2)', nullRate: 2.5, sampleValue: '756200.00', fieldComment: '订单总金额（含税）', sensitive: false, sensitiveType: '', isPK: false, allowQuery: true, mappedTo: '订单.订单金额' },
  { fieldName: 'order_date', fieldDisplayName: '下单日期', dataType: 'DATETIME', nullRate: 0, sampleValue: '2026-06-15 09:30:00', fieldComment: '客户下单时间', sensitive: false, sensitiveType: '', isPK: false, allowQuery: true, mappedTo: '订单.下单日期' },
  { fieldName: 'phone_number', fieldDisplayName: '联系电话', dataType: 'VARCHAR(20)', nullRate: 5, sampleValue: '138xxxx5678', fieldComment: '', sensitive: true, sensitiveType: 'PII', isPK: false, allowQuery: true, mappedTo: '' },
  { fieldName: 'status', fieldDisplayName: '订单状态', dataType: 'VARCHAR(20)', nullRate: 0, sampleValue: '已发货', fieldComment: '订单当前业务状态', sensitive: false, sensitiveType: '', isPK: false, allowQuery: true, mappedTo: '订单.订单状态' },
  { fieldName: 'remark', fieldDisplayName: '备注', dataType: 'TEXT', nullRate: 85, sampleValue: '(NULL)', fieldComment: '订单特殊备注信息', sensitive: false, sensitiveType: '', isPK: false, allowQuery: false, mappedTo: '' },
]

const filteredFields = computed(() => {
  if (!fieldSearch.value) return fields
  const s = fieldSearch.value.toLowerCase()
  return fields.filter(f => f.fieldName.toLowerCase().includes(s) || f.fieldDisplayName.includes(s) || f.fieldComment.includes(s))
})

const fieldColumns: ColumnSchema[] = [
  { type: 'custom', prop: 'fieldName', label: '字段名', width: 160 },
  { type: 'custom', prop: 'fieldDisplayName', label: '字段说明', minWidth: 200 },
  { type: 'text', prop: 'dataType', label: '类型', width: 120 },
  { type: 'custom', prop: 'nullRate', label: '空值率', width: 140 },
  { type: 'text', prop: 'sampleValue', label: '样例值', width: 150 },
  { type: 'custom', prop: 'sensitive', label: '敏感', width: 80, align: 'center' },
  { type: 'tag', prop: 'isPK', label: '主键', width: 70, formatter: (v: boolean) => v ? '是' : '否', tagMap: { true: 'success' } } as ColumnSchema,
  { type: 'tag', prop: 'allowQuery', label: '可查询', width: 80, formatter: (v: boolean) => v ? '是' : '否', tagMap: { true: 'success', false: 'info' } } as ColumnSchema,
  { type: 'text', prop: 'mappedTo', label: '语义映射', width: 140, formatter: (v: string) => v || '-' },
  { type: 'custom', prop: 'actions', label: '操作', width: 80 },
]

const qualityChecks = [
  { ruleName: '主键完整性检查', type: '完整性', result: '通过', lastRun: '2026-07-10 09:35' },
  { ruleName: '订单ID唯一性检查', type: '唯一性', result: '通过', lastRun: '2026-07-10 09:35' },
  { ruleName: '金额格式检查', type: '格式', result: '警告', lastRun: '2026-07-10 09:35' },
]

const qualityColumns: ColumnSchema[] = [
  { type: 'custom', prop: 'ruleName', label: '规则名称', minWidth: 160 },
  { type: 'tag', prop: 'type', label: '类型', width: 100 },
  { type: 'tag', prop: 'result', label: '结果', width: 80, tagMap: { '通过': 'success', '警告': 'warning' } },
  { type: 'text', prop: 'lastRun', label: '最近执行', width: 170 },
]

const passRules = 2
const warnRules = 1
const errRules = 0

const semanticMappings = [
  { semantic: '订单.订单编号', sourceField: 'order_id', transform: '直接映射', confidence: '高', status: '已确认' },
  { semantic: '客户.客户名称', sourceField: 'customer_name', transform: '直接映射', confidence: '高', status: '已确认' },
  { semantic: '订单.订单金额', sourceField: 'amount', transform: '直接映射', confidence: '高', status: '已确认' },
]

const mappingColumns: ColumnSchema[] = [
  { type: 'text', prop: 'semantic', label: '语义对象/属性', minWidth: 160 },
  { type: 'text', prop: 'sourceField', label: '来源字段', width: 140 },
  { type: 'text', prop: 'transform', label: '转换方式', width: 100 },
  { type: 'tag', prop: 'confidence', label: '可信度', width: 80, tagMap: { '高': 'success', '中': 'warning', '低': 'info' } },
  { type: 'tag', prop: 'status', label: '状态', width: 80, tagMap: { '已确认': 'success', '待确认': 'warning' } },
]

const usageRecords = [
  { time: '2026-07-10 09:30', user: '张三', operation: 'Agent 查询', details: '查询销售额Top 10', result: '成功' },
  { time: '2026-07-09 14:20', user: '李四', operation: '数据导出', details: '导出 500 条记录', result: '成功' },
]

const usageColumns: ColumnSchema[] = [
  { type: 'text', prop: 'time', label: '时间', width: 170 },
  { type: 'text', prop: 'user', label: '用户', width: 80 },
  { type: 'text', prop: 'operation', label: '操作', width: 100 },
  { type: 'text', prop: 'details', label: '详情', minWidth: 160 },
  { type: 'tag', prop: 'result', label: '结果', width: 80, tagMap: { '成功': 'success' } },
]
</script>

<style lang="scss" scoped>
.summary-row { margin: 0 0 16px; }
.summary-card { padding: 16px; background: #f9fafb; border: 1px solid #e5e7eb; border-radius: 8px; }
.summary-label { font-size: 13px; color: #6b7280; margin-bottom: 4px; }
.summary-value { font-size: 16px; color: #1f2937; font-weight: 500; }

.tab-content { padding-top: 16px; }

.toolbar { display: flex; align-items: center; gap: 8px; margin-bottom: 12px; }
.spacer { flex: 1; }

.stat-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 16px; }
:deep(.bg-green) { background: #dcfce7; color: $color-success; }
:deep(.bg-yellow) { background: #fef3c7; color: $color-warning; }
:deep(.bg-red) { background: #fee2e2; color: $color-danger; }
:deep(.bg-blue) { background: #dbeafe; color: $color-primary; }

.green { color: $color-success; }
.yellow { color: $color-warning; }
.red { color: $color-danger; }

.mono { font-family: $font-family-mono; font-size: 13px; color: $color-text-primary; }
.row-sub { font-size: 11px; color: $color-text-placeholder; margin-top: 2px; }
.row-sub-muted { font-size: 11px; color: $color-text-placeholder; margin-top: 2px; font-style: italic; }

.null-cell { display: flex; align-items: center; gap: 8px; }
.null-text { font-size: 12px; font-weight: 500; }
.text-danger { color: $color-danger; }
.text-warning { color: $color-warning; }

.action-btns { display: flex; gap: 4px; }

.link { color: $color-primary; text-decoration: none; &:hover { text-decoration: underline; } }

.empty { text-align: center; padding: 60px; color: $color-text-placeholder; font-size: 14px; }
</style>
