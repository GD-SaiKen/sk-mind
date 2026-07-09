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
import { Network, Search, CheckCircle2, AlertCircle, Plus, GitBranch } from "lucide-react";

const tabs = ["关系边列表", "关系查询", "待确认关系"];

const relationEdges = [
  { id: "1", fromEntity: "客户", fromId: "CUST-8856", relation: "下单", toEntity: "订单", toId: "SO-2026-001234", source: "销售订单表", generatedBy: "数据映射", confidence: 0.95, confirmed: true },
  { id: "2", fromEntity: "订单", fromId: "SO-2026-001234", relation: "包含", toEntity: "产品", toId: "PROD-5678", source: "订单明细表", generatedBy: "数据映射", confidence: 0.98, confirmed: true },
  { id: "3", fromEntity: "客户", fromId: "CUST-8856", relation: "可能关联", toEntity: "客户", toId: "CUST-7745", source: "AI推理", generatedBy: "AI生成", confidence: 0.65, confirmed: false },
];

const pendingRelations = relationEdges.filter(e => !e.confirmed);

export function RelationGraph() {
  const [activeTab, setActiveTab] = useState("关系边列表");
  const [searchTerm, setSearchTerm] = useState("");
  const [queryObjectType, setQueryObjectType] = useState("");
  const [queryObjectId, setQueryObjectId] = useState("");

  return (
    <div className="flex flex-col h-full">
      {/* 小标签 */}
      <div className="border-b border-gray-200 px-6">
        <div className="flex gap-0">
          {tabs.map(tab => (
            <button key={tab} onClick={() => setActiveTab(tab)}
              className={`px-4 py-2.5 text-sm border-b-2 transition-colors ${activeTab === tab ? "border-blue-600 text-blue-600 font-medium" : "border-transparent text-gray-500 hover:text-gray-800"}`}>
              {tab}{tab === "待确认关系" && <span className="ml-1.5 text-xs text-gray-400">{pendingRelations.length}</span>}
            </button>
          ))}
        </div>
      </div>

      <div className="flex-1 overflow-auto p-6 flex flex-col gap-4">
        {/* 筛选区 + 操作区 */}
        <div className="flex items-center gap-3">
          <div className="relative max-w-sm flex-1">
            <Search className="absolute left-3 top-1/2 -translate-y-1/2 size-4 text-gray-400" />
            <Input placeholder="搜索关系..." value={searchTerm} onChange={e => setSearchTerm(e.target.value)} className="pl-10" />
          </div>
          <div className="ml-auto">
            {activeTab !== "关系查询" && (
              <Button><Plus className="size-4 mr-2" />创建关系边</Button>
            )}
          </div>
        </div>

        {/* 统计卡片 */}
        <div className="grid grid-cols-4 gap-4">
          <Card className="p-5 flex flex-col justify-between h-[160px]">
            <div className="flex items-center justify-between gap-2">
              <div className="flex items-center gap-2 min-w-0">
                <div className="p-2 bg-blue-100 rounded-lg shrink-0"><Network className="size-4 text-blue-600" /></div>
                <span className="text-sm text-gray-500 truncate">关系边总数</span>
              </div>
              <span className="text-xs text-gray-500 bg-gray-100 px-1.5 py-0.5 rounded shrink-0 whitespace-nowrap">图谱边</span>
            </div>
            <div className="flex items-baseline gap-2">
              <span className="text-3xl font-bold text-gray-800 truncate min-w-0">{relationEdges.length}</span>
              <span className="text-xs text-green-600 bg-green-50 px-1.5 py-0.5 rounded shrink-0 whitespace-nowrap">↑ 2 较昨日</span>
            </div>
            <div className="text-xs text-gray-400">全部关系边</div>
          </Card>
          <Card className="p-5 flex flex-col justify-between h-[160px]">
            <div className="flex items-center justify-between gap-2">
              <div className="flex items-center gap-2 min-w-0">
                <div className="p-2 bg-green-100 rounded-lg shrink-0"><CheckCircle2 className="size-4 text-green-600" /></div>
                <span className="text-sm text-gray-500 truncate">已确认</span>
              </div>
              <span className="text-xs text-green-600 bg-green-50 px-1.5 py-0.5 rounded shrink-0 whitespace-nowrap">可信关系</span>
            </div>
            <div className="flex items-baseline gap-2">
              <span className="text-3xl font-bold text-green-600 truncate min-w-0">{relationEdges.filter(e => e.confirmed).length}</span>
              <span className="text-xs text-gray-400 bg-gray-100 px-1.5 py-0.5 rounded shrink-0 whitespace-nowrap">较昨日持平</span>
            </div>
            <div className="flex items-center gap-2 text-xs text-gray-400">
              <span className="whitespace-nowrap">确认率</span>
              <div className="flex-1 h-1 bg-gray-100 rounded-full overflow-hidden"><div className="h-full bg-green-400 rounded-full" style={{width: `${relationEdges.filter(e => e.confirmed).length / relationEdges.length * 100}%`}} /></div>
              <span className="whitespace-nowrap">{Math.round(relationEdges.filter(e => e.confirmed).length / relationEdges.length * 100)}%</span>
            </div>
          </Card>
          <Card className="p-5 flex flex-col justify-between h-[160px]">
            <div className="flex items-center justify-between gap-2">
              <div className="flex items-center gap-2 min-w-0">
                <div className="p-2 bg-yellow-100 rounded-lg shrink-0"><AlertCircle className="size-4 text-yellow-500" /></div>
                <span className="text-sm text-gray-500 truncate">待确认</span>
              </div>
              <span className={`text-xs px-1.5 py-0.5 rounded shrink-0 whitespace-nowrap ${pendingRelations.length > 0 ? "text-yellow-600 bg-yellow-50 border border-yellow-200" : "text-gray-500 bg-gray-100"}`}>{pendingRelations.length > 0 ? "待审核" : "暂无"}</span>
            </div>
            <div className="flex items-baseline gap-2">
              <span className="text-3xl font-bold text-yellow-500 truncate min-w-0">{pendingRelations.length}</span>
              <span className="text-xs text-gray-400 bg-gray-100 px-1.5 py-0.5 rounded shrink-0 whitespace-nowrap">较昨日持平</span>
            </div>
            <div className="text-xs text-gray-400">{pendingRelations.length > 0 ? "AI生成，需人工确认" : "暂无待确认"}</div>
          </Card>
          <Card className="p-5 flex flex-col justify-between h-[160px]">
            <div className="flex items-center justify-between gap-2">
              <div className="flex items-center gap-2 min-w-0">
                <div className="p-2 bg-purple-100 rounded-lg shrink-0"><GitBranch className="size-4 text-purple-600" /></div>
                <span className="text-sm text-gray-500 truncate">对象类型</span>
              </div>
              <span className="text-xs text-gray-500 bg-gray-100 px-1.5 py-0.5 rounded shrink-0 whitespace-nowrap">实体类别</span>
            </div>
            <div className="flex items-baseline gap-2">
              <span className="text-3xl font-bold text-gray-800 truncate min-w-0">3</span>
              <span className="text-xs text-gray-400 bg-gray-100 px-1.5 py-0.5 rounded shrink-0 whitespace-nowrap">较昨日持平</span>
            </div>
            <div className="text-xs text-gray-400">客户 · 订单 · 产品</div>
          </Card>
        </div>

        {/* 内容区 */}
        {activeTab === "关系边列表" && (
          <div className="bg-white rounded-lg border border-gray-200">
            <Table>
              <TableHeader><TableRow>
                <TableHead>起点对象</TableHead><TableHead>起点ID</TableHead><TableHead>关系</TableHead>
                <TableHead>终点对象</TableHead><TableHead>终点ID</TableHead><TableHead>来源</TableHead>
                <TableHead>生成方式</TableHead><TableHead>可信度</TableHead><TableHead>状态</TableHead>
                <TableHead className="text-right">操作</TableHead>
              </TableRow></TableHeader>
              <TableBody>
                {relationEdges.map(edge => (
                  <TableRow key={edge.id}>
                    <TableCell><Badge variant="outline">{edge.fromEntity}</Badge></TableCell>
                    <TableCell className="font-mono text-sm">{edge.fromId}</TableCell>
                    <TableCell className="font-medium">{edge.relation}</TableCell>
                    <TableCell><Badge variant="outline">{edge.toEntity}</Badge></TableCell>
                    <TableCell className="font-mono text-sm">{edge.toId}</TableCell>
                    <TableCell className="text-sm">{edge.source}</TableCell>
                    <TableCell>
                      <Badge variant="outline" className={edge.generatedBy === "AI生成" ? "bg-purple-50 text-purple-700 border-purple-200" : "bg-blue-50 text-blue-700 border-blue-200"}>{edge.generatedBy}</Badge>
                    </TableCell>
                    <TableCell>
                      <Badge variant="outline" className={edge.confidence >= 0.9 ? "bg-green-50 text-green-700 border-green-200" : "bg-yellow-50 text-yellow-700 border-yellow-200"}>{(edge.confidence * 100).toFixed(0)}%</Badge>
                    </TableCell>
                    <TableCell>
                      {edge.confirmed ? <Badge variant="outline" className="bg-green-50 text-green-700 border-green-200">已确认</Badge> : <Badge variant="outline" className="bg-yellow-50 text-yellow-700 border-yellow-200">待确认</Badge>}
                    </TableCell>
                    <TableCell><div className="flex justify-end"><Button variant="ghost" size="sm">查看</Button></div></TableCell>
                  </TableRow>
                ))}
              </TableBody>
            </Table>
          </div>
        )}

        {activeTab === "关系查询" && (
          <div className="bg-white rounded-lg border border-gray-200 p-6">
            <div className="space-y-4 mb-6">
              <div className="grid grid-cols-2 gap-4">
                <div>
                  <label className="text-sm text-gray-600 mb-2 block">对象类型</label>
                  <Select value={queryObjectType} onValueChange={setQueryObjectType}>
                    <SelectTrigger><SelectValue placeholder="选择对象类型" /></SelectTrigger>
                    <SelectContent>
                      <SelectItem value="customer">客户</SelectItem>
                      <SelectItem value="order">订单</SelectItem>
                      <SelectItem value="product">产品</SelectItem>
                    </SelectContent>
                  </Select>
                </div>
                <div>
                  <label className="text-sm text-gray-600 mb-2 block">对象ID</label>
                  <Input placeholder="输入对象ID,例如: CUST-8856" value={queryObjectId} onChange={e => setQueryObjectId(e.target.value)} />
                </div>
              </div>
              <div className="grid grid-cols-3 gap-4">
                <div>
                  <label className="text-sm text-gray-600 mb-2 block">关系类型</label>
                  <Select><SelectTrigger><SelectValue placeholder="全部关系" /></SelectTrigger>
                    <SelectContent><SelectItem value="all">全部关系</SelectItem><SelectItem value="order">下单</SelectItem><SelectItem value="contain">包含</SelectItem></SelectContent>
                  </Select>
                </div>
                <div>
                  <label className="text-sm text-gray-600 mb-2 block">跳数范围</label>
                  <Select defaultValue="2"><SelectTrigger><SelectValue /></SelectTrigger>
                    <SelectContent><SelectItem value="1">1 跳</SelectItem><SelectItem value="2">2 跳</SelectItem><SelectItem value="3">3 跳</SelectItem></SelectContent>
                  </Select>
                </div>
                <div>
                  <label className="text-sm text-gray-600 mb-2 block">可信度下限</label>
                  <Select defaultValue="0.7"><SelectTrigger><SelectValue /></SelectTrigger>
                    <SelectContent><SelectItem value="0.9">≥ 90%</SelectItem><SelectItem value="0.7">≥ 70%</SelectItem><SelectItem value="0.5">≥ 50%</SelectItem></SelectContent>
                  </Select>
                </div>
              </div>
              <Button className="w-full"><Search className="size-4 mr-2" />查询关系路径</Button>
            </div>
            <div className="border-t border-gray-200 pt-6 space-y-3">
              <div className="text-sm font-medium text-gray-600 mb-3">查询结果示例</div>
              <div className="p-4 bg-blue-50 border border-blue-200 rounded-lg">
                <div className="flex items-center gap-2 text-sm flex-wrap">
                  <Badge variant="outline">客户 CUST-8856</Badge><span className="text-gray-500">→ 下单 →</span>
                  <Badge variant="outline">订单 SO-2026-001234</Badge><span className="text-gray-500">→ 包含 →</span>
                  <Badge variant="outline">产品 PROD-5678</Badge>
                </div>
                <div className="text-xs text-gray-500 mt-2">可信度: 93% · 已确认</div>
              </div>
              <div className="p-4 bg-gray-50 border border-gray-200 rounded-lg">
                <div className="flex items-center gap-2 text-sm flex-wrap">
                  <Badge variant="outline">客户 CUST-8856</Badge><span className="text-gray-500">→ 下单 →</span>
                  <Badge variant="outline">订单 SO-2026-001235</Badge>
                </div>
                <div className="text-xs text-gray-500 mt-2">可信度: 95% · 已确认</div>
              </div>
            </div>
          </div>
        )}

        {activeTab === "待确认关系" && (
          <div className="space-y-3">
            {pendingRelations.length > 0 ? pendingRelations.map(edge => (
              <div key={edge.id} className="p-4 bg-yellow-50 border border-yellow-200 rounded-lg">
                <div className="flex items-start justify-between mb-3">
                  <div>
                    <div className="flex items-center gap-2 mb-1 flex-wrap text-sm">
                      <Badge variant="outline">{edge.fromEntity}</Badge><span className="font-mono text-xs">{edge.fromId}</span>
                      <span className="text-gray-500">→ {edge.relation} →</span>
                      <Badge variant="outline">{edge.toEntity}</Badge><span className="font-mono text-xs">{edge.toId}</span>
                    </div>
                    <div className="text-xs text-gray-500">来源: {edge.source} · 生成方式: {edge.generatedBy} · 可信度: {(edge.confidence * 100).toFixed(0)}%</div>
                  </div>
                  <Badge variant="outline" className="bg-yellow-100 text-yellow-700 border-yellow-300">待确认</Badge>
                </div>
                <div className="flex gap-2">
                  <Button size="sm" variant="outline">查看证据</Button>
                  <Button size="sm">确认关系</Button>
                  <Button size="sm" variant="outline">拒绝</Button>
                </div>
              </div>
            )) : (
              <div className="text-center py-12 bg-white rounded-lg border border-gray-200">
                <CheckCircle2 className="size-12 mx-auto mb-2 text-green-600" />
                <p className="text-gray-500">暂无待确认关系</p>
              </div>
            )}
          </div>
        )}
      </div>
    </div>
  );
}
