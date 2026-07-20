<template>
  <div class="page-layout detail-page">
    <Index
      :title="`字段: ${fieldName}`"
      :breadcrumb="[{ label: '首页', to: '/' }, { label: '数据表', to: '/tables' }, { label: tableName, to: `/tables/${tableId}` }, { label: fieldName }]"
    />
    <el-card shadow="never">
      <el-empty description="字段详情功能开发中" />
    </el-card>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { useRoute } from 'vue-router'
import Index from '@/components/page-header/index.vue'

const route = useRoute()
const tableId = route.params.tableId as string || ''
const tableName = String(route.query.table || '—')
const fieldName = route.params.fieldName as string || '—'
</script>

<style lang="scss" scoped>
</style>
