<template>
  <div class="detail-page">
    <div class="breadcrumb">
      <router-link to="/data-tables" class="bread-link">数据表</router-link>
      <span class="bread-sep">/</span>
      <span class="bread-current">{{ tableName }}</span>
    </div>
    <div class="title-row"><h1>{{ tableName }}</h1></div>
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

const route = useRoute()
const activeTab = ref('fields')
const tableName = ref(route.params.id as string || '—')
</script>

<style lang="scss" scoped>
.detail-page { display: flex; flex-direction: column; gap: 16px; }
.breadcrumb { display: flex; align-items: center; gap: 6px; font-size: $font-size-sm; }
.bread-link { color: $color-text-placeholder; text-decoration: none; &:hover { color: $color-text-secondary; } }
.bread-sep { color: $color-border; }
.bread-current { color: $color-text-secondary; }
.title-row h1 { font-size: $font-size-xl; }
</style>
