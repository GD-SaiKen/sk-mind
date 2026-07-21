<template>
  <div class="tab-nav">
    <button
      v-for="tab in tabs"
      :key="tab.key"
      class="tab-btn"
      :class="{ active: modelValue === tab.key }"
      @click="emit('update:modelValue', tab.key)"
    >
      {{ tab.label }}
      <span v-if="tab.count !== undefined" class="tab-count">{{ tab.count }}</span>
    </button>
    <div class="tab-nav-spacer" />
    <slot name="actions" />
  </div>
</template>

<script setup lang="ts">
export interface TabItem {
  key: string
  label: string
  count?: number
}

defineProps<{
  tabs: TabItem[]
  modelValue: string
}>()

const emit = defineEmits<{
  'update:modelValue': [value: string]
}>()
</script>

<style lang="scss" scoped>
.tab-nav {
  display: flex; align-items: center;
  border-bottom: 1px solid $color-border;
}
.tab-btn {
  padding: 10px 16px; border: none; background: none;
  font-size: $font-size-base; color: $color-text-secondary;
  cursor: pointer; border-bottom: 2px solid transparent;
  transition: color 0.15s;
  &:hover { color: $color-text-primary; }
  &.active { color: $color-primary; border-bottom-color: $color-primary; font-weight: $font-weight-medium; }
}
.tab-count { font-size: $font-size-xs; color: $color-text-placeholder; margin-left: 4px; }
.tab-nav-spacer { flex: 1; }
</style>
