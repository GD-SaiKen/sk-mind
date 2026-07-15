<template>
  <div class="page-layout detail-page">
    <PageHeader
      :title="ds?.name ?? '数据源详情'"
      :breadcrumb="[{ label: '首页', to: '/' }, { label: '数据源', to: '/data-sources' }, { label: ds?.name ?? '...' }]"
    >
      <template #tags>
        <el-tag v-if="ds" :type="statusTag(ds.status)" effect="plain">{{ statusLabel(ds.status) }}</el-tag>
        <el-tag v-if="ds" effect="plain">{{ ds.type }}</el-tag>
      </template>
      <template #actions>
        <el-button :icon="Edit" plain>编辑</el-button>
        <el-button :icon="VideoPlay" plain>创建任务</el-button>
        <el-button plain>检测连接</el-button>
        <el-button :icon="SwitchButton" plain type="danger">停用</el-button>
      </template>
    </PageHeader>

    <div v-if="!ds">
      <el-empty description="数据源不存在" />
    </div>
    <template v-else>
      <p class="desc">{{ ds.description }}</p>

      <!-- 信息卡片 -->
      <el-row :gutter="16" class="info-row">
        <el-col :span="6"><el-card shadow="never"><div class="info-label">接入方式</div><div>{{ ds.method }}</div></el-card></el-col>
        <el-col :span="6"><el-card shadow="never"><div class="info-label">业务负责人</div><div>{{ ds.businessOwner }}</div></el-card></el-col>
        <el-col :span="6"><el-card shadow="never"><div class="info-label">技术负责人</div><div>{{ ds.techOwner }}</div></el-card></el-col>
        <el-col :span="6"><el-card shadow="never"><div class="info-label">最近接入时间</div><div>{{ ds.lastSync }}</div></el-card></el-col>
      </el-row>

      <!-- 标签页内容 -->
      <el-tabs v-model="activeTab">
        <el-tab-pane label="基本信息" name="info">
          <el-card shadow="never">
            <h3>基本信息</h3>
            <el-descriptions :column="2" border>
              <el-descriptions-item label="数据源名称">{{ ds.name }}</el-descriptions-item>
              <el-descriptions-item label="数据源类型">{{ ds.type }}</el-descriptions-item>
              <el-descriptions-item label="接入方式">{{ ds.method }}</el-descriptions-item>
              <el-descriptions-item label="业务描述">{{ ds.description }}</el-descriptions-item>
              <el-descriptions-item label="业务负责人">{{ ds.businessOwner }}</el-descriptions-item>
              <el-descriptions-item label="技术负责人">{{ ds.techOwner }}</el-descriptions-item>
              <el-descriptions-item label="创建时间">2026-01-15 10:30</el-descriptions-item>
              <el-descriptions-item label="更新时间">{{ ds.lastSync }}</el-descriptions-item>
            </el-descriptions>
          </el-card>
        </el-tab-pane>

        <el-tab-pane label="接入任务 (2)" name="tasks">
          <el-card shadow="never">
            <div class="tab-header"><h3>关联的接入任务</h3><el-button type="primary">创建新任务</el-button></div>
            <div class="link-list">
              <div class="link-item">
                <div class="link-item-left">
                  <el-icon :size="18" class="text-success"><CircleCheckFilled /></el-icon>
                  <div><div>SAP 销售订单同步</div><div class="link-item-sub">最近执行: 2026-06-29 09:30 · 导入 1,250 条</div></div>
                </div>
                <span>成功 1,250 / 失败 0</span>
              </div>
              <div class="link-item">
                <div class="link-item-left">
                  <el-icon :size="18" class="text-warning"><WarningFilled /></el-icon>
                  <div><div>MES 生产记录同步</div><div class="link-item-sub">最近执行: 2026-06-29 09:00 · 部分成功</div></div>
                </div>
                <span>成功 800 / 失败 56</span>
              </div>
            </div>
          </el-card>
        </el-tab-pane>

        <el-tab-pane label="产出数据表 (2)" name="tables">
          <el-card shadow="never">
            <h3>产出的数据表</h3>
            <div class="link-list">
              <router-link to="/tables/1" class="link-item"><div><span>销售订单表</span><el-tag effect="plain" class="ml-sm">Serving</el-tag></div><span>1,250 条 · 24 字段</span></router-link>
              <router-link to="/tables/2" class="link-item"><div><span>客户信息表</span><el-tag effect="plain" class="ml-sm">Serving</el-tag></div><span>180 条 · 15 字段</span></router-link>
            </div>
          </el-card>
        </el-tab-pane>

        <el-tab-pane label="风险说明" name="risk">
          <el-card shadow="never">
            <h3>风险说明</h3>
            <el-descriptions :column="1" border>
              <el-descriptions-item label="数据敏感度">包含销售订单、客户信息等敏感业务数据</el-descriptions-item>
              <el-descriptions-item label="访问控制">需要财务部门或管理层权限才能访问</el-descriptions-item>
              <el-descriptions-item label="影响范围">该数据源停用将影响 2 个接入任务和 2 个数据表</el-descriptions-item>
            </el-descriptions>
          </el-card>
        </el-tab-pane>

        <el-tab-pane label="操作记录" name="logs">
          <el-card shadow="never">
            <h3>操作记录</h3>
            <div class="log-list">
              <div class="log-item highlight">2026-06-29 09:30 · 接入任务执行成功 · SAP 销售订单同步</div>
              <div class="log-item">2026-06-28 18:00 · 编辑数据源配置 · 更新技术负责人</div>
              <div class="log-item">2026-01-15 10:30 · 创建数据源 · 由管理员创建</div>
            </div>
          </el-card>
        </el-tab-pane>
      </el-tabs>
    </template>
  </div>
</template>

<script setup lang="ts">
import { computed, ref } from 'vue'
import { useRoute } from 'vue-router'
import { Edit, VideoPlay, SwitchButton, CircleCheckFilled, WarningFilled } from '@element-plus/icons-vue'
import PageHeader from '@/components/page-header.vue'

const route = useRoute()
const activeTab = ref('info')

interface DataSource {
  id: number; name: string; description: string; type: string; method: string;
  status: 'success' | 'warning' | 'error' | 'inactive';
  businessOwner: string; techOwner: string; lastSync: string; taskCount: number;
}

const mockData: Record<number, DataSource> = {
  1: { id: 1, name: 'SAP ERP 生产系统', description: '西门子 MES 核心数据库', type: 'ERP', method: 'JDBC 直连', status: 'success', businessOwner: '刘伟', techOwner: '赵一', lastSync: '2026-07-10 10:00', taskCount: 4 },
  2: { id: 2, name: 'MES 生产制造执行', description: 'Plataine MES 系统数据', type: 'MES', method: 'API 拉取', status: 'warning', businessOwner: '张涛', techOwner: '王芳', lastSync: '2026-07-10 09:30', taskCount: 2 },
  3: { id: 3, name: 'Excel 考勤数据', description: '人力资源部员工考勤表', type: 'Excel', method: '文件上传', status: 'error', businessOwner: '李敏', techOwner: '陈亮', lastSync: '2026-07-09 18:00', taskCount: 1 },
  4: { id: 4, name: '供应商主数据', description: 'ERP 供应商档案接口', type: 'API', method: 'REST API', status: 'success', businessOwner: '周磊', techOwner: '杨帆', lastSync: '2026-07-10 08:00', taskCount: 3 },
  5: { id: 5, name: '财务月报', description: 'CFO 月度财务汇总报表', type: 'Excel', method: '文件上传', status: 'inactive', businessOwner: '吴婷', techOwner: '马超', lastSync: '2026-07-01 12:00', taskCount: 0 },
  6: { id: 6, name: 'MES 设备 OEE 数据', description: '设备综合效率实时数据', type: 'MES', method: 'MQTT 订阅', status: 'success', businessOwner: '张涛', techOwner: '王芳', lastSync: '2026-07-10 10:15', taskCount: 2 },
}

const ds = computed(() => {
  const id = Number(route.params.id)
  return mockData[id] ?? null
})

function statusTag(s: string) { return s === 'success' ? 'success' : s === 'warning' ? 'warning' : s === 'error' ? 'danger' : 'info' }
function statusLabel(s: string) { const m: Record<string, string> = { success: '正常', warning: '警告', error: '异常', inactive: '停用' }; return m[s] ?? s }
</script>

<style lang="scss" scoped>
.desc { color: $color-text-secondary; font-size: $font-size-base; margin: 0; }
.info-row { margin: 0 !important; }
.info-label { font-size: $font-size-sm; color: $color-text-secondary; margin-bottom: 4px; }
.tab-header { display: flex; align-items: center; justify-content: space-between; margin-bottom: 16px; }
h3 { font-size: $font-size-body; margin-bottom: 16px; }
.link-list { display: flex; flex-direction: column; gap: 8px; }
.link-item { display: flex; align-items: center; justify-content: space-between; padding: 12px; border: 1px solid $color-border; border-radius: $radius-base; text-decoration: none; color: inherit; &:hover { background: #f9fafb; } }
.link-item-left { display: flex; align-items: center; gap: 12px; }
.link-item-sub { font-size: $font-size-sm; color: $color-text-secondary; }
.text-success { color: $color-success; }
.text-warning { color: $color-warning; }
.ml-sm { margin-left: 8px; }
.log-list { display: flex; flex-direction: column; }
.log-item { padding: 10px 12px; border-left: 2px solid $color-border; font-size: $font-size-base; color: $color-text-regular; &.highlight { border-left-color: $color-primary; background: #eff6ff; } }
</style>
