<script setup lang="ts">
import { ref, computed } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import {
  DataBoard,
  Coin,
  Upload,
  Collection,
  CircleCheck,
  ArrowLeft,
  ArrowRight,
} from '@element-plus/icons-vue'

const router = useRouter()
const route = useRoute()
const isCollapsed = ref(false)

const menuItems = [
  { path: '/home', title: '首页', icon: DataBoard },
  { path: '/data-sources', title: '数据源管理', icon: Coin },
  { path: '/ingestion', title: '接入任务', icon: Upload },
  { path: '/catalog', title: '数据目录', icon: Collection },
  { path: '/quality', title: '数据质量', icon: CircleCheck },
]

const activeMenu = computed(() => route.path)
const pageTitle = computed(() => route.meta?.title as string ?? '')

function navigate(path: string) {
  router.push(path)
}
</script>

<template>
  <el-container class="main-layout">
    <!-- 侧边栏 -->
    <el-aside :width="isCollapsed ? '64px' : '220px'" class="layout-aside">
      <div class="logo-area" @click="navigate('/home')">
        <span v-if="!isCollapsed" class="logo-text">sk-mind</span>
        <span v-else class="logo-text-mini">S</span>
      </div>
      <el-menu
        :default-active="activeMenu"
        :collapse="isCollapsed"
        :collapse-transition="false"
        background-color="#001529"
        text-color="#ffffffa6"
        active-text-color="#fff"
        @select="navigate"
      >
        <el-menu-item v-for="item in menuItems" :key="item.path" :index="item.path">
          <el-icon><component :is="item.icon" /></el-icon>
          <template #title>{{ item.title }}</template>
        </el-menu-item>
      </el-menu>
    </el-aside>

    <el-container>
      <!-- 顶栏 -->
      <el-header class="layout-header">
        <div class="header-left">
          <el-button
            :icon="isCollapsed ? ArrowRight : ArrowLeft"
            text
            @click="isCollapsed = !isCollapsed"
          />
          <span class="page-title">{{ pageTitle }}</span>
        </div>
        <div class="header-right">
          <span class="user-info">管理员</span>
        </div>
      </el-header>

      <!-- 主内容区 -->
      <el-main class="layout-main">
        <router-view />
      </el-main>
    </el-container>
  </el-container>
</template>

<style scoped>
.main-layout {
  height: 100vh;
}

.layout-aside {
  background-color: #001529;
  overflow: hidden;
  transition: width 0.2s;
}

.logo-area {
  height: 60px;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
}

.logo-text {
  color: #fff;
  font-size: 18px;
  font-weight: 600;
  letter-spacing: 1px;
}

.logo-text-mini {
  color: #fff;
  font-size: 20px;
  font-weight: 700;
}

.layout-header {
  background: #fff;
  border-bottom: 1px solid #e4e7ed;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 16px;
}

.header-left {
  display: flex;
  align-items: center;
  gap: 8px;
}

.page-title {
  font-size: 16px;
  font-weight: 500;
  color: #303133;
}

.header-right {
  display: flex;
  align-items: center;
}

.user-info {
  color: #606266;
  font-size: 14px;
}

.layout-main {
  background: #f5f7fa;
  min-height: 0;
}

:deep(.el-menu) {
  border-right: none;
}
</style>
