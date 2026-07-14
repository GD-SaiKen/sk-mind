<!--
  ingestion-task/list.vue — 接入任务列表
-->
<template>
  <div class="page">
    <div class="toolbar">
      <el-input
        v-model="search"
        placeholder="搜索任务名称..."
        :prefix-icon="'Search'"
        style="width:260px"
        clearable
        @change="loadTasks"
      />
      <el-select
        v-model="statusFilter"
        placeholder="状态"
        clearable
        style="width:110px"
        @change="loadTasks"
      >
        <el-option label="全部" value="" />
        <el-option label="正常" value="active" />
        <el-option label="草稿" value="draft" />
        <el-option label="停用" value="paused" />
      </el-select>
      <el-button
        :icon="DataAnalysis"
        @click="router.push('/data-browse')"
      >
        Raw 数据浏览
      </el-button>
      <div class="spacer" />
      <el-button type="primary" :icon="Plus">创建任务</el-button>
    </div>

    <div class="stat-grid">
      <div
        v-for="card in statCards"
        :key="card.label"
        class="stat-card"
      >
        <div class="sc-top">
          <div :class="['sc-icon', card.iconBg]">
            <el-icon :size="16"><component :is="card.icon" /></el-icon>
          </div>
          <span class="sc-label">{{ card.label }}</span>
          <el-tag
            v-if="card.badge"
            size="small"
            :type="card.badgeType"
            effect="plain"
          >
            {{ card.badge }}
          </el-tag>
        </div>
        <div :class="['sc-value', card.color]">{{ card.value }}</div>
        <div class="sc-foot">{{ card.footer }}</div>
      </div>
    </div>

    <el-table
      v-loading="loading"
      :data="tasks"
      stripe
    >
      <el-table-column
        prop="name"
        label="任务名称"
        min-width="180"
      >
        <template #default="{ row }">
          <el-link
            type="primary"
            :underline="false"
            @click="router.push(`/ingestion/${row.id}`)"
          >
            {{ row.name }}
          </el-link>
        </template>
      </el-table-column>
      <el-table-column
        prop="code"
        label="编码"
        width="150"
      />
      <el-table-column
        prop="scheduleType"
        label="调度"
        width="80"
      />
      <el-table-column
        label="最近同步"
        width="170"
      >
        <template #default="{ row }">
          <span v-if="row.lastSyncAt" :style="{ color: syncFreshColor(row.lastSyncAt) }">
            {{ row.lastSyncAt.slice(0, 16).replace('T', ' ') }}
          </span>
          <span v-else class="never-sync">未同步过</span>
        </template>
      </el-table-column>
      <el-table-column
        prop="syncMode"
        label="模式"
        width="70"
      >
        <template #default="{ row }">
          <el-tag size="small" :type="row.syncMode === 'incremental' ? '' : 'info'" effect="plain">
            {{ row.syncMode === 'incremental' ? '增量' : '全量' }}
          </el-tag>
        </template>
      </el-table-column>
      <el-table-column
        prop="status"
        label="状态"
        width="90"
      >
        <template #default="{ row }">
          <el-tag
            :type="statusMap[row.status]?.type ?? 'info'"
            size="small"
            effect="plain"
          >
            {{ statusMap[row.status]?.text ?? row.status }}
          </el-tag>
        </template>
      </el-table-column>
      <el-table-column
        prop="createdAt"
        label="创建时间"
        width="170"
      />
      <el-table-column
        label="操作"
        width="280"
        fixed="right"
      >
        <template #default="{ row }">
          <template v-if="running[row.id]">
            <div class="inline-progress">
              <span class="ip-step">{{ running[row.id].step }}</span>
              <div class="ip-row">
                <el-progress
                  :percentage="running[row.id].pct >= 0 ? running[row.id].pct : 0"
                  :indeterminate="running[row.id].pct < 0"
                  :stroke-width="6"
                  :show-text="false"
                  style="width:100px"
                />
                <el-button
                  size="small"
                  type="danger"
                  text
                  @click="handleCancel(row.id, running[row.id].batchId)"
                >
                  停止
                </el-button>
              </div>
            </div>
          </template>
          <template v-else>
            <el-button size="small" @click="router.push(`/ingestion/${row.id}`)">
              详情
            </el-button>
            <el-button
              size="small"
              type="success"
              :icon="VideoPlay"
              @click="handleExecute(row)"
            >
              执行
            </el-button>
            <el-button
              v-if="row.status !== 'disabled'"
              size="small"
              text
              type="danger"
              @click="handleDelete(row)"
            >
              停用
            </el-button>
          </template>
        </template>
      </el-table-column>
    </el-table>

    <div
      v-if="tasks.length === 0 && !loading"
      class="empty"
    >
      暂无任务，请先创建
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed, onMounted, onUnmounted, reactive, ref } from 'vue';
import { useRouter } from 'vue-router';

import {
  CircleCheck,
  CircleCloseFilled,
  Clock,
  Collection,
  DataAnalysis,
  Plus,
  VideoPlay,
  WarningFilled,
} from '@element-plus/icons-vue';
import { ElMessage, ElMessageBox } from 'element-plus';

import { ingestionService, type IngestionTask } from '@/api';

const router = useRouter();
const tasks = ref<IngestionTask[]>([]);
const loading = ref(false);
const total = ref(0);
const search = ref('');
const statusFilter = ref('');
const running = reactive<Record<string, { pct: number; step: string; batchId: string }>>({});
let _pollEss: EventSource[] = [];

const statusMap: Record<string, { text: string; type: '' | 'success' | 'warning' | 'danger' | 'info' }> = {
  draft: { text: '草稿', type: 'info' },
  active: { text: '正常', type: 'success' },
  paused: { text: '停用', type: 'warning' },
  disabled: { text: '已禁用', type: 'danger' },
};

const statCards = computed(() => {
  const activeTasks = tasks.value.filter(t => t.status === 'active');
  const staleTasks = activeTasks.filter(t => {
    if (!t.lastSyncAt) return true;
    return Date.now() - new Date(t.lastSyncAt).getTime() > 24 * 3600000;
  });
  const lastSync = activeTasks
    .map(t => t.lastSyncAt)
    .filter(Boolean)
    .sort()
    .pop();

  return [
    {
      label: '活跃任务',
      value: activeTasks.length,
      icon: Collection,
      iconBg: 'sc-icon-blue',
      footer: lastSync ? `最近同步: ${lastSync.slice(0, 16).replace('T', ' ')}` : '暂无同步记录',
    },
    {
      label: '数据新鲜',
      value: activeTasks.length - staleTasks.length,
      icon: CircleCheck,
      iconBg: 'sc-icon-green',
      color: 'green' as const,
      footer: '24h 内有同步',
    },
    {
      label: '数据过期',
      value: staleTasks.length,
      icon: WarningFilled,
      iconBg: 'sc-icon-yellow',
      color: 'yellow' as const,
      footer: '超过 24h 未更新',
    },
    {
      label: '停用',
      value: tasks.value.filter(t => t.status === 'paused' || t.status === 'disabled').length,
      icon: CircleCloseFilled,
      iconBg: 'sc-icon-red',
      color: 'red' as const,
      footer: '已停用的任务',
    },
  ];
});

async function loadTasks() {
  loading.value = true;
  try {
    const res = await ingestionService.getList({
      keyword: search.value || undefined,
      status: statusFilter.value || undefined,
      pageSize: 20,
    });
    tasks.value = res.items;
    total.value = res.total;
  } finally {
    loading.value = false;
  }
}

async function handleExecute(task: IngestionTask) {
  try {
    const { batchId } = await ingestionService.execute(task.id);
    ElMessage.success('已提交');
    startPoll(task.id, batchId);
  } catch { /* handled */ }
}

function startPoll(taskId: string, batchId: string) {
  running[taskId] = { pct: -1, step: '等待 Worker...', batchId };
  const es = ingestionService.streamProgress(
    batchId,
    (d) => { running[taskId] = { pct: d.pct, step: d.step, batchId }; },
    () => {
      setTimeout(() => delete running[taskId], 3000);
      loadTasks();
    },
  );
  _pollEss.push(es);
}

async function handleCancel(taskId: string, batchId: string) {
  try {
    await ingestionService.cancelBatch(batchId);
    ElMessage.success('取消信号已发送');
  } catch { /* handled */ }
}

async function handleDelete(task: IngestionTask) {
  await ElMessageBox.confirm('确定停用该任务？', '确认');
  await ingestionService.delete(task.id);
  ElMessage.success('已停用');
  await loadTasks();
}

onMounted(loadTasks);
onUnmounted(() => _pollEss.forEach(es => es.close()));
function syncFreshColor(lastSyncAt: string | null): string {
  if (!lastSyncAt) return '#909399'
  const ms = Date.now() - new Date(lastSyncAt).getTime()
  const hours = ms / 3600000
  if (hours < 6) return '#67c23a'
  if (hours < 24) return '#e6a23c'
  return '#f56c6c'
}
</script>

<style lang="scss" scoped>
.page {
}

.toolbar {
  display: flex;
  gap: 10px;
  align-items: center;
  margin-bottom: 16px;
}

.spacer {
  flex: 1;
}

.stat-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 16px;
  margin-bottom: 16px;
}

.stat-card {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  height: 160px;
  padding: 20px;
  border: 1px solid $color-border-light;
  border-radius: $radius-base;
  background: $color-bg-white;
}

.sc-top {
  display: flex;
  align-items: center;
  gap: 8px;
}

.sc-icon {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 32px;
  height: 32px;
  border-radius: $radius-base;

  &-blue {
    background: #dbeafe;
    color: $color-primary;
  }

  &-green {
    background: #dcfce7;
    color: $color-success;
  }

  &-yellow {
    background: #fef9c3;
    color: $color-warning;
  }

  &-red {
    background: #fee2e2;
    color: $color-danger;
  }
}

.sc-label {
  font-size: $font-size-base;
  color: $color-text-secondary;
  flex: 1;
}

.sc-value {
  font-size: $font-size-3xl;
  font-weight: $font-weight-bold;
  color: $color-text-primary;
  margin: 6px 0 2px;

  &.green {
    color: $color-success;
  }

  &.yellow {
    color: $color-warning;
  }

  &.red {
    color: $color-danger;
  }
}

.sc-foot {
  font-size: $font-size-xs;
  color: $color-text-placeholder;
}

.empty {
  text-align: center;
  padding: 80px;
  color: $color-text-placeholder;
  font-size: $font-size-base;
}

.inline-progress {
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.ip-step {
  font-size: 11px;
  color: $color-primary;
}

.ip-row {
  display: flex;
  align-items: center;
  gap: 6px;
}

.never-sync {
  color: $color-text-placeholder;
  font-size: $font-size-xs;
}
</style>
