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

      <main class="content">
        <router-view />
      </main>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import {
  HomeFilled, Coin, Tickets, Collection, CircleCheck, User, Setting,
  Search, Bell, QuestionFilled, Fold, Expand, DataAnalysis, Connection, Service,
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

function logout() {
  localStorage.removeItem('access_token')
  router.push('/login')
}
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

.content {
  flex: 1;
  overflow: auto;
  padding: 20px;
  background: #fff;
}
</style>
