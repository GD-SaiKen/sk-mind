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
import { onMounted, ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { ElMessage } from 'element-plus'
import { dataSourceService } from '@/api'
import type { DataSource, DataSourceFormData, AuthType, ConnectionConfig } from '@/api'
import {
  SOURCE_TYPE_OPTIONS,
  ACCESS_METHOD_OPTIONS,
  AUTH_TYPE_OPTIONS,
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

const form = ref<DataSourceFormData & {
  remark: string
  baseUrl: string
  authType: AuthType
  authHeaderName: string
  authCredentials: string
  authHeaderName2: string
  authCredentials2: string
  qpsLimit: number
  timeout: number
  sslVerify: boolean
}>({
  name: '',
  code: '',
  sourceType: 'erp',
  accessMethod: 'db_sync',
  description: '',
  businessOwner: '',
  techOwner: '',
  ownerDept: '',
  remark: '',
  baseUrl: '',
  authType: 'none',
  authHeaderName: 'Authorization',
  authCredentials: '',
  authHeaderName2: '',
  authCredentials2: '',
  qpsLimit: 10,
  timeout: 30,
  sslVerify: true,
})

const needsAuth = (m: Record<string, any>) => m.authType !== 'none' && m.authType !== undefined
const isDualKey = (m: Record<string, any>) => m.authType === 'dual_key'

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
    cols: 2,
    fields: [
      {
        type: 'select',
        prop: 'accessMethod',
        label: '接入方式',
        options: ACCESS_METHOD_OPTIONS,
        rules: { required: true, message: '请选择接入方式' },
        tip: '选择"API 拉取"后展开 API 连接配置',
      },
    ],
  },
  {
    title: '三、API 连接配置',
    cols: 2,
    description: '配置目标 API 系统的基础路径、鉴权方式与凭据',
    hidden: (m) => m.accessMethod !== 'api_pull',
    fields: [
      {
        type: 'input',
        prop: 'baseUrl',
        label: '基础路径',
        placeholder: '如 https://mes.example.com',
        rules: { required: true, message: '基础路径不能为空' },
        colSpan: 2,
        tip: 'API 基础路径（主机 + 端口）；具体接口路径在创建接入任务时配置',
      },
      {
        type: 'select',
        prop: 'authType',
        label: '鉴权方式',
        options: AUTH_TYPE_OPTIONS,
        tip: '无鉴权 / Bearer / Basic / API Key / 双密钥 / 动态登录',
      },
      {
        type: 'input',
        prop: 'authHeaderName',
        label: '鉴权 Header 名',
        placeholder: '默认 Authorization',
        hidden: (m) => !needsAuth(m),
        tip: '携带凭据的请求头名称',
      },
      {
        type: 'input',
        prop: 'authCredentials',
        label: '凭据 / 密钥',
        placeholder: 'Token / API Key',
        showPassword: true,
        hidden: (m) => !needsAuth(m),
        colSpan: 2,
        tip: '生产环境建议通过环境变量注入，避免明文落库',
      },
      {
        type: 'input',
        prop: 'authHeaderName2',
        label: '第二 Header 名',
        placeholder: '如 AccessKeySecret',
        hidden: (m) => !isDualKey(m),
      },
      {
        type: 'input',
        prop: 'authCredentials2',
        label: '第二凭据',
        placeholder: '第二密钥',
        showPassword: true,
        hidden: (m) => !isDualKey(m),
      },
      {
        type: 'number',
        prop: 'qpsLimit',
        label: 'QPS 限制',
        min: 1,
        step: 1,
        tip: '令牌桶限流，防止压垮目标系统',
      },
      {
        type: 'number',
        prop: 'timeout',
        label: '超时（秒）',
        min: 1,
        step: 1,
      },
      {
        type: 'switch',
        prop: 'sslVerify',
        label: '验证 SSL 证书',
        tip: '自签名证书场景可关闭',
      },
    ],
  },
  {
    title: '四、负责人与标签',
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
    form.value.name = ds.name ?? ''
    form.value.code = ds.code ?? ''
    form.value.sourceType = ds.sourceType ?? 'erp'
    form.value.accessMethod = ds.accessMethod ?? 'db_sync'
    form.value.description = ds.description ?? ''
    form.value.businessOwner = ds.businessOwner ?? ''
    form.value.techOwner = ds.techOwner ?? ''
    form.value.ownerDept = ds.ownerDept ?? ''
    form.value.remark = ''

    // 回显连接配置
    const cc = ds.connectionConfig
    if (cc) {
      form.value.baseUrl = cc.baseUrl ?? ''
      form.value.authType = (cc.authType as AuthType) ?? 'none'
      form.value.authHeaderName = cc.authHeaderName ?? 'Authorization'
      form.value.authCredentials = cc.authCredentials ?? ''
      form.value.authHeaderName2 = cc.authHeaderName2 ?? ''
      form.value.authCredentials2 = cc.authCredentials2 ?? ''
      form.value.qpsLimit = cc.qpsLimit ?? 10
      form.value.timeout = cc.timeout ?? 30
      form.value.sslVerify = cc.sslVerify ?? true
    }
  } finally {
    loading.value = false
  }
})

function buildConnectionConfig(): ConnectionConfig | null {
  if (form.value.accessMethod !== 'api_pull') return null
  const dual = form.value.authType === 'dual_key'
  return {
    baseUrl: form.value.baseUrl,
    authType: form.value.authType,
    authHeaderName: form.value.authHeaderName || undefined,
    authCredentials: form.value.authCredentials || undefined,
    authHeaderName2: dual ? (form.value.authHeaderName2 || undefined) : undefined,
    authCredentials2: dual ? (form.value.authCredentials2 || undefined) : undefined,
    qpsLimit: form.value.qpsLimit,
    timeout: form.value.timeout,
    sslVerify: form.value.sslVerify,
  }
}

async function handleSave() {
  const valid = await formRef.value?.validate()
  if (!valid) return
  saving.value = true
  try {
    await dataSourceService.update(id, {
      name: form.value.name,
      sourceType: form.value.sourceType,
      accessMethod: form.value.accessMethod,
      description: form.value.description,
      businessOwner: form.value.businessOwner,
      techOwner: form.value.techOwner,
      ownerDept: form.value.ownerDept,
      connectionConfig: buildConnectionConfig(),
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
