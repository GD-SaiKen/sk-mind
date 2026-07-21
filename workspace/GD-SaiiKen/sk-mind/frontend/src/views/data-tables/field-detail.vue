<template>
  <div class="page-layout detail-page">
    <Index
      :title="`字段: ${field.fieldName}`"
      :breadcrumb="[{ label: '首页', to: '/' }, { label: '数据表', to: '/tables' }, { label: tableName, to: `/tables/${tableId}` }, { label: field.fieldName }]"
    >
      <template #tags>
        <el-tag v-if="field.sensitive" type="danger" effect="plain">{{ field.sensitiveType }}</el-tag>
        <el-tag v-if="field.isPK" type="success" effect="plain">主键</el-tag>
        <el-tag v-if="field.mappedTo" type="" effect="plain">已映射</el-tag>
      </template>
      <template #actions>
        <el-button :icon="Edit">编辑字段说明</el-button>
      </template>
    </Index>

    <el-row class="summary-row" :gutter="16">
      <el-col :span="6"><div class="summary-card"><div class="summary-label">数据类型</div><div class="summary-value mono">{{ field.dataType }}</div></div></el-col>
      <el-col :span="6"><div class="summary-card"><div class="summary-label">空值率</div><div class="summary-value" :class="field.nullRate > 30 ? 'text-danger' : field.nullRate > 10 ? 'text-warning' : ''">{{ field.nullRate }}%</div></div></el-col>
      <el-col :span="6"><div class="summary-card"><div class="summary-label">敏感等级</div><div class="summary-value">{{ field.sensitive ? field.sensitiveType : '普通' }}</div></div></el-col>
      <el-col :span="6"><div class="summary-card"><div class="summary-label">Agent 可查询</div><div class="summary-value">{{ field.allowQuery ? '是' : '否' }}</div></div></el-col>
    </el-row>

    <TabNav v-model="activeTab" :tabs="tabs" />

    <div v-if="activeTab === 'info'" class="tab-content">
      <el-descriptions :column="2" border>
        <el-descriptions-item label="字段名">{{ field.fieldName }}</el-descriptions-item>
        <el-descriptions-item label="显示名">{{ field.fieldDisplayName }}</el-descriptions-item>
        <el-descriptions-item label="数据类型">{{ field.dataType }}</el-descriptions-item>
        <el-descriptions-item label="所属表">{{ tableName }}</el-descriptions-item>
        <el-descriptions-item label="空值率">{{ field.nullRate }}%</el-descriptions-item>
        <el-descriptions-item label="样例值">{{ field.sampleValue }}</el-descriptions-item>
        <el-descriptions-item label="字段说明" :span="2">
          <span v-if="field.fieldComment">{{ field.fieldComment }}</span>
          <span v-else class="text-muted">未填写字段说明</span>
        </el-descriptions-item>
        <el-descriptions-item label="敏感标记">
          <el-tag v-if="field.sensitive" type="danger" effect="plain">{{ field.sensitiveType }}</el-tag>
          <span v-else>普通字段</span>
        </el-descriptions-item>
        <el-descriptions-item label="主键">{{ field.isPK ? '是' : '否' }}</el-descriptions-item>
        <el-descriptions-item label="允许查询">{{ field.allowQuery ? '是' : '否（受控字段）' }}</el-descriptions-item>
        <el-descriptions-item label="语义映射">{{ field.mappedTo || '未映射' }}</el-descriptions-item>
      </el-descriptions>
    </div>

    <div v-if="activeTab === 'quality'" class="tab-content">
      <el-descriptions :column="2" border>
        <el-descriptions-item label="完整性检查">通过</el-descriptions-item>
        <el-descriptions-item label="唯一性检查">{{ field.isPK ? '通过' : '不适用' }}</el-descriptions-item>
        <el-descriptions-item label="格式检查">通过</el-descriptions-item>
        <el-descriptions-item label="枚举检查">不适用</el-descriptions-item>
        <el-descriptions-item label="空值率">{{ field.nullRate }}%</el-descriptions-item>
        <el-descriptions-item label="最近检查">2026-07-10 09:35</el-descriptions-item>
      </el-descriptions>
    </div>

    <div v-if="activeTab === 'usage'" class="tab-content">
      <Table :columns="usageColumns" :data="usageRecords" />
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { useRoute } from 'vue-router'
import { Edit } from '@element-plus/icons-vue'
import Index from '@/components/page-header/index.vue'
import TabNav from '@/components/tab-nav/index.vue'
import type { TabItem } from '@/components/tab-nav/index.vue'
import { Table } from '@/components/crud'
import type { ColumnSchema } from '@/components/crud'

const route = useRoute()

const tableId = route.params.tableId as string || ''
const tableName = (route.query.table as string) || '-'
const activeTab = ref('info')

const field = {
  fieldName: route.params.fieldName as string || '-',
  fieldDisplayName: '订单编号',
  dataType: 'VARCHAR(32)',
  nullRate: 0,
  sampleValue: 'SO-2026-001234',
  fieldComment: '销售订单唯一标识，格式 SO-年份-序号',
  sensitive: false,
  sensitiveType: '',
  isPK: true,
  allowQuery: true,
  mappedTo: '订单.订单编号',
}

const tabs: TabItem[] = [
  { key: 'info', label: '基本信息' },
  { key: 'quality', label: '质量状态' },
  { key: 'usage', label: '使用记录' },
]

const usageRecords = [
  { time: '2026-07-10 09:30', user: '张三', operation: 'Agent 查询', details: 'WHERE order_id = ...' },
  { time: '2026-07-09 14:20', user: '李四', operation: '数据导出', details: 'SELECT order_id, amount...' },
]

const usageColumns: ColumnSchema[] = [
  { type: 'text', prop: 'time', label: '时间', width: 170 },
  { type: 'text', prop: 'user', label: '用户', width: 80 },
  { type: 'text', prop: 'operation', label: '操作', width: 100 },
  { type: 'text', prop: 'details', label: '详情', minWidth: 160 },
]
</script>

<style lang="scss" scoped>
.summary-row { margin: 0 0 16px; }
.summary-card { padding: 16px; background: #f9fafb; border: 1px solid #e5e7eb; border-radius: 8px; }
.summary-label { font-size: 13px; color: #6b7280; margin-bottom: 4px; }
.summary-value { font-size: 16px; color: #1f2937; font-weight: 500; }
.mono { font-family: $font-family-mono; }
.text-danger { color: $color-danger; }
.text-warning { color: $color-warning; }
.text-muted { color: $color-text-placeholder; font-style: italic; }
.tab-content { padding-top: 16px; }
</style>
