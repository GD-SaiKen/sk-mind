<template>
  <div class="page-layout detail-page">
    <PageHeader
      :title="`批次详情`"
      :breadcrumb="[
        { label: '首页', to: '/' },
        { label: '接入任务', to: '/ingestion' },
        { label: taskName, to: `/ingestion/${taskId}` },
        { label: '批次详情' },
      ]"
    >
      <template #tags>
        <el-tag
          :type="batchTypeMap[batch?.status ?? '']"
          effect="plain"
        >{{ batchStatusLabel[batch?.status ?? ''] }}</el-tag>
      </template>
      <template #actions>
        <el-button @click="router.push(`/ingestion/${taskId}`)">返回任务详情</el-button>
      </template>
    </PageHeader>

    <div
      v-if="loading"
      class="loading-wrap"
    ><el-skeleton :rows="6" /></div>
    <el-empty
      v-else-if="!batch"
      description="批次不存在"
    />

    <template v-else>
      <el-row
        :gutter="16"
        class="summary-row"
      >
        <el-col :span="6">
          <div class="summary-card">
            <div class="s-label">执行时间</div>
            <div class="s-value">{{ fmtDateTime(batch.startedAt) || '-' }}</div>
          </div>
        </el-col>
        <el-col :span="6">
          <div class="summary-card">
            <div class="s-label">触发方式</div>
            <div class="s-value">{{ triggerLabel[batch.triggerType] ?? batch.triggerType }}</div>
          </div>
        </el-col>
        <el-col :span="6">
          <div class="summary-card">
            <div class="s-label">耗时</div>
            <div class="s-value">{{ duration }}</div>
          </div>
        </el-col>
      </el-row>

      <el-row
        :gutter="16"
        class="summary-row"
      >
        <el-col :span="6">
          <div class="summary-card">
            <div class="s-label">成功数量</div>
            <div class="s-value s-ok">{{ (batch.successCount ?? 0).toLocaleString() }}</div>
          </div>
        </el-col>
        <el-col :span="6">
          <div class="summary-card">
            <div class="s-label">失败数量</div>
            <div class="s-value s-err">{{ (batch.failCount ?? 0).toLocaleString() }}</div>
          </div>
        </el-col>
        <el-col :span="6">
          <div class="summary-card">
            <div class="s-label">跳过数量</div>
            <div class="s-value s-warn">{{ (batch.skipCount ?? 0).toLocaleString() }}</div>
          </div>
        </el-col>
        <el-col :span="6">
          <div class="summary-card">
            <div class="s-label">总记录数</div>
            <div class="s-value">{{ (batch.recordCount ?? 0).toLocaleString() }}</div>
          </div>
        </el-col>
      </el-row>

      <el-card
        v-if="batch.errorSummary"
        shadow="never"
        class="error-card"
      >
        <template #header><span class="card-header-title">错误原因</span></template>
        <el-alert
          :title="batch.errorSummary"
          type="error"
          :closable="false"
          show-icon
        />
      </el-card>

      <el-card
        shadow="never"
        class="error-list-card"
      >
        <template #header><span class="card-header-title">错误清单</span></template>
        <el-empty
          v-if="errorList.length === 0"
          description="无错误记录"
          :image-size="60"
        />
        <Table
          v-else
          :columns="errorColumns"
          :data="errorList"
        />
      </el-card>
    </template>
  </div>
</template>

<script setup lang="ts">
import type { IngestionBatch, ImportError } from '@/api'
import type { ColumnSchema } from '@/components/crud'
import { computed, onMounted, ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { ingestionService } from '@/api'
import PageHeader from '@/components/page-header/index.vue'
import { Table } from '@/components/crud'
import { fmtDateTime } from '@/utils/datetime'

const route = useRoute()
const router = useRouter()
const taskId = route.params.taskId as string
const batchId = route.params.batchId as string

const loading = ref(true)
const batch = ref<IngestionBatch | null>(null)
const errorList = ref<ImportError[]>([])
const taskName = ref('...')

const batchStatusLabel: Record<string, string> = {
  pending: '等待中',
  running: '运行中',
  success: '成功',
  partial_success: '部分成功',
  failed: '失败',
  cancelled: '已取消',
}

const batchTypeMap: Record<string, '' | 'success' | 'warning' | 'danger' | 'info'> = {
  pending: 'info',
  running: '',
  success: 'success',
  partial_success: 'warning',
  failed: 'danger',
  cancelled: 'info',
}

const triggerLabel: Record<string, string> = {
  manual: '手动',
  scheduled: '定时',
  retry: '重试',
  backfill: '全量回溯',
  quick_fill: '快补',
}

const duration = computed(() => {
  if (!batch.value?.startedAt || !batch.value?.finishedAt) return '-'
  const s = (new Date(batch.value.finishedAt).getTime() - new Date(batch.value.startedAt).getTime()) / 1000
  if (s < 60) return `${s.toFixed(0)}s`
  return `${Math.floor(s / 60)}m${(s % 60).toFixed(0)}s`
})

const errorColumns: ColumnSchema[] = [
  {
    type: 'text',
    prop: 'errorType',
    label: '错误类型',
    width: 120,
  },
  {
    type: 'text',
    prop: 'errorMessage',
    label: '错误信息',
    minWidth: 250,
  },
  {
    type: 'text',
    prop: 'fieldName',
    label: '字段',
    width: 120,
    formatter: (v: string) => v || '-',
  },
  {
    type: 'text',
    prop: 'rowNumber',
    label: '行号',
    width: 80,
    align: 'center',
    formatter: (v: number) => v ? String(v) : '-',
  },
  {
    type: 'text',
    prop: 'createdAt',
    label: '时间',
    width: 170,
    formatter: (v: string) => fmtDateTime(v) || '-',
  },
]

onMounted(async () => {
  try {
    const [task, batchData, batchErr] = await Promise.all([
      ingestionService.get(taskId).catch(() => null),
      ingestionService.getBatch(batchId).catch(() => null),
      ingestionService.getBatchErrors(batchId, { pageSize: 100 }).catch(() => ({ items: [] })),
    ])
    if (task) taskName.value = task.name
    batch.value = batchData
    errorList.value = batchErr.items ?? []
  } finally {
    loading.value = false
  }
})
</script>

<style lang="scss" scoped>
.loading-wrap {
  padding: 40px;
}

.summary-row {
  margin-bottom: 16px;
}

.summary-card {
  padding: 16px;
  background: #f9fafb;
  border: 1px solid #e5e7eb;
  border-radius: 8px;
}

.s-label {
  font-size: 13px;
  color: #6b7280;
  margin-bottom: 4px;
}

.s-value {
  font-size: 14px;
  font-weight: 500;
  color: #1f2937;
}

.s-ok {
  color: #16a34a;
}

.s-err {
  color: #dc2626;
}

.s-warn {
  color: #ca8a04;
}

.error-card {
  margin-bottom: 16px;
}

.error-list-card {
  margin-bottom: 16px;
}

.card-header-title {
  font-size: 14px;
  font-weight: 500;
}
</style>
