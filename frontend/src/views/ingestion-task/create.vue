<template>
  <div class="page-layout detail-page">
    <PageHeader
      :title="isEdit ? '编辑接入任务' : '创建接入任务'"
      :breadcrumb="[
        { label: '首页', to: '/' },
        { label: '接入任务', to: '/ingestion' },
        { label: isEdit ? '编辑任务' : '创建任务' },
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
            :disabled="isEdit"
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

        <el-form-item label="调度方式" prop="scheduleType">
          <el-radio-group v-model="form.scheduleType" @change="onScheduleTypeChange">
            <el-radio value="manual">手动触发</el-radio>
            <el-radio value="cron">定时调度</el-radio>
          </el-radio-group>
        </el-form-item>

        <template v-if="form.scheduleType === 'cron'">
          <el-form-item label="预设频率" prop="cronPreset">
            <el-select
              v-model="cronPreset"
              placeholder="选择常用频率"
              style="width: 240px"
              @change="onPresetChange"
            >
              <el-option
                v-for="p in cronPresets"
                :key="p.value"
                :label="p.label"
                :value="p.value"
              />
            </el-select>
          </el-form-item>

          <el-form-item
            v-if="cronPreset === '__custom__'"
            label="Cron 表达式"
            prop="cronExpression"
          >
            <el-input
              v-model="form.cronExpression"
              placeholder="0 3 * * * (每天凌晨3点)"
              style="max-width: 320px"
              @input="refreshCronPreview"
            />
          </el-form-item>

          <el-form-item label="下次执行">
            <div v-if="cronPreview.loading" class="cron-preview-line">
              <el-icon class="is-loading"><Loading /></el-icon>
              <span class="cron-preview-text">计算中…</span>
            </div>
            <el-tag v-else-if="cronPreview.nextRun" type="primary" effect="plain">
              <el-icon style="margin-right: 4px; vertical-align: middle"><Clock /></el-icon>
              {{ fmtDateTime(cronPreview.nextRun, true) }}
            </el-tag>
            <el-text v-else-if="cronPreview.error" type="danger" size="small">
              {{ cronPreview.error }}
            </el-text>
            <el-text v-else type="info" size="small">填写 Cron 后自动计算</el-text>
          </el-form-item>

          <el-form-item label="回放窗口" prop="replayWindowDays">
            <el-input-number v-model="form.replayWindowDays" :min="1" :max="30" :step="1" />
            <span class="form-tip">天 · 增量同步从水位往前回放 N 天，默认 3</span>
          </el-form-item>
        </template>

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
                <div style="display: flex; flex-direction: column; align-items: flex-end; margin-left: 12px">
                  <el-tooltip
                    :content="item.pkFields && item.pkFields.length ? '定期检测 API 中已删除的记录' : '需配置 PK 字段后方可开启'"
                    placement="top"
                  >
                    <el-switch
                      :model-value="!!detectOptions[item.name]"
                      :disabled="!(item.pkFields && item.pkFields.length)"
                      @change="onDetectToggle(item.name, $event as boolean)"
                      inline-prompt
                      active-text="软删"
                      inactive-text="软删"
                    />
                  </el-tooltip>
                  <span
                    v-if="!(item.pkFields && item.pkFields.length)"
                    style="font-size: 11px; color: #c0c4cc; margin-top: 2px"
                  >需 PK 字段</span>
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
          {{ isEdit ? '保存修改' : '创建任务并执行' }}
        </el-button>
      </div>
    </el-card>
  </div>
</template>

<script setup lang="ts">
import { ref, reactive, computed, onMounted, watch } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { ElMessage } from 'element-plus'
import { Clock, Loading } from '@element-plus/icons-vue'
import PageHeader from '@/components/page-header/index.vue'
import { dataSourceService, ingestionService } from '@/api'
import type { DataSource, ApiInterfaceItem, IngestionTask } from '@/api'
import { fmtDateTime } from '@/utils/datetime'

/** 常用 Cron 预设（6/7 字段 Quartz 会在后端 _normalize_cron 归一为 5 字段标准 cron） */
const cronPresets = [
  { label: '每天凌晨 3 点', value: '0 3 * * *' },
  { label: '每小时整点', value: '0 * * * *' },
  { label: '每 6 小时', value: '0 */6 * * *' },
  { label: '每 12 小时', value: '0 */12 * * *' },
  { label: '每 30 分钟', value: '*/30 * * * *' },
  { label: '每 15 分钟', value: '*/15 * * * *' },
  { label: '每周一凌晨 4 点', value: '0 4 * * 1' },
  { label: '自定义…', value: '__custom__' },
]
const CUSTOM_PRESET = '__custom__'

const router = useRouter()
const route = useRoute()
const formRef = ref()
const submitting = ref(false)
const loadingInterfaces = ref(false)
const loadingTask = ref(false)

const isEdit = computed(() => !!route.params.id)
const editTaskId = computed(() => route.params.id as string)

const dataSources = ref<DataSource[]>([])
const selectedDataSourceCode = ref('')
const interfaces = ref<ApiInterfaceItem[]>([])

/** 每个接口的软删除检测开关（仅在 PK 接口上可用），提交时随 config 传后端 */
const detectOptions = ref<Record<string, boolean>>({})

const form = ref({
  dataSourceId: (route.query.sourceId as string) || '',
  name: '',
  code: '',
  syncMode: 'full',
  scheduleType: 'manual',
  cronExpression: '',
  cronPreset: '0 3 * * *',
  replayWindowDays: 3,
  description: '',
  selectedInterfaces: [] as string[],
})

/** 当前选中的 Cron 预设（与 form.cronExpression 联动） */
const cronPreset = ref('0 3 * * *')

/** Cron 预览状态（下次执行时间） */
const cronPreview = reactive<{
  loading: boolean
  nextRun: string | null
  description: string
  error: string
}>({
  loading: false,
  nextRun: null,
  description: '',
  error: '',
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

/** 切换某接口的软删除检测开关（F3.1） */
function onDetectToggle(name: string, val: boolean) {
  if (val) {
    detectOptions.value[name] = true
  } else {
    delete detectOptions.value[name]
  }
}

/** 仅收集已选中接口中开启软删除检测的条目，提交给后端 */
function buildSoftDeleteMap(): Record<string, boolean> {
  const map: Record<string, boolean> = {}
  for (const name of form.value.selectedInterfaces) {
    if (detectOptions.value[name]) map[name] = true
  }
  return map
}

function onScheduleTypeChange(val: string) {
  if (val === 'cron') {
    // 初次切到定时：若 cronExpression 为空则套用当前预设
    if (!form.value.cronExpression && cronPreset.value !== CUSTOM_PRESET) {
      form.value.cronExpression = cronPreset.value
    }
    refreshCronPreview()
  } else {
    cronPreview.nextRun = null
    cronPreview.error = ''
    cronPreview.description = ''
  }
}

function onPresetChange(val: string) {
  if (val !== CUSTOM_PRESET) {
    form.value.cronExpression = val
  }
  refreshCronPreview()
}

let _previewTimer: ReturnType<typeof setTimeout> | undefined
function refreshCronPreview() {
  if (form.value.scheduleType !== 'cron' || !form.value.cronExpression) {
    cronPreview.nextRun = null
    cronPreview.error = ''
    cronPreview.description = ''
    return
  }
  cronPreview.loading = true
  cronPreview.error = ''
  if (_previewTimer) clearTimeout(_previewTimer)
  _previewTimer = setTimeout(async () => {
    try {
      const res = await ingestionService.previewCron(form.value.cronExpression)
      if (res?.isValid) {
        cronPreview.nextRun = res.nextRun || null
        cronPreview.description = res.description || ''
        cronPreview.error = ''
      } else {
        cronPreview.nextRun = null
        cronPreview.error = 'Cron 表达式无效'
      }
    } catch {
      cronPreview.nextRun = null
      cronPreview.error = '预览请求失败'
    } finally {
      cronPreview.loading = false
    }
  }, 400)
}

async function onDataSourceChange(dsId: string) {
  if (!isEdit.value) form.value.selectedInterfaces = []
  if (!dsId) return
  // 记录选中数据源的 code，用于拼接 configPath
  const ds = dataSources.value.find(d => d.id === dsId)
  selectedDataSourceCode.value = ds?.code ?? ''
  loadingInterfaces.value = true
  try {
    interfaces.value = await dataSourceService.getInterfaces(dsId)
    // In edit mode, re-apply pre-selected interfaces after loading
    if (isEdit.value) {
      form.value.selectedInterfaces = form.value.selectedInterfaces.filter(
        name => interfaces.value.some(i => i.name === name)
      )
    }
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

  // 定时调度必须带有效 Cron 表达式
  if (form.value.scheduleType === 'cron' && !form.value.cronExpression) {
    ElMessage.error('请选择或输入 Cron 表达式')
    return
  }

  submitting.value = true
  try {
    if (isEdit.value) {
      // Edit mode: update existing task
      const data: Record<string, unknown> = {
        name: form.value.name,
        syncMode: form.value.syncMode,
        scheduleType: form.value.scheduleType,
        cronExpression: form.value.scheduleType === 'cron' ? form.value.cronExpression || undefined : undefined,
        description: form.value.description || undefined,
        config: {
          accessMethod: 'api',
          configPath: `config/data_sources/${selectedDataSourceCode.value}.yaml`,
          interfaces: form.value.selectedInterfaces,
          replayWindowDays: form.value.replayWindowDays,
          softDelete: buildSoftDeleteMap(),
        },
      }
      await ingestionService.update(editTaskId.value, data)
      ElMessage.success('任务已更新')
      router.push(`/ingestion/${editTaskId.value}`)
    } else {
      // Create mode
      const task = await ingestionService.createApiTask(
        form.value.name,
        form.value.code,
        form.value.dataSourceId,
        form.value.selectedInterfaces,
        selectedDataSourceCode.value,
        form.value.syncMode,
        form.value.scheduleType,
        form.value.scheduleType === 'cron' ? form.value.cronExpression : '',
        form.value.description,
        form.value.replayWindowDays,
        buildSoftDeleteMap(),
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
    }
  } catch (e: unknown) {
    const msg = (e as { response?: { data?: { detail?: string } } })?.response?.data?.detail || (isEdit.value ? '更新失败' : '创建失败')
    ElMessage.error(msg)
  } finally {
    submitting.value = false
  }
}

async function loadEditTask() {
  if (!isEdit.value) return
  loadingTask.value = true
  try {
    const task: IngestionTask = await ingestionService.get(editTaskId.value)

    // Pre-fill form
    form.value.dataSourceId = task.dataSourceId
    form.value.name = task.name
    form.value.code = task.code
    form.value.syncMode = task.syncMode
    form.value.scheduleType = task.scheduleType
    form.value.cronExpression = task.cronExpression || ''
    form.value.description = task.description || ''

    // 选中预设（若现有 cronExpression 命中某个预设则高亮它，否则归为自定义）
    const matched = cronPresets.find(p => p.value === task.cronExpression)
    cronPreset.value = matched ? matched.value : CUSTOM_PRESET
    form.value.cronPreset = cronPreset.value
    form.value.replayWindowDays = (task.config as any)?.replayWindowDays ?? 3

    // Pre-select interfaces from task config
    const configInterfaces = (task.config as any)?.interfaces || []
    form.value.selectedInterfaces = configInterfaces

    // 回显软删除检测开关（F3.1）
    detectOptions.value = (task.config as any)?.softDelete || {}

    // Load the data source code and interfaces
    const ds = dataSources.value.find(d => d.id === task.dataSourceId)
    if (ds) {
      selectedDataSourceCode.value = ds.code
      loadingInterfaces.value = true
      try {
        interfaces.value = await dataSourceService.getInterfaces(task.dataSourceId)
      } catch { /* ignore */ }
      loadingInterfaces.value = false
    }

    // 计算定时调度的下次执行预览
    if (form.value.scheduleType === 'cron' && form.value.cronExpression) {
      refreshCronPreview()
    }
  } catch {
    ElMessage.error('加载任务信息失败')
    router.push('/ingestion')
  } finally {
    loadingTask.value = false
  }
}

onMounted(async () => {
  // Load data sources
  try {
    const result = await dataSourceService.getList({ page: 1, pageSize: 100 })
    dataSources.value = result.items || []
  } catch {
    // ignore
  }

  if (isEdit.value) {
    // Edit mode: load task data, then populate form
    await loadEditTask()
  } else if (form.value.dataSourceId) {
    // Create mode with pre-selected source
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

.cron-preview-line {
  display: flex;
  align-items: center;
  gap: 6px;
  color: #909399;
  font-size: 13px;
}

.cron-preview-text {
  font-size: 13px;
}

.form-tip {
  margin-left: 10px;
  font-size: 12px;
  color: #909399;
}
</style>
