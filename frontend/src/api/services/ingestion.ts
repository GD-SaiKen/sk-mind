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
}

export const ingestionService = new IngestionService()
