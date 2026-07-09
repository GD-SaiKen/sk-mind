import { useState } from "react";
import { Card } from "../components/ui/card";
import { Badge } from "../components/ui/badge";
import { Button } from "../components/ui/button";
import { Input } from "../components/ui/input";
import {
  Table, TableBody, TableCell, TableHead, TableHeader, TableRow,
} from "../components/ui/table";
import { Brain, Plus, Eye, Edit, Search, Network, GitMerge, ArrowRightLeft } from "lucide-react";
import { mockSemanticObjects } from "../data/mockData";

const tabs = ["业务对象", "对象属性", "语义关系", "数据映射", "行动策略"];

const objectAttributes = [
  { id: "1", code: "order_id", name: "订单ID", object: "订单", type: "STRING", sensitive: false, mappedField: "sales_orders.order_id", agentQueryable: true },
  { id: "2", code: "order_amount", name: "订单金额", object: "订单", type: "DECIMAL", sensitive: false, mappedField: "sales_orders.amount", agentQueryable: true },
  { id: "3", code: "customer_id", name: "客户ID", object: "客户", type: "STRING", sensitive: false, mappedField: "sales_orders.customer_id", agentQueryable: true },
];

const semanticRelations = [
  { id: "1", name: "下单", subject: "客户", object: "订单", direction: "单向", type: "创建", agentEnabled: true, graphGenerated: true },
  { id: "2", name: "包含", subject: "订单", object: "产品", direction: "多对多", type: "关联", agentEnabled: true, graphGenerated: true },
  { id: "3", name: "属于", subject: "产品", object: "分类", direction: "多对一", type: "归属", agentEnabled: false, graphGenerated: false },
];

const dataMappings = [
  { id: "1", semantic: "订单.订单ID", sourceTable: "sales_orders", sourceField: "order_id", transform: "直接映射", confidence: "高", status: "已确认" },
  { id: "2", semantic: "订单.订单金额", sourceTable: "sales_orders", sourceField: "amount", transform: "直接映射", confidence: "高", status: "已确认" },
  { id: "3", semantic: "客户.客户名称", sourceTable: "customer_info", sourceField: "name", transform: "TRIM函数", confidence: "中", status: "待确认" },
];

const actionPolicies = [
  { id: "1", objectType: "订单", allowedActions: "查询, 创建", forbiddenActions: "删除", riskLevel: "中", requireConfirm: false },
  { id: "2", objectType: "客户", allowedActions: "查询", forbiddenActions: "修改, 删除", riskLevel: "高", requireConfirm: true },
  { id: "3", objectType: "产品", allowedActions: "查询", forbiddenActions: "修改, 删除, 创建", riskLevel: "低", requireConfirm: false },
];

const actionLabel: Record<string, string> = {
  "业务对象": "创建业务对象", "对象属性": "创建属性", "语义关系": "创建关系",
  "数据映射": "创建映射", "行动策略": "配置策略",
};

export function SemanticModel() {
  const [activeTab, setActiveTab] = useState("业务对象");
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

        {/* 统计卡片 */}
        <div className="grid grid-cols-4 gap-4">
          <Card className="p-5 flex flex-col justify-between h-[160px]">
            <div className="flex items-center justify-between gap-2">
              <div className="flex items-center gap-2 min-w-0">
                <div className="p-2 bg-indigo-100 rounded-lg shrink-0"><Brain className="size-4 text-indigo-600" /></div>
                <span className="text-sm text-gray-500 truncate">业务对象</span>
              </div>
              <span className="text-xs text-gray-500 bg-gray-100 px-1.5 py-0.5 rounded shrink-0 whitespace-nowrap">已建模</span>
            </div>
            <div className="flex items-baseline gap-2">
              <span className="text-3xl font-bold text-gray-800 truncate min-w-0">{mockSemanticObjects.length}</span>
              <span className="text-xs text-gray-400 bg-gray-100 px-1.5 py-0.5 rounded shrink-0 whitespace-nowrap">较昨日持平</span>
            </div>
            <div className="text-xs text-gray-400">订单 · 客户 · 产品</div>
          </Card>
          <Card className="p-5 flex flex-col justify-between h-[160px]">
            <div className="flex items-center justify-between gap-2">
              <div className="flex items-center gap-2 min-w-0">
                <div className="p-2 bg-purple-100 rounded-lg shrink-0"><GitMerge className="size-4 text-purple-600" /></div>
                <span className="text-sm text-gray-500 truncate">对象属性</span>
              </div>
              <span className="text-xs text-gray-500 bg-gray-100 px-1.5 py-0.5 rounded shrink-0 whitespace-nowrap">字段定义</span>
            </div>
            <div className="flex items-baseline gap-2">
              <span className="text-3xl font-bold text-gray-800 truncate min-w-0">{objectAttributes.length}</span>
              <span className="text-xs text-gray-400 bg-gray-100 px-1.5 py-0.5 rounded shrink-0 whitespace-nowrap">较昨日持平</span>
            </div>
            <div className="text-xs text-gray-400">平均每对象 {Math.round(objectAttributes.length / mockSemanticObjects.length)} 个属性</div>
          </Card>
          <Card className="p-5 flex flex-col justify-between h-[160px]">
            <div className="flex items-center justify-between gap-2">
              <div className="flex items-center gap-2 min-w-0">
                <div className="p-2 bg-blue-100 rounded-lg shrink-0"><Network className="size-4 text-blue-600" /></div>
                <span className="text-sm text-gray-500 truncate">语义关系</span>
              </div>
              <span className="text-xs text-blue-600 bg-blue-50 px-1.5 py-0.5 rounded shrink-0 whitespace-nowrap">已定义</span>
            </div>
            <div className="flex items-baseline gap-2">
              <span className="text-3xl font-bold text-gray-800 truncate min-w-0">{semanticRelations.length}</span>
              <span className="text-xs text-green-600 bg-green-50 px-1.5 py-0.5 rounded shrink-0 whitespace-nowrap">↑ 1 较昨日</span>
            </div>
            <div className="text-xs text-gray-400">下单 · 包含 · 属于</div>
          </Card>
          <Card className="p-5 flex flex-col justify-between h-[160px]">
            <div className="flex items-center justify-between gap-2">
              <div className="flex items-center gap-2 min-w-0">
                <div className="p-2 bg-green-100 rounded-lg shrink-0"><ArrowRightLeft className="size-4 text-green-600" /></div>
                <span className="text-sm text-gray-500 truncate">数据映射</span>
              </div>
              <span className="text-xs text-green-600 bg-green-50 px-1.5 py-0.5 rounded shrink-0 whitespace-nowrap">已配置</span>
            </div>
            <div className="flex items-baseline gap-2">
              <span className="text-3xl font-bold text-gray-800 truncate min-w-0">{dataMappings.length}</span>
              <span className="text-xs text-gray-400 bg-gray-100 px-1.5 py-0.5 rounded shrink-0 whitespace-nowrap">较昨日持平</span>
            </div>
            <div className="flex items-center gap-2 text-xs text-gray-400">
              <span className="whitespace-nowrap">已确认</span>
              <div className="flex-1 h-1 bg-gray-100 rounded-full overflow-hidden"><div className="h-full bg-green-400 rounded-full" style={{width: `${dataMappings.filter(m => m.status === "已确认").length / dataMappings.length * 100}%`}} /></div>
              <span className="whitespace-nowrap">{Math.round(dataMappings.filter(m => m.status === "已确认").length / dataMappings.length * 100)}%</span>
            </div>
          </Card>
        </div>

        {/* 内容区 */}
        {activeTab === "业务对象" && (
          <div className="bg-white rounded-lg border border-gray-200">
            <Table>
              <TableHeader><TableRow>
                <TableHead>对象编码</TableHead><TableHead>对象名称</TableHead><TableHead>分类</TableHead>
                <TableHead>负责人</TableHead><TableHead>属性数</TableHead><TableHead>关系数</TableHead>
                <TableHead>映射状态</TableHead><TableHead className="text-right">操作</TableHead>
              </TableRow></TableHeader>
              <TableBody>
                {mockSemanticObjects.map(obj => (
                  <TableRow key={obj.id}>
                    <TableCell className="font-mono text-sm">{obj.code}</TableCell>
                    <TableCell>{obj.name}</TableCell>
                    <TableCell><Badge variant="outline">{obj.category}</Badge></TableCell>
                    <TableCell>{obj.owner}</TableCell>
                    <TableCell>{obj.attributes}</TableCell>
                    <TableCell>{obj.relations}</TableCell>
                    <TableCell>
                      <Badge variant="outline" className={obj.mappingStatus === "已映射" ? "bg-green-50 text-green-700 border-green-200" : "bg-yellow-50 text-yellow-700 border-yellow-200"}>
                        {obj.mappingStatus}
                      </Badge>
                    </TableCell>
                    <TableCell>
                      <div className="flex items-center justify-end gap-1">
                        <Button variant="ghost" size="sm"><Eye className="size-4" /></Button>
                        <Button variant="ghost" size="sm"><Edit className="size-4" /></Button>
                      </div>
                    </TableCell>
                  </TableRow>
                ))}
              </TableBody>
            </Table>
          </div>
        )}

        {activeTab === "对象属性" && (
          <div className="bg-white rounded-lg border border-gray-200">
            <Table>
              <TableHeader><TableRow>
                <TableHead>属性编码</TableHead><TableHead>属性名称</TableHead><TableHead>所属对象</TableHead>
                <TableHead>数据类型</TableHead><TableHead>敏感等级</TableHead><TableHead>映射字段</TableHead>
                <TableHead>Agent 可查询</TableHead><TableHead className="text-right">操作</TableHead>
              </TableRow></TableHeader>
              <TableBody>
                {objectAttributes.map(attr => (
                  <TableRow key={attr.id}>
                    <TableCell className="font-mono text-sm">{attr.code}</TableCell>
                    <TableCell>{attr.name}</TableCell>
                    <TableCell><Badge variant="outline">{attr.object}</Badge></TableCell>
                    <TableCell className="text-sm">{attr.type}</TableCell>
                    <TableCell>{attr.sensitive ? <Badge variant="outline" className="bg-red-50 text-red-700 border-red-200">敏感</Badge> : <Badge variant="outline">普通</Badge>}</TableCell>
                    <TableCell className="font-mono text-sm">{attr.mappedField}</TableCell>
                    <TableCell>{attr.agentQueryable ? <Badge variant="outline" className="bg-green-50 text-green-700 border-green-200">是</Badge> : <Badge variant="outline">否</Badge>}</TableCell>
                    <TableCell><div className="flex justify-end"><Button variant="ghost" size="sm"><Edit className="size-4" /></Button></div></TableCell>
                  </TableRow>
                ))}
              </TableBody>
            </Table>
          </div>
        )}

        {activeTab === "语义关系" && (
          <div className="bg-white rounded-lg border border-gray-200">
            <Table>
              <TableHeader><TableRow>
                <TableHead>关系名称</TableHead><TableHead>主体对象</TableHead><TableHead>客体对象</TableHead>
                <TableHead>关系方向</TableHead><TableHead>关系类型</TableHead><TableHead>Agent 可用</TableHead>
                <TableHead>已生成图谱边</TableHead><TableHead className="text-right">操作</TableHead>
              </TableRow></TableHeader>
              <TableBody>
                {semanticRelations.map(rel => (
                  <TableRow key={rel.id}>
                    <TableCell>{rel.name}</TableCell>
                    <TableCell><Badge variant="outline">{rel.subject}</Badge></TableCell>
                    <TableCell><Badge variant="outline">{rel.object}</Badge></TableCell>
                    <TableCell>{rel.direction}</TableCell>
                    <TableCell>{rel.type}</TableCell>
                    <TableCell>{rel.agentEnabled ? <Badge variant="outline" className="bg-blue-50 text-blue-700 border-blue-200">是</Badge> : <Badge variant="outline">否</Badge>}</TableCell>
                    <TableCell>{rel.graphGenerated ? <Badge variant="outline" className="bg-green-50 text-green-700 border-green-200">是</Badge> : <Badge variant="outline">否</Badge>}</TableCell>
                    <TableCell><div className="flex justify-end"><Button variant="ghost" size="sm"><Edit className="size-4" /></Button></div></TableCell>
                  </TableRow>
                ))}
              </TableBody>
            </Table>
          </div>
        )}

        {activeTab === "数据映射" && (
          <div className="bg-white rounded-lg border border-gray-200">
            <Table>
              <TableHeader><TableRow>
                <TableHead>语义对象/属性</TableHead><TableHead>来源数据表</TableHead><TableHead>来源字段</TableHead>
                <TableHead>转换说明</TableHead><TableHead>可信度</TableHead><TableHead>状态</TableHead>
                <TableHead className="text-right">操作</TableHead>
              </TableRow></TableHeader>
              <TableBody>
                {dataMappings.map(m => (
                  <TableRow key={m.id}>
                    <TableCell>{m.semantic}</TableCell>
                    <TableCell className="font-mono text-sm">{m.sourceTable}</TableCell>
                    <TableCell className="font-mono text-sm">{m.sourceField}</TableCell>
                    <TableCell className="text-sm">{m.transform}</TableCell>
                    <TableCell><Badge variant="outline" className={m.confidence === "高" ? "bg-green-50 text-green-700 border-green-200" : "bg-yellow-50 text-yellow-700 border-yellow-200"}>{m.confidence}</Badge></TableCell>
                    <TableCell><Badge variant="outline" className={m.status === "已确认" ? "bg-green-50 text-green-700 border-green-200" : "bg-yellow-50 text-yellow-700 border-yellow-200"}>{m.status}</Badge></TableCell>
                    <TableCell>
                      <div className="flex justify-end gap-1">
                        <Button variant="ghost" size="sm">确认</Button>
                        <Button variant="ghost" size="sm"><Edit className="size-4" /></Button>
                      </div>
                    </TableCell>
                  </TableRow>
                ))}
              </TableBody>
            </Table>
          </div>
        )}

        {activeTab === "行动策略" && (
          <div className="bg-white rounded-lg border border-gray-200">
            <Table>
              <TableHeader><TableRow>
                <TableHead>对象类型</TableHead><TableHead>允许行动</TableHead><TableHead>禁止行动</TableHead>
                <TableHead>风险等级</TableHead><TableHead>需要人工确认</TableHead><TableHead className="text-right">操作</TableHead>
              </TableRow></TableHeader>
              <TableBody>
                {actionPolicies.map(p => (
                  <TableRow key={p.id}>
                    <TableCell><Badge variant="outline">{p.objectType}</Badge></TableCell>
                    <TableCell className="text-sm">{p.allowedActions}</TableCell>
                    <TableCell className="text-sm text-red-600">{p.forbiddenActions}</TableCell>
                    <TableCell>
                      <Badge variant="outline" className={p.riskLevel === "高" ? "bg-red-50 text-red-700 border-red-200" : p.riskLevel === "中" ? "bg-yellow-50 text-yellow-700 border-yellow-200" : "bg-green-50 text-green-700 border-green-200"}>{p.riskLevel}</Badge>
                    </TableCell>
                    <TableCell>{p.requireConfirm ? <Badge variant="outline" className="bg-orange-50 text-orange-700 border-orange-200">是</Badge> : <Badge variant="outline">否</Badge>}</TableCell>
                    <TableCell><div className="flex justify-end"><Button variant="ghost" size="sm"><Edit className="size-4" /></Button></div></TableCell>
                  </TableRow>
                ))}
              </TableBody>
            </Table>
          </div>
        )}
      </div>
    </div>
  );
}
