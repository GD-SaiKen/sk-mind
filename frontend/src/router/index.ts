import { createRouter, createWebHistory } from 'vue-router'
import MainLayout from '@/layouts/MainLayout.vue'

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/',
      component: MainLayout,
      redirect: '/home',
      children: [
        {
          path: 'home',
          name: 'Home',
          component: () => import('@/views/Home.vue'),
          meta: { title: '首页' },
        },
        {
          path: 'data-sources',
          name: 'DataSources',
          component: () => import('@/views/DataSources.vue'),
          meta: { title: '数据源管理' },
        },
        {
          path: 'ingestion',
          name: 'Ingestion',
          component: () => import('@/views/Ingestion.vue'),
          meta: { title: '接入任务' },
        },
        {
          path: 'catalog',
          name: 'Catalog',
          component: () => import('@/views/Catalog.vue'),
          meta: { title: '数据目录' },
        },
        {
          path: 'quality',
          name: 'Quality',
          component: () => import('@/views/Quality.vue'),
          meta: { title: '数据质量' },
        },
      ],
    },
  ],
})

export default router
