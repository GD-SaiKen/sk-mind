import { useState } from "react";
import { Card } from "../components/ui/card";
import { Badge } from "../components/ui/badge";
import { Button } from "../components/ui/button";
import { Input } from "../components/ui/input";
import {
  Table, TableBody, TableCell, TableHead, TableHeader, TableRow,
} from "../components/ui/table";
import {
  Select, SelectContent, SelectItem, SelectTrigger, SelectValue,
} from "../components/ui/select";
import { ShieldCheck, Play, Edit, Power, AlertCircle, CheckCircle2, XCircle, Search, Plus } from "lucide-react";
import { mockQualityIssues } from "../data/mockData";

const tabs = ["质量规则", "执行记录", "问题清单"];

const qualityRules = [
  { id: "1", name: "主键完整性检查", type: "完整性", dataset: "销售订单表", status: "success", lastRun: "2026-06-29 09:35" },
  { id: "2", name: "订单ID唯一性检查", type: "唯一性", dataset: "销售订单表", status: "success", lastRun: "2026-06-29 09:35" },
  { id: "3", name: "考勤时间空值检查", type: "完整性", dataset: "每日考勤表", status: "warning", lastRun: "2026-06-28 18:05" },
  { id: "4", name: "金额格式检查", type: "格式", dataset: "财务月报表", status: "error", lastRun: "2026-06-27 14:05" },
];

const executionRecords = [
  { id: "1", rule: "主键完整性检查", dataset: "销售订单表", time: "2026-06-29 09:35", result: "通过", issues: 0 },
  { id: "2", rule: "考勤时间空值检查", dataset: "每日考勤表", time: "2026-06-28 18:05", result: "发现问题", issues: 5 },
  { id: "3", rule: "金额格式检查", dataset: "财务月报表", time: "2026-06-27 14:05", result: "发现问题", issues: 12 },
];

export function DataQuality() {
  const [activeTab, setActiveTab] = useState("质量规则");
  const [searchTerm, setSearchTerm] = useState("");
  const [typeFilter, setTypeFilter] = useState("all");

  const statusBadge = (status: string) => {
    if (status === "success") return <Badge variant="outline" className="bg-green-50 text-green-700 border-green-200">通过</Badge>;
    if (status === "warning") return <Badge variant="outline" className="bg-yellow-50 text-yellow-700 border-yellow-200">警告</Badge>;
    return <Badge variant="outline" className="bg-red-50 text-red-700 border-red-200">异常</Badge>;
  };

  return (
    <div className="flex flex-col h-full">
      {/* 小标签 */}
      <div className="border-b border-gray-200 px-6">
        <div className="flex gap-0">
          {tabs.map(tab => (
            <button key={tab} onClick={() => setActiveTab(tab)}
              className={`px-4 py-2.5 text-sm border-b-2 transition-colors ${activeTab === tab ? "border-blue-600 text-blue-600 font-medium" : "border-transparent text-gray-500 hover:text-gray-800"}`}>
              {tab}{tab === "问题清单" && <span className="ml-1.5 text-xs text-gray-400">{mockQualityIssues.length}</span>}
            </button>
          ))}
        </div>
      </div>

      <div className="flex-1 overflow-auto p-6 flex flex-col gap-4">
        {/* 筛选区 + 操作区 */}
        <div className="flex items-center gap-3">
          <div className="relative max-w-sm flex-1">
            <Search className="absolute left-3 top-1/2 -translate-y-1/2 size-4 text-gray-400" />
            <Input placeholder="搜索规则名称或数据集..." value={searchTerm} onChange={e => setSearchTerm(e.target.value)} className="pl-10" />
          </div>
          {activeTab === "质量规则" && (
            <Select value={typeFilter} onValueChange={setTypeFilter}>
              <SelectTrigger className="w-32"><SelectValue placeholder="规则类型" /></SelectTrigger>
              <SelectContent>
                <SelectItem value="all">全部类型</SelectItem>
                <SelectItem value="完整性">完整性</SelectItem>
                <SelectItem value="唯一性">唯一性</SelectItem>
                <SelectItem value="格式">格式</SelectItem>
              </SelectContent>
            </Select>
          )}
          <div className="ml-auto">
            <Button><Plus className="size-4 mr-2" />创建质量规则</Button>
          </div>
        </div>

        {/* 统计卡片 */}
        <div className="grid grid-cols-4 gap-4">
          <Card className="p-5 flex flex-col justify-between h-[160px]">
            <div className="flex items-center justify-between gap-2">
              <div className="flex items-center gap-2 min-w-0">
                <div className="p-2 bg-green-100 rounded-lg shrink-0"><CheckCircle2 className="size-4 text-green-600" /></div>
                <span className="text-sm text-gray-500 truncate">质量通过</span>
              </div>
              <span className="text-xs text-green-600 bg-green-50 px-1.5 py-0.5 rounded shrink-0 whitespace-nowrap">状态良好</span>
            </div>
            <div className="flex items-baseline gap-2">
              <span className="text-3xl font-bold text-green-600 truncate min-w-0">2</span>
              <span className="text-xs text-green-600 bg-green-50 px-1.5 py-0.5 rounded shrink-0 whitespace-nowrap">↑ 较昨日</span>
            </div>
            <div className="flex items-center gap-2 text-xs text-gray-400">
              <span className="whitespace-nowrap">通过率</span>
              <div className="flex-1 h-1 bg-gray-100 rounded-full overflow-hidden"><div className="h-full bg-green-400 rounded-full" style={{width: `${2 / qualityRules.length * 100}%`}} /></div>
              <span className="whitespace-nowrap">{Math.round(2 / qualityRules.length * 100)}%</span>
            </div>
          </Card>
          <Card className="p-5 flex flex-col justify-between h-[160px]">
            <div className="flex items-center justify-between gap-2">
              <div className="flex items-center gap-2 min-w-0">
                <div className="p-2 bg-yellow-100 rounded-lg shrink-0"><AlertCircle className="size-4 text-yellow-500" /></div>
                <span className="text-sm text-gray-500 truncate">质量警告</span>
              </div>
              <span className="text-xs text-yellow-600 bg-yellow-50 px-1.5 py-0.5 rounded shrink-0 whitespace-nowrap">需关注</span>
            </div>
            <div className="flex items-baseline gap-2">
              <span className="text-3xl font-bold text-yellow-500 truncate min-w-0">1</span>
              <span className="text-xs text-gray-400 bg-gray-100 px-1.5 py-0.5 rounded shrink-0 whitespace-nowrap">较昨日持平</span>
            </div>
            <div className="text-xs text-gray-400">轻微问题，建议修复</div>
          </Card>
          <Card className="p-5 flex flex-col justify-between h-[160px]">
            <div className="flex items-center justify-between gap-2">
              <div className="flex items-center gap-2 min-w-0">
                <div className="p-2 bg-red-100 rounded-lg shrink-0"><XCircle className="size-4 text-red-500" /></div>
                <span className="text-sm text-gray-500 truncate">质量异常</span>
              </div>
              <span className="text-xs text-red-600 bg-red-50 border border-red-200 px-1.5 py-0.5 rounded shrink-0 whitespace-nowrap">⚠ 需修复</span>
            </div>
            <div className="flex items-baseline gap-2">
              <span className="text-3xl font-bold text-red-500 truncate min-w-0">1</span>
              <span className="text-xs text-gray-400 bg-gray-100 px-1.5 py-0.5 rounded shrink-0 whitespace-nowrap">较昨日持平</span>
            </div>
            <div className="text-xs text-gray-400">严重问题，请立即处理</div>
          </Card>
          <Card className="p-5 flex flex-col justify-between h-[160px]">
            <div className="flex items-center justify-between gap-2">
              <div className="flex items-center gap-2 min-w-0">
                <div className="p-2 bg-blue-100 rounded-lg shrink-0"><ShieldCheck className="size-4 text-blue-600" /></div>
                <span className="text-sm text-gray-500 truncate">活跃规则</span>
              </div>
              <span className="text-xs text-gray-500 bg-gray-100 px-1.5 py-0.5 rounded shrink-0 whitespace-nowrap">已配置</span>
            </div>
            <div className="flex items-baseline gap-2">
              <span className="text-3xl font-bold text-gray-800 truncate min-w-0">{qualityRules.length}</span>
              <span className="text-xs text-gray-400 bg-gray-100 px-1.5 py-0.5 rounded shrink-0 whitespace-nowrap">较昨日持平</span>
            </div>
            <div className="text-xs text-gray-400">完整性 · 唯一性 · 格式</div>
          </Card>
        </div>

        {/* 内容区 */}
        {activeTab === "质量规则" && (
          <div className="bg-white rounded-lg border border-gray-200">
            <Table>
              <TableHeader>
                <TableRow>
                  <TableHead>规则名称</TableHead>
                  <TableHead>类型</TableHead>
                  <TableHead>适用数据集</TableHead>
                  <TableHead>状态</TableHead>
                  <TableHead>最近执行</TableHead>
                  <TableHead className="text-right">操作</TableHead>
                </TableRow>
              </TableHeader>
              <TableBody>
                {qualityRules.filter(r =>
                  r.name.includes(searchTerm) || r.dataset.includes(searchTerm)
                ).filter(r => typeFilter === "all" || r.type === typeFilter).map(rule => (
                  <TableRow key={rule.id}>
                    <TableCell>{rule.name}</TableCell>
                    <TableCell><Badge variant="outline">{rule.type}</Badge></TableCell>
                    <TableCell>{rule.dataset}</TableCell>
                    <TableCell>{statusBadge(rule.status)}</TableCell>
                    <TableCell>{rule.lastRun}</TableCell>
                    <TableCell>
                      <div className="flex items-center justify-end gap-1">
                        <Button variant="ghost" size="sm"><Play className="size-4" /></Button>
                        <Button variant="ghost" size="sm"><Edit className="size-4" /></Button>
                        <Button variant="ghost" size="sm"><Power className="size-4" /></Button>
                      </div>
                    </TableCell>
                  </TableRow>
                ))}
              </TableBody>
            </Table>
          </div>
        )}

        {activeTab === "执行记录" && (
          <div className="bg-white rounded-lg border border-gray-200">
            <Table>
              <TableHeader>
                <TableRow>
                  <TableHead>规则名称</TableHead>
                  <TableHead>数据集</TableHead>
                  <TableHead>执行时间</TableHead>
                  <TableHead>结果</TableHead>
                  <TableHead>发现问题数</TableHead>
                  <TableHead className="text-right">操作</TableHead>
                </TableRow>
              </TableHeader>
              <TableBody>
                {executionRecords.map(record => (
                  <TableRow key={record.id}>
                    <TableCell>{record.rule}</TableCell>
                    <TableCell>{record.dataset}</TableCell>
                    <TableCell>{record.time}</TableCell>
                    <TableCell>
                      {record.result === "通过"
                        ? <Badge variant="outline" className="bg-green-50 text-green-700 border-green-200">通过</Badge>
                        : <Badge variant="outline" className="bg-yellow-50 text-yellow-700 border-yellow-200">发现问题</Badge>}
                    </TableCell>
                    <TableCell className={record.issues > 0 ? "text-red-600" : ""}>{record.issues}</TableCell>
                    <TableCell className="text-right"><Button variant="ghost" size="sm">查看详情</Button></TableCell>
                  </TableRow>
                ))}
              </TableBody>
            </Table>
          </div>
        )}

        {activeTab === "问题清单" && (
          <div className="space-y-3">
            {mockQualityIssues.map(issue => (
              <div key={issue.id} className="p-4 bg-yellow-50 border border-yellow-200 rounded-lg">
                <div className="flex items-start justify-between mb-3">
                  <div className="flex items-center gap-2">
                    <AlertCircle className="size-5 text-yellow-600" />
                    <div>
                      <div>{issue.dataset} · {issue.field}</div>
                      <div className="text-sm text-gray-600">{issue.type}</div>
                    </div>
                  </div>
                  <Badge variant="outline" className="bg-yellow-100 text-yellow-700 border-yellow-300">{issue.status}</Badge>
                </div>
                <div className="grid grid-cols-4 gap-4 text-sm mb-3">
                  <div><div className="text-gray-500">问题数量</div><div className="text-yellow-700">{issue.count} 条</div></div>
                  <div><div className="text-gray-500">样例值</div><div className="font-mono text-xs">{issue.sample}</div></div>
                  <div><div className="text-gray-500">影响范围</div><div>{issue.impact}</div></div>
                  <div><div className="text-gray-500">负责人</div><div>{issue.owner}</div></div>
                </div>
                <div className="flex gap-2">
                  <Button size="sm" variant="outline">查看</Button>
                  <Button size="sm" variant="outline">分派</Button>
                  <Button size="sm" variant="outline">标记为可接受</Button>
                  <Button size="sm" variant="outline">关闭</Button>
                </div>
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  );
}
