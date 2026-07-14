<template>
  <div class="page">
    <div class="toolbar">
      <el-button type="primary" :icon="Plus" @click="openCreate">新增数据源</el-button>
      <div class="spacer" />
    </div>

    <el-table v-loading="loading" :data="sources" stripe size="small">
      <el-table-column prop="name" label="名称" min-width="160">
        <template #default="{ row }">
          <el-link type="primary" :underline="false" @click="openEdit(row)">{{ row.name }}</el-link>
          <div class="row-sub">{{ row.description }}</div>
        </template>
      </el-table-column>
      <el-table-column prop="sourceType" label="类型" width="100">
        <template #default="{ row }">
          <el-tag size="small" effect="plain">{{ row.sourceType }}</el-tag>
        </template>
      </el-table-column>
      <el-table-column prop="accessMethod" label="接入方式" width="110" />
      <el-table-column prop="status" label="状态" width="90">
        <template #default="{ row }">
          <el-tag :type="row.status === 'active' ? 'success' : row.status === 'draft' ? 'info' : 'warning'" size="small" effect="plain">
            {{ row.status === 'active' ? '正常' : row.status === 'draft' ? '草稿' : row.status === 'archived' ? '已归档' : row.status }}
          </el-tag>
        </template>
      </el-table-column>
      <el-table-column prop="createdAt" label="创建时间" width="170">
        <template #default="{ row }">{{ row.createdAt?.slice(0, 19).replace('T', ' ') }}</template>
      </el-table-column>
      <el-table-column label="操作" width="120">
        <template #default="{ row }">
          <el-button size="small" text @click="openEdit(row)">编辑</el-button>
          <el-button size="small" text type="danger" @click="handleDelete(row)">归档</el-button>
        </template>
      </el-table-column>
    </el-table>
    <div v-if="sources.length === 0 && !loading" class="empty">暂无数据源</div>

    <!-- 编辑/新建弹窗 -->
    <el-dialog v-model="dialogVisible" :title="editingId ? '编辑数据源' : '新增数据源'" width="560px" destroy-on-close @closed="resetForm">
      <el-form :model="form" label-width="90px" size="small">
        <el-form-item label="名称" required><el-input v-model="form.name" maxlength="200" /></el-form-item>
        <el-form-item label="编码" required><el-input v-model="form.code" maxlength="100" :disabled="!!editingId" /></el-form-item>
        <el-form-item label="类型" required>
          <el-select v-model="form.sourceType" style="width:100%">
            <el-option label="数据库 (database)" value="database" />
            <el-option label="API 接口 (api)" value="api" />
            <el-option label="Excel 文件 (excel)" value="excel" />
            <el-option label="CSV 文件 (csv)" value="csv" />
          </el-select>
        </el-form-item>
        <el-form-item label="接入方式" required>
          <el-select v-model="form.accessMethod" style="width:100%">
            <el-option label="数据库同步 (db_sync)" value="db_sync" />
            <el-option label="API 拉取 (api_pull)" value="api_pull" />
            <el-option label="文件上传 (file_upload)" value="file_upload" />
          </el-select>
        </el-form-item>
        <el-form-item label="描述"><el-input v-model="form.description" type="textarea" :rows="2" /></el-form-item>
        <el-form-item label="负责人"><el-input v-model="form.ownerName" maxlength="100" /></el-form-item>
        <el-form-item label="所属部门"><el-input v-model="form.ownerDept" maxlength="100" /></el-form-item>
      </el-form>
      <template #footer>
        <el-button @click="dialogVisible = false">取消</el-button>
        <el-button type="primary" :loading="saving" @click="handleSave">{{ editingId ? '保存' : '创建' }}</el-button>
      </template>
    </el-dialog>
  </div>
</template>

<script setup lang="ts">
import { onMounted, ref } from 'vue';
import { Plus } from '@element-plus/icons-vue';
import { ElMessage, ElMessageBox } from 'element-plus';
import { dataSourceService } from '@/api/services/data-source';

interface DS {
  id: string; name: string; code: string; sourceType: string; accessMethod: string;
  description: string; ownerName: string; ownerDept: string; status: string; createdAt: string;
}

const sources = ref<DS[]>([]);
const loading = ref(false);
const dialogVisible = ref(false);
const editingId = ref('');
const saving = ref(false);
const form = ref({ name: '', code: '', sourceType: 'api', accessMethod: 'api_pull', description: '', ownerName: '', ownerDept: '' });

function resetForm() {
  editingId.value = '';
  form.value = { name: '', code: '', sourceType: 'api', accessMethod: 'api_pull', description: '', ownerName: '', ownerDept: '' };
}

async function load() {
  loading.value = true;
  try {
    const r = await dataSourceService.getList({ pageSize: 50 });
    sources.value = r.items;
  } finally { loading.value = false; }
}

function openCreate() { resetForm(); dialogVisible.value = true; }
async function openEdit(row: DS) {
  editingId.value = row.id;
  const detail = await dataSourceService.get(row.id);
  form.value = {
    name: detail.name, code: detail.code,
    sourceType: detail.sourceType, accessMethod: detail.accessMethod,
    description: detail.description || '', ownerName: detail.ownerName || '', ownerDept: detail.ownerDept || '',
  };
  dialogVisible.value = true;
}

async function handleSave() {
  saving.value = true;
  try {
    if (editingId.value) {
      await dataSourceService.update(editingId.value, form.value);
      ElMessage.success('已保存');
    } else {
      await dataSourceService.create(form.value);
      ElMessage.success('已创建');
    }
    dialogVisible.value = false;
    await load();
  } catch { /* handled */ }
  finally { saving.value = false; }
}

async function handleDelete(row: DS) {
  await ElMessageBox.confirm('确定归档该数据源？', '确认');
  await dataSourceService.delete(row.id);
  ElMessage.success('已归档');
  await load();
}

onMounted(load);
</script>

<style lang="scss" scoped>
.page { }
.toolbar { display: flex; gap: 10px; align-items: center; margin-bottom: 16px; }
.spacer { flex: 1; }
.row-sub { font-size: 11px; color: $color-text-placeholder; margin-top: 2px; }
.empty { text-align: center; padding: 60px; color: $color-text-placeholder; }
</style>
