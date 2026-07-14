<template>
  <div class="detail-page">
    <div class="breadcrumb">
      <router-link to="/" class="bread-link">首页</router-link>
      <span class="bread-sep">/</span>
      <router-link to="/data-tables" class="bread-link">数据表</router-link>
      <span class="bread-sep">/</span>
      <router-link :to="`/data-tables/${tableId}`" class="bread-link">{{ tableName }}</router-link>
      <span class="bread-sep">/</span>
      <span class="bread-current">{{ fieldName }}</span>
    </div>
    <div class="title-row"><h1>字段: {{ fieldName }}</h1></div>
    <el-card shadow="never">
      <el-empty description="字段详情功能开发中" />
    </el-card>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { useRoute } from 'vue-router'

const route = useRoute()
const tableId = route.params.tableId as string || ''
const tableName = route.query.table || '—'
const fieldName = route.params.fieldName as string || '—'
</script>

<style lang="scss" scoped>
.detail-page { display: flex; flex-direction: column; gap: 16px; }
.breadcrumb { display: flex; align-items: center; gap: 6px; font-size: $font-size-sm; }
.bread-link { color: $color-text-placeholder; text-decoration: none; &:hover { color: $color-text-secondary; } }
.bread-sep { color: $color-border; }
.bread-current { color: $color-text-secondary; }
.title-row h1 { font-size: $font-size-xl; }
</style>
