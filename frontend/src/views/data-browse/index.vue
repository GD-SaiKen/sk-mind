<!--
  data-browse/index.vue — Raw 层数据浏览：查看各系统表名和行数
-->
<template>
  <div class="page">
    <div class="title-row">
      <h1>Raw 层数据浏览</h1>
      <div class="spacer" />
      <el-button :icon="Refresh" size="small" @click="load">刷新</el-button>
    </div>

    <div class="toolbar">
      <el-select v-model="system" placeholder="选择系统" clearable style="width:160px" @change="load">
        <el-option label="全部系统" value="" />
        <el-option label="ERP (E10)" value="erp" />
        <el-option label="MES (LightMES)" value="mes" />
        <el-option label="SRM" value="srm" />
      </el-select>
      <span class="hint">仅显示 raw schema 下的物理表</span>
    </div>

    <div v-loading="loading">
      <el-table :data="tables" stripe size="small" empty-text="该 schema 下暂无数据表">
        <el-table-column prop="table_name" label="表名" min-width="260">
          <template #default="{ row }">
            <el-link type="primary" :underline="false" @click="browseSample(row.table_name)">
              {{ row.table_name }}
            </el-link>
          </template>
        </el-table-column>
        <el-table-column prop="row_count" label="行数" width="120" sortable>
          <template #default="{ row }">
            <span :style="{ fontWeight: 'bold', color: row.row_count > 0 ? '#67c23a' : '#909399' }">
              {{ row.row_count?.toLocaleString() ?? '-' }}
            </span>
          </template>
        </el-table-column>
      </el-table>

      <div v-if="tables.length > 0" class="summary-bar">
        共 {{ tables.length }} 张表 ·
        总行数 {{ totalRows.toLocaleString() }}
      </div>
    </div>

    <!-- 抽样弹窗 -->
    <el-dialog v-model="dialogVisible" :title="`抽样: ${sampleTable}`" width="900px" destroy-on-close>
      <div v-loading="sampleLoading">
        <el-table v-if="sampleRows.length > 0" :data="sampleRows" stripe size="small" max-height="400">
          <el-table-column type="index" label="#" width="50" />
          <el-table-column label="数据" min-width="300">
            <template #default="{ row }">
              <pre class="json-cell">{{ JSON.stringify(row, null, 2) }}</pre>
            </template>
          </el-table-column>
        </el-table>
        <div v-else-if="!sampleLoading" class="empty">暂无数据</div>
      </div>
    </el-dialog>
  </div>
</template>

<script setup lang="ts">
import { computed, ref } from 'vue';
import { Refresh } from '@element-plus/icons-vue';
import api from '@/api/client';

const loading = ref(false);
const system = ref('');
const tables = ref<{ table_name: string; row_count: number }[]>([]);

const totalRows = computed(() => tables.value.reduce((s, t) => s + (t.row_count || 0), 0));

// 抽样
const dialogVisible = ref(false);
const sampleTable = ref('');
const sampleRows = ref<Record<string, unknown>[]>([]);
const sampleLoading = ref(false);

async function load() {
  loading.value = true;
  try {
    const params: Record<string, string> = { schema: 'raw' };
    if (system.value) params.system = system.value;
    const r = await api.get('/data-browse/tables', { params });
    tables.value = r.data.data || [];
  } finally {
    loading.value = false;
  }
}

async function browseSample(tableName: string) {
  sampleTable.value = tableName;
  dialogVisible.value = true;
  sampleLoading.value = true;
  try {
    const r = await api.get('/data-browse/sample', { params: { table: tableName, limit: 20 } });
    sampleRows.value = r.data.data || [];
  } finally {
    sampleLoading.value = false;
  }
}

load();
</script>

<style lang="scss" scoped>
.page { }

.title-row {
  display: flex;
  align-items: center;
  gap: 10px;
  margin-bottom: 16px;
  h1 { margin: 0; font-size: $font-size-xl; font-weight: $font-weight-semibold; }
}

.spacer { flex: 1; }

.toolbar {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 16px;
}

.hint {
  color: $color-text-placeholder;
  font-size: $font-size-sm;
}

.summary-bar {
  margin-top: 10px;
  padding: 8px 0;
  color: $color-text-secondary;
  font-size: $font-size-sm;
}

.json-cell {
  margin: 0;
  font-size: 11px;
  line-height: 1.4;
  max-width: 600px;
  overflow-x: auto;
  white-space: pre-wrap;
  word-break: break-all;
}

.empty {
  text-align: center;
  padding: 60px;
  color: $color-text-placeholder;
}
</style>
