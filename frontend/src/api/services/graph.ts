import api from '../client'
import type {
  GraphEdge, GraphStats, GraphQueryResult,
  PaginatedData,
} from '../types'

export class GraphService {
  // ── 边列表 / 详情 ──
  getEdges(params?: {
    keyword?: string
    relationCode?: string
    status?: string
    generatedBy?: string
    page?: number
    pageSize?: number
  }): Promise<PaginatedData<GraphEdge>> {
    return api.get('/graph/edges', { params }).then(r => r.data.data)
  }

  getEdge(id: string): Promise<GraphEdge> {
    return api.get(`/graph/edges/${id}`).then(r => r.data.data)
  }

  // ── 边生成 ──
  generateEdges(relationCode: string): Promise<{ relationCode: string; generated: number }> {
    return api.post('/graph/edges/generate', null, {
      params: { relationCode },
    }).then(r => r.data.data)
  }

  // ── 状态流转 ──
  confirmEdge(id: string): Promise<GraphEdge> {
    return api.post(`/graph/edges/${id}/confirm`).then(r => r.data.data)
  }

  rejectEdge(id: string): Promise<unknown> {
    return api.post(`/graph/edges/${id}/reject`).then(r => r.data)
  }

  markInsufficient(id: string): Promise<unknown> {
    return api.post(`/graph/edges/${id}/insufficient`).then(r => r.data)
  }

  // ── 路径查询 / 统计 ──
  queryGraph(params?: {
    type?: string
    id?: string
    relationCode?: string
    hops?: number
    minConfidence?: number
    confirmedOnly?: boolean
  }): Promise<GraphQueryResult> {
    return api.get('/graph/query', { params }).then(r => r.data.data)
  }

  getStats(): Promise<GraphStats> {
    return api.get('/graph/stats').then(r => r.data.data)
  }
}

export const graphService = new GraphService()
