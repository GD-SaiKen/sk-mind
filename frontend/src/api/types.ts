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

// ── API Interfaces (for task creation) ──
export interface ApiInterfaceItem {
  name: string
  endpoint: string
  method: string
  targetTable: string
  order: number
  isTimeBased: boolean
  pkFields: string[]
}

export interface IngestionTaskFormData {
  name: string
  code: string
  dataSourceId: string
  syncMode: string
  scheduleType: string
  cronExpression: string | null
  description: string
  selectedInterfaces: string[]
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

// ── Dataset ──
export interface DatasetResponse {
  id: string
  name: string
  code: string
  description: string | null
  dataLayer: string
  dataSourceId: string | null
  sourceObjectId: string | null
  generatedByTaskId: string | null
  lastBatchId: string | null
  recordCount: number | null
  fieldCount: number | null
  businessDomain: string | null
  ownerName: string | null
  tags: string | null
  sensitivityLevel: string
  isAgentAccessible: boolean
  status: string
  createdAt: string
  updatedAt: string
}

export interface DatasetFieldResponse {
  id: string
  datasetId: string
  fieldName: string
  fieldAlias: string | null
  description: string | null
  dataType: string
  fieldLength: number | null
  isNullable: boolean
  ordinalPosition: number
  sensitivityLevel: string
  qualityStatus: string | null
  sampleValues: string | null
  createdAt: string
  updatedAt: string
}

export interface DataTableResponse {
  id: string
  datasetId: string | null
  schemaName: string
  tableName: string
  tableType: string
  description: string | null
  rowCount: number | null
  dataSizeBytes: number | null
  createdAt: string
  updatedAt: string
}

export interface PaginatedData<T> {
  items: T[]
  total: number
  page: number
  pageSize: number
}

// ── Quality ──
export type QualityRuleType =
  | 'not_null' | 'unique' | 'enum' | 'range'
  | 'format' | 'freshness' | 'completeness'

export type QualitySeverity = 'info' | 'warning' | 'error' | 'critical'

export interface QualityRule {
  id: string
  name: string
  code: string
  description: string | null
  ruleType: string
  datasetId: string | null
  fieldId: string | null
  ruleParams: Record<string, unknown> | null
  isEnabled: boolean
  severity: string
  createdAt: string
  updatedAt: string
}

export interface QualityRun {
  id: string
  triggeredBy: string | null
  triggerType: string
  ruleIds: string | null
  datasetIds: string | null
  startedAt: string | null
  finishedAt: string | null
  totalRules: number
  passedRules: number
  failedRules: number
  totalIssues: number
  status: string
  createdAt: string
}

export interface QualityIssue {
  id: string
  qualityRunId: string
  ruleId: string
  datasetId: string | null
  fieldId: string | null
  batchId: string | null
  issueType: string
  severity: string
  issueMessage: string
  sampleValue: string | null
  sampleRow: number | null
  affectedRecordCount: number | null
  status: string
  createdAt: string
}

export interface QualityStats {
  totalRules: number
  enabledRules: number
  passedCount: number
  warningCount: number
  errorCount: number
  passRate: number
  openIssues: number
}

// ── Lineage ──
export interface LineageEdge {
  id: string
  sourceType: string
  sourceId: string
  sourceName: string
  targetType: string
  targetId: string
  targetName: string
  transformType: string
  transformRule: string | null
  ingestionTaskId: string | null
  batchId: string | null
  description: string | null
  createdAt: string
  updatedAt: string
}

export interface LineageStats {
  totalEdges: number
  confirmedCount: number
  aiGeneratedCount: number
  pendingCount: number
  confirmRate: number
}
