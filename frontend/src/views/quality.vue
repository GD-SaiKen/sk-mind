<template>
  <div class="quality-page">
    <!-- 标签页 -->
    <div class="tab-bar">
      <button
        v-for="tab in tabs" :key="tab.key" class="tab-btn"
        :class="{ active: activeTab === tab.key }" @click="activeTab = tab.key"
      >{{ tab.label }}<span v-if="tab.count" class="tab-count">{{ tab.count }}</span></button>
    </div>

    <!-- 筛选区 -->
    <div class="toolbar">
      <el-input
        v-model="searchTerm" placeholder="搜索规则名称或数据集..."
        :prefix-icon="Search" class="search-input" clearable
      />
      <el-select
        v-if="activeTab === 'rules'" v-model="typeFilter" placeholder="规则类型" class="filter-select" clearable
      >
        <el-option label="全部类型" value="" />
        <el-option label="完整性" value="完整性" />
        <el-option label="唯一性" value="唯一性" />
        <el-option label="格式" value="格式" />
      </el-select>
      <div class="spacer" />
      <el-button type="primary" :icon="Plus">创建质量规则</el-button>
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

    <!-- 质量规则列表 -->
    <el-card v-if="activeTab === 'rules'" shadow="never">
      <el-table :data="filteredRules" stripe>
        <el-table-column label="规则名称" min-width="180" prop="name" />
        <el-table-column label="类型" width="100">
          <template #default="{ row }"><el-tag size="small" effect="plain">{{ row.type }}</el-tag></template>
        </el-table-column>
        <el-table-column label="适用数据集" min-width="140" prop="dataset" />
        <el-table-column label="状态" width="90">
          <template #default="{ row }">
            <el-tag :type="statusTagType(row.status)" size="small" effect="plain">{{ statusLabel(row.status) }}</el-tag>
          </template>
        </el-table-column>
        <el-table-column label="最近执行" width="180" prop="lastRun" />
        <el-table-column label="操作" width="120" fixed="right">
          <template #default>
            <div class="action-btns">
              <el-button link type="primary" :icon="VideoPlay" />
              <el-button link type="primary" :icon="Edit" />
            </div>
          </template>
        </el-table-column>
      </el-table>
    </el-card>

    <!-- 执行记录 -->
    <el-card v-if="activeTab === 'records'" shadow="never">
      <el-table :data="executionRecords" stripe>
        <el-table-column label="规则名称" min-width="160" prop="rule" />
        <el-table-column label="数据集" min-width="140" prop="dataset" />
        <el-table-column label="执行时间" width="180" prop="time" />
        <el-table-column label="结果" width="100">
          <template #default="{ row }">
            <el-tag :type="row.result === '通过' ? 'success' : 'warning'" size="small" effect="plain">{{ row.result }}</el-tag>
          </template>
        </el-table-column>
        <el-table-column label="发现问题" width="100" align="center">
          <template #default="{ row }">
            <span :class="row.issues > 0 ? 'text-danger' : ''">{{ row.issues }}</span>
          </template>
        </el-table-column>
        <el-table-column label="操作" width="100">
          <template #default><el-button link type="primary" size="small">查看详情</el-button></template>
        </el-table-column>
      </el-table>
    </el-card>

    <!-- 问题清单 -->
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
          <el-tag type="warning" size="small" effect="plain">{{ issue.status }}</el-tag>
        </div>
        <div class="issue-meta-row">
          <div class="issue-meta-item"><span class="meta-label">问题数量</span><span class="meta-value">{{ issue.count }} 条</span></div>
          <div class="issue-meta-item"><span class="meta-label">样例值</span><span class="meta-value mono">{{ issue.sample }}</span></div>
          <div class="issue-meta-item"><span class="meta-label">影响范围</span><span class="meta-value">{{ issue.impact }}</span></div>
          <div class="issue-meta-item"><span class="meta-label">负责人</span><span class="meta-value">{{ issue.owner }}</span></div>
        </div>
        <div class="issue-actions">
          <el-button size="small" plain>查看</el-button>
          <el-button size="small" plain>分派</el-button>
          <el-button size="small" plain>标记为可接受</el-button>
          <el-button size="small" plain type="danger">关闭</el-button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed, ref } from 'vue'
import {
  Search, Plus, CircleCheckFilled, WarningFilled, CircleCloseFilled, Setting,
  VideoPlay, Edit,
} from '@element-plus/icons-vue'

const activeTab = ref('rules')
const searchTerm = ref('')
const typeFilter = ref('')

const tabs = [
  { key: 'rules', label: '质量规则' },
  { key: 'records', label: '执行记录' },
  { key: 'issues', label: '问题清单', count: 2 },
]

interface QualityRule {
  id: string; name: string; type: string; dataset: string;
  status: 'success' | 'warning' | 'error'; lastRun: string;
}

const qualityRules: QualityRule[] = [
  { id: '1', name: '主键完整性检查', type: '完整性', dataset: '销售订单表', status: 'success', lastRun: '2026-06-29 09:35' },
  { id: '2', name: '订单ID唯一性检查', type: '唯一性', dataset: '销售订单表', status: 'success', lastRun: '2026-06-29 09:35' },
  { id: '3', name: '考勤时间空值检查', type: '完整性', dataset: '每日考勤表', status: 'warning', lastRun: '2026-06-28 18:05' },
  { id: '4', name: '金额格式检查', type: '格式', dataset: '财务月报表', status: 'error', lastRun: '2026-06-27 14:05' },
]

const executionRecords = [
  { id: '1', rule: '主键完整性检查', dataset: '销售订单表', time: '2026-06-29 09:35', result: '通过', issues: 0 },
  { id: '2', rule: '考勤时间空值检查', dataset: '每日考勤表', time: '2026-06-28 18:05', result: '发现问题', issues: 5 },
  { id: '3', rule: '金额格式检查', dataset: '财务月报表', time: '2026-06-27 14:05', result: '发现问题', issues: 12 },
]

const mockIssues = [
  { id: 1, dataset: '每日考勤表', field: 'check_in_time', type: '空值', status: '待处理', count: 5, sample: 'NULL', impact: '考勤统计', owner: '李敏' },
  { id: 2, dataset: '财务月报表', field: 'amount', type: '格式异常', status: '调查中', count: 12, sample: '"¥12,34"', impact: '财务报表', owner: '吴婷' },
]

const filteredRules = computed(() =>
  qualityRules.filter((r) => {
    const matchSearch = r.name.includes(searchTerm.value) || r.dataset.includes(searchTerm.value)
    const matchType = !typeFilter.value || r.type === typeFilter.value
    return matchSearch && matchType
  })
)

const throughCount = computed(() => qualityRules.filter((r) => r.status === 'success').length)
const issueCount = 2
const errorCount = computed(() => qualityRules.filter((r) => r.status === 'error').length)
const passRate = computed(() =>
  qualityRules.length > 0 ? Math.round((throughCount.value / qualityRules.length) * 100) : 0
)

function statusTagType(status: string) {
  const map: Record<string, 'success' | 'warning' | 'danger'> = { success: 'success', warning: 'warning', error: 'danger' }
  return map[status] ?? 'info'
}
function statusLabel(status: string) {
  const map: Record<string, string> = { success: '通过', warning: '警告', error: '异常' }
  return map[status] ?? status
}
</script>

<style lang="scss" scoped>
.quality-page {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.tab-bar { display: flex; gap: 0; border-bottom: 1px solid $color-border; margin-bottom: 0; }
.tab-btn {
  padding: 10px 16px; border: none; background: none;
  font-size: $font-size-base; color: $color-text-secondary; cursor: pointer;
  border-bottom: 2px solid transparent;
  &:hover { color: $color-text-primary; }
  &.active { color: $color-primary; border-bottom-color: $color-primary; font-weight: $font-weight-medium; }
}
.tab-count { font-size: $font-size-xs; color: $color-text-placeholder; margin-left: 4px; }

.toolbar { display: flex; align-items: center; gap: 12px; }
.search-input { width: 320px; }
.filter-select { width: 130px; }
.spacer { flex: 1; }

.stat-row {
  margin: 0 !important;
  :deep(.el-col) { padding-left: 8px !important; padding-right: 8px !important; }
  :deep(.el-col:first-child) { padding-left: 0 !important; }
  :deep(.el-col:last-child) { padding-right: 0 !important; }
}

.info-card {
  :deep(.el-card__body) { padding: 20px; display: flex; flex-direction: column; gap: 8px; }
}
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
.info-card-foot {
  display: flex; align-items: center; gap: 6px;
  font-size: $font-size-xs; color: $color-text-placeholder;
}
.health-bar { flex: 1; height: 4px; background: #f3f4f6; border-radius: 2px; overflow: hidden; }
.health-bar-fill { height: 100%; background: $color-success; border-radius: 2px; }

.action-btns { display: flex; gap: 0; }
.text-warning { color: $color-warning; }
.text-danger { color: $color-danger; }

.issue-list { display: flex; flex-direction: column; gap: 12px; }
.issue-card {
  padding: 16px; background: #fefce8;
  border: 1px solid #fef08a; border-radius: $radius-base;
}
.issue-header {
  display: flex; align-items: flex-start; justify-content: space-between;
  margin-bottom: 12px;
}
.issue-title-row { display: flex; align-items: flex-start; gap: 8px; }
.issue-info { display: flex; flex-direction: column; gap: 2px; font-size: $font-size-base; }
.issue-type { font-size: $font-size-sm; color: $color-text-secondary; }
.issue-meta-row {
  display: grid; grid-template-columns: repeat(4, 1fr);
  gap: 16px; margin-bottom: 12px;
}
.issue-meta-item { display: flex; flex-direction: column; gap: 2px; }
.meta-label { font-size: $font-size-xs; color: $color-text-placeholder; }
.meta-value { font-size: $font-size-base; color: $color-warning; }
.mono { font-family: $font-family-mono; font-size: $font-size-xs; }
.issue-actions { display: flex; gap: 8px; }
</style>
