import api from '../client'

export class IngestionService {
  private api = api

  // ── Task CRUD ──
  getList(params?: Record<string, unknown>) {
    return this.api.get('/ingestion-tasks', { params }).then(r => r.data.data)
  }

  get(id: string) {
    return this.api.get(`/ingestion-tasks/${id}`).then(r => r.data.data)
  }

  create(data: Record<string, unknown>) {
    return this.api.post('/ingestion-tasks', data).then(r => r.data.data)
  }

  /** Create a task with selected API interfaces */
  createApiTask(
    name: string,
    code: string,
    dataSourceId: string,
    interfaces: string[],
    dataSourceCode: string = '',
    syncMode: string = 'full',
    scheduleType: string = 'manual',
    cronExpression: string = '',
    description: string = '',
  ) {
    return this.api.post('/ingestion-tasks', {
      name,
      code,
      dataSourceId,
      targetLayer: 'raw',
      syncMode,
      scheduleType,
      cronExpression: cronExpression || undefined,
      config: {
        accessMethod: 'api',
        configPath: `config/data_sources/${dataSourceCode}.yaml`,
        interfaces,
      },
      description,
    }).then(r => r.data.data)
  }

  update(id: string, data: Record<string, unknown>) {
    return this.api.put(`/ingestion-tasks/${id}`, data).then(r => r.data.data)
  }

  delete(id: string) {
    return this.api.delete(`/ingestion-tasks/${id}`).then(r => r.data)
  }

  enable(id: string) {
    return this.api.post(`/ingestion-tasks/${id}/enable`).then(r => r.data)
  }

  disable(id: string) {
    return this.api.post(`/ingestion-tasks/${id}/disable`).then(r => r.data)
  }

  // ── Execute ──
  execute(id: string) {
    return this.api.post(`/ingestion-tasks/${id}/execute`).then(r => r.data.data)
  }

  // ── Batches ──
  getBatches(taskId: string, params?: Record<string, unknown>) {
    return this.api.get(`/ingestion-tasks/${taskId}/batches`, { params }).then(r => r.data.data)
  }

  getBatch(batchId: string) {
    return this.api.get(`/ingestion-tasks/batches/${batchId}`).then(r => r.data.data)
  }

  getBatchProgress(batchId: string) {
    return this.api.get(`/ingestion-tasks/batches/${batchId}/progress`).then(r => r.data.data)
  }

  getBatchErrors(batchId: string, params?: Record<string, unknown>) {
    return this.api.get(`/ingestion-tasks/batches/${batchId}/errors`, { params }).then(r => r.data.data)
  }

  retryBatch(batchId: string) {
    return this.api.post(`/ingestion-tasks/batches/${batchId}/retry`).then(r => r.data.data)
  }

  // ── 取消 / 回退 ──
  cancelBatch(batchId: string) {
    return this.api.post(`/ingestion-tasks/batches/${batchId}/cancel`).then(r => r.data.data)
  }

  rollbackBatch(batchId: string) {
    return this.api.post(`/ingestion-tasks/batches/${batchId}/rollback`).then(r => r.data.data)
  }

  // ── 全量回溯 / 快补 / 时间范围预览（目标1+3）──
  backfill(id: string) {
    return this.api.post(`/ingestion-tasks/${id}/backfill`).then(r => r.data.data)
  }

  quickFill(id: string, startTime: string, endTime: string) {
    return this.api.post(`/ingestion-tasks/${id}/quick-fill`, { startTime, endTime }).then(r => r.data.data)
  }

  getTimeRange(id: string) {
    return this.api.get(`/ingestion-tasks/${id}/time-range`).then(r => r.data.data)
  }

  // ── 对账（同步引擎优化）──
  getReconciliations(taskId: string, params?: Record<string, unknown>) {
    return this.api.get(`/ingestion-tasks/${taskId}/reconciliations`, { params }).then(r => r.data.data)
  }

  getReconciliation(reconId: string) {
    return this.api.get(`/ingestion-tasks/reconciliations/${reconId}`).then(r => r.data.data)
  }

  triggerReconciliation(taskId: string, level: 'L1' | 'L2' | 'L3') {
    return this.api.post(`/ingestion-tasks/${taskId}/reconcile`, { level }).then(r => r.data.data)
  }

  repairReconciliation(reconId: string, segment?: string) {
    return this.api.post(`/ingestion-tasks/reconciliations/${reconId}/repair`, { segment }).then(r => r.data.data)
  }

  // ── Schema 变更审计 ──
  getSchemaChanges(taskId: string) {
    return this.api.get(`/ingestion-tasks/${taskId}/schema-changes`).then(r => r.data.data)
  }

  // ── 隔离区 ──
  getQuarantine(taskId: string, params?: Record<string, unknown>) {
    return this.api.get(`/ingestion-tasks/${taskId}/quarantine`, { params }).then(r => r.data.data)
  }

  getQuarantineStats(taskId: string) {
    return this.api.get(`/ingestion-tasks/${taskId}/quarantine/stats`).then(r => r.data.data)
  }

  retryQuarantine(quarantineId: string) {
    return this.api.post(`/ingestion-tasks/quarantine/${quarantineId}/retry`).then(r => r.data.data)
  }

  ignoreQuarantine(quarantineId: string) {
    return this.api.post(`/ingestion-tasks/quarantine/${quarantineId}/ignore`).then(r => r.data.data)
  }

  // ── 定时调度 ──
  previewCron(cronExpression: string) {
    return this.api.post('/ingestion-tasks/preview-cron', { cronExpression }).then(r => r.data.data)
  }

  // ── SSE 进度流 ──
  streamProgress(
    batchId: string,
    onProgress: (data: {
      pct: number
      step: string
      status: string
      startedAt: string | null
      recordCount: number
      successCount: number
      failCount: number
      skipCount: number
      sourceSignature: string | null
    }) => void,
    onDone: () => void,
  ): EventSource {
    const base = this.api.defaults.baseURL || ''
    const es = new EventSource(`${base}/ingestion-tasks/batches/${batchId}/stream`)
    es.onmessage = (e) => {
      const d = JSON.parse(e.data)
      onProgress(d)
      if (d.status === 'success' || d.status === 'failed' || d.status === 'cancelled') {
        es.close()
        onDone()
      }
    }
    es.onerror = () => { es.close(); onDone() }
    return es
  }
}

export const ingestionService = new IngestionService()
