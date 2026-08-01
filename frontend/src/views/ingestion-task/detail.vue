<template>
  <div class="page-layout" v-if="task">
    <Index :title="task.name"
      :breadcrumb="[{ label: '首页', to: '/' }, { label: '接入任务', to: '/ingestion' }, { label: task.name }]">
      <template #tags>
        <el-tag type="success" effect="plain">正常</el-tag>
        <el-tag type="info" effect="plain">{{ task.code }}</el-tag>
      </template>
      <template #actions>
        <el-button type="primary" :icon="VideoPlay" :loading="executing" @click="handleExecute">立即执行</el-button>
        <template v-if="!isEditing">
          <el-button :icon="Edit" @click="toggleEdit">编辑</el-button>
        </template>
        <template v-else>
          <el-button type="primary" :loading="saving" @click="handleSave">保存</el-button>
          <el-button @click="handleCancelEdit">取消</el-button>
        </template>
      </template>
    </Index>

    <div class="summary-row">
      <div v-for="s in summary" :key="s.label" class="sum-item">
        <span class="sum-label">{{ s.label }}</span>
        <span class="sum-val">{{ s.value }}</span>
      </div>
    </div>

    <el-tabs v-model="activeTab">
      <el-tab-pane name="config">
        <template #label>
          <el-badge :value="schemaChangeCount" :hidden="schemaChangeCount === 0" :max="99">
            <span>当前配置</span>
          </el-badge>
        </template>
        <template v-if="!isEditing">
          <el-descriptions :column="2" border style="max-width: 600px">
            <el-descriptions-item label="名称">{{ task.name }}</el-descriptions-item>
            <el-descriptions-item label="编码">{{ task.code }}</el-descriptions-item>
            <el-descriptions-item label="调度">
              <template v-if="task.scheduleType === 'cron'">
                <div class="sched-block">
                  <el-tag type="primary" effect="light" size="small">定时</el-tag>
                  <code class="cron-code">{{ task.cronExpression }}</code>
                  <span v-if="nextRunLoading" class="sched-next">计算中…</span>
                  <span v-else-if="nextRun" class="sched-next">下次执行：{{ fmtDateTime(nextRun, true) }}</span>
                  <span v-else class="sched-next sched-dim">下次执行：—</span>
                </div>
              </template>
              <el-tag v-else type="info" effect="plain" size="small">手动触发</el-tag>
            </el-descriptions-item>
            <el-descriptions-item label="最近同步">{{ fmtDateTime(task.lastSyncAt) || '未同步过' }}</el-descriptions-item>
            <el-descriptions-item label="上次结果">{{ task.lastSyncStatus || '-' }}</el-descriptions-item>
            <el-descriptions-item label="创建时间">{{ fmtDateTime(task.createdAt) }}</el-descriptions-item>
          </el-descriptions>
        </template>
        <template v-else>
          <el-form :model="editForm" label-width="100px" style="max-width: 500px">
            <el-form-item label="名称">
              <el-input v-model="editForm.name" />
            </el-form-item>
            <el-form-item label="编码">
              <el-input :model-value="task.code" disabled />
            </el-form-item>
            <el-form-item label="调度方式">
              <el-select v-model="editForm.scheduleType" style="width: 100%">
                <el-option label="手动触发" value="manual" />
                <el-option label="定时" value="cron" />
              </el-select>
            </el-form-item>
            <el-form-item v-if="editForm.scheduleType === 'cron'" label="Cron 表达式">
              <el-input v-model="editForm.cronExpression" placeholder="0 0 */30 * * ?" />
            </el-form-item>
            <el-form-item label="描述">
              <el-input v-model="editForm.description" type="textarea" :rows="3" />
            </el-form-item>
          </el-form>
        </template>

        <!-- F3.2 — 软删除检测状态标记 -->
        <el-divider content-position="left">
          接口与软删除检测
          <el-button size="small" type="primary" plain :loading="softDeleteChecking" style="margin-left: 12px"
            @click="triggerSoftDelete">立即检测</el-button>
        </el-divider>
        <el-table :data="softDeleteInterfaces" empty-text="暂无接口" style="width: 100%" size="small">
          <el-table-column prop="name" label="接口" min-width="170" />
          <el-table-column label="软删除检测" width="130">
            <template #default="{ row }">
              <el-tag v-if="row.enabled" type="warning" effect="light" size="small">
                已启用
              </el-tag>
              <el-tag v-else type="info" effect="plain" size="small">未启用</el-tag>
            </template>
          </el-table-column>
          <el-table-column label="最近检测" min-width="220">
            <template #default="{ row }">
              <span v-if="row.lastCheckedAt">
                {{ fmtDateTime(row.lastCheckedAt, true) }}
                <span class="sd-count">删除 {{ row.lastDeleted }} 行</span>
              </span>
              <span v-else class="sd-dim">—</span>
            </template>
          </el-table-column>
          <el-table-column label="上一次结果" min-width="160">
            <template #default="{ row }">
              <el-tag v-if="row.lastSkipped" type="info" size="small">跳过（{{ row.lastReason }}）</el-tag>
              <el-tag v-else type="success" size="small">已检测</el-tag>
            </template>
          </el-table-column>
        </el-table>

        <!-- F1.2 — Schema 变更审计 -->
        <el-divider />
        <el-collapse>
          <el-collapse-item name="schema">
            <template #title>
              <span>Schema 变更审计</span>
              <el-tag v-if="schemaChangeCount > 0" type="warning" size="small" style="margin-left: 8px">
                {{ schemaChangeCount }}
              </el-tag>
            </template>
            <div v-loading="schemaChangeLoading">
              <el-table :data="schemaChanges" empty-text="暂无 Schema 变更" style="width: 100%">
                <el-table-column prop="tableName" label="数据表" min-width="180" />
                <el-table-column label="变更类型" width="120">
                  <template #default="{ row }">
                    <el-tag :type="schemaChangeTagType(row.changeType)" size="small">
                      {{ SCHEMA_CHANGE_LABELS[row.changeType] ?? row.changeType }}
                    </el-tag>
                  </template>
                </el-table-column>
                <el-table-column prop="columnName" label="列名" min-width="160" />
                <el-table-column label="检测时间" width="180">
                  <template #default="{ row }">{{ fmtDateTime(row.detectedAt) }}</template>
                </el-table-column>
              </el-table>
            </div>
          </el-collapse-item>
        </el-collapse>
      </el-tab-pane>

      <el-tab-pane :label="`执行记录 (${groupedBatches.length})`" name="batches">
        <Crud :pagination="batchesPagination">
          <template #table>
            <Table :columns="batchesColumns" :data="pagedBatches" :tree-props="{ children: 'children' }"
              :expand-row-keys="expandedKeys" :default-expand-all="false" :row-class-name="batchRowClass"
              @expand-change="onExpandChange">
              <template #col-createdAt="{ row }">{{ fmtDateTime(row.createdAt) }}</template>
              <template #col-sourceSignature="{ row }">
                <span v-if="(row.sourceSignature || '').startsWith('(')" class="iface-tag iface-tag-agg">{{
                  row.sourceSignature }}</span>
                <span v-else-if="row.isSummary" class="iface-tag iface-tag-agg">(汇总)</span>
                <span v-else class="iface-tag">{{ ifaceLabel(row) }}</span>
              </template>
              <template #col-triggerType="{ row }"><span class="trigger-text">{{ triggerLabel[row.triggerType] ??
                row.triggerType }}</span></template>
              <template #col-status="{ row }">
                <div class="status-cell">
                  <el-tag :type="batchType[row.status]" effect="plain">{{ batchLabel[row.status] ?? row.status
                    }}</el-tag>
                  <template v-if="row.status === 'running'">
                    <el-progress :percentage="row._pct >= 0 ? row._pct : 0" :indeterminate="row._pct < 0"
                      :stroke-width="5" :show-text="false" style="width: 100%" />
                    <span v-if="row._step" class="step-text">{{ row._step }}</span>
                  </template>
                  <span v-if="row.errorSummary" class="err-text">{{ row.errorSummary }}</span>
                </div>
              </template>
              <template #col-successCount="{ row }">
                <template v-if="row.status === 'success' || row.status === 'partial_success'">
                  <span class="count-ok">{{ row.successCount?.toLocaleString() }} 行写入</span>
                  <span v-if="row.skipCount > 0" class="count-warn"> · {{ row.skipCount }} 跳过</span>
                  <span v-if="row.failCount > 0" class="count-err"> · {{ row.failCount }} 拒绝</span>
                </template>
                <span v-else-if="row.status === 'running'">—</span>
                <span v-else class="count-dim">-</span>
              </template>
              <template #col-duration="{ row }">
                <span v-if="row.startedAt && row.finishedAt" class="dur-text">{{ duration(row.startedAt, row.finishedAt)
                  }}</span>
                <span v-else-if="row.status === 'running' && row.startedAt" class="dur-text">{{ elapsed(row.startedAt)
                  }}</span>
                <span v-else>-</span>
              </template>
              <template #col-actions="{ row }">
                <div class="action-btns">
                  <el-button v-if="row.status === 'running'" text type="danger"
                    @click="handleCancel(row.id)">停止</el-button>
                  <template v-else>
                    <el-button text @click="showLog(row)">日志</el-button>
                    <el-button v-if="row.status === 'failed' || row.status === 'cancelled'" text type="warning"
                      @click="handleRetry(row.id)">重试</el-button>
                  </template>
                </div>
              </template>
            </Table>
          </template>
        </Crud>
        <div v-if="batches.length === 0" class="empty">暂无执行记录，点击「立即执行」开始</div>
      </el-tab-pane>

      <!-- F1.3 — 数据对账 -->
      <el-tab-pane name="recon">
        <template #label>
          <span>数据对账</span>
          <el-badge v-if="reconSummary.toRepair > 0" :value="reconSummary.toRepair" type="danger" :max="99"
            style="margin-left: 4px" />
        </template>
        <div v-loading="reconLoading">
          <!-- 概览卡片 -->
          <div class="recon-cards">
            <div class="recon-card">
              <span class="recon-card-label">最近对账</span>
              <span class="recon-card-val">{{ reconSummary.lastCheck ? fmtDateTime(reconSummary.lastCheck) : '—'
                }}</span>
            </div>
            <div class="recon-card">
              <span class="recon-card-label">数据一致</span>
              <span class="recon-card-val" style="color: var(--el-color-success)">{{ reconSummary.consistent }}</span>
            </div>
            <div class="recon-card">
              <span class="recon-card-label">存在差异</span>
              <span class="recon-card-val" style="color: #ca8a04">{{ reconSummary.diff }}</span>
            </div>
            <div class="recon-card">
              <span class="recon-card-label">待修复</span>
              <span class="recon-card-val" :class="{ 'recon-card-err': reconSummary.toRepair > 0 }">{{
                reconSummary.toRepair
                }}</span>
            </div>
          </div>

          <!-- 对账记录表格 -->
          <el-table :data="reconciliations" empty-text="暂无对账记录" style="width: 100%; margin-top: 16px">
            <el-table-column prop="interfaceName" label="接口" min-width="170" />
            <el-table-column label="级别" width="90">
              <template #default="{ row }">
                <el-tag :type="row.checkLevel === 'L1' ? 'info' : row.checkLevel === 'L2' ? 'warning' : 'danger'"
                  size="small" effect="plain">{{ CHECK_LEVEL_LABELS[row.checkLevel] ?? row.checkLevel }}</el-tag>
              </template>
            </el-table-column>
            <el-table-column label="模式" width="80">
              <template #default="{ row }">
                <el-tag :type="row.syncMode === 'incremental' ? 'warning' : 'success'" size="small" effect="plain">
                  {{ SYNC_MODE_LABELS[row.syncMode] ?? row.syncMode ?? '全量' }}
                </el-tag>
              </template>
            </el-table-column>
            <el-table-column prop="apiTotal" label="API 总量" width="100" align="right" />
            <el-table-column label="对比基准" width="110" align="right">
              <template #default="{ row }">
                <el-tooltip :content="row.syncMode === 'incremental'
                  ? '增量模式：与「本批拉取行数」对比（窗口内是否拉全）'
                  : '全量模式：与「整表行数」对比'" placement="top">
                  <span>{{ row.syncMode === 'incremental' ? (row.pulledCount ?? 0).toLocaleString() : (row.dbCount ??
                    0).toLocaleString() }}</span>
                </el-tooltip>
              </template>
            </el-table-column>
            <el-table-column label="差异" width="90" align="right">
              <template #default="{ row }">
                <span
                  :class="{ 'diff-ok': row.status === 'pass', 'diff-warn': row.status === 'warning', 'diff-err': row.status === 'failed' }">
                  {{ (row.diffCount ?? 0) > 0 ? `+${row.diffCount}` : '0' }}
                </span>
              </template>
            </el-table-column>
            <el-table-column label="差异率" width="100" align="right">
              <template #default="{ row }">
                <span
                  :class="{ 'diff-ok': row.status === 'pass', 'diff-warn': row.status === 'warning', 'diff-err': row.status === 'failed' }">
                  {{ ((row.diffRatio ?? 0) * 100).toFixed(2) }}%
                </span>
              </template>
            </el-table-column>
            <el-table-column label="状态" width="100">
              <template #default="{ row }">
                <el-tag
                  :type="row.status === 'pass' ? 'success' : row.status === 'warning' ? 'warning' : row.status === 'failed' ? 'danger' : 'info'"
                  size="small">{{ RECON_STATUS_LABELS[row.status] ?? row.status }}</el-tag>
              </template>
            </el-table-column>
            <el-table-column prop="checkedAt" label="检查时间" width="180">
              <template #default="{ row }">{{ fmtDateTime(row.checkedAt) }}</template>
            </el-table-column>
            <el-table-column label="操作" width="200" align="center">
              <template #default="{ row }">
                <div class="action-btns">
                  <el-button text @click="showReconDetail(row)">查看详情</el-button>
                  <el-button v-if="row.status === 'warning' || row.status === 'failed'" text type="warning"
                    @click="handleTriggerRecon('L2')">触发深度对账</el-button>
                  <el-button v-if="row.status === 'failed'" text type="danger"
                    @click="handleRepair(row.id)">修复</el-button>
                </div>
              </template>
            </el-table-column>
          </el-table>
        </div>

        <!-- 对账详情弹窗 -->
        <el-dialog v-model="reconDialog" title="对账详情" width="800px" destroy-on-close>
          <div v-loading="reconDetailLoading">
            <template v-if="reconDetail">
              <div class="recon-summary-grid">
                <div class="recon-sum-item">
                  <span class="recon-label">API 总量</span>
                  <span class="recon-val">{{ reconDetail.apiTotal?.toLocaleString() }}</span>
                </div>
                <div class="recon-sum-item">
                  <span class="recon-label">
                    对比基准
                    <el-tag :type="reconDetail.syncMode === 'incremental' ? 'warning' : 'success'" size="small"
                      effect="plain" style="margin-left: 4px">{{ SYNC_MODE_LABELS[reconDetail.syncMode ?? 'full'] ??
                        '全量' }}</el-tag>
                  </span>
                  <span class="recon-val">
                    {{ (reconDetail.syncMode === 'incremental' ? reconDetail.pulledCount :
                      reconDetail.dbCount)?.toLocaleString() }}
                    <span class="recon-sub">{{ reconDetail.syncMode === 'incremental' ? '（本批拉取）' : '（整表行数）' }}</span>
                  </span>
                </div>
                <div class="recon-sum-item">
                  <span class="recon-label">差异行数</span>
                  <span class="recon-val" :class="{ 'diff-err': (reconDetail.diffCount ?? 0) > 0 }">{{
                    reconDetail.diffCount?.toLocaleString() }}</span>
                </div>
                <div class="recon-sum-item">
                  <span class="recon-label">差异率</span>
                  <span class="recon-val"
                    :class="{ 'diff-err': reconDetail.status === 'failed', 'diff-warn': reconDetail.status === 'warning' }">
                    {{ ((reconDetail.diffRatio ?? 0) * 100).toFixed(2) }}%
                  </span>
                </div>
              </div>
              <el-divider>分段明细（L2 深度对账）</el-divider>
              <el-table v-if="reconDetail.detail && reconDetail.detail.length" :data="reconDetail.detail" stripe
                style="margin-top: 8px">
                <el-table-column prop="dateRange" label="日期段" min-width="200" />
                <el-table-column prop="apiCount" label="API 行数" width="100" align="right" />
                <el-table-column prop="dbCount" label="DB 行数" width="100" align="right" />
                <el-table-column label="差异" width="80" align="right">
                  <template #default="{ row }">
                    <span :class="{ 'diff-err': row.diff !== 0 }">{{ row.diff > 0 ? `+${row.diff}` : row.diff }}</span>
                  </template>
                </el-table-column>
                <el-table-column label="状态" width="100">
                  <template #default="{ row }">
                    <el-tag :type="row.diff === 0 ? 'success' : 'danger'" size="small">{{ row.diff === 0 ? '一致' : '需修复'
                      }}</el-tag>
                  </template>
                </el-table-column>
              </el-table>
              <el-empty v-else description="暂无分段明细（L2 深度对账尚未实现）" :image-size="80" />
            </template>
          </div>
        </el-dialog>
      </el-tab-pane>

      <!-- F2.3 — 隔离区 -->
      <el-tab-pane name="quarantine">
        <template #label>
          <span>隔离区</span>
          <el-badge v-if="quarantineStats.pending > 0" :value="quarantineStats.pending" type="warning" :max="99"
            style="margin-left: 4px" />
        </template>
        <div v-loading="quarantineLoading">
          <!-- 熔断状态卡片 -->
          <div class="qb-circuit">
            <div class="qb-circuit-head">
              <span class="qb-circuit-title">熔断状态</span>
              <el-tag :type="circuitState.type" effect="light" size="small">{{ circuitState.label }}</el-tag>
            </div>
            <div class="qb-circuit-rate">
              <span class="qb-rate-label">隔离率</span>
              <el-progress :percentage="Math.min(quarantineStats.quarantineRate, 100)" :color="circuitState.color"
                :stroke-width="14" :format="() => `${quarantineStats.quarantineRate}%`" />
              <span class="qb-threshold">阈值 {{ quarantineStats.threshold }}%</span>
            </div>
            <div class="qb-circuit-counts">
              <span>待处理 <b>{{ quarantineStats.pending }}</b></span>
              <span>已修复 <b>{{ quarantineStats.resolved }}</b></span>
              <span>已忽略 <b>{{ quarantineStats.ignored }}</b></span>
            </div>
          </div>

          <!-- 筛选 -->
          <div class="qb-filter">
            <el-select v-model="qFilter.status" placeholder="状态" clearable style="width: 140px"
              @change="loadQuarantine">
              <el-option label="待处理" value="pending" />
              <el-option label="已修复" value="resolved" />
              <el-option label="已忽略" value="ignored" />
            </el-select>
            <el-select v-model="qFilter.interfaceName" placeholder="接口" clearable filterable style="width: 200px"
              @change="loadQuarantine">
              <el-option v-for="iface in quarantineInterfaces" :key="iface" :label="iface" :value="iface" />
            </el-select>
            <el-button :icon="Refresh" @click="loadQuarantine">刷新</el-button>
          </div>

          <!-- 表格 -->
          <el-table :data="quarantineList" empty-text="暂无隔离记录" style="width: 100%; margin-top: 12px">
            <el-table-column prop="interfaceName" label="接口" min-width="170" />
            <el-table-column prop="pkValue" label="PK 值" min-width="140" show-overflow-tooltip />
            <el-table-column label="拒绝原因" width="130">
              <template #default="{ row }">
                <el-tag :type="reasonTag(row.rejectionReason)" size="small">{{ reasonLabel(row.rejectionReason)
                  }}</el-tag>
              </template>
            </el-table-column>
            <el-table-column label="原始数据" min-width="100">
              <template #default="{ row }">
                <el-button text type="primary" @click="showRaw(row)">查看</el-button>
              </template>
            </el-table-column>
            <el-table-column label="状态" width="100">
              <template #default="{ row }">
                <el-tag :type="statusTag(row.status)" size="small" effect="plain">{{ statusLabel(row.status) }}</el-tag>
              </template>
            </el-table-column>
            <el-table-column label="时间" width="170">
              <template #default="{ row }">{{ fmtDateTime(row.createdAt) }}</template>
            </el-table-column>
            <el-table-column label="操作" width="150">
              <template #default="{ row }">
                <div class="action-btns">
                  <el-button v-if="row.status === 'pending'" text type="success" @click="onRetry(row.id)">重试</el-button>
                  <el-button v-if="row.status === 'pending'" text type="danger" @click="onIgnore(row.id)">忽略</el-button>
                  <span v-if="row.status !== 'pending'" class="count-dim">—</span>
                </div>
              </template>
            </el-table-column>
          </el-table>
          <div class="qb-pager" v-if="qTotal > 0">
            <el-pagination layout="total, prev, pager, next" :total="qTotal" :page-size="qPageSize"
              :current-page="qPage" @current-change="(p: number) => { qPage = p; loadQuarantine() }" />
          </div>
        </div>
      </el-tab-pane>
    </el-tabs>

    <!-- F2.3 — 原始数据弹窗 -->
    <el-dialog v-model="rawDialog" title="原始数据" width="720px" destroy-on-close>
      <pre class="raw-json">{{ rawJsonText }}</pre>
    </el-dialog>

    <!-- 日志弹窗 -->
    <el-dialog v-model="logDialog" title="同步详情" width="680px" destroy-on-close>
      <div class="log-detail" v-if="logBatch">
        <!-- 同步摘要 -->
        <div class="log-summary-grid">
          <div class="log-sum-item">
            <span class="log-sum-label">状态</span>
            <el-tag :type="batchType[logBatch.status]" effect="plain" size="small">{{ batchLabel[logBatch.status] ??
              logBatch.status }}</el-tag>
          </div>
          <div class="log-sum-item" v-if="logBatch.sourceSignature">
            <span class="log-sum-label">接口</span>
            <span class="log-sum-val"><span class="iface-tag">{{ logBatch.sourceSignature }}</span></span>
          </div>
          <div class="log-sum-item">
            <span class="log-sum-label">触发方式</span>
            <span class="log-sum-val">{{ triggerLabel[logBatch.triggerType] ?? logBatch.triggerType }}</span>
          </div>
          <div class="log-sum-item">
            <span class="log-sum-label">耗时</span>
            <span class="log-sum-val" v-if="logBatch.startedAt && logBatch.finishedAt">{{ duration(logBatch.startedAt,
              logBatch.finishedAt) }}</span>
            <span class="log-sum-val" v-else>-</span>
          </div>
          <div class="log-sum-item">
            <span class="log-sum-label">拉取行数</span>
            <span class="log-sum-val">{{ logBatch.recordCount?.toLocaleString() ?? 0 }}</span>
          </div>
          <div class="log-sum-item">
            <span class="log-sum-label">写入行数<small class="log-sub">（实际变更）</small></span>
            <span class="log-sum-val log-ok-val">{{ logBatch.successCount?.toLocaleString() ?? 0 }}</span>
          </div>
          <div class="log-sum-item">
            <span class="log-sum-label">跳过行数<small class="log-sub">（已存在未变）</small></span>
            <span class="log-sum-val" :class="{ 'log-warn-val': (logBatch.skipCount ?? 0) > 0 }">{{
              logBatch.skipCount?.toLocaleString() ?? 0 }}</span>
          </div>
          <div class="log-sum-item">
            <span class="log-sum-label">拒绝行数</span>
            <span class="log-sum-val" :class="{ 'log-err-val': (logBatch.failCount ?? 0) > 0 }">{{
              logBatch.failCount?.toLocaleString() ?? 0 }}</span>
          </div>
        </div>

        <!-- 时间范围 -->
        <div class="log-time-row" v-if="logBatch.startedAt">
          <span class="log-sum-label">执行时间</span>
          <span class="log-sum-val">{{ fmtDateTime(logBatch.startedAt) }} → {{ fmtDateTime(logBatch.finishedAt) || '进行中'
            }}</span>
        </div>

        <!-- 最后步骤 -->
        <div class="log-step-row" v-if="logBatch.progressStep">
          <span class="log-sum-label">最后步骤</span>
          <code class="log-step-code">{{ logBatch.progressStep }}</code>
        </div>

        <!-- 错误摘要 -->
        <el-alert v-if="logBatch.errorSummary" :title="logBatch.errorSummary" type="error" :closable="false" show-icon
          style="margin-top: 12px" />

        <!-- 错误清单 -->
        <el-table v-if="errorList.length > 0" :data="errorList" stripe style="margin-top: 12px">
          <el-table-column prop="errorType" label="类型" width="100" />
          <el-table-column prop="errorMessage" label="错误信息" min-width="250" />
          <el-table-column label="位置" width="100">
            <template #default="{ row: e }">{{ e.fieldName || (e.rowNumber ? '行 ' + e.rowNumber : '-') }}</template>
          </el-table-column>
          <el-table-column prop="createdAt" label="时间" width="160">
            <template #default="{ row: e }">{{ fmtDateTime(e.createdAt) }}</template>
          </el-table-column>
        </el-table>
      </div>
    </el-dialog>
  </div>
</template>

<script setup lang="ts">
import { computed, onMounted, onUnmounted, reactive, ref, watch } from 'vue'
import { useRoute } from 'vue-router'
import { Edit, VideoPlay, Refresh } from '@element-plus/icons-vue'
import { ElMessage, ElMessageBox } from 'element-plus'
import { ingestionService, type IngestionBatch, type ImportError, type IngestionTask, type SchemaChange, type Reconciliation } from '@/api'
import { SCHEMA_CHANGE_LABELS, RECON_STATUS_LABELS, CHECK_LEVEL_LABELS, SYNC_MODE_LABELS } from '@/constants/ingestion'
import { fmtDateTime } from '@/utils/datetime'
import Index from '@/components/page-header/index.vue'
import { Crud, Table } from '@/components/crud'
import type { ColumnSchema } from '@/components/crud'

const route = useRoute()
const taskId = route.params.id as string
const task = ref<IngestionTask | null>(null)
const batches = ref<(IngestionBatch & { _pct?: number; _step?: string })[]>([])
const activeTab = ref('batches')

// 执行记录树形分组：基于后端显式维护的 parent_id 关联
// （多接口任务：子接口批次 parent_id 指向其「(汇总)」父批次）。
// 不再依赖「(汇总) 哨兵 + 时间连续归组」的脆弱推断，可正确处理
// 「同一分钟多次运行交错 / 双 (汇总) 同秒」等场景，父子关系 100% 准确。
const isSummary = (row: any) =>
  (row.sourceSignature || '') === '(汇总)' ||
  ((row.sourceSignature || '') === '' && (row.status === 'running' || row.status === 'pending'))
const expandedKeys = ref<string[]>([])
const groupedBatches = computed(() => {
  const all = batches.value
  const byId = new Map<string, any>()
  for (const r of all) byId.set(r.id, r)
  // parentId -> 子批次列表
  const childrenOf = new Map<string, any[]>()
  for (const r of all) {
    const pid = (r as any).parentId
    if (pid && byId.has(pid)) {
      if (!childrenOf.has(pid)) childrenOf.set(pid, [])
      childrenOf.get(pid)!.push(r)
    }
  }
  const out: any[] = []
  for (const r of all) {
    // 顶层行 = parentId 为空的批次（(汇总) 父 或 单接口独立行）
    if (!(r as any).parentId) {
      const kids = (childrenOf.get(r.id) || []).slice()
      kids.sort((a: any, b: any) =>
        new Date(b.createdAt).getTime() - new Date(a.createdAt).getTime())
      out.push({ ...r, isSummary: isSummary(r), children: kids.map((c: any) => ({ ...c, isChild: true })) })
    }
  }
  out.sort((a, b) => new Date(b.createdAt).getTime() - new Date(a.createdAt).getTime())
  for (const g of out) {
    if (g.children?.length) {
      g.children.sort((a: any, b: any) =>
        new Date(b.createdAt).getTime() - new Date(a.createdAt).getTime())
    }
  }
  return out
})
// 新出现的汇总父节点默认展开（row-key=id 稳定，poll 重算后展开状态保持）
watch(groupedBatches, (g) => {
  for (const grp of g) {
    if (grp.id && !expandedKeys.value.includes(grp.id as string)) {
      expandedKeys.value.push(grp.id as string)
    }
  }
}, { immediate: true })
function onExpandChange(_row: any, expandedRows: any[]) {
  expandedKeys.value = expandedRows.map((r) => r.id as string)
}
function batchRowClass({ row }: any): string {
  return row.isSummary ? 'batch-row-summary' : ''
}
const executing = ref(false)
const logDialog = ref(false)
const isEditing = ref(route.query.edit === '1')
const editForm = reactive({ name: '', scheduleType: 'manual', cronExpression: '', description: '' })
const saving = ref(false)
const logBatch = ref<IngestionBatch | null>(null)
const errorList = ref<ImportError[]>([])
// F1.2 — Schema 变更审计
const schemaChanges = ref<SchemaChange[]>([])
const schemaChangeLoading = ref(false)
const schemaChangeCount = computed(() => schemaChanges.value.length)

// F1.3 — 数据对账
const reconciliations = ref<Reconciliation[]>([])
const reconLoading = ref(false)
const reconDialog = ref(false)
const reconDetail = ref<Reconciliation | null>(null)
const reconDetailLoading = ref(false)

// F2.4 — 详情页调度状态展示（定时任务显示下次执行）
const nextRun = ref<string | null>(null)
const nextRunLoading = ref(false)
async function loadNextRun() {
  if (task.value?.scheduleType !== 'cron' || !task.value?.cronExpression) {
    nextRun.value = null
    return
  }
  nextRunLoading.value = true
  try {
    const r = await ingestionService.previewCron(task.value.cronExpression)
    nextRun.value = r && r.isValid ? r.nextRun : null
  } catch {
    nextRun.value = null
  } finally {
    nextRunLoading.value = false
  }
}

// F2.3 — 隔离区（依赖 B2.6 端点）
const quarantineList = ref<any[]>([])
const quarantineStats = ref({
  total: 0, pending: 0, resolved: 0, ignored: 0,
  quarantineRate: 0, threshold: 5, circuitBreakerTriggered: false,
})
const quarantineLoading = ref(false)
const qFilter = reactive({ status: '', interfaceName: '' })
const quarantineInterfaces = ref<string[]>([])
const qPage = ref(1)
const qPageSize = ref(20)
const qTotal = ref(0)
const rawDialog = ref(false)
const rawJsonText = ref('')

const circuitState = computed(() => {
  const rate = quarantineStats.value.quarantineRate
  const thr = quarantineStats.value.threshold || 5
  if (quarantineStats.value.circuitBreakerTriggered || rate >= thr) {
    return { type: 'danger' as const, label: '熔断', color: '#f56c6c' }
  }
  if (rate >= thr * 0.6) {
    return { type: 'warning' as const, label: '告警', color: '#e6a23c' }
  }
  return { type: 'success' as const, label: '正常', color: '#67c23a' }
})

function reasonLabel(r: string): string {
  return { null_pk: '主键为空', dup_in_batch: '批内重复', write_error: '写入失败' }[r] ?? r
}
function reasonTag(r: string): '' | 'success' | 'warning' | 'danger' | 'info' {
  if (r === 'null_pk') return 'danger'
  if (r === 'dup_in_batch') return 'warning'
  if (r === 'write_error') return 'danger'
  return 'info'
}
function statusLabel(s: string): string {
  return { pending: '待处理', resolved: '已修复', ignored: '已忽略' }[s] ?? s
}
function statusTag(s: string): '' | 'success' | 'warning' | 'danger' | 'info' {
  if (s === 'pending') return 'warning'
  if (s === 'resolved') return 'success'
  if (s === 'ignored') return 'info'
  return 'info'
}

// F3.2 — 软删除检测接口列表（从 task.config 读取启用状态与最近检测结果）
const softDeleteChecking = ref(false)
const softDeleteInterfaces = computed(() => {
  const cfg = (task.value?.config || {}) as any
  const softDeleteMap: Record<string, boolean> = cfg.softDelete || {}
  const last: any = cfg.softDeleteLast || {}
  const byIface: Record<string, any> = last.byInterface || {}
  const names: string[] = cfg.interfaces || []
  return names.map((name: string) => {
    const r = byIface[name] || {}
    return {
      name,
      enabled: !!softDeleteMap[name],
      lastCheckedAt: last.checkedAt || null,
      lastDeleted: r.deleted ?? null,
      lastSkipped: !!r.skipped,
      lastReason: r.reason || '',
    }
  })
})

async function triggerSoftDelete() {
  if (!task.value?.id) return
  softDeleteChecking.value = true
  try {
    await ingestionService.softDeleteCheck(task.value.id)
    ElMessage.success('软删除检测已启动（异步执行）')
    // 稍后刷新，读取 task.config.softDeleteLast 结果
    setTimeout(async () => {
      try {
        await load()
      } catch {
        /* ignore */
      }
    }, 1500)
  } catch {
    ElMessage.error('软删除检测启动失败')
  } finally {
    softDeleteChecking.value = false
  }
}

async function loadQuarantine() {
  quarantineLoading.value = true
  try {
    const res: any = await ingestionService.getQuarantine(taskId, {
      status: qFilter.status || undefined,
      interfaceName: qFilter.interfaceName || undefined,
      page: qPage.value,
      pageSize: qPageSize.value,
    })
    const items = res?.items ?? []
    quarantineList.value = items
    qTotal.value = res?.total ?? items.length
    // 收集接口名用于筛选下拉
    const ifaces = new Set(quarantineInterfaces.value)
    items.forEach((i: any) => i.interfaceName && ifaces.add(i.interfaceName))
    quarantineInterfaces.value = Array.from(ifaces)
  } catch (e) {
    console.error('加载隔离区失败:', e)
  } finally {
    quarantineLoading.value = false
  }
}

async function loadQuarantineStats() {
  try {
    const stats: any = await ingestionService.getQuarantineStats(taskId)
    if (stats) quarantineStats.value = stats
  } catch (e) {
    console.error('加载隔离区统计失败:', e)
  }
}

function showRaw(row: any) {
  try {
    rawJsonText.value = JSON.stringify(row.rawJson, null, 2)
  } catch {
    rawJsonText.value = String(row.rawJson)
  }
  rawDialog.value = true
}

async function onRetry(id: string) {
  try {
    await ingestionService.retryQuarantine(id)
    ElMessage.success('重试已提交')
    await Promise.all([loadQuarantine(), loadQuarantineStats()])
  } catch { /* handled */ }
}

async function onIgnore(id: string) {
  try {
    await ElMessageBox.confirm('确认忽略该隔离记录？忽略后不可重试。', '忽略确认', { type: 'warning' })
    await ingestionService.ignoreQuarantine(id)
    ElMessage.success('已忽略')
    await Promise.all([loadQuarantine(), loadQuarantineStats()])
  } catch (e) {
    // 用户取消不提示
    if (e === 'cancel') return
  }
}

// 概览卡片：最近对账时间 / 数据一致 / 存在差异 / 待修复
const reconSummary = computed(() => {
  const list = reconciliations.value
  const lastCheck = list.length
    ? list.reduce((m, r) => (r.checkedAt > m ? r.checkedAt : m), list[0].checkedAt)
    : null
  const consistent = list.filter(r => r.status === 'pass' || r.status === 'repaired').length
  const diff = list.filter(r => r.status === 'warning').length
  const toRepair = list.filter(r => r.status === 'failed').length
  return { lastCheck, consistent, diff, toRepair }
})
let _esList: EventSource[] = []
let _tickTimer: ReturnType<typeof setInterval> | null = null
let _pollTimer: ReturnType<typeof setInterval> | null = null

function startTick() {
  if (_tickTimer) return
  _tickTimer = setInterval(() => {
    // Force re-render so elapsed() timer updates every second
    batches.value = [...batches.value]
  }, 1000)
}
function stopTick() {
  if (_tickTimer) { clearInterval(_tickTimer); _tickTimer = null }
}

// 一次性拉取该任务的全部批次（后端按 page_size 分页，但前端需要完整数据做客户端分页）。
// 用后端返回的 real total 计算总页数翻页，避免只取到第一页导致「执行记录只显示少量」的问题。
async function fetchAllBatches(taskId: string): Promise<any[]> {
  const pageSize = 100
  const first = await ingestionService.getBatches(taskId, { page: 1, pageSize })
  const total: number = (first as any)?.total ?? (first as any)?.items?.length ?? 0
  const all: any[] = [...((first as any).items ?? [])]
  const totalPages = Math.max(1, Math.ceil(total / pageSize))
  for (let page = 2; page <= totalPages; page++) {
    const b = await ingestionService.getBatches(taskId, { page, pageSize })
    all.push(...((b as any).items ?? []))
  }
  return all
}

// Re-fetch batches periodically while any are still running.
// The engine creates one batch per interface for a multi-interface task, but the
// SSE progress stream is only opened for the first batch. Secondary batches (e.g.
// OEE) have no SSE stream of their own, so without this poll their status would
// stay "running" forever even after they finished on the backend.
async function pollRunning() {
  try {
    const items = await fetchAllBatches(taskId)
    batches.value = items
    const hasRunning = items.some((x: any) => x.status === 'running' || x.status === 'pending')
    if (!hasRunning) stopPolling()
  } catch { /* ignore transient poll errors */ }
}
function startPolling() {
  if (_pollTimer) return
  _pollTimer = setInterval(pollRunning, 3000)
}
function stopPolling() {
  if (_pollTimer) { clearInterval(_pollTimer); _pollTimer = null }
}

const batchLabel: Record<string, string> = { pending: '等待中', running: '运行中', success: '成功', partial_success: '部分成功', failed: '失败', cancelled: '已取消' }
const batchType: Record<string, '' | 'success' | 'warning' | 'danger' | 'info'> = { pending: 'info', running: '', success: 'success', partial_success: 'warning', failed: 'danger', cancelled: 'info' }
const triggerLabel: Record<string, string> = { manual: '手动', scheduled: '定时', retry: '重试', backfill: '全量回溯', quick_fill: '快补' }

const summary = computed(() => [
  { label: '调度', value: task.value?.scheduleType === 'cron' ? `定时 ${task.value?.cronExpression}` : task.value?.scheduleType ?? '-' },
  { label: '最近同步', value: fmtDateTime(task.value?.lastSyncAt, false) || '未同步过' },
  { label: '上次结果', value: task.value?.lastSyncStatus || '-' },
])
const batchesPagination = reactive({
  page: 1,
  pageSize: 20,
  total: 0,
  onPageChange(p: number) { batchesPagination.page = p },
  onSizeChange(s: number) { batchesPagination.pageSize = s; batchesPagination.page = 1 },
})

// 分页按「运行组」切片：每组 = 一次同步的 (汇总) 父 + 其接口子节点，
// 避免按行分页把同一组的父子拆到两页、破坏树形折叠。
watch(groupedBatches, (g) => {
  batchesPagination.total = g.length
  const maxPage = Math.max(1, Math.ceil(g.length / batchesPagination.pageSize))
  if (batchesPagination.page > maxPage) batchesPagination.page = maxPage
}, { immediate: true })

const pagedBatches = computed(() => {
  const start = (batchesPagination.page - 1) * batchesPagination.pageSize
  return groupedBatches.value.slice(start, start + batchesPagination.pageSize)
})

const batchesColumns: ColumnSchema[] = [
  { type: 'custom', prop: 'sourceSignature', label: '接口', width: 180 },
  { type: 'custom', prop: 'createdAt', label: '时间', width: 170 },
  { type: 'custom', prop: 'triggerType', label: '触发', width: 90 },
  { type: 'custom', prop: 'status', label: '状态 / 进度', width: 200 },
  { type: 'custom', prop: 'successCount', label: '数据量' },
  { type: 'custom', prop: 'duration', label: '耗时', width: 80 },
  { type: 'custom', prop: 'actions', label: '操作', width: 160 },
]

function duration(start: string, end: string): string {
  const s = (new Date(end).getTime() - new Date(start).getTime()) / 1000
  if (s < 60) return `${s.toFixed(0)}s`
  return `${Math.floor(s / 60)}m${(s % 60).toFixed(0)}s`
}
function elapsed(start: string): string {
  const s = (Date.now() - new Date(start).getTime()) / 1000
  if (s < 60) return `${s.toFixed(0)}s`
  return `${Math.floor(s / 60)}m${(s % 60).toFixed(0)}s`
}
function ifaceLabel(row: any): string {
  if (row.sourceSignature) return row.sourceSignature
  const ps = row.progressStep || ''
  const m = ps.match(/([A-Za-z][A-Za-z0-9_]*)/)
  return m ? m[1] : '—'
}

// F1.2 — Schema 变更审计：后端接口（B1.4）未实现时静默失败，不阻塞页面
function schemaChangeTagType(t: string): '' | 'success' | 'warning' | 'danger' | 'info' {
  if (t === 'added') return 'warning'
  if (t === 'removed') return 'danger'
  if (t === 'type_changed') return 'info'
  return 'info'
}

async function loadSchemaChanges() {
  schemaChangeLoading.value = true
  try {
    const res = await ingestionService.getSchemaChanges(taskId)
    const list = res && Array.isArray((res as any).items)
      ? (res as any).items
      : Array.isArray(res) ? res : []
    schemaChanges.value = list as SchemaChange[]
  } catch (e) {
    console.error('加载 Schema 变更失败:', e)
    schemaChanges.value = []
  } finally {
    schemaChangeLoading.value = false
  }
}

// F1.3 — 数据对账：后端接口（B1.4）未实现时静默失败，不阻塞页面
async function loadReconciliations() {
  reconLoading.value = true
  try {
    const res = await ingestionService.getReconciliations(taskId, { pageSize: 50 })
    const list = res && Array.isArray((res as any).items)
      ? (res as any).items
      : Array.isArray(res) ? res : []
    reconciliations.value = list as Reconciliation[]
  } catch (e) {
    console.error('加载对账记录失败:', e)
    reconciliations.value = []
  } finally {
    reconLoading.value = false
  }
}

async function showReconDetail(row: Reconciliation) {
  reconDetailLoading.value = true
  reconDialog.value = true
  try {
    reconDetail.value = await ingestionService.getReconciliation(row.id)
  } catch (e) {
    console.error('加载对账详情失败:', e)
    reconDetail.value = null
  } finally {
    reconDetailLoading.value = false
  }
}

async function handleTriggerRecon(level: 'L1' | 'L2' | 'L3') {
  try {
    await ingestionService.triggerReconciliation(taskId, level)
    ElMessage.success(`${level} 对账已触发`)
    await loadReconciliations()
  } catch { /* handled */ }
}

async function handleRepair(reconId: string) {
  try {
    await ingestionService.repairReconciliation(reconId)
    ElMessage.success('修复已提交')
    await loadReconciliations()
  } catch { /* handled */ }
}

async function load() {
  task.value = await ingestionService.get(taskId)
  // F2.4 — 定时任务下次执行时间
  await loadNextRun()
  const allItems = await fetchAllBatches(taskId)
  batches.value = allItems
  // Start/stop tick + polling timers based on whether any batch is running
  const hasRunning = allItems.some((x: any) => x.status === 'running' || x.status === 'pending')
  if (hasRunning) { startTick(); startPolling() }
  else { stopTick(); stopPolling() }
  // F1.2 — Schema 变更审计列表
  await loadSchemaChanges()
  // F1.3 — 数据对账记录
  await loadReconciliations()
  // F2.3 — 隔离区（页面加载即拉取，Tab 切换时也会刷新）
  await loadQuarantine()
  await loadQuarantineStats()
}

async function handleExecute() {
  executing.value = true
  try {
    const { batchId } = await ingestionService.execute(taskId)
    ElMessage.success('已提交')
    const placeholder: any = {
      id: batchId, triggerType: 'manual', status: 'pending',
      recordCount: 0, successCount: 0, failCount: 0,
      sourceSignature: '(汇总)',
      createdAt: new Date().toISOString(),
      _pct: -1, _step: '等待 Worker...',
    }
    // 追加到末尾而非头部：聚合(汇总)行在最终列表里应始终排在最后，
    // 若插到头部会产生"刚点同步时汇总先出现"的错觉（后端按 created_at
    // 倒序时，汇总批次 created_at 最早，本就落在每个运行批次的底部）。
    batches.value.push(placeholder)
    startTick()
    const es = ingestionService.streamProgress(batchId,
      (d) => {
        const b = batches.value.find(x => x.id === batchId)
        if (b) {
          b._pct = d.pct
          b._step = d.step
          if (d.status === 'running') {
            b.status = 'running'
            if (d.startedAt) (b as any).startedAt = d.startedAt
          } else if (d.status !== 'pending') {
            b.status = d.status === 'success' ? 'success' : d.status === 'cancelled' ? 'cancelled' : 'failed'
          }
          if (d.recordCount !== undefined) (b as any).recordCount = d.recordCount
          if (d.successCount !== undefined) (b as any).successCount = d.successCount
          if (d.failCount !== undefined) (b as any).failCount = d.failCount
          if (d.skipCount !== undefined) (b as any).skipCount = d.skipCount
          if (d.sourceSignature !== undefined && d.sourceSignature) (b as any).sourceSignature = d.sourceSignature
        }
      },
      () => { stopTick(); load() },
    )
    _esList.push(es)
  } catch { /* */ } finally { executing.value = false }
}

async function handleRetry(bid: string) {
  try { await ingestionService.retryBatch(bid); ElMessage.success('重试已提交'); await load() } catch { /* */ }
}
async function handleCancel(bid: string) {
  try { await ingestionService.cancelBatch(bid); ElMessage.success('已停止') } catch { /* */ }
}
async function showLog(row: IngestionBatch) {
  logBatch.value = row
  const e = await ingestionService.getBatchErrors(row.id, { pageSize: 50 })
  errorList.value = e.items
  logDialog.value = true
}

function toggleEdit() {
  isEditing.value = true
  activeTab.value = 'config'
  if (task.value) {
    editForm.name = task.value.name
    editForm.scheduleType = task.value.scheduleType
    editForm.cronExpression = task.value.cronExpression || ''
    editForm.description = task.value.description || ''
  }
}

function handleCancelEdit() {
  isEditing.value = false
}

async function handleSave() {
  if (!task.value) return
  saving.value = true
  try {
    const data: Record<string, unknown> = {}
    if (editForm.name !== task.value.name) data.name = editForm.name
    if (editForm.scheduleType !== task.value.scheduleType) {
      data.scheduleType = editForm.scheduleType
      data.cronExpression = editForm.scheduleType === 'cron' ? editForm.cronExpression || undefined : undefined
    } else if (editForm.scheduleType === 'cron' && editForm.cronExpression !== (task.value.cronExpression || '')) {
      data.cronExpression = editForm.cronExpression || undefined
    }
    if (editForm.description !== (task.value.description || '')) data.description = editForm.description || undefined

    if (Object.keys(data).length === 0) {
      ElMessage.info('无变更')
      isEditing.value = false
      return
    }

    await ingestionService.update(taskId, data)
    ElMessage.success('已更新')
    isEditing.value = false
    await load()
  } catch { /* handled */ } finally { saving.value = false }
}

onMounted(load)
onUnmounted(() => { _esList.forEach(es => es.close()); stopTick(); stopPolling() })

// F2.3 — 切换到隔离区 Tab 时刷新数据
watch(activeTab, (t) => {
  if (t === 'quarantine') {
    loadQuarantine()
    loadQuarantineStats()
  }
})
</script>

<style lang="scss" scoped>
.page {}

.summary-row {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 12px;
  margin-bottom: 16px;
}

.sum-item {
  display: flex;
  flex-direction: column;
  gap: 4px;
  padding: 14px 16px;
  border: 1px solid $color-border-light;
  border-radius: 6px;
}

.sum-label {
  font-size: $font-size-xs;
  color: $color-text-placeholder;
}

.sum-val {
  font-size: $font-size-lg;
  font-weight: $font-weight-semibold;
}

.empty {
  text-align: center;
  padding: 60px;
  color: $color-text-placeholder;
}

.status-cell {
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.step-text {
  font-size: 11px;
  color: $color-primary;
}

.err-text {
  font-size: 11px;
  color: $color-danger;
}

.count-ok {
  font-weight: $font-weight-semibold;
  color: $color-success;
}

.count-err {
  color: $color-danger;
  font-size: $font-size-xs;
}

.count-warn {
  color: #ca8a04;
  font-size: $font-size-xs;
}

.count-dim {
  color: $color-text-placeholder;
}

.dur-text {
  color: $color-text-secondary;
  font-size: $font-size-sm;
}

.trigger-text {
  color: $color-text-secondary;
  font-size: $font-size-sm;
}

.iface-tag {
  display: inline-block;
  padding: 1px 8px;
  border-radius: 4px;
  background: rgba(0, 0, 0, 0.04);
  color: $color-text-secondary;
  font-size: 11px;
  font-family: monospace;
}

.iface-tag-agg {
  background: rgba(64, 158, 255, 0.12);
  color: #2563eb;
  font-weight: 600;
}

// 执行记录树形缩进现由 el-table 原生(.el-table__indent)负责：
// table.vue 在 tree 模式(.tree-mode)下已对树形表关闭 flex / auto 布局，
// 故此处无需手动兜底，子节点会自动获得 level×16px 的原生缩进。
// 执行记录树形：汇总父节点行加底色/加粗，与子节点区分
:deep(.batch-row-summary)>td.el-table__cell {
  background: #f5f7fa;
}

:deep(.batch-row-summary) .iface-tag-agg {
  font-size: 12px;
}

:deep(.el-table__row.batch-row-summary) {
  font-weight: 600;
}

.action-btns {
  display: flex;
  align-items: center;
  gap: 4px;
}

.log-summary-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 12px;
  padding: 12px 0;
  border-bottom: 1px solid $color-border-light;
}

.log-sum-item {
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.log-sum-label {
  font-size: 12px;
  color: $color-text-placeholder;
}

.log-sum-val {
  font-size: 14px;
  font-weight: $font-weight-semibold;
  color: $color-text-primary;
}

.log-ok-val {
  color: $color-success;
}

.log-err-val {
  color: $color-danger;
}

.log-warn-val {
  color: #ca8a04;
}

.log-sub {
  font-size: 11px;
  color: $color-text-placeholder;
  margin-left: 2px;
  font-weight: normal;
}

.log-time-row,
.log-step-row {
  display: flex;
  align-items: flex-start;
  gap: 8px;
  padding: 8px 0;
  font-size: 13px;
}

.log-step-code {
  font-size: 12px;
  color: $color-primary;
  background: rgba(0, 0, 0, 0.04);
  padding: 2px 8px;
  border-radius: 4px;
  word-break: break-all;
  flex: 1;
}

/* F1.3 — 数据对账 */
.recon-cards {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 12px;
  margin-bottom: 4px;
}

.recon-card {
  display: flex;
  flex-direction: column;
  gap: 6px;
  padding: 14px 16px;
  border: 1px solid $color-border-light;
  border-radius: 6px;
}

.recon-card-label {
  font-size: $font-size-xs;
  color: $color-text-placeholder;
}

.recon-card-val {
  font-size: $font-size-lg;
  font-weight: $font-weight-semibold;
  color: $color-text-primary;
}

.recon-card-err {
  color: $color-danger;
}

.recon-summary-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 12px;
  padding: 12px 0;
  border-bottom: 1px solid $color-border-light;
}

.recon-sum-item {
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.recon-label {
  font-size: 12px;
  color: $color-text-placeholder;
}

.recon-val {
  font-size: 14px;
  font-weight: $font-weight-semibold;
  color: $color-text-primary;
}

.recon-sub {
  font-size: 12px;
  font-weight: $font-weight-normal;
  color: $color-text-placeholder;
}

.diff-ok {
  color: $color-success;
  font-weight: $font-weight-semibold;
}

.diff-warn {
  color: #ca8a04;
  font-weight: $font-weight-semibold;
}

.diff-err {
  color: $color-danger;
  font-weight: $font-weight-semibold;
}

/* F2.4 — 调度状态展示 */
.sched-block {
  display: flex;
  align-items: center;
  gap: 8px;
  flex-wrap: wrap;
}

.cron-code {
  font-family: monospace;
  background: rgba(0, 0, 0, 0.04);
  padding: 1px 8px;
  border-radius: 4px;
  font-size: 13px;
  color: $color-text-primary;
}

.sched-next {
  font-size: 12px;
  color: $color-text-secondary;
}

.sched-dim {
  color: $color-text-placeholder;
}

/* F2.3 — 隔离区 */
.qb-circuit {
  padding: 16px;
  border: 1px solid $color-border-light;
  border-radius: 8px;
  margin-bottom: 16px;
  background: rgba(0, 0, 0, 0.015);
}

.qb-circuit-head {
  display: flex;
  align-items: center;
  gap: 10px;
  margin-bottom: 12px;
}

.qb-circuit-title {
  font-size: 14px;
  font-weight: $font-weight-semibold;
}

.qb-circuit-rate {
  display: flex;
  align-items: center;
  gap: 12px;
}

.qb-rate-label {
  font-size: 13px;
  color: $color-text-secondary;
  white-space: nowrap;
}

.qb-circuit-rate :deep(.el-progress) {
  flex: 1;
}

.qb-threshold {
  font-size: 12px;
  color: $color-text-placeholder;
  white-space: nowrap;
}

.qb-circuit-counts {
  display: flex;
  gap: 24px;
  margin-top: 12px;
  font-size: 13px;
  color: $color-text-secondary;
}

.qb-circuit-counts b {
  color: $color-text-primary;
  font-size: 15px;
}

.qb-filter {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 8px;
}

.qb-pager {
  display: flex;
  justify-content: flex-end;
  margin-top: 12px;
}

.raw-json {
  background: #1e1e2e;
  color: #cdd6f4;
  padding: 16px;
  border-radius: 6px;
  font-size: 12px;
  line-height: 1.6;
  max-height: 500px;
  overflow: auto;
  white-space: pre-wrap;
  word-break: break-all;
  font-family: monospace;
}

/* F3.2 — 软删除检测 */
.sd-count {
  font-size: 12px;
  color: $color-danger;
  margin-left: 8px;
}

.sd-dim {
  color: $color-text-placeholder;
}
</style>