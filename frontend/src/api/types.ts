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
