<template>
  <el-card
    shadow="hover"
    :class="['stat-card', { clickable }]"
    @click="clickable && $emit('click')"
  >
    <div class="sc-header">
      <div class="sc-title-wrap">
        <div
          v-if="icon"
          :class="['sc-icon', iconBg]"
        >
          <el-icon :size="16">
            <component :is="icon" />
          </el-icon>
        </div>
        <span class="sc-label">{{ label }}</span>
      </div>
      <span
        v-if="badge"
        :class="['sc-badge', badgeType]"
      >{{ badge }}</span>
    </div>

    <div
      :class="['sc-value', valueColor]"
      :style="valueStyle"
    >{{ value }}</div>

    <div
      v-if="footer || $slots.footer"
      class="sc-footer"
    >
      <slot name="footer">
        {{ footer }}
      </slot>
    </div>
  </el-card>
</template>

<script setup lang="ts">
import type { Component } from 'vue'
import { computed } from 'vue'

const props = withDefaults(defineProps<{
  icon?: Component
  iconBg?: string
  label: string
  value: string | number
  valueColor?: string
  badge?: string
  badgeType?: string
  footer?: string
  clickable?: boolean
}>(), {
  iconBg: 'bg-blue',
  badgeType: 'success',
  clickable: false,
})

defineEmits<{
  click: []
}>()

const valueStyle = computed(() => {
  if (props.valueColor) return { color: props.valueColor }
  return {}
})
</script>

<style lang="scss" scoped>
.stat-card {
  :deep(.el-card__body) {
    display: flex;
    flex-direction: column;
    gap: 8px;
    padding: 20px;
  }

  &.clickable {
    cursor: pointer;

    &:hover {
      border-color: $color-primary;
    }
  }
}

.sc-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.sc-title-wrap {
  display: flex;
  align-items: center;
  gap: 8px;
}

.sc-icon {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 32px;
  height: 32px;
  border-radius: 8px;

  &.bg-blue {
    background: #dbeafe;
    color: #2563eb;
  }

  &.bg-green {
    background: #dcfce7;
    color: #16a34a;
  }

  &.bg-yellow, &.bg-orange {
    background: #fef3c7;
    color: #ca8a04;
  }

  &.bg-red {
    background: #fee2e2;
    color: #dc2626;
  }

  &.bg-purple {
    background: #ede9fe;
    color: #7c3aed;
  }

  &.bg-indigo {
    background: #e0e7ff;
    color: #4f46e5;
  }

  &.bg-cyan {
    background: #cffafe;
    color: #0891b2;
  }

  &.bg-pink {
    background: #fce7f3;
    color: #db2777;
  }
}

.sc-label {
  font-size: 14px;
  font-weight: 500;
  color: #1f2937;
}

.sc-badge {
  font-size: 12px;
  padding: 2px 8px;
  border-radius: 12px;

  &.success {
    color: #16a34a;
    background: #f0fdf4;
    border: 1px solid #bbf7d0;
  }

  &.warning {
    color: #ca8a04;
    background: #fefce8;
    border: 1px solid #fef08a;
  }

  &.danger {
    color: #dc2626;
    background: #fef2f2;
    border: 1px solid #fecaca;
  }

  &.info {
    color: #2563eb;
    background: #eff6ff;
    border: 1px solid #bfdbfe;
  }
}

.sc-value {
  font-size: 28px;
  font-weight: 700;
  color: #1f2937;
}

.sc-footer {
  font-size: 12px;
  color: #9ca3af;
}
</style>
