import api from '../client'
import type { LineageEdge, LineageStats, PaginatedData } from '../types'

export class LineageService {
  getEdges(params?: Record<string, unknown>): Promise<PaginatedData<LineageEdge>> {
    return api.get('/lineage/edges', { params }).then(r => r.data.data)
  }

  getEdge(id: string): Promise<LineageEdge> {
    return api.get(`/lineage/edges/${id}`).then(r => r.data.data)
  }

  createEdge(data: Record<string, unknown>): Promise<LineageEdge> {
    return api.post('/lineage/edges', data).then(r => r.data.data)
  }

  updateEdge(id: string, data: Record<string, unknown>): Promise<LineageEdge> {
    return api.put(`/lineage/edges/${id}`, data).then(r => r.data.data)
  }

  confirmEdge(id: string): Promise<unknown> {
    return api.post(`/lineage/edges/${id}/confirm`).then(r => r.data.data)
  }

  rejectEdge(id: string): Promise<unknown> {
    return api.post(`/lineage/edges/${id}/reject`).then(r => r.data)
  }

  getStats(): Promise<LineageStats> {
    return api.get('/lineage/stats').then(r => r.data.data)
  }

  queryLineage(params?: Record<string, unknown>): Promise<unknown> {
    return api.get('/lineage/query', { params }).then(r => r.data.data)
  }
}

export const lineageService = new LineageService()
