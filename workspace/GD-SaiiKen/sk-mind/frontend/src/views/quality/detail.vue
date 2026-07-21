<template>
  <div class="page-layout detail-page">
    <Index
      title="数据集质量详情"
      :breadcrumb="[{ label: '首页', to: '/' }, { label: '数据质量', to: '/quality' }, { label: '质量详情' }]"
    />

    <el-row class="summary-row" :gutter="16">
      <el-col :span="6"><div class="summary-card"><div class="summary-label">数据集</div><div class="summary-value">{{ dsName }}</div></div></el-col>
      <el-col :span="6"><div class="summary-card"><div class="summary-label">总体状态</div><div class="summary-value"><el-tag type="warning" effect="plain">警告</el-tag></div></div></el-col>
      <el-col :span="6"><div class="summary-card"><div class="summary-label">检查时间</div><div class="summary-value">2026-07-10 09:35</div></div></el-col>
      <el-col :span="6"><div class="summary-card"><div class="summary-label">影响 Agent</div><div class="summary-value">不影响使用</div></div></el-col>
    </el-row>

    <TabNav v-model="activeTab" :tabs="tabs" />

    <div v-if="activeTab === 'overview'" class="tab-content">
      <div class="stat-grid">
        <StatCard :icon="CircleCheckFilled" icon-bg="bg-green" label="通过" :value="passCount" value-class="green" footer-text="已通过的规则" />
        <StatCard :icon="WarningFilled" icon-bg="bg-yellow" label="警告" :value="warnCount" value-class="yellow" footer-text="待确认的问题" />
        <StatCard :icon="CircleCloseFilled" icon-bg="bg-red" label="异常" :value="errCount" value-class="red" footer-text="需立即修复" />
        <StatCard :icon="Setting" icon-bg="bg-blue" label="规则数" :value="checks.length" footer-text="已配置的质量规则" />
      </div>
    </div>

    <div v-if="activeTab === 'rules'" class="tab-content">
      <Table :columns="ruleColumns" :data="checks">
        <template #col-ruleName="{ row }">
          <span class="mono">{{ row.ruleName }}</span>
        </template>
      </Table>
    </div>

    <div v-if="activeTab === 'issues'" class="tab-content">
      <div class="issue-list">
        <div v-for="issue in issues" :key="issue.id" class="issue-card">
          <div class="issue-header">
            <div class="issue-title">
              <el-icon :size="18" class="text-warning"><WarningFilled /></el-icon>
              <div>
                <div>{{ issue.field }} · {{ issue.type }}</div>
                <div class="issue-desc">{{ issue.desc }}</div>
              </div>
            </div>
            <el-tag :type="issue.status === '未处理' ? 'danger' : issue.status === '处理中' ? 'warning' : 'success'" effect="plain">{{ issue.status }}</el-tag>
          </div>
          <div class="issue-meta">
            <span>数量: {{ issue.count }} 条</span>
            <span>样例: <code>{{ issue.sample }}</code></span>
            <span>影响: {{ issue.impact }}</span>
            <span>负责人: {{ issue.owner }}</span>
          </div>
          <div class="issue-actions">
            <el-button plain size="small">查看</el-button>
            <el-button plain size="small">分派</el-button>
            <el-button plain size="small" type="danger">关闭</el-button>
          </div>
        </div>
      </div>
    </div>

    <div v-if="activeTab === 'history'" class="tab-content">
      <Table :columns="historyColumns" :data="history" />
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { useRoute } from 'vue-router'
import { CircleCheckFilled, CircleCloseFilled, Setting, WarningFilled } from '@element-plus/icons-vue'
import Index from '@/components/page-header/index.vue'
import TabNav from '@/components/tab-nav/index.vue'
import type { TabItem } from '@/components/tab-nav/index.vue'
import StatCard from '@/components/stat-card/index.vue'
import { Table } from '@/components/crud'
import type { ColumnSchema } from '@/components/crud'

const route = useRoute()
const dsName = ref(String(route.params.id || '-'))
const activeTab = ref('overview')

const tabs: TabItem[] = [
  { key: 'overview', label: '质量概览' },
  { key: 'rules', label: '规则结果' },
  { key: 'issues', label: '问题清单', count: 2 },
  { key: 'history', label: '处理记录' },
]

const checks = [
  { id: '1', ruleName: '主键完整性检查', type: '完整性', result: '通过', runAt: '2026-07-10 09:35' },
  { id: '2', ruleName: '订单ID唯一性检查', type: '唯一性', result: '通过', runAt: '2026-07-10 09:35' },
  { id: '3', ruleName: '金额格式检查', type: '格式', result: '警告', runAt: '2026-07-10 09:35' },
]

const passCount = checks.filter(c => c.result === '通过').length
const warnCount = checks.filter(c => c.result === '警告').length
const errCount = checks.filter(c => c.result === '异常').length

const issues = [
  { id: 1, field: 'amount', type: '格式异常', desc: '存在非标准金额格式', status: '未处理', count: 5, sample: '"￥12,345"', impact: '金额统计', owner: '李敏' },
  { id: 2, field: 'phone_number', type: '空值', desc: '部分记录缺少联系电话', status: '处理中', count: 3, sample: 'NULL', impact: '客户联系', owner: '周磊' },
]

const ruleColumns: ColumnSchema[] = [
  { type: 'custom', prop: 'ruleName', label: '规则名称', minWidth: 180 },
  { type: 'tag', prop: 'type', label: '类型', width: 100 },
  { type: 'tag', prop: 'result', label: '结果', width: 80, tagMap: { '通过': 'success', '警告': 'warning', '异常': 'danger' } },
  { type: 'date', prop: 'runAt', label: '执行时间', width: 170 },
]

const history = [
  { time: '2026-07-09 12:00', user: '管理员', action: '标记为可接受', field: 'amount', note: '已确认该格式为Excel导出遗留问题' },
  { time: '2026-07-08 15:30', user: '李敏', action: '分派给周磊', field: 'phone_number', note: '需与业务确认是否必填' },
]

const historyColumns: ColumnSchema[] = [
  { type: 'text', prop: 'time', label: '时间', width: 170 },
  { type: 'text', prop: 'user', label: '用户', width: 80 },
  { type: 'text', prop: 'action', label: '操作', width: 130 },
  { type: 'text', prop: 'field', label: '字段', width: 130 },
  { type: 'text', prop: 'note', label: '备注', minWidth: 200 },
]
</script>

<style lang="scss" scoped>
.summary-row { margin: 0 0 16px; }
.summary-card { padding: 16px; background: #f9fafb; border: 1px solid #e5e7eb; border-radius: 8px; }
.summary-label { font-size: 13px; color: #6b7280; margin-bottom: 4px; }
.summary-value { font-size: 16px; color: #1f2937; font-weight: 500; }
.tab-content { padding-top: 16px; }
.mono { font-family: $font-family-mono; font-size: 13px; }
.stat-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 16px; }
:deep(.bg-green) { background: #dcfce7; color: $color-success; }
:deep(.bg-yellow) { background: #fef3c7; color: $color-warning; }
:deep(.bg-red) { background: #fee2e2; color: $color-danger; }
:deep(.bg-blue) { background: #dbeafe; color: $color-primary; }
.green { color: $color-success; }
.yellow { color: $color-warning; }
.red { color: $color-danger; }
.text-warning { color: $color-warning; }
.issue-list { display: flex; flex-direction: column; gap: 12px; }
.issue-card { padding: 16px; background: #fefce8; border: 1px solid #fef08a; border-radius: 8px; }
.issue-header { display: flex; align-items: flex-start; justify-content: space-between; }
.issue-title { display: flex; align-items: flex-start; gap: 8px; font-size: 14px; }
.issue-desc { font-size: 13px; color: $color-text-secondary; margin-top: 2px; }
.issue-meta { display: flex; gap: 16px; font-size: 12px; color: $color-text-secondary; margin: 10px 0; }
.issue-meta code { background: #f3f4f6; padding: 1px 4px; border-radius: 3px; }
.issue-actions { display: flex; gap: 6px; }
</style>
