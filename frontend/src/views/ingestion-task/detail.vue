<!--
  ingestion-task/detail.vue — 接入任务详情
-->
<template>
  <div class="page" v-if="task">
    <div class="title-row">
      <h1>{{ task.name }}</h1>
      <el-tag
        type="success"
        size="small"
        effect="plain"
      >正常</el-tag>
      <el-tag
        type="info"
        size="small"
        effect="plain"
      >{{ task.code }}</el-tag>
      <div class="spacer" />
      <el-button
        type="primary"
        :icon="VideoPlay"
        :loading="executing"
        size="small"
        @click="handleExecute"
      >
        立即执行
      </el-button>
      <el-button :icon="Refresh" size="small">
        重试
      </el-button>
      <el-button size="small">编辑</el-button>
    </div>

    <div class="summary-row">
      <div
        v-for="s in summary"
        :key="s.label"
        class="sum-item"
      >
        <span class="sum-label">{{ s.label }}</span>
        <span class="sum-val">{{ s.value }}</span>
      </div>
    </div>

    <el-tabs v-model="activeTab">
      <el-tab-pane label="当前配置" name="config">
        <el-descriptions
          :column="2"
          border
          size="small"
          style="max-width:600px"
        >
          <el-descriptions-item label="名称">{{ task.name }}</el-descriptions-item>
          <el-descriptions-item label="编码">{{ task.code }}</el-descriptions-item>
          <el-descriptions-item label="目标层">{{ task.targetLayer }}</el-descriptions-item>
          <el-descriptions-item label="调度类型">{{ task.scheduleType }}</el-descriptions-item>
          <el-descriptions-item label="状态">{{ task.status }}</el-descriptions-item>
          <el-descriptions-item label="创建时间">{{ task.createdAt }}</el-descriptions-item>
        </el-descriptions>
      </el-tab-pane>
      <el-tab-pane :label="`批次列表 (${batches.length})`" name="batches">
        <el-table
          :data="batches"
          stripe
          size="small"
        >
          <el-table-column label="批次ID" width="110">
            <template #default="{ row }">...{{ row.id?.slice(-8) }}</template>
          </el-table-column>
          <el-table-column
            prop="triggerType"
            label="触发方式"
            width="90"
          />
          <el-table-column prop="status" label="状态" width="100">
            <template #default="{ row }">
              <el-tag
                :type="batchType[row.status]"
                size="small"
                effect="plain"
              >
                {{ batchLabel[row.status] ?? row.status }}
              </el-tag>
            </template>
          </el-table-column>
          <el-table-column
            prop="recordCount"
            label="总行数"
            width="90"
          />
          <el-table-column
            prop="successCount"
            label="成功"
            width="80"
          />
          <el-table-column label="失败" width="80">
            <template #default="{ row }">
              <span :style="{ color: row.failCount > 0 ? '#ef4444' : '' }">
                {{ row.failCount }}
              </span>
            </template>
          </el-table-column>
          <el-table-column
            prop="createdAt"
            label="时间"
            min-width="160"
          />
          <el-table-column label="操作" width="140">
            <template #default="{ row }">
              <el-button
                size="small"
                text
                @click="loadErrors(row.id)"
              >
                错误
              </el-button>
              <el-button
                v-if="row.status === 'failed'"
                size="small"
                text
                type="warning"
                :icon="Refresh"
                @click="handleRetry(row.id)"
              >
                重试
              </el-button>
            </template>
          </el-table-column>
        </el-table>
      </el-tab-pane>
      <el-tab-pane :label="`错误清单 (${errors.length})`" name="errors">
        <div
          v-if="errors.length === 0"
          class="empty"
        >
          暂无错误
        </div>
        <div
          v-for="err in errors"
          :key="err.id"
          class="err-row"
        >
          <el-tag
            type="danger"
            size="small"
            effect="plain"
          >{{ err.errorType }}</el-tag>
          <span>{{ err.errorMessage }}</span>
          <span class="err-time">{{ err.createdAt?.slice(0, 19) }}</span>
        </div>
      </el-tab-pane>
      <el-tab-pane label="执行日志" name="log">
        <div class="empty">暂无日志</div>
      </el-tab-pane>
    </el-tabs>
  </div>
</template>

<script setup lang="ts">
import { computed, onMounted, ref } from 'vue';
import { useRoute } from 'vue-router';

import { Refresh, VideoPlay } from '@element-plus/icons-vue';
import { ElMessage } from 'element-plus';

import {
  ingestionService,
  type IngestionBatch,
  type ImportError,
  type IngestionTask,
} from '@/api';

const route = useRoute();
const taskId = route.params.id as string;
const task = ref<IngestionTask | null>(null);
const batches = ref<IngestionBatch[]>([]);
const errors = ref<ImportError[]>([]);
const activeTab = ref('batches');
const executing = ref(false);

const batchLabel: Record<string, string> = {
  pending: '等待中',
  running: '运行中',
  success: '成功',
  partial_success: '部分成功',
  failed: '失败',
};
const batchType: Record<string, '' | 'success' | 'warning' | 'danger' | 'info'> = {
  pending: 'info',
  running: '',
  success: 'success',
  partial_success: 'warning',
  failed: 'danger',
};

const summary = computed(() => [
  { label: '调度', value: task.value?.scheduleType ?? '-' },
  { label: '目标层', value: task.value?.targetLayer ?? '-' },
  { label: '创建时间', value: task.value?.createdAt?.slice(0, 10) ?? '-' },
  { label: '最近状态', value: batches.value[0]?.status ?? '-' },
  { label: '总行数', value: (batches.value[0]?.recordCount ?? 0).toLocaleString() },
]);

async function load() {
  task.value = await ingestionService.get(taskId);
  const b = await ingestionService.getBatches(taskId, { pageSize: 20 });
  batches.value = b.items;
}

async function handleExecute() {
  executing.value = true;
  try {
    await ingestionService.execute(taskId);
    ElMessage.success('已提交');
    await load();
  } finally {
    executing.value = false;
  }
}

async function handleRetry(bid: string) {
  await ingestionService.retryBatch(bid);
  ElMessage.success('重试已提交');
  await load();
}

async function loadErrors(bid: string) {
  const e = await ingestionService.getBatchErrors(bid, { pageSize: 50 });
  errors.value = e.items;
  activeTab.value = 'errors';
}

onMounted(load);
</script>

<style lang="scss" scoped>
.page {
}

.title-row {
  display: flex;
  align-items: center;
  gap: 10px;
  margin-bottom: 16px;

  h1 {
    margin: 0;
    font-size: $font-size-xl;
    font-weight: $font-weight-semibold;
    color: $color-text-primary;
  }
}

.spacer {
  flex: 1;
}

.summary-row {
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  gap: 12px;
  margin-bottom: 16px;
}

.sum-item {
  display: flex;
  flex-direction: column;
  gap: 4px;
  padding: 14px 16px;
  border: 1px solid $color-border-light;
  border-radius: 6px;
}

.sum-label {
  font-size: $font-size-xs;
  color: $color-text-placeholder;
}

.sum-val {
  font-size: $font-size-lg;
  font-weight: $font-weight-semibold;
  color: $color-text-primary;
}

.empty {
  text-align: center;
  padding: 60px;
  color: $color-text-placeholder;
  font-size: $font-size-base;
}

.err-row {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 8px 10px;
  border-bottom: 1px solid $color-border-light;
  font-size: $font-size-sm;
}

.err-time {
  margin-left: auto;
  color: $color-text-placeholder;
  font-size: $font-size-xs;
}
</style>
