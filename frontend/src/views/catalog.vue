<template>
  <div class="catalog-page">
    <!-- 标签页 -->
    <div class="tab-bar">
      <button
        v-for="tab in tabs" :key="tab" class="tab-btn"
        :class="{ active: activeTab === tab }" @click="activeTab = tab"
      >{{ tab }}</button>
    </div>

    <!-- 筛选区 -->
    <div class="toolbar">
      <el-input
        v-model="searchTerm" placeholder="搜索数据集、字段、业务含义..."
        :prefix-icon="Search" class="search-input" clearable
      />
      <el-select v-model="qualityFilter" placeholder="质量状态" class="filter-select" clearable>
        <el-option label="全部状态" value="" />
        <el-option label="正常" value="success" />
        <el-option label="警告" value="warning" />
        <el-option label="异常" value="error" />
      </el-select>
    </div>

    <!-- 统计卡片 -->
    <el-row :gutter="16" class="stat-row">
      <el-col :span="6">
        <el-card shadow="never" class="info-card">
          <div class="info-card-header">
            <div class="info-card-icon bg-blue"><el-icon :size="16"><Coin /></el-icon></div>
            <span class="info-card-label">数据集总数</span>
            <span class="info-card-subtag">已接入</span>
          </div>
          <div class="info-card-value-row">
            <span class="info-card-value">{{ datasets.length }}</span>
            <span class="badge blue">+1 本周</span>
          </div>
          <div class="info-card-foot">全部数据集</div>
        </el-card>
      </el-col>
      <el-col :span="6">
        <el-card shadow="never" class="info-card">
          <div class="info-card-header">
            <div class="info-card-icon bg-green"><el-icon :size="16"><CircleCheckFilled /></el-icon></div>
            <span class="info-card-label">质量正常</span>
            <span class="info-card-subtag">数据健康</span>
          </div>
          <div class="info-card-value-row">
            <span class="info-card-value green">{{ normalCount }}</span>
            <span class="badge neutral">较昨日持平</span>
          </div>
          <div class="info-card-foot"><span>健康率</span><div class="health-bar"><div class="health-bar-fill" :style="{ width: healthRate + '%' }" /></div><span>{{ healthRate }}%</span></div>
        </el-card>
      </el-col>
      <el-col :span="6">
        <el-card shadow="never" class="info-card">
          <div class="info-card-header">
            <div class="info-card-icon bg-yellow"><el-icon :size="16"><WarningFilled /></el-icon></div>
            <span class="info-card-label">质量警告</span>
            <span class="info-card-subtag">需关注</span>
          </div>
          <div class="info-card-value-row">
            <span class="info-card-value yellow">{{ warningCount }}</span>
            <span class="badge neutral">较昨日持平</span>
          </div>
          <div class="info-card-foot">{{ warningCount > 0 ? '请及时处理' : '暂无告警' }}</div>
        </el-card>
      </el-col>
      <el-col :span="6">
        <el-card shadow="never" class="info-card">
          <div class="info-card-header">
            <div class="info-card-icon bg-purple"><el-icon :size="16"><Lock /></el-icon></div>
            <span class="info-card-label">未开放 Agent</span>
            <span class="info-card-subtag">权限管控</span>
          </div>
          <div class="info-card-value-row">
            <span class="info-card-value">{{ notAgentCount }}</span>
            <span class="badge neutral">较昨日持平</span>
          </div>
          <div class="info-card-foot">需申请权限访问</div>
        </el-card>
      </el-col>
    </el-row>

    <!-- 数据集卡片网格 -->
    <div v-if="filteredDatasets.length > 0" class="dataset-grid">
      <el-card
        v-for="ds in filteredDatasets" :key="ds.id"
        shadow="never"
        :class="['dataset-card', ds.quality === 'error' ? 'border-red' : ds.quality === 'warning' ? 'border-yellow' : '']"
      >
        <div class="ds-top">
          <div class="ds-name-row">
            <span :class="['ds-dot', ds.quality === 'error' ? 'red' : ds.quality === 'warning' ? 'yellow' : 'green']" />
            <span class="ds-name">{{ ds.displayName }}</span>
            <el-tag
              size="small" effect="plain"
              :type="ds.quality === 'error' ? 'danger' : ds.quality === 'warning' ? 'warning' : 'success'"
            >{{ ds.quality === 'error' ? '异常' : ds.quality === 'warning' ? '警告' : '正常' }}</el-tag>
          </div>
          <div class="ds-code-row">
            <span class="ds-code">{{ ds.name }}</span>
            <el-tag v-if="ds.layer === 'Serving'" size="small" effect="plain" class="layer-tag">语义: 订单</el-tag>
          </div>
        </div>

        <div class="ds-meta-grid">
          <div class="ds-meta-item">
            <el-icon :size="14" class="text-gray"><OfficeBuilding /></el-icon>
            <span>{{ ds.source }}</span>
          </div>
          <div class="ds-meta-item">
            <el-icon :size="14" class="text-gray"><Clock /></el-icon>
            <span>{{ ds.updatedAt.split(' ')[0] }}</span>
          </div>
          <div :class="['ds-meta-item', { 'text-danger': ds.records === 0 }]">
            <el-icon :size="14" :class="ds.records === 0 ? 'text-danger' : 'text-gray'"><Grid /></el-icon>
            <span>{{ ds.records === 0 ? '0 条 — 空表' : ds.records.toLocaleString() + ' 条' }}</span>
          </div>
          <div class="ds-meta-item">
            <el-icon :size="14" class="text-gray"><Collection /></el-icon>
            <span>{{ ds.fields }} 个字段</span>
          </div>
        </div>

        <div class="ds-actions">
          <el-button
            v-if="ds.agentEnabled && ds.records > 0"
            size="small" plain type="primary"
          >
            <el-icon :size="14"><Service /></el-icon>
            问问 Agent
          </el-button>
          <el-button v-else-if="ds.agentEnabled" size="small" plain disabled>
            <el-icon :size="14"><Service /></el-icon>
            暂无可查数据
          </el-button>
          <el-button v-else size="small" plain disabled>
            <el-icon :size="14"><Lock /></el-icon>
            申请权限
          </el-button>
          <router-link :to="/tables/">
            <el-button size="small" link type="primary">
              {{ ds.records === 0 ? '查看表结构' : '查看详情' }}
            </el-button>
          </router-link>
        </div>
      </el-card>
    </div>

    <el-empty v-else description="没有找到匹配的数据集" />
  </div>
</template>

<script setup lang="ts">
import { computed, ref } from 'vue'
import {
  Search, Coin, CircleCheckFilled, WarningFilled, Lock, Service,
  OfficeBuilding, Clock, Grid, Collection,
} from '@element-plus/icons-vue'

const activeTab = ref('全部数据集')
const searchTerm = ref('')
const qualityFilter = ref('')

const tabs = ['全部数据集', '财务数据', '销售数据', '生产数据', '人事数据']

interface Dataset {
  id: number
  name: string
  displayName: string
  source: string
  layer: string
  records: number
  fields: number
  quality: 'success' | 'warning' | 'error'
  agentEnabled: boolean
  updatedAt: string
}

const datasets: Dataset[] = [
  { id: 1, name: 'sap_sales_orders', displayName: '销售订单表', source: 'SAP ERP', layer: 'Raw', records: 1250, fields: 24, quality: 'success', agentEnabled: true, updatedAt: '2026-07-10 09:30' },
  { id: 2, name: 'mes_production_records', displayName: 'MES 生产记录', source: 'Plataine MES', layer: 'Serving', records: 856, fields: 18, quality: 'success', agentEnabled: true, updatedAt: '2026-07-10 09:00' },
  { id: 3, name: 'daily_attendance', displayName: '每日考勤表', source: 'Excel', layer: 'Raw', records: 320, fields: 12, quality: 'warning', agentEnabled: true, updatedAt: '2026-07-09 18:00' },
  { id: 4, name: 'supplier_master', displayName: '供应商主数据', source: 'ERP API', layer: 'Serving', records: 180, fields: 15, quality: 'success', agentEnabled: true, updatedAt: '2026-07-10 08:00' },
  { id: 5, name: 'finance_monthly_report', displayName: '财务月报表', source: 'Excel', layer: 'Raw', records: 0, fields: 32, quality: 'error', agentEnabled: true, updatedAt: '2026-07-01 12:00' },
  { id: 6, name: 'mes_oee_data', displayName: '设备 OEE 数据', source: 'MES MQTT', layer: 'Raw', records: 5200, fields: 10, quality: 'success', agentEnabled: false, updatedAt: '2026-07-10 10:15' },
]

const filteredDatasets = computed(() =>
  datasets.filter((ds) => {
    const matchSearch = ds.displayName.toLowerCase().includes(searchTerm.value.toLowerCase()) ||
      ds.name.toLowerCase().includes(searchTerm.value.toLowerCase())
    const matchQuality = !qualityFilter.value || ds.quality === qualityFilter.value
    return matchSearch && matchQuality
  })
)

const normalCount = computed(() => datasets.filter((d) => d.quality === 'success').length)
const warningCount = computed(() => datasets.filter((d) => d.quality === 'warning').length)
const notAgentCount = computed(() => datasets.filter((d) => !d.agentEnabled).length)
const healthRate = computed(() =>
  datasets.length > 0 ? Math.round((normalCount.value / datasets.length) * 100) : 0
)
</script>

<style lang="scss" scoped>
.catalog-page {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.tab-bar {
  display: flex;
  gap: 0;
  border-bottom: 1px solid $color-border;
  margin-bottom: 0;
}
.tab-btn {
  padding: 10px 16px;
  border: none;
  background: none;
  font-size: $font-size-base;
  color: $color-text-secondary;
  cursor: pointer;
  border-bottom: 2px solid transparent;
  &:hover { color: $color-text-primary; }
  &.active {
    color: $color-primary;
    border-bottom-color: $color-primary;
    font-weight: $font-weight-medium;
  }
}

.toolbar {
  display: flex;
  align-items: center;
  gap: 12px;
}
.search-input { width: 360px; }
.filter-select { width: 130px; }

.stat-row {
  margin: 0 !important;
  :deep(.el-col) { padding-left: 8px !important; padding-right: 8px !important; }
  :deep(.el-col:first-child) { padding-left: 0 !important; }
  :deep(.el-col:last-child) { padding-right: 0 !important; }
}

.info-card {
  :deep(.el-card__body) {
    padding: 20px;
    display: flex;
    flex-direction: column;
    gap: 8px;
  }
}
.info-card-header {
  display: flex;
  align-items: center;
  gap: 6px;
}
.info-card-icon {
  width: 32px; height: 32px;
  border-radius: 8px;
  display: flex; align-items: center; justify-content: center;
  &.bg-blue { background: #dbeafe; color: $color-primary; }
  &.bg-green { background: #dcfce7; color: $color-success; }
  &.bg-yellow { background: #fef3c7; color: $color-warning; }
  &.bg-purple { background: #ede9fe; color: #7c3aed; }
}
.info-card-label { font-size: $font-size-base; color: $color-text-secondary; }
.info-card-subtag {
  font-size: $font-size-xs; color: $color-text-placeholder;
  background: #f3f4f6; padding: 1px 6px;
  border-radius: 4px; margin-left: auto; white-space: nowrap;
}
.info-card-value-row {
  display: flex; align-items: baseline; gap: 8px;
}
.info-card-value {
  font-size: 28px; font-weight: $font-weight-bold; color: $color-text-primary;
  &.green { color: $color-success; }
  &.yellow { color: $color-warning; }
}
.badge {
  font-size: $font-size-xs; padding: 1px 6px; border-radius: 4px;
  &.blue { color: $color-primary; background: #eff6ff; }
  &.neutral { color: $color-text-placeholder; background: #f3f4f6; }
}
.info-card-foot {
  display: flex; align-items: center; gap: 6px;
  font-size: $font-size-xs; color: $color-text-placeholder;
}
.health-bar {
  flex: 1; height: 4px; background: #f3f4f6;
  border-radius: 2px; overflow: hidden;
}
.health-bar-fill {
  height: 100%; background: $color-success; border-radius: 2px;
  transition: width 0.3s;
}

.dataset-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 16px;
}
@media (max-width: 1200px) { .dataset-grid { grid-template-columns: repeat(2, 1fr); } }
@media (max-width: 750px) { .dataset-grid { grid-template-columns: 1fr; } }

.dataset-card {
  :deep(.el-card__body) {
    display: flex; flex-direction: column; gap: 12px; padding: 20px;
  }
  &.border-red { border: 1px solid #fecaca; }
  &.border-yellow { border: 1px solid #fef08a; }
}

.ds-top {
  display: flex; flex-direction: column; gap: 4px;
}
.ds-name-row {
  display: flex; align-items: center; gap: 8px;
}
.ds-dot {
  width: 8px; height: 8px; border-radius: 50%; flex-shrink: 0;
  &.green { background: $color-success; }
  &.yellow { background: $color-warning; }
  &.red { background: $color-danger; }
}
.ds-name {
  font-size: $font-size-base; font-weight: $font-weight-semibold; color: $color-text-primary;
  flex: 1; overflow: hidden; text-overflow: ellipsis; white-space: nowrap;
}
.ds-code-row {
  display: flex; align-items: center; gap: 8px; padding-left: 16px;
}
.ds-code { font-size: $font-size-xs; color: $color-text-placeholder; font-family: $font-family-mono; }

.ds-meta-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 8px 16px;
}
.ds-meta-item {
  display: flex; align-items: center; gap: 4px;
  font-size: $font-size-xs; color: $color-text-secondary;
}
.text-gray { color: $color-text-placeholder; }
.text-danger { color: $color-danger; }

.ds-actions {
  display: flex; align-items: center; justify-content: space-between;
  padding-top: 12px; border-top: 1px solid $color-border-light;
}
</style>
