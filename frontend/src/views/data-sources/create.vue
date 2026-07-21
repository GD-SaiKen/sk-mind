<template>
  <div class="page-layout detail-page">
    <PageHeader
      title="新增数据源"
      :breadcrumb="[
        { label: '首页', to: '/' },
        { label: '数据源', to: '/data-sources' },
        { label: '新增数据源' },
      ]"
    />

    <el-card shadow="never">
      <Form
        ref="formRef"
        v-model="form"
        :sections="sections"
        label-width="120px"
      />

      <template #footer>
        <div class="form-footer">
          <el-button @click="router.back()">取消</el-button>
          <div class="form-footer-right">
            <el-button
              type="primary"
              :loading="saving"
              @click="handleSave"
            >保存</el-button>
            <el-button
              type="success"
              :loading="saving"
              @click="handleSaveAndCreateTask"
            >保存并创建接入任务</el-button>
          </div>
        </div>
      </template>
    </el-card>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { ElMessage } from 'element-plus'
import { dataSourceService } from '@/api'
import type { DataSourceFormData } from '@/api'
import { SOURCE_TYPE_OPTIONS, ACCESS_METHOD_OPTIONS } from '@/constants/data-source'
import PageHeader from '@/components/page-header/index.vue'
import { Form } from '@/components/crud'
import type { FormSection } from '@/components/crud'

const router = useRouter()
const formRef = ref<InstanceType<typeof Form>>()
const saving = ref(false)

const form = ref<DataSourceFormData & { remark: string }>({
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
    cols: 2,
    description: '描述数据源的基本属性',
    fields: [
      {
        type: 'input',
        prop: 'name',
        label: '数据源名称',
        placeholder: '如"生产订单数据"，只描述数据内容',
        rules: { required: true, message: '名称不能为空' },
        maxlength: 200,
        tip: '建议只描述数据内容，不包含系统名',
      },
      {
        type: 'input',
        prop: 'code',
        label: '编码',
        placeholder: '系统唯一标识',
        rules: { required: true, message: '编码不能为空' },
        maxlength: 100,
        tip: '创建后不可修改',
      },
      {
        type: 'select',
        prop: 'sourceType',
        label: '类型',
        options: SOURCE_TYPE_OPTIONS,
        rules: { required: true, message: '请选择类型' },
        tip: '选择最贴切的类型即可。如"ERP"或"数据库"',
      },
      {
        type: 'textarea',
        prop: 'description',
        label: '备注',
        placeholder: '为什么要建、有什么注意事项',
        rows: 2,
        colSpan: 2
      },
    ],
  },
  {
    title: '二、接入配置',
    cols: 2,
    description: '决定用什么技术手段把数据搬进平台',
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
    description: '指定数据源的责任人和业务分类',
    cols: 2,
    fields: [
      {
        type: 'input',
        prop: 'businessOwner',
        label: '业务负责人',
        placeholder: '姓名',
        tip: '出问题时优先确认数据含义和业务影响',
      },
      {
        type: 'input',
        prop: 'techOwner',
        label: '技术负责人',
        placeholder: '姓名',
        tip: '排查连接/配置/执行问题',
      },
      {
        type: 'input',
        prop: 'remark',
        label: '标签',
        placeholder: '自由文本（后续切换为选择模式）⏸️',
        tip: '标签字典未建立，暂时自由输入',
      },
    ],
  },
]

async function doSave(): Promise<string | null> {
  const valid = await formRef.value?.validate()
  if (!valid) return null
  try {
    saving.value = true
    const result = await dataSourceService.create({
      name: form.value.name,
      code: form.value.code,
      sourceType: form.value.sourceType,
      accessMethod: form.value.accessMethod,
      description: form.value.description,
      businessOwner: form.value.businessOwner,
      techOwner: form.value.techOwner,
      ownerDept: form.value.ownerDept,
    })
    ElMessage.success('数据源创建成功')
    return result?.id ?? null
  } catch {
    return null
  } finally {
    saving.value = false
  }
}

async function handleSave() {
  const id = await doSave()
  if (id) router.replace(`/data-sources/${id}`)
}

async function handleSaveAndCreateTask() {
  const id = await doSave()
  if (id) router.replace(`/ingestion?sourceId=${id}`)
}
</script>

<style lang="scss" scoped>
.form-footer {
  display: flex;
  justify-content: space-between;
  width: 100%;
}

.form-footer-right {
  display: flex;
  gap: 8px;
}
</style>
