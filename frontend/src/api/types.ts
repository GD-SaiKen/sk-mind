// API 类型定义

// ── Auth ──
export interface LoginParams {
  username: string
  password: string
}

// ── DataSource ──
export type DataSourceType =
  | 'erp'
  | 'mes'
  | 'purchase'
  | 'attendance'
  | 'database'
  | 'api'
  | 'excel'
  | 'share_drive'
  | 'other'

export type AccessMethod =
  | 'db_sync'
  | 'api_pull'
  | 'file_upload'
  | 'excel_import'
  | 'share_scan'

export type DataSourceStatus =
  | 'unconnected'
  | 'syncing'
  | 'active'
  | 'error'
  | 'paused'

export interface DataSource {
  id: string
  name: string
  code: string
  sourceType: DataSourceType
  accessMethod: AccessMethod
  description: string
  businessOwner: string
  techOwner: string
  ownerDept: string
  status: DataSourceStatus
  lastSyncAt: string | null
  taskCount: number
  createdAt: string
  updatedAt: string
}

export interface DataSourceFormData {
  name: string
  code: string
  sourceType: DataSourceType
  accessMethod: AccessMethod
  description: string
  businessOwner: string
  techOwner: string
  ownerDept: string
}

// ── Ingestion ──
export interface IngestionTask {
  id: string
  name: string
  code: string
  dataSourceId: string
  targetLayer: string
  syncMode: string
  scheduleType: string
  cronExpression: string | null
  lastSyncAt: string | null
  lastSyncStatus: string | null
  status: string
  config: Record<string, unknown> | null
  createdAt: string
  updatedAt: string
}

export interface IngestionBatch {
  id: string
  taskId: string
  triggerType: string
  status: string
  startedAt: string | null
  finishedAt: string | null
  recordCount: number
  successCount: number
  failCount: number
  skipCount: number
  createdAt: string
}

export interface BatchProgress {
  batchId: string
  status: string
  progress: number
  step: string
  lastHeartbeat: string | null
}

export interface ImportError {
  id: string
  batchId: string
  errorLevel: string
  errorType: string
  errorMessage: string
  rawValue: string | null
  createdAt: string
}

export interface TimeRange {
  syncMode: string
  lastSyncAt: string | null
  suggestedStart: string | null
  suggestedEnd: string | null
  historyStartDate: string | null
  scheduleCron: string | null
  scheduleDescription: string | null
}
