<template>
  <div class="form-root" :class="[props.className, { 'form-box': box }]">
    <!-- 分区循环 -->
    <template v-for="(section, si) in visibleSections" :key="si">
      <div class="form-section" :class="{ 'is-collapsed': isCollapsed(si) }">
        <!-- 分区标题行 -->
        <div
          class="form-section-header"
          :class="{ 'is-clickable': section.collapsible }"
          @click="section.collapsible && toggleSection(si)"
        >
          <div class="form-section-title-line">
            <span class="form-section-title" v-if="section.title">{{ section.title }}</span>
            <span class="form-section-desc" v-if="section.description">{{ section.description }}</span>
          </div>
          <el-icon v-if="section.collapsible" class="section-toggle-icon">
            <ArrowDown v-if="!collapsedMap[si]" />
            <ArrowRight v-else />
          </el-icon>
        </div>

        <!-- 分区内容 -->
        <transition name="form-section-collapse">
          <div v-show="!isCollapsed(si)" class="form-section-body">
            <!-- 自定义插槽模式 -->
            <slot
              v-if="section.slotName"
              :name="section.slotName"
              :model="currentModel"
            />
            <!-- 字段列表模式 -->
            <template v-else>
              <el-row :gutter="20">
                <template v-for="field in section.fields" :key="field.prop">
                  <el-col
                    v-if="isFieldVisible(field)"
                    :span="fieldColSpan(section, field)"
                  >
                    <el-form-item
                      :prop="field.prop"
                      :rules="(field.rules ?? undefined) as any"
                      :error="fieldErrors[field.prop]"
                      :label-width="props.labelWidth"
                    >
                      <!-- label + 提示图标 -->
                      <template #label>
                        <span class="form-label">
                          <span class="form-label-text">{{ field.label }}</span>
                          <el-tooltip
                            v-if="field.tip"
                            :content="field.tip"
                            placement="top"
                            :show-after="300"
                          >
                            <el-icon class="form-label-tip-icon"><WarningFilled /></el-icon>
                          </el-tooltip>
                        </span>
                      </template>
                      <!-- ===== input ===== -->
                      <el-input
                        v-if="!field.type || field.type === 'input'"
                        :model-value="currentModel[field.prop]"
                        :placeholder="field.placeholder"
                        :disabled="field.disabled || disabled"
                        :readonly="field.readonly"
                        :clearable="field.clearable ?? true"
                        :maxlength="field.maxlength"
                        :show-word-limit="field.showWordLimit"
                        :style="{ width: field.width || '100%' }"
                        @update:model-value="onFieldChange(field, $event)"
                      >
                        <template v-if="field.prefixIcon" #prefix>
                          <el-icon><component :is="field.prefixIcon" /></el-icon>
                        </template>
                        <template v-if="field.suffix || field.suffixIcon" #suffix>
                          <el-icon v-if="field.suffixIcon"><component :is="field.suffixIcon" /></el-icon>
                          <span v-if="field.suffix">{{ field.suffix }}</span>
                        </template>
                      </el-input>

                      <!-- ===== textarea ===== -->
                      <el-input
                        v-else-if="field.type === 'textarea'"
                        type="textarea"
                        :model-value="currentModel[field.prop]"
                        :placeholder="field.placeholder"
                        :disabled="field.disabled || disabled"
                        :readonly="field.readonly"
                        :rows="field.rows ?? 3"
                        :maxlength="field.maxlength"
                        :show-word-limit="field.showWordLimit"
                        :style="{ width: field.width || '100%' }"
                        @update:model-value="onFieldChange(field, $event)"
                      />

                      <!-- ===== select ===== -->
                      <el-select
                        v-else-if="field.type === 'select'"
                        :model-value="currentModel[field.prop]"
                        :placeholder="field.placeholder"
                        :disabled="field.disabled || disabled"
                        :clearable="field.clearable ?? true"
                        :filterable="field.filterable"
                        :multiple="field.multiple"
                        :style="{ width: field.width || '100%' }"
                        @update:model-value="onFieldChange(field, $event)"
                      >
                        <el-option
                          v-for="opt in field.options"
                          :key="String(opt.value)"
                          :label="opt.label"
                          :value="opt.value"
                        />
                      </el-select>

                      <!-- ===== radio ===== -->
                      <el-radio-group
                        v-else-if="field.type === 'radio'"
                        :model-value="currentModel[field.prop]"
                        :disabled="field.disabled || disabled"
                        @update:model-value="onFieldChange(field, $event)"
                      >
                        <el-radio
                          v-for="opt in field.options"
                          :key="String(opt.value)"
                          :value="opt.value"
                        >{{ opt.label }}</el-radio>
                      </el-radio-group>

                      <!-- ===== checkbox ===== -->
                      <el-checkbox-group
                        v-else-if="field.type === 'checkbox'"
                        :model-value="currentModel[field.prop]"
                        :disabled="field.disabled || disabled"
                        @update:model-value="onFieldChange(field, $event)"
                      >
                        <el-checkbox
                          v-for="opt in field.options"
                          :key="String(opt.value)"
                          :value="opt.value"
                          :label="opt.value"
                        >{{ opt.label }}</el-checkbox>
                      </el-checkbox-group>

                      <!-- ===== switch ===== -->
                      <el-switch
                        v-else-if="field.type === 'switch'"
                        :model-value="currentModel[field.prop]"
                        :disabled="field.disabled || disabled"
                        @update:model-value="onFieldChange(field, $event)"
                      />

                      <!-- ===== date ===== -->
                      <el-date-picker
                        v-else-if="field.type === 'date'"
                        :model-value="currentModel[field.prop]"
                        type="date"
                        :placeholder="field.placeholder"
                        :disabled="field.disabled || disabled"
                        :clearable="field.clearable ?? true"
                        :format="field.format ?? 'YYYY-MM-DD'"
                        :value-format="field.valueFormat ?? 'YYYY-MM-DD'"
                        :style="{ width: field.width || '100%' }"
                        @update:model-value="onFieldChange(field, $event)"
                      />

                      <!-- ===== number ===== -->
                      <el-input-number
                        v-else-if="field.type === 'number'"
                        :model-value="currentModel[field.prop]"
                        :placeholder="field.placeholder"
                        :disabled="field.disabled || disabled"
                        :min="field.min"
                        :max="field.max"
                        :step="field.step ?? 1"
                        :style="{ width: field.width || '100%' }"
                        @update:model-value="onFieldChange(field, $event)"
                      />

                      <!-- ===== readonly（详情展示）===== -->
                      <div
                        v-else-if="field.type === 'readonly'"
                        class="form-readonly"
                        :style="{ width: field.width || '100%' }"
                      >
                        <span v-if="field.formatter">
                          {{ field.formatter(currentModel[field.prop], currentModel) }}
                        </span>
                        <span v-else>{{ currentModel[field.prop] ?? '-' }}</span>
                      </div>

                      <!-- ===== custom 插槽 ===== -->
                      <slot
                        v-else-if="field.type === 'custom'"
                        :name="field.slotName ?? `form-${field.prop}`"
                        :value="currentModel[field.prop]"
                        :model="currentModel"
                        :field="field"
                      />

                    </el-form-item>
                  </el-col>
                </template>
              </el-row>
            </template>
          </div>
        </transition>
      </div>
    </template>
  </div>
</template>

<script setup lang="ts">
import { computed, reactive, watch } from 'vue'
import { ArrowDown, ArrowRight, WarningFilled } from '@element-plus/icons-vue'
import type { FormField, FormProps } from './types'

const props = withDefaults(defineProps<FormProps>(), {
  labelWidth: '100px',
  labelPosition: 'left',
  size: '' as const,
  disabled: false,
  box: false,
  className: '',
})

const emit = defineEmits<{
  'update:modelValue': [value: Record<string, any>]
}>()

const currentModel = computed(() => props.modelValue)

const fieldErrors = reactive<Record<string, string>>({})

// ---- 折叠 ----
const collapsedMap = reactive<Record<number, boolean>>({})
watch(() => props.sections, (sections) => {
  sections.forEach((s, i) => {
    if (s.collapsible) collapsedMap[i] = s.defaultCollapsed ?? false
  })
}, { immediate: true })

function isCollapsed(idx: number) { return collapsedMap[idx] ?? false }
function toggleSection(idx: number) { collapsedMap[idx] = !collapsedMap[idx] }

// ---- 可见分区 ----
const visibleSections = computed(() =>
  props.sections.filter(s => {
    if (typeof s.hidden === 'function') return !s.hidden(currentModel.value)
    return !s.hidden
  })
)

// ---- 可见字段 ----
function isFieldVisible(field: FormField): boolean {
  if (typeof field.hidden === 'function') return !field.hidden(currentModel.value)
  return !field.hidden
}

// ---- 列宽 ----
function colSpan(section: { cols?: number }): number {
  return Math.floor(24 / (section.cols ?? 1))
}

// 字段级 colSpan 优先于分区级 col
function fieldColSpan(section: { cols?: number }, field: { colSpan?: number }): number {
  if (field.colSpan) {
    return Math.floor((24 / (section.cols ?? 1)) * field.colSpan)
  }
  return colSpan(section)
}

// ---- 字段值变化 ----
function onFieldChange(field: FormField, val: any) {
  const newModel = { ...currentModel.value, [field.prop]: val }
  emit('update:modelValue', newModel)
  field.onChange?.(val, newModel)
}

// ---- 对外方法 ----
function validate(): Promise<boolean> {
  let valid = true
  Object.keys(fieldErrors).forEach(k => delete fieldErrors[k])
  for (const section of props.sections) {
    if (typeof section.hidden === 'function' ? section.hidden(currentModel.value) : section.hidden) continue
    for (const field of section.fields) {
      if (!isFieldVisible(field) || !field.rules) continue
      const rules = Array.isArray(field.rules) ? field.rules : [field.rules]
      for (const rule of rules) {
        const val = currentModel.value[field.prop]
        if (rule.required && (val === undefined || val === null || val === '')) {
          fieldErrors[field.prop] = rule.message ?? `${field.label ?? field.prop} 不能为空`
          valid = false; break
        }
        if (rule.min !== undefined && typeof val === 'string' && val.length < rule.min) {
          fieldErrors[field.prop] = rule.message ?? `${field.label ?? field.prop} 长度不能小于 ${rule.min}`
          valid = false; break
        }
        if (rule.max !== undefined && typeof val === 'string' && val.length > rule.max) {
          fieldErrors[field.prop] = rule.message ?? `${field.label ?? field.prop} 长度不能大于 ${rule.max}`
          valid = false; break
        }
      }
    }
  }
  return Promise.resolve(valid)
}

function getModel(): Record<string, any> { return { ...currentModel.value } }
function clearErrors() { Object.keys(fieldErrors).forEach(k => delete fieldErrors[k]) }

defineExpose({ validate, getModel, clearErrors })
</script>

<style lang="scss" scoped>
.form-root {
  display: flex;
  flex-direction: column;
  flex: 1;
  min-height: 0;
}

.form-root.form-box {
  background: #fff;
  border-radius: 6px;
  border: 1px solid #ebeef5;
  padding: 20px 24px;
}

// ===== 分区 =====
.form-section {
  margin-bottom: 24px;

  &:last-child { margin-bottom: 0; }
}

.form-section-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 0 12px;
  margin-bottom: 12px;
  border-bottom: 1px solid #f0f0f0;

  &.is-clickable {
    cursor: pointer;
    user-select: none;
    &:hover .form-section-title { color: #409eff; }
  }
}

.form-section-title-line {
  display: flex;
  align-items: baseline;
  gap: 8px;
}

.form-section-title {
  font-size: 14px;
  font-weight: 600;
  color: #303133;
  transition: color 0.2s;
}

.form-section-desc {
  font-size: 12px;
  color: #909399;
}

.section-toggle-icon {
  font-size: 14px;
  color: #909399;
}

.form-section-body {
  padding-top: 4px;

  :deep(.el-col) {
    margin-bottom: 22px;
  }

  :deep(.el-form-item) {
    margin-bottom: 0;
  }

  :deep(.el-form-item__label) {
    align-items: flex-start;
    justify-content: flex-end;
    text-align: right;
  }
}

// 折叠过渡
.form-section-collapse-enter-active,
.form-section-collapse-leave-active {
  transition: all 0.25s ease;
  overflow: hidden;
}

.form-section-collapse-enter-from,
.form-section-collapse-leave-to {
  opacity: 0;
  max-height: 0;
  margin-top: -12px;
}

// ===== 小元素 =====
.form-readonly {
  font-size: 14px;
  color: #303133;
  line-height: 32px;
  padding: 0 4px;
}

// ===== label 提示图标 =====
.form-label {
  display: inline-flex;
  align-items: flex-start;
  gap: 3px;
}

.form-label-text {
  text-align: right;
}

.form-label-tip-icon {
  font-size: 13px;
  color: $color-warning;
  cursor: help;
  margin-top: 2px;

  &:hover {
    opacity: 0.8;
  }
}
</style>
