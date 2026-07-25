<template>
  <div class="page-layout detail-page">
    <!-- ===== 标题区 ===== -->
    <PageHeader
      :title="source?.name ?? '数据源详情'"
      :breadcrumb="[
        { label: '首页', to: '/' },
        { label: '数据源', to: '/data-sources' },
        { label: source?.name ?? '...' },
      ]"
    >
      <template #tags>
        <el-tag
          v-if="source"
          :type="STATUS_TAG_MAP[source.status]"
          effect="plain"
        >{{ STATUS_LABELS[source.status] }}</el-tag>
        <el-tag
          v-if="source"
          effect="plain"
        >{{ SOURCE_TYPE_LABELS[source.sourceType] }}</el-tag>
      </template>
      <template #actions>
        <el-button
          :icon="Edit"
          plain
          @click="router.push(`/data-sources/${id}/edit`)"
        >编辑</el-button>
        <el-button
          v-if="showCreateTask"
          :icon="VideoPlay"
          plain
          @click="router.push(`/ingestion/create?sourceId=${id}`)"
        >创建任务</el-button>
        <el-button
          v-if="showTestConn"
          plain
          @click="handleTestConnection"
        >检测连接</el-button>
        <el-button
          v-if="showPause"
          :icon="SwitchButton"
          plain
          type="danger"
          @click="handlePause"
        >停用</el-button>
        <el-button
          v-if="showResume"
          plain
          type="success"
          @click="handleResume"
        >启用</el-button>
      </template>
    </PageHeader>

    <!-- 加载态 -->
    <div v-if="loading" class="loading-wrap">
      <el-skeleton :rows="6" />
    </div>

    <!-- 不存在 -->
    <el-empty
      v-else-if="!source"
      description="数据源不存在"
    />

    <!-- ===== 内容 ===== -->
    <template v-else>
      <!-- 摘要区 -->
      <el-row class="summary-row" :gutter="16">
        <el-col :span="6">
          <div class="summary-card">
            <div class="summary-label">接入方式</div>
            <div class="summary-value">{{ ACCESS_METHOD_LABELS[source.accessMethod] }}</div>
          </div>
        </el-col>
        <el-col :span="6">
          <div class="summary-card">
            <div class="summary-label">业务负责人</div>
            <div class="summary-value">{{ source.businessOwner || '-' }}</div>
          </div>
        </el-col>
        <el-col :span="6">
          <div class="summary-card">
            <div class="summary-label">技术负责人</div>
            <div class="summary-value">{{ source.techOwner || '-' }}</div>
          </div>
        </el-col>
        <el-col :span="6">
          <div class="summary-card">
            <div class="summary-label">最近接入时间</div>
            <div class="summary-value">{{ source.lastSyncAt || '未接入' }}</div>
          </div>
        </el-col>
      </el-row>

      <!-- 标签页 -->
      <el-tabs v-model="activeTab">
        <!-- 基本信息 -->
        <el-tab-pane label="基本信息" name="info">
          <Form
            v-model="formReadonly"
            :sections="infoSections"
            label-width="110px"
          />
        </el-tab-pane>

        <!-- 系统状态 -->
        <el-tab-pane
          label="系统状态"
          name="status"
        >
          <Form
            v-model="formStatus"
            :sections="statusSections"
            label-width="110px"
          />
        </el-tab-pane>

        <!-- 接入任务 -->
        <el-tab-pane
          label="接入任务"
          name="tasks"
        >
          <el-card shadow="never">
            <div class="tab-header">
              <h3>关联的接入任务</h3>
              <el-button
                type="primary"
                @click="router.push(`/ingestion/create?sourceId=${id}`)"
              >创建新任务</el-button>
            </div>
            <div v-if="loadingTasks" class="loading-wrap">
              <el-skeleton :rows="2" />
            </div>
            <el-empty
              v-else-if="relatedTasks.length === 0"
              description="暂无接入任务"
              :image-size="60"
            />
            <div v-else class="link-list">
              <router-link
                v-for="task in relatedTasks"
                :key="task.id"
                :to="`/ingestion/${task.id}`"
                class="link-item"
              >
                <div class="link-item-left">
                  <el-icon
                    :size="18"
                    :class="task.lastSyncStatus === 'success' ? 'text-success' : task.lastSyncStatus === 'partial_success' ? 'text-warning' : 'text-warning'"
                  >
                    <CircleCheckFilled v-if="task.lastSyncStatus === 'success'" />
                    <WarningFilled v-else />
                  </el-icon>
                  <div>
                    <div>{{ task.name }}</div>
                    <div class="link-item-sub">
                      <template v-if="task.lastSyncAt">最近执行: {{ fmtDateTime(task.lastSyncAt, false) }}</template>
                      <template v-else>尚未执行</template>
                    </div>
                  </div>
                </div>
                <el-tag
                  :type="task.status === 'active' ? 'success' : task.status === 'draft' ? 'info' : task.status === 'paused' ? 'warning' : 'danger'"
                  size="small"
                  effect="plain"
                >{{ task.status }}</el-tag>
              </router-link>
            </div>
          </el-card>
        </el-tab-pane>

        <!-- 产出数据表 -->
        <el-tab-pane
          label="产出数据表"
          name="tables"
        >
          <el-card shadow="never">
            <h3>产出的数据表</h3>
            <el-empty
              description="暂无产出数据表"
              :image-size="60"
            />
          </el-card>
        </el-tab-pane>

        <!-- 风险说明 -->
        <el-tab-pane label="风险说明" name="risk">
          <el-card shadow="never">
            <h3>风险说明</h3>
            <el-empty
              description="待后续版本实现"
              :image-size="60"
            />
          </el-card>
        </el-tab-pane>

        <!-- 操作记录 -->
        <el-tab-pane label="操作记录" name="logs">
          <el-card shadow="never">
            <h3>操作记录</h3>
            <div class="log-list">
              <div
                v-for="(log, li) in mockLogs"
                :key="li"
                class="log-item"
                :class="{ highlight: li === 0 }"
              >{{ log }}</div>
            </div>
          </el-card>
        </el-tab-pane>
      </el-tabs>
    </template>
  </div>
</template>

<script setup lang="ts">
import { computed, onMounted, reactive, ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import {
  Edit,
  VideoPlay,
  SwitchButton,
  CircleCheckFilled,
  WarningFilled,
} from '@element-plus/icons-vue'
import { ElMessage, ElMessageBox } from 'element-plus'
import { dataSourceService, ingestionService } from '@/api'
import type { DataSource, IngestionTask } from '@/api'
import {
  SOURCE_TYPE_LABELS,
  ACCESS_METHOD_LABELS,
  AUTH_TYPE_LABELS,
  STATUS_LABELS,
  STATUS_TAG_MAP,
} from '@/constants/data-source'
import PageHeader from '@/components/page-header/index.vue'
import { Form } from '@/components/crud'
import type { FormSection } from '@/components/crud'
import { fmtDateTime } from '@/utils/datetime'

const route = useRoute()
const router = useRouter()
const id = route.params.id as string

const loading = ref(true)
const source = ref<DataSource | null>(null)
const activeTab = ref('info')
const loadingTasks = ref(false)
const relatedTasks = ref<IngestionTask[]>([])

// 操作按钮的显示逻辑（按状态）
const showCreateTask = computed(() => source.value?.status !== 'paused')
const showTestConn = computed(() => source.value?.status === 'active' || source.value?.status === 'error')
const showPause = computed(() => source.value?.status !== 'paused')
const showResume = computed(() => source.value?.status === 'paused')

// 基本信息（readonly 模式）
const formReadonly = reactive<Record<string, any>>({})

const infoSections: FormSection[] = [
  {
    title: '一、基本信息',
    cols: 2,
    fields: [
      {
        type: 'readonly',
        prop: 'name',
        label: '数据源名称',
      },
      {
        type: 'readonly',
        prop: 'code',
        label: '编码',
      },
      {
        type: 'readonly',
        prop: 'sourceType',
        label: '类型',
        formatter: (v: string) => SOURCE_TYPE_LABELS[v as keyof typeof SOURCE_TYPE_LABELS] ?? v,
      },
      {
        type: 'readonly',
        prop: 'description',
        label: '备注',
        formatter: (v: string) => v || '-',
      },
    ],
  },
  {
    title: '二、接入配置',
    cols: 2,
    fields: [
      {
        type: 'readonly',
        prop: 'accessMethod',
        label: '接入方式',
        formatter: (v: string) => ACCESS_METHOD_LABELS[v as keyof typeof ACCESS_METHOD_LABELS] ?? v,
      },
      {
        type: 'readonly',
        prop: 'baseUrl',
        label: '基础路径',
        hidden: (m: Record<string, any>) => m.accessMethod !== 'api_pull',
      },
      {
        type: 'readonly',
        prop: 'authType',
        label: '鉴权方式',
        formatter: (v: string) => AUTH_TYPE_LABELS[v as keyof typeof AUTH_TYPE_LABELS] ?? v ?? '-',
        hidden: (m: Record<string, any>) => m.accessMethod !== 'api_pull',
      },
      {
        type: 'readonly',
        prop: 'authHeaderName',
        label: '鉴权 Header 名',
        formatter: (v: string) => v || '-',
        hidden: (m: Record<string, any>) => m.accessMethod !== 'api_pull',
      },
      {
        type: 'readonly',
        prop: 'authCredentials',
        label: '凭据 / 密钥',
        formatter: (v: string) => (v ? '已配置' : '-'),
        hidden: (m: Record<string, any>) => m.accessMethod !== 'api_pull',
      },
      {
        type: 'readonly',
        prop: 'qpsLimit',
        label: 'QPS 限制',
        formatter: (v: number) => String(v ?? '-'),
        hidden: (m: Record<string, any>) => m.accessMethod !== 'api_pull',
      },
      {
        type: 'readonly',
        prop: 'timeout',
        label: '超时（秒）',
        formatter: (v: number) => String(v ?? '-'),
        hidden: (m: Record<string, any>) => m.accessMethod !== 'api_pull',
      },
      {
        type: 'readonly',
        prop: 'sslVerify',
        label: 'SSL 验证',
        formatter: (v: boolean) => (v ? '是' : '否'),
        hidden: (m: Record<string, any>) => m.accessMethod !== 'api_pull',
      },
    ],
  },
  {
    title: '三、负责人与标签',
    cols: 2,
    fields: [
      {
        type: 'readonly',
        prop: 'businessOwner',
        label: '业务负责人',
        formatter: (v: string) => v || '-',
      },
      {
        type: 'readonly',
        prop: 'techOwner',
        label: '技术负责人',
        formatter: (v: string) => v || '-',
      },
      {
        type: 'readonly',
        prop: 'ownerDept',
        label: '所属部门',
        formatter: (v: string) => v || '-',
      },
    ],
  },
]

// 系统状态
const formStatus = reactive<Record<string, any>>({})

const statusSections: FormSection[] = [
  {
    cols: 2,
    fields: [
      {
        type: 'readonly',
        prop: 'status',
        label: '状态',
        formatter: (v: string) => STATUS_LABELS[v as keyof typeof STATUS_LABELS] ?? v,
      },
      {
        type: 'readonly',
        prop: 'lastSyncAt',
        label: '最近接入时间',
        formatter: (v: string) => v || '未接入',
      },
      {
        type: 'readonly',
        prop: 'taskCount',
        label: '关联任务数',
        formatter: (v: number) => String(v ?? 0),
      },
      {
        type: 'readonly',
        prop: 'createdAt',
        label: '创建时间',
      },
      {
        type: 'readonly',
        prop: 'updatedAt',
        label: '更新时间',
      },
    ],
  },
]

// 操作记录（后续版本替换为真实审计日志）
const mockLogs = [
  '2026-06-29 09:30 · 接入任务执行成功 · SAP 销售订单同步',
  '2026-06-28 18:00 · 编辑数据源配置 · 更新技术负责人',
  '2026-01-15 10:30 · 创建数据源 · 由管理员创建',
]

async function loadRelatedTasks() {
  loadingTasks.value = true
  try {
    const result = await ingestionService.getList({ dataSourceId: id, pageSize: 20 })
    relatedTasks.value = (result.items ?? []) as IngestionTask[]
  } catch {
    relatedTasks.value = []
  } finally {
    loadingTasks.value = false
  }
}

onMounted(async () => {
  try {
    const ds: DataSource = await dataSourceService.get(id)
    source.value = ds
    formReadonly.name = ds.name ?? ''
    formReadonly.code = ds.code ?? ''
    formReadonly.sourceType = ds.sourceType ?? ''
    formReadonly.accessMethod = ds.accessMethod ?? ''
    formReadonly.description = ds.description ?? ''
    formReadonly.businessOwner = ds.businessOwner ?? ''
    formReadonly.techOwner = ds.techOwner ?? ''
    formReadonly.ownerDept = ds.ownerDept ?? ''

    // 回填连接配置（详情只读展示）
    const cc = ds.connectionConfig
    if (cc) {
      formReadonly.baseUrl = cc.baseUrl ?? ''
      formReadonly.authType = cc.authType ?? ''
      formReadonly.authHeaderName = cc.authHeaderName ?? ''
      formReadonly.authCredentials = cc.authCredentials ?? ''
      formReadonly.qpsLimit = cc.qpsLimit
      formReadonly.timeout = cc.timeout
      formReadonly.sslVerify = cc.sslVerify
    }

    formStatus.status = ds.status
    formStatus.lastSyncAt = ds.lastSyncAt
    formStatus.taskCount = ds.taskCount
    formStatus.createdAt = ds.createdAt ?? ''
    formStatus.updatedAt = ds.updatedAt ?? ''
    // 异步加载关联任务列表
    loadRelatedTasks()
  } finally {
    loading.value = false
  }
})

async function handlePause() {
  await ElMessageBox.confirm(
    `确定停用数据源「${source.value?.name}」？停用后关联的接入任务将不再执行。`,
    '确认停用',
  )
  await dataSourceService.pause(id)
  ElMessage.success('已停用')
  // reload
  const ds: DataSource = await dataSourceService.get(id)
  source.value = ds
}

async function handleResume() {
  await dataSourceService.resume(id)
  ElMessage.success('已启用')
  const ds: DataSource = await dataSourceService.get(id)
  source.value = ds
}

async function handleTestConnection() {
  const fileMethods = ['file_upload', 'excel_import', 'share_scan'] as const
  if (fileMethods.includes(source.value?.accessMethod as never)) {
    ElMessage.info('文件导入方式无需检测连接')
    return
  }
  try {
    const result = await dataSourceService.testConnection(id)
    if (result?.connectionStatus === 'healthy') {
      ElMessage.success(`连接正常${result?.detail ? `（${result.detail}）` : ''}`)
    } else {
      ElMessage.warning(`连接异常${result?.detail ? `：${result.detail}` : ''}`)
    }
    // 刷新数据源以更新连接状态展示
    source.value = await dataSourceService.get(id)
  } catch {
    /* 错误已由拦截器处理 */
  }
}
</script>

<style lang="scss" scoped>
.loading-wrap {
  padding: 40px;
}

.summary-row {
  margin: 0 0 20px;
}

.summary-card {
  padding: 16px;
  background: #f9fafb;
  border: 1px solid #e5e7eb;
  border-radius: 8px;
}

.summary-label {
  font-size: 13px;
  color: #6b7280;
  margin-bottom: 4px;
}

.summary-value {
  font-size: 14px;
  color: #1f2937;
  font-weight: 500;
}

.tab-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 16px;
}

h3 {
  font-size: 16px;
  margin: 0 0 16px;
}

.link-list {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.link-item {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 12px;
  border: 1px solid #e5e7eb;
  border-radius: 8px;
  text-decoration: none;
  color: inherit;

  &:hover {
    background: #f9fafb;
  }
}

.link-item-left {
  display: flex;
  align-items: center;
  gap: 12px;
}

.link-item-sub {
  font-size: 13px;
  color: #6b7280;
}

.text-success {
  color: #16a34a;
}

.text-warning {
  color: #ca8a04;
}

.log-list {
  display: flex;
  flex-direction: column;
}

.log-item {
  padding: 10px 12px;
  border-left: 2px solid #e5e7eb;
  font-size: 14px;
  color: #374151;

  &.highlight {
    border-left-color: #2563eb;
    background: #eff6ff;
  }
}
</style>
