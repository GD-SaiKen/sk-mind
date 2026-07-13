<template>
  <div class="perm-page">
    <div class="tab-bar">
      <button v-for="tab in tabs" :key="tab" class="tab-btn" :class="{ active: activeTab === tab }" @click="activeTab = tab">{{ tab }}</button>
    </div>

    <div class="toolbar">
      <el-input v-model="searchTerm" placeholder="搜索..." :prefix-icon="Search" class="search-input" clearable />
      <div class="spacer" />
      <el-button v-if="activeTab !== '审计日志'" type="primary" :icon="Plus">{{ actionLabel[activeTab] }}</el-button>
      <el-button v-else plain :icon="View">导出日志</el-button>
    </div>

    <el-row :gutter="16" class="stat-row">
      <el-col :span="6"><el-card shadow="never" class="info-card"><div class="info-card-header"><div class="info-card-icon bg-blue"><el-icon :size="16"><User /></el-icon></div><span class="info-card-label">活跃用户</span><span class="subtag green">在线</span></div><div class="val-row"><span class="val">45</span><span class="badge green-bg">↑ 3 较昨日</span></div><div class="foot">在线用户</div></el-card></el-col>
      <el-col :span="6"><el-card shadow="never" class="info-card"><div class="info-card-header"><div class="info-card-icon bg-purple"><el-icon :size="16"><Lock /></el-icon></div><span class="info-card-label">角色数量</span><span class="subtag">持平</span></div><div class="val-row"><span class="val">8</span><span class="badge neutral">较昨日持平</span></div><div class="foot">管理员 · 财务 · 销售 等</div></el-card></el-col>
      <el-col :span="6"><el-card shadow="never" class="info-card"><div class="info-card-header"><div class="info-card-icon bg-green"><el-icon :size="16"><CircleCheckFilled /></el-icon></div><span class="info-card-label">通过率</span><span class="subtag green">良好</span></div><div class="val-row"><span class="val green">98%</span><span class="badge neutral">较昨日持平</span></div><div class="foot">审核通过率</div></el-card></el-col>
      <el-col :span="6"><el-card shadow="never" class="info-card"><div class="info-card-header"><div class="info-card-icon bg-red"><el-icon :size="16"><WarningFilled /></el-icon></div><span class="info-card-label">被拒绝</span><span class="subtag danger-tag">异常</span></div><div class="val-row"><span class="val red">3</span><span class="badge neutral">较昨日持平</span></div><div class="foot">权限不足拒绝</div></el-card></el-col>
    </el-row>

    <el-card v-if="activeTab === '审计日志'" shadow="never">
      <el-table :data="auditLogs" stripe>
        <el-table-column label="时间" prop="time" width="170" />
        <el-table-column label="用户" prop="user" width="80" />
        <el-table-column label="角色" width="100"><template #default="{ row }"><el-tag size="small" effect="plain">{{ row.role }}</el-tag></template></el-table-column>
        <el-table-column label="操作" prop="operation" width="100" />
        <el-table-column label="对象" prop="object" min-width="130" />
        <el-table-column label="范围" prop="range" width="120" />
        <el-table-column label="结果" width="100"><template #default="{ row }"><el-tag :type="row.result === '成功' ? 'success' : 'danger'" size="small" effect="plain">{{ row.result }}</el-tag></template></el-table-column>
        <el-table-column label="IP" prop="ip" width="130" />
      </el-table>
    </el-card>

    <el-card v-if="activeTab === '角色管理'" shadow="never">
      <div v-for="role in roles" :key="role.name" class="role-item">
        <div class="role-left"><div :class="['role-icon', role.bg]"><el-icon :size="16"><component :is="role.icon" /></el-icon></div><div><div class="role-name">{{ role.name }}</div><div class="role-desc">{{ role.desc }}</div></div></div>
        <div class="role-right"><el-tag size="small" effect="plain">{{ role.count }} 人</el-tag><el-button link size="small">编辑</el-button><el-button link size="small">查看成员</el-button></div>
      </div>
    </el-card>

    <el-card v-if="activeTab === '敏感字段'" shadow="never">
      <el-table :data="sensitiveFields" stripe>
        <el-table-column label="字段名" width="160"><template #default="{ row }"><span class="mono">{{ row.field }}</span></template></el-table-column>
        <el-table-column label="数据集" prop="dataset" min-width="140" />
        <el-table-column label="类型" width="100"><template #default="{ row }"><el-tag type="danger" size="small" effect="plain">{{ row.type }}</el-tag></template></el-table-column>
        <el-table-column label="脱敏方式" prop="masking" width="140" />
        <el-table-column label="可访问角色" prop="roles" min-width="160" />
        <el-table-column label="操作" width="80" fixed="right"><template #default><el-button link type="primary" :icon="Edit" /></template></el-table-column>
      </el-table>
    </el-card>

    <el-card v-if="activeTab === '用户管理' || activeTab === '数据集权限'" shadow="never">
      <el-empty :description="activeTab + ' 功能即将上线'" />
    </el-card>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { Search, Plus, View, User, Lock, CircleCheckFilled, WarningFilled, Edit, Coin, Upload, Service } from '@element-plus/icons-vue'

const activeTab = ref('审计日志')
const searchTerm = ref('')
const tabs = ['用户管理', '角色管理', '数据集权限', '敏感字段', '审计日志']

const actionLabel: Record<string, string> = { '用户管理': '添加用户', '角色管理': '创建角色', '数据集权限': '配置权限', '敏感字段': '标记敏感字段' }

const auditLogs = [
  { id: '1', time: '2026-06-29 10:15', user: '张三', role: '管理员', operation: '数据查询', object: '销售订单表', range: '全部字段', tool: 'Agent 查询', result: '成功', ip: '192.168.1.100' },
  { id: '2', time: '2026-06-29 10:10', user: '李四', role: '财务部门', operation: '数据导出', object: '财务月报表', range: '500 条记录', tool: '手动导出', result: '成功', ip: '192.168.1.101' },
  { id: '3', time: '2026-06-29 10:05', user: '王五', role: '普通用户', operation: '数据查询', object: '每日考勤表', range: '特定记录', tool: 'Agent 查询', result: '权限不足', ip: '192.168.1.102' },
]

const roles = [
  { name: '管理员', desc: '系统全部权限', count: 2, bg: 'bg-blue', icon: User, color: '' },
  { name: '财务部门', desc: '财务数据读写权限', count: 5, bg: 'bg-green', icon: Coin, color: '' },
  { name: '销售部门', desc: '销售数据读写权限', count: 8, bg: 'bg-purple', icon: Upload, color: '' },
  { name: 'HR部门', desc: '人事数据读写权限', count: 3, bg: 'bg-orange', icon: Service, color: '' },
]

const sensitiveFields = [
  { id: '1', field: 'employee_salary', dataset: '员工信息表', type: '薪资', masking: '脱敏显示(前缀)', roles: '管理员, HR部门' },
  { id: '2', field: 'phone_number', dataset: '客户信息表', type: '个人信息', masking: '部分隐藏', roles: '管理员, 销售部门' },
  { id: '3', field: 'bank_account', dataset: '财务信息表', type: '金融信息', masking: '完全隐藏', roles: '管理员' },
]
</script>

<style lang="scss" scoped>
.perm-page { display: flex; flex-direction: column; gap: 20px; }
.tab-bar { display: flex; gap: 0; border-bottom: 1px solid $color-border; }
.tab-btn { padding: 10px 16px; border: none; background: none; font-size: $font-size-base; color: $color-text-secondary; cursor: pointer; border-bottom: 2px solid transparent; &:hover { color: $color-text-primary; } &.active { color: $color-primary; border-bottom-color: $color-primary; font-weight: $font-weight-medium; } }
.toolbar { display: flex; align-items: center; gap: 12px; }
.search-input { width: 280px; }
.spacer { flex: 1; }
.stat-row { margin: 0 !important; :deep(.el-col) { padding-left: 8px !important; padding-right: 8px !important; } :deep(.el-col:first-child) { padding-left: 0 !important; } :deep(.el-col:last-child) { padding-right: 0 !important; } }
.info-card { :deep(.el-card__body) { padding: 20px; display: flex; flex-direction: column; gap: 8px; } }
.info-card-header { display: flex; align-items: center; gap: 6px; }
.info-card-icon { width: 32px; height: 32px; border-radius: 8px; display: flex; align-items: center; justify-content: center; &.bg-blue { background: #dbeafe; color: $color-primary; } &.bg-green { background: #dcfce7; color: $color-success; } &.bg-yellow { background: #fef3c7; color: $color-warning; } &.bg-red { background: #fee2e2; color: $color-danger; } &.bg-purple { background: #ede9fe; color: #7c3aed; } &.bg-orange { background: #fff7ed; color: #ea580c; } }
.info-card-label { font-size: $font-size-base; color: $color-text-secondary; }
.subtag { font-size: $font-size-xs; padding: 1px 6px; border-radius: 4px; margin-left: auto; white-space: nowrap; background: #f3f4f6; color: $color-text-placeholder; &.green { color: $color-success; background: #f0fdf4; } &.danger-tag { color: $color-danger; background: #fee2e2; border: 1px solid #fecaca; } }
.val-row { display: flex; align-items: baseline; gap: 8px; }
.val { font-size: 28px; font-weight: $font-weight-bold; color: $color-text-primary; &.green { color: $color-success; } &.red { color: $color-danger; } }
.badge { font-size: $font-size-xs; padding: 1px 6px; border-radius: 4px; &.green-bg { color: $color-success; background: #f0fdf4; } &.neutral { color: $color-text-placeholder; background: #f3f4f6; } }
.foot { font-size: $font-size-xs; color: $color-text-placeholder; }

.role-item { display: flex; align-items: center; justify-content: space-between; padding: 16px; border: 1px solid $color-border; border-radius: $radius-base; margin-bottom: 8px; }
.role-left { display: flex; align-items: center; gap: 12px; }
.role-icon { width: 40px; height: 40px; border-radius: 10px; display: flex; align-items: center; justify-content: center; }
.role-name { font-size: $font-size-base; font-weight: $font-weight-medium; }
.role-desc { font-size: $font-size-sm; color: $color-text-secondary; }
.role-right { display: flex; align-items: center; gap: 8px; }
.mono { font-family: $font-family-mono; font-size: $font-size-sm; }
</style>
