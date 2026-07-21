<template>
  <div class="page-layout detail-page">
    <PageHeader
      :title="field?.displayName || fieldName"
      :breadcrumb="[
        { label: '首页', to: '/' },
        { label: '数据表', to: '/tables' },
        { label: tableName, to: `/tables/${tableId}` },
        { label: field?.displayName || fieldName },
      ]"
    >
      <template #tags>
        <el-tag
          v-if="field?.sensitive"
          type="danger"
          effect="plain"
        >{{ field?.sensitiveType }}</el-tag>
        <el-tag
          v-if="field?.isPk"
          type="warning"
          effect="plain"
        >主键</el-tag>
      </template>
      <template #actions>
        <el-button plain @click="router.push(`/tables/${tableId}`)">返回表详情</el-button>
      </template>
    </PageHeader>

    <el-card
      shadow="never"
      class="info-card"
    >
      <template #header><span class="card-header-title">基本信息</span></template>
      <Form
        v-model="formData"
        :sections="infoSections"
        label-width="110px"
      />
    </el-card>

    <el-card
      shadow="never"
      class="sample-card"
    >
      <template #header><span class="card-header-title">示例值采样（前 10 条）</span></template>
      <div
        v-if="samples.length > 0"
        class="sample-list"
      >
        <div
          v-for="(s, si) in samples"
          :key="si"
          class="sample-item"
        >
          <span class="sample-idx">{{ si + 1 }}</span>
          <code class="sample-val">{{ s.value }}</code>
        </div>
      </div>
      <el-empty
        v-else
        description="暂无采样数据"
        :image-size="60"
      />
    </el-card>

    <el-card
      shadow="never"
      class="quality-card"
    >
      <template #header><span class="card-header-title">质量统计</span></template>
      <el-descriptions
        :column="3"
        border
      >
        <el-descriptions-item label="空值率">{{ qualityStats.nullRate }}%</el-descriptions-item>
        <el-descriptions-item label="唯一率">{{ qualityStats.uniqueRate }}%</el-descriptions-item>
        <el-descriptions-item label="空值数量">{{ qualityStats.nullCount.toLocaleString() }}</el-descriptions-item>
        <el-descriptions-item label="非空数量">{{ qualityStats.nonNullCount.toLocaleString() }}</el-descriptions-item>
        <el-descriptions-item label="去重数量">{{ qualityStats.distinctCount.toLocaleString() }}</el-descriptions-item>
        <el-descriptions-item label="总记录数">{{ qualityStats.total.toLocaleString() }}</el-descriptions-item>
      </el-descriptions>
    </el-card>
  </div>
</template>

<script setup lang="ts">
import type { FormSection } from '@/components/crud'
import { reactive, ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import PageHeader from '@/components/page-header/index.vue'
import { Form } from '@/components/crud'

const route = useRoute()
const router = useRouter()
const tableId = route.params.tableId as string
const fieldName = route.params.fieldName as string
const tableName = 'sap_sales_orders'

interface FieldDetail {
  name: string
  displayName: string
  type: string
  description: string
  nullRate: number
  sampleValue: string
  sensitive: boolean
  sensitiveType: string
  isPk: boolean
}

const field = ref<FieldDetail>({
  name: fieldName,
  displayName: '订单编号',
  type: 'VARCHAR(32)',
  description: '销售订单唯一标识',
  nullRate: 0,
  sampleValue: 'SO-2026-001234',
  sensitive: false,
  sensitiveType: '',
  isPk: true,
})

interface FieldFormData {
  name: string
  displayName: string
  type: string
  description: string
  sensitive: string
  isPk: string
}

const formData = reactive<FieldFormData>({
  name: field.value.name,
  displayName: field.value.displayName,
  type: field.value.type,
  description: field.value.description,
  sensitive: field.value.sensitive ? '是' : '否',
  isPk: field.value.isPk ? '是' : '否',
})

const infoSections: FormSection[] = [
  {
    title: '一、基本信息',
    cols: 2,
    fields: [
      {
        type: 'readonly',
        prop: 'name',
        label: '字段名',
      },
      {
        type: 'readonly',
        prop: 'displayName',
        label: '显示名',
      },
      {
        type: 'readonly',
        prop: 'type',
        label: '类型',
      },
      {
        type: 'readonly',
        prop: 'description',
        label: '说明',
      },
      {
        type: 'readonly',
        prop: 'sensitive',
        label: '敏感字段',
      },
      {
        type: 'readonly',
        prop: 'isPk',
        label: '是否主键',
      },
    ],
  },
]

const samples = [
  { value: 'SO-2026-001234' },
  { value: 'SO-2026-001235' },
  { value: 'SO-2026-001236' },
  { value: 'SO-2026-001237' },
  { value: 'SO-2026-001238' },
]

const qualityStats = {
  nullRate: 0,
  uniqueRate: 99.98,
  nullCount: 0,
  nonNullCount: 50000,
  distinctCount: 49990,
  total: 50000,
}
</script>

<style lang="scss" scoped>
.card-header-title {
  font-size: 14px;
  font-weight: 500;
}

.info-card,
.sample-card,
.quality-card {
  margin-bottom: 16px;
}

.sample-list {
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.sample-item {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 6px 0;
  border-bottom: 1px solid #f3f4f6;
}

.sample-idx {
  width: 24px;
  font-size: 12px;
  color: #9ca3af;
  text-align: right;
}

.sample-val {
  padding: 2px 6px;
  border-radius: 4px;
  background: #f3f4f6;
  font-family: 'Consolas', monospace;
  font-size: 13px;
  color: #374151;
}
</style>
