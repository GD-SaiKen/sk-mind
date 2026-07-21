<template>
  <div class="page-layout detail-page">
    <PageHeader
      :title="`质量规则详情`"
      :breadcrumb="[
        { label: '首页', to: '/' },
        { label: '数据质量', to: '/quality' },
        { label: '规则详情' },
      ]"
    >
      <template #tags>
        <el-tag
          :type="rule?.status === 'success' ? 'success' : rule?.status === 'warning' ? 'warning' : 'danger'"
          effect="plain"
        >
          {{ rule?.status === 'success' ? '通过' : rule?.status === 'warning' ? '警告' : '异常' }}
        </el-tag>
      </template>
      <template #actions>
        <el-button plain @click="router.push('/quality')">返回质量列表</el-button>
        <el-button
          type="primary"
          @click="ElMessage.info('执行已提交')"
        >立即执行</el-button>
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
        label="总体状态"
        name="status"
      >
        <el-card shadow="never">
          <h3>检测结果</h3>
          <Form
            v-model="formData"
            :sections="infoSections"
            label-width="110px"
          />
        </el-card>
      </el-tab-pane>

      <el-tab-pane
        label="问题分布"
        name="issues"
      >
        <el-row
          :gutter="16"
          class="stat-row"
        >
          <el-col :span="6">
            <StatCard
              icon-bg="bg-red"
              label="问题总数"
              :value="issues.length"
              value-color="#dc2626"
              footer="本次检查发现问题"
            />
          </el-col>
          <el-col :span="6">
            <StatCard
              icon-bg="bg-yellow"
              label="空值问题"
              :value="nullIssues"
              footer="完整性检查"
            />
          </el-col>
          <el-col :span="6">
            <StatCard
              icon-bg="bg-orange"
              label="格式问题"
              :value="formatIssues"
              footer="格式检查"
            />
          </el-col>
          <el-col :span="6">
            <StatCard
              icon-bg="bg-blue"
              label="重复问题"
              :value="dupIssues"
              footer="唯一性检查"
            />
          </el-col>
        </el-row>
        <Crud :pagination="issuesPagination">
          <template #table>
            <Table
              :columns="issuesColumns"
              :data="pagedIssues"
            />
          </template>
        </Crud>
      </el-tab-pane>

      <el-tab-pane
        label="最近检查记录"
        name="records"
      >
        <el-card shadow="never">
          <h3>执行历史</h3>
          <el-table
            :data="checkRecords"
            stripe
          >
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
              prop="total"
              label="检测数"
              width="80"
            />
            <el-table-column label="问题数">
              <template #default="{ row }">
                <span :style="{ color: row.issues > 0 ? '#dc2626' : '' }">{{ row.issues }}</span>
              </template>
            </el-table-column>
            <el-table-column
              prop="duration"
              label="耗时"
              width="80"
            />
          </el-table>
        </el-card>
      </el-tab-pane>

      <el-tab-pane
        label="影响分析"
        name="impact"
      >
        <el-card shadow="never">
          <h3>影响范围分析</h3>
          <el-alert
            title="Agent 查询影响"
            :type="rule?.status === 'success' ? 'success' : 'warning'"
            :closable="false"
            show-icon
            style="margin-bottom: 16px"
          >
            <template #default>
              <p>{{ impactDescription }}</p>
            </template>
          </el-alert>
          <el-descriptions
            :column="2"
            border
            style="max-width: 600px"
          >
            <el-descriptions-item label="影响数据集">{{ rule?.dataset || '-' }}</el-descriptions-item>
            <el-descriptions-item label="影响字段">{{ impactedFields }}</el-descriptions-item>
            <el-descriptions-item label="Agent 可用性">{{ rule?.status === 'success' ? '正常查询' : '结果可能缺失' }}</el-descriptions-item>
            <el-descriptions-item label="数据负责人">{{ rule?.owner || '-' }}</el-descriptions-item>
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
import { ElMessage } from 'element-plus'
import PageHeader from '@/components/page-header/index.vue'
import StatCard from '@/components/stat-card/index.vue'
import { Crud, Table, Form } from '@/components/crud'

const route = useRoute()
const router = useRouter()
const qId = route.params.id as string
const activeTab = ref('status')

interface QualityRule {
  id: string
  name: string
  type: string
  dataset: string
  status: string
  lastRun: string
  owner?: string
}

const rule = ref<QualityRule>({
  id: qId,
  name: '考勤时间空值检查',
  type: '完整性',
  dataset: '每日考勤表',
  status: 'warning',
  lastRun: '2026-06-28 18:05',
  owner: '李敏',
})

const summary = computed(() => [
  { label: '规则类型', value: rule.value?.type || '-' },
  { label: '适用数据集', value: rule.value?.dataset || '-' },
  { label: '最近执行', value: rule.value?.lastRun || '-' },
  { label: '负责人', value: rule.value?.owner || '-' },
])

const formData = reactive({
  name: rule.value.name,
  type: rule.value.type,
  dataset: rule.value.dataset,
  lastRun: rule.value.lastRun,
  status: rule.value.status === 'success' ? '通过' : rule.value.status === 'warning' ? '警告(5条空值)' : '异常',
})

const infoSections: FormSection[] = [
  {
    cols: 2,
    fields: [
      {
        type: 'readonly',
        prop: 'name',
        label: '规则名称',
      },
      {
        type: 'readonly',
        prop: 'type',
        label: '规则类型',
      },
      {
        type: 'readonly',
        prop: 'dataset',
        label: '适用数据集',
      },
      {
        type: 'readonly',
        prop: 'lastRun',
        label: '最近执行',
      },
      {
        type: 'readonly',
        prop: 'status',
        label: '状态',
        colSpan: 2,
      },
    ],
  },
]

const issues = [
  {
    field: 'check_in_time',
    type: '空值',
    count: 3,
    sample: 'NULL',
    description: '3条考勤记录的签到时间为空',
  },
  {
    field: 'check_out_time',
    type: '空值',
    count: 2,
    sample: 'NULL',
    description: '2条考勤记录的签退时间为空',
  },
]

const nullIssues = computed(() => issues.filter(i => i.type === '空值').length)
const formatIssues = computed(() => issues.filter(i => i.type === '格式异常').length)
const dupIssues = computed(() => issues.filter(i => i.type === '重复').length)

const issuesPagination = reactive({
  page: 1,
  pageSize: 20,
  total: issues.length,
  onPageChange() {},
  onSizeChange() {},
})

const pagedIssues = computed(() => issues.slice(
  (issuesPagination.page - 1) * issuesPagination.pageSize,
  issuesPagination.page * issuesPagination.pageSize,
))

const issuesColumns: ColumnSchema[] = [
  {
    type: 'text',
    prop: 'field',
    label: '字段',
    width: 160,
  },
  {
    type: 'tag',
    prop: 'type',
    label: '类型',
    width: 100,
    tagType: 'danger',
  },
  {
    type: 'text',
    prop: 'count',
    label: '数量',
    width: 80,
    align: 'center',
  },
  {
    type: 'text',
    prop: 'sample',
    label: '样例值',
    width: 120,
  },
  {
    type: 'text',
    prop: 'description',
    label: '说明',
    minWidth: 200,
  },
]

const checkRecords = [
  {
    time: '2026-06-28 18:05',
    result: '发现问题',
    total: 320,
    issues: 5,
    duration: '2s',
  },
  {
    time: '2026-06-27 18:05',
    result: '发现问题',
    total: 320,
    issues: 3,
    duration: '1s',
  },
  {
    time: '2026-06-26 18:05',
    result: '通过',
    total: 320,
    issues: 0,
    duration: '1s',
  },
]

const impactedFields = 'check_in_time, check_out_time'
const impactDescription = rule.value?.status === 'success'
  ? '数据质量正常，Agent 查询结果完整可靠'
  : '存在 5 条空值记录，Agent 查询结果可能缺少部分数据，建议尽快处理'
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
