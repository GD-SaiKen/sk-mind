<template>
  <el-card>
    <!-- 1. 标题 + 筛选区（同行） -->
    <template #header>
      <div class="crud-top" v-if="title || $slots['title-extra'] || $slots.filters">
        <div class="crud-top-left">
          <span class="crud-title-text" v-if="title">{{ title }}</span>
          <slot name="title-extra" />
        </div>
        <div class="crud-top-right" v-if="$slots.filters">
          <slot name="filters" />
        </div>
      </div>
    </template>

    <!-- 2. 表头操作区 -->
    <div class="crud-actions" v-if="$slots.actions">
      <slot name="actions" />
    </div>

    <!-- 3. 表格 -->
    <div class="crud-table">
      <slot name="table" />
    </div>

    <!-- 4. 分页导航 -->
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
defineProps<{
  title?: string
  pagination?: {
    page: number
    pageSize: number
    total: number
    layout?: string
    pageSizes?: number[]
    onPageChange?: (page: number) => void
    onSizeChange?: (size: number) => void
  }
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

:deep(.el-card) {
  flex: 1;
  display: flex;
  flex-direction: column;
  overflow: hidden;
}

.crud-top {
  display: flex;
  align-items: center;
  gap: 16px;
  flex-wrap: wrap;
}

.crud-top-left {
  display: flex;
  align-items: center;
  gap: 8px;
  flex-shrink: 0;
}

.crud-top-right {
  display: flex;
  align-items: center;
  gap: 12px;
  flex: 1;
  flex-wrap: wrap;
  min-width: 0;
}

.crud-title-text {
  font-size: 15px;
  font-weight: 600;
  color: #303133;
  white-space: nowrap;
}

.crud-actions {
  display: flex;
  align-items: center;
  gap: 8px;
  padding-bottom: 12px;
  flex-shrink: 0;
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
