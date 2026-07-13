<template>
  <div class="sem-page">
    <div class="tab-bar">
      <button v-for="tab in tabs" :key="tab" class="tab-btn" :class="{ active: activeTab === tab }" @click="activeTab = tab">{{ tab }}</button>
    </div>

    <div class="toolbar">
      <el-input v-model="searchTerm" placeholder="搜索..." :prefix-icon="Search" class="search-input" clearable />
      <div class="spacer" />
      <el-button type="primary" :icon="Plus">{{ actionLabel[activeTab] }}</el-button>
    </div>

    <el-row :gutter="16" class="stat-row">
      <el-col :span="6"><el-card shadow="never" class="info-card"><div class="info-card-header"><div class="info-card-icon bg-indigo"><el-icon :size="16"><Service /></el-icon></div><span class="info-card-label">业务对象</span><span class="subtag">已建模</span></div><div class="val-row"><span class="val">3</span><span class="badge neutral">较昨日持平</span></div><div class="foot">订单 · 客户 · 产品</div></el-card></el-col>
      <el-col :span="6"><el-card shadow="never" class="info-card"><div class="info-card-header"><div class="info-card-icon bg-blue"><el-icon :size="16"><Collection /></el-icon></div><span class="info-card-label">对象属性</span><span class="subtag">已定义</span></div><div class="val-row"><span class="val">28</span><span class="badge neutral">较昨日持平</span></div><div class="foot">全部已映射</div></el-card></el-col>
      <el-col :span="6"><el-card shadow="never" class="info-card"><div class="info-card-header"><div class="info-card-icon bg-green"><el-icon :size="16"><Connection /></el-icon></div><span class="info-card-label">语义关系</span><span class="subtag green">健康</span></div><div class="val-row"><span class="val green">56</span><span class="badge neutral">较昨日持平</span></div><div class="foot">已确认</div></el-card></el-col>
      <el-col :span="6"><el-card shadow="never" class="info-card"><div class="info-card-header"><div class="info-card-icon bg-purple"><el-icon :size="16"><Link /></el-icon></div><span class="info-card-label">数据映射</span><span class="subtag">待确认</span></div><div class="val-row"><span class="val">3</span><span class="badge neutral">较昨日持平</span></div><div class="foot">1 个待确认</div></el-card></el-col>
    </el-row>

    <el-card v-if="activeTab === '业务对象'" shadow="never">
      <el-table :data="semanticObjects" stripe>
        <el-table-column label="对象编码" width="130"><template #default="{ row }"><span class="mono">{{ row.code }}</span></template></el-table-column>
        <el-table-column label="对象名称" prop="name" min-width="120" />
        <el-table-column label="描述" prop="description" min-width="200" />
        <el-table-column label="属性数" prop="attrCount" width="80" align="center" />
        <el-table-column label="关系数" prop="relCount" width="80" align="center" />
        <el-table-column label="操作" width="80" fixed="right"><template #default><el-button link type="primary" :icon="Edit" /></template></el-table-column>
      </el-table>
    </el-card>

    <el-card v-if="activeTab === '语义关系'" shadow="never">
      <el-table :data="semanticRelations" stripe>
        <el-table-column label="关系名称" prop="name" min-width="100" />
        <el-table-column label="主体对象" width="100"><template #default="{ row }"><el-tag size="small" effect="plain">{{ row.subject }}</el-tag></template></el-table-column>
        <el-table-column label="客体对象" width="100"><template #default="{ row }"><el-tag size="small" effect="plain">{{ row.object }}</el-tag></template></el-table-column>
        <el-table-column label="方向" prop="direction" width="80" />
        <el-table-column label="类型" prop="type" width="80" />
        <el-table-column label="Agent可用" width="100"><template #default="{ row }"><el-tag :type="row.agentEnabled ? 'success' : 'info'" size="small" effect="plain">{{ row.agentEnabled ? '是' : '否' }}</el-tag></template></el-table-column>
        <el-table-column label="操作" width="80"><template #default><el-button link type="primary" :icon="Edit" /></template></el-table-column>
      </el-table>
    </el-card>

    <el-card v-if="activeTab === '数据映射'" shadow="never">
      <el-table :data="dataMappings" stripe>
        <el-table-column label="语义对象/属性" prop="semantic" min-width="160" />
        <el-table-column label="来源表" width="140"><template #default="{ row }"><span class="mono">{{ row.sourceTable }}</span></template></el-table-column>
        <el-table-column label="来源字段" width="140"><template #default="{ row }"><span class="mono">{{ row.sourceField }}</span></template></el-table-column>
        <el-table-column label="转换" prop="transform" width="100" />
        <el-table-column label="可信度" width="90"><template #default="{ row }"><el-tag :type="row.confidence === '高' ? 'success' : 'warning'" size="small" effect="plain">{{ row.confidence }}</el-tag></template></el-table-column>
        <el-table-column label="状态" width="90"><template #default="{ row }"><el-tag :type="row.status === '已确认' ? 'success' : 'warning'" size="small" effect="plain">{{ row.status }}</el-tag></template></el-table-column>
        <el-table-column label="操作" width="120" fixed="right"><template #default><el-button link type="primary" size="small">确认</el-button><el-button link type="primary" size="small">编辑</el-button></template></el-table-column>
      </el-table>
    </el-card>

    <el-card v-if="activeTab === '行动策略'" shadow="never">
      <el-table :data="actionPolicies" stripe>
        <el-table-column label="对象类型" width="100"><template #default="{ row }"><el-tag size="small" effect="plain">{{ row.objectType }}</el-tag></template></el-table-column>
        <el-table-column label="允许行动" prop="allowedActions" min-width="140" />
        <el-table-column label="禁止行动" min-width="140"><template #default="{ row }"><span class="text-danger">{{ row.forbiddenActions }}</span></template></el-table-column>
        <el-table-column label="风险等级" width="100"><template #default="{ row }"><el-tag :type="row.riskLevel === '高' ? 'danger' : row.riskLevel === '中' ? 'warning' : 'success'" size="small" effect="plain">{{ row.riskLevel }}</el-tag></template></el-table-column>
        <el-table-column label="需确认" width="100"><template #default="{ row }"><el-tag :type="row.requireConfirm ? 'warning' : 'info'" size="small" effect="plain">{{ row.requireConfirm ? '是' : '否' }}</el-tag></template></el-table-column>
        <el-table-column label="操作" width="80"><template #default><el-button link type="primary" :icon="Edit" /></template></el-table-column>
      </el-table>
    </el-card>

    <el-card v-if="activeTab === '对象属性'" shadow="never">
      <el-empty description="对象属性管理功能即将上线" />
    </el-card>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { Search, Plus, Edit, Service, Collection, Connection, Link } from '@element-plus/icons-vue'

const activeTab = ref('业务对象')
const searchTerm = ref('')
const tabs = ['业务对象', '对象属性', '语义关系', '数据映射', '行动策略']
const actionLabel: Record<string, string> = { '业务对象': '创建业务对象', '对象属性': '创建属性', '语义关系': '创建关系', '数据映射': '创建映射', '行动策略': '配置策略' }

const semanticObjects = [
  { code: 'ORDER', name: '订单', description: '销售订单业务对象', attrCount: 8, relCount: 12 },
  { code: 'CUSTOMER', name: '客户', description: '客户信息业务对象', attrCount: 10, relCount: 8 },
  { code: 'PRODUCT', name: '产品', description: '产品信息业务对象', attrCount: 10, relCount: 6 },
]

const semanticRelations = [
  { name: '下单', subject: '客户', object: '订单', direction: '单向', type: '创建', agentEnabled: true },
  { name: '包含', subject: '订单', object: '产品', direction: '多对多', type: '关联', agentEnabled: true },
  { name: '属于', subject: '产品', object: '分类', direction: '多对一', type: '归属', agentEnabled: false },
]

const dataMappings = [
  { semantic: '订单.订单ID', sourceTable: 'sales_orders', sourceField: 'order_id', transform: '直接映射', confidence: '高', status: '已确认' },
  { semantic: '订单.订单金额', sourceTable: 'sales_orders', sourceField: 'amount', transform: '直接映射', confidence: '高', status: '已确认' },
  { semantic: '客户.客户名称', sourceTable: 'customer_info', sourceField: 'name', transform: 'TRIM函数', confidence: '中', status: '待确认' },
]

const actionPolicies = [
  { objectType: '订单', allowedActions: '查询, 创建', forbiddenActions: '删除', riskLevel: '中', requireConfirm: false },
  { objectType: '客户', allowedActions: '查询', forbiddenActions: '修改, 删除', riskLevel: '高', requireConfirm: true },
  { objectType: '产品', allowedActions: '查询', forbiddenActions: '修改, 删除, 创建', riskLevel: '低', requireConfirm: false },
]
</script>

<style lang="scss" scoped>
.sem-page { display: flex; flex-direction: column; gap: 20px; }
.tab-bar { display: flex; gap: 0; border-bottom: 1px solid $color-border; }
.tab-btn { padding: 10px 16px; border: none; background: none; font-size: $font-size-base; color: $color-text-secondary; cursor: pointer; border-bottom: 2px solid transparent; &:hover { color: $color-text-primary; } &.active { color: $color-primary; border-bottom-color: $color-primary; font-weight: $font-weight-medium; } }
.toolbar { display: flex; align-items: center; gap: 12px; }
.search-input { width: 280px; }
.spacer { flex: 1; }
.stat-row { margin: 0 !important; :deep(.el-col) { padding-left: 8px !important; padding-right: 8px !important; } :deep(.el-col:first-child) { padding-left: 0 !important; } :deep(.el-col:last-child) { padding-right: 0 !important; } }
.info-card { :deep(.el-card__body) { padding: 20px; display: flex; flex-direction: column; gap: 8px; } }
.info-card-header { display: flex; align-items: center; gap: 6px; }
.info-card-icon { width: 32px; height: 32px; border-radius: 8px; display: flex; align-items: center; justify-content: center; &.bg-indigo { background: #e0e7ff; color: #4f46e5; } &.bg-blue { background: #dbeafe; color: $color-primary; } &.bg-green { background: #dcfce7; color: $color-success; } &.bg-purple { background: #ede9fe; color: #7c3aed; } }
.info-card-label { font-size: $font-size-base; color: $color-text-secondary; }
.subtag { font-size: $font-size-xs; padding: 1px 6px; border-radius: 4px; margin-left: auto; white-space: nowrap; background: #f3f4f6; color: $color-text-placeholder; &.green { color: $color-success; background: #f0fdf4; } }
.val-row { display: flex; align-items: baseline; gap: 8px; }
.val { font-size: 28px; font-weight: $font-weight-bold; color: $color-text-primary; &.green { color: $color-success; } }
.badge { font-size: $font-size-xs; padding: 1px 6px; border-radius: 4px; &.neutral { color: $color-text-placeholder; background: #f3f4f6; } }
.foot { font-size: $font-size-xs; color: $color-text-placeholder; }
.mono { font-family: $font-family-mono; font-size: $font-size-sm; }
.text-danger { color: $color-danger; }
</style>
