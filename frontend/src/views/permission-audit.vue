﻿<template>
  <div class="perm-page">
    <div class="tab-bar">
      <button v-for="tab in tabs" :key="tab" class="tab-btn" :class="{ active: activeTab === tab }" @click="activeTab = tab">{{ tab }}</button>
    </div>

    <!-- 统计卡片 -->
    <el-row :gutter="16" class="stat-row">
      <el-col :span="6"><el-card shadow="never" class="info-card"><div class="info-card-header"><div class="info-card-icon bg-blue"><el-icon :size="16"><User /></el-icon></div><span class="info-card-label">活跃用户</span><span class="subtag green">在线</span></div><div class="val-row"><span class="val">45</span><span class="badge green-bg">↑ 3 较昨日</span></div><div class="foot">在线用户</div></el-card></el-col>
      <el-col :span="6"><el-card shadow="never" class="info-card"><div class="info-card-header"><div class="info-card-icon bg-purple"><el-icon :size="16"><Lock /></el-icon></div><span class="info-card-label">角色数量</span><span class="subtag">持平</span></div><div class="val-row"><span class="val">8</span><span class="badge neutral">较昨日持平</span></div><div class="foot">管理员 · 财务 · 销售 等</div></el-card></el-col>
      <el-col :span="6"><el-card shadow="never" class="info-card"><div class="info-card-header"><div class="info-card-icon bg-green"><el-icon :size="16"><CircleCheckFilled /></el-icon></div><span class="info-card-label">通过率</span><span class="subtag green">良好</span></div><div class="val-row"><span class="val green">98%</span><span class="badge neutral">较昨日持平</span></div><div class="foot">审核通过率</div></el-card></el-col>
      <el-col :span="6"><el-card shadow="never" class="info-card"><div class="info-card-header"><div class="info-card-icon bg-red"><el-icon :size="16"><WarningFilled /></el-icon></div><span class="info-card-label">被拒绝</span><span class="subtag danger-tag">异常</span></div><div class="val-row"><span class="val red">3</span><span class="badge neutral">较昨日持平</span></div><div class="foot">权限不足拒绝</div></el-card></el-col>
    </el-row>

    <!-- 审计日志表 -->
    <Crud :filter-items="searchFilterItems" v-model:filter-values="searchValues" v-if="activeTab === '审计日志'" :pagination="auditPagination">
      <template #actions>
        <el-button plain :icon="View">导出日志</el-button>
      </template>
      <template #table>
        <Table :columns="auditColumns" :data="pagedAuditLogs" />
      </template>
    </Crud>

    <!-- 角色管理（卡片布局） -->
    <div v-if="activeTab === '角色管理'">
      <div class="toolbar">
        <el-input v-model="searchTerm" placeholder="搜索..." :prefix-icon="Search" class="search-input" clearable />
        <div class="spacer" />
        <el-button type="primary" :icon="Plus">创建角色</el-button>
      </div>
      <div v-for="role in roles" :key="role.name" class="role-item">
        <div class="role-left"><div :class="['role-icon', role.bg]"><el-icon :size="16"><component :is="role.icon" /></el-icon></div><div><div class="role-name">{{ role.name }}</div><div class="role-desc">{{ role.desc }}</div></div></div>
        <div class="role-right"><el-tag effect="plain">{{ role.count }} 人</el-tag><el-button link>编辑</el-button><el-button link>查看成员</el-button></div>
      </div>
    </div>

    <!-- 敏感字段表 -->
    <Crud :filter-items="searchFilterItems" v-model:filter-values="searchValues" v-if="activeTab === '敏感字段'" :pagination="sfPagination">
      <template #actions>
        <el-button type="primary" :icon="Plus">标记敏感字段</el-button>
      </template>
      <template #table>
        <Table :columns="sfColumns" :data="pagedSensitiveFields" />
      </template>
    </Crud>

    <!-- 用户管理 / 数据集权限（占位） -->
    <el-card v-if="activeTab === '用户管理' || activeTab === '数据集权限'" shadow="never">
      <el-empty :description="activeTab + ' 功能即将上线'" />
    </el-card>
  </div>
</template>

<script setup lang="ts">
import { computed, reactive, ref, watch } from 'vue'
import { Search, Plus, View, User, Lock, CircleCheckFilled, WarningFilled, Edit, Coin, Upload, Service } from '@element-plus/icons-vue'
import { Crud, Table } from '@/components/crud'
import type { ColumnSchema, FilterItem } from '@/components/crud'

const activeTab = ref('审计日志')
const searchFilterItems: FilterItem[] = [
  { key: 'keyword', placeholder: '搜索...', width: '260px' },
]
const searchValues = ref<Record<string, any>>({})
const searchTerm = ref('')
const tabs = ['用户管理', '角色管理', '数据集权限', '敏感字段', '审计日志']

// ===================== Mock 数据 =====================

const auditLogs = [
  { id: '1', time: '2026-06-29 10:15', user: '张三', role: '管理员', operation: '数据查询', object: '销售订单表', range: '全部字段', result: '成功', ip: '192.168.1.100' },
  { id: '2', time: '2026-06-29 10:10', user: '李四', role: '财务部门', operation: '数据导出', object: '财务月报表', range: '500 条记录', result: '成功', ip: '192.168.1.101' },
  { id: '3', time: '2026-06-29 10:05', user: '王五', role: '普通用户', operation: '数据查询', object: '每日考勤表', range: '特定记录', result: '权限不足', ip: '192.168.1.102' },
]

const roles = [
  { name: '管理员', desc: '系统全部权限', count: 2, bg: 'bg-blue', icon: User },
  { name: '财务部门', desc: '财务数据读写权限', count: 5, bg: 'bg-green', icon: Coin },
  { name: '销售部门', desc: '销售数据读写权限', count: 8, bg: 'bg-purple', icon: Upload },
  { name: 'HR部门', desc: '人事数据读写权限', count: 3, bg: 'bg-orange', icon: Service },
]

const sensitiveFields = [
  { id: '1', field: 'employee_salary', dataset: '员工信息表', type: '薪资', masking: '脱敏显示(前缀)', roles: '管理员, HR部门' },
  { id: '2', field: 'phone_number', dataset: '客户信息表', type: '个人信息', masking: '部分隐藏', roles: '管理员, 销售部门' },
  { id: '3', field: 'bank_account', dataset: '财务信息表', type: '金融信息', masking: '完全隐藏', roles: '管理员' },
]

// ===================== 过滤 & 分页 =====================

const filteredAuditLogs = computed(() =>
  auditLogs.filter(l => l.user.includes(searchValues.value.keyword || '') || l.object.includes(searchValues.value.keyword || '') || l.operation.includes(searchValues.value.keyword || ''))
)
const filteredSensitiveFields = computed(() =>
  sensitiveFields.filter(f => f.field.includes(searchValues.value.keyword || '') || f.dataset.includes(searchValues.value.keyword || ''))
)

function slicePage<T>(data: T[], page: number, size: number) {
  return data.slice((page - 1) * size, page * size)
}

const auditPagination = reactive({ page: 1, pageSize: 20, total: 0, onPageChange() {}, onSizeChange() {} })
const pagedAuditLogs = computed(() => slicePage(filteredAuditLogs.value, auditPagination.page, auditPagination.pageSize))
watch([filteredAuditLogs, () => auditPagination.pageSize], () => {
  auditPagination.total = filteredAuditLogs.value.length
})

const sfPagination = reactive({ page: 1, pageSize: 20, total: 0, onPageChange() {}, onSizeChange() {} })
const pagedSensitiveFields = computed(() => slicePage(filteredSensitiveFields.value, sfPagination.page, sfPagination.pageSize))
watch([filteredSensitiveFields, () => sfPagination.pageSize], () => {
  sfPagination.total = filteredSensitiveFields.value.length
})

// ===================== 列配置 =====================

const auditColumns: ColumnSchema[] = [
  { type: 'text', prop: 'time', label: '时间', width: 170 },
  { type: 'text', prop: 'user', label: '用户', width: 80 },
  { type: 'tag', prop: 'role', label: '角色', width: 100 },
  { type: 'text', prop: 'operation', label: '操作', width: 100 },
  { type: 'text', prop: 'object', label: '对象', minWidth: 130 },
  { type: 'text', prop: 'range', label: '范围', width: 120 },
  {
    type: 'tag', prop: 'result', label: '结果', width: 100,
    tagMap: { '成功': 'success', '权限不足': 'danger' },
  },
  { type: 'text', prop: 'ip', label: 'IP', width: 130 },
]

const sfColumns: ColumnSchema[] = [
  { type: 'text', prop: 'field', label: '字段名', width: 160 },
  { type: 'text', prop: 'dataset', label: '数据集', minWidth: 140 },
  { type: 'tag', prop: 'type', label: '类型', width: 100, tagType: 'danger' },
  { type: 'text', prop: 'masking', label: '脱敏方式', width: 140 },
  { type: 'text', prop: 'roles', label: '可访问角色', minWidth: 160 },
  {
    type: 'action', label: '操作', width: 80,
    buttons: [{ label: '编辑', icon: Edit, onClick: () => {} }],
  },
]
</script>

<style lang="scss" scoped>
.perm-page { display: flex; flex-direction: column; gap: 20px; }
.tab-bar { display: flex; gap: 0; border-bottom: 1px solid $color-border; }
.tab-btn { padding: 10px 16px; border: none; background: none; font-size: $font-size-base; color: $color-text-secondary; cursor: pointer; border-bottom: 2px solid transparent; &:hover { color: $color-text-primary; } &.active { color: $color-primary; border-bottom-color: $color-primary; font-weight: $font-weight-medium; } }
.search-input { width: 280px; }
.spacer { flex: 1; }
.toolbar { display: flex; align-items: center; gap: 12px; margin-bottom: 16px; }

.stat-row { margin: 0 !important; :deep(.el-col) { padding-left: 8px !important; padding-right: 8px !important; } :deep(.el-col:first-child) { padding-left: 0 !important; } :deep(.el-col:last-child) { padding-right: 0 !important; } }
.info-card { :deep(.el-card__body) { padding: 20px; display: flex; flex-direction: column; gap: 8px; } }
.info-card-header { display: flex; align-items: center; gap: 6px; }
.info-card-icon { width: 32px; height: 32px; border-radius: 8px; display: flex; align-items: center; justify-content: center; &.bg-blue { background: #dbeafe; color: $color-primary; } &.bg-green { background: #dcfce7; color: $color-success; } &.bg-yellow { background: #fef3c7; color: $color-warning; } &.bg-red { background: #fee2e2; color: $color-danger; } &.bg-purple { background: #ede9fe; color: #7c3aed; } }
.info-card-label { font-size: $font-size-base; color: $color-text-secondary; }
.subtag { font-size: $font-size-xs; padding: 1px 6px; border-radius: 4px; margin-left: auto; white-space: nowrap; background: #f3f4f6; color: $color-text-placeholder; &.green { color: $color-success; background: #f0fdf4; } &.danger-tag { color: $color-danger; background: #fee2e2; border: 1px solid #fecaca; } }
.val-row { display: flex; align-items: baseline; gap: 8px; }
.val { font-size: 28px; font-weight: $font-weight-bold; color: $color-text-primary; &.green { color: $color-success; } &.red { color: $color-danger; } }
.badge { font-size: $font-size-xs; padding: 1px 6px; border-radius: 4px; &.green-bg { color: $color-success; background: #f0fdf4; } &.neutral { color: $color-text-placeholder; background: #f3f4f6; } }
.foot { font-size: $font-size-xs; color: $color-text-placeholder; }

.role-item { display: flex; align-items: center; justify-content: space-between; padding: 16px; border: 1px solid $color-border; border-radius: $radius-base; margin-bottom: 8px; background: #fff; }
.role-left { display: flex; align-items: center; gap: 12px; }
.role-icon { width: 40px; height: 40px; border-radius: 10px; display: flex; align-items: center; justify-content: center; }
.bg-blue { background: #dbeafe; color: $color-primary; }
.bg-green { background: #dcfce7; color: $color-success; }
.bg-purple { background: #ede9fe; color: #7c3aed; }
.bg-orange { background: #fff7ed; color: #ea580c; }
.role-name { font-size: $font-size-base; font-weight: $font-weight-medium; }
.role-desc { font-size: $font-size-sm; color: $color-text-secondary; }
.role-right { display: flex; align-items: center; gap: 8px; }
</style>
