<template>
  <div class="page-layout">
    <Index
      title="系统设置"
      :breadcrumb="[{ label: '首页', to: '/' }, { label: '系统设置' }]"
      description="管理系统基础字典和参数，包括数据源类型、接入方式、质量状态、敏感字段类型和平台参数。"
    />

    <TabNav v-model="activeTab" :tabs="tabs" />

    <Crud v-if="activeTab === '数据源类型'" :filter-items="searchFilterItems" v-model:filter-values="searchValues" :pagination="dsPagination">
      <template #filters-actions>
        <el-button type="primary" :icon="Plus">{{ actionLabel }}</el-button>
      </template>
      <template #table>
        <Table :columns="dsTypeColumns" :data="pagedDataSourceTypes">
          <template #col-code="{ row }"><span class="mono">{{ row.code }}</span></template>
        </Table>
      </template>
    </Crud>

    <Crud v-if="activeTab === '接入方式'" :filter-items="searchFilterItems" v-model:filter-values="searchValues" :pagination="imPagination">
      <template #filters-actions>
        <el-button type="primary" :icon="Plus">{{ actionLabel }}</el-button>
      </template>
      <template #table>
        <Table :columns="imColumns" :data="pagedIngestionMethods">
          <template #col-code="{ row }"><span class="mono">{{ row.code }}</span></template>
        </Table>
      </template>
    </Crud>

    <Crud v-if="activeTab === '质量状态'" :filter-items="searchFilterItems" v-model:filter-values="searchValues" :pagination="qsPagination">
      <template #filters-actions>
        <el-button type="primary" :icon="Plus">{{ actionLabel }}</el-button>
      </template>
      <template #table><Table :columns="qsColumns" :data="pagedQualityStatuses" /></template>
    </Crud>

    <Crud v-if="activeTab === '敏感字段类型'" :filter-items="searchFilterItems" v-model:filter-values="searchValues" :pagination="stPagination">
      <template #filters-actions>
        <el-button type="primary" :icon="Plus">{{ actionLabel }}</el-button>
      </template>
      <template #table>
        <Table :columns="stColumns" :data="pagedSensitiveTypes">
          <template #col-code="{ row }"><span class="mono">{{ row.code }}</span></template>
        </Table>
      </template>
    </Crud>

    <template v-if="activeTab === '业务标签'">
      <div class="tag-toolbar">
        <el-input v-model="searchTerm" placeholder="搜索..." :prefix-icon="Search" class="search-input" clearable />
        <div class="spacer" />
        <el-button type="primary" :icon="Plus">{{ actionLabel }}</el-button>
      </div>
      <div class="tag-grid">
        <el-card v-for="tag in businessTags" :key="tag.id" shadow="never" class="tag-card">
          <div class="tag-card-header">
            <el-tag effect="plain" :type="tag.color === 'blue' ? '' : tag.color === 'green' ? 'success' : tag.color === 'purple' ? '' : 'warning'" :class="'tag-' + tag.color">{{ tag.name }}</el-tag>
            <el-button link type="primary" :icon="Edit" />
          </div>
          <div class="tag-usage">使用次数: {{ tag.usageCount }}</div>
        </el-card>
      </div>
    </template>

    <Crud v-if="activeTab === '平台参数'" :filter-items="searchFilterItems" v-model:filter-values="searchValues" :pagination="ppPagination">
      <template #filters-actions>
        <el-button type="primary" :icon="Plus">{{ actionLabel }}</el-button>
      </template>
      <template #table>
        <Table :columns="ppColumns" :data="pagedPlatformParams">
          <template #col-key="{ row }"><span class="mono">{{ row.key }}</span></template>
        </Table>
      </template>
    </Crud>

    <el-card shadow="never" class="sys-info-card">
      <template #header>
        <div class="sys-header"><el-icon :size="16"><Setting /></el-icon><span>系统信息</span></div>
      </template>
      <el-row :gutter="16">
        <el-col :span="6"><div class="sys-info-item"><div class="sys-info-label">平台版本</div><div>v1.0.0 (草案)</div></div></el-col>
        <el-col :span="6"><div class="sys-info-item"><div class="sys-info-label">部署环境</div><el-tag type="warning" effect="plain">测试环境</el-tag></div></el-col>
        <el-col :span="6"><div class="sys-info-item"><div class="sys-info-label">最近更新</div><div>2026-06-13</div></div></el-col>
        <el-col :span="6"><div class="sys-info-item"><div class="sys-info-label">系统管理员</div><div>admin@company.com</div></div></el-col>
      </el-row>
    </el-card>
  </div>
</template>

<script setup lang="ts">
import { computed, reactive, ref, watch } from 'vue'
import { Search, Plus, Edit, Setting } from '@element-plus/icons-vue'
import TabNav from '@/components/tab-nav/index.vue'
import type { TabItem } from '@/components/tab-nav/types'
import Index from '@/components/page-header/index.vue'
import { Crud, Table } from '@/components/crud'
import type { ColumnSchema, FilterItem } from '@/components/crud'

const activeTab = ref('数据源类型')
const searchFilterItems: FilterItem[] = [{ key: 'keyword', placeholder: '搜索...', width: '260px' }]
const searchValues = ref<Record<string, any>>({})
const searchTerm = ref('')
const tabs: TabItem[] = [
  { key: '数据源类型', label: '数据源类型' },
  { key: '接入方式', label: '接入方式' },
  { key: '质量状态', label: '质量状态' },
  { key: '敏感字段类型', label: '敏感字段类型' },
  { key: '业务标签', label: '业务标签' },
  { key: '平台参数', label: '平台参数' },
]

const actionLabel = computed(() => {
  const map: Record<string, string> = { '数据源类型': '添加类型', '接入方式': '添加方式', '质量状态': '添加状态', '敏感字段类型': '添加类型', '业务标签': '添加标签', '平台参数': '添加参数' }
  return map[activeTab.value] ?? '添加'
})

interface SettingItem { id: string; code?: string; name: string; description: string; status?: string; color?: string; maskingRule?: string; key?: string; value?: string; usageCount?: number }

const dataSourceTypes: SettingItem[] = [
  { id: '1', code: 'ERP', name: 'ERP 系统', description: '企业资源计划系统', status: '启用' },
  { id: '2', code: 'MES', name: 'MES 系统', description: '制造执行系统', status: '启用' },
  { id: '3', code: 'EXCEL', name: 'Excel 文件', description: 'Excel 表格文件导入', status: '启用' },
]
const ingestionMethods: SettingItem[] = [
  { id: '1', code: 'DB_SYNC', name: '数据库同步', description: '通过数据库连接直接同步', status: '启用' },
  { id: '2', code: 'API', name: 'API 拉取', description: '通过 API 接口拉取数据', status: '启用' },
  { id: '3', code: 'FILE', name: '文件导入', description: '上传文件导入数据', status: '启用' },
]
const qualityStatuses: SettingItem[] = [
  { id: '1', code: 'PASS', name: '通过', color: 'green', description: '数据质量检查通过' },
  { id: '2', code: 'WARNING', name: '警告', color: 'yellow', description: '存在轻微质量问题' },
  { id: '3', code: 'ERROR', name: '异常', color: 'red', description: '存在严重质量问题' },
]
const sensitiveTypes: SettingItem[] = [
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
const platformParams: SettingItem[] = [
  { id: '1', key: 'max_query_rows', name: '最大查询行数', value: '10000', description: 'Agent 单次查询返回的最大行数' },
  { id: '2', key: 'sync_frequency', name: '默认同步频率', value: '每日', description: '接入任务的默认执行频率' },
  { id: '3', key: 'quality_check_enabled', name: '自动质量检查', value: '启用', description: '数据接入后自动执行质量检查' },
  { id: '4', key: 'audit_retention_days', name: '审计日志保留天数', value: '90', description: '审计日志的保留时长' },
]

function filterItems<T extends { name: string; description?: string }>(items: T[]): T[] {
  if (!searchValues.value.keyword || '') return items
  return items.filter(item => item.name.includes(searchValues.value.keyword || '') || (item.description ?? '').includes(searchValues.value.keyword || ''))
}

const filteredDataSourceTypes = computed(() => filterItems(dataSourceTypes))
const filteredIngestionMethods = computed(() => filterItems(ingestionMethods))
const filteredQualityStatuses = computed(() => filterItems(qualityStatuses))
const filteredSensitiveTypes = computed(() => filterItems(sensitiveTypes))
const filteredPlatformParams = computed(() => filterItems(platformParams))

function slicePage<T>(data: T[], page: number, size: number) { return data.slice((page - 1) * size, page * size) }
function usePagination() { return reactive({ page: 1, pageSize: 20, total: 0, onPageChange() {}, onSizeChange() {} }) }

const dsPagination = usePagination()
const pagedDataSourceTypes = computed(() => slicePage(filteredDataSourceTypes.value, dsPagination.page, dsPagination.pageSize))
watch([filteredDataSourceTypes, () => dsPagination.pageSize], () => { dsPagination.total = filteredDataSourceTypes.value.length; if (dsPagination.page > 1 && (dsPagination.page - 1) * dsPagination.pageSize >= dsPagination.total) dsPagination.page = 1 })

const imPagination = usePagination()
const pagedIngestionMethods = computed(() => slicePage(filteredIngestionMethods.value, imPagination.page, imPagination.pageSize))
watch([filteredIngestionMethods, () => imPagination.pageSize], () => { imPagination.total = filteredIngestionMethods.value.length; if (imPagination.page > 1 && (imPagination.page - 1) * imPagination.pageSize >= imPagination.total) imPagination.page = 1 })

const qsPagination = usePagination()
const pagedQualityStatuses = computed(() => slicePage(filteredQualityStatuses.value, qsPagination.page, qsPagination.pageSize))
watch([filteredQualityStatuses, () => qsPagination.pageSize], () => { qsPagination.total = filteredQualityStatuses.value.length; if (qsPagination.page > 1 && (qsPagination.page - 1) * qsPagination.pageSize >= qsPagination.total) qsPagination.page = 1 })

const stPagination = usePagination()
const pagedSensitiveTypes = computed(() => slicePage(filteredSensitiveTypes.value, stPagination.page, stPagination.pageSize))
watch([filteredSensitiveTypes, () => stPagination.pageSize], () => { stPagination.total = filteredSensitiveTypes.value.length; if (stPagination.page > 1 && (stPagination.page - 1) * stPagination.pageSize >= stPagination.total) stPagination.page = 1 })

const ppPagination = usePagination()
const pagedPlatformParams = computed(() => slicePage(filteredPlatformParams.value, ppPagination.page, ppPagination.pageSize))
watch([filteredPlatformParams, () => ppPagination.pageSize], () => { ppPagination.total = filteredPlatformParams.value.length; if (ppPagination.page > 1 && (ppPagination.page - 1) * ppPagination.pageSize >= ppPagination.total) ppPagination.page = 1 })

const dsTypeColumns: ColumnSchema[] = [
  { type: 'custom', prop: 'code', label: '类型编码', width: 120 },
  { type: 'text', prop: 'name', label: '类型名称', minWidth: 140 },
  { type: 'text', prop: 'description', label: '描述', minWidth: 200 },
  { type: 'tag', prop: 'status', label: '状态', width: 100, tagType: 'success' },
  { type: 'action', label: '操作', width: 80, buttons: [{ label: '编辑', icon: Edit, onClick: () => {} }] },
]

const imColumns: ColumnSchema[] = [
  { type: 'custom', prop: 'code', label: '方式编码', width: 140 },
  { type: 'text', prop: 'name', label: '方式名称', minWidth: 140 },
  { type: 'text', prop: 'description', label: '描述', minWidth: 200 },
  { type: 'tag', prop: 'status', label: '状态', width: 100, tagType: 'success' },
  { type: 'action', label: '操作', width: 80, buttons: [{ label: '编辑', icon: Edit, onClick: () => {} }] },
]

const qsColumns: ColumnSchema[] = [
  { type: 'text', prop: 'code', label: '状态编码', width: 120 },
  { type: 'text', prop: 'name', label: '状态名称', minWidth: 120 },
  { type: 'tag', prop: 'color', label: '颜色标识', width: 100, tagMap: { green: 'success', yellow: 'warning', red: 'danger' } },
  { type: 'text', prop: 'description', label: '描述', minWidth: 200 },
  { type: 'action', label: '操作', width: 80, buttons: [{ label: '编辑', icon: Edit, onClick: () => {} }] },
]

const stColumns: ColumnSchema[] = [
  { type: 'custom', prop: 'code', label: '类型编码', width: 130 },
  { type: 'text', prop: 'name', label: '类型名称', minWidth: 120 },
  { type: 'text', prop: 'description', label: '描述', minWidth: 220 },
  { type: 'tag', prop: 'maskingRule', label: '默认脱敏规则', width: 140, tagType: 'warning' },
  { type: 'action', label: '操作', width: 80, buttons: [{ label: '编辑', icon: Edit, onClick: () => {} }] },
]

const ppColumns: ColumnSchema[] = [
  { type: 'custom', prop: 'key', label: '参数键', width: 180 },
  { type: 'text', prop: 'name', label: '参数名称', minWidth: 140 },
  { type: 'tag', prop: 'value', label: '当前值', width: 120 },
  { type: 'text', prop: 'description', label: '描述', minWidth: 240 },
  { type: 'action', label: '操作', width: 80, buttons: [{ label: '编辑', icon: Edit, onClick: () => {} }] },
]
</script>

<style lang="scss" scoped>
.tab-bar-old-removed { display: none; border-bottom: 1px solid $color-border; }
.tab-btn { padding: 10px 16px; border: none; background: none; font-size: $font-size-base; color: $color-text-secondary; cursor: pointer; border-bottom: 2px solid transparent; &:hover { color: $color-text-primary; } &.active { color: $color-primary; border-bottom-color: $color-primary; font-weight: $font-weight-medium; } }
.search-input { width: 280px; }
.spacer { flex: 1; }
.tag-toolbar { display: flex; align-items: center; gap: 12px; }
.mono { font-family: $font-family-mono; font-size: $font-size-sm; }
.tag-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 16px; }
.tag-card { :deep(.el-card__body) { display: flex; flex-direction: column; gap: 8px; padding: 16px; } }
.tag-card-header { display: flex; align-items: center; justify-content: space-between; }
.tag-blue { background: #eff6ff; color: $color-primary; border-color: #bfdbfe; }
.tag-green { background: #f0fdf4; color: $color-success; border-color: #bbf7d0; }
.tag-purple { background: #f5f3ff; color: #7c3aed; border-color: #ddd6fe; }
.tag-orange { background: #fff7ed; color: #ea580c; border-color: #fed7aa; }
.tag-usage { font-size: $font-size-sm; color: $color-text-secondary; }
.sys-info-card { .sys-header { display: flex; align-items: center; gap: 8px; font-size: $font-size-base; font-weight: $font-weight-medium; } }
.sys-info-item { display: flex; flex-direction: column; gap: 4px; font-size: $font-size-base; }
.sys-info-label { font-size: $font-size-xs; color: $color-text-placeholder; }
</style>
