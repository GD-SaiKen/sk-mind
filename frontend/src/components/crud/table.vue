<template>
  <div class="table-wrapper">
    <el-table
      ref="tableRef"
      :data="data"
      :size="size"
      v-loading="loading"
      :border="border"
      :stripe="stripe"
      :row-key="rowKey"
      :max-height="maxHeight"
      :height="maxHeight ? undefined : '100%'"
      :highlight-current-row="highlightCurrentRow"
      table-layout="auto"
      @row-click="onRowClick"
      @selection-change="onSelectionChange"
    >
      <template v-for="col in columns" :key="colKey(col)">
        <el-table-column
          v-if="col.type === 'selection'"
          type="selection"
          :width="col.width ?? 50"
          :align="col.align ?? 'center'"
          fixed="left"
          :reserve-selection="true"
        />

        <el-table-column
          v-else-if="col.type === 'index'"
          type="index"
          :label="col.label ?? '序号'"
          :width="col.width ?? 60"
          :align="col.align ?? 'center'"
          fixed="left"
          :index="indexMethod(col)"
        />

        <el-table-column
          v-else-if="col.type === 'image'"
          :prop="col.prop"
          :label="col.label"
          :width="col.width"
          :min-width="col.minWidth ?? 100"
          :align="col.align ?? 'center'"
          :sortable="col.sortable"
        >
          <template #default="{ row }">
            <el-image
              v-if="row[col.prop]"
              :src="row[col.prop]"
              :style="{ width: (col.imageWidth ?? 40) + 'px', height: (col.imageHeight ?? 40) + 'px' }"
              fit="cover"
              :preview-src-list="getPreviewList(row, col)"
              :preview-teleported="true"
              lazy
            />
            <span v-else class="text-muted">-</span>
          </template>
        </el-table-column>

        <el-table-column
          v-else-if="col.type === 'tag'"
          :prop="col.prop"
          :label="col.label"
          :width="col.width"
          :min-width="col.minWidth"
          :align="col.align ?? 'center'"
          :sortable="col.sortable"
        >
          <template #default="{ row }">
            <el-tag
              :type="getTagType(row[col.prop], col)"
              :round="col.round ?? false"
              :class="{ 'is-clickable': !!col.onClick }"
              @click="col.onClick?.(row[col.prop], row)"
            >
              {{ col.formatter ? col.formatter(row[col.prop], row, 0) : row[col.prop] }}
            </el-tag>
          </template>
        </el-table-column>

        <el-table-column
          v-else-if="col.type === 'date'"
          :prop="col.prop"
          :label="col.label"
          :width="col.width"
          :min-width="col.minWidth ?? 170"
          :align="col.align ?? 'center'"
          :sortable="col.sortable"
          :show-overflow-tooltip="col.showOverflowTooltip"
          :formatter="dateFormatter(col)"
        />

        <el-table-column
          v-else-if="col.type === 'custom'"
          :prop="col.prop"
          :label="col.label"
          :width="col.width"
          :min-width="col.minWidth"
          :align="col.align"
          :sortable="col.sortable"
          :show-overflow-tooltip="col.showOverflowTooltip"
        >
          <template #default="scope">
            <slot
              :name="col.slotName ?? `col-${col.prop}`"
              v-bind="scope"
            />
          </template>
        </el-table-column>

        <el-table-column
          v-else-if="col.type === 'action'"
          :label="col.label ?? '操作'"
          :width="col.width ?? actionColWidth(col)"
          :min-width="col.minWidth"
          :align="col.align ?? 'center'"
          fixed="right"
        >
          <template #default="{ row, $index }">
            <div class="action-btns">
              <template
                v-for="(btn, i) in visibleButtons(col, row)"
                :key="i"
              >
                <el-tooltip
                  v-if="btn.icon"
                  :content="btn.tooltip ?? btn.label"
                  placement="top"
                  :show-after="400"
                >
                  <el-button
                    link
                    :type="btn.type ?? 'primary'"
                    @click="btn.onClick(row, $index)"
                  >
                    <el-icon>
                      <component :is="btn.icon" />
                    </el-icon>
                  </el-button>
                </el-tooltip>
                <el-button
                  v-else
                  link
                  :type="btn.type ?? 'primary'"
                  @click="btn.onClick(row, $index)"
                >
                  {{ btn.label }}
                </el-button>
              </template>

              <el-dropdown
                v-if="hasMore(col, row)"
                trigger="hover"
                :teleported="true"
              >
                <el-button link type="primary">
                  更多
                  <el-icon class="el-icon--right">
                    <ArrowDown />
                  </el-icon>
                </el-button>
                <template #dropdown>
                  <el-dropdown-menu>
                    <el-dropdown-item
                      v-for="(btn, i) in hiddenButtons(col, row)"
                      :key="i"
                      @click="btn.onClick(row, $index)"
                    >
                      <el-icon v-if="btn.icon">
                        <component :is="btn.icon" />
                      </el-icon>
                      {{ btn.label }}
                    </el-dropdown-item>
                  </el-dropdown-menu>
                </template>
              </el-dropdown>
            </div>
          </template>
        </el-table-column>

        <el-table-column
          v-else
          :prop="col.prop"
          :label="col.label"
          :width="col.width"
          :min-width="col.minWidth ?? 120"
          :align="col.align"
          :sortable="col.sortable"
          :show-overflow-tooltip="col.showOverflowTooltip ?? true"
          :formatter="col.formatter ? (r: any, _c: any, v: any, i: number) => col.formatter!(v, r, i) : undefined"
        />
      </template>
    </el-table>
  </div>
</template>

<script setup lang="ts">
import { computed, ref } from 'vue'
import { ArrowDown } from '@element-plus/icons-vue'
import type {
  ActionButton,
  ActionColumn,
  ColumnSchema,
  DateColumn,
  ImageColumn,
  IndexColumn,
  SelectionColumn,
  TableProps,
  TagColumn,
} from './types'

const props = withDefaults(defineProps<TableProps>(), {
  size: '' as const,
  loading: false,
  border: true,
  stripe: true,
  rowKey: 'id',
})

const emit = defineEmits<{
  'update:selection': [rows: any[]]
  'selection-change': [rows: any[]]
}>()

const tableRef = ref()

defineExpose({
  getTableRef: () => tableRef.value,
  clearSelection: () => tableRef.value?.clearSelection(),
  toggleRowSelection: (row: any, selected?: boolean) => tableRef.value?.toggleRowSelection(row, selected),
  sort: (prop: string, order: string) => tableRef.value?.sort(prop, order),
})

function onSelectionChange(rows: any[]) {
  emit('update:selection', rows)
  emit('selection-change', rows)
  const selCol = props.columns.find(c => c.type === 'selection') as SelectionColumn | undefined
  selCol?.onSelectionChange?.(rows)
}

function indexMethod(col: IndexColumn) {
  return (i: number) => (col.startIndex ?? 1) + i
}

function colKey(col: ColumnSchema): string {
  if (col.type === 'selection') return '_selection'
  if (col.type === 'index') return '_index'
  if (col.type === 'action') return '_action'
  return (col as any).prop ?? ''
}

function getPreviewList(row: Record<string, any>, col: ImageColumn): string[] {
  const src = col.previewSrcList ? row[col.previewSrcList] : row[col.prop]
  if (Array.isArray(src)) return src
  return src ? [src] : []
}

function getTagType(value: any, col: TagColumn): '' | 'success' | 'warning' | 'danger' | 'info' {
  if (col.tagMap && typeof value === 'string') {
    return col.tagMap[value] ?? col.tagType ?? ''
  }
  return col.tagType ?? ''
}

function dateFormatter(col: DateColumn) {
  const fmt = col.format ?? 'YYYY-MM-DD HH:mm:ss'
  return (_row: any, _column: any, cellValue: any, _index: number) => {
    if (!cellValue) return '-'
    const d = new Date(cellValue)
    if (isNaN(d.getTime())) return String(cellValue)

    const pad = (n: number) => String(n).padStart(2, '0')
    const map: Record<string, string> = {
      YYYY: String(d.getFullYear()),
      MM: pad(d.getMonth() + 1),
      DD: pad(d.getDate()),
      HH: pad(d.getHours()),
      mm: pad(d.getMinutes()),
      ss: pad(d.getSeconds()),
    }
    return fmt.replace(/YYYY|MM|DD|HH|mm|ss/g, m => map[m])
  }
}

function visibleButtons(col: ActionColumn, row: Record<string, any>): ActionButton[] {
  const all = col.buttons.filter(b => !b.hidden?.(row))
  const max = col.maxVisible ?? 3
  return all.slice(0, max)
}

function hasMore(col: ActionColumn, row: Record<string, any>): boolean {
  const all = col.buttons.filter(b => !b.hidden?.(row))
  const max = col.maxVisible ?? 3
  return all.length > max
}

function hiddenButtons(col: ActionColumn, row: Record<string, any>): ActionButton[] {
  const all = col.buttons.filter(b => !b.hidden?.(row))
  const max = col.maxVisible ?? 3
  return all.slice(max)
}

function actionColWidth(col: ActionColumn): number {
  const count = Math.min(col.buttons.length, col.maxVisible ?? 3)
  const base = count * 56 + 24
  return col.buttons.length > (col.maxVisible ?? 3) ? base + 60 : base
}
</script>

<style lang="scss" scoped>
.table-wrapper {
  display: flex;
  flex: 1;
  min-height: 0;
  overflow: hidden;
}

.table-wrapper :deep(.el-table) {
  display: flex;
  flex-direction: column;
}

.table-wrapper :deep(.el-table__inner-wrapper) {
  display: flex;
  flex: 1;
  flex-direction: column;
  overflow: hidden;
}

.table-wrapper :deep(.el-table__header-wrapper) {
  flex-shrink: 0;
}

.table-wrapper :deep(.el-table__body-wrapper) {
  flex: 1;
  overflow-y: auto;
}

.text-muted {
  color: #c0c4cc;
}

.action-btns {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 4px;
  flex-wrap: nowrap;
}

.is-clickable {
  cursor: pointer;
}
</style>
