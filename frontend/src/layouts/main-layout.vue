<template>
  <div class="root">
    <!-- 左侧导航 — 白色背景，非 menu 组件 -->
    <aside class="aside" :class="{ collapsed: !sidebarOpen }">
      <div class="aside-header">
        <span v-if="sidebarOpen" class="aside-logo">AI 数据平台</span>
      </div>
      <nav class="aside-nav">
        <router-link
          v-for="item in navItems"
          :key="item.path"
          :to="item.path"
          class="nav-item"
          :class="{ active: route.path === item.path || (item.path !== '/' && route.path.startsWith(item.path)) }"
        >
          <el-icon :size="18">
            <component :is="item.icon" />
          </el-icon>
          <span v-if="sidebarOpen" class="nav-label">{{ item.label }}</span>
        </router-link>
      </nav>
    </aside>
    
    <!-- 右侧主区域 -->
    <div class="main-area">
      <!-- 顶栏 -->
      <header class="topbar">
        <div class="topbar-left">
          <el-button
            :icon="sidebarOpen ? Fold : Expand"
            text
            size="default"
            @click="sidebarOpen = !sidebarOpen"
          />
          <div class="search-wrap">
            <el-input
              placeholder="搜索数据源、数据表、数据集、字段..."
              :prefix-icon="Search"
            />
          </div>
        </div>
        <div class="topbar-right">
          <el-button
            text
            size="default"
            circle
          >
            <el-icon :size="18">
              <Bell />
            </el-icon>
          </el-button>
          <el-button
            text
            size="default"
            circle
          >
            <el-icon :size="18">
              <QuestionFilled />
            </el-icon>
          </el-button>
          <el-dropdown trigger="hover">
            <div class="user-area">
              <div class="avatar">管</div>
              <div class="user-meta">
                <div class="user-name">管理员</div>
                <div class="user-email">admin@company.com</div>
              </div>
            </div>
            <template #dropdown>
              <el-dropdown-menu>
                <el-dropdown-item @click="logout">退出登录</el-dropdown-item>
              </el-dropdown-menu>
            </template>
          </el-dropdown>
        </div>
      </header>
      
      <!-- 面包屑 + 标签（同容器） -->
      <div class="bread-tab-bar">
        <div class="breadcrumb-row">
          <router-link to="/" class="bread-link">首页</router-link>
          <template v-if="activeTabPath !== '/'">
            <span class="bread-sep">›</span>
            <span class="bread-current">{{ currentNav?.label }}</span>
          </template>
        </div>
        <div class="tab-row">
          <router-link
            v-for="tab in tabs"
            :key="tab.path"
            :to="tab.path"
            class="tab-item"
            :class="{ active: tab.path === activeTabPath }"
          >
            <el-icon :size="13">
              <component :is="tab.icon" />
            </el-icon>
            <span class="tab-text">{{ tab.label }}</span>
            <span
              v-if="tabs.length > 1"
              class="tab-close"
              @click.prevent.stop="closeTab(tab)"
            >
              <el-icon :size="12"><Close /></el-icon>
            </span>
          </router-link>
        </div>
      </div>
      
      <!-- 内容区 — 白底 -->
      <main class="content">
        <router-view />
      </main>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed, watch } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import {
  HomeFilled, Coin, Upload, Collection, CircleCheck, User, Setting,
  Search, Bell, QuestionFilled, Fold, Expand, Close,
} from '@element-plus/icons-vue'
import type { Component } from 'vue'

const router = useRouter()
const route = useRoute()
const sidebarOpen = ref(true)

const navItems: { path: string; icon: Component; label: string }[] = [
  { path: '/home', icon: HomeFilled, label: '首页' },
  { path: '/ingestion', icon: Upload, label: '接入任务' },
  { path: '/data-browse', icon: Collection, label: '数据浏览' },
  { path: '/data-sources', icon: Coin, label: '数据源' },
  { path: '/catalog', icon: Collection, label: '数据目录' },
  { path: '/quality', icon: CircleCheck, label: '数据质量' },
  { path: '/settings', icon: Setting, label: '系统设置' },
]

function matchNav(pathname: string) {
  return [...navItems].reverse().find(item =>
    item.path === '/' ? pathname === '/' : pathname === item.path || pathname.startsWith(item.path + '/')
  ) ?? navItems[0]
}

// Browser tabs
interface Tab {
  path: string;
  label: string;
  icon: Component
}

const tabs = ref<Tab[]>([])
const activeTabPath = ref('/home')

watch(() => route.path, (pathname) => {
  const item = matchNav(pathname)
  activeTabPath.value = item.path
  if (!tabs.value.find(t => t.path === item.path)) {
    tabs.value.push({ path: item.path, label: item.label, icon: item.icon })
  }
}, { immediate: true })

function closeTab(tab: Tab) {
  if (tabs.value.length <= 1) return
  const idx = tabs.value.indexOf(tab)
  tabs.value = tabs.value.filter(t => t.path !== tab.path)
  if (tab.path === activeTabPath.value) {
    const next = tabs.value[Math.min(idx, tabs.value.length - 1)]
    if (next) router.push(next.path)
  }
}

function logout() {
  localStorage.removeItem('access_token')
  router.push('/login')
}

const currentNav = computed(() => matchNav(route.path))
</script>

<style scoped>
.root {
  display: flex;
  height: 100vh;
  background: #f9fafb;
}

/* -- 侧边栏 -- */
.aside {
  width: 240px;
  background: #fff;
  border-right: 1px solid #e5e7eb;
  display: flex;
  flex-direction: column;
  transition: width 0.2s;
  flex-shrink: 0;
}

.aside.collapsed {
  width: 60px;
}

.aside-header {
  height: 52px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-bottom: 1px solid #e5e7eb;
  padding: 0 12px;
}

.aside-logo {
  font-size: $font-size-body;
  font-weight: $font-weight-semibold;
  color: #1f2937;
}

.aside-nav {
  flex: 1;
  overflow-y: auto;
  padding: 6px;
  display: flex;
  flex-direction: column;
  gap: 2px;
}

.nav-item {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 8px 10px;
  border-radius: 8px;
  color: #374151;
  text-decoration: none;
  font-size: $font-size-base;
  transition: background 0.15s;
}

.nav-item:hover {
  background: #f9fafb;
}

.nav-item.active {
  background: #eff6ff;
  color: #2563eb;
}

.collapsed .nav-item {
  justify-content: center;
  padding: 8px 0;
}

.nav-label {
  white-space: nowrap;
}

/* -- 主区域 -- */
.main-area {
  flex: 1;
  display: flex;
  flex-direction: column;
  overflow: hidden;
}

/* -- 顶栏 -- */
.topbar {
  background: #fff;
  border-bottom: 1px solid #e5e7eb;
  padding: 0 20px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 52px;
  flex-shrink: 0;
}

.topbar-left {
  display: flex;
  align-items: center;
  gap: 8px;
  flex: 1;
  max-width: 420px;
}

.search-wrap {
  flex: 1;

  :deep(.el-input__wrapper) {
    background: #f3f4f6;
    border-radius: 8px;
    box-shadow: none;
    transition: background 0.2s;

    &:hover {
      background: #e5e7eb;
    }
  }

  :deep(.el-input__inner) {
    &::placeholder {
      color: #9ca3af;
      font-size: 13px;
    }
  }
}

.topbar-right {
  display: flex;
  align-items: center;
  gap: 4px;
}

.user-area {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 8px 10px 8px 12px;
  margin-left: 4px;
  border-radius: 8px;
  cursor: pointer;
  transition: background 0.15s;

  &:hover {
    background: #f3f4f6;
  }
}

.avatar {
  width: 30px;
  height: 30px;
  border-radius: 50%;
  background: #dbeafe;
  color: #2563eb;
  font-size: $font-size-base;
  display: flex;
  align-items: center;
  justify-content: center;
}

.user-name {
  font-size: $font-size-base;
  color: #1f2937;
}

.user-email {
  font-size: $font-size-xs;
  color: #6b7280;
}

/* -- 面包屑 + 标签 -- */
.bread-tab-bar {
  background: #f3f4f6;
  border-bottom: 1px solid #e5e7eb;
  display: flex;
  flex-direction: column;
}

.breadcrumb-row {
  padding: 4px 12px 0;
  display: flex;
  align-items: center;
  gap: 4px;
  font-size: $font-size-sm;
}

.bread-link {
  color: #9ca3af;
  text-decoration: none;
}

.bread-link:hover {
  color: #4b5563;
}

.bread-sep {
  color: #d1d5db;
}

.bread-current {
  color: #6b7280;
}

.tab-row {
  display: flex;
  align-items: flex-end;
  gap: 2px;
  padding: 2px 8px 0 0;
  overflow-x: auto;
}

.tab-item {
  display: flex;
  align-items: center;
  gap: 5px;
  padding: 6px 14px;
  font-size: $font-size-sm;
  text-decoration: none;
  color: #6b7280;
  border-radius: 6px 6px 0 0;
  transition: all 0.15s;
  white-space: nowrap;
  max-width: 160px;
}

.tab-item:hover {
  color: #374151;
  background: rgba(255, 255, 255, 0.5);
}

.tab-item.active {
  background: #fff;
  color: #1f2937;
  border: 1px solid #e5e7eb;
  border-bottom-color: #fff;
  position: relative;
}

.tab-item.active::after {
  content: '';
  position: absolute;
  bottom: -1px;
  left: 0;
  right: 0;
  height: 1px;
  background: #fff;
}

.tab-text {
  overflow: hidden;
  text-overflow: ellipsis;
}

.tab-close {
  display: flex;
  align-items: center;
  opacity: 0;
  transition: opacity 0.1s;
  color: #9ca3af;
}

.tab-item:hover .tab-close {
  opacity: 1;
}

.tab-close:hover {
  color: #ef4444;
}

.tab-item.active .tab-close {
  opacity: 1;
  color: #d1d5db;
}

.tab-item.active .tab-close:hover {
  color: #ef4444;
}

/* -- 内容区 -- */
.content {
  flex: 1;
  overflow: auto;
  background: #fff;
  padding: 20px;
}
</style>
