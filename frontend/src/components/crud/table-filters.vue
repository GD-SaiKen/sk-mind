<template>
  <div class="table-filters">
    <slot />
  </div>
</template>

<style scoped>
.table-filters {
  display: flex;
  align-items: center;
  gap: 12px;
  flex-wrap: wrap;
  padding-bottom: 12px;
}
</style>
