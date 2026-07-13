<template>
  <div class="ds-page">
    <!-- 筛选栏 + 操作 -->
    <div class="toolbar">
      <el-input
        v-model="searchTerm"
        placeholder="搜索数据源名称或描述..."
        :prefix-icon="Search"
        class="search-input"
        clearable
      />
      <el-select
        v-model="typeFilter"
        placeholder="数据源类型"
        class="filter-select-type"
        clearable
      >
        <el-option label="全部类型" value="" />
        <el-option
          v-for="t in dataSourceTypes"
          :key="t"
          :label="t"
          :value="t"
        />
      </el-select>
      <el-select
        v-model="statusFilter"
        placeholder="状态"
        class="filter-select-status"
        clearable
      >
        <el-option label="全部状态" value="" />
        <el-option label="正常" value="success" />
        <el-option label="警告" value="warning" />
        <el-option label="异常" value="error" />
        <el-option label="停用" value="inactive" />
      </el-select>
      <div class="spacer" />
      <el-button type="primary" :icon="Plus">新增数据源</el-button>
    </div>

    <!-- 统计卡片 4列 -->
    <el-row :gutter="16" class="stat-row">
      <el-col :span="6">
        <el-card shadow="never" class="info-card">
          <div class="info-card-header">
            <div class="info-card-icon bg-blue">
              <el-icon :size="16"><Coin /></el-icon>
            </div>
            <span class="info-card-label">数据源总数</span>
            <span class="info-card-subtag">已配置</span>
          </div>
          <div class="info-card-value-row">
            <span class="info-card-value">{{ counts.total }}</span>
            <span class="info-card-badge blue">+1 本月</span>
          </div>
          <div class="info-card-footer">ERP · MES · Excel</div>
        </el-card>
      </el-col>
      <el-col :span="6">
        <el-card shadow="never" class="info-card">
          <div class="info-card-header">
            <div class="info-card-icon bg-green">
              <el-icon :size="16"><CircleCheckFilled /></el-icon>
            </div>
            <span class="info-card-label">正常</span>
            <span class="info-card-subtag">状态良好</span>
          </div>
          <div class="info-card-value-row">
            <span class="info-card-value green">{{ counts.normal }}</span>
            <span class="info-card-badge green">↑ 较昨日</span>
          </div>
          <div class="info-card-footer">
            <span>健康率</span>
            <div class="health-bar">
              <div
                class="health-bar-fill"
                :style="{ width: healthRate + '%' }"
              />
            </div>
            <span>{{ healthRate }}%</span>
          </div>
        </el-card>
      </el-col>
      <el-col :span="6">
        <el-card shadow="never" class="info-card">
          <div class="info-card-header">
            <div class="info-card-icon bg-yellow">
              <el-icon :size="16"><WarningFilled /></el-icon>
            </div>
            <span class="info-card-label">警告</span>
            <span class="info-card-subtag">需关注</span>
          </div>
          <div class="info-card-value-row">
            <span class="info-card-value yellow">{{ counts.warning }}</span>
            <span class="info-card-badge neutral">较昨日持平</span>
          </div>
          <div class="info-card-footer">上次告警: 2h 前</div>
        </el-card>
      </el-col>
      <el-col :span="6">
        <el-card shadow="never" class="info-card">
          <div class="info-card-header">
            <div class="info-card-icon bg-red">
              <el-icon :size="16"><CircleCloseFilled /></el-icon>
            </div>
            <span class="info-card-label">异常</span>
            <span class="info-card-subtag danger-tag">{{ counts.error > 0 ? '⚠ 需处理' : '正常' }}</span>
          </div>
          <div class="info-card-value-row">
            <span class="info-card-value red">{{ counts.error }}</span>
            <span class="info-card-badge neutral">较昨日持平</span>
          </div>
          <div class="info-card-footer">{{ counts.error > 0 ? '请立即排查' : '暂无异常' }}</div>
        </el-card>
      </el-col>
    </el-row>

    <!-- 表格 -->
    <el-card shadow="never">
      <el-table
        :data="filteredSources"
        stripe
        style="width: 100%"
        empty-text="没有找到匹配的数据源"
      >
        <el-table-column label="数据源名称" min-width="200">
          <template #default="{ row }">
            <router-link
              :to="/data-sources/"
              class="ds-name-link"
            >
              <div>{{ row.name }}</div>
              <div class="ds-desc">{{ row.description }}</div>
            </router-link>
          </template>
        </el-table-column>
        <el-table-column label="类型" width="100">
          <template #default="{ row }">
            <el-tag size="small" effect="plain">{{ row.type }}</el-tag>
          </template>
        </el-table-column>
        <el-table-column prop="method" label="接入方式" width="110" />
        <el-table-column label="状态" width="90">
          <template #default="{ row }">
            <el-tag
              :type="statusTagType(row.status)"
              size="small"
              effect="plain"
            >
              {{ statusLabel(row.status) }}
            </el-tag>
          </template>
        </el-table-column>
        <el-table-column prop="businessOwner" label="业务负责人" width="110" />
        <el-table-column prop="techOwner" label="技术负责人" width="110" />
        <el-table-column prop="lastSync" label="最近接入" width="160" />
        <el-table-column prop="taskCount" label="关联任务" width="90" align="center" />
        <el-table-column label="操作" width="140" fixed="right">
          <template #default="{ row }">
            <div class="action-btns">
              <router-link :to="/data-sources/">
                <el-button link type="primary" :icon="View" />
              </router-link>
              <el-button link type="primary" :icon="Edit" />
              <el-button link type="primary" :icon="VideoPlay" />
            </div>
          </template>
        </el-table-column>
      </el-table>
    </el-card>
  </div>
</template>

<script setup lang="ts">
import { computed, ref } from 'vue'
import {
  Search, Plus, Coin, CircleCheckFilled, WarningFilled, CircleCloseFilled,
  View, Edit, VideoPlay,
} from '@element-plus/icons-vue'

const searchTerm = ref('')
const typeFilter = ref('')
const statusFilter = ref('')

const dataSourceTypes = ['ERP', 'MES', 'Excel', 'API', 'CSV']

interface DataSource {
  id: number
  name: string
  description: string
  type: string
  method: string
  status: 'success' | 'warning' | 'error' | 'inactive'
  businessOwner: string
  techOwner: string
  lastSync: string
  taskCount: number
}

const mockData: DataSource[] = [
  {
    id: 1, name: 'SAP ERP 生产系统', description: '西门子 MES 核心数据库',
    type: 'ERP', method: 'JDBC 直连', status: 'success',
    businessOwner: '刘伟', techOwner: '赵一',
    lastSync: '2026-07-10 10:00', taskCount: 4,
  },
  {
    id: 2, name: 'MES 生产制造执行', description: 'Plataine MES 系统数据',
    type: 'MES', method: 'API 拉取', status: 'warning',
    businessOwner: '张涛', techOwner: '王芳',
    lastSync: '2026-07-10 09:30', taskCount: 2,
  },
  {
    id: 3, name: 'Excel 考勤数据', description: '人力资源部员工考勤表',
    type: 'Excel', method: '文件上传', status: 'error',
    businessOwner: '李敏', techOwner: '陈亮',
    lastSync: '2026-07-09 18:00', taskCount: 1,
  },
  {
    id: 4, name: '供应商主数据', description: 'ERP 供应商档案接口',
    type: 'API', method: 'REST API', status: 'success',
    businessOwner: '周磊', techOwner: '杨帆',
    lastSync: '2026-07-10 08:00', taskCount: 3,
  },
  {
    id: 5, name: '财务月报', description: 'CFO 月度财务汇总报表',
    type: 'Excel', method: '文件上传', status: 'inactive',
    businessOwner: '吴婷', techOwner: '马超',
    lastSync: '2026-07-01 12:00', taskCount: 0,
  },
  {
    id: 6, name: 'MES 设备 OEE 数据', description: '设备综合效率实时数据',
    type: 'MES', method: 'MQTT 订阅', status: 'success',
    businessOwner: '张涛', techOwner: '王芳',
    lastSync: '2026-07-10 10:15', taskCount: 2,
  },
]

const filteredSources = computed(() =>
  mockData.filter((s) => {
    const matchSearch =
      s.name.toLowerCase().includes(searchTerm.value.toLowerCase()) ||
      s.description.toLowerCase().includes(searchTerm.value.toLowerCase())
    const matchType = !typeFilter.value || s.type === typeFilter.value
    const matchStatus = !statusFilter.value || s.status === statusFilter.value
    return matchSearch && matchType && matchStatus
  })
)

const counts = computed(() => ({
  total: mockData.length,
  normal: mockData.filter((s) => s.status === 'success').length,
  warning: mockData.filter((s) => s.status === 'warning').length,
  error: mockData.filter((s) => s.status === 'error').length,
}))

const healthRate = computed(() =>
  counts.value.total > 0
    ? Math.round((counts.value.normal / counts.value.total) * 100)
    : 0
)

function statusTagType(status: string) {
  const map: Record<string, 'success' | 'warning' | 'danger' | 'info'> = {
    success: 'success',
    warning: 'warning',
    error: 'danger',
    inactive: 'info',
  }
  return map[status] ?? 'info'
}

function statusLabel(status: string) {
  const map: Record<string, string> = {
    success: '正常',
    warning: '警告',
    error: '异常',
    inactive: '停用',
  }
  return map[status] ?? status
}
</script>

<style lang="scss" scoped>
.ds-page {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

/* 筛选栏 */
.toolbar {
  display: flex;
  align-items: center;
  gap: 12px;
}

.search-input {
  width: 320px;
}

.filter-select-type {
  width: 140px;
}

.filter-select-status {
  width: 120px;
}

.spacer {
  flex: 1;
}

/* 统计卡片 */
.stat-row {
  margin: 0 !important;

  :deep(.el-col) {
    padding-left: 8px !important;
    padding-right: 8px !important;
  }

  :deep(.el-col:first-child) {
    padding-left: 0 !important;
  }

  :deep(.el-col:last-child) {
    padding-right: 0 !important;
  }
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
  width: 32px;
  height: 32px;
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;

  &.bg-blue { background: #dbeafe; color: $color-primary; }
  &.bg-green { background: #dcfce7; color: $color-success; }
  &.bg-yellow { background: #fef3c7; color: $color-warning; }
  &.bg-red { background: #fee2e2; color: $color-danger; }
}

.info-card-label {
  font-size: $font-size-base;
  color: $color-text-secondary;
}

.info-card-subtag {
  font-size: $font-size-xs;
  color: $color-text-placeholder;
  background: #f3f4f6;
  padding: 1px 6px;
  border-radius: 4px;
  margin-left: auto;
  white-space: nowrap;
}

.danger-tag {
  color: $color-danger;
  background: #fee2e2;
  border: 1px solid #fecaca;
}

.info-card-value-row {
  display: flex;
  align-items: baseline;
  gap: 8px;
}

.info-card-value {
  font-size: 28px;
  font-weight: $font-weight-bold;
  color: $color-text-primary;

  &.green { color: $color-success; }
  &.yellow { color: $color-warning; }
  &.red { color: $color-danger; }
}

.info-card-badge {
  font-size: $font-size-xs;
  padding: 1px 6px;
  border-radius: 4px;

  &.blue { color: $color-primary; background: #eff6ff; }
  &.green { color: $color-success; background: #f0fdf4; }
  &.neutral { color: $color-text-placeholder; background: #f3f4f6; }
}

.info-card-footer {
  display: flex;
  align-items: center;
  gap: 6px;
  font-size: $font-size-xs;
  color: $color-text-placeholder;
}

.health-bar {
  flex: 1;
  height: 4px;
  background: #f3f4f6;
  border-radius: 2px;
  overflow: hidden;
}

.health-bar-fill {
  height: 100%;
  background: $color-success;
  border-radius: 2px;
  transition: width 0.3s;
}

/* 表格 */
.ds-name-link {
  text-decoration: none;
  color: inherit;

  &:hover {
    color: $color-primary;
  }
}

.ds-desc {
  font-size: $font-size-xs;
  color: $color-text-placeholder;
  margin-top: 2px;
}

.action-btns {
  display: flex;
  gap: 0;
}
</style>
