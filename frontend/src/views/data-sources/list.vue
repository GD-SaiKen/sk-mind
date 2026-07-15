<template>
  <div class="page-layout">
    <PageHeader
      title="数据源"
      :breadcrumb="[{ label: '首页', to: '/' }, { label: '数据源' }]"
      description="管理企业数据源连接，维护数据源的基础信息、接入方式和负责人。"
    >
      <template #actions>
        <el-button type="primary" :icon="Plus" @click="openCreate">新增数据源</el-button>
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
              @click="handleView(row)"
            >{{ row.name }}</el-link>
            <div class="row-sub">{{ row.description }}</div>
          </template>
        </Table>
      </template>
    </Crud>

    <el-dialog
      v-model="dialogVisible"
      :title="editingId ? '编辑数据源' : '新增数据源'"
      width="600px"
      destroy-on-close
      @closed="resetForm"
    >
      <el-form :model="form" label-width="100px">
        <el-form-item label="名称" required>
          <el-input v-model="form.name" maxlength="200" />
        </el-form-item>
        <el-form-item label="编码" required>
          <el-input v-model="form.code" maxlength="100" :disabled="!!editingId" />
        </el-form-item>
        <el-form-item label="类型" required>
          <el-select v-model="form.sourceType" style="width: 100%">
            <el-option label="数据库 (database)" value="database" />
            <el-option label="API 接口 (api)" value="api" />
            <el-option label="Excel 文件 (excel)" value="excel" />
            <el-option label="CSV 文件 (csv)" value="csv" />
          </el-select>
        </el-form-item>
        <el-form-item label="接入方式" required>
          <el-select v-model="form.accessMethod" style="width: 100%">
            <el-option label="数据库同步 (db_sync)" value="db_sync" />
            <el-option label="API 拉取 (api_pull)" value="api_pull" />
            <el-option label="文件上传 (file_upload)" value="file_upload" />
          </el-select>
        </el-form-item>
        <el-form-item label="描述">
          <el-input v-model="form.description" type="textarea" :rows="2" />
        </el-form-item>
        <el-row :gutter="12">
          <el-col :span="12">
            <el-form-item label="业务负责人">
              <el-input v-model="form.businessOwner" maxlength="100" placeholder="姓名" />
            </el-form-item>
          </el-col>
          <el-col :span="12">
            <el-form-item label="技术负责人">
              <el-input v-model="form.techOwner" maxlength="100" placeholder="姓名" />
            </el-form-item>
          </el-col>
        </el-row>
        <el-form-item label="所属部门">
          <el-input v-model="form.ownerDept" maxlength="100" />
        </el-form-item>
      </el-form>
      <template #footer>
        <el-button @click="dialogVisible = false">取消</el-button>
        <el-button type="primary" :loading="saving" @click="handleSave">
          {{ editingId ? '保存' : '创建' }}
        </el-button>
      </template>
    </el-dialog>
  </div>
</template>

<script setup lang="ts">
import { onMounted, reactive, ref } from 'vue'
import { useRouter } from 'vue-router'
import { Plus, View, Edit, Delete } from '@element-plus/icons-vue'
import { ElMessage, ElMessageBox } from 'element-plus'
import { dataSourceService } from '@/api/services/data-source'
import PageHeader from '@/components/page-header.vue'
import { Crud, Table } from '@/components/crud'
import type { ColumnSchema, FilterItem } from '@/components/crud'

const router = useRouter()

interface DS {
  id: string
  name: string
  code: string
  sourceType: string
  accessMethod: string
  description: string
  businessOwner: string
  techOwner: string
  ownerDept: string
  status: string
  lastSyncAt: string
  taskCount: number
  createdAt: string
}

const tableRef = ref()
const sources = ref<DS[]>([])
const loading = ref(false)
const filterItems: FilterItem[] = [
  { key: 'keyword', placeholder: '数据源名称...', width: '220px' },
  {
    key: 'type', type: 'select', placeholder: '类型', width: '120px',
    options: [
      { label: '数据库', value: 'database' },
      { label: 'API 接口', value: 'api' },
      { label: 'Excel', value: 'excel' },
      { label: 'CSV', value: 'csv' },
    ],
  },
  {
    key: 'status', type: 'select', placeholder: '状态', width: '100px',
    options: [
      { label: '正常', value: 'active' },
      { label: '草稿', value: 'draft' },
      { label: '停用', value: 'paused' },
    ],
  },
  { key: 'owner', placeholder: '负责人...', width: '160px' },
]
const filterValues = ref<Record<string, any>>({})

// 分页
const page = ref(1)
const pageSize = ref(20)
const total = ref(0)

const paginationConfig = reactive({
  page, pageSize,
  get total() { return total.value },
  onPageChange(p: number) { page.value = p; load() },
  onSizeChange(s: number) { pageSize.value = s; page.value = 1; load() },
})

// 状态映射
const statusLabelMap: Record<string, string> = { active: '正常', draft: '草稿', paused: '停用', archived: '已归档' }
const statusTagMap: Record<string, '' | 'success' | 'warning' | 'danger' | 'info'> = { active: 'success', draft: 'info', paused: 'warning', archived: 'warning' }
const sourceTypeLabelMap: Record<string, string> = { database: '数据库', api: 'API 接口', excel: 'Excel', csv: 'CSV' }
const accessMethodLabelMap: Record<string, string> = { db_sync: '数据库同步', api_pull: 'API 拉取', file_upload: '文件上传' }

const columns: ColumnSchema[] = [
  { type: 'custom', prop: 'name', label: '数据源名称', minWidth: 180 },
  { type: 'tag', prop: 'sourceType', label: '类型', width: 90, formatter: (v: string) => sourceTypeLabelMap[v] ?? v },
  { type: 'text', prop: 'accessMethod', label: '接入方式', width: 110, formatter: (v: string) => accessMethodLabelMap[v] ?? v },
  { type: 'tag', prop: 'status', label: '状态', width: 80, tagMap: statusTagMap, formatter: (v: string) => statusLabelMap[v] ?? v },
  { type: 'text', prop: 'businessOwner', label: '业务负责人', width: 100 },
  { type: 'text', prop: 'techOwner', label: '技术负责人', width: 100 },
  { type: 'date', prop: 'lastSyncAt', label: '最近接入时间', width: 170 },
  { type: 'text', prop: 'taskCount', label: '关联任务', width: 80, align: 'center' },
  {
    type: 'action', label: '操作', width: 200,
    buttons: [
      { label: '查看', icon: View, onClick: (row) => handleView(row as DS) },
      { label: '编辑', icon: Edit, onClick: (row) => openEdit(row as DS) },
      { label: '创建接入任务', icon: Plus, onClick: (row) => handleCreateTask(row as DS) },
      { label: '停用', type: 'danger', icon: Delete, onClick: (row) => handleDisable(row as DS), hidden: (row) => (row as DS).status === 'paused' || (row as DS).status === 'archived' },
    ],
  },
]

// 弹窗
const dialogVisible = ref(false)
const editingId = ref('')
const saving = ref(false)
const form = ref({ name: '', code: '', sourceType: 'api', accessMethod: 'api_pull', description: '', businessOwner: '', techOwner: '', ownerDept: '' })

function resetForm() {
  editingId.value = ''
  form.value = { name: '', code: '', sourceType: 'api', accessMethod: 'api_pull', description: '', businessOwner: '', techOwner: '', ownerDept: '' }
}

async function load() {
  loading.value = true
  try {
    const r = await dataSourceService.getList({
      keyword: filterValues.value.keyword || undefined,
      sourceType: filterValues.value.type || undefined,
      status: filterValues.value.status || undefined,
      owner: filterValues.value.owner || undefined,
      page: page.value, pageSize: pageSize.value,
    })
    sources.value = (r.items ?? []).map(normalizeSource)
    total.value = r.total ?? 0
  } finally { loading.value = false }
}

function normalizeSource(item: any): DS {
  return {
    id: item.id ?? '', name: item.name ?? '', code: item.code ?? '',
    sourceType: item.sourceType ?? '', accessMethod: item.accessMethod ?? '',
    description: item.description ?? '',
    businessOwner: item.businessOwner ?? item.ownerName ?? '',
    techOwner: item.techOwner ?? '', ownerDept: item.ownerDept ?? '',
    status: item.status ?? 'draft',
    lastSyncAt: item.lastSyncAt ?? item.createdAt ?? '',
    taskCount: item.taskCount ?? 0, createdAt: item.createdAt ?? '',
  }
}

function openCreate() { resetForm(); dialogVisible.value = true }

async function openEdit(row: DS) {
  editingId.value = row.id
  const detail = await dataSourceService.get(row.id)
  form.value = {
    name: detail.name ?? '', code: detail.code ?? '',
    sourceType: detail.sourceType ?? 'api', accessMethod: detail.accessMethod ?? 'api_pull',
    description: detail.description ?? '',
    businessOwner: detail.businessOwner ?? detail.ownerName ?? '',
    techOwner: detail.techOwner ?? '', ownerDept: detail.ownerDept ?? '',
  }
  dialogVisible.value = true
}

async function handleSave() {
  saving.value = true
  try {
    if (editingId.value) { await dataSourceService.update(editingId.value, form.value); ElMessage.success('已保存') }
    else { await dataSourceService.create(form.value); ElMessage.success('已创建') }
    dialogVisible.value = false
    await load()
  } catch { /* handled */ } finally { saving.value = false }
}

function handleView(row: DS) { router.push(`/data-sources/${row.id}`) }
function handleCreateTask(row: DS) { router.push(`/ingestion?sourceId=${row.id}`) }

async function handleDisable(row: DS) {
  await ElMessageBox.confirm(`确定停用数据源「${row.name}」？停用后关联的接入任务将不再执行。`, '确认停用')
  await dataSourceService.delete(row.id)
  ElMessage.success('已停用')
  await load()
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
