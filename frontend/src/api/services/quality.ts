import api from '../client'
import type { QualityRule, QualityRun, QualityIssue, QualityStats, PaginatedData } from '../types'

export class QualityService {
  getRules(params?: Record<string, unknown>): Promise<PaginatedData<QualityRule>> {
    return api.get('/quality/rules', { params }).then(r => r.data.data)
  }

  getRule(id: string): Promise<QualityRule> {
    return api.get(`/quality/rules/${id}`).then(r => r.data.data)
  }

  createRule(data: Record<string, unknown>): Promise<QualityRule> {
    return api.post('/quality/rules', data).then(r => r.data.data)
  }

  updateRule(id: string, data: Record<string, unknown>): Promise<QualityRule> {
    return api.put(`/quality/rules/${id}`, data).then(r => r.data.data)
  }

  executeRule(id: string): Promise<unknown> {
    return api.post(`/quality/rules/${id}/execute`).then(r => r.data.data)
  }

  getRuns(params?: Record<string, unknown>): Promise<PaginatedData<QualityRun>> {
    return api.get('/quality/runs', { params }).then(r => r.data.data)
  }

  getIssues(params?: Record<string, unknown>): Promise<PaginatedData<QualityIssue>> {
    return api.get('/quality/issues', { params }).then(r => r.data.data)
  }

  updateIssueStatus(id: string, status: string): Promise<QualityIssue> {
    return api.put(`/quality/issues/${id}/status`, { status }).then(r => r.data.data)
  }

  getStats(): Promise<QualityStats> {
    return api.get('/quality/stats').then(r => r.data.data)
  }
}

export const qualityService = new QualityService()
