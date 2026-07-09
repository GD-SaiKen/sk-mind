import { useState } from "react";
import { Badge } from "../components/ui/badge";
import { Button } from "../components/ui/button";
import { Input } from "../components/ui/input";
import {
  Table, TableBody, TableCell, TableHead, TableHeader, TableRow,
} from "../components/ui/table";
import { Settings, Edit, Plus, Search } from "lucide-react";

const tabs = ["数据源类型", "接入方式", "质量状态", "敏感字段类型", "业务标签", "平台参数"];

const dataSourceTypes = [
  { id: "1", code: "ERP", name: "ERP 系统", description: "企业资源计划系统", status: "启用" },
  { id: "2", code: "MES", name: "MES 系统", description: "制造执行系统", status: "启用" },
  { id: "3", code: "EXCEL", name: "Excel 文件", description: "Excel 表格文件导入", status: "启用" },
];

const ingestionMethods = [
  { id: "1", code: "DB_SYNC", name: "数据库同步", description: "通过数据库连接直接同步", status: "启用" },
  { id: "2", code: "API", name: "API 拉取", description: "通过 API 接口拉取数据", status: "启用" },
  { id: "3", code: "FILE", name: "文件导入", description: "上传文件导入数据", status: "启用" },
];

const qualityStatuses = [
  { id: "1", code: "PASS", name: "通过", color: "green", description: "数据质量检查通过" },
  { id: "2", code: "WARNING", name: "警告", color: "yellow", description: "存在轻微质量问题" },
  { id: "3", code: "ERROR", name: "异常", color: "red", description: "存在严重质量问题" },
];

const sensitiveTypes = [
  { id: "1", code: "PII", name: "个人信息", description: "姓名、身份证号、电话等", maskingRule: "部分隐藏" },
  { id: "2", code: "FINANCIAL", name: "金融信息", description: "银行账号、薪资等", maskingRule: "完全隐藏" },
  { id: "3", code: "BUSINESS", name: "商业机密", description: "合同金额、客户信息等", maskingRule: "脱敏显示" },
];

const businessTags = [
  { id: "1", name: "财务", color: "blue", usageCount: 12 },
  { id: "2", name: "销售", color: "green", usageCount: 18 },
  { id: "3", name: "生产", color: "purple", usageCount: 8 },
  { id: "4", name: "人事", color: "orange", usageCount: 6 },
];

const platformParams = [
  { id: "1", key: "max_query_rows", name: "最大查询行数", value: "10000", description: "Agent 单次查询返回的最大行数" },
  { id: "2", key: "sync_frequency", name: "默认同步频率", value: "每日", description: "接入任务的默认执行频率" },
  { id: "3", key: "quality_check_enabled", name: "自动质量检查", value: "启用", description: "数据接入后自动执行质量检查" },
  { id: "4", key: "audit_retention_days", name: "审计日志保留天数", value: "90", description: "审计日志的保留时长" },
];

const actionLabel: Record<string, string> = {
  "数据源类型": "添加类型", "接入方式": "添加方式", "质量状态": "添加状态",
  "敏感字段类型": "添加类型", "业务标签": "添加标签", "平台参数": "添加参数",
};

const tagColorClass: Record<string, string> = {
  blue: "bg-blue-50 text-blue-700 border-blue-200",
  green: "bg-green-50 text-green-700 border-green-200",
  purple: "bg-purple-50 text-purple-700 border-purple-200",
  orange: "bg-orange-50 text-orange-700 border-orange-200",
};

export function SystemSettings() {
  const [activeTab, setActiveTab] = useState("数据源类型");
  const [searchTerm, setSearchTerm] = useState("");

  return (
    <div className="flex flex-col h-full">
      {/* 小标签 */}
      <div className="border-b border-gray-200 px-6">
        <div className="flex gap-0">
          {tabs.map(tab => (
            <button key={tab} onClick={() => setActiveTab(tab)}
              className={`px-4 py-2.5 text-sm border-b-2 transition-colors ${activeTab === tab ? "border-blue-600 text-blue-600 font-medium" : "border-transparent text-gray-500 hover:text-gray-800"}`}>
              {tab}
            </button>
          ))}
        </div>
      </div>

      <div className="flex-1 overflow-auto p-6 flex flex-col gap-4">
        {/* 筛选区 + 操作区 */}
        <div className="flex items-center gap-3">
          <div className="relative max-w-sm flex-1">
            <Search className="absolute left-3 top-1/2 -translate-y-1/2 size-4 text-gray-400" />
            <Input placeholder="搜索..." value={searchTerm} onChange={e => setSearchTerm(e.target.value)} className="pl-10" />
          </div>
          <div className="ml-auto">
            <Button><Plus className="size-4 mr-2" />{actionLabel[activeTab]}</Button>
          </div>
        </div>

        {/* 内容区 (设置页无统计卡片) */}
        {activeTab === "数据源类型" && (
          <div className="bg-white rounded-lg border border-gray-200">
            <Table>
              <TableHeader><TableRow><TableHead>类型编码</TableHead><TableHead>类型名称</TableHead><TableHead>描述</TableHead><TableHead>状态</TableHead><TableHead className="text-right">操作</TableHead></TableRow></TableHeader>
              <TableBody>
                {dataSourceTypes.map(t => (
                  <TableRow key={t.id}>
                    <TableCell className="font-mono text-sm">{t.code}</TableCell>
                    <TableCell>{t.name}</TableCell>
                    <TableCell className="text-sm text-gray-600">{t.description}</TableCell>
                    <TableCell><Badge variant="outline" className="bg-green-50 text-green-700 border-green-200">{t.status}</Badge></TableCell>
                    <TableCell><div className="flex justify-end"><Button variant="ghost" size="sm"><Edit className="size-4" /></Button></div></TableCell>
                  </TableRow>
                ))}
              </TableBody>
            </Table>
          </div>
        )}

        {activeTab === "接入方式" && (
          <div className="bg-white rounded-lg border border-gray-200">
            <Table>
              <TableHeader><TableRow><TableHead>方式编码</TableHead><TableHead>方式名称</TableHead><TableHead>描述</TableHead><TableHead>状态</TableHead><TableHead className="text-right">操作</TableHead></TableRow></TableHeader>
              <TableBody>
                {ingestionMethods.map(m => (
                  <TableRow key={m.id}>
                    <TableCell className="font-mono text-sm">{m.code}</TableCell>
                    <TableCell>{m.name}</TableCell>
                    <TableCell className="text-sm text-gray-600">{m.description}</TableCell>
                    <TableCell><Badge variant="outline" className="bg-green-50 text-green-700 border-green-200">{m.status}</Badge></TableCell>
                    <TableCell><div className="flex justify-end"><Button variant="ghost" size="sm"><Edit className="size-4" /></Button></div></TableCell>
                  </TableRow>
                ))}
              </TableBody>
            </Table>
          </div>
        )}

        {activeTab === "质量状态" && (
          <div className="bg-white rounded-lg border border-gray-200">
            <Table>
              <TableHeader><TableRow><TableHead>状态编码</TableHead><TableHead>状态名称</TableHead><TableHead>颜色标识</TableHead><TableHead>描述</TableHead><TableHead className="text-right">操作</TableHead></TableRow></TableHeader>
              <TableBody>
                {qualityStatuses.map(s => (
                  <TableRow key={s.id}>
                    <TableCell className="font-mono text-sm">{s.code}</TableCell>
                    <TableCell>{s.name}</TableCell>
                    <TableCell>
                      <Badge variant="outline" className={s.color === "green" ? "bg-green-50 text-green-700 border-green-200" : s.color === "yellow" ? "bg-yellow-50 text-yellow-700 border-yellow-200" : "bg-red-50 text-red-700 border-red-200"}>{s.color}</Badge>
                    </TableCell>
                    <TableCell className="text-sm text-gray-600">{s.description}</TableCell>
                    <TableCell><div className="flex justify-end"><Button variant="ghost" size="sm"><Edit className="size-4" /></Button></div></TableCell>
                  </TableRow>
                ))}
              </TableBody>
            </Table>
          </div>
        )}

        {activeTab === "敏感字段类型" && (
          <div className="bg-white rounded-lg border border-gray-200">
            <Table>
              <TableHeader><TableRow><TableHead>类型编码</TableHead><TableHead>类型名称</TableHead><TableHead>描述</TableHead><TableHead>默认脱敏规则</TableHead><TableHead className="text-right">操作</TableHead></TableRow></TableHeader>
              <TableBody>
                {sensitiveTypes.map(t => (
                  <TableRow key={t.id}>
                    <TableCell className="font-mono text-sm">{t.code}</TableCell>
                    <TableCell>{t.name}</TableCell>
                    <TableCell className="text-sm text-gray-600">{t.description}</TableCell>
                    <TableCell><Badge variant="outline" className="bg-orange-50 text-orange-700 border-orange-200">{t.maskingRule}</Badge></TableCell>
                    <TableCell><div className="flex justify-end"><Button variant="ghost" size="sm"><Edit className="size-4" /></Button></div></TableCell>
                  </TableRow>
                ))}
              </TableBody>
            </Table>
          </div>
        )}

        {activeTab === "业务标签" && (
          <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
            {businessTags.map(tag => (
              <div key={tag.id} className="p-4 bg-white border border-gray-200 rounded-lg">
                <div className="flex items-center justify-between mb-2">
                  <Badge variant="outline" className={tagColorClass[tag.color]}>{tag.name}</Badge>
                  <Button variant="ghost" size="sm"><Edit className="size-4" /></Button>
                </div>
                <div className="text-sm text-gray-500">使用次数: {tag.usageCount}</div>
              </div>
            ))}
          </div>
        )}

        {activeTab === "平台参数" && (
          <div className="bg-white rounded-lg border border-gray-200">
            <Table>
              <TableHeader><TableRow><TableHead>参数键</TableHead><TableHead>参数名称</TableHead><TableHead>当前值</TableHead><TableHead>描述</TableHead><TableHead className="text-right">操作</TableHead></TableRow></TableHeader>
              <TableBody>
                {platformParams.map(p => (
                  <TableRow key={p.id}>
                    <TableCell className="font-mono text-sm">{p.key}</TableCell>
                    <TableCell>{p.name}</TableCell>
                    <TableCell><Badge variant="outline">{p.value}</Badge></TableCell>
                    <TableCell className="text-sm text-gray-600">{p.description}</TableCell>
                    <TableCell><div className="flex justify-end"><Button variant="ghost" size="sm"><Edit className="size-4" /></Button></div></TableCell>
                  </TableRow>
                ))}
              </TableBody>
            </Table>
          </div>
        )}

        {/* 系统信息 (always visible at bottom) */}
        <div className="bg-white rounded-lg border border-gray-200 p-6">
          <div className="flex items-center gap-2 mb-4">
            <Settings className="size-4 text-gray-500" />
            <span className="font-medium text-sm">系统信息</span>
          </div>
          <div className="grid grid-cols-4 gap-4 text-sm">
            <div><div className="text-gray-500 mb-1">平台版本</div><div>v1.0.0 (草案)</div></div>
            <div><div className="text-gray-500 mb-1">部署环境</div><Badge variant="outline" className="bg-yellow-50 text-yellow-700 border-yellow-200">测试环境</Badge></div>
            <div><div className="text-gray-500 mb-1">最近更新</div><div>2026-06-13</div></div>
            <div><div className="text-gray-500 mb-1">系统管理员</div><div>admin@company.com</div></div>
          </div>
        </div>
      </div>
    </div>
  );
}
