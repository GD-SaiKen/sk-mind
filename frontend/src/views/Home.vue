<script setup lang="ts">
import { ref, onMounted } from 'vue'
import api from '@/api/client'

const healthStatus = ref<string>('检查中...')
const appVersion = ref<string>('')

async function checkHealth() {
  try {
    const res = await api.get('/api/health')
    healthStatus.value = '运行正常'
    appVersion.value = res.data.version ?? ''
  } catch {
    healthStatus.value = '连接失败'
  }
}

onMounted(() => {
  checkHealth()
})
</script>

<template>
  <div class="home-page">
    <h2>平台概览</h2>

    <el-row :gutter="20" class="stat-row">
      <el-col :span="6">
        <el-card shadow="hover">
          <el-statistic title="数据源" :value="0" />
        </el-card>
      </el-col>
      <el-col :span="6">
        <el-card shadow="hover">
          <el-statistic title="接入任务" :value="0" />
        </el-card>
      </el-col>
      <el-col :span="6">
        <el-card shadow="hover">
          <el-statistic title="数据集" :value="0" />
        </el-card>
      </el-col>
      <el-col :span="6">
        <el-card shadow="hover">
          <el-statistic title="质量问题" :value="0" />
        </el-card>
      </el-col>
    </el-row>

    <el-card class="status-card" shadow="hover">
      <template #header>
        <span>系统状态</span>
      </template>
      <el-descriptions :column="2" border>
        <el-descriptions-item label="后端服务">
          <el-tag :type="healthStatus === '运行正常' ? 'success' : 'danger'" size="small">
            {{ healthStatus }}
          </el-tag>
        </el-descriptions-item>
        <el-descriptions-item label="版本">{{ appVersion || '-' }}</el-descriptions-item>
      </el-descriptions>
    </el-card>
  </div>
</template>

<style scoped>
.home-page {
  max-width: 1200px;
}

.stat-row {
  margin-bottom: 20px;
}
</style>
