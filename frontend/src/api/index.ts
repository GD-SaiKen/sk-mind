// API 统一导出
export { default as api } from './client';
export { authService } from './services/auth';
export { ingestionService } from './services/ingestion';
export { dataSourceService } from './services/data-source';
export type {
  LoginParams,
  IngestionTask,
  IngestionBatch,
  BatchProgress,
  ImportError,
  DataSource,
  DataSourceType,
  AccessMethod,
  DataSourceStatus,
  DataSourceFormData,
} from './types';
