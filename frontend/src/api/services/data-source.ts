import api from '../client'
import type { DataSource, DataSourceFormData } from '../types'

export class DataSourceService {
  getList(params?: Record<string, unknown>) {
    return api.get('/data-sources', { params }).then(r => r.data.data)
  }

  get(id: string) {
    return api.get(`/data-sources/${id}`).then(r => r.data.data)
  }

  create(data: DataSourceFormData) {
    return api.post('/data-sources', data).then(r => r.data.data)
  }

  update(id: string, data: Partial<DataSourceFormData>) {
    return api.put(`/data-sources/${id}`, data).then(r => r.data.data)
  }

  delete(id: string) {
    return api.delete(`/data-sources/${id}`).then(r => r.data)
  }

  pause(id: string) {
    return api.post(`/data-sources/${id}/pause`).then(r => r.data)
  }

  resume(id: string) {
    return api.post(`/data-sources/${id}/resume`).then(r => r.data)
  }

  testConnection(id: string) {
    return api.post(`/data-sources/${id}/test-connection`).then(r => r.data.data)
  }
}

export const dataSourceService = new DataSourceService()
