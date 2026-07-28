<template>
  <div class="page-layout">
    <Index
      title="数据表"
      :breadcrumb="[{ label: '首页', to: '/' }, { label: '数据表' }]"
      description="查看平台中已接入的数据表，了解表结构、字段信息和质量状态。"
    >
      <template #actions>
        <el-button :icon="DataAnalysis" @click="router.push('/tables/browse')">Raw 数据浏览</el-button>
      </template>
    </Index>

    <Crud
      :filter-items="filterItems"
      v-model:filter-values="filterValues"
      :pagination="pagination"
      @filter-change="load"
    >
      <template #table>
        <Table
          ref="tableRef"
          :columns="columns"
          :data="tables"
          :loading="loading"
          empty-text="当前还没有接入数据"
        >
          <template #col-name="{ row }">
            <el-link type="primary" :underline="false" @click="router.push(`/tables/${row.id}`)">
              {{ row.tableName }}
            </el-link>
            <div class="row-sub">{{ row.displayName }}</div>
          </template>
          <template #col-layer="{ row }">
            <el-tag effect="plain" :type="layerTagType(row.layer)">{{ row.layer }}</el-tag>
          </template>
          <template #col-sourceName="{ row }">
            <el-link type="primary" :underline="false" @click="router.push('/data-sources')">{{ row.sourceName }}</el-link>
          </template>
          <template #col-qualityStatus="{ row }">
            <el-tag :type="qualityTagType(row.qualityStatus)" effect="plain">{{ qualityLabel(row.qualityStatus) }}</el-tag>
          </template>
          <template #col-agentEnabled="{ row }">
            <el-tag :type="row.agentEnabled ? 'success' : 'info'" effect="plain">{{ row.agentEnabled ? '已开放' : '未开放' }}</el-tag>
          </template>
        </Table>
      </template>
    </Crud>
  </div>
</template>

<script setup lang="ts">
import { onMounted, reactive, ref } from 'vue'
import { useRouter } from 'vue-router'
import { DataAnalysis, Edit, View, Setting, Connection } from '@element-plus/icons-vue'
import Index from '@/components/page-header/index.vue'
import { Crud, Table } from '@/components/crud'
import type { ColumnSchema, FilterItem } from '@/components/crud'
import { datasetService } from '@/api/services/dataset'
import type { DatasetResponse } from '@/api/types'

const router = useRouter()

interface DataTable {
  id: string; tableName: string; displayName: string; layer: string; sourceName: string
  recordCount: number; fieldCount: number; qualityStatus: string; agentEnabled: boolean; updatedAt: string
}

function mapDatasetToTable(ds: DatasetResponse): DataTable {
  return {
    id: ds.id,
    tableName: ds.code,
    displayName: ds.name,
    layer: ds.dataLayer || '-',
    sourceName: ds.sourceName || ds.dataSourceId || '-',
    recordCount: ds.recordCount ?? 0,
    fieldCount: ds.fieldCount ?? 0,
    qualityStatus: ds.qualityStatus || (ds.status === 'active' ? 'ok' : ds.status === 'archived' ? 'error' : 'warning'),
    agentEnabled: ds.isAgentAccessible,
    updatedAt: ds.updatedAt,
  }
}

const tableRef = ref()
const tables = ref<DataTable[]>([])
const loading = ref(false)

const filterItems: FilterItem[] = [
  { key: 'keyword', placeholder: '搜索表名或显示名...', width: '220px' },
  { key: 'source', type: 'input', placeholder: '来源', width: '140px' },
  { key: 'layer', type: 'select', placeholder: '层级', width: '120px',
    options: [{ label: '全部层级', value: '' }, { label: 'Raw', value: 'raw' }, { label: 'Clean', value: 'clean' }, { label: 'Serving', value: 'serving' }] },
  { key: 'quality', type: 'select', placeholder: '质量状态', width: '120px',
    options: [{ label: '全部', value: '' }, { label: '正常', value: 'ok' }, { label: '警告', value: 'warning' }, { label: '异常', value: 'error' }] },
  { key: 'agent', type: 'select', placeholder: 'Agent 可用', width: '130px',
    options: [{ label: '全部', value: '' }, { label: '已开放', value: 'true' }, { label: '未开放', value: 'false' }] },
  { key: 'category', type: 'input', placeholder: '业务域', width: '130px' },
]
const filterValues = ref<Record<string, any>>({})

const page = ref(1)
const pageSize = ref(20)
const total = ref(0)

const pagination = reactive({
  page, pageSize,
  get total() { return total.value },
  onPageChange(p: number) { page.value = p; load() },
  onSizeChange(s: number) { pageSize.value = s; page.value = 1; load() },
})

function layerTagType(layer: string) {
  if (layer === 'serving' || layer === 'Serving') return 'success'
  if (layer === 'clean' || layer === 'Clean') return 'warning'
  return ''
}
function qualityTagType(status: string) { if (status === 'ok' || status === 'pass') return 'success'; if (status === 'warning') return 'warning'; if (status === 'error') return 'danger'; return 'info' }
function qualityLabel(status: string) { const map: Record<string, string> = { ok: '正常', pass: '正常', warning: '警告', error: '异常' }; return map[status] ?? status }

const columns: ColumnSchema[] = [
  { type: 'custom', prop: 'name', label: '数据表', minWidth: 180 },
  { type: 'custom', prop: 'layer', label: '层级', width: 100, align: 'center' },
  { type: 'custom', prop: 'sourceName', label: '来源', width: 130 },
  { type: 'text', prop: 'recordCount', label: '记录数', width: 100, align: 'right', formatter: (v: number) => v?.toLocaleString() ?? '-' },
  { type: 'text', prop: 'fieldCount', label: '字段数', width: 80, align: 'center' },
  { type: 'custom', prop: 'qualityStatus', label: '质量', width: 80, align: 'center' },
  { type: 'custom', prop: 'agentEnabled', label: 'Agent 可用', width: 100, align: 'center' },
  { type: 'date', prop: 'updatedAt', label: '更新时间', width: 170 },
  {
    type: 'action', label: '操作', width: 200,
    buttons: [
      { label: '查看', icon: View, onClick: (row) => router.push(`/tables/${(row as DataTable).id}`) },
      { label: '编辑说明', icon: Edit, onClick: (_row) => {} },
      { label: '配置权限', icon: Setting, onClick: (_row) => {} },
      { label: '建立映射', icon: Connection, onClick: (_row) => {} },
    ],
  },
]

async function load() {
  loading.value = true
  try {
    const params: Record<string, unknown> = {
      page: page.value,
      pageSize: pageSize.value,
    }
    const fv = filterValues.value
    if (fv.keyword) params.keyword = fv.keyword
    if (fv.source) params.source = fv.source
    if (fv.layer) params.dataLayer = fv.layer
    if (fv.quality) params.quality = fv.quality
    if (fv.agent !== undefined && fv.agent !== '') params.isAgentAccessible = fv.agent === 'true'
    if (fv.category) params.category = fv.category
    const res = await datasetService.getList(params)
    tables.value = res.items.map(mapDatasetToTable)
    total.value = res.total
  } catch {
    tables.value = []
    total.value = 0
  } finally {
    loading.value = false
  }
}

onMounted(() => { load() })
</script>

<style lang="scss" scoped>
.row-sub { font-size: 11px; color: $color-text-placeholder; margin-top: 2px; }
</style>
