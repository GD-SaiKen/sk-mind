import api from '../client'
import type {
  CatalogDatasetItem, CatalogDatasetListResponse,
  CatalogFieldItem, CatalogFieldListResponse,
  CatalogDatasetDetail, CatalogStats,
} from '../types'

export class CatalogService {
  // 数据集目录（业务视角列表）
  getDatasets(params?: {
    keyword?: string
    source?: string
    domain?: string
    isAgentAccessible?: boolean
    page?: number
    pageSize?: number
  }): Promise<CatalogDatasetListResponse> {
    return api.get('/catalog/datasets', { params }).then(r => r.data.data)
  }

  // 字段目录（跨表搜索）
  getFields(params?: {
    keyword?: string
    datasetId?: string
    dataType?: string
    isSensitive?: boolean
    page?: number
    pageSize?: number
  }): Promise<CatalogFieldListResponse> {
    return api.get('/catalog/fields', { params }).then(r => r.data.data)
  }

  // 统计
  getStats(): Promise<CatalogStats> {
    return api.get('/catalog/stats').then(r => r.data.data)
  }

  // 数据集详情（业务视角）
  getDatasetDetail(id: string): Promise<CatalogDatasetDetail> {
    return api.get(`/catalog/datasets/${id}`).then(r => r.data.data)
  }
}

export const catalogService = new CatalogService()
