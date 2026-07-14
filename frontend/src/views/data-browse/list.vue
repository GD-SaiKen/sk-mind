<template>
  <div class="page">
    <div class="title-row">
      <h1>鏁版嵁娴忚� <span class="count">({{ tables.length }} 寮犺〃)</span></h1>
    </div>

    <!-- 绛涢€夊尯 -->
    <TableFilters :items="filterItems" v-model:filter-values="filterValues" />

    <el-row :gutter="16">
      <el-col :span="7">
        <div class="table-list">
          <div
            v-for="t in filteredTables" :key="t.table_name" class="table-row"
            :class="{ active: activeTable === t.table_name }"
            @click="loadSample(t.table_name)"
          >
            <div class="tname">{{ t.table_name }}</div>
            <div class="tinfo">{{ t.row_count?.toLocaleString() }} 琛?/div>
          </div>
          <div v-if="filteredTables.length === 0 && !filterValues.keyword" class="empty">鏆傛棤鏁版嵁</div>
        </div>
      </el-col>

      <el-col :span="17">
        <div class="preview-panel">
          <template v-if="!activeTable">
            <div class="empty">鈫?鐐瑰嚮宸︿晶琛ㄥ悕鏌ョ湅鏁版嵁</div>
          </template>
          <template v-else>
            <div class="preview-header">
              <span class="preview-title">{{ activeTable }}</span>
              <el-tag type="info">Raw 灞?/el-tag>
            </div>
            <el-table
              v-if="sampleData.length > 0"
              v-loading="sampleLoading"
              :data="pagedSample"
              stripe
             
              max-height="560"
            >
              <el-table-column
                v-for="(_, key) in sampleData[0]"
                :key="key"
                :prop="String(key)"
                :label="String(key)"
                min-width="130"
                show-overflow-tooltip
              />
            </el-table>
            <div v-else class="empty">鏆傛棤鏁版嵁</div>
            <!-- 鍒嗛〉 -->
            <Pagination v-if="sampleData.length > 0" :config="samplePagination" />
          </template>
        </div>
      </el-col>
    </el-row>
  </div>
</template>

<script setup lang="ts">
import { computed, reactive, ref, watch } from 'vue'
import { Search } from '@element-plus/icons-vue'
import { api } from '@/api'
import { TableFilters, Pagination } from '@/components/crud'

import type { FilterItem } from '@/components/crud'

interface RawTable {
  table_name: string
  row_count: number
}

const tables = ref<RawTable[]>([])
const loading = ref(false)
const activeTable = ref('')
const sampleData = ref<Record<string, unknown>[]>([])
const sampleLoading = ref(false)
const filterItems: FilterItem[] = [
  { key: 'keyword', placeholder: '鎼滅储琛ㄥ悕...', width: '280px' },
]
const filterValues = ref<Record<string, any>>({})
const searchKey = ref('')

const filteredTables = computed(() => {
  if (!filterValues.value.keyword) return tables.value
  return tables.value.filter(t => t.table_name.includes(filterValues.value.keyword || ''))
})

// ---- 鎶芥牱鏁版嵁鍒嗛〉 ----
const samplePagination = reactive({
  page: 1,
  pageSize: 20,
  total: 0,
  onPageChange: () => {},
  onSizeChange: () => {},
})

const pagedSample = computed(() => {
  const start = (samplePagination.page - 1) * samplePagination.pageSize
  return sampleData.value.slice(start, start + samplePagination.pageSize)
})

watch(sampleData, (v) => {
  samplePagination.total = v.length
  samplePagination.page = 1
})

async function loadTables() {
  loading.value = true
  try {
    const res = await api.get('/data-browse/tables', {
      params: { schema: 'raw', system: 'mes_light' },
    })
    const data: RawTable[] = res.data.data ?? []
    tables.value = data.sort((a, b) => b.row_count - a.row_count)
  } finally {
    loading.value = false
  }
}

async function loadSample(tableName: string) {
  activeTable.value = tableName
  sampleLoading.value = true
  try {
    const res = await api.get('/data-browse/sample', {
      params: { table: tableName, limit: 20 },
    })
    sampleData.value = (res.data.data ?? []) as Record<string, unknown>[]
  } finally {
    sampleLoading.value = false
  }
}

loadTables()
</script>

<style lang="scss" scoped>
.page { }

.title-row {
  display: flex;
  align-items: center;
  margin-bottom: 12px;
  h1 { margin: 0; font-size: $font-size-lg; color: $color-text-primary; }
}

.count {
  font-size: $font-size-sm;
  color: $color-text-placeholder;
  font-weight: 400;
}

.table-list {
  overflow: hidden;
  overflow-y: auto;
  max-height: 640px;
  border: 1px solid $color-border;
  border-radius: $radius-base;
  background: $color-bg-white;
}

.table-row {
  padding: 10px 16px;
  cursor: pointer;
  border-bottom: 1px solid $color-border-light;
  transition: background 0.15s;
  &:hover { background: $color-bg; }
  &.active {
    border-left: 3px solid $color-primary;
    background: #eff6ff;
  }
}

.tname {
  font-size: $font-size-sm;
  font-family: $font-family-mono;
  color: $color-text-primary;
}

.tinfo {
  font-size: $font-size-xs;
  color: $color-text-secondary;
  margin-top: 2px;
}

.preview-panel {
  min-height: 400px;
  border: 1px solid $color-border;
  border-radius: $radius-base;
  background: $color-bg-white;
}

.preview-header {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 12px 16px;
  border-bottom: 1px solid $color-border;
}

.preview-title {
  font-size: 14px;
  font-weight: 600;
  font-family: 'Consolas', monospace;
}

.empty {
  text-align: center;
  padding: 80px 20px;
  color: $color-text-placeholder;
  font-size: 14px;
}
</style>
