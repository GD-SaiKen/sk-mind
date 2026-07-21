<template>
  <div class="page-layout detail-page">
    <PageHeader
      :title="dataset?.displayName || '数据集详情'"
      :breadcrumb="[
        { label: '首页', to: '/' },
        { label: '数据目录', to: '/catalog' },
        { label: dataset?.displayName || '...' },
      ]"
    >
      <template #tags>
        <el-tag
          v-if="dataset"
          effect="plain"
          :type="dataset.quality === 'error' ? 'danger' : dataset.quality === 'warning' ? 'warning' : 'success'"
        >
          {{ dataset.quality === 'error' ? '异常' : dataset.quality === 'warning' ? '警告' : '正常' }}
        </el-tag>
        <el-tag
          v-if="dataset"
          effect="plain"
        >{{ dataset.source }}</el-tag>
      </template>
      <template #actions>
        <el-button plain @click="router.push('/catalog')">返回目录</el-button>
        <el-button
          v-if="dataset?.agentEnabled"
          type="primary"
          @click="router.push('/agent')"
        >问问 Agent</el-button>
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
        label="业务概览"
        name="overview"
      >
        <el-card shadow="never">
          <h3>数据集信息</h3>
          <Form
            v-model="formData"
            :sections="overviewSections"
            label-width="100px"
          />
        </el-card>
      </el-tab-pane>

      <el-tab-pane
        label="字段目录"
        name="fields"
      >
        <el-row
          :gutter="16"
          class="stat-row"
        >
          <el-col :span="6">
            <StatCard
              icon-bg="bg-blue"
              label="字段总数"
              :value="catalogFields.length"
              footer="全部字段"
            />
          </el-col>
          <el-col :span="6">
            <StatCard
              icon-bg="bg-green"
              label="敏感字段"
              :value="sensitiveFieldCount"
              value-color="#dc2626"
              footer="含 PII 等"
            />
          </el-col>
          <el-col :span="6">
            <StatCard
              icon-bg="bg-indigo"
              label="已映射"
              :value="mappedFieldCount"
              value-color="#4f46e5"
              footer="语义映射"
            />
          </el-col>
          <el-col :span="6">
            <StatCard
              icon-bg="bg-purple"
              label="Agent开放"
              :value="agentFieldCount"
              footer="可查询字段"
            />
          </el-col>
        </el-row>
        <Crud :pagination="fieldsPagination">
          <template #table>
            <Table
              :columns="fieldColumns"
              :data="pagedFields"
            >
              <template #col-sensitive="{ row }">
                <el-tag
                  v-if="row.sensitive"
                  type="danger"
                  effect="plain"
                  size="small"
                >{{ row.sensitiveType }}</el-tag>
                <span v-else>-</span>
              </template>
              <template #col-quality="{ row }">
                <el-tag
                  :type="row.quality === 'pass' ? 'success' : 'warning'"
                  effect="plain"
                  size="small"
                >{{ row.quality === 'pass' ? '正常' : '警告' }}</el-tag>
              </template>
            </Table>
          </template>
        </Crud>
      </el-tab-pane>

      <el-tab-pane
        label="质量状态"
        name="quality"
      >
        <el-card shadow="never">
          <h3>最近质量检查</h3>
          <el-empty
            v-if="qualityData.length === 0"
            description="暂无检查记录"
            :image-size="60"
          />
          <el-table
            v-else
            :data="qualityData"
            stripe
          >
            <el-table-column
              prop="rule"
              label="规则"
              min-width="160"
            />
            <el-table-column
              prop="time"
              label="时间"
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
              prop="detail"
              label="详情"
              min-width="200"
            />
          </el-table>
        </el-card>
      </el-tab-pane>

      <el-tab-pane
        label="使用说明"
        name="usage"
      >
        <el-card shadow="never">
          <h3>使用说明</h3>
          <el-descriptions
            :column="1"
            border
            style="max-width: 700px"
          >
            <el-descriptions-item label="业务含义">{{ dataset?.description || '-' }}</el-descriptions-item>
            <el-descriptions-item label="来源系统">{{ dataset?.source || '-' }}</el-descriptions-item>
            <el-descriptions-item label="更新频率">每天 06:00</el-descriptions-item>
            <el-descriptions-item label="数据负责人">{{ dataset?.owner || '-' }}</el-descriptions-item>
            <el-descriptions-item label="访问限制">需权限审批</el-descriptions-item>
          </el-descriptions>
        </el-card>
      </el-tab-pane>
    </el-tabs>
  </div>
</template>

<script setup lang="ts">
import type { ColumnSchema, FormSection } from '@/components/crud'
import { computed, reactive, ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import PageHeader from '@/components/page-header/index.vue'
import StatCard from '@/components/stat-card/index.vue'
import { Crud, Table, Form } from '@/components/crud'

const route = useRoute()
const router = useRouter()
const dsId = route.params.id as string
const activeTab = ref('overview')

interface DatasetDetail {
  id: string
  name: string
  displayName: string
  source: string
  layer: string
  records: number
  fields: number
  quality: string
  agentEnabled: boolean
  updatedAt: string
  description: string
  owner: string
}

const dataset = ref<DatasetDetail>({
  id: dsId,
  name: 'sap_sales_orders',
  displayName: '销售订单表',
  source: 'SAP ERP',
  layer: 'Serving',
  records: 1250,
  fields: 24,
  quality: 'success',
  agentEnabled: true,
  updatedAt: '2026-07-10 09:30',
  description: 'SAP系统中的销售订单数据，包含订单编号、客户名称、金额等信息',
  owner: '张三',
})

const summary = computed(() => [
  { label: '来源系统', value: dataset.value?.source || '-' },
  { label: '记录数', value: (dataset.value?.records ?? 0).toLocaleString() },
  { label: '字段数', value: dataset.value?.fields ?? 0 },
  { label: '更新时间', value: dataset.value?.updatedAt || '-' },
])

const formData = reactive({
  name: dataset.value.name,
  displayName: dataset.value.displayName,
  source: dataset.value.source,
  layer: dataset.value.layer,
  records: (dataset.value.records ?? 0).toLocaleString(),
  fields: String(dataset.value.fields ?? 0),
  description: dataset.value.description,
})

const overviewSections: FormSection[] = [
  {
    cols: 2,
    fields: [
      {
        type: 'readonly',
        prop: 'name',
        label: '表名',
      },
      {
        type: 'readonly',
        prop: 'displayName',
        label: '显示名',
      },
      {
        type: 'readonly',
        prop: 'source',
        label: '来源',
      },
      {
        type: 'readonly',
        prop: 'layer',
        label: '层级',
      },
      {
        type: 'readonly',
        prop: 'records',
        label: '记录数',
      },
      {
        type: 'readonly',
        prop: 'fields',
        label: '字段数',
      },
      {
        type: 'readonly',
        prop: 'description',
        label: '描述',
        colSpan: 2,
      },
    ],
  },
]

const catalogFields = [
  {
    name: 'order_id',
    displayName: '订单编号',
    type: 'VARCHAR(32)',
    sensitive: false,
    sensitiveType: '',
    quality: 'pass',
    meaning: '销售订单唯一标识',
    semanticMapping: '订单.订单ID',
  },
  {
    name: 'customer_name',
    displayName: '客户名称',
    type: 'VARCHAR(128)',
    sensitive: false,
    sensitiveType: '',
    quality: 'pass',
    meaning: '客户企业全称',
    semanticMapping: '客户.客户名称',
  },
  {
    name: 'amount',
    displayName: '订单金额',
    type: 'DECIMAL(12,2)',
    sensitive: false,
    sensitiveType: '',
    quality: 'pass',
    meaning: '订单总金额(元)',
    semanticMapping: '订单.订单金额',
  },
  {
    name: 'phone_number',
    displayName: '联系电话',
    type: 'VARCHAR(20)',
    sensitive: true,
    sensitiveType: 'PII',
    quality: 'pass',
    meaning: '客户联系电话',
    semanticMapping: '',
  },
  {
    name: 'order_date',
    displayName: '下单日期',
    type: 'DATE',
    sensitive: false,
    sensitiveType: '',
    quality: 'warning',
    meaning: '客户下单日期',
    semanticMapping: '',
  },
]

const sensitiveFieldCount = computed(() => catalogFields.filter(f => f.sensitive).length)
const mappedFieldCount = computed(() => catalogFields.filter(f => f.semanticMapping).length)
const agentFieldCount = computed(() => catalogFields.filter(f => !f.sensitive).length)

const fieldsPagination = reactive({
  page: 1,
  pageSize: 20,
  total: catalogFields.length,
  onPageChange() {},
  onSizeChange() {},
})

const pagedFields = computed(() => catalogFields.slice(
  (fieldsPagination.page - 1) * fieldsPagination.pageSize,
  fieldsPagination.page * fieldsPagination.pageSize,
))

const fieldColumns: ColumnSchema[] = [
  {
    type: 'text',
    prop: 'name',
    label: '字段名',
    width: 160,
  },
  {
    type: 'text',
    prop: 'displayName',
    label: '显示名',
    width: 120,
  },
  {
    type: 'text',
    prop: 'type',
    label: '类型',
    width: 130,
  },
  {
    type: 'text',
    prop: 'meaning',
    label: '字段含义',
    minWidth: 160,
  },
  {
    type: 'custom',
    prop: 'sensitive',
    label: '敏感',
    width: 80,
    align: 'center',
  },
  {
    type: 'custom',
    prop: 'quality',
    label: '质量',
    width: 80,
    align: 'center',
  },
  {
    type: 'text',
    prop: 'semanticMapping',
    label: '语义映射',
    width: 140,
    formatter: (v: string) => v || '-',
  },
]

const qualityData = [
  {
    rule: '主键完整性检查',
    time: '2026-06-29 09:35',
    result: '通过',
    detail: 'order_id 字段无重复、无空值',
  },
  {
    rule: '订单ID唯一性检查',
    time: '2026-06-29 09:35',
    result: '通过',
    detail: '全部订单ID唯一',
  },
]
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

.stat-row {
  margin-bottom: 16px;

  :deep(.el-col) {
    padding-left: 8px !important;
    padding-right: 8px !important;
  }

  :deep(.el-col:first-child) {
    padding-left: 0 !important;
  }

  :deep(.el-col:last-child) {
    padding-right: 0 !important;
  }
}

h3 {
  font-size: 16px;
  margin: 0 0 16px;
  color: #1f2937;
}
</style>
