<template>
  <el-card class="crud-root">
    <!-- 筛选区（卡片 body 顶部） -->
    <div
      class="crud-filters"
      v-if="filterItems.length || $slots.filters || $slots['filters-actions']"
    >
      <TableFilters
        :items="filterItems"
        v-model:filter-values="filterValues"
        @change="(k: any, v: any) => emit('filterChange', k, v)"
      />
      <slot name="filters" />
      <div class="crud-filters-spacer" v-if="$slots['filters-actions']" />
      <slot name="filters-actions" />
    </div>

    <!-- 表格 -->
    <div class="crud-table">
      <slot name="table" />
    </div>

    <!-- 分页导航 -->
    <div class="crud-pagination" v-if="pagination">
      <el-pagination
        v-model:current-page="pagination.page"
        v-model:page-size="pagination.pageSize"
        :total="pagination.total"
        :layout="pagination.layout ?? 'total, sizes, prev, pager, next, jumper'"
        :page-sizes="pagination.pageSizes ?? [10, 20, 50, 100, 500, 1000]"
        background
        @current-change="pagination.onPageChange?.(pagination.page)"
        @size-change="pagination.onSizeChange?.(pagination.pageSize)"
      />
    </div>
  </el-card>
</template>

<script setup lang="ts">
import TableFilters from './table-filters.vue'
import type { FilterItem } from './types'

withDefaults(defineProps<{
  filterItems?: FilterItem[]
  pagination?: {
    page: number
    pageSize: number
    total: number
    layout?: string
    pageSizes?: number[]
    onPageChange?: (page: number) => void
    onSizeChange?: (size: number) => void
  }
}>(), {
  filterItems: () => [],
})

const filterValues = defineModel<Record<string, any>>('filterValues', { default: () => ({}) })

const emit = defineEmits<{
  filterChange: [key: string, value: any]
}>()
</script>

<style scoped>
/* 让卡片填满父容器，内部 flex 列布局 */
.crud-root {
  height: 100%;
  display: flex;
  flex-direction: column;
}

:deep(.el-card__body) {
  flex: 1;
  display: flex;
  flex-direction: column;
  overflow: hidden;
}

.crud-filters {
  display: flex;
  align-items: center;
  gap: 12px;
  flex-wrap: wrap;
  padding-bottom: 16px;
  margin-bottom: 16px;
  border-bottom: 1px solid #f0f0f0;
  flex-shrink: 0;
}

.crud-filters-spacer {
  flex: 1;
}

.crud-table {
  flex: 1;
  min-height: 0;
}

.crud-pagination {
  display: flex;
  justify-content: flex-start;
  padding-top: 16px;
  flex-shrink: 0;
}
</style>
