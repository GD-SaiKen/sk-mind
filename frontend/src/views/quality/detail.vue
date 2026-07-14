<template>
  <div class="detail-page">
    <div class="breadcrumb">
      <router-link to="/quality" class="bread-link">数据质量</router-link>
      <span class="bread-sep">/</span>
      <span class="bread-current">质量详情</span>
    </div>
    <div class="title-row"><h1>数据集质量详情</h1></div>
    <el-card shadow="never">
      <el-empty description="数据集质量详情功能开发中" />
    </el-card>
  </div>
</template>

<script setup lang="ts">
</script>

<style lang="scss" scoped>
.detail-page { display: flex; flex-direction: column; gap: 16px; }
.breadcrumb { display: flex; align-items: center; gap: 6px; font-size: $font-size-sm; }
.bread-link { color: $color-text-placeholder; text-decoration: none; &:hover { color: $color-text-secondary; } }
.bread-sep { color: $color-border; }
.bread-current { color: $color-text-secondary; }
.title-row h1 { font-size: $font-size-xl; }
</style>
