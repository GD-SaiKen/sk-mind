<template>
  <div class="page-header">
    <!-- 面包屑 -->
    <div class="ph-breadcrumb" v-if="breadcrumb.length">
      <template v-for="(item, idx) in breadcrumb" :key="idx">
        <router-link
          v-if="item.to"
          :to="item.to"
          class="ph-bread-link"
        >{{ item.label }}</router-link>
        <span v-else class="ph-bread-current">{{ item.label }}</span>
        <span v-if="idx < breadcrumb.length - 1" class="ph-bread-sep">/</span>
      </template>
    </div>

    <!-- 标题行 -->
    <div class="ph-title-row">
      <div class="ph-title-left">
        <h1 class="ph-title">{{ title }}</h1>
        <slot name="tags" />
      </div>
      <div class="ph-actions" v-if="$slots.actions">
        <slot name="actions" />
      </div>
    </div>

    <!-- 描述 -->
    <p class="ph-desc" v-if="description || $slots.description">
      <slot name="description">{{ description }}</slot>
    </p>
  </div>
</template>

<script setup lang="ts">
export interface BreadcrumbItem {
  label: string
  to?: string
}

withDefaults(defineProps<{
  title: string
  breadcrumb?: BreadcrumbItem[]
  description?: string
}>(), {
  breadcrumb: () => [],
})
</script>

<style lang="scss" scoped>
.page-header {}

.ph-breadcrumb {
  display: flex;
  align-items: center;
  gap: 6px;
  font-size: $font-size-sm;
  margin-bottom: 8px;
}

.ph-bread-link {
  color: $color-text-placeholder;
  text-decoration: none;

  &:hover {
    color: $color-primary;
  }
}

.ph-bread-sep {
  color: $color-border;
}

.ph-bread-current {
  color: $color-text-secondary;
  font-weight: $font-weight-medium;
}

.ph-title-row {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
}

.ph-title-left {
  display: flex;
  align-items: center;
  gap: 8px;
  flex: 1;
}

.ph-title {
  font-size: $font-size-xl;
  font-weight: $font-weight-bold;
  color: $color-text-primary;
  margin: 0;
  line-height: 1.4;
}

.ph-actions {
  display: flex;
  align-items: center;
  gap: 8px;
  flex-shrink: 0;
}

.ph-desc {
  margin: 4px 0 0;
  font-size: $font-size-base;
  color: $color-text-secondary;
  line-height: 1.5;
}
</style>
