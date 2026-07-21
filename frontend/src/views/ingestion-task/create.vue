<template>
  <div class="page-layout detail-page">
    <PageHeader
      title="创建接入任务"
      :breadcrumb="[
        { label: '首页', to: '/' },
        { label: '接入任务', to: '/ingestion' },
        { label: '创建任务' },
      ]"
    />

    <el-card shadow="never">
      <el-form
        ref="formRef"
        :model="form"
        :rules="rules"
        label-width="110px"
        style="max-width: 800px"
      >
        <el-divider content-position="left">基本信息</el-divider>

        <el-form-item label="数据源" prop="dataSourceId">
          <el-select
            v-model="form.dataSourceId"
            filterable
            placeholder="选择数据源"
            style="width: 100%"
            @change="onDataSourceChange"
          >
            <el-option
              v-for="ds in dataSources"
              :key="ds.id"
              :label="`${ds.name} (${ds.code})`"
              :value="ds.id"
            />
          </el-select>
        </el-form-item>

        <el-form-item label="任务名称" prop="name">
          <el-input v-model="form.name" placeholder="如：MES 安灯报表同步" maxlength="200" />
        </el-form-item>

        <el-form-item label="任务编码" prop="code">
          <el-input v-model="form.code" placeholder="唯一标识，如 mes_andon_sync" maxlength="100" />
        </el-form-item>

        <el-form-item label="同步模式" prop="syncMode">
          <el-radio-group v-model="form.syncMode">
            <el-radio value="full">全量同步</el-radio>
            <el-radio value="incremental">增量同步</el-radio>
          </el-radio-group>
        </el-form-item>

        <el-form-item label="调度方式" prop="scheduleType">
          <el-radio-group v-model="form.scheduleType">
            <el-radio value="manual">手动触发</el-radio>
            <el-radio value="cron">定时调度</el-radio>
          </el-radio-group>
        </el-form-item>

        <el-form-item
          v-if="form.scheduleType === 'cron'"
          label="Cron 表达式"
          prop="cronExpression"
        >
          <el-input v-model="form.cronExpression" placeholder="0 3 * * * (每天凌晨3点)" />
        </el-form-item>

        <el-divider content-position="left">
          接口勾选
          <span v-if="interfaces.length" style="font-weight: normal; font-size: 13px; color: #909399; margin-left: 8px">
            (已选 {{ selectedCount }} / {{ interfaces.length }})
          </span>
        </el-divider>

        <el-form-item v-if="!form.dataSourceId">
          <el-text type="info">请先选择数据源，然后加载可用接口</el-text>
        </el-form-item>
        <el-form-item v-else-if="loadingInterfaces">
          <el-icon class="is-loading"><Loading /></el-icon>
          <el-text type="info" style="margin-left: 8px">正在加载接口列表…</el-text>
        </el-form-item>
        <el-form-item v-else-if="interfaces.length === 0">
          <el-text type="warning">该数据源下没有可用的 API 接口</el-text>
        </el-form-item>
        <el-form-item v-else>
          <div style="width: 100%">
            <div style="margin-bottom: 8px">
              <el-button size="small" @click="selectAll">全选</el-button>
              <el-button size="small" @click="deselectAll">取消全选</el-button>
              <el-tag size="small" type="info" style="margin-left: 8px">
                已选择 {{ selectedCount }} 个接口
              </el-tag>
            </div>
            <el-checkbox-group v-model="form.selectedInterfaces" style="width: 100%">
              <div
                v-for="item in interfaces"
                :key="item.name"
                style="display: flex; align-items: flex-start; padding: 8px 0; border-bottom: 1px solid #f0f0f0"
              >
                <el-checkbox :value="item.name" style="margin-right: 12px; margin-top: 2px" />
                <div style="flex: 1">
                  <div style="font-weight: 500">{{ item.name }}</div>
                  <div style="font-size: 12px; color: #909399; margin-top: 2px">
                    <el-tag size="small" :type="item.isTimeBased ? 'success' : 'info'" style="margin-right: 6px">
                      {{ item.isTimeBased ? '时间驱动' : '非时间' }}
                    </el-tag>
                    {{ item.method }} {{ item.endpoint }}
                  </div>
                  <div style="font-size: 12px; color: #c0c4cc; margin-top: 1px">
                    → {{ item.targetTable }}
                  </div>
                </div>
              </div>
            </el-checkbox-group>
          </div>
        </el-form-item>

        <el-divider content-position="left">备注</el-divider>
        <el-form-item label="备注" prop="description">
          <el-input
            v-model="form.description"
            type="textarea"
            :rows="2"
            placeholder="为什么创建这个任务、有什么注意事项"
          />
        </el-form-item>
      </el-form>

      <div class="form-footer">
        <el-button @click="router.back()">取消</el-button>
        <el-button
          type="primary"
          :loading="submitting"
          :disabled="selectedCount === 0"
          @click="handleSubmit"
        >
          创建任务并执行
        </el-button>
      </div>
    </el-card>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, onMounted } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { ElMessage } from 'element-plus'
import { Loading } from '@element-plus/icons-vue'
import PageHeader from '@/components/page-header/index.vue'
import { dataSourceService, ingestionService } from '@/api'
import type { DataSource, ApiInterfaceItem } from '@/api'

const router = useRouter()
const route = useRoute()
const formRef = ref()
const submitting = ref(false)
const loadingInterfaces = ref(false)

const dataSources = ref<DataSource[]>([])
const interfaces = ref<ApiInterfaceItem[]>([])

const form = ref({
  dataSourceId: (route.query.sourceId as string) || '',
  name: '',
  code: '',
  syncMode: 'full',
  scheduleType: 'manual',
  cronExpression: '',
  description: '',
  selectedInterfaces: [] as string[],
})

const rules = {
  dataSourceId: [{ required: true, message: '请选择数据源', trigger: 'change' }],
  name: [{ required: true, message: '请输入任务名称', trigger: 'blur' }],
  code: [{ required: true, message: '请输入任务编码', trigger: 'blur' }],
}

const selectedCount = computed(() => form.value.selectedInterfaces.length)

function selectAll() {
  form.value.selectedInterfaces = interfaces.value.map(i => i.name)
}

function deselectAll() {
  form.value.selectedInterfaces = []
}

async function onDataSourceChange(dsId: string) {
  form.value.selectedInterfaces = []
  if (!dsId) return
  loadingInterfaces.value = true
  try {
    interfaces.value = await dataSourceService.getInterfaces(dsId)
  } catch {
    interfaces.value = []
    ElMessage.warning('接口列表加载失败')
  } finally {
    loadingInterfaces.value = false
  }
}

async function handleSubmit() {
  const valid = await formRef.value?.validate().catch(() => false)
  if (!valid) return

  submitting.value = true
  try {
    const task = await ingestionService.createApiTask(
      form.value.name,
      form.value.code,
      form.value.dataSourceId,
      form.value.selectedInterfaces,
      form.value.syncMode,
      form.value.scheduleType,
      form.value.description,
    )
    ElMessage.success(`任务创建成功: ${task.name || task.code}`)

    // Immediately execute
    try {
      const execResult = await ingestionService.execute(task.id)
      ElMessage.success(`同步已启动 (batch: ${execResult.batchId?.slice(0, 8)}…)`)
    } catch {
      ElMessage.warning('任务已创建但执行启动失败，请手动执行')
    }

    router.push(`/ingestion?sourceId=${form.value.dataSourceId}`)
  } catch (e: unknown) {
    const msg = (e as { response?: { data?: { detail?: string } } })?.response?.data?.detail || '创建失败'
    ElMessage.error(msg)
  } finally {
    submitting.value = false
  }
}

onMounted(async () => {
  try {
    const result = await dataSourceService.getList({ page: 1, pageSize: 100 })
    dataSources.value = result.items || []
  } catch {
    // ignore
  }

  // If sourceId is pre-selected via query param, auto-load interfaces
  if (form.value.dataSourceId) {
    onDataSourceChange(form.value.dataSourceId)
  }
})
</script>

<style lang="scss" scoped>
.form-footer {
  display: flex;
  justify-content: flex-end;
  gap: 8px;
  margin-top: 24px;
  padding-top: 16px;
  border-top: 1px solid #ebeef5;
}
</style>
