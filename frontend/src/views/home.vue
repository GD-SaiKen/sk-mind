<template>
  <div class="home-page">
    <!-- 标签页 -->
    <div class="tab-bar">
      <button
        v-for="tab in tabs"
        :key="tab.key"
        class="tab-btn"
        :class="{ active: activeTab === tab.key }"
        @click="activeTab = tab.key"
      >
        {{ tab.label }}
      </button>
    </div>

    <!-- 运行状态 -->
    <div v-if="activeTab === 'status'" class="tab-content">
      <!-- 状态总览卡片 3x2 -->
      <div class="cards-grid">
        <el-card
          v-for="card in statusCards"
          :key="card.label"
          shadow="hover"
          class="stat-card"
        >
          <!-- 第一层：认知层 -->
          <div class="card-header-row">
            <div class="card-title-wrap">
              <div :class="['card-icon', card.iconBg]">
                <el-icon :size="16">
                  <component :is="card.icon" />
                </el-icon>
              </div>
              <span class="card-title">{{ card.label }}</span>
            </div>
            <span
              :class="['status-badge', card.statusType]"
            >
              <span :class="['status-dot', card.statusType]" />
              {{ card.statusText }}
            </span>
          </div>

          <!-- 第二层：数据层 3列 -->
          <div class="card-stats-row">
            <div
              v-for="stat in card.stats"
              :key="stat.label"
              class="card-stat-item"
            >
              <div class="card-stat-value" :style="{ color: stat.color }">
                {{ stat.value }}
              </div>
              <div class="card-stat-label">{{ stat.label }}</div>
            </div>
          </div>

          <!-- 第三层：元数据+操作 -->
          <div class="card-footer-row">
            <span class="card-meta">{{ card.meta }}</span>
            <router-link :to="card.linkTo" class="card-link">
              查看详情
              <el-icon :size="12"><ArrowRight /></el-icon>
            </router-link>
          </div>
        </el-card>
      </div>

      <!-- 快捷操作 -->
      <div class="section">
        <h3 class="section-title">快捷操作</h3>
        <div class="quick-actions">
          <router-link
            v-for="action in quickActions"
            :key="action.label"
            :to="action.to"
            class="quick-action-btn"
          >
            <el-icon :size="16">
              <component :is="action.icon" />
            </el-icon>
            <span>{{ action.label }}</span>
          </router-link>
        </div>
      </div>
    </div>

    <!-- 待处理事项 -->
    <div v-if="activeTab === 'pending'" class="tab-content">
      <el-card shadow="never" class="pending-section">
        <template #header>
          <div class="section-header-row">
            <el-icon :size="18" class="text-warning"><WarningFilled /></el-icon>
            <span>待处理事项</span>
          </div>
        </template>
        <div class="pending-list">
          <div
            v-for="item in pendingItems"
            :key="item.id"
            :class="['pending-item', item.level]"
          >
            <div class="pending-item-left">
              <el-icon
                :size="18"
                :class="item.level === 'error' ? 'text-danger' : 'text-warning'"
              >
                <component :is="item.icon" />
              </el-icon>
              <div class="pending-item-info">
                <div class="pending-item-title">{{ item.title }}</div>
                <div class="pending-item-desc">{{ item.desc }}</div>
              </div>
            </div>
            <el-tag
              :type="item.level === 'error' ? 'danger' : 'warning'"
              size="small"
              effect="plain"
            >
              {{ item.tag }}
            </el-tag>
          </div>
        </div>
      </el-card>
    </div>

    <!-- 最近任务 -->
    <div v-if="activeTab === 'recent'" class="tab-content">
      <el-card shadow="never">
        <template #header>
          <span>最近接入任务</span>
        </template>
        <div class="recent-list">
          <div
            v-for="task in recentTasks"
            :key="task.id"
            class="recent-item"
          >
            <div class="recent-item-left">
              <el-icon
                :size="18"
                :class="task.status === 'success' ? 'text-success' : 'text-warning'"
              >
                <component :is="task.icon" />
              </el-icon>
              <div class="recent-item-info">
                <div class="recent-item-title">{{ task.title }}</div>
                <div class="recent-item-time">{{ task.time }} · {{ task.desc }}</div>
              </div>
            </div>
            <el-tag
              :type="task.tagType"
              size="small"
              effect="plain"
            >
              {{ task.tag }}
            </el-tag>
          </div>
        </div>
      </el-card>
    </div>

    <!-- 系统状态 -->
    <el-card shadow="never" class="sys-status-card">
      <template #header>
        <span>系统状态</span>
      </template>
      <el-descriptions :column="3" border>
        <el-descriptions-item label="后端服务">
          <el-tag
            :type="healthStatus === '运行正常' ? 'success' : 'danger'"
            size="small"
          >
            {{ healthStatus }}
          </el-tag>
        </el-descriptions-item>
        <el-descriptions-item label="版本">{{ appVersion || '-' }}</el-descriptions-item>
        <el-descriptions-item label="运行环境">开发环境</el-descriptions-item>
      </el-descriptions>
    </el-card>
  </div>
</template>

<script setup lang="ts">
import type { Component } from 'vue'
import { onMounted, ref } from 'vue'
import {
  ArrowRight, Coin, Upload, Collection, CircleCheck,
  Cpu, Service, WarningFilled, Clock, CircleCheckFilled,
} from '@element-plus/icons-vue'
import { api } from '@/api'

const activeTab = ref('status')

const tabs = [
  { key: 'status', label: '运行状态' },
  { key: 'pending', label: '待处理事项' },
  { key: 'recent', label: '最近任务' },
]

const statusCards = [
  {
    label: '数据源',
    icon: Coin,
    iconBg: 'bg-blue',
    statusType: 'success',
    statusText: '正常',
    stats: [
      { label: '运行状态', value: '—', color: '#1f2937' },
      { label: '当前状态', value: '正常', color: '#1f2937' },
      { label: '最后同步', value: '10:00', color: '#1f2937' },
    ],
    meta: '连接池 5/10',
    linkTo: '/data-sources',
  },
  {
    label: '接入任务',
    icon: Upload,
    iconBg: 'bg-purple',
    statusType: 'warning',
    statusText: '部分异常',
    stats: [
      { label: '成功', value: '2', color: '#16a34a' },
      { label: '部分', value: '1', color: '#ca8a04' },
      { label: '失败', value: '1', color: '#dc2626' },
    ],
    meta: '上次执行：10:30',
    linkTo: '/ingestion',
  },
  {
    label: '数据表',
    icon: Collection,
    iconBg: 'bg-green',
    statusType: 'success',
    statusText: '正常',
    stats: [
      { label: '已注册', value: '47', color: '#1f2937' },
      { label: '有数据', value: '38', color: '#1f2937' },
      { label: '新发现', value: '3', color: '#1f2937' },
    ],
    meta: '昨日新增 2 张表',
    linkTo: '/data-browse',
  },
  {
    label: '数据质量',
    icon: CircleCheck,
    iconBg: 'bg-orange',
    statusType: 'warning',
    statusText: '5 条警告',
    stats: [
      { label: '质检通过率', value: '96.4%', color: '#16a34a' },
      { label: '空值率', value: '0.8%', color: '#ca8a04' },
      { label: '待确认', value: '5', color: '#dc2626' },
    ],
    meta: '昨日扫描 1,250 条',
    linkTo: '/quality',
  },
  {
    label: '语义模型',
    icon: Cpu,
    iconBg: 'bg-indigo',
    statusType: 'success',
    statusText: '已构建',
    stats: [
      { label: '领域模型', value: '3', color: '#1f2937' },
      { label: '实体数', value: '28', color: '#1f2937' },
      { label: '关系数', value: '56', color: '#1f2937' },
    ],
    meta: '最后更新：09:45',
    linkTo: '/semantic',
  },
  {
    label: 'Agent 服务',
    icon: Service,
    iconBg: 'bg-cyan',
    statusType: 'success',
    statusText: '运行中',
    stats: [
      { label: '今日调用', value: '128', color: '#1f2937' },
      { label: '成功', value: '124', color: '#16a34a' },
      { label: '平均耗时', value: '1.2s', color: '#1f2937' },
    ],
    meta: '峰值 QPS：12',
    linkTo: '/agent',
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
  {
    id: 1,
    level: 'error',
    title: '接入任务失败: 财务月报导入',
    desc: 'Excel 解析失败，12 个文件无法导入',
    tag: '紧急',
    icon: WarningFilled,
  },
  {
    id: 2,
    level: 'warning',
    title: '待确认质量问题',
    desc: '每日考勤表存在 5 条空值记录',
    tag: '待处理',
    icon: Clock,
  },
]

const recentTasks = [
  {
    id: 1,
    title: 'SAP 销售订单同步',
    time: '2026-06-29 09:30',
    desc: '成功导入 1,250 条记录',
    status: 'success',
    tag: '成功',
    tagType: 'success',
    icon: CircleCheckFilled,
  },
  {
    id: 2,
    title: 'MES 生产记录拉取',
    time: '2026-06-29 09:00',
    desc: '成功导入 856 条记录',
    status: 'success',
    tag: '成功',
    tagType: 'success',
    icon: CircleCheckFilled,
  },
  {
    id: 3,
    title: '考勤数据日同步',
    time: '2026-06-28 18:00',
    desc: '成功 320 条，失败 5 条',
    status: 'warning',
    tag: '部分成功',
    tagType: 'warning',
    icon: WarningFilled,
  },
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

onMounted(() => {
  checkHealth()
})
</script>

<style lang="scss" scoped>
.home-page {
  max-width: 1200px;
}

/* 标签页 */
.tab-bar {
  display: flex;
  gap: 0;
  border-bottom: 1px solid $color-border;
  margin-bottom: 20px;
}

.tab-btn {
  padding: 10px 16px;
  border: none;
  background: none;
  font-size: $font-size-base;
  color: $color-text-secondary;
  cursor: pointer;
  border-bottom: 2px solid transparent;
  transition: all 0.2s;

  &:hover {
    color: $color-text-primary;
  }

  &.active {
    color: $color-primary;
    border-bottom-color: $color-primary;
    font-weight: $font-weight-medium;
  }
}

.tab-content {
  display: flex;
  flex-direction: column;
  gap: 24px;
}

/* 状态卡片网格 */
.cards-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 20px;
}

@media (max-width: 1100px) {
  .cards-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 750px) {
  .cards-grid {
    grid-template-columns: 1fr;
  }
}

.stat-card {
  :deep(.el-card__body) {
    display: flex;
    flex-direction: column;
    gap: 12px;
    padding: 20px;
  }
}

.card-header-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.card-title-wrap {
  display: flex;
  align-items: center;
  gap: 8px;
}

.card-icon {
  width: 32px;
  height: 32px;
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;

  &.bg-blue { background: #dbeafe; color: $color-primary; }
  &.bg-purple { background: #ede9fe; color: #7c3aed; }
  &.bg-green { background: #dcfce7; color: $color-success; }
  &.bg-orange { background: #fff7ed; color: #ea580c; }
  &.bg-indigo { background: #e0e7ff; color: #4f46e5; }
  &.bg-cyan { background: #cffafe; color: #0891b2; }
}

.card-title {
  font-size: $font-size-base;
  font-weight: $font-weight-medium;
  color: $color-text-primary;
}

.status-badge {
  display: inline-flex;
  align-items: center;
  gap: 4px;
  font-size: $font-size-xs;
  padding: 2px 8px;
  border-radius: 12px;

  &.success {
    color: $color-success;
    background: #f0fdf4;
    border: 1px solid #bbf7d0;
  }

  &.warning {
    color: $color-warning;
    background: #fefce8;
    border: 1px solid #fef08a;
  }
}

.status-dot {
  width: 6px;
  height: 6px;
  border-radius: 50%;
  display: inline-block;

  &.success { background: $color-success; }
  &.warning { background: $color-warning; }
}

.card-stats-row {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 8px;
  text-align: center;
}

.card-stat-value {
  font-size: $font-size-xl;
  font-weight: $font-weight-bold;
}

.card-stat-label {
  font-size: $font-size-xs;
  color: $color-text-placeholder;
  margin-top: 2px;
}

.card-footer-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.card-meta {
  font-size: $font-size-xs;
  color: $color-text-placeholder;
}

.card-link {
  display: inline-flex;
  align-items: center;
  gap: 2px;
  font-size: $font-size-xs;
  color: $color-primary;
  text-decoration: none;

  &:hover {
    gap: 6px;
  }
}

/* 快捷操作 */
.section {
  margin: 0;
}

.section-title {
  font-size: $font-size-base;
  font-weight: $font-weight-medium;
  color: $color-text-secondary;
  margin-bottom: 12px;
}

.quick-actions {
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  gap: 12px;
}

.quick-action-btn {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  padding: 12px 16px;
  border: 1px solid $color-border;
  border-radius: $radius-base;
  color: $color-text-regular;
  font-size: $font-size-base;
  text-decoration: none;
  transition: all 0.15s;

  &:hover {
    background: #f9fafb;
    border-color: $color-primary;
    color: $color-primary;
  }
}

/* 待处理事项 */
.section-header-row {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: $font-size-base;
  font-weight: $font-weight-medium;
}

.text-warning { color: $color-warning; }
.text-danger { color: $color-danger; }
.text-success { color: $color-success; }

.pending-list,
.recent-list {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.pending-item {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 12px;
  border-radius: $radius-base;

  &.error {
    background: #fef2f2;
    border: 1px solid #fecaca;
  }

  &.warning {
    background: #fefce8;
    border: 1px solid #fef08a;
  }
}

.pending-item-left {
  display: flex;
  align-items: center;
  gap: 12px;
}

.pending-item-info,
.recent-item-info {
  display: flex;
  flex-direction: column;
  gap: 2px;
}

.pending-item-title,
.recent-item-title {
  font-size: $font-size-base;
  color: $color-text-primary;
  font-weight: $font-weight-medium;
}

.pending-item-desc,
.recent-item-time {
  font-size: $font-size-sm;
  color: $color-text-secondary;
}

/* 最近任务 */
.recent-item {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 12px;
  border: 1px solid $color-border;
  border-radius: $radius-base;
}

.recent-item-left {
  display: flex;
  align-items: center;
  gap: 12px;
}

/* 系统状态 */
.sys-status-card {
  margin-top: 24px;
}
</style>

