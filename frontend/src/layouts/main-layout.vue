<template>
  <div class="root">
    <aside
      class="aside"
      :class="{ collapsed: !sidebarOpen }"
    >
      <div class="aside-header">
        <span
          v-if="sidebarOpen"
          class="aside-logo"
        >AI 数据平台</span>
      </div>
      <nav class="aside-nav">
        <router-link
          v-for="item in navItems"
          :key="item.path"
          :to="item.path"
          class="nav-item"
          :class="{
            active: route.path === item.path || (item.path !== '/' && route.path.startsWith(item.path)),
          }"
        >
          <el-icon :size="18">
            <component :is="item.icon" />
          </el-icon>
          <span
            v-if="sidebarOpen"
            class="nav-label"
          >{{ item.label }}</span>
        </router-link>
      </nav>
    </aside>

    <div class="main-area">
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
              placeholder="搜索数据源、数据表、数据集、字段、业务对象、接入任务..."
              :prefix-icon="Search"
            />
          </div>
        </div>
        <div class="topbar-right">
          <el-tag
            effect="plain"
            class="env-tag"
          >
            测试环境
          </el-tag>
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
                <div class="user-role">超级管理员</div>
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

      <div class="bread-tab-bar">
        <div class="breadcrumb-row">
          <router-link
            to="/"
            class="bread-link"
          >
            首页
          </router-link>
          <template v-if="activeTabPath !== '/'">
            <span class="bread-sep">/</span>
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
  HomeFilled, Coin, Tickets, Collection, CircleCheck, User, Setting,
  Search, Bell, QuestionFilled, Fold, Expand, Close, DataAnalysis, Connection, Service,
} from '@element-plus/icons-vue'
import type { Component } from 'vue'

const router = useRouter()
const route = useRoute()
const sidebarOpen = ref(true)

const navItems: { path: string; icon: Component; label: string }[] = [
  {
    path: '/home',
    icon: HomeFilled,
    label: '首页',
  },
  {
    path: '/data-sources',
    icon: Coin,
    label: '数据源',
  },
  {
    path: '/ingestion',
    icon: Tickets,
    label: '接入任务',
  },
  {
    path: '/tables',
    icon: Collection,
    label: '数据表',
  },
  {
    path: '/catalog',
    icon: Collection,
    label: '数据目录',
  },
  {
    path: '/quality',
    icon: CircleCheck,
    label: '数据质量',
  },
  {
    path: '/permissions',
    icon: User,
    label: '权限审计',
  },
  {
    path: '/semantic',
    icon: DataAnalysis,
    label: '语义模型',
  },
  {
    path: '/graph',
    icon: Connection,
    label: '关系图谱',
  },
  {
    path: '/agent',
    icon: Service,
    label: 'Agent 服务',
  },
  {
    path: '/settings',
    icon: Setting,
    label: '系统设置',
  },
]

function matchNav(pathname: string) {
  return [...navItems].reverse().find(item =>
    item.path === '/'
      ? pathname === '/'
      : pathname === item.path || pathname.startsWith(item.path + '/'),
  ) ?? navItems[0]
}

interface Tab {
  path: string
  label: string
  icon: Component
}

const tabs = ref<Tab[]>([])
const activeTabPath = ref('/home')

watch(() => route.path, (pathname) => {
  const item = matchNav(pathname)
  activeTabPath.value = item.path
  if (!tabs.value.find(t => t.path === item.path)) {
    tabs.value.push({
      path: item.path,
      label: item.label,
      icon: item.icon,
    })
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

<style lang="scss" scoped>
.root {
  display: flex;
  height: 100vh;
  background: #f9fafb;
}

.aside {
  display: flex;
  flex-direction: column;
  flex-shrink: 0;
  width: 240px;
  background: #fff;
  border-right: 1px solid #e5e7eb;
  transition: width 0.2s;
}

.aside.collapsed {
  width: 60px;
}

.aside-header {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 52px;
  padding: 0 12px;
  border-bottom: 1px solid #e5e7eb;
}

.aside-logo {
  font-size: 16px;
  font-weight: 600;
  color: #1f2937;
}

.aside-nav {
  display: flex;
  flex: 1;
  flex-direction: column;
  gap: 2px;
  overflow-y: auto;
  padding: 6px;
}

.nav-item {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 8px 10px;
  border-radius: 8px;
  color: #374151;
  text-decoration: none;
  font-size: 14px;
  transition: background 0.15s;

  &:hover {
    background: #f9fafb;
  }

  &.active {
    background: #eff6ff;
    color: #2563eb;
  }
}

.collapsed .nav-item {
  justify-content: center;
  padding: 8px 0;
}

.nav-label {
  white-space: nowrap;
}

.main-area {
  display: flex;
  flex: 1;
  flex-direction: column;
  overflow: hidden;
}

.topbar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-shrink: 0;
  height: 52px;
  padding: 0 20px;
  background: #fff;
  border-bottom: 1px solid #e5e7eb;
}

.topbar-left {
  display: flex;
  align-items: center;
  flex: 1;
  gap: 8px;
  max-width: 460px;
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

  :deep(.el-input__inner::placeholder) {
    color: #9ca3af;
    font-size: 13px;
  }
}

.topbar-right {
  display: flex;
  align-items: center;
  gap: 4px;
}

.env-tag {
  margin-right: 4px;
  font-size: 12px;
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
  display: flex;
  align-items: center;
  justify-content: center;
  width: 30px;
  height: 30px;
  border-radius: 50%;
  background: #dbeafe;
  color: #2563eb;
  font-size: 14px;
}

.user-name {
  font-size: 14px;
  color: #1f2937;
}

.user-role {
  font-size: 12px;
  color: #9ca3af;
}

.bread-tab-bar {
  display: flex;
  flex-direction: column;
  background: #f3f4f6;
  border-bottom: 1px solid #e5e7eb;
}

.breadcrumb-row {
  display: flex;
  align-items: center;
  gap: 4px;
  padding: 4px 12px 0;
  font-size: 13px;
}

.bread-link {
  color: #9ca3af;
  text-decoration: none;

  &:hover {
    color: #4b5563;
  }
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
  border-radius: 6px 6px 0 0;
  color: #6b7280;
  text-decoration: none;
  font-size: 13px;
  white-space: nowrap;
  max-width: 160px;
  transition: all 0.15s;

  &:hover {
    color: #374151;
    background: rgba(255, 255, 255, 0.5);
  }

  &.active {
    position: relative;
    background: #fff;
    color: #1f2937;
    border: 1px solid #e5e7eb;
    border-bottom-color: #fff;

    &::after {
      content: '';
      position: absolute;
      bottom: -1px;
      left: 0;
      right: 0;
      height: 1px;
      background: #fff;
    }
  }
}

.tab-text {
  overflow: hidden;
  text-overflow: ellipsis;
}

.tab-close {
  display: flex;
  align-items: center;
  opacity: 0;
  color: #9ca3af;
  transition: opacity 0.1s;

  &:hover {
    color: #ef4444;
  }
}

.tab-item:hover .tab-close {
  opacity: 1;
}

.tab-item.active .tab-close {
  opacity: 1;
  color: #d1d5db;

  &:hover {
    color: #ef4444;
  }
}

.content {
  flex: 1;
  overflow: auto;
  padding: 20px;
  background: #fff;
}
</style>
