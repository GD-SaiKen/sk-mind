import type { DataSourceStatus, DataSourceType, AccessMethod, AuthType } from '@/api'

// ===== 数据源类型 =====
export const SOURCE_TYPE_LABELS: Record<DataSourceType, string> = {
  erp: 'ERP',
  mes: 'MES',
  purchase: '采购',
  attendance: '考勤',
  database: '数据库',
  api: 'API',
  excel: 'Excel',
  share_drive: '共享盘',
  other: '其他',
}

export const SOURCE_TYPE_OPTIONS = Object.entries(SOURCE_TYPE_LABELS).map(
  ([value, label]) => ({ label, value }),
)

// ===== 接入方式 =====
export const ACCESS_METHOD_LABELS: Record<AccessMethod, string> = {
  db_sync: '数据库同步',
  api_pull: 'API 拉取',
  file_upload: '文件上传',
  excel_import: 'Excel 导入',
  share_scan: '共享盘扫描',
}

export const ACCESS_METHOD_OPTIONS = Object.entries(ACCESS_METHOD_LABELS).map(
  ([value, label]) => ({ label, value }),
)

// ===== 鉴权方式 =====
export const AUTH_TYPE_LABELS: Record<AuthType, string> = {
  none: '无需鉴权',
  bearer: 'Bearer Token',
  basic: 'Basic Auth',
  api_key: 'API Key',
  dual_key: '双密钥（Dual Key）',
  session: '动态登录（Session）',
}

export const AUTH_TYPE_OPTIONS = Object.entries(AUTH_TYPE_LABELS).map(
  ([value, label]) => ({ label, value }),
)

// ===== 数据源状态 =====
export const STATUS_LABELS: Record<DataSourceStatus, string> = {
  draft: '草稿',
  unconnected: '未接入',
  syncing: '接入中',
  active: '正常',
  error: '异常',
  paused: '停用',
  archived: '已归档',
}

export const STATUS_TAG_MAP: Record<DataSourceStatus, '' | 'success' | 'warning' | 'danger' | 'info'> = {
  draft: 'info',
  unconnected: 'info',
  syncing: '',
  active: 'success',
  error: 'danger',
  paused: 'warning',
  archived: 'info',
}

export const STATUS_OPTIONS = Object.entries(STATUS_LABELS).map(
  ([value, label]) => ({ label, value }),
)
