﻿<template>
  <div class="quality-page">
    <!-- 标签页 -->
    <div class="tab-bar">
      <button
        v-for="tab in tabs" :key="tab.key" class="tab-btn"
        :class="{ active: activeTab === tab.key }" @click="activeTab = tab.key"
      >{{ tab.label }}<span v-if="tab.count" class="tab-count">{{ tab.count }}</span></button>
    </div>

    <!-- 统计卡片 -->
    <el-row :gutter="16" class="stat-row">
      <el-col :span="6">
        <el-card shadow="never" class="info-card">
          <div class="info-card-header">
            <div class="info-card-icon bg-green"><el-icon :size="16"><CircleCheckFilled /></el-icon></div>
            <span class="info-card-label">质量通过</span>
            <span class="info-card-subtag">状态良好</span>
          </div>
          <div class="info-card-value-row">
            <span class="info-card-value green">{{ throughCount }}</span>
            <span class="badge green-bg">↑ 较昨日</span>
          </div>
          <div class="info-card-foot"><span>通过率</span><div class="health-bar"><div class="health-bar-fill" :style="{ width: passRate + '%' }" /></div><span>{{ passRate }}%</span></div>
        </el-card>
      </el-col>
      <el-col :span="6">
        <el-card shadow="never" class="info-card">
          <div class="info-card-header">
            <div class="info-card-icon bg-yellow"><el-icon :size="16"><WarningFilled /></el-icon></div>
            <span class="info-card-label">待处理问题</span>
            <span class="info-card-subtag danger-tag">{{ issueCount > 0 ? '需处理' : '正常' }}</span>
          </div>
          <div class="info-card-value-row">
            <span class="info-card-value yellow">{{ issueCount }}</span>
            <span class="badge neutral">较昨日持平</span>
          </div>
          <div class="info-card-foot">{{ issueCount > 0 ? '5 条空值记录' : '暂无问题' }}</div>
        </el-card>
      </el-col>
      <el-col :span="6">
        <el-card shadow="never" class="info-card">
          <div class="info-card-header">
            <div class="info-card-icon bg-red"><el-icon :size="16"><CircleCloseFilled /></el-icon></div>
            <span class="info-card-label">异常</span>
            <span class="info-card-subtag danger-tag">需修复</span>
          </div>
          <div class="info-card-value-row">
            <span class="info-card-value red">{{ errorCount }}</span>
            <span class="badge neutral">较昨日持平</span>
          </div>
          <div class="info-card-foot">金额格式检查失败</div>
        </el-card>
      </el-col>
      <el-col :span="6">
        <el-card shadow="never" class="info-card">
          <div class="info-card-header">
            <div class="info-card-icon bg-blue"><el-icon :size="16"><Setting /></el-icon></div>
            <span class="info-card-label">规则总数</span>
            <span class="info-card-subtag">已配置</span>
          </div>
          <div class="info-card-value-row">
            <span class="info-card-value">{{ qualityRules.length }}</span>
            <span class="badge neutral">较昨日持平</span>
          </div>
          <div class="info-card-foot">完整性 · 唯一性 · 格式</div>
        </el-card>
      </el-col>
    </el-row>

    <!-- 质量规则表 -->
    <Crud v-if="activeTab === 'rules'" :filter-items="rulesFilterItems" v-model:filter-values="filterValues" :pagination="rulesPagination">
      <template #actions>
        <el-button type="primary" :icon="Plus">创建质量规则</el-button>
      </template>
      <template #table>
        <Table :columns="rulesColumns" :data="pagedRules" />
      </template>
    </Crud>

    <!-- 执行记录表 -->
    <Crud v-if="activeTab === 'records'" :filter-items="recordsFilterItems" v-model:filter-values="filterValues" :pagination="recordsPagination">
      <template #table>
        <Table :columns="recordsColumns" :data="pagedRecords">
          <template #col-issues="{ row }">
            <span :class="row.issues > 0 ? 'text-danger' : ''">{{ row.issues }}</span>
          </template>
        </Table>
      </template>
    </Crud>

    <!-- 问题清单（卡片布局） -->
    <div v-if="activeTab === 'issues'" class="issue-list">
      <div v-for="issue in mockIssues" :key="issue.id" class="issue-card">
        <div class="issue-header">
          <div class="issue-title-row">
            <el-icon :size="18" class="text-warning"><WarningFilled /></el-icon>
            <div class="issue-info">
              <div>{{ issue.dataset }} · {{ issue.field }}</div>
              <div class="issue-type">{{ issue.type }}</div>
            </div>
          </div>
          <el-tag type="warning" effect="plain">{{ issue.status }}</el-tag>
        </div>
        <div class="issue-meta-row">
          <div class="issue-meta-item"><span class="meta-label">问题数量</span><span class="meta-value">{{ issue.count }} 条</span></div>
          <div class="issue-meta-item"><span class="meta-label">样例值</span><span class="meta-value mono">{{ issue.sample }}</span></div>
          <div class="issue-meta-item"><span class="meta-label">影响范围</span><span class="meta-value">{{ issue.impact }}</span></div>
          <div class="issue-meta-item"><span class="meta-label">负责人</span><span class="meta-value">{{ issue.owner }}</span></div>
        </div>
        <div class="issue-actions">
          <el-button plain>查看</el-button>
          <el-button plain>分派</el-button>
          <el-button plain>标记为可接受</el-button>
          <el-button plain type="danger">关闭</el-button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed, reactive, ref, watch } from 'vue'
import {
  Search, Plus, CircleCheckFilled, WarningFilled, CircleCloseFilled, Setting,
  VideoPlay, Edit, View,
} from '@element-plus/icons-vue'
import { Crud, Table } from '@/components/crud'
import type { ColumnSchema, FilterItem } from '@/components/crud'

const activeTab = ref('rules')
const filterValues = ref<Record<string, any>>({})

const rulesFilterItems: FilterItem[] = [
  { key: 'keyword', placeholder: '搜索规则名称或数据集...', width: '260px' },
  { key: 'type', type: 'select', placeholder: '规则类型', width: '120px',
    options: [
      { label: '全部类型', value: '' },
      { label: '完整性', value: '完整性' },
      { label: '唯一性', value: '唯一性' },
      { label: '格式', value: '格式' },
    ] },
]

const recordsFilterItems: FilterItem[] = [
  { key: 'keyword', placeholder: '搜索...', width: '260px' },
]

const searchTerm = ref('')
const typeFilter = ref('')

const tabs = [
  { key: 'rules', label: '质量规则' },
  { key: 'records', label: '执行记录' },
  { key: 'issues', label: '问题清单', count: 2 },
]

// ===================== Mock 数据 =====================

interface QualityRule {
  id: string; name: string; type: string; dataset: string
  status: 'success' | 'warning' | 'error'; lastRun: string
}

const qualityRules: QualityRule[] = [
  { id: '1', name: '主键完整性检查', type: '完整性', dataset: '销售订单表', status: 'success', lastRun: '2026-06-29 09:35' },
  { id: '2', name: '订单ID唯一性检查', type: '唯一性', dataset: '销售订单表', status: 'success', lastRun: '2026-06-29 09:35' },
  { id: '3', name: '考勤时间空值检查', type: '完整性', dataset: '每日考勤表', status: 'warning', lastRun: '2026-06-28 18:05' },
  { id: '4', name: '金额格式检查', type: '格式', dataset: '财务月报表', status: 'error', lastRun: '2026-06-27 14:05' },
]

interface ExecRecord {
  id: string; rule: string; dataset: string; time: string; result: string; issues: number
}

const executionRecords: ExecRecord[] = [
  { id: '1', rule: '主键完整性检查', dataset: '销售订单表', time: '2026-06-29 09:35', result: '通过', issues: 0 },
  { id: '2', rule: '考勤时间空值检查', dataset: '每日考勤表', time: '2026-06-28 18:05', result: '发现问题', issues: 5 },
  { id: '3', rule: '金额格式检查', dataset: '财务月报表', time: '2026-06-27 14:05', result: '发现问题', issues: 12 },
]

const mockIssues = [
  { id: 1, dataset: '每日考勤表', field: 'check_in_time', type: '空值', status: '待处理', count: 5, sample: 'NULL', impact: '考勤统计', owner: '李敏' },
  { id: 2, dataset: '财务月报表', field: 'amount', type: '格式异常', status: '调查中', count: 12, sample: '"¥12,34"', impact: '财务报表', owner: '吴婷' },
]

// ===================== 过滤 & 分页 =====================

const filteredRules = computed(() =>
  qualityRules.filter(r => {
    const matchSearch = r.name.includes(filterValues.value.keyword || '') || r.dataset.includes(filterValues.value.keyword || '')
    const matchType = !filterValues.value.type || r.type === filterValues.value.type
    return matchSearch && matchType
  })
)
const filteredRecords = computed(() =>
  executionRecords.filter(r =>
    r.rule.includes(filterValues.value.keyword || '') || r.dataset.includes(filterValues.value.keyword || '')
  )
)

function slicePage<T>(data: T[], page: number, size: number) {
  return data.slice((page - 1) * size, page * size)
}

// 规则分页
const rulesPagination = reactive({ page: 1, pageSize: 20, total: 0, onPageChange() {}, onSizeChange() {} })
const pagedRules = computed(() => slicePage(filteredRules.value, rulesPagination.page, rulesPagination.pageSize))
watch([filteredRules, () => rulesPagination.pageSize], () => {
  rulesPagination.total = filteredRules.value.length
  if (rulesPagination.page > 1 && (rulesPagination.page - 1) * rulesPagination.pageSize >= rulesPagination.total) rulesPagination.page = 1
})

// 执行记录分页
const recordsPagination = reactive({ page: 1, pageSize: 20, total: 0, onPageChange() {}, onSizeChange() {} })
const pagedRecords = computed(() => slicePage(filteredRecords.value, recordsPagination.page, recordsPagination.pageSize))
watch([filteredRecords, () => recordsPagination.pageSize], () => {
  recordsPagination.total = filteredRecords.value.length
  if (recordsPagination.page > 1 && (recordsPagination.page - 1) * recordsPagination.pageSize >= recordsPagination.total) recordsPagination.page = 1
})

// ===================== 统计 =====================

const throughCount = computed(() => qualityRules.filter(r => r.status === 'success').length)
const issueCount = 2
const errorCount = computed(() => qualityRules.filter(r => r.status === 'error').length)
const passRate = computed(() =>
  qualityRules.length > 0 ? Math.round((throughCount.value / qualityRules.length) * 100) : 0
)

// ===================== 列配置 =====================

const rulesColumns: ColumnSchema[] = [
  { type: 'text', prop: 'name', label: '规则名称', minWidth: 180 },
  { type: 'tag', prop: 'type', label: '类型', width: 100 },
  { type: 'text', prop: 'dataset', label: '适用数据集', minWidth: 140 },
  {
    type: 'tag', prop: 'status', label: '状态', width: 90,
    tagMap: { success: 'success', warning: 'warning', error: 'danger' },
    formatter: (v: string) => ({ success: '通过', warning: '警告', error: '异常' }[v] ?? v),
  },
  { type: 'text', prop: 'lastRun', label: '最近执行', width: 180 },
  {
    type: 'action', label: '操作', width: 120,
    buttons: [
      { label: '执行', icon: VideoPlay, onClick: () => {} },
      { label: '编辑', icon: Edit, onClick: () => {} },
    ],
  },
]

const recordsColumns: ColumnSchema[] = [
  { type: 'text', prop: 'rule', label: '规则名称', minWidth: 160 },
  { type: 'text', prop: 'dataset', label: '数据集', minWidth: 140 },
  { type: 'text', prop: 'time', label: '执行时间', width: 180 },
  {
    type: 'tag', prop: 'result', label: '结果', width: 100,
    tagMap: { '通过': 'success', '发现问题': 'warning' },
  },
  { type: 'custom', prop: 'issues', label: '发现问题', width: 100, align: 'center' },
  {
    type: 'action', label: '操作', width: 100,
    buttons: [{ label: '查看详情', icon: View, onClick: () => {} }],
  },
]
</script>

<style lang="scss" scoped>
.quality-page { display: flex; flex-direction: column; gap: 20px; }

.tab-bar { display: flex; gap: 0; border-bottom: 1px solid $color-border; margin-bottom: 0; }
.tab-btn {
  padding: 10px 16px; border: none; background: none;
  font-size: $font-size-base; color: $color-text-secondary; cursor: pointer;
  border-bottom: 2px solid transparent;
  &:hover { color: $color-text-primary; }
  &.active { color: $color-primary; border-bottom-color: $color-primary; font-weight: $font-weight-medium; }
}
.tab-count { font-size: $font-size-xs; color: $color-text-placeholder; margin-left: 4px; }

.search-input { width: 320px; }
.filter-select { width: 130px; }

.stat-row {
  margin: 0 !important;
  :deep(.el-col) { padding-left: 8px !important; padding-right: 8px !important; }
  :deep(.el-col:first-child) { padding-left: 0 !important; }
  :deep(.el-col:last-child) { padding-right: 0 !important; }
}

.info-card { :deep(.el-card__body) { padding: 20px; display: flex; flex-direction: column; gap: 8px; } }
.info-card-header { display: flex; align-items: center; gap: 6px; }
.info-card-icon {
  width: 32px; height: 32px; border-radius: 8px;
  display: flex; align-items: center; justify-content: center;
  &.bg-blue { background: #dbeafe; color: $color-primary; }
  &.bg-green { background: #dcfce7; color: $color-success; }
  &.bg-yellow { background: #fef3c7; color: $color-warning; }
  &.bg-red { background: #fee2e2; color: $color-danger; }
}
.info-card-label { font-size: $font-size-base; color: $color-text-secondary; }
.info-card-subtag {
  font-size: $font-size-xs; color: $color-text-placeholder;
  background: #f3f4f6; padding: 1px 6px;
  border-radius: 4px; margin-left: auto; white-space: nowrap;
}
.danger-tag { color: $color-danger; background: #fee2e2; border: 1px solid #fecaca; }
.info-card-value-row { display: flex; align-items: baseline; gap: 8px; }
.info-card-value {
  font-size: 28px; font-weight: $font-weight-bold; color: $color-text-primary;
  &.green { color: $color-success; }
  &.yellow { color: $color-warning; }
  &.red { color: $color-danger; }
}
.badge {
  font-size: $font-size-xs; padding: 1px 6px; border-radius: 4px;
  &.green-bg { color: $color-success; background: #f0fdf4; }
  &.neutral { color: $color-text-placeholder; background: #f3f4f6; }
}
.info-card-foot { display: flex; align-items: center; gap: 6px; font-size: $font-size-xs; color: $color-text-placeholder; }
.health-bar { flex: 1; height: 4px; background: #f3f4f6; border-radius: 2px; overflow: hidden; }
.health-bar-fill { height: 100%; background: $color-success; border-radius: 2px; }

.text-warning { color: $color-warning; }
.text-danger { color: $color-danger; }

.issue-list { display: flex; flex-direction: column; gap: 12px; }
.issue-card {
  padding: 16px; background: #fefce8;
  border: 1px solid #fef08a; border-radius: $radius-base;
}
.issue-header { display: flex; align-items: flex-start; justify-content: space-between; margin-bottom: 12px; }
.issue-title-row { display: flex; align-items: flex-start; gap: 8px; }
.issue-info { display: flex; flex-direction: column; gap: 2px; font-size: $font-size-base; }
.issue-type { font-size: $font-size-sm; color: $color-text-secondary; }
.issue-meta-row { display: grid; grid-template-columns: repeat(4, 1fr); gap: 16px; margin-bottom: 12px; }
.issue-meta-item { display: flex; flex-direction: column; gap: 2px; }
.meta-label { font-size: $font-size-xs; color: $color-text-placeholder; }
.meta-value { font-size: $font-size-base; color: $color-warning; }
.mono { font-family: $font-family-mono; font-size: $font-size-xs; }
.issue-actions { display: flex; gap: 8px; }
</style>
