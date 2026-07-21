<template>
  <el-card shadow="never" class="stat-card">
    <div class="sc-header">
      <div class="sc-icon" :class="iconBg">
        <el-icon :size="16"><component :is="icon" /></el-icon>
      </div>
      <span class="sc-label">{{ label }}</span>
      <span v-if="subtag" :class="['sc-subtag', subtagClass]">{{ subtag }}</span>
    </div>
    <div class="sc-value-row">
      <span class="sc-value" :class="valueClass">{{ value }}</span>
      <span v-if="badge" :class="['sc-badge', badgeClass]">{{ badge }}</span>
    </div>
    <div class="sc-foot" v-if="footerText || $slots.footer">
      <slot name="footer">
        <div v-if="showBar" class="sc-bar"><div class="sc-bar-fill" :style="{ width: barPercent + '%' }" /></div>
        <span>{{ footerText }}</span>
        <span v-if="afterText">{{ afterText }}</span>
      </slot>
    </div>
  </el-card>
</template>

<script setup lang="ts">
import type { Component } from 'vue'

withDefaults(defineProps<{
  icon: Component
  iconBg: string
  label: string
  subtag?: string
  subtagClass?: string
  value: string | number
  valueClass?: string
  badge?: string
  badgeClass?: string
  footerText?: string
  showBar?: boolean
  barPercent?: number
  afterText?: string
}>(), {
  subtagClass: '',
  valueClass: '',
  badgeClass: '',
  showBar: false,
  barPercent: 0,
})
</script>

<style lang="scss" scoped>
.stat-card {
  :deep(.el-card__body) { display: flex; flex-direction: column; gap: 8px; padding: 20px; }
}

.sc-header { display: flex; align-items: center; gap: 6px; }
.sc-icon {
  display: flex; align-items: center; justify-content: center;
  width: 32px; height: 32px; border-radius: $radius-base; flex-shrink: 0;
}
.sc-label { font-size: $font-size-base; color: $color-text-secondary; }
.sc-subtag {
  font-size: $font-size-xs; padding: 1px 6px; border-radius: 4px;
  margin-left: auto; white-space: nowrap;
  background: #f3f4f6; color: $color-text-placeholder;
}
.sc-value-row { display: flex; align-items: baseline; gap: 8px; }
.sc-value { font-size: 28px; font-weight: $font-weight-bold; color: $color-text-primary; white-space: nowrap; }
.sc-badge { font-size: $font-size-xs; padding: 1px 6px; border-radius: 4px; }
.sc-foot { display: flex; align-items: center; gap: 6px; font-size: $font-size-xs; color: $color-text-placeholder; }
.sc-bar { flex: 1; height: 4px; background: #f3f4f6; border-radius: 2px; overflow: hidden; }
.sc-bar-fill { height: 100%; background: $color-success; border-radius: 2px; transition: width 0.3s; }
</style>
