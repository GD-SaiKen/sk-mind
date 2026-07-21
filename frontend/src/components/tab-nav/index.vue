<template>
  <el-tabs
    v-model="currentTab"
    class="tab-nav"
  >
    <el-tab-pane
      v-for="tab in tabs"
      :key="tab.key"
      :label="tabLabel(tab)"
      :name="tab.key"
    />
  </el-tabs>
</template>

<script setup lang="ts">
import type { TabItem } from './types'
import { computed } from 'vue'

const props = defineProps<{
  modelValue: string
  tabs: TabItem[]
}>()

const emit = defineEmits<{
  'update:modelValue': [value: string]
}>()

const currentTab = computed({
  get: () => props.modelValue,
  set: (v: string) => emit('update:modelValue', v),
})

function tabLabel(tab: TabItem): string {
  if (tab.count !== undefined) return `${tab.label} (${tab.count})`
  return tab.label
}
</script>

<style lang="scss" scoped>
.tab-nav {
  margin-bottom: 16px;
}
</style>
