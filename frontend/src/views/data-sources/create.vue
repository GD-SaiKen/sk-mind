<template>
  <div class="page-layout detail-page">
    <PageHeader
      title="新增数据源"
      :breadcrumb="[{ label: '首页', to: '/' }, { label: '数据源', to: '/data-sources' }, { label: '新增数据源' }]"
    />
    <el-card shadow="never">
      <el-empty description="新增数据源向导功能开发中" />
    </el-card>
  </div>
</template>

<script setup lang="ts">
import PageHeader from '@/components/page-header.vue'
</script>

<style lang="scss" scoped>
</style>
