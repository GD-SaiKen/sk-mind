<template>
  <div class="page-layout">
    <Index
      title="语义模型"
      :breadcrumb="[{ label: '首页', to: '/' }, { label: '语义模型' }]"
      description="维护业务对象、属性、语义关系和数据映射，为 Agent 提供业务语义理解能力。"
    >
      <template #extra>
        <el-tag type="warning" size="small" style="margin-right:8px">数据来源: YAML</el-tag>
        <el-button size="small" :icon="Refresh" @click="handleReload" :loading="reloading">重新加载</el-button>
      </template>
    </Index>

    <TabNav v-model="activeTab" :tabs="tabs" />

    <el-row :gutter="16" class="stat-row">
      <el-col :span="6">
        <el-card shadow="never" class="info-card">
          <div class="info-card-header">
            <div class="info-card-icon bg-indigo"><el-icon :size="16"><Service /></el-icon></div>
            <span class="info-card-label">业务对象</span>
            <span class="subtag">已建模</span>
          </div>
          <div class="val-row"><span class="val">{{ stats?.totalObjects ?? 0 }}</span><span class="badge neutral">活跃 {{ stats?.activeObjects ?? 0 }}</span></div>
          <div class="foot">共计 {{ stats?.totalObjects ?? 0 }} 个业务对象</div>
        </el-card>
      </el-col>
      <el-col :span="6">
        <el-card shadow="never" class="info-card">
          <div class="info-card-header">
            <div class="info-card-icon bg-blue"><el-icon :size="16"><Collection /></el-icon></div>
            <span class="info-card-label">对象属性</span>
            <span class="subtag">已定义</span>
          </div>
          <div class="val-row"><span class="val">{{ stats?.totalProperties ?? 0 }}</span><span class="badge neutral">全部</span></div>
          <div class="foot">平均 {{ stats?.totalObjects ? (stats.totalProperties / stats.totalObjects).toFixed(1) : 0 }} 个/对象</div>
        </el-card>
      </el-col>
      <el-col :span="6">
        <el-card shadow="never" class="info-card">
          <div class="info-card-header">
            <div class="info-card-icon bg-green"><el-icon :size="16"><Connection /></el-icon></div>
            <span class="info-card-label">数据映射</span>
            <span class="subtag green">已确认</span>
          </div>
          <div class="val-row"><span class="val green">{{ stats?.totalMappings ?? 0 }}</span><span class="badge neutral">已确认 {{ stats?.confirmedMappings ?? 0 }}</span></div>
          <div class="foot">{{ stats?.confirmedMappings ?? 0 }} 个已确认</div>
        </el-card>
      </el-col>
      <el-col :span="6">
        <el-card shadow="never" class="info-card">
          <div class="info-card-header">
            <div class="info-card-icon bg-purple"><el-icon :size="16"><Link /></el-icon></div>
            <span class="info-card-label">类型分布</span>
            <span class="subtag">覆盖</span>
          </div>
          <div class="val-row"><span class="val">{{ stats?.byObjectType?.length ?? 0 }}</span><span class="badge neutral">个类型</span></div>
          <div class="foot">{{ stats?.byObjectType?.map(t => t.type).join(' · ') || '-' }}</div>
        </el-card>
      </el-col>
    </el-row>

    <!-- ====== 业务对象 Tab ====== -->
    <Crud v-if="activeTab === '业务对象'" :filter-items="searchFilterItems" v-model:filter-values="searchValues" :pagination="soPagination" @filter-change="loadObjects">
      <template #filters-actions>
        <el-button type="primary" :icon="Plus" @click="openObjectDialog()">创建业务对象</el-button>
      </template>
      <template #table>
        <Table :columns="soColumns" :data="objects" :loading="objLoading" />
      </template>
    </Crud>

    <!-- ====== 对象属性 Tab ====== -->
    <Crud v-if="activeTab === '对象属性'" :filter-items="propFilterItems" v-model:filter-values="propFilterValues" :pagination="oaPagination" @filter-change="loadProperties">
      <template #table>
        <Table :columns="oaColumns" :data="properties" :loading="propLoading">
          <template #col-objectName="{ row }"><el-tag size="small" type="primary">{{ row.objectName }}</el-tag></template>
        </Table>
      </template>
    </Crud>

    <!-- ====== 语义关系 Tab ====== -->
    <Crud v-if="activeTab === '语义关系'" :filter-items="relFilterItems" v-model:filter-values="relFilterValues" :pagination="srPagination" @filter-change="loadRelations">
      <template #filters-actions>
        <el-button type="primary" :icon="Plus" @click="openRelationDialog()">创建关系</el-button>
      </template>
      <template #table>
        <Table :columns="srColumns" :data="relations" :loading="relLoading">
          <template #col-subject="{ row }">
            <el-tag size="small" type="primary">{{ row.subjectObjectName }}</el-tag>
          </template>
          <template #col-object="{ row }">
            <el-tag size="small" type="success">{{ row.objectObjectName }}</el-tag>
          </template>
        </Table>
      </template>
    </Crud>

    <!-- ====== 数据映射 Tab ====== -->
    <Crud v-if="activeTab === '数据映射'" :filter-items="searchFilterItems" v-model:filter-values="searchValues" :pagination="dmPagination" @filter-change="loadMappings">
      <template #filters-actions>
        <el-button type="primary" :icon="Plus" @click="openMappingDialog()">创建映射</el-button>
      </template>
      <template #table>
        <Table :columns="dmColumns" :data="mappings" :loading="mapLoading" />
      </template>
    </Crud>

    <!-- ====== 行动策略 Tab (Phase 2 占位) ====== -->
    <Crud v-if="activeTab === '行动策略'" :filter-items="searchFilterItems" v-model:filter-values="searchValues" :pagination="apPagination">
      <template #filters-actions>
        <el-button type="primary" :icon="Plus" disabled>配置策略</el-button>
      </template>
      <template #table>
        <Table :columns="apColumns" :data="actionPolicies">
          <template #col-forbiddenActions="{ row }"><span class="text-danger">{{ row.forbiddenActions }}</span></template>
        </Table>
      </template>
    </Crud>

    <!-- ====== 对话框 ====== -->

    <!-- 业务对象创建/编辑 -->
    <el-dialog v-model="objectDialogVisible" :title="editingObject ? '编辑业务对象' : '创建业务对象'" width="560px">
      <el-form :model="objectForm" label-width="80px">
        <el-form-item label="对象编码">
          <el-input v-model="objectForm.code" placeholder="如 ORDER" :disabled="!!editingObject" />
        </el-form-item>
        <el-form-item label="对象名称">
          <el-input v-model="objectForm.name" placeholder="如 订单" />
        </el-form-item>
        <el-form-item label="对象类型">
          <el-select v-model="objectForm.objectType" placeholder="选择类型">
            <el-option label="主数据" value="master_data" />
            <el-option label="交易" value="transaction" />
            <el-option label="资源" value="resource" />
            <el-option label="流程" value="process" />
            <el-option label="事件/状态" value="event_state" />
            <el-option label="指标" value="metric" />
            <el-option label="规则" value="rule" />
            <el-option label="数据" value="data" />
          </el-select>
        </el-form-item>
        <el-form-item label="业务域">
          <el-input v-model="objectForm.domain" placeholder="如 工单管理" />
        </el-form-item>
        <el-form-item label="描述">
          <el-input v-model="objectForm.description" type="textarea" :rows="3" placeholder="业务说明" />
        </el-form-item>
      </el-form>
      <template #footer>
        <el-button @click="objectDialogVisible = false">取消</el-button>
        <el-button type="primary" @click="saveObject">保存</el-button>
      </template>
    </el-dialog>

    <!-- 属性创建/编辑 -->
    <el-dialog v-model="propDialogVisible" :title="editingProperty ? '编辑属性' : '创建属性'" width="560px">
      <el-form :model="propForm" label-width="80px">
        <el-form-item label="所属对象">
          <el-select v-model="propForm.semanticObjectId" placeholder="选择业务对象" :disabled="!!editingProperty">
            <el-option v-for="o in objects" :key="o.id" :label="o.name" :value="o.id" />
          </el-select>
        </el-form-item>
        <el-form-item label="属性编码">
          <el-input v-model="propForm.code" placeholder="如 ORDER_ID" />
        </el-form-item>
        <el-form-item label="属性名称">
          <el-input v-model="propForm.name" placeholder="如 订单号" />
        </el-form-item>
        <el-form-item label="属性类型">
          <el-select v-model="propForm.propertyType" placeholder="选择类型">
            <el-option label="标识" value="identifier" />
            <el-option label="描述" value="descriptive" />
            <el-option label="状态" value="status" />
            <el-option label="时间" value="temporal" />
            <el-option label="度量" value="measure" />
            <el-option label="指标" value="metric" />
          </el-select>
        </el-form-item>
        <el-form-item label="数据类型">
          <el-select v-model="propForm.dataType" placeholder="选择类型">
            <el-option label="STRING" value="STRING" />
            <el-option label="INTEGER" value="INTEGER" />
            <el-option label="DECIMAL" value="DECIMAL" />
            <el-option label="DATE" value="DATE" />
            <el-option label="DATETIME" value="DATETIME" />
            <el-option label="BOOLEAN" value="BOOLEAN" />
          </el-select>
        </el-form-item>
        <el-form-item label="描述">
          <el-input v-model="propForm.description" type="textarea" :rows="2" placeholder="属性说明" />
        </el-form-item>
        <el-form-item label="排序">
          <el-input-number v-model="propForm.ordinalPosition" :min="0" />
        </el-form-item>
        <el-form-item label="选项">
          <el-checkbox v-model="propForm.isRequired">必填</el-checkbox>
          <el-checkbox v-model="propForm.isSensitive">敏感字段</el-checkbox>
        </el-form-item>
      </el-form>
      <template #footer>
        <el-button @click="propDialogVisible = false">取消</el-button>
        <el-button type="primary" @click="saveProperty">保存</el-button>
      </template>
    </el-dialog>

    <!-- 数据映射创建/编辑 -->
    <el-dialog v-model="mappingDialogVisible" :title="editingMapping ? '编辑映射' : '创建映射'" width="560px">
      <el-form :model="mappingForm" label-width="80px">
        <el-form-item label="映射类型">
          <el-select v-model="mappingForm.mappingType">
            <el-option label="对象级" value="object" />
            <el-option label="字段级" value="field" />
            <el-option label="关系级" value="relation" />
            <el-option label="指标级" value="metric" />
          </el-select>
        </el-form-item>
        <el-form-item label="语义对象">
          <el-select v-model="mappingForm.semanticObjectId" placeholder="可选" clearable>
            <el-option v-for="o in objects" :key="o.id" :label="o.name" :value="o.id" />
          </el-select>
        </el-form-item>
        <el-form-item label="语义属性">
          <el-select v-model="mappingForm.semanticPropertyId" placeholder="可选" clearable>
            <el-option v-for="p in allProperties" :key="p.id" :label="`${p.objectName}.${p.name}`" :value="p.id" />
          </el-select>
        </el-form-item>
        <el-form-item label="目标类型">
          <el-select v-model="mappingForm.targetType" @change="mappingForm.targetId = ''">
            <el-option label="数据集" value="dataset" />
            <el-option label="字段" value="dataset_field" />
            <el-option label="数据源" value="data_source" />
          </el-select>
        </el-form-item>
        <el-form-item label="目标ID">
          <el-input v-model="mappingForm.targetId" placeholder="UUID" />
        </el-form-item>
        <el-form-item label="转换规则">
          <el-input v-model="mappingForm.transformRule" placeholder="如 直接映射 / TRIM() / 单位转换" />
        </el-form-item>
        <el-form-item label="可信度">
          <el-select v-model="mappingForm.confidence">
            <el-option label="高" value="high" />
            <el-option label="中" value="medium" />
            <el-option label="低" value="low" />
          </el-select>
        </el-form-item>
      </el-form>
      <template #footer>
        <el-button @click="mappingDialogVisible = false">取消</el-button>
        <el-button type="primary" @click="saveMapping">保存</el-button>
      </template>
    </el-dialog>

    <!-- 语义关系创建/编辑 -->
    <el-dialog v-model="relationDialogVisible" :title="editingRelation ? '编辑关系' : '创建关系'" width="600px">
      <el-form :model="relationForm" label-width="90px">
        <el-form-item label="关系编码">
          <el-input v-model="relationForm.code" placeholder="如 REL-M05" :disabled="!!editingRelation" />
        </el-form-item>
        <el-form-item label="关系名称">
          <el-input v-model="relationForm.name" placeholder="如 产生报工记录" />
        </el-form-item>
        <el-form-item label="关系类型">
          <el-select v-model="relationForm.relationType" placeholder="选择类型">
            <el-option label="结构关系" value="structural" />
            <el-option label="交易关系" value="transactional" />
            <el-option label="资源关系" value="resource" />
            <el-option label="过程关系" value="process" />
            <el-option label="责任关系" value="responsibility" />
            <el-option label="财务关系" value="financial" />
            <el-option label="质量关系" value="quality" />
            <el-option label="事件关系" value="event" />
          </el-select>
        </el-form-item>
        <el-row :gutter="12">
          <el-col :span="12">
            <el-form-item label="主体对象">
              <el-select v-model="relationForm.subjectObjectId" placeholder="选择对象" filterable>
                <el-option v-for="o in activeObjects" :key="o.id" :label="o.name" :value="o.id" />
              </el-select>
            </el-form-item>
          </el-col>
          <el-col :span="12">
            <el-form-item label="客体对象">
              <el-select v-model="relationForm.objectObjectId" placeholder="选择对象" filterable>
                <el-option v-for="o in activeObjects" :key="o.id" :label="o.name" :value="o.id" />
              </el-select>
            </el-form-item>
          </el-col>
        </el-row>
        <el-form-item label="基数">
          <el-select v-model="relationForm.cardinality">
            <el-option label="1:1" value="1:1" />
            <el-option label="1:N" value="1:N" />
            <el-option label="N:1" value="N:1" />
            <el-option label="N:M" value="N:M" />
          </el-select>
        </el-form-item>
        <el-form-item label="关联字段">
          <el-input v-model="relationForm.joinMechanism" placeholder="如 workorder_no / workorder_no + procedure_no" />
        </el-form-item>
        <el-form-item label="描述">
          <el-input v-model="relationForm.description" type="textarea" :rows="2" placeholder="关系业务说明" />
        </el-form-item>
        <el-form-item label="Agent可用">
          <el-switch v-model="relationForm.agentEnabled" />
        </el-form-item>
      </el-form>
      <template #footer>
        <el-button @click="relationDialogVisible = false">取消</el-button>
        <el-button type="primary" @click="saveRelation">保存</el-button>
      </template>
    </el-dialog>
  </div>
</template>

<script setup lang="ts">
import { computed, reactive, ref, watch, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { ElMessage, ElMessageBox } from 'element-plus'
import { Search, Plus, Edit, Delete, Service, Collection, Connection, Link, Select, Refresh } from '@element-plus/icons-vue'
import TabNav from '@/components/tab-nav/index.vue'
import type { TabItem } from '@/components/tab-nav/types'
import Index from '@/components/page-header/index.vue'
import { Crud, Table } from '@/components/crud'
import type { ColumnSchema, FilterItem } from '@/components/crud'
import { semanticService } from '@/api/services/semantic'
import { graphService } from '@/api/services/graph'
import type { SemanticObject, SemanticProperty, SemanticRelation, DataMappingItem, SemanticStats } from '@/api/types'

const router = useRouter()

// ── Tab & Filter ──
const activeTab = ref('业务对象')
const tabs: TabItem[] = [
  { key: '业务对象', label: '业务对象' },
  { key: '对象属性', label: '对象属性' },
  { key: '语义关系', label: '语义关系' },
  { key: '数据映射', label: '数据映射' },
  { key: '行动策略', label: '行动策略' },
]

const searchFilterItems: FilterItem[] = [{ key: 'keyword', placeholder: '搜索...', width: '260px' }]
const searchValues = ref<Record<string, any>>({})

const propFilterItems: FilterItem[] = [
  { key: 'keyword', placeholder: '搜索属性...', width: '220px' },
]
const propFilterValues = ref<Record<string, any>>({})

const relFilterItems: FilterItem[] = [
  { key: 'keyword', placeholder: '搜索关系...', width: '220px' },
]
const relFilterValues = ref<Record<string, any>>({})

// ── Data ──
const objects = ref<SemanticObject[]>([])
const properties = ref<SemanticProperty[]>([])
const relations = ref<SemanticRelation[]>([])
const mappings = ref<DataMappingItem[]>([])
const allProperties = ref<SemanticProperty[]>([]) // all properties for dropdown
const stats = ref<SemanticStats | null>(null)

const objLoading = ref(false)
const propLoading = ref(false)
const relLoading = ref(false)
const mapLoading = ref(false)
const reloading = ref(false)

const activeObjects = computed(() => objects.value.filter(o => o.status === 'active'))

// ── Stats ──
async function loadStats() {
  try {
    stats.value = await semanticService.getStats()
  } catch { /* ignore */ }
}

// ── Reload ──
async function handleReload() {
  reloading.value = true
  try {
    await semanticService.reloadSemantic()
    ElMessage.success('YAML 配置已重新加载并同步到数据库')
    // Refresh all tabs
    loadObjects()
    loadProperties()
    loadMappings()
    loadStats()
  } catch { /* 错误提示由 axios 拦截器统一处理 */ } finally {
    reloading.value = false
  }
}

// ── Objects ──
async function loadObjects() {
  objLoading.value = true
  try {
    const res = await semanticService.getObjects({
      keyword: searchValues.value.keyword || undefined,
      page: soPage.value,
      pageSize: soPageSize.value,
    })
    objects.value = res.items
    soPagination.total = res.total
  } catch { objects.value = [] }
  finally { objLoading.value = false }
}

const soPage = ref(1)
const soPageSize = ref(20)
const soPagination = reactive({
  get page() { return soPage.value },
  set page(v) { soPage.value = v },
  get pageSize() { return soPageSize.value },
  set pageSize(v) { soPageSize.value = v },
  get total() { return soPageTotal.value },
  set total(v) { soPageTotal.value = v },
  onPageChange() { loadObjects() },
  onSizeChange() { soPage.value = 1; loadObjects() },
})
const soPageTotal = ref(0)

// Object dialog
const objectDialogVisible = ref(false)
const editingObject = ref<SemanticObject | null>(null)
const objectForm = reactive({
  code: '', name: '', objectType: 'master_data', domain: '', description: '',
})

function openObjectDialog(obj?: SemanticObject) {
  editingObject.value = obj || null
  if (obj) {
    objectForm.code = obj.code
    objectForm.name = obj.name
    objectForm.objectType = obj.objectType
    objectForm.domain = obj.domain || ''
    objectForm.description = obj.description || ''
  } else {
    objectForm.code = ''
    objectForm.name = ''
    objectForm.objectType = 'master_data'
    objectForm.domain = ''
    objectForm.description = ''
  }
  objectDialogVisible.value = true
}

async function saveObject() {
  try {
    if (editingObject.value) {
      await semanticService.updateObject(editingObject.value.id, { ...objectForm })
      ElMessage.success('更新成功')
    } else {
      await semanticService.createObject({ ...objectForm })
      ElMessage.success('创建成功')
    }
    objectDialogVisible.value = false
    loadObjects()
    loadStats()
  } catch { /* 错误提示由 axios 拦截器统一处理 */ }
}

async function handleDeleteObject(row: SemanticObject) {
  try {
    await ElMessageBox.confirm(`确认归档「${row.name}」？`, '提示', { type: 'warning' })
    await semanticService.deleteObject(row.id)
    ElMessage.success('已归档')
    loadObjects()
    loadStats()
  } catch { /* cancelled */ }
}

// ── Properties ──
async function loadProperties() {
  propLoading.value = true
  try {
    const res = await semanticService.getProperties({
      page: oaPage.value,
      pageSize: oaPageSize.value,
    })
    properties.value = res.items
    oaPagination.total = res.total
  } catch { properties.value = [] }
  finally { propLoading.value = false }
}

const oaPage = ref(1)
const oaPageSize = ref(20)
const oaPagination = reactive({
  get page() { return oaPage.value },
  set page(v) { oaPage.value = v },
  get pageSize() { return oaPageSize.value },
  set pageSize(v) { oaPageSize.value = v },
  get total() { return oaPageTotal.value },
  set total(v) { oaPageTotal.value = v },
  onPageChange() { loadProperties() },
  onSizeChange() { oaPage.value = 1; loadProperties() },
})
const oaPageTotal = ref(0)

// Property dialog
const propDialogVisible = ref(false)
const editingProperty = ref<SemanticProperty | null>(null)
const propForm = reactive<Record<string, any>>({
  semanticObjectId: '', code: '', name: '', propertyType: 'descriptive',
  dataType: 'STRING', description: '', ordinalPosition: 0,
  isRequired: false, isSensitive: false,
})

function openPropDialog(prop?: SemanticProperty) {
  editingProperty.value = prop || null
  if (prop) {
    propForm.semanticObjectId = prop.semanticObjectId
    propForm.code = prop.code
    propForm.name = prop.name
    propForm.propertyType = prop.propertyType
    propForm.dataType = prop.dataType
    propForm.description = prop.description || ''
    propForm.ordinalPosition = prop.ordinalPosition
    propForm.isRequired = prop.isRequired
    propForm.isSensitive = prop.isSensitive
  } else {
    Object.assign(propForm, {
      semanticObjectId: '', code: '', name: '', propertyType: 'descriptive',
      dataType: 'STRING', description: '', ordinalPosition: 0,
      isRequired: false, isSensitive: false,
    })
  }
  propDialogVisible.value = true
}

async function saveProperty() {
  try {
    if (editingProperty.value) {
      await semanticService.updateProperty(editingProperty.value.id, { ...propForm })
      ElMessage.success('更新成功')
    } else {
      await semanticService.createProperty({ ...propForm })
      ElMessage.success('创建成功')
    }
    propDialogVisible.value = false
    loadProperties()
    loadStats()
  } catch { /* 错误提示由 axios 拦截器统一处理 */ }
}

async function handleDeleteProperty(row: SemanticProperty) {
  try {
    await ElMessageBox.confirm(`确认删除属性「${row.name}」？`, '提示', { type: 'warning' })
    await semanticService.deleteProperty(row.id)
    ElMessage.success('已删除')
    loadProperties()
    loadStats()
  } catch { /* cancelled */ }
}

// ── Mappings ──
async function loadMappings() {
  mapLoading.value = true
  try {
    const res = await semanticService.getMappings({
      page: dmPage.value,
      pageSize: dmPageSize.value,
    })
    mappings.value = res.items
    dmPagination.total = res.total
  } catch { mappings.value = [] }
  finally { mapLoading.value = false }
}

const dmPage = ref(1)
const dmPageSize = ref(20)
const dmPagination = reactive({
  get page() { return dmPage.value },
  set page(v) { dmPage.value = v },
  get pageSize() { return dmPageSize.value },
  set pageSize(v) { dmPageSize.value = v },
  get total() { return dmPageTotal.value },
  set total(v) { dmPageTotal.value = v },
  onPageChange() { loadMappings() },
  onSizeChange() { dmPage.value = 1; loadMappings() },
})
const dmPageTotal = ref(0)

// Mapping dialog
const mappingDialogVisible = ref(false)
const editingMapping = ref<DataMappingItem | null>(null)
const mappingForm = reactive<Record<string, any>>({
  mappingType: 'field', semanticObjectId: '', semanticPropertyId: '',
  targetType: 'dataset', targetId: '', transformRule: '', confidence: 'medium',
})

function openMappingDialog(map?: DataMappingItem) {
  editingMapping.value = map || null
  if (map) {
    mappingForm.mappingType = map.mappingType
    mappingForm.semanticObjectId = map.semanticObjectId || ''
    mappingForm.semanticPropertyId = map.semanticPropertyId || ''
    mappingForm.targetType = map.targetType
    mappingForm.targetId = map.targetId
    mappingForm.transformRule = map.transformRule || ''
    mappingForm.confidence = map.confidence
  } else {
    Object.assign(mappingForm, {
      mappingType: 'field', semanticObjectId: '', semanticPropertyId: '',
      targetType: 'dataset', targetId: '', transformRule: '', confidence: 'medium',
    })
  }
  mappingDialogVisible.value = true
}

async function saveMapping() {
  try {
    if (editingMapping.value) {
      await semanticService.updateMapping(editingMapping.value.id, { ...mappingForm })
      ElMessage.success('更新成功')
    } else {
      await semanticService.createMapping({ ...mappingForm })
      ElMessage.success('创建成功')
    }
    mappingDialogVisible.value = false
    loadMappings()
    loadStats()
  } catch { /* 错误提示由 axios 拦截器统一处理 */ }
}

async function handleDeleteMapping(row: DataMappingItem) {
  try {
    await ElMessageBox.confirm('确认删除此映射？', '提示', { type: 'warning' })
    await semanticService.deleteMapping(row.id)
    ElMessage.success('已删除')
    loadMappings()
    loadStats()
  } catch { /* cancelled */ }
}

async function handleConfirmMapping(row: DataMappingItem) {
  try {
    await semanticService.updateMapping(row.id, { status: 'confirmed' })
    ElMessage.success('已确认')
    loadMappings()
    loadStats()
  } catch { /* 错误提示由 axios 拦截器统一处理 */ }
}

// ── Relations ──
async function loadRelations() {
  relLoading.value = true
  try {
    const res = await semanticService.getRelations({
      keyword: relFilterValues.value.keyword || undefined,
      page: srPage.value,
      pageSize: srPageSize.value,
    })
    relations.value = res.items
    srPagination.total = res.total
  } catch { relations.value = [] }
  finally { relLoading.value = false }
}

const srPage = ref(1)
const srPageSize = ref(20)
const srPagination = reactive({
  get page() { return srPage.value },
  set page(v) { srPage.value = v },
  get pageSize() { return srPageSize.value },
  set pageSize(v) { srPageSize.value = v },
  get total() { return srPageTotal.value },
  set total(v) { srPageTotal.value = v },
  onPageChange() { loadRelations() },
  onSizeChange() { srPage.value = 1; loadRelations() },
})
const srPageTotal = ref(0)

// Relation dialog
const relationDialogVisible = ref(false)
const editingRelation = ref<SemanticRelation | null>(null)
const relationForm = reactive<Record<string, any>>({
  code: '', name: '', relationType: 'process',
  subjectObjectId: '', objectObjectId: '',
  cardinality: '1:N', joinMechanism: '',
  description: '', agentEnabled: true,
})

function openRelationDialog(rel?: SemanticRelation) {
  editingRelation.value = rel || null
  if (rel) {
    relationForm.code = rel.code
    relationForm.name = rel.name
    relationForm.relationType = rel.relationType
    relationForm.subjectObjectId = rel.subjectObjectId
    relationForm.objectObjectId = rel.objectObjectId
    relationForm.cardinality = rel.cardinality
    relationForm.joinMechanism = rel.joinMechanism || ''
    relationForm.description = rel.description || ''
    relationForm.agentEnabled = rel.agentEnabled
  } else {
    Object.assign(relationForm, {
      code: '', name: '', relationType: 'process',
      subjectObjectId: '', objectObjectId: '',
      cardinality: '1:N', joinMechanism: '',
      description: '', agentEnabled: true,
    })
  }
  relationDialogVisible.value = true
}

async function saveRelation() {
  try {
    if (editingRelation.value) {
      await semanticService.updateRelation(editingRelation.value.id, { ...relationForm })
      ElMessage.success('更新成功')
    } else {
      await semanticService.createRelation({ ...relationForm })
      ElMessage.success('创建成功')
    }
    relationDialogVisible.value = false
    loadRelations()
  } catch { /* 错误提示由 axios 拦截器统一处理 */ }
}

async function handleDeleteRelation(row: SemanticRelation) {
  try {
    await ElMessageBox.confirm(`确认归档关系「${row.name}」？`, '提示', { type: 'warning' })
    await semanticService.deleteRelation(row.id)
    ElMessage.success('已归档')
    loadRelations()
  } catch { /* cancelled */ }
}

const generatingCode = ref<string | null>(null)

async function handleGenerateEdges(row: SemanticRelation) {
  if (generatingCode.value) return  // 防止重复点击
  generatingCode.value = row.code
  try {
    const res = await graphService.generateEdges(row.code)
    ElMessage.success(`已生成 ${res.generated} 条边`)
    loadRelations()
  } catch { /* 错误提示由 axios 拦截器统一处理 */ }
  finally { generatingCode.value = null }
}

function handleViewEdges(row: SemanticRelation) {
  router.push({ path: '/graph', query: { relationCode: row.code } })
}

// ── Column Schemas ──

const soColumns: ColumnSchema[] = [
  { type: 'text', prop: 'code', label: '对象编码', width: 130 },
  { type: 'text', prop: 'name', label: '对象名称', minWidth: 120 },
  { type: 'tag', prop: 'objectType', label: '类型', width: 100,
    tagMap: { master_data: '', transaction: 'success', resource: 'warning', process: 'info', event_state: '', metric: 'danger', rule: '', data: '' } },
  { type: 'text', prop: 'description', label: '描述', minWidth: 200 },
  { type: 'text', prop: 'propertyCount', label: '属性数', width: 80, align: 'center' },
  { type: 'text', prop: 'mappingCount', label: '映射数', width: 80, align: 'center' },
  { type: 'tag', prop: 'status', label: '状态', width: 80, tagMap: { active: 'success', draft: 'info', archived: 'warning' } },
  { type: 'action', label: '操作', width: 140, buttons: [
    { label: '编辑', icon: Edit, onClick: (row: any) => openObjectDialog(row as SemanticObject), tooltip: '当前数据由 YAML 同步，编辑将在下次重载时被覆盖' },
    { label: '归档', icon: Delete, onClick: (row: any) => handleDeleteObject(row as SemanticObject), type: 'danger', tooltip: '当前数据由 YAML 同步，归档将在下次重载时被覆盖' },
  ] },
]

const oaColumns: ColumnSchema[] = [
  { type: 'text', prop: 'code', label: '属性编码', width: 140 },
  { type: 'text', prop: 'name', label: '属性名称', minWidth: 100 },
  { type: 'custom', prop: 'objectName', label: '所属对象', width: 100 },
  { type: 'text', prop: 'propertyType', label: '属性类型', width: 100 },
  { type: 'text', prop: 'dataType', label: '数据类型', width: 100 },
  { type: 'text', prop: 'description', label: '业务含义', minWidth: 140 },
  { type: 'tag', prop: 'isSensitive', label: '敏感', width: 70,
    formatter: (v: boolean) => v ? '是' : '否',
    tagMap: { true: 'danger', false: 'info' } } as ColumnSchema,
  { type: 'tag', prop: 'hasMapping', label: '已映射', width: 80,
    formatter: (v: boolean) => v ? '是' : '否',
    tagMap: { true: 'success', false: 'info' } } as ColumnSchema,
  { type: 'action', label: '操作', width: 140, buttons: [
    { label: '编辑', icon: Edit, onClick: (row: any) => openPropDialog(row as SemanticProperty), tooltip: '当前数据由 YAML 同步，编辑将在下次重载时被覆盖' },
    { label: '', icon: Delete, onClick: (row: any) => handleDeleteProperty(row as SemanticProperty), type: 'danger', tooltip: '当前数据由 YAML 同步，删除将在下次重载时被覆盖' },
  ] },
]

const dmColumns: ColumnSchema[] = [
  { type: 'text', prop: 'semanticObjectName', label: '业务对象', width: 120 },
  { type: 'text', prop: 'semanticPropertyName', label: '属性', width: 120 },
  { type: 'text', prop: 'targetType', label: '目标类型', width: 110 },
  { type: 'text', prop: 'targetName', label: '目标名称', minWidth: 140 },
  { type: 'text', prop: 'transformRule', label: '转换规则', width: 120 },
  { type: 'tag', prop: 'confidence', label: '可信度', width: 80,
    tagMap: { high: 'success', medium: 'warning', low: 'danger' } },
  { type: 'tag', prop: 'status', label: '状态', width: 90,
    tagMap: { confirmed: 'success', unconfirmed: 'warning' } },
  { type: 'action', label: '操作', width: 180, buttons: [
    { label: '确认', icon: Select, onClick: (row: any) => handleConfirmMapping(row as DataMappingItem),
      hidden: (row: any) => (row as DataMappingItem).status === 'confirmed' },
    { label: '', icon: Edit, onClick: (row: any) => openMappingDialog(row as DataMappingItem), tooltip: '当前数据由 YAML 同步，编辑将在下次重载时被覆盖' },
    { label: '', icon: Delete, onClick: (row: any) => handleDeleteMapping(row as DataMappingItem), type: 'danger', tooltip: '当前数据由 YAML 同步，删除将在下次重载时被覆盖' },
  ] },
]

// ── 行动策略仍为 Phase 2 占位 ──
const actionPolicies = [
  { objectType: '订单', allowedActions: '查询, 创建', forbiddenActions: '删除', riskLevel: '中', requireConfirm: false },
  { objectType: '客户', allowedActions: '查询', forbiddenActions: '修改, 删除', riskLevel: '高', requireConfirm: true },
  { objectType: '产品', allowedActions: '查询', forbiddenActions: '修改, 删除, 创建', riskLevel: '低', requireConfirm: false },
]

const srColumns: ColumnSchema[] = [
  { type: 'text', prop: 'code', label: '关系编码', width: 110 },
  { type: 'text', prop: 'name', label: '关系名称', minWidth: 110 },
  { type: 'custom', prop: 'subject', label: '主体对象', width: 150, slotName: 'col-subject' },
  { type: 'custom', prop: 'object', label: '客体对象', width: 150, slotName: 'col-object' },
  { type: 'text', prop: 'relationType', label: '类型', width: 90 },
  { type: 'text', prop: 'cardinality', label: '基数', width: 70, align: 'center' },
  { type: 'tag', prop: 'agentEnabled', label: 'Agent可用', width: 100,
    formatter: (v: boolean) => v ? '是' : '否',
    tagMap: { true: 'success', false: 'info' } } as ColumnSchema,
  { type: 'text', prop: 'edgeCount', label: '图谱边数', width: 90, align: 'center' },
  { type: 'tag', prop: 'status', label: '状态', width: 80,
    tagMap: { active: 'success', draft: 'info', archived: 'warning' } },
  { type: 'action', label: '操作', width: 180, buttons: [
    { label: '生成边', icon: Connection, onClick: (row: any) => handleGenerateEdges(row as SemanticRelation), tooltip: '按关系定义从 serving 视图生成实例边' },
    { label: '查看边', icon: Link, onClick: (row: any) => handleViewEdges(row as SemanticRelation), tooltip: '跳转关系图谱页查看该关系的实例边' },
    { label: '', icon: Edit, onClick: (row: any) => openRelationDialog(row as SemanticRelation), tooltip: '当前数据由 YAML 同步，编辑将在下次重载时被覆盖' },
    { label: '', icon: Delete, onClick: (row: any) => handleDeleteRelation(row as SemanticRelation), type: 'danger', tooltip: '当前数据由 YAML 同步，归档将在下次重载时被覆盖' },
  ] },
]

const apColumns: ColumnSchema[] = [
  { type: 'tag', prop: 'objectType', label: '对象类型', width: 100 },
  { type: 'text', prop: 'allowedActions', label: '允许行动', minWidth: 140 },
  { type: 'custom', prop: 'forbiddenActions', label: '禁止行动', minWidth: 140 },
  { type: 'tag', prop: 'riskLevel', label: '风险等级', width: 100,
    tagMap: { '高': 'danger', '中': 'warning', '低': 'success' } },
  { type: 'tag', prop: 'requireConfirm', label: '需确认', width: 100,
    formatter: (v: boolean) => v ? '是' : '否',
    tagMap: { true: 'warning', false: 'info' } } as ColumnSchema,
]

// Pagination for placeholder tab
const apPagination = reactive({ page: 1, pageSize: 20, total: actionPolicies.length, onPageChange() {}, onSizeChange() {} })

// ── Lifecycle ──
onMounted(() => {
  loadObjects()
  loadProperties()
  loadRelations()
  loadMappings()
  loadStats()
})

// Load all properties for dropdowns (no pagination)
async function loadAllProperties() {
  try {
    const res = await semanticService.getProperties({ page: 1, pageSize: 1000 })
    allProperties.value = res.items
  } catch { allProperties.value = [] }
}

watch(objectDialogVisible, (v) => { if (v) loadAllProperties() })
watch(mappingDialogVisible, (v) => { if (v) loadAllProperties() })

// Watch tab changes to reload
watch(activeTab, () => {
  soPage.value = 1
  oaPage.value = 1
  srPage.value = 1
  dmPage.value = 1
})
</script>

<style lang="scss" scoped>
.tab-btn { padding: 10px 16px; border: none; background: none; font-size: $font-size-base; color: $color-text-secondary; cursor: pointer; border-bottom: 2px solid transparent; &:hover { color: $color-text-primary; } &.active { color: $color-primary; border-bottom-color: $color-primary; font-weight: $font-weight-medium; } }
.stat-row { margin: 0 !important; :deep(.el-col) { padding-left: 8px !important; padding-right: 8px !important; } :deep(.el-col:first-child) { padding-left: 0 !important; } :deep(.el-col:last-child) { padding-right: 0 !important; } }
.info-card { :deep(.el-card__body) { display: flex; flex-direction: column; gap: 8px; padding: 20px; } }
.info-card-header { display: flex; align-items: center; gap: 6px; }
.info-card-icon { display: flex; align-items: center; justify-content: center; width: 32px; height: 32px; border-radius: 8px; &.bg-indigo { background: #e0e7ff; color: #4f46e5; } &.bg-blue { background: #dbeafe; color: $color-primary; } &.bg-green { background: #dcfce7; color: $color-success; } &.bg-purple { background: #ede9fe; color: #7c3aed; } }
.info-card-label { font-size: $font-size-base; color: $color-text-secondary; }
.subtag { font-size: $font-size-xs; padding: 1px 6px; border-radius: 4px; margin-left: auto; white-space: nowrap; background: #f3f4f6; color: $color-text-placeholder; &.green { color: $color-success; background: #f0fdf4; } }
.val-row { display: flex; align-items: baseline; gap: 8px; }
.val { font-size: 28px; font-weight: $font-weight-bold; color: $color-text-primary; &.green { color: $color-success; } }
.badge { font-size: $font-size-xs; padding: 1px 6px; border-radius: 4px; &.neutral { color: $color-text-placeholder; background: #f3f4f6; } }
.foot { font-size: $font-size-xs; color: $color-text-placeholder; }
.text-danger { color: $color-danger; }
</style>
