<template>
  <div class="page-layout">
    <PageHeader
      title="数据源"
      :breadcrumb="[
        { label: '首页', to: '/' },
        { label: '数据源' },
      ]"
      description="管理企业数据源连接，维护数据源的基础信息、接入方式和负责人。"
    >
      <template #actions>
        <el-button
          type="primary"
          :icon="Plus"
          @click="router.push('/data-sources/create')"
        >新增数据源</el-button>
      </template>
    </PageHeader>

    <Crud
      :filter-items="filterItems"
      v-model:filter-values="filterValues"
      :pagination="paginationConfig"
      @filter-change="load"
    >
      <template #table>
        <Table
          ref="tableRef"
          :columns="columns"
          :data="sources"
          :loading="loading"
        >
          <template #col-name="{ row }">
            <el-link
              type="primary"
              :underline="false"
              @click="router.push(`/data-sources/${row.id}`)"
            >{{ row.name }}</el-link>
            <div class="row-sub">{{ row.description }}</div>
          </template>
      <template #col-taskCount="{ row }">
        <el-link
          v-if="row.taskCount > 0"
          type="primary"
          :underline="false"
          @click="router.push(`/ingestion?sourceId=${row.id}`)"
        >{{ row.taskCount }}</el-link>
        <span v-else>0</span>
      </template>
        </Table>
      </template>
    </Crud>
  </div>
</template>

<script setup lang="ts">
import { onMounted, reactive, ref } from 'vue'
import { useRouter } from 'vue-router'
import { Plus, View, Edit, Delete, VideoPlay } from '@element-plus/icons-vue'
import { RefreshRight, SwitchButton } from '@element-plus/icons-vue'
import { ElMessage, ElMessageBox } from 'element-plus'
import { dataSourceService } from '@/api'
import type { DataSource } from '@/api'
import {
  SOURCE_TYPE_LABELS,
  ACCESS_METHOD_LABELS,
  STATUS_LABELS,
  STATUS_TAG_MAP,
} from '@/constants/data-source'
import PageHeader from '@/components/page-header/index.vue'
import { Crud, Table } from '@/components/crud'
import type { ColumnSchema, FilterItem } from '@/components/crud'

const router = useRouter()

const tableRef = ref()
const sources = ref<DataSource[]>([])
const loading = ref(false)

// 筛选
const filterItems: FilterItem[] = [
  {
    key: 'keyword',
    placeholder: '请输入关键词...',
    width: '220px',
  },
  {
    key: 'type',
    type: 'select',
    placeholder: '类型',
    width: '110px',
    options: Object.entries(SOURCE_TYPE_LABELS).map(([v, l]) => ({ label: l, value: v })),
  },
  {
    key: 'status',
    type: 'select',
    placeholder: '状态',
    width: '100px',
    options: Object.entries(STATUS_LABELS).map(([v, l]) => ({ label: l, value: v })),
  },
  {
    key: 'owner',
    placeholder: '负责人...',
    width: '160px',
  },
]

const filterValues = ref<Record<string, any>>({})

// 分页
const page = ref(1)
const pageSize = ref(20)
const total = ref(0)

const paginationConfig = reactive({
  page,
  pageSize,
  get total() {
    return total.value
  },
  onPageChange(p: number) {
    page.value = p
    load()
  },
  onSizeChange(s: number) {
    pageSize.value = s
    page.value = 1
    load()
  },
})

// 列表列
const columns: ColumnSchema[] = [
  {
    type: 'custom',
    prop: 'name',
    label: '数据源名称',
    minWidth: 120,
  },
  {
    type: 'tag',
    prop: 'sourceType',
    label: '类型',
    width: 90,
    formatter: (v: string) => SOURCE_TYPE_LABELS[v as keyof typeof SOURCE_TYPE_LABELS] ?? v,
  },
  {
    type: 'text',
    prop: 'accessMethod',
    label: '接入方式',
    width: 110,
    formatter: (v: string) => ACCESS_METHOD_LABELS[v as keyof typeof ACCESS_METHOD_LABELS] ?? v,
  },
  {
    type: 'tag',
    prop: 'status',
    label: '状态',
    width: 80,
    tagMap: STATUS_TAG_MAP,
    formatter: (v: string) => STATUS_LABELS[v as keyof typeof STATUS_LABELS] ?? v,
  },
  {
    type: 'text',
    prop: 'businessOwner',
    label: '业务负责人',
    width: 100,
  },
  {
    type: 'text',
    prop: 'techOwner',
    label: '技术负责人',
    width: 100,
  },
  {
    type: 'date',
    prop: 'lastSyncAt',
    label: '最近接入时间',
    width: 170,
  },
  {
    type: 'custom',
    prop: 'taskCount',
    label: '关联任务',
    width: 100,
    align: 'center',
  },
  {
    type: 'action',
    label: '操作',
    width: 260,
    buttons: [
      {
        label: '查看',
        icon: View,
        onClick: (row) => router.push(`/data-sources/${(row as DataSource).id}`),
      },
      {
        label: '编辑',
        icon: Edit,
        onClick: (row) => router.push(`/data-sources/${(row as DataSource).id}/edit`),
      },
      {
        label: '创建任务',
        icon: VideoPlay,
        onClick: (row) => router.push(`/ingestion?sourceId=${(row as DataSource).id}`),
        hidden: (row) => (row as DataSource).status === 'paused',
      },
      {
        label: '重试',
        icon: RefreshRight,
        type: 'warning',
        onClick: (row) => handleRetry(row as DataSource),
        hidden: (row) => (row as DataSource).status !== 'error',
      },
      {
        label: '停用',
        icon: SwitchButton,
        type: 'danger',
        onClick: (row) => handlePause(row as DataSource),
        hidden: (row) => {
          const s = (row as DataSource).status
          return s === 'paused' || s === 'syncing' || s === 'syncing'
        },
      },
      {
        label: '启用',
        icon: SwitchButton,
        type: 'success',
        onClick: (row) => handleResume(row as DataSource),
        hidden: (row) => (row as DataSource).status !== 'paused',
      },
    ],
  },
]

async function load() {
  loading.value = true
  try {
    const r = await dataSourceService.getList({
      keyword: filterValues.value.keyword || undefined,
      sourceType: filterValues.value.type || undefined,
      status: filterValues.value.status || undefined,
      owner: filterValues.value.owner || undefined,
      page: page.value,
      pageSize: pageSize.value,
    })
    sources.value = (r.items ?? []) as DataSource[]
    total.value = r.total ?? 0
  } finally {
    loading.value = false
  }
}

async function handlePause(row: DataSource) {
  await ElMessageBox.confirm(
    `确定停用数据源「${row.name}」？停用后关联的接入任务将不再执行。`,
    '确认停用',
  )
  try {
    await dataSourceService.pause(row.id)
  } catch { return }
  ElMessage.success('已停用')
  await load()
}

async function handleRetry(row: DataSource) {
  ElMessage.info('重试已提交')
  await load()
}

async function handleResume(row: DataSource) {
  try {
    await dataSourceService.resume(row.id)
    ElMessage.success('已启用')
    await load()
  } catch { /* handled by interceptor */ }
}

onMounted(load)
</script>

<style lang="scss" scoped>
.row-sub {
  font-size: 11px;
  color: $color-text-placeholder;
  margin-top: 2px;
}
</style>
