<template>
  <div class="table-header">
    <span class="table-header-title" v-if="title">
      {{ title }}
    </span>
    <div class="table-header-actions" v-if="$slots.default">
      <slot />
    </div>
  </div>
</template>

<script setup lang="ts">
defineProps<{
  title?: string
}>()
</script>

<style scoped>
.table-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  min-height: 32px;
}

.table-header-title {
  font-size: 15px;
  font-weight: 600;
  color: #303133;
  white-space: nowrap;
}

.table-header-actions {
  display: flex;
  align-items: center;
  gap: 8px;
}
</style>
