<template>
  <div class="settings-page">
    <!-- 标签页 -->
    <div class="tab-bar">
      <button
        v-for="tab in tabs" :key="tab" class="tab-btn"
        :class="{ active: activeTab === tab }" @click="activeTab = tab"
      >{{ tab }}</button>
    </div>

    <!-- 筛选区 + 操作 -->
    <div class="toolbar">
      <el-input
        v-model="searchTerm" placeholder="搜索..." :prefix-icon="Search"
        class="search-input" clearable
      />
      <div class="spacer" />
      <el-button type="primary" :icon="Plus">{{ actionLabel }}</el-button>
    </div>

    <!-- 数据源类型 -->
    <el-card v-if="activeTab === '数据源类型'" shadow="never">
      <el-table :data="filteredDataSourceTypes" stripe>
        <el-table-column label="类型编码" width="120">
          <template #default="{ row }"><span class="mono">{{ row.code }}</span></template>
        </el-table-column>
        <el-table-column label="类型名称" min-width="140" prop="name" />
        <el-table-column label="描述" min-width="200" prop="description" />
        <el-table-column label="状态" width="100">
          <template #default="{ row }">
            <el-tag type="success" size="small" effect="plain">{{ row.status }}</el-tag>
          </template>
        </el-table-column>
        <el-table-column label="操作" width="80" fixed="right">
          <template #default><el-button link type="primary" :icon="Edit" /></template>
        </el-table-column>
      </el-table>
    </el-card>

    <!-- 接入方式 -->
    <el-card v-if="activeTab === '接入方式'" shadow="never">
      <el-table :data="filteredIngestionMethods" stripe>
        <el-table-column label="方式编码" width="140">
          <template #default="{ row }"><span class="mono">{{ row.code }}</span></template>
        </el-table-column>
        <el-table-column label="方式名称" min-width="140" prop="name" />
        <el-table-column label="描述" min-width="200" prop="description" />
        <el-table-column label="状态" width="100">
          <template #default="{ row }">
            <el-tag type="success" size="small" effect="plain">{{ row.status }}</el-tag>
          </template>
        </el-table-column>
        <el-table-column label="操作" width="80" fixed="right">
          <template #default><el-button link type="primary" :icon="Edit" /></template>
        </el-table-column>
      </el-table>
    </el-card>

    <!-- 质量状态 -->
    <el-card v-if="activeTab === '质量状态'" shadow="never">
      <el-table :data="filteredQualityStatuses" stripe>
        <el-table-column label="状态编码" width="120">
          <template #default="{ row }"><span class="mono">{{ row.code }}</span></template>
        </el-table-column>
        <el-table-column label="状态名称" min-width="120" prop="name" />
        <el-table-column label="颜色标识" width="100">
          <template #default="{ row }">
            <el-tag
              :type="row.color === 'green' ? 'success' : row.color === 'yellow' ? 'warning' : 'danger'"
              size="small" effect="plain"
            >{{ row.color }}</el-tag>
          </template>
        </el-table-column>
        <el-table-column label="描述" min-width="200" prop="description" />
        <el-table-column label="操作" width="80" fixed="right">
          <template #default><el-button link type="primary" :icon="Edit" /></template>
        </el-table-column>
      </el-table>
    </el-card>

    <!-- 敏感字段类型 -->
    <el-card v-if="activeTab === '敏感字段类型'" shadow="never">
      <el-table :data="filteredSensitiveTypes" stripe>
        <el-table-column label="类型编码" width="130">
          <template #default="{ row }"><span class="mono">{{ row.code }}</span></template>
        </el-table-column>
        <el-table-column label="类型名称" min-width="120" prop="name" />
        <el-table-column label="描述" min-width="220" prop="description" />
        <el-table-column label="默认脱敏规则" width="140">
          <template #default="{ row }">
            <el-tag type="warning" size="small" effect="plain">{{ row.maskingRule }}</el-tag>
          </template>
        </el-table-column>
        <el-table-column label="操作" width="80" fixed="right">
          <template #default><el-button link type="primary" :icon="Edit" /></template>
        </el-table-column>
      </el-table>
    </el-card>

    <!-- 业务标签 -->
    <div v-if="activeTab === '业务标签'" class="tag-grid">
      <el-card v-for="tag in businessTags" :key="tag.id" shadow="never" class="tag-card">
        <div class="tag-card-header">
          <el-tag
            :type="tag.color === 'blue' ? '' : tag.color === 'green' ? 'success' : tag.color === 'purple' ? '' : 'warning'"
            size="small" effect="plain"
            :class="'tag-' + tag.color"
          >{{ tag.name }}</el-tag>
          <el-button link type="primary" :icon="Edit" />
        </div>
        <div class="tag-usage">使用次数: {{ tag.usageCount }}</div>
      </el-card>
    </div>

    <!-- 平台参数 -->
    <el-card v-if="activeTab === '平台参数'" shadow="never">
      <el-table :data="filteredPlatformParams" stripe>
        <el-table-column label="参数键" width="180">
          <template #default="{ row }"><span class="mono">{{ row.key }}</span></template>
        </el-table-column>
        <el-table-column label="参数名称" min-width="140" prop="name" />
        <el-table-column label="当前值" width="120">
          <template #default="{ row }">
            <el-tag size="small" effect="plain">{{ row.value }}</el-tag>
          </template>
        </el-table-column>
        <el-table-column label="描述" min-width="240" prop="description" />
        <el-table-column label="操作" width="80" fixed="right">
          <template #default><el-button link type="primary" :icon="Edit" /></template>
        </el-table-column>
      </el-table>
    </el-card>

    <!-- 系统信息 -->
    <el-card shadow="never" class="sys-info-card">
      <template #header>
        <div class="sys-header">
          <el-icon :size="16"><Setting /></el-icon>
          <span>系统信息</span>
        </div>
      </template>
      <el-row :gutter="16">
        <el-col :span="6">
          <div class="sys-info-item">
            <div class="sys-info-label">平台版本</div>
            <div>v1.0.0 (草案)</div>
          </div>
        </el-col>
        <el-col :span="6">
          <div class="sys-info-item">
            <div class="sys-info-label">部署环境</div>
            <el-tag type="warning" size="small" effect="plain">测试环境</el-tag>
          </div>
        </el-col>
        <el-col :span="6">
          <div class="sys-info-item">
            <div class="sys-info-label">最近更新</div>
            <div>2026-06-13</div>
          </div>
        </el-col>
        <el-col :span="6">
          <div class="sys-info-item">
            <div class="sys-info-label">系统管理员</div>
            <div>admin@company.com</div>
          </div>
        </el-col>
      </el-row>
    </el-card>
  </div>
</template>

<script setup lang="ts">
import { computed, ref } from 'vue'
import { Search, Plus, Edit, Setting } from '@element-plus/icons-vue'

const activeTab = ref('数据源类型')
const searchTerm = ref('')

const tabs = ['数据源类型', '接入方式', '质量状态', '敏感字段类型', '业务标签', '平台参数']

const actionLabel = computed(() => {
  const map: Record<string, string> = {
    '数据源类型': '添加类型', '接入方式': '添加方式', '质量状态': '添加状态',
    '敏感字段类型': '添加类型', '业务标签': '添加标签', '平台参数': '添加参数',
  }
  return map[activeTab.value] ?? '添加'
})

interface SettingItem {
  id: string; code?: string; name: string; description: string; status?: string;
  color?: string; maskingRule?: string; key?: string; value?: string;
  usageCount?: number;
}

const dataSourceTypes = [
  { id: '1', code: 'ERP', name: 'ERP 系统', description: '企业资源计划系统', status: '启用' },
  { id: '2', code: 'MES', name: 'MES 系统', description: '制造执行系统', status: '启用' },
  { id: '3', code: 'EXCEL', name: 'Excel 文件', description: 'Excel 表格文件导入', status: '启用' },
]

const ingestionMethods = [
  { id: '1', code: 'DB_SYNC', name: '数据库同步', description: '通过数据库连接直接同步', status: '启用' },
  { id: '2', code: 'API', name: 'API 拉取', description: '通过 API 接口拉取数据', status: '启用' },
  { id: '3', code: 'FILE', name: '文件导入', description: '上传文件导入数据', status: '启用' },
]

const qualityStatuses = [
  { id: '1', code: 'PASS', name: '通过', color: 'green', description: '数据质量检查通过' },
  { id: '2', code: 'WARNING', name: '警告', color: 'yellow', description: '存在轻微质量问题' },
  { id: '3', code: 'ERROR', name: '异常', color: 'red', description: '存在严重质量问题' },
]

const sensitiveTypes = [
  { id: '1', code: 'PII', name: '个人信息', description: '姓名、身份证号、电话等', maskingRule: '部分隐藏' },
  { id: '2', code: 'FINANCIAL', name: '金融信息', description: '银行账号、薪资等', maskingRule: '完全隐藏' },
  { id: '3', code: 'BUSINESS', name: '商业机密', description: '合同金额、客户信息等', maskingRule: '脱敏显示' },
]

const businessTags = [
  { id: '1', name: '财务', color: 'blue', usageCount: 12 },
  { id: '2', name: '销售', color: 'green', usageCount: 18 },
  { id: '3', name: '生产', color: 'purple', usageCount: 8 },
  { id: '4', name: '人事', color: 'orange', usageCount: 6 },
]

const platformParams = [
  { id: '1', key: 'max_query_rows', name: '最大查询行数', value: '10000', description: 'Agent 单次查询返回的最大行数' },
  { id: '2', key: 'sync_frequency', name: '默认同步频率', value: '每日', description: '接入任务的默认执行频率' },
  { id: '3', key: 'quality_check_enabled', name: '自动质量检查', value: '启用', description: '数据接入后自动执行质量检查' },
  { id: '4', key: 'audit_retention_days', name: '审计日志保留天数', value: '90', description: '审计日志的保留时长' },
]

function filterItems<T extends { name: string; description?: string }>(items: T[]): T[] {
  return items.filter((item) =>
    item.name.includes(searchTerm.value) || (item.description ?? '').includes(searchTerm.value)
  )
}

const filteredDataSourceTypes = computed(() => filterItems(dataSourceTypes))
const filteredIngestionMethods = computed(() => filterItems(ingestionMethods))
const filteredQualityStatuses = computed(() => filterItems(qualityStatuses))
const filteredSensitiveTypes = computed(() => filterItems(sensitiveTypes))
const filteredPlatformParams = computed(() => filterItems(platformParams))
</script>

<style lang="scss" scoped>
.settings-page {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.tab-bar { display: flex; gap: 0; border-bottom: 1px solid $color-border; }
.tab-btn {
  padding: 10px 16px; border: none; background: none;
  font-size: $font-size-base; color: $color-text-secondary; cursor: pointer;
  border-bottom: 2px solid transparent;
  &:hover { color: $color-text-primary; }
  &.active { color: $color-primary; border-bottom-color: $color-primary; font-weight: $font-weight-medium; }
}

.toolbar { display: flex; align-items: center; gap: 12px; }
.search-input { width: 280px; }
.spacer { flex: 1; }

.mono { font-family: $font-family-mono; font-size: $font-size-sm; }

.tag-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 16px;
}
.tag-card {
  :deep(.el-card__body) {
    padding: 16px;
    display: flex;
    flex-direction: column;
    gap: 8px;
  }
}
.tag-card-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
}
.tag-blue { background: #eff6ff; color: $color-primary; border-color: #bfdbfe; }
.tag-green { background: #f0fdf4; color: $color-success; border-color: #bbf7d0; }
.tag-purple { background: #f5f3ff; color: #7c3aed; border-color: #ddd6fe; }
.tag-orange { background: #fff7ed; color: #ea580c; border-color: #fed7aa; }
.tag-usage { font-size: $font-size-sm; color: $color-text-secondary; }

.sys-info-card {
  .sys-header { display: flex; align-items: center; gap: 8px; font-size: $font-size-base; font-weight: $font-weight-medium; }
}
.sys-info-item { display: flex; flex-direction: column; gap: 4px; font-size: $font-size-base; }
.sys-info-label { font-size: $font-size-xs; color: $color-text-placeholder; }
</style>
