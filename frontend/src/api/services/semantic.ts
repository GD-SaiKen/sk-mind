import api from '../client'
import type {
  SemanticObject, SemanticProperty, DataMappingItem, SemanticStats,
  SemanticRelation,
  PaginatedData,
} from '../types'

export class SemanticService {
  // ── SemanticObject CRUD ──
  getObjects(params?: {
    keyword?: string
    objectType?: string
    domain?: string
    status?: string
    page?: number
    pageSize?: number
  }): Promise<PaginatedData<SemanticObject>> {
    return api.get('/semantic/objects', { params }).then(r => r.data.data)
  }

  getObject(id: string): Promise<SemanticObject> {
    return api.get(`/semantic/objects/${id}`).then(r => r.data.data)
  }

  createObject(data: Record<string, unknown>): Promise<SemanticObject> {
    return api.post('/semantic/objects', data).then(r => r.data.data)
  }

  updateObject(id: string, data: Record<string, unknown>): Promise<SemanticObject> {
    return api.put(`/semantic/objects/${id}`, data).then(r => r.data.data)
  }

  deleteObject(id: string): Promise<unknown> {
    return api.delete(`/semantic/objects/${id}`).then(r => r.data)
  }

  // ── SemanticProperty CRUD ──
  getProperties(params?: {
    semanticObjectId?: string
    propertyType?: string
    page?: number
    pageSize?: number
  }): Promise<{ items: SemanticProperty[]; total: number }> {
    return api.get('/semantic/properties', { params }).then(r => r.data.data)
  }

  createProperty(data: Record<string, unknown>): Promise<SemanticProperty> {
    return api.post('/semantic/properties', data).then(r => r.data.data)
  }

  updateProperty(id: string, data: Record<string, unknown>): Promise<SemanticProperty> {
    return api.put(`/semantic/properties/${id}`, data).then(r => r.data.data)
  }

  deleteProperty(id: string): Promise<unknown> {
    return api.delete(`/semantic/properties/${id}`).then(r => r.data)
  }

  // ── DataMapping CRUD ──
  getMappings(params?: {
    mappingType?: string
    status?: string
    page?: number
    pageSize?: number
  }): Promise<PaginatedData<DataMappingItem>> {
    return api.get('/semantic/mappings', { params }).then(r => r.data.data)
  }

  createMapping(data: Record<string, unknown>): Promise<DataMappingItem> {
    return api.post('/semantic/mappings', data).then(r => r.data.data)
  }

  updateMapping(id: string, data: Record<string, unknown>): Promise<DataMappingItem> {
    return api.put(`/semantic/mappings/${id}`, data).then(r => r.data.data)
  }

  deleteMapping(id: string): Promise<unknown> {
    return api.delete(`/semantic/mappings/${id}`).then(r => r.data)
  }

  // ── SemanticRelation CRUD ──
  getRelations(params?: {
    keyword?: string
    relationType?: string
    subjectObjectId?: string
    objectObjectId?: string
    agentEnabled?: boolean
    status?: string
    page?: number
    pageSize?: number
  }): Promise<PaginatedData<SemanticRelation>> {
    return api.get('/semantic/relations', { params }).then(r => r.data.data)
  }

  getRelation(id: string): Promise<SemanticRelation> {
    return api.get(`/semantic/relations/${id}`).then(r => r.data.data)
  }

  createRelation(data: Record<string, unknown>): Promise<SemanticRelation> {
    return api.post('/semantic/relations', data).then(r => r.data.data)
  }

  updateRelation(id: string, data: Record<string, unknown>): Promise<SemanticRelation> {
    return api.put(`/semantic/relations/${id}`, data).then(r => r.data.data)
  }

  deleteRelation(id: string): Promise<unknown> {
    return api.delete(`/semantic/relations/${id}`).then(r => r.data)
  }

  // ── Stats ──
  getStats(): Promise<SemanticStats> {
    return api.get('/semantic/stats').then(r => r.data.data)
  }

  // ── Agent Reload ──
  reloadSemantic(source: string = 'mes'): Promise<unknown> {
    return api.post('/agent/reload', null, { params: { source } }).then(r => r.data)
  }
}

export const semanticService = new SemanticService()
