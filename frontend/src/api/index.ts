// API 统一导出
export { default as api } from './client';
export { authService } from './services/auth';
export { ingestionService } from './services/ingestion';
export type {
  LoginParams,
  IngestionTask,
  IngestionBatch,
  BatchProgress,
  ImportError,
} from './types';
