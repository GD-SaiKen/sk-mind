<template>
  <div class="page-layout detail-page">
    <Index
      title="数据集质量详情"
      :breadcrumb="[{ label: '首页', to: '/' }, { label: '数据质量', to: '/quality' }, { label: '质量详情' }]"
    />
    <el-card shadow="never">
      <el-empty description="数据集质量详情功能开发中" />
    </el-card>
  </div>
</template>

<script setup lang="ts">
import Index from '@/components/page-header/index.vue'
</script>

<style lang="scss" scoped>
</style>
