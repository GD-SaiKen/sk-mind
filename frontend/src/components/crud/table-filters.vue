<template>
  <div class="table-filters" v-if="items.length || $slots.default">
    <template v-for="item in items" :key="item.key">
      <el-input
        v-if="!item.type || item.type === 'input'"
        :model-value="filterValues[item.key]"
        :placeholder="item.placeholder"
        :clearable="item.clearable ?? true"
        :style="{ width: item.width || '160px' }"
        @update:model-value="onChange(item.key, $event)"
      />
      <el-select
        v-else-if="item.type === 'select'"
        :model-value="filterValues[item.key]"
        :placeholder="item.placeholder"
        :clearable="item.clearable ?? true"
        :style="{ width: item.width || '140px' }"
        @update:model-value="onChange(item.key, $event)"
      >
        <el-option
          v-for="opt in item.options"
          :key="opt.value"
          :label="opt.label"
          :value="opt.value"
        />
      </el-select>
    </template>
    <slot />
  </div>
</template>

<script setup lang="ts">
import type { FilterItem } from './types'

withDefaults(defineProps<{
  items?: FilterItem[]
}>(), {
  items: () => [],
})

const filterValues = defineModel<Record<string, any>>('filterValues', { default: () => ({}) })

const emit = defineEmits<{
  change: [key: string, value: any]
}>()

function onChange(key: string, val: any) {
  filterValues.value = { ...filterValues.value, [key]: val }
  emit('change', key, val)
}
</script>

<style scoped>
.table-filters {
  display: flex;
  align-items: center;
  gap: 12px;
  flex-wrap: wrap;
}
</style>
