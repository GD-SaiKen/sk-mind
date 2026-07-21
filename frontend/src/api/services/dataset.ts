import api from '../client'
import type { DatasetResponse, DatasetFieldResponse, DataTableResponse, PaginatedData } from '../types'

export class DatasetService {
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

  getFields(datasetId: string): Promise<{ items: DatasetFieldResponse[]; total: number }> {
    return api.get(`/datasets/${datasetId}/fields`).then(r => r.data.data)
  }

  getTables(datasetId: string): Promise<{ items: DataTableResponse[]; total: number }> {
    return api.get(`/datasets/${datasetId}/tables`).then(r => r.data.data)
  }
}

export const datasetService = new DatasetService()
