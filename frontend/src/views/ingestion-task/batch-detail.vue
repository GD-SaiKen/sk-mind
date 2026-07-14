<template>
  <div class="detail-page">
    <div class="breadcrumb">
      <router-link to="/ingestion" class="bread-link">接入任务</router-link>
      <span class="bread-sep">/</span>
      <router-link :to="`/ingestion/${taskId}`" class="bread-link">{{ taskName }}</router-link>
      <span class="bread-sep">/</span>
      <span class="bread-current">批次详情</span>
    </div>
    <div class="title-row"><h1>批次详情</h1></div>
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

const route = useRoute()
const activeTab = ref('summary')
const taskId = route.params.taskId as string || ''
const taskName = route.query.task || '—'
</script>

<style lang="scss" scoped>
.detail-page { display: flex; flex-direction: column; gap: 16px; }
.breadcrumb { display: flex; align-items: center; gap: 6px; font-size: $font-size-sm; }
.bread-link { color: $color-text-placeholder; text-decoration: none; &:hover { color: $color-text-secondary; } }
.bread-sep { color: $color-border; }
.bread-current { color: $color-text-secondary; }
.title-row h1 { font-size: $font-size-xl; }
</style>
