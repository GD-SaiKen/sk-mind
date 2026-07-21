<template>
  <div class="page-layout">
    <Index
      title="Agent 数据服务"
      :breadcrumb="[{ label: '首页', to: '/' }, { label: 'Agent 服务' }]"
      description="通过自然语言查询已授权的企业数据，查看数据来源、质量状态和调用记录。"
    />

    <TabNav v-model="activeTab" :tabs="tabs" />


    <el-row :gutter="16" class="stat-row">
      <el-col :span="6">
        <el-card shadow="never" class="info-card">
          <div class="info-card-header">
            <div class="info-card-icon bg-pink"><el-icon :size="16"><Service /></el-icon></div>
            <span class="info-card-label">今日查询</span>
            <span class="subtag green">正常</span>
          </div>
          <div class="val-row"><span class="val">156</span><span class="badge green-bg">↑ 12%</span></div>
          <div class="foot"><span>目标 200</span><div class="health-bar"><div class="health-bar-fill" style="width:78%" /></div><span>78%</span></div>
        </el-card>
      </el-col>
      <el-col :span="6">
        <el-card shadow="never" class="info-card">
          <div class="info-card-header">
            <div class="info-card-icon bg-orange"><el-icon :size="16"><CircleCheckFilled /></el-icon></div>
            <span class="info-card-label">成功率</span>
            <span class="subtag danger-tag">⚠ 低于阈值</span>
          </div>
          <div class="val-row"><span class="val orange">96%</span><span class="badge red-bg">↓ 2%</span></div>
          <div class="foot"><span>目标 ≥99%</span><div class="health-bar"><div class="health-bar-fill alert" style="width:96%" /></div><span>96%</span></div>
        </el-card>
      </el-col>
      <el-col :span="6">
        <el-card shadow="never" class="info-card">
          <div class="info-card-header">
            <div class="info-card-icon bg-blue"><el-icon :size="16"><Setting /></el-icon></div>
            <span class="info-card-label">可用工具</span>
            <span class="subtag">已配置</span>
          </div>
          <div class="val-row"><span class="val">5</span><span class="badge neutral">较昨日持平</span></div>
          <div class="foot">查询 · 元数据 · 图谱</div>
        </el-card>
      </el-col>
      <el-col :span="6">
        <el-card shadow="never" class="info-card">
          <div class="info-card-header">
            <div class="info-card-icon bg-green"><el-icon :size="16"><Timer /></el-icon></div>
            <span class="info-card-label">平均响应</span>
            <span class="subtag green">良好</span>
          </div>
          <div class="val-row"><span class="val green">1.2s</span><span class="badge neutral">较昨日持平</span></div>
          <div class="foot">最快 0.3s / 最慢 5.6s</div>
        </el-card>
      </el-col>
    </el-row>

    <div v-if="activeTab === 'Agent查询'" class="query-section">
      <el-card shadow="never" class="query-card">
        <div class="query-input-area">
          <div class="scope-hints">
            <el-alert title="权限范围说明" type="info" :closable="false" show-icon>
              <template #default>
                <p>Agent 仅查询您已被授权的数据，回答依赖平台数据质量，不会自动写回业务系统。</p>
              </template>
            </el-alert>
          </div>
          <el-input v-model="query" type="textarea" :rows="3" placeholder="输入你的问题，例如：上个月销售额最高的前10个客户是谁？" class="query-textarea" />
          <el-button type="primary" size="large" :icon="Promotion" class="send-btn" @click="submitQuery">发送查询</el-button>
        </div>
        <div v-if="showAnswer" class="answer-area">
          <h4>查询结果</h4>
          <div class="answer-sql">生成 SQL: SELECT customer_name, SUM(amount) as total FROM sales_orders WHERE order_date BETWEEN '2026-06-01' AND '2026-06-30' GROUP BY customer_name ORDER BY total DESC LIMIT 10</div>
          <el-table :data="mockResult" stripe class="result-table">
            <el-table-column label="排名" type="index" width="60" />
            <el-table-column label="客户名称" prop="customer" />
            <el-table-column label="销售额" prop="amount" />
          </el-table>
          <div class="answer-meta">
            <div class="answer-meta-row"><span class="meta-label">数据来源:</span><span>销售订单表、客户信息表</span></div>
            <div class="answer-meta-row"><span class="meta-label">更新时间:</span><span>2026-07-10 09:30</span></div>
            <div class="answer-meta-row"><span class="meta-label">质量状态:</span><el-tag type="success" effect="plain" size="small">正常</el-tag></div>
            <div class="answer-meta-row"><span class="meta-label">使用工具:</span><span>受控数据查询, 聚合计算</span></div>
            <div class="answer-meta-row"><span class="meta-label">说明:</span><span class="text-warning">以上数据基于已授权数据集，可能与实际业务系统存在延迟</span></div>
          </div>
        </div>
      </el-card>
      <el-card shadow="never" class="suggest-card">
        <h4>示例问题</h4>
        <div class="suggest-list">
          <el-button v-for="q in suggestions" :key="q" plain class="suggest-btn" @click="query = q">{{ q }}</el-button>
        </div>
      </el-card>
    </div>

    <Crud v-if="activeTab === '工具管理'" :filter-items="searchFilterItems" v-model:filter-values="searchValues" :pagination="toolsPagination">
      <template #filters-actions>
        <el-button type="primary" :icon="Edit">配置工具</el-button>
      </template>
      <template #table><Table :columns="toolsColumns" :data="pagedTools" /></template>
    </Crud>

    <Crud v-if="activeTab === '调用记录'" :filter-items="searchFilterItems" v-model:filter-values="searchValues" :pagination="callsPagination">
      <template #filters-actions>
        <el-button plain>导出记录</el-button>
      </template>
      <template #table><Table :columns="callsColumns" :data="pagedCalls" /></template>
    </Crud>
  </div>
</template>

<script setup lang="ts">
import { computed, reactive, ref, watch } from 'vue'
import { Search, Edit, Service, CircleCheckFilled, Setting, Timer, Promotion, View } from '@element-plus/icons-vue'
import TabNav from '@/components/tab-nav/index.vue'
import type { TabItem } from '@/components/tab-nav/types'
import Index from '@/components/page-header/index.vue'
import { Crud, Table } from '@/components/crud'
import type { ColumnSchema, FilterItem } from '@/components/crud'

const activeTab = ref('Agent查询')
const searchFilterItems: FilterItem[] = [{ key: 'keyword', placeholder: '搜索...', width: '260px' }]
const searchValues = ref<Record<string, any>>({})
const query = ref('')
const showAnswer = ref(false)
const tabs: TabItem[] = [
  { key: 'Agent查询', label: 'Agent查询' },
  { key: '工具管理', label: '工具管理' },
  { key: '调用记录', label: '调用记录' },
]

const suggestions = ['上个月销售额最高的前10个客户是谁?', '生产线A的平均良品率是多少?', '本周有哪些订单状态异常?']

const mockResult = [
  { customer: '先锋科技股份有限公司', amount: '¥756,200' },
  { customer: '深圳创新材料集团', amount: '¥623,500' },
  { customer: '上海精密仪器有限公司', amount: '¥498,800' },
]

const agentTools = [
  { name: '数据目录检索', type: '查询工具', datasets: '全部', permission: '所有用户', risk: '低' },
  { name: '受控数据查询', type: '查询工具', datasets: '销售订单表, 生产记录表', permission: '继承用户权限', risk: '中' },
  { name: '质量状态查询', type: '元数据工具', datasets: '全部', permission: '所有用户', risk: '低' },
  { name: '语义检索', type: '查询工具', datasets: '语义对象', permission: '所有用户', risk: '低' },
  { name: '图谱查询', type: '图谱工具', datasets: '关系图谱', permission: '所有用户', risk: '低' },
]

const agentCalls = [
  { time: '2026-06-29 10:15', user: '张三', question: '上个月销售额最高的前10个客户?', tools: '受控查询, 聚合', datasets: '销售订单表, 客户表', status: '成功' },
  { time: '2026-06-29 10:10', user: '李四', question: '生产线A良品率?', tools: '受控查询', datasets: '生产记录表', status: '成功' },
  { time: '2026-06-29 10:05', user: '王五', question: '考勤表空值记录?', tools: '质量查询', datasets: '每日考勤表', status: '失败' },
]

const filteredTools = computed(() => agentTools.filter(t => t.name.includes(searchValues.value.keyword || '') || t.type.includes(searchValues.value.keyword || '')))
const filteredCalls = computed(() => agentCalls.filter(c => c.user.includes(searchValues.value.keyword || '') || c.question.includes(searchValues.value.keyword || '')))

function slicePage<T>(data: T[], page: number, size: number) { return data.slice((page - 1) * size, page * size) }

const toolsPagination = reactive({ page: 1, pageSize: 20, total: 0, onPageChange() {}, onSizeChange() {} })
const pagedTools = computed(() => slicePage(filteredTools.value, toolsPagination.page, toolsPagination.pageSize))
watch([filteredTools, () => toolsPagination.pageSize], () => { toolsPagination.total = filteredTools.value.length })

const callsPagination = reactive({ page: 1, pageSize: 20, total: 0, onPageChange() {}, onSizeChange() {} })
const pagedCalls = computed(() => slicePage(filteredCalls.value, callsPagination.page, callsPagination.pageSize))
watch([filteredCalls, () => callsPagination.pageSize], () => { callsPagination.total = filteredCalls.value.length })

const toolsColumns: ColumnSchema[] = [
  { type: 'text', prop: 'name', label: '工具名称', minWidth: 160 },
  { type: 'tag', prop: 'type', label: '类型', width: 100 },
  { type: 'text', prop: 'datasets', label: '关联数据集', minWidth: 160 },
  { type: 'text', prop: 'permission', label: '权限', minWidth: 130 },
  { type: 'tag', prop: 'risk', label: '风险', width: 80, tagMap: { '低': 'success', '中': 'warning', '高': 'danger' } },
  { type: 'tag', prop: 'status', label: '状态', width: 80, tagType: 'success', formatter: () => '启用' },
  { type: 'action', label: '操作', width: 80, buttons: [{ label: '编辑', icon: Edit, onClick: () => {} }] },
]

const callsColumns: ColumnSchema[] = [
  { type: 'text', prop: 'time', label: '时间', width: 170 },
  { type: 'text', prop: 'user', label: '用户', width: 80 },
  { type: 'text', prop: 'question', label: '问题', minWidth: 200 },
  { type: 'text', prop: 'tools', label: '工具', width: 120 },
  { type: 'text', prop: 'datasets', label: '数据集', width: 140 },
  { type: 'tag', prop: 'status', label: '状态', width: 80, tagMap: { '成功': 'success', '失败': 'danger' } },
  { type: 'action', label: '操作', width: 90, buttons: [{ label: '查看详情', icon: View, onClick: () => {} }] },
]

function submitQuery() { if (query.value.trim()) showAnswer.value = true }
</script>

<style lang="scss" scoped>
.tab-btn { padding: 10px 16px; border: none; background: none; font-size: $font-size-base; color: $color-text-secondary; cursor: pointer; border-bottom: 2px solid transparent; &:hover { color: $color-text-primary; } &.active { color: $color-primary; border-bottom-color: $color-primary; font-weight: $font-weight-medium; } }
.stat-row { margin: 0 !important; :deep(.el-col) { padding-left: 8px !important; padding-right: 8px !important; } :deep(.el-col:first-child) { padding-left: 0 !important; } :deep(.el-col:last-child) { padding-right: 0 !important; } }
.info-card { :deep(.el-card__body) { display: flex; flex-direction: column; gap: 8px; padding: 20px; } }
.info-card-header { display: flex; align-items: center; gap: 6px; }
.info-card-icon { display: flex; align-items: center; justify-content: center; width: 32px; height: 32px; border-radius: 8px; &.bg-pink { background: #fce7f3; color: #db2777; } &.bg-orange { background: #fff7ed; color: #ea580c; } &.bg-blue { background: #dbeafe; color: $color-primary; } &.bg-green { background: #dcfce7; color: $color-success; } }
.info-card-label { font-size: $font-size-base; color: $color-text-secondary; }
.subtag { font-size: $font-size-xs; padding: 1px 6px; border-radius: 4px; margin-left: auto; white-space: nowrap; background: #f3f4f6; color: $color-text-placeholder; &.green { color: $color-success; background: #f0fdf4; } &.danger-tag { color: $color-danger; background: #fee2e2; border: 1px solid #fecaca; } }
.val-row { display: flex; align-items: baseline; gap: 8px; }
.val { font-size: 28px; font-weight: $font-weight-bold; color: $color-text-primary; &.green { color: $color-success; } &.orange { color: #ea580c; } }
.badge { font-size: $font-size-xs; padding: 1px 6px; border-radius: 4px; &.green-bg { color: $color-success; background: #f0fdf4; } &.red-bg { color: $color-danger; background: #fee2e2; } &.neutral { color: $color-text-placeholder; background: #f3f4f6; } }
.foot { display: flex; align-items: center; gap: 6px; font-size: $font-size-xs; color: $color-text-placeholder; }
.health-bar { flex: 1; height: 4px; background: #f3f4f6; border-radius: 2px; overflow: hidden; }
.health-bar-fill { height: 100%; background: $color-success; border-radius: 2px; &.alert { background: #f97316; } }
.query-section { display: flex; gap: 16px; }
.query-card { flex: 1; }
.query-input-area { display: flex; flex-direction: column; gap: 12px; }
.query-textarea { :deep(textarea) { font-size: $font-size-base; } }
.send-btn { align-self: flex-end; }
.answer-area { border-top: 1px solid $color-border; margin-top: 16px; padding-top: 16px; h4 { margin-bottom: 12px; } }
.answer-sql { padding: 12px; background: #f3f4f6; border-radius: $radius-base; font-family: $font-family-mono; font-size: $font-size-xs; color: $color-text-secondary; margin-bottom: 12px; word-break: break-all; }
.result-table { margin-bottom: 8px; }
.answer-meta { display: flex; flex-direction: column; gap: 6px; font-size: $font-size-sm; color: $color-text-secondary; }
.answer-meta-row { display: flex; align-items: center; gap: 8px; }
.meta-label { color: $color-text-placeholder; flex-shrink: 0; }
.scope-hints { :deep(.el-alert__content) { p { margin: 0; font-size: $font-size-sm; } } }
.text-warning { color: $color-warning; }
.suggest-card { width: 280px; flex-shrink: 0; h4 { margin-bottom: 12px; font-size: $font-size-base; } }
.suggest-list { display: flex; flex-direction: column; gap: 8px; }
.suggest-btn { justify-content: flex-start; text-align: left; white-space: normal; height: auto; padding: 8px 12px; }
</style>
