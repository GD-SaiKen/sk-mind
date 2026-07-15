<template>
  <div class="page-layout detail-page">
    <PageHeader
      title="批次详情"
      :breadcrumb="[{ label: '首页', to: '/' }, { label: '接入任务', to: '/ingestion' }, { label: taskName, to: `/ingestion/${taskId}` }, { label: '批次详情' }]"
    />
    <el-tabs v-model="activeTab">
      <el-tab-pane label="批次概要" name="summary"><el-card shadow="never"><el-empty description="批次概要功能开发中" /></el-card></el-tab-pane>
      <el-tab-pane label="错误清单" name="errors"><el-card shadow="never"><el-empty description="错误清单功能开发中" /></el-card></el-tab-pane>
      <el-tab-pane label="产出数据表" name="tables"><el-card shadow="never"><el-empty description="产出数据表功能开发中" /></el-card></el-tab-pane>
      <el-tab-pane label="日志" name="logs"><el-card shadow="never"><el-empty description="日志功能开发中" /></el-card></el-tab-pane>
    </el-tabs>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { useRoute } from 'vue-router'
import PageHeader from '@/components/page-header.vue'

const route = useRoute()
const activeTab = ref('summary')
const taskId = route.params.taskId as string || ''
const taskName = String(route.query.task || '—')
</script>

<style lang="scss" scoped>
</style>
