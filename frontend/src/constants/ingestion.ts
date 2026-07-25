// 同步引擎优化：状态枚举中文映射常量
// 对应后端方案 08-同步引擎优化方案-d2a对标 / 前端方案 09

/** 对账状态：pass 一致 / warning 有差异 / failed 不一致 / repaired 已修复 */
export const RECON_STATUS_LABELS: Record<string, string> = {
  pass: '一致',
  warning: '有差异',
  failed: '不一致',
  repaired: '已修复',
}

/** Schema 变更类型：added 新增列 / removed 删除列 / type_changed 类型变更 */
export const SCHEMA_CHANGE_LABELS: Record<string, string> = {
  added: '新增列',
  removed: '删除列',
  type_changed: '类型变更',
}

/** 隔离区拒绝原因 */
export const REJECTION_LABELS: Record<string, string> = {
  null_pk: 'PK为空',
  dup_in_batch: '批次内重复',
  type_error: '类型错误',
  write_error: '写入失败',
}

/** 隔离区记录状态 */
export const QUARANTINE_STATUS_LABELS: Record<string, string> = {
  pending: '待处理',
  retried: '已重试',
  resolved: '已修复',
  ignored: '已忽略',
}

/** 对账级别：L1 轻量 / L2 深度 / L3 行级 */
export const CHECK_LEVEL_LABELS: Record<string, string> = {
  L1: '轻量',
  L2: '深度',
  L3: '行级',
}
