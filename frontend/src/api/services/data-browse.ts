import api from '../client'
import type { DataTableResponse } from '../types'

export class DataBrowseService {
  getTables(schema?: string, system?: string): Promise<{ items: DataTableResponse[]; total: number }> {
    return api.get('/data-browse/tables', { params: { schema, system } }).then(r => r.data.data)
  }

  getSample(table: string, limit?: number): Promise<{ columns: string[]; rows: Record<string, unknown>[] }> {
    return api.get(`/data-browse/sample/${table}`, { params: { limit } }).then(r => r.data.data)
  }
}

export const dataBrowseService = new DataBrowseService()
