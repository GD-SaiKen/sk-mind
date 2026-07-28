<template>
  <div class="page-layout" v-loading="loading">
    <Index
      :title="dataset?.name || '数据集详情'"
      :breadcrumb="[{ label: '首页', to: '/' }, { label: '数据目录', to: '/catalog' }, { label: dataset?.name || '详情' }]"
    />

    <!-- 摘要区 -->
    <el-descriptions v-if="dataset" :column="3" border style="margin-bottom: 16px">
      <el-descriptions-item label="数据集名称">{{ dataset.name }}</el-descriptions-item>
      <el-descriptions-item label="数据来源">{{ dataset.sourceName || '-' }}</el-descriptions-item>
      <el-descriptions-item label="业务域">
        <el-tag v-if="dataset.businessDomain" effect="plain">{{ dataset.businessDomain }}</el-tag>
        <span v-else>—</span>
      </el-descriptions-item>
      <el-descriptions-item label="数据分层">{{ dataset.dataLayer }}</el-descriptions-item>
      <el-descriptions-item label="记录数">{{ dataset.recordCount?.toLocaleString() || '0' }} 条</el-descriptions-item>
      <el-descriptions-item label="字段数">{{ dataset.fieldCount || 0 }}</el-descriptions-item>
      <el-descriptions-item label="质量状态">
        <el-tag :type="dataset.qualityStatus === 'ok' ? 'success' : dataset.qualityStatus === 'warning' ? 'warning' : 'danger'" effect="plain">
          {{ qualityLabel(dataset.qualityStatus) }}
        </el-tag>
      </el-descriptions-item>
      <el-descriptions-item label="Agent 可用">
        <el-tag :type="dataset.isAgentAccessible ? 'success' : 'info'" effect="plain">
          {{ dataset.isAgentAccessible ? '可用' : '未开放' }}
        </el-tag>
      </el-descriptions-item>
      <el-descriptions-item label="更新时间">{{ formatDate(dataset.updatedAt) }}</el-descriptions-item>
    </el-descriptions>

    <!-- Agent 限制 -->
    <el-alert
      v-if="dataset?.agentAccessibleReason"
      type="warning"
      :title="'Agent 使用限制：' + dataset.agentAccessibleReason"
      :closable="false"
      style="margin-bottom: 16px"
    />

    <!-- Tab -->
    <el-tabs v-model="activeTab" v-if="dataset">
      <el-tab-pane label="字段目录" name="fields">
        <el-table :data="dataset.fields" stripe>
          <el-table-column prop="fieldName" label="字段名" width="180" />
          <el-table-column prop="fieldAlias" label="显示名" width="150">
            <template #default="{ row }">{{ row.fieldAlias || '—' }}</template>
          </el-table-column>
          <el-table-column prop="description" label="字段含义" min-width="200">
            <template #default="{ row }">{{ row.description || '—' }}</template>
          </el-table-column>
          <el-table-column prop="dataType" label="类型" width="120" />
          <el-table-column label="主键" width="70" align="center">
            <template #default="{ row }">
              <el-tag v-if="row.isPrimaryKey" type="warning" effect="plain" size="small">PK</el-tag>
              <span v-else>—</span>
            </template>
          </el-table-column>
          <el-table-column label="敏感" width="100" align="center">
            <template #default="{ row }">
              <el-tag v-if="row.isSensitive" type="danger" effect="plain" size="small">{{ row.sensitivityLevel }}</el-tag>
              <span v-else>内部</span>
            </template>
          </el-table-column>
          <el-table-column label="空值率" width="100" align="center">
            <template #default="{ row }">
              <span :style="{ color: row.nullRate != null && row.nullRate > 0.1 ? '#dc2626' : row.nullRate != null && row.nullRate > 0.01 ? '#ca8a04' : '' }">
                {{ row.nullRate != null ? (row.nullRate * 100).toFixed(1) + '%' : '—' }}
              </span>
            </template>
          </el-table-column>
        </el-table>
      </el-tab-pane>

      <el-tab-pane v-if="dataset.sensitiveFields && dataset.sensitiveFields.length > 0" label="敏感字段" name="sensitive">
        <el-table :data="dataset.sensitiveFields" stripe>
          <el-table-column prop="fieldName" label="字段名" width="180" />
          <el-table-column prop="fieldAlias" label="显示名" width="150">
            <template #default="{ row }">{{ row.fieldAlias || '—' }}</template>
          </el-table-column>
          <el-table-column prop="description" label="字段含义" min-width="200">
            <template #default="{ row }">{{ row.description || '—' }}</template>
          </el-table-column>
          <el-table-column prop="dataType" label="类型" width="120" />
          <el-table-column label="敏感等级" width="120" align="center">
            <template #default="{ row }">
              <el-tag type="danger" effect="plain" size="small">{{ row.sensitivityLevel }}</el-tag>
            </template>
          </el-table-column>
        </el-table>
      </el-tab-pane>

      <el-tab-pane label="Agent 使用限制" name="agent">
        <div style="padding: 20px">
          <el-descriptions :column="1" border>
            <el-descriptions-item label="Agent 可用状态">
              <el-tag :type="dataset.isAgentAccessible ? 'success' : 'danger'">
                {{ dataset.isAgentAccessible ? '已开放' : '未开放' }}
              </el-tag>
            </el-descriptions-item>
            <el-descriptions-item label="限制原因">
              {{ dataset.agentAccessibleReason || '无限制' }}
            </el-descriptions-item>
            <el-descriptions-item label="字段说明覆盖率">
              {{ computeCoverage() }}%
            </el-descriptions-item>
            <el-descriptions-item label="敏感字段数">
              {{ dataset.sensitiveFields?.length || 0 }} 个
            </el-descriptions-item>
          </el-descriptions>
        </div>
      </el-tab-pane>
    </el-tabs>

    <!-- 返回 -->
    <div style="margin-top: 16px">
      <router-link to="/tables/">
        <el-button link type="primary">→ 查看技术详情（数据表模块）</el-button>
      </router-link>
    </div>
  </div>
</template>

<script setup lang="ts">
import { onMounted, ref } from 'vue'
import { useRoute } from 'vue-router'
import Index from '@/components/page-header/index.vue'
import { catalogService } from '@/api/services/catalog'
import type { CatalogDatasetDetail } from '@/api/types'

const route = useRoute()
const dataset = ref<CatalogDatasetDetail | null>(null)
const loading = ref(false)
const activeTab = ref('fields')

function qualityLabel(s: string | null) {
  const map: Record<string, string> = { ok: '正常', warning: '警告', error: '异常' }
  return map[s || ''] || '—'
}

function formatDate(s: string) {
  return s ? s.substring(0, 19).replace('T', ' ') : '—'
}

function computeCoverage() {
  if (!dataset.value) return 0
  const total = dataset.value.fields.length
  if (total === 0) return 0
  const withDesc = dataset.value.fields.filter(f => f.description).length
  return Math.round((withDesc / total) * 100)
}

onMounted(async () => {
  const id = route.params.id as string
  if (!id) return
  loading.value = true
  try {
    dataset.value = await catalogService.getDatasetDetail(id)
  } catch {
    dataset.value = null
  } finally {
    loading.value = false
  }
})
</script>
