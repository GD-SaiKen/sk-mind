import { createRouter, createWebHistory } from 'vue-router';
import MainLayout from '@/layouts/main-layout.vue';

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/login',
      name: 'Login',
      component: () => import('@/views/login.vue'),
    },
    {
      path: '/',
      component: MainLayout,
      redirect: '/home',
      children: [
        {
          path: 'home',
          name: 'Home',
          component: () => import('@/views/home.vue'),
          meta: { title: '首页', icon: 'HomeFilled' },
        },
        {
          path: 'ingestion',
          name: 'Ingestion',
          component: () => import('@/views/ingestion-task/list.vue'),
          meta: { title: '接入任务', icon: 'Upload' },
        },
        {
          path: 'ingestion/:id',
          name: 'IngestionDetail',
          component: () => import('@/views/ingestion-task/detail.vue'),
          meta: { title: '任务详情', icon: 'Upload', hidden: true },
        },
        {
          path: 'data-browse',
          name: 'DataBrowse',
          component: () => import('@/views/data-browse/list.vue'),
          meta: { title: '数据浏览', icon: 'Collection' },
        },
        {
          path: 'data-sources',
          name: 'DataSources',
          component: () => import('@/views/data-sources.vue'),
          meta: { title: '数据源', icon: 'Coin' },
        },
        {
          path: 'catalog',
          name: 'Catalog',
          component: () => import('@/views/catalog.vue'),
          meta: { title: '数据目录', icon: 'Collection' },
        },
        {
          path: 'quality',
          name: 'Quality',
          component: () => import('@/views/quality.vue'),
          meta: { title: '数据质量', icon: 'CircleCheck' },
        },
        {
          path: 'settings',
          name: 'Settings',
          component: () => import('@/views/settings.vue'),
          meta: { title: '系统设置', icon: 'Setting' },
        },
      ],
    },
  ],
});

router.beforeEach((to) => {
  const token = localStorage.getItem('access_token');
  if (to.path !== '/login' && !token) {
    return '/login';
  }
});

export default router;
