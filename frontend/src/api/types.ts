// API 类型定义

// ── Auth ──
export interface LoginParams {
  username: string
  password: string
}

// ── Ingestion ──
export interface IngestionTask {
  id: string
  name: string
  code: string
  dataSourceId: string
  targetLayer: string
  scheduleType: string
  status: string
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
