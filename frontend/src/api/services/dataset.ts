import api from '../client'
import type {
  DatasetResponse, DatasetFieldResponse, DataTableResponse, PaginatedData,
  DatasetFieldUpdate, DatasetFieldBatchUpdate,
  SampleDataResponse, AgentCheckResponse,
} from '../types'

export class DatasetService {
  // ── Dataset CRUD ──
  getList(params?: Record<string, unknown>): Promise<PaginatedData<DatasetResponse>> {
    return api.get('/datasets', { params }).then(r => r.data.data)
  }

  get(id: string): Promise<DatasetResponse> {
    return api.get(`/datasets/${id}`).then(r => r.data.data)
  }

  create(data: Record<string, unknown>): Promise<DatasetResponse> {
    return api.post('/datasets', data).then(r => r.data.data)
  }

  update(id: string, data: Record<string, unknown>): Promise<DatasetResponse> {
    return api.put(`/datasets/${id}`, data).then(r => r.data.data)
  }

  delete(id: string): Promise<unknown> {
    return api.delete(`/datasets/${id}`).then(r => r.data)
  }

  // ── Fields ──
  getFields(datasetId: string): Promise<{ items: DatasetFieldResponse[]; total: number }> {
    return api.get(`/datasets/${datasetId}/fields`).then(r => r.data.data)
  }

  // T4: 字段 CRUD
  updateField(datasetId: string, fieldId: string, data: DatasetFieldUpdate): Promise<DatasetFieldResponse> {
    return api.put(`/datasets/${datasetId}/fields/${fieldId}`, data).then(r => r.data.data)
  }

  batchUpdateFields(datasetId: string, data: DatasetFieldBatchUpdate): Promise<{ updated: number }> {
    return api.put(`/datasets/${datasetId}/fields/batch`, data).then(r => r.data.data)
  }

  deleteField(datasetId: string, fieldId: string): Promise<unknown> {
    return api.delete(`/datasets/${datasetId}/fields/${fieldId}`).then(r => r.data)
  }

  // ── Tables ──
  getTables(datasetId: string): Promise<{ items: DataTableResponse[]; total: number }> {
    return api.get(`/datasets/${datasetId}/tables`).then(r => r.data.data)
  }

  // T4: 样例数据
  getSampleData(datasetId: string, limit?: number): Promise<SampleDataResponse> {
    return api.get(`/datasets/${datasetId}/sample-data`, { params: { limit } }).then(r => r.data.data)
  }

  // T5: 空值率统计
  computeNullRates(datasetId: string): Promise<{ updated: number }> {
    return api.post(`/datasets/${datasetId}/compute-null-rates`).then(r => r.data.data)
  }

  // T6: Agent 可用性检查
  checkAgent(datasetId: string): Promise<AgentCheckResponse> {
    return api.post(`/datasets/${datasetId}/check-agent`).then(r => r.data.data)
  }
}

export const datasetService = new DatasetService()
