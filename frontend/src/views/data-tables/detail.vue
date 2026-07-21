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
            <Table
              :columns="fieldColumns"
              :data="pagedFields"
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
        </Crud>
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
import { computed, reactive, ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { View, Edit } from '@element-plus/icons-vue'
import PageHeader from '@/components/page-header/index.vue'
import { Crud, Table } from '@/components/crud'

const route = useRoute()
const router = useRouter()
const id = route.params.id as string
const activeTab = ref('fields')

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

const table = ref<DataTableDetail>({
  id,
  tableName: 'sap_sales_orders',
  displayName: '销售订单表',
  layer: 'Serving',
  sourceName: 'SAP ERP',
  taskName: 'SAP 销售订单同步',
  recordCount: 1250,
  fieldCount: 24,
  qualityStatus: 'pass',
  agentEnabled: true,
  updatedAt: '2026-07-10 09:30',
})

const summary = computed(() => [
  { label: '来源', value: table.value?.sourceName || '-' },
  { label: '记录数', value: (table.value?.recordCount ?? 0).toLocaleString() },
  { label: '字段数', value: table.value?.fieldCount ?? 0 },
  { label: '更新时间', value: table.value?.updatedAt || '-' },
])

function layerTagType(layer: string) {
  if (layer === 'Serving') return 'success'
  if (layer === 'Clean') return 'warning'
  return ''
}

const sampleColumns = ['order_id', 'customer_name', 'amount', 'order_date']

const sampleData = [
  {
    order_id: 'SO-2026-001234',
    customer_name: '先锋科技股份有限公司',
    amount: '756,200',
    order_date: '2026-06-28',
  },
  {
    order_id: 'SO-2026-001235',
    customer_name: '深圳创新材料集团',
    amount: '623,500',
    order_date: '2026-06-28',
  },
  {
    order_id: 'SO-2026-001236',
    customer_name: '上海精密仪器有限公司',
    amount: '498,800',
    order_date: '2026-06-29',
  },
]

const fieldData = [
  {
    name: 'order_id',
    displayName: '订单编号',
    type: 'VARCHAR(32)',
    nullRate: 0,
    sampleValue: 'SO-2026-001234',
    description: '销售订单唯一标识',
    sensitive: false,
    sensitiveType: '',
    isPk: true,
    agentEnabled: true,
    mappedField: '订单.订单ID',
  },
  {
    name: 'customer_name',
    displayName: '客户名称',
    type: 'VARCHAR(128)',
    nullRate: 0,
    sampleValue: '先锋科技股份有限公司',
    description: '客户企业全称',
    sensitive: false,
    sensitiveType: '',
    isPk: false,
    agentEnabled: true,
    mappedField: '客户.客户名称',
  },
  {
    name: 'amount',
    displayName: '订单金额',
    type: 'DECIMAL(12,2)',
    nullRate: 0.01,
    sampleValue: '756200.00',
    description: '订单总金额(元)',
    sensitive: false,
    sensitiveType: '',
    isPk: false,
    agentEnabled: true,
    mappedField: '订单.订单金额',
  },
  {
    name: 'order_date',
    displayName: '下单日期',
    type: 'DATE',
    nullRate: 0.02,
    sampleValue: '2026-06-28',
    description: '客户下单日期',
    sensitive: false,
    sensitiveType: '',
    isPk: false,
    agentEnabled: true,
    mappedField: '',
  },
  {
    name: 'phone_number',
    displayName: '联系电话',
    type: 'VARCHAR(20)',
    nullRate: 0.05,
    sampleValue: '138****1234',
    description: '客户联系电话',
    sensitive: true,
    sensitiveType: 'PII',
    isPk: false,
    agentEnabled: false,
    mappedField: '',
  },
]

const fieldsPagination = reactive({
  page: 1,
  pageSize: 20,
  total: fieldData.length,
  onPageChange() {},
  onSizeChange() {},
})

const pagedFields = computed(() => fieldData.slice(
  (fieldsPagination.page - 1) * fieldsPagination.pageSize,
  fieldsPagination.page * fieldsPagination.pageSize,
))

const fieldColumns: ColumnSchema[] = [
  {
    type: 'text',
    prop: 'name',
    label: '字段名',
    width: 160,
    showOverflowTooltip: true,
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
    type: 'custom',
    prop: 'nullRate',
    label: '空值率',
    width: 90,
    align: 'center',
  },
  {
    type: 'text',
    prop: 'sampleValue',
    label: '样例值',
    minWidth: 130,
    showOverflowTooltip: true,
  },
  {
    type: 'text',
    prop: 'description',
    label: '字段说明',
    minWidth: 150,
    formatter: (v: string) => v || '-',
  },
  {
    type: 'custom',
    prop: 'sensitive',
    label: '敏感',
    width: 90,
    align: 'center',
  },
  {
    type: 'custom',
    prop: 'isPk',
    label: '主键',
    width: 70,
    align: 'center',
  },
  {
    type: 'custom',
    prop: 'agentEnabled',
    label: 'Agent可用',
    width: 90,
    align: 'center',
  },
  {
    type: 'custom',
    prop: 'mapped',
    label: '已映射',
    width: 130,
  },
]

const qualityRecords = [
  {
    rule: '主键完整性检查',
    time: '2026-06-29 09:35',
    result: '通过',
    issues: 0,
  },
  {
    rule: '订单ID唯一性检查',
    time: '2026-06-29 09:35',
    result: '通过',
    issues: 0,
  },
]

const semanticMappings = [
  {
    field: 'order_id',
    semantic: '订单.订单ID',
    confidence: '高',
  },
  {
    field: 'customer_name',
    semantic: '客户.客户名称',
    confidence: '高',
  },
  {
    field: 'amount',
    semantic: '订单.订单金额',
    confidence: '高',
  },
]

const usageRecords = [
  {
    time: '2026-06-29 10:15',
    user: '张三',
    operation: 'Agent 查询',
    detail: '查询上月销售额前10客户',
  },
  {
    time: '2026-06-28 14:20',
    user: '李四',
    operation: '数据浏览',
    detail: '浏览订单表样例数据',
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
</style>
