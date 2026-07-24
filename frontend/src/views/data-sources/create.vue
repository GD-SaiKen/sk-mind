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
import type { DataSourceFormData, AuthType, ConnectionConfig } from '@/api'
import {
  SOURCE_TYPE_OPTIONS,
  ACCESS_METHOD_OPTIONS,
  AUTH_TYPE_OPTIONS,
} from '@/constants/data-source'
import PageHeader from '@/components/page-header/index.vue'
import { Form } from '@/components/crud'
import type { FormSection } from '@/components/crud'

const router = useRouter()
const formRef = ref<InstanceType<typeof Form>>()
const saving = ref(false)

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
  // ── API 连接配置（扁平字段，保存时打包为 connectionConfig）──
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

// 鉴权 Header / 凭据 仅在非 none 时显示
const needsAuth = (m: Record<string, any>) => m.authType !== 'none' && m.authType !== undefined
// 双密钥字段仅在 dual_key 时显示
const isDualKey = (m: Record<string, any>) => m.authType === 'dual_key'

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

/** 按接入方式打包连接配置 */
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
      connectionConfig: buildConnectionConfig(),
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
  if (id) router.replace(`/ingestion/create?sourceId=${id}`)
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
