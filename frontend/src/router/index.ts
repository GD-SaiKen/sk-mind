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
          component: () => import('@/views/home/index.vue'),
          meta: { title: '首页', icon: 'HomeFilled' },
        },
        {
          path: 'data-sources',
          name: 'DataSources',
          component: () => import('@/views/data-sources/list.vue'),
          meta: { title: '数据源', icon: 'Coin' },
        },
        {
          path: 'data-sources/create',
          name: 'DataSourceCreate',
          component: () => import('@/views/data-sources/create.vue'),
          meta: { title: '新增数据源', icon: 'Coin', hidden: true },
        },
        {
          path: 'data-sources/:id',
          name: 'DataSourceDetail',
          component: () => import('@/views/data-sources/detail.vue'),
          meta: { title: '数据源详情', icon: 'Coin', hidden: true },
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
          path: 'ingestion/:taskId/batch/:batchId',
          name: 'IngestionBatchDetail',
          component: () => import('@/views/ingestion-task/batch-detail.vue'),
          meta: { title: '批次详情', icon: 'Upload', hidden: true },
        },
        {
          path: 'tables',
          name: 'DataTables',
          component: () => import('@/views/data-tables/index.vue'),
          meta: { title: '数据表', icon: 'Collection' },
        },
        {
          path: 'tables/browse',
          name: 'DataBrowse',
          component: () => import('@/views/data-tables/list.vue'),
          meta: { title: '数据浏览', icon: 'Collection', hidden: true },
        },
        {
          path: 'tables/:id',
          name: 'DataTableDetail',
          component: () => import('@/views/data-tables/detail.vue'),
          meta: { title: '数据表详情', icon: 'Collection', hidden: true },
        },
        {
          path: 'tables/:tableId/field/:fieldName',
          name: 'DataTableFieldDetail',
          component: () => import('@/views/data-tables/field-detail.vue'),
          meta: { title: '字段详情', icon: 'Collection', hidden: true },
        },
        {
          path: 'catalog',
          name: 'Catalog',
          component: () => import('@/views/catalog/index.vue'),
          meta: { title: '数据目录', icon: 'Collection' },
        },
        {
          path: 'catalog/:id',
          name: 'CatalogDetail',
          component: () => import('@/views/catalog/detail.vue'),
          meta: { title: '数据集详情', icon: 'Collection', hidden: true },
        },
        {
          path: 'quality',
          name: 'Quality',
          component: () => import('@/views/quality/index.vue'),
          meta: { title: '数据质量', icon: 'CircleCheck' },
        },
        {
          path: 'quality/:id',
          name: 'QualityDetail',
          component: () => import('@/views/quality/detail.vue'),
          meta: { title: '质量详情', icon: 'CircleCheck', hidden: true },
        },
        {
          path: 'permissions',
          name: 'PermissionAudit',
          component: () => import('@/views/permission-audit/index.vue'),
          meta: { title: '权限审计', icon: 'User' },
        },
        {
          path: 'semantic',
          name: 'SemanticModel',
          component: () => import('@/views/semantic-model/index.vue'),
          meta: { title: '语义模型', icon: 'DataAnalysis' },
        },
        {
          path: 'graph',
          name: 'RelationGraph',
          component: () => import('@/views/relation-graph/index.vue'),
          meta: { title: '关系图谱', icon: 'Connection' },
        },
        {
          path: 'agent',
          name: 'AgentService',
          component: () => import('@/views/agent-service/index.vue'),
          meta: { title: 'Agent 服务', icon: 'Service' },
        },
        {
          path: 'settings',
          name: 'Settings',
          component: () => import('@/views/settings/index.vue'),
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
