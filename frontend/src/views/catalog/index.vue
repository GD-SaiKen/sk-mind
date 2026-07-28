<template>
  <div class="page-layout">
    <Index
      title="数据目录"
      :breadcrumb="[{ label: '首页', to: '/' }, { label: '数据目录' }]"
      description="以业务视角浏览平台中的数据集和字段，了解数据来源、质量状态和可用性。"
    />

    <TabNav v-model="activeTab" :tabs="tabs" />

    <div class="toolbar">
      <el-input v-model="searchTerm" placeholder="搜索数据集、字段、业务含义..." :prefix-icon="Search" class="search-input" clearable @change="onSearch" />
      <el-select v-model="qualityFilter" placeholder="质量状态" class="filter-select" clearable @change="onSearch">
        <el-option label="全部状态" value="" />
        <el-option label="正常" value="ok" />
        <el-option label="警告" value="warning" />
        <el-option label="异常" value="error" />
      </el-select>
      <el-input v-model="sourceFilter" placeholder="来源系统" class="filter-input" clearable @change="onSearch" />
      <el-input v-model="domainFilter" placeholder="业务域" class="filter-input" clearable @change="onSearch" />
      <el-select v-model="agentFilter" placeholder="Agent 可用" class="filter-select" clearable @change="onSearch">
        <el-option label="全部" value="" />
        <el-option label="已开放" :value="true" />
        <el-option label="未开放" :value="false" />
      </el-select>
    </div>

    <el-row :gutter="16" class="stat-row">
      <el-col :span="6">
        <el-card shadow="never" class="info-card">
          <div class="info-card-header">
            <div class="info-card-icon bg-blue"><el-icon :size="16"><Coin /></el-icon></div>
            <span class="info-card-label">数据集总数</span>
          </div>
          <div class="info-card-value-row">
            <span class="info-card-value">{{ stats.total }}</span>
          </div>
        </el-card>
      </el-col>
      <el-col :span="6">
        <el-card shadow="never" class="info-card">
          <div class="info-card-header">
            <div class="info-card-icon bg-green"><el-icon :size="16"><CircleCheckFilled /></el-icon></div>
            <span class="info-card-label">质量正常</span>
          </div>
          <div class="info-card-value-row">
            <span class="info-card-value green">{{ stats.qualityOk }}</span>
          </div>
        </el-card>
      </el-col>
      <el-col :span="6">
        <el-card shadow="never" class="info-card">
          <div class="info-card-header">
            <div class="info-card-icon bg-yellow"><el-icon :size="16"><WarningFilled /></el-icon></div>
            <span class="info-card-label">质量警告</span>
          </div>
          <div class="info-card-value-row">
            <span class="info-card-value yellow">{{ stats.qualityWarning }}</span>
          </div>
        </el-card>
      </el-col>
      <el-col :span="6">
        <el-card shadow="never" class="info-card">
          <div class="info-card-header">
            <div class="info-card-icon bg-purple"><el-icon :size="16"><Service /></el-icon></div>
            <span class="info-card-label">Agent 可用</span>
          </div>
          <div class="info-card-value-row">
            <span class="info-card-value">{{ stats.agentAccessible }}</span>
          </div>
        </el-card>
      </el-col>
    </el-row>

    <!-- 数据集列表 -->
    <div v-if="activeTab !== '字段目录'" class="dataset-grid" v-loading="loading">
      <el-card v-for="ds in datasets" :key="ds.id" shadow="never" :class="['dataset-card', ds.qualityStatus === 'error' ? 'border-red' : ds.qualityStatus === 'warning' ? 'border-yellow' : '']">
        <div class="ds-top">
          <div class="ds-name-row">
            <span :class="['ds-dot', ds.qualityStatus === 'error' ? 'red' : ds.qualityStatus === 'warning' ? 'yellow' : 'green']" />
            <span class="ds-name">{{ ds.name }}</span>
            <el-tag effect="plain" :type="ds.qualityStatus === 'error' ? 'danger' : ds.qualityStatus === 'warning' ? 'warning' : 'success'">
              {{ qualityLabel(ds.qualityStatus) }}
            </el-tag>
          </div>
          <div class="ds-code-row">
            <span class="ds-code">{{ ds.code }}</span>
            <el-tag v-if="ds.businessDomain" effect="plain" size="small">{{ ds.businessDomain }}</el-tag>
          </div>
        </div>
        <div class="ds-meta-grid">
          <div class="ds-meta-item"><el-icon :size="14" class="text-gray"><OfficeBuilding /></el-icon><span>{{ ds.sourceName || '-' }}</span></div>
          <div class="ds-meta-item"><el-icon :size="14" class="text-gray"><Clock /></el-icon><span>{{ formatDate(ds.updatedAt) }}</span></div>
          <div class="ds-meta-item">
            <el-icon :size="14" class="text-gray"><Grid /></el-icon>
            <span>{{ ds.recordCount?.toLocaleString() || '0' }} 条</span>
          </div>
          <div class="ds-meta-item"><el-icon :size="14" class="text-gray"><Collection /></el-icon><span>{{ ds.fieldCount || 0 }} 个字段</span></div>
        </div>
        <div class="ds-actions">
          <el-tag v-if="ds.isAgentAccessible" type="success" effect="plain" size="small">Agent 可用</el-tag>
          <el-tag v-else type="info" effect="plain" size="small">未开放</el-tag>
          <router-link :to="'/catalog/' + ds.id"><el-button link type="primary">查看详情</el-button></router-link>
        </div>
      </el-card>
      <el-empty v-if="!loading && datasets.length === 0" description="没有找到匹配的数据集" />
    </div>

    <!-- 字段目录 -->
    <div v-if="activeTab === '字段目录'" v-loading="fieldLoading">
      <div class="toolbar" style="margin-bottom: 12px">
        <el-input v-model="fieldSearch" placeholder="搜索字段名..." :prefix-icon="Search" class="search-input" clearable @change="loadFields" />
      </div>
      <el-table :data="fieldItems" stripe v-if="fieldItems.length > 0">
        <el-table-column prop="fieldName" label="字段名" width="160" />
        <el-table-column prop="fieldAlias" label="显示名" width="130">
          <template #default="{ row }">{{ row.fieldAlias || '—' }}</template>
        </el-table-column>
        <el-table-column prop="datasetName" label="所属数据集" width="200" />
        <el-table-column prop="description" label="字段含义" min-width="160">
          <template #default="{ row }">{{ row.description || '—' }}</template>
        </el-table-column>
        <el-table-column prop="dataType" label="类型" width="100" />
        <el-table-column label="主键" width="70" align="center">
          <template #default="{ row }">
            <el-tag v-if="row.isPrimaryKey" type="warning" effect="plain" size="small">PK</el-tag>
            <span v-else>—</span>
          </template>
        </el-table-column>
        <el-table-column label="敏感" width="80" align="center">
          <template #default="{ row }">
            <el-tag v-if="row.isSensitive" type="danger" effect="plain" size="small">{{ row.sensitivityLevel }}</el-tag>
            <span v-else>—</span>
          </template>
        </el-table-column>
        <el-table-column label="空值率" width="90" align="center">
          <template #default="{ row }">
            <span :style="{ color: row.nullRate != null && row.nullRate > 0.1 ? '#dc2626' : row.nullRate != null && row.nullRate > 0.01 ? '#ca8a04' : '' }">
              {{ row.nullRate != null ? (row.nullRate * 100).toFixed(1) + '%' : '—' }}
            </span>
          </template>
        </el-table-column>
      </el-table>
      <el-empty v-if="!fieldLoading && fieldItems.length === 0" description="没有找到匹配的字段" />
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed, onMounted, ref } from 'vue'
import {
  Search, Coin, CircleCheckFilled, WarningFilled, Service,
  OfficeBuilding, Clock, Grid, Collection,
} from '@element-plus/icons-vue'
import Index from '@/components/page-header/index.vue'
import TabNav from '@/components/tab-nav/index.vue'
import type { TabItem } from '@/components/tab-nav/types'
import { catalogService } from '@/api/services/catalog'
import type { CatalogDatasetItem, CatalogFieldItem, CatalogStats } from '@/api/types'

const activeTab = ref('全部数据集')
const searchTerm = ref('')
const qualityFilter = ref('')
const sourceFilter = ref('')
const domainFilter = ref('')
const agentFilter = ref<string | boolean>('')
const fieldSearch = ref('')
const loading = ref(false)
const fieldLoading = ref(false)

const tabs: TabItem[] = [
  { key: '全部数据集', label: '全部数据集' },
  { key: '字段目录', label: '字段目录' },
]

const datasets = ref<CatalogDatasetItem[]>([])
const fieldItems = ref<CatalogFieldItem[]>([])
const stats = ref<CatalogStats>({ total: 0, qualityOk: 0, qualityWarning: 0, agentAccessible: 0, byDomain: [] })

function qualityLabel(s: string | null) {
  const map: Record<string, string> = { ok: '正常', warning: '警告', error: '异常' }
  return map[s || ''] || '—'
}

function formatDate(s: string) {
  return s ? s.substring(0, 10) : '—'
}

async function onSearch() {
  await loadDatasets()
}

async function loadDatasets() {
  loading.value = true
  try {
    const params: Record<string, unknown> = { page: 1, pageSize: 100 }
    if (searchTerm.value) params.keyword = searchTerm.value
    if (qualityFilter.value) params.quality = qualityFilter.value
    if (sourceFilter.value) params.source = sourceFilter.value
    if (domainFilter.value) params.domain = domainFilter.value
    if (agentFilter.value !== '') params.isAgentAccessible = agentFilter.value
    const res = await catalogService.getDatasets(params as any)
    datasets.value = res.items
  } catch {
    datasets.value = []
  } finally {
    loading.value = false
  }
}

async function loadFields() {
  fieldLoading.value = true
  try {
    const params: Record<string, unknown> = { page: 1, pageSize: 100 }
    if (fieldSearch.value) params.keyword = fieldSearch.value
    const res = await catalogService.getFields(params as any)
    fieldItems.value = res.items
  } catch {
    fieldItems.value = []
  } finally {
    fieldLoading.value = false
  }
}

async function loadStats() {
  try {
    stats.value = await catalogService.getStats()
  } catch {
    // keep defaults
  }
}

onMounted(() => {
  loadDatasets()
  loadStats()
  loadFields()
})
</script>

<style lang="scss" scoped>
.toolbar { display: flex; align-items: center; gap: 12px; }
.search-input { width: 360px; }
.filter-select { width: 130px; }
.filter-input { width: 140px; }

.stat-row { margin: 0 !important; :deep(.el-col) { padding-left: 8px !important; padding-right: 8px !important; } :deep(.el-col:first-child) { padding-left: 0 !important; } :deep(.el-col:last-child) { padding-right: 0 !important; } }

.info-card { :deep(.el-card__body) { display: flex; flex-direction: column; gap: 8px; padding: 20px; } }
.info-card-header { display: flex; align-items: center; gap: 6px; }
.info-card-icon { display: flex; align-items: center; justify-content: center; width: 32px; height: 32px; border-radius: 8px; &.bg-blue { background: #dbeafe; color: var(--el-color-primary); } &.bg-green { background: #dcfce7; color: var(--el-color-success); } &.bg-yellow { background: #fef3c7; color: var(--el-color-warning); } &.bg-purple { background: #ede9fe; color: #7c3aed; } }
.info-card-label { font-size: 14px; color: var(--el-text-color-secondary); }
.info-card-value-row { display: flex; align-items: baseline; gap: 8px; }
.info-card-value { font-size: 28px; font-weight: 700; color: var(--el-text-color-primary); &.green { color: var(--el-color-success); } &.yellow { color: var(--el-color-warning); } }

.dataset-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px; }
@media (max-width: 1200px) { .dataset-grid { grid-template-columns: repeat(2, 1fr); } }
@media (max-width: 750px) { .dataset-grid { grid-template-columns: 1fr; } }

.dataset-card { :deep(.el-card__body) { display: flex; flex-direction: column; gap: 12px; padding: 20px; } &.border-red { border: 1px solid #fecaca; } &.border-yellow { border: 1px solid #fef08a; } }
.ds-top { display: flex; flex-direction: column; gap: 4px; }
.ds-name-row { display: flex; align-items: center; gap: 8px; }
.ds-dot { width: 8px; height: 8px; border-radius: 50%; flex-shrink: 0; &.green { background: var(--el-color-success); } &.yellow { background: var(--el-color-warning); } &.red { background: var(--el-color-danger); } }
.ds-name { font-size: 14px; font-weight: 600; color: var(--el-text-color-primary); flex: 1; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
.ds-code-row { display: flex; align-items: center; gap: 8px; padding-left: 16px; }
.ds-code { font-size: 12px; color: var(--el-text-color-placeholder); font-family: monospace; }
.ds-meta-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 8px 16px; }
.ds-meta-item { display: flex; align-items: center; gap: 4px; font-size: 12px; color: var(--el-text-color-secondary); }
.text-gray { color: var(--el-text-color-placeholder); }
.ds-actions { display: flex; align-items: center; justify-content: space-between; padding-top: 12px; border-top: 1px solid #f0f0f0; }
</style>
