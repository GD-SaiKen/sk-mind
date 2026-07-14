import api from '../client'

export class DataSourceService {
  getList(params?: Record<string, unknown>) {
    return api.get('/data-sources', { params }).then(r => r.data.data)
  }
  get(id: string) {
    return api.get(`/data-sources/${id}`).then(r => r.data.data)
  }
  create(data: Record<string, unknown>) {
    return api.post('/data-sources', data).then(r => r.data.data)
  }
  update(id: string, data: Record<string, unknown>) {
    return api.put(`/data-sources/${id}`, data).then(r => r.data.data)
  }
  delete(id: string) {
    return api.delete(`/data-sources/${id}`).then(r => r.data)
  }
}

export const dataSourceService = new DataSourceService()
