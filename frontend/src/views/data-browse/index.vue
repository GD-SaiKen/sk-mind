<template>
  <Index :pagination="indexPagination">
    <template #title-extra>
      <el-button :icon="Refresh" @click="load">刷新</el-button>
    </template>
    <template #filters>
      <el-select v-model="system" placeholder="选择系统" clearable style="width: 160px" @change="load">
        <el-option label="全部系统" value="" />
        <el-option label="ERP (E10)" value="erp" />
        <el-option label="MES (LightMES)" value="mes" />
        <el-option label="SRM" value="srm" />
      </el-select>
      <span class="hint">仅显示 raw schema 下的物理表</span>
    </template>
    <template #table>
      <Table :columns="columns" :data="tables" :loading="loading" empty-text="该 schema 下暂无数据表">
        <template #col-table_name="{ row }">
          <el-link type="primary" :underline="false" @click="browseSample(row.table_name)">
            {{ row.table_name }}
          </el-link>
        </template>
        <template #col-row_count="{ row }">
          <span :style="{ fontWeight: 'bold', color: row.row_count > 0 ? '#67c23a' : '#909399' }">
            {{ row.row_count?.toLocaleString() ?? '-' }}
          </span>
        </template>
      </Table>
    </template>
  </Index>

  <!-- 抽样弹窗 -->
  <el-dialog v-model="dialogVisible" :title="`抽样: ${sampleTable}`" width="900px" destroy-on-close>
    <div v-loading="sampleLoading">
      <el-table v-if="sampleRows.length > 0" :data="sampleRows" stripe max-height="400">
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
</template>

<script setup lang="ts">
import { computed, reactive, ref, watch } from 'vue'
import { Refresh } from '@element-plus/icons-vue'
import api from '@/api/client'
import { Index, Table } from '@/components/crud'
import type { ColumnSchema } from '@/components/crud'

const loading = ref(false)
const system = ref('')
const tables = ref<{ table_name: string; row_count: number }[]>([])

// 抽样
const dialogVisible = ref(false)
const sampleTable = ref('')
const sampleRows = ref<Record<string, unknown>[]>([])
const sampleLoading = ref(false)

// ---- 分页 ----
const indexPagination = reactive({ page: 1, pageSize: 20, total: 0, onPageChange() {}, onSizeChange() {} })
watch(tables, (v) => { indexPagination.total = v.length })

// ---- 列配置 ----
const columns: ColumnSchema[] = [
  { type: 'custom', prop: 'table_name', label: '表名', minWidth: 260 },
  { type: 'custom', prop: 'row_count', label: '行数', width: 120, sortable: true },
]

async function load() {
  loading.value = true
  try {
    const params: Record<string, string> = { schema: 'raw' }
    if (system.value) params.system = system.value
    const r = await api.get('/data-browse/tables', { params })
    tables.value = r.data.data || []
  } finally {
    loading.value = false
  }
}

async function browseSample(tableName: string) {
  sampleTable.value = tableName
  dialogVisible.value = true
  sampleLoading.value = true
  try {
    const r = await api.get('/data-browse/sample', { params: { table: tableName, limit: 20 } })
    sampleRows.value = r.data.data || []
  } finally {
    sampleLoading.value = false
  }
}

load()
</script>

<style lang="scss" scoped>
.hint {
  color: $color-text-placeholder;
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
