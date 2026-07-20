<template>
  <div class="page-layout detail-page">
    <PageHeader
      :title="`编辑数据源 - ${originalName}`"
      :breadcrumb="[
        { label: '首页', to: '/' },
        { label: '数据源', to: '/data-sources' },
        { label: originalName, to: `/data-sources/${id}` },
        { label: '编辑' },
      ]"
    >
      <template #tags>
        <el-tag
          v-if="source"
          :type="STATUS_TAG_MAP[source.status]"
          effect="plain"
        >{{ STATUS_LABELS[source.status] }}</el-tag>
      </template>
    </PageHeader>

    <div v-if="loading" class="loading-wrap">
      <el-skeleton :rows="8" />
    </div>
    <el-card v-else shadow="never">
      <Form
        ref="formRef"
        v-model="form"
        :sections="sections"
        label-width="110px"
      />
      <template #footer>
        <div class="form-footer">
          <el-button @click="router.back()">取消</el-button>
          <el-button
            type="primary"
            :loading="saving"
            @click="handleSave"
          >保存</el-button>
        </div>
      </template>
    </el-card>
  </div>
</template>

<script setup lang="ts">
import { onMounted, reactive, ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { ElMessage } from 'element-plus'
import { dataSourceService } from '@/api'
import type { DataSource, DataSourceFormData } from '@/api'
import {
  SOURCE_TYPE_OPTIONS,
  ACCESS_METHOD_OPTIONS,
  STATUS_LABELS,
  STATUS_TAG_MAP,
} from '@/constants/data-source'
import PageHeader from '@/components/page-header/index.vue'
import { Form } from '@/components/crud'
import type { FormSection } from '@/components/crud'

const route = useRoute()
const router = useRouter()
const id = route.params.id as string
const formRef = ref<InstanceType<typeof Form>>()
const loading = ref(true)
const saving = ref(false)
const source = ref<DataSource | null>(null)
const originalName = ref('')

const form = reactive<DataSourceFormData & { remark: string }>({
  name: '',
  code: '',
  sourceType: 'erp',
  accessMethod: 'db_sync',
  description: '',
  businessOwner: '',
  techOwner: '',
  ownerDept: '',
  remark: '',
})

const sections: FormSection[] = [
  {
    title: '一、基本信息',
    fields: [
      {
        type: 'input',
        prop: 'name',
        label: '数据源名称',
        rules: { required: true, message: '名称不能为空' },
        maxlength: 200,
      },
      {
        type: 'input',
        prop: 'code',
        label: '编码',
        disabled: true,
        tip: '编码创建后不可修改',
      },
      {
        type: 'select',
        prop: 'sourceType',
        label: '类型',
        options: SOURCE_TYPE_OPTIONS,
        rules: { required: true, message: '请选择类型' },
      },
      {
        type: 'textarea',
        prop: 'description',
        label: '备注',
        rows: 2,
      },
    ],
  },
  {
    title: '二、接入配置',
    fields: [
      {
        type: 'select',
        prop: 'accessMethod',
        label: '接入方式',
        options: ACCESS_METHOD_OPTIONS,
        rules: { required: true, message: '请选择接入方式' },
      },
    ],
  },
  {
    title: '三、负责人与标签',
    cols: 2,
    fields: [
      {
        type: 'input',
        prop: 'businessOwner',
        label: '业务负责人',
        placeholder: '姓名',
      },
      {
        type: 'input',
        prop: 'techOwner',
        label: '技术负责人',
        placeholder: '姓名',
      },
      {
        type: 'input',
        prop: 'ownerDept',
        label: '所属部门',
      },
      {
        type: 'input',
        prop: 'remark',
        label: '标签',
        placeholder: '自由文本（后续切换为选择模式）⏸️',
      },
    ],
  },
]

onMounted(async () => {
  try {
    const ds: DataSource = await dataSourceService.get(id)
    source.value = ds
    originalName.value = ds.name ?? ''
    form.name = ds.name ?? ''
    form.code = ds.code ?? ''
    form.sourceType = ds.sourceType ?? 'erp'
    form.accessMethod = ds.accessMethod ?? 'db_sync'
    form.description = ds.description ?? ''
    form.businessOwner = ds.businessOwner ?? ''
    form.techOwner = ds.techOwner ?? ''
    form.ownerDept = ds.ownerDept ?? ''
    form.remark = ''
  } finally {
    loading.value = false
  }
})

async function handleSave() {
  const valid = await formRef.value?.validate()
  if (!valid) return
  saving.value = true
  try {
    await dataSourceService.update(id, {
      name: form.name,
      sourceType: form.sourceType,
      accessMethod: form.accessMethod,
      description: form.description,
      businessOwner: form.businessOwner,
      techOwner: form.techOwner,
      ownerDept: form.ownerDept,
    })
    ElMessage.success('已保存')
    router.replace(`/data-sources/${id}`)
  } catch {
    /* handled */
  } finally {
    saving.value = false
  }
}
</script>

<style lang="scss" scoped>
.loading-wrap {
  padding: 40px;
}

.form-footer {
  display: flex;
  justify-content: space-between;
  width: 100%;
}
</style>
