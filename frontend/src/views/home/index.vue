<template>
  <div class="page-layout home-page">
    <Index
      title="首页"
      :breadcrumb="[{ label: '首页' }]"
      description="平台运行状态总览，快速了解数据源、接入、质量、语义和 Agent 服务的整体情况，发现异常并及时处理。"
    />

    <!-- 状态总览卡片 -->
    <div class="cards-grid">
      <el-card
        v-for="card in statusCards"
        :key="card.label"
        shadow="hover"
        class="stat-card clickable"
        @click="router.push(card.linkTo)"
      >
        <div class="card-header-row">
          <div class="card-title-wrap">
            <div :class="['card-icon', card.iconBg]">
              <el-icon :size="16"><component :is="card.icon" /></el-icon>
            </div>
            <span class="card-title">{{ card.label }}</span>
          </div>
          <span :class="['status-badge', card.statusType]">
            <span :class="['status-dot', card.statusType]" />
            {{ card.statusText }}
          </span>
        </div>

        <div class="card-stats-row">
          <div v-for="stat in card.stats" :key="stat.label" class="card-stat-item">
            <div class="card-stat-value" :style="{ color: stat.color }">{{ stat.value }}</div>
            <div class="card-stat-label">{{ stat.label }}</div>
          </div>
        </div>

        <div class="card-footer-row">
          <span class="card-meta">{{ card.meta }}</span>
          <router-link :to="card.linkTo" class="card-link">
            查看详情
            <el-icon :size="12"><ArrowRight /></el-icon>
          </router-link>
        </div>
      </el-card>
    </div>

    <!-- 待处理事项 -->
    <h2 class="section-title">待处理事项</h2>
    <div class="pending-list">
      <div v-for="item in pendingItems" :key="item.id" :class="['pending-item', item.level]" @click="router.push(item.linkTo)" style="cursor: pointer;">
        <div class="pending-item-left">
          <el-icon :size="18" :class="item.level === 'error' ? 'text-danger' : 'text-warning'">
            <component :is="item.icon" />
          </el-icon>
          <div class="pending-item-info">
            <div class="pending-item-title">{{ item.title }}</div>
            <div class="pending-item-desc">{{ item.desc }}</div>
          </div>
        </div>
        <el-tag :type="item.level === 'error' ? 'danger' : 'warning'" effect="plain">
          {{ item.tag }}
        </el-tag>
      </div>
    </div>

    <!-- 最近接入任务 -->
    <h2 class="section-title">最近接入任务</h2>
    <div class="recent-list">
      <div v-for="task in recentTasks" :key="task.id" class="recent-item" @click="router.push(task.linkTo)" style="cursor: pointer;">
        <div class="recent-item-left">
          <el-icon :size="18" :class="task.status === 'success' ? 'text-success' : 'text-warning'">
            <component :is="task.icon" />
          </el-icon>
          <div class="recent-item-info">
            <div class="recent-item-title">{{ task.title }}</div>
            <div class="recent-item-time">{{ task.time }} · {{ task.desc }}</div>
          </div>
        </div>
        <el-tag :type="task.tagType" effect="plain">{{ task.tag }}</el-tag>
      </div>
    </div>

    <!-- 快捷入口 -->
    <h2 class="section-title">快捷入口</h2>
    <div class="quick-actions">
      <router-link v-for="action in quickActions" :key="action.label" :to="action.to" class="quick-action-btn">
        <el-icon :size="16"><component :is="action.icon" /></el-icon>
        <span>{{ action.label }}</span>
      </router-link>
    </div>

    <!-- 系统信息 -->
    <el-card shadow="never" class="sys-status-card">
      <template #header>
        <div class="sys-header">
          <el-icon :size="16"><Setting /></el-icon>
          <span>系统信息</span>
        </div>
      </template>
      <el-descriptions :column="3" border>
        <el-descriptions-item label="后端服务">
          <el-tag :type="healthStatus === '运行正常' ? 'success' : 'danger'">{{ healthStatus }}</el-tag>
        </el-descriptions-item>
        <el-descriptions-item label="版本">{{ appVersion || '-' }}</el-descriptions-item>
        <el-descriptions-item label="运行环境">开发环境</el-descriptions-item>
      </el-descriptions>
    </el-card>
  </div>
</template>

<script setup lang="ts">
import { onMounted, ref } from 'vue'
import { useRouter } from 'vue-router'
import {
  ArrowRight, Coin, Upload, Collection, CircleCheck,
  Cpu, Service, WarningFilled, Clock, CircleCheckFilled, Setting,
} from '@element-plus/icons-vue'
import Index from '@/components/page-header/index.vue'
import { api } from '@/api'

const router = useRouter()

const statusCards = [
  {
    label: '数据源', icon: Coin, iconBg: 'bg-blue', statusType: 'success', statusText: '正常',
    stats: [
      { label: '总数', value: '6', color: '#1f2937' },
      { label: '正常', value: '5', color: '#16a34a' },
      { label: '异常', value: '1', color: '#dc2626' },
    ],
    meta: '连接池 5/10', linkTo: '/data-sources',
  },
  {
    label: '接入任务', icon: Upload, iconBg: 'bg-purple', statusType: 'warning', statusText: '部分异常',
    stats: [
      { label: '成功', value: '2', color: '#16a34a' },
      { label: '部分', value: '1', color: '#ca8a04' },
      { label: '失败', value: '1', color: '#dc2626' },
    ],
    meta: '上次执行：10:30', linkTo: '/ingestion',
  },
  {
    label: '数据表', icon: Collection, iconBg: 'bg-green', statusType: 'success', statusText: '正常',
    stats: [
      { label: '总数', value: '47', color: '#1f2937' },
      { label: 'Agent 开放', value: '38', color: '#16a34a' },
      { label: '新增', value: '3', color: '#4f46e5' },
    ],
    meta: '昨日新增 2 张表', linkTo: '/tables',
  },
  {
    label: '数据质量', icon: CircleCheck, iconBg: 'bg-orange', statusType: 'warning', statusText: '5 条警告',
    stats: [
      { label: '质检通过率', value: '96.4%', color: '#16a34a' },
      { label: '空值率', value: '0.8%', color: '#ca8a04' },
      { label: '待确认', value: '5', color: '#dc2626' },
    ],
    meta: '昨日扫描 1,250 条', linkTo: '/quality',
  },
  {
    label: '语义模型', icon: Cpu, iconBg: 'bg-indigo', statusType: 'success', statusText: '已构建',
    stats: [
      { label: '对象数', value: '3', color: '#1f2937' },
      { label: '关系数', value: '56', color: '#1f2937' },
      { label: '映射数', value: '28', color: '#1f2937' },
    ],
    meta: '最后更新：09:45', linkTo: '/semantic',
  },
  {
    label: 'Agent 服务', icon: Service, iconBg: 'bg-cyan', statusType: 'success', statusText: '运行中',
    stats: [
      { label: '今日调用', value: '128', color: '#1f2937' },
      { label: '成功', value: '124', color: '#16a34a' },
      { label: '失败', value: '4', color: '#dc2626' },
    ],
    meta: '峰值 QPS：12', linkTo: '/agent',
  },
]

const quickActions = [
  { label: '新增数据源', to: '/data-sources', icon: Coin },
  { label: '创建任务', to: '/ingestion', icon: Upload },
  { label: '数据目录', to: '/catalog', icon: Collection },
  { label: '质量检查', to: '/quality', icon: CircleCheck },
  { label: 'Agent 查询', to: '/agent', icon: Service },
]

const pendingItems = [
  { id: 1, level: 'error', title: '接入任务失败: 财务月报导入', desc: 'Excel 解析失败，12 个文件无法导入', tag: '紧急', icon: WarningFilled, linkTo: '/ingestion' },
  { id: 2, level: 'warning', title: '待确认质量问题', desc: '每日考勤表存在 5 条空值记录', tag: '待处理', icon: Clock, linkTo: '/quality' },
  { id: 3, level: 'warning', title: '待确认字段说明', desc: '3 张数据表存在未填写的字段说明', tag: '待处理', icon: Clock, linkTo: '/tables' },
  { id: 4, level: 'warning', title: '待确认关系边', desc: 'AI 生成了 1 条新的实体关系待审核', tag: '待处理', icon: Clock, linkTo: '/graph' },
  { id: 5, level: 'error', title: 'Excel 解析失败: 供应商导入', desc: '模板字段不匹配，3 个文件解析失败', tag: '紧急', icon: WarningFilled, linkTo: '/ingestion' },
]

const recentTasks = [
  { id: 1, title: 'SAP 销售订单同步', time: '2026-06-29 09:30', desc: '成功导入 1,250 条记录', status: 'success', tag: '成功', tagType: 'success', icon: CircleCheckFilled, linkTo: '/ingestion/1' },
  { id: 2, title: 'MES 生产记录拉取', time: '2026-06-29 09:00', desc: '成功导入 856 条记录', status: 'success', tag: '成功', tagType: 'success', icon: CircleCheckFilled, linkTo: '/ingestion/2' },
  { id: 3, title: '考勤数据日同步', time: '2026-06-28 18:00', desc: '成功 320 条，失败 5 条', status: 'warning', tag: '部分成功', tagType: 'warning', icon: WarningFilled, linkTo: '/ingestion/3' },
]

const healthStatus = ref('检查中...')
const appVersion = ref('')

async function checkHealth() {
  try {
    const res = await api.get('/health')
    healthStatus.value = '运行正常'
    appVersion.value = res.data.version ?? ''
  } catch {
    healthStatus.value = '连接失败'
  }
}

onMounted(() => { checkHealth() })
</script>

<style lang="scss" scoped>


.cards-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 20px;
}

@media (max-width: 1100px) { .cards-grid { grid-template-columns: repeat(2, 1fr); } }
@media (max-width: 750px) { .cards-grid { grid-template-columns: 1fr; } }

.stat-card {
  :deep(.el-card__body) { display: flex; flex-direction: column; gap: 12px; padding: 20px; }
  &.clickable { cursor: pointer; }
}

.card-header-row { display: flex; align-items: center; justify-content: space-between; }
.card-title-wrap { display: flex; align-items: center; gap: 8px; }

.card-icon {
  width: 32px; height: 32px; border-radius: 8px;
  display: flex; align-items: center; justify-content: center;
  &.bg-blue { background: #dbeafe; color: #2563eb; }
  &.bg-purple { background: #ede9fe; color: #7c3aed; }
  &.bg-green { background: #dcfce7; color: #16a34a; }
  &.bg-orange { background: #fff7ed; color: #ea580c; }
  &.bg-indigo { background: #e0e7ff; color: #4f46e5; }
  &.bg-cyan { background: #cffafe; color: #0891b2; }
}

.card-title { font-size: 14px; font-weight: 500; color: #1f2937; }

.status-badge {
  display: inline-flex; align-items: center; gap: 4px;
  font-size: 12px; padding: 2px 8px; border-radius: 12px;
  &.success { color: #16a34a; background: #f0fdf4; border: 1px solid #bbf7d0; }
  &.warning { color: #ca8a04; background: #fefce8; border: 1px solid #fef08a; }
}

.status-dot {
  width: 6px; height: 6px; border-radius: 50%; display: inline-block;
  &.success { background: #16a34a; }
  &.warning { background: #ca8a04; }
}

.card-stats-row { display: grid; grid-template-columns: repeat(3, 1fr); gap: 8px; text-align: center; }
.card-stat-value { font-size: 20px; font-weight: 700; }
.card-stat-label { font-size: 12px; color: #9ca3af; margin-top: 2px; }
.card-footer-row { display: flex; align-items: center; justify-content: space-between; }
.card-meta { font-size: 12px; color: #9ca3af; }
.card-link { display: inline-flex; align-items: center; gap: 2px; font-size: 12px; color: #2563eb; text-decoration: none; &:hover { gap: 6px; } }

.section-title {
  font-size: 16px; font-weight: 600; color: #1f2937; margin: 0;
}

.quick-actions {
  display: grid; grid-template-columns: repeat(5, 1fr); gap: 12px;
}

.quick-action-btn {
  display: flex; align-items: center; justify-content: center; gap: 8px;
  padding: 12px 16px; border: 1px solid #e5e7eb; border-radius: 8px;
  color: #374151; font-size: 14px; text-decoration: none; transition: all 0.15s;
  &:hover { background: #f9fafb; border-color: #2563eb; color: #2563eb; }
}

.text-warning { color: #ca8a04; }
.text-danger { color: #dc2626; }
.text-success { color: #16a34a; }

.pending-list, .recent-list { display: flex; flex-direction: column; gap: 8px; }

.pending-item {
  display: flex; align-items: center; justify-content: space-between;
  padding: 12px; border-radius: 8px;
  &.error { background: #fef2f2; border: 1px solid #fecaca; }
  &.warning { background: #fefce8; border: 1px solid #fef08a; }
}

.pending-item-left { display: flex; align-items: center; gap: 12px; }
.pending-item-info, .recent-item-info { display: flex; flex-direction: column; gap: 2px; }
.pending-item-title, .recent-item-title { font-size: 14px; color: #1f2937; font-weight: 500; }
.pending-item-desc, .recent-item-time { font-size: 13px; color: #6b7280; }

.recent-item {
  display: flex; align-items: center; justify-content: space-between;
  padding: 12px; border: 1px solid #e5e7eb; border-radius: 8px;
}
.recent-item-left { display: flex; align-items: center; gap: 12px; }

.sys-status-card { margin-top: 0; }
.sys-header { display: flex; align-items: center; gap: 8px; font-size: 14px; font-weight: 500; }
</style>