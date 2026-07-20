<template>
  <div class="page-layout detail-page">
    <Index
      :title="datasetName"
      :breadcrumb="[{ label: '首页', to: '/' }, { label: '数据目录', to: '/catalog' }, { label: datasetName }]"
    />
    <el-tabs v-model="activeTab">
      <el-tab-pane label="数据集说明" name="desc"><el-card shadow="never"><el-empty description="数据集说明功能开发中" /></el-card></el-tab-pane>
      <el-tab-pane label="字段目录" name="fields"><el-card shadow="never"><el-empty description="字段目录功能开发中" /></el-card></el-tab-pane>
      <el-tab-pane label="来源和血缘" name="lineage"><el-card shadow="never"><el-empty description="来源和血缘功能开发中" /></el-card></el-tab-pane>
      <el-tab-pane label="质量状态" name="quality"><el-card shadow="never"><el-empty description="质量状态功能开发中" /></el-card></el-tab-pane>
      <el-tab-pane label="权限和敏感字段" name="permission"><el-card shadow="never"><el-empty description="权限功能开发中" /></el-card></el-tab-pane>
      <el-tab-pane label="Agent 使用限制" name="agent"><el-card shadow="never"><el-empty description="Agent 使用限制功能开发中" /></el-card></el-tab-pane>
      <el-tab-pane label="关联语义对象" name="semantic"><el-card shadow="never"><el-empty description="关联语义对象功能开发中" /></el-card></el-tab-pane>
    </el-tabs>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { useRoute } from 'vue-router'
import Index from '@/components/page-header/index.vue'

const route = useRoute()
const activeTab = ref('desc')
const datasetName = ref(route.params.id as string || '—')
</script>

<style lang="scss" scoped>
</style>
