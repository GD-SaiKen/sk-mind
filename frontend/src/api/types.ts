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
  | 'draft'
  | 'unconnected'
  | 'syncing'
  | 'active'
  | 'error'
  | 'paused'
  | 'archived'

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
  sourceCategory?: string | null
  lastSyncAt: string | null
  taskCount: number
  connectionConfig?: ConnectionConfig | null
  createdAt: string
  updatedAt: string
}

/** 数据源连接配置（API 拉取 / 数据库同步等） */
export interface ConnectionConfig {
  baseUrl?: string
  authType?: AuthType
  authHeaderName?: string
  authCredentials?: string
  authHeaderName2?: string
  authCredentials2?: string
  qpsLimit?: number
  timeout?: number
  sslVerify?: boolean
  recordsPath?: string
  totalPath?: string
}

export type AuthType =
  | 'none'
  | 'bearer'
  | 'basic'
  | 'api_key'
  | 'dual_key'
  | 'session'

export interface DataSourceFormData {
  name: string
  code: string
  sourceType: DataSourceType
  accessMethod: AccessMethod
  description: string
  businessOwner: string
  techOwner: string
  ownerDept: string
  connectionConfig?: ConnectionConfig | null
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
  description?: string | null
  nextRunAt?: string | null
  replayWindowDays?: number
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
  errorSummary: string | null
  progressStep: string | null
  sourceSignature: string | null
  rejectedRows: string | null
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
  agentUnavailableReason: string | null  // T6
  status: string
  sourceName: string | null  // derived from JOIN data_sources
  qualityStatus: string | null  // ok / warning / error
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
  isPrimaryKey: boolean          // T1
  sourceColumn: string | null     // T1
  nullRate: number | null         // T5
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

// ── 同步引擎优化：对账机制 ──
export interface Reconciliation {
  id: string
  dataSourceId: string
  interfaceName: string
  batchId: string | null
  checkLevel: 'L1' | 'L2' | 'L3'
  apiTotal: number | null
  dbCount: number | null
  pulledCount: number | null
  diffCount: number | null
  diffRatio: number | null
  status: 'pass' | 'warning' | 'failed' | 'repaired'
  syncMode: 'full' | 'incremental' | null
  detail: ReconciliationSegment[] | null
  checkedAt: string
}

export interface ReconciliationSegment {
  dateRange: string
  apiCount: number
  dbCount: number
  diff: number
  status: 'consistent' | 'inconsistent'
}

// ── 同步引擎优化：Schema 变更 ──
export interface SchemaChange {
  id: string
  tableName: string
  changeType: 'added' | 'removed' | 'type_changed'
  columnName: string
  detail: Record<string, unknown> | null
  detectedAt: string
}

// ── 同步引擎优化：隔离区 ──
export interface QuarantineRecord {
  id: string
  batchId: string
  dataSourceId: string
  interfaceName: string
  pkValue: string | null
  rejectionReason: 'null_pk' | 'dup_in_batch' | 'type_error' | 'write_error'
  // rawJson: 后端 JSONB 字段，CamelModel 序列化后可能返回 object 或 string
  // 类型用联合类型，formatRawJson() 统一处理两种情况
  rawJson: string | Record<string, unknown>
  status: 'pending' | 'retried' | 'resolved' | 'ignored'
  createdAt: string
  retriedAt: string | null
  resolvedAt: string | null
}

export interface QuarantineStats {
  totalCount: number
  pendingCount: number
  resolvedCount: number
  ignoredCount: number
  quarantineRate: number
  threshold: number              // 熔断阈值（百分比，如 5 表示 5%），从后端 YAML 配置返回
  circuitBreakerTriggered: boolean
}

// ── 同步引擎优化：定时调度 ──
export interface CronPreview {
  cronExpression: string
  nextRun: string | null
  isValid: boolean
  description: string | null
}

// ── T4: 字段编辑 ──
export interface DatasetFieldUpdate {
  fieldAlias?: string
  description?: string
  sensitivityLevel?: string
}

export interface DatasetFieldBatchUpdate {
  fieldIds: string[]
  sensitivityLevel?: string
}

// T4: 样例数据
export interface SampleDataResponse {
  columns: string[]
  rows: unknown[][]
  total: number
}

// ── T6: Agent 可用性检查 ──
export interface AgentCheckResponse {
  passed: boolean
  reasons: string[]
  fieldDescriptionCoverage: number
  unmarkedSensitiveCount: number
}
