<template>
  <div class="page-layout detail-page">
    <Index
      :title="tableName"
      :breadcrumb="[{ label: '首页', to: '/' }, { label: '数据表', to: '/tables' }, { label: tableName }]"
    />
    <el-tabs v-model="activeTab">
      <el-tab-pane label="样例数据" name="sample"><el-card shadow="never"><el-empty description="样例数据功能开发中" /></el-card></el-tab-pane>
      <el-tab-pane label="字段列表" name="fields"><el-card shadow="never"><el-empty description="字段列表功能开发中" /></el-card></el-tab-pane>
      <el-tab-pane label="来源和批次" name="source"><el-card shadow="never"><el-empty description="来源和批次功能开发中" /></el-card></el-tab-pane>
      <el-tab-pane label="质量结果" name="quality"><el-card shadow="never"><el-empty description="质量结果功能开发中" /></el-card></el-tab-pane>
      <el-tab-pane label="权限" name="permission"><el-card shadow="never"><el-empty description="权限功能开发中" /></el-card></el-tab-pane>
      <el-tab-pane label="语义映射" name="mapping"><el-card shadow="never"><el-empty description="语义映射功能开发中" /></el-card></el-tab-pane>
      <el-tab-pane label="使用记录" name="usage"><el-card shadow="never"><el-empty description="使用记录功能开发中" /></el-card></el-tab-pane>
    </el-tabs>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { useRoute } from 'vue-router'
import Index from '@/components/page-header/index.vue'

const route = useRoute()
const activeTab = ref('fields')
const tableName = ref(route.params.id as string || '—')
</script>

<style lang="scss" scoped>
</style>
