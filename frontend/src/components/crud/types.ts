// ==================== 操作按钮 ====================

/** 单个操作按钮配置 */
export interface ActionButton {
  /** 按钮文字 */
  label: string
  /** 按钮类型 */
  type?: 'primary' | 'success' | 'warning' | 'danger' | 'info' | 'text'
  /** 是否显示为链接样式 */
  link?: boolean
  /** 点击回调，接收当前行数据 */
  onClick: (row: Record<string, any>, index: number) => void
  /** 是否隐藏（动态控制） */
  hidden?: (row: Record<string, any>) => boolean
  /** 图标名（element-plus icon） */
  icon?: string
}

// ==================== 列类型枚举 ====================

export type ColumnType =
  | 'selection'   // 多选框（固定在左侧）
  | 'index'        // 序号列（固定在左侧）
  | 'text'         // 普通文本
  | 'image'        // 图片（带预览）
  | 'tag'          // 标签
  | 'date'         // 日期（自动格式化）
  | 'custom'       // 自定义插槽（外部传入 #col-{prop}）
  | 'action'       // 操作列（固定在右侧）

// ==================== 列 Schema ====================

/** 基础列属性 */
interface BaseColumn {
  /** 列类型 */
  type: ColumnType
  /** 列标题 */
  label?: string
  /** 字段名（selection / index / action 可不传） */
  prop?: string
  /** 列宽 */
  width?: string | number
  /** 最小列宽 */
  minWidth?: string | number
  /** 对齐方式 */
  align?: 'left' | 'center' | 'right'
  /** 是否可排序 */
  sortable?: boolean | 'custom'
  /** 是否显示 tooltip 溢出文本 */
  showOverflowTooltip?: boolean
  /** 格式化函数 */
  formatter?: (value: any, row: Record<string, any>, index: number) => string
  /** 列附加 class */
  className?: string
}

/** 选择列 */
export interface SelectionColumn extends BaseColumn {
  type: 'selection'
  /** 已选中的行数据（v-model） */
  modelValue?: any[]
  /** 选择变化回调 */
  onSelectionChange?: (rows: any[]) => void
}

/** 序号列 */
export interface IndexColumn extends BaseColumn {
  type: 'index'
  /** 起始序号，默认 1（分页场景自动 + (page-1) * pageSize） */
  startIndex?: number
}

/** 文本列 */
export interface TextColumn extends BaseColumn {
  type: 'text'
  prop: string
}

/** 图片列 */
export interface ImageColumn extends BaseColumn {
  type: 'image'
  prop: string
  /** 缩略图宽度 */
  imageWidth?: number
  /** 缩略图高度 */
  imageHeight?: number
  /** 预览图片列表字段（默认取 prop，可配数组字段） */
  previewSrcList?: string
}

/** 标签列 */
export interface TagColumn extends BaseColumn {
  type: 'tag'
  prop: string
  /** 标签类型映射：值 -> 类型 */
  tagMap?: Record<string, '' | 'success' | 'warning' | 'danger' | 'info'>
  /** 统一的标签类型 */
  tagType?: '' | 'success' | 'warning' | 'danger' | 'info'
  /** 是否圆角 */
  round?: boolean
  /** 点击回调 */
  onClick?: (value: any, row: Record<string, any>) => void
}

/** 日期列 */
export interface DateColumn extends BaseColumn {
  type: 'date'
  prop: string
  /** 日期格式，默认 'YYYY-MM-DD HH:mm:ss' */
  format?: string
}

/** 自定义列 */
export interface CustomColumn extends BaseColumn {
  type: 'custom'
  prop: string
  /** 插槽名（默认 col-{prop}） */
  slotName?: string
}

/** 操作列 */
export interface ActionColumn extends BaseColumn {
  type: 'action'
  /** 操作按钮列表 */
  buttons: ActionButton[]
  /** 超出此数量后折叠到"更多"下拉，默认 3 */
  maxVisible?: number
}

// ==================== 联合类型 ====================

export type ColumnSchema =
  | SelectionColumn
  | IndexColumn
  | TextColumn
  | ImageColumn
  | TagColumn
  | DateColumn
  | CustomColumn
  | ActionColumn

// ==================== 分页配置 ====================

export interface PaginationConfig {
  /** 当前页（支持 v-model） */
  page?: number
  /** 每页条数 */
  pageSize?: number
  /** 总条数 */
  total: number
  /** 布局，默认 'total, sizes, prev, pager, next, jumper' */
  layout?: string
  /** 每页条数选项 */
  pageSizes?: number[]
  /** 背景色 */
  background?: boolean
  /** 是否小型 */
  small?: boolean
  /** 是否禁用 */
  disabled?: boolean
  /** 页码变化 */
  onPageChange?: (page: number) => void
  /** 每页条数变化 */
  onSizeChange?: (size: number) => void
}

// ==================== 表格 Props ====================

export interface TableProps {
  /** 列配置 */
  columns: ColumnSchema[]
  /** 表格数据 */
  data: Record<string, any>[]
  /** 表格尺寸 */
  size?: '' | 'small' | 'large'
  /** 加载状态 */
  loading?: boolean
  /** 是否显示边框 */
  border?: boolean
  /** 是否斑马纹 */
  stripe?: boolean
  /** 行 key */
  rowKey?: string
  /** 最大高度 */
  maxHeight?: string | number
  /** 表头行高亮 */
  highlightCurrentRow?: boolean
  /** 行点击 */
  onRowClick?: (row: Record<string, any>, column: any, event: Event) => void
}

// ==================== 分页组件 Props ====================

export interface PaginationProps {
  /** 分页配置 */
  config: PaginationConfig
  /** 是否固定在底部 */
  fixed?: boolean
}
