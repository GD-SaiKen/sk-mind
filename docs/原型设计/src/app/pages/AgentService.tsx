import { useState } from "react";
import { Card } from "../components/ui/card";
import { Badge } from "../components/ui/badge";
import { Button } from "../components/ui/button";
import { Input } from "../components/ui/input";
import { Textarea } from "../components/ui/textarea";
import {
  Table, TableBody, TableCell, TableHead, TableHeader, TableRow,
} from "../components/ui/table";
import { Bot, Send, Info, CheckCircle2, Search, Edit } from "lucide-react";
import { mockAgentCalls } from "../data/mockData";

const tabs = ["Agent查询", "工具管理", "调用记录"];

const agentTools = [
  { id: "1", name: "数据目录检索", type: "查询工具", datasets: "全部", permission: "所有用户", risk: "低", status: "启用" },
  { id: "2", name: "受控数据查询", type: "查询工具", datasets: "销售订单表, 生产记录表", permission: "继承用户权限", risk: "中", status: "启用" },
  { id: "3", name: "质量状态查询", type: "元数据工具", datasets: "全部", permission: "所有用户", risk: "低", status: "启用" },
  { id: "4", name: "语义检索", type: "查询工具", datasets: "语义对象", permission: "所有用户", risk: "低", status: "启用" },
  { id: "5", name: "图谱查询", type: "图谱工具", datasets: "关系图谱", permission: "所有用户", risk: "低", status: "启用" },
];

export function AgentService() {
  const [activeTab, setActiveTab] = useState("Agent查询");
  const [searchTerm, setSearchTerm] = useState("");
  const [query, setQuery] = useState("");
  const [showAnswer, setShowAnswer] = useState(false);

  const handleSubmit = () => { if (query.trim()) setShowAnswer(true); };

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
            {activeTab === "工具管理" && <Button><Edit className="size-4 mr-2" />配置工具</Button>}
            {activeTab === "调用记录" && <Button variant="outline">导出记录</Button>}
          </div>
        </div>

        {/* 统计卡片 */}
        <div className="grid grid-cols-4 gap-4">
          <Card className="p-5 flex flex-col justify-between h-[160px]">
            <div className="flex items-center justify-between gap-2">
              <div className="flex items-center gap-2 min-w-0">
                <div className="p-2 bg-pink-100 rounded-lg shrink-0"><Bot className="size-4 text-pink-600" /></div>
                <span className="text-sm text-gray-500 truncate">今日查询</span>
              </div>
              <span className="text-xs text-green-600 bg-green-50 px-1.5 py-0.5 rounded shrink-0 whitespace-nowrap">正常</span>
            </div>
            <div className="flex items-baseline gap-2">
              <span className="text-3xl font-bold text-gray-800 truncate min-w-0">156</span>
              <span className="text-xs text-green-600 bg-green-50 px-1.5 py-0.5 rounded shrink-0 whitespace-nowrap">↑ 12%</span>
            </div>
            <div className="flex items-center gap-2 text-xs text-gray-400">
              <span className="whitespace-nowrap">目标 200</span>
              <div className="flex-1 h-1 bg-gray-100 rounded-full overflow-hidden"><div className="h-full bg-pink-400 rounded-full" style={{width: "78%"}} /></div>
              <span className="whitespace-nowrap">78%</span>
            </div>
          </Card>
          <Card className="p-5 flex flex-col justify-between h-[160px]">
            <div className="flex items-center justify-between gap-2">
              <div className="flex items-center gap-2 min-w-0">
                <div className="p-2 bg-orange-100 rounded-lg shrink-0"><CheckCircle2 className="size-4 text-orange-500" /></div>
                <span className="text-sm text-gray-500 truncate">成功率</span>
              </div>
              <span className="text-xs text-orange-600 bg-orange-50 border border-orange-200 px-1.5 py-0.5 rounded shrink-0 whitespace-nowrap">⚠ 低于阈值</span>
            </div>
            <div className="flex items-baseline gap-2">
              <span className="text-3xl font-bold text-orange-500 truncate min-w-0">96%</span>
              <span className="text-xs text-red-600 bg-red-50 px-1.5 py-0.5 rounded shrink-0 whitespace-nowrap">↓ 2%</span>
            </div>
            <div className="flex items-center gap-2 text-xs text-gray-400">
              <span className="whitespace-nowrap">目标 ≥99%</span>
              <div className="flex-1 h-1 bg-gray-100 rounded-full overflow-hidden"><div className="h-full bg-orange-400 rounded-full" style={{width: "96%"}} /></div>
              <span className="whitespace-nowrap">96/99</span>
            </div>
          </Card>
          <Card className="p-5 flex flex-col justify-between h-[160px]">
            <div className="flex items-center justify-between gap-2">
              <div className="flex items-center gap-2 min-w-0">
                <div className="p-2 bg-blue-100 rounded-lg shrink-0"><Bot className="size-4 text-blue-600" /></div>
                <span className="text-sm text-gray-500 truncate">可用工具</span>
              </div>
              <span className="text-xs text-green-600 bg-green-50 px-1.5 py-0.5 rounded shrink-0 whitespace-nowrap">已启用</span>
            </div>
            <div className="flex items-baseline gap-2">
              <span className="text-3xl font-bold text-gray-800 truncate min-w-0">{agentTools.length}</span>
              <span className="text-xs text-green-600 bg-green-50 px-1.5 py-0.5 rounded shrink-0 whitespace-nowrap">+1 较昨日</span>
            </div>
            <div className="text-xs text-gray-400">查询 · 元数据 · 图谱</div>
          </Card>
          <Card className="p-5 flex flex-col justify-between h-[160px]">
            <div className="flex items-center justify-between gap-2">
              <div className="flex items-center gap-2 min-w-0">
                <div className="p-2 bg-purple-100 rounded-lg shrink-0"><Bot className="size-4 text-purple-600" /></div>
                <span className="text-sm text-gray-500 truncate">可用数据集</span>
              </div>
              <span className="text-xs text-gray-500 bg-gray-100 px-1.5 py-0.5 rounded shrink-0 whitespace-nowrap">持平</span>
            </div>
            <div className="flex items-baseline gap-2">
              <span className="text-3xl font-bold text-gray-800 truncate min-w-0">2</span>
              <span className="text-xs text-gray-400 bg-gray-100 px-1.5 py-0.5 rounded shrink-0 whitespace-nowrap">较昨日持平</span>
            </div>
            <div className="text-xs text-gray-400">最后同步: 今日 09:00</div>
          </Card>
        </div>

        {/* 内容区 */}
        {activeTab === "Agent查询" && (
          <div className="grid grid-cols-3 gap-6">
            <div className="col-span-2">
              <Card className="p-6">
                <div className="flex items-center gap-3 mb-4">
                  <Bot className="size-6 text-blue-600" />
                  <span className="font-medium">AI 数据查询</span>
                </div>
                <div className="bg-blue-50 border border-blue-200 rounded-lg p-4 mb-4">
                  <div className="flex items-start gap-2">
                    <Info className="size-4 text-blue-600 mt-0.5 shrink-0" />
                    <ul className="text-sm text-blue-700 space-y-1 list-disc list-inside">
                      <li>Agent 只能查询已授权的数据集</li>
                      <li>回答依赖平台数据质量</li>
                      <li>Agent 不会自动写回业务系统</li>
                    </ul>
                  </div>
                </div>
                <Textarea placeholder="例如: 上个月销售额最高的前10个客户是谁?" value={query} onChange={e => setQuery(e.target.value)} rows={4} className="mb-3" />
                <Button onClick={handleSubmit} className="w-full"><Send className="size-4 mr-2" />发送查询</Button>
                {showAnswer && (
                  <div className="border-t border-gray-200 mt-4 pt-4">
                    <div className="flex items-center gap-2 mb-3"><Bot className="size-5 text-blue-600" /><span className="font-medium">Agent 回答:</span></div>
                    <div className="bg-gray-50 rounded-lg p-4 text-sm">
                      <p className="mb-3">根据销售订单表数据,上个月销售额最高的前10个客户如下:</p>
                      <Table>
                        <TableHeader><TableRow><TableHead>排名</TableHead><TableHead>客户ID</TableHead><TableHead>客户名称</TableHead><TableHead>销售额</TableHead></TableRow></TableHeader>
                        <TableBody>
                          <TableRow><TableCell>1</TableCell><TableCell className="font-mono text-xs">CUST-8856</TableCell><TableCell>华东制造有限公司</TableCell><TableCell className="text-green-600">¥1,258,000</TableCell></TableRow>
                          <TableRow><TableCell>2</TableCell><TableCell className="font-mono text-xs">CUST-7745</TableCell><TableCell>南方贸易集团</TableCell><TableCell className="text-green-600">¥985,500</TableCell></TableRow>
                          <TableRow><TableCell>3</TableCell><TableCell className="font-mono text-xs">CUST-9123</TableCell><TableCell>北京科技公司</TableCell><TableCell className="text-green-600">¥756,200</TableCell></TableRow>
                        </TableBody>
                      </Table>
                    </div>
                    <div className="mt-3 space-y-2 text-sm">
                      <div className="flex items-center gap-2"><span className="text-gray-500 min-w-20">数据来源:</span><Badge variant="outline">销售订单表</Badge><Badge variant="outline">客户信息表</Badge></div>
                      <div className="flex items-center gap-2"><span className="text-gray-500 min-w-20">质量状态:</span><Badge variant="outline" className="bg-green-50 text-green-700 border-green-200">正常</Badge></div>
                      <div className="flex items-center gap-2"><span className="text-gray-500 min-w-20">使用工具:</span><span>受控数据查询, 聚合分析</span></div>
                    </div>
                  </div>
                )}
              </Card>
            </div>
            <div>
              <Card className="p-6">
                <div className="font-medium mb-4">当前权限范围</div>
                <div className="space-y-3 mb-6 text-sm">
                  <div><div className="text-gray-500 mb-1">当前用户</div><div>管理员</div></div>
                  <div><div className="text-gray-500 mb-1">可访问角色</div><Badge variant="outline" className="bg-blue-50 text-blue-700 border-blue-200">管理员</Badge></div>
                  <div><div className="text-gray-500 mb-1">可查询数据集</div><div className="flex flex-wrap gap-1 mt-1"><Badge variant="outline">销售订单表</Badge><Badge variant="outline">生产记录表</Badge></div></div>
                </div>
                <div className="border-t border-gray-200 pt-4">
                  <div className="font-medium mb-3">示例问题</div>
                  <div className="space-y-2">
                    {["上个月销售额最高的前10个客户是谁?", "生产线A的平均良品率是多少?", "本周有哪些订单状态异常?"].map(q => (
                      <Button key={q} variant="outline" size="sm" className="w-full justify-start text-left h-auto py-2" onClick={() => setQuery(q)}>
                        <span className="text-sm">{q}</span>
                      </Button>
                    ))}
                  </div>
                </div>
              </Card>
            </div>
          </div>
        )}

        {activeTab === "工具管理" && (
          <div className="bg-white rounded-lg border border-gray-200">
            <Table>
              <TableHeader><TableRow>
                <TableHead>工具名称</TableHead><TableHead>工具类型</TableHead><TableHead>关联数据集</TableHead>
                <TableHead>权限要求</TableHead><TableHead>风险等级</TableHead><TableHead>状态</TableHead>
                <TableHead className="text-right">操作</TableHead>
              </TableRow></TableHeader>
              <TableBody>
                {agentTools.map(tool => (
                  <TableRow key={tool.id}>
                    <TableCell>{tool.name}</TableCell>
                    <TableCell><Badge variant="outline">{tool.type}</Badge></TableCell>
                    <TableCell className="text-sm">{tool.datasets}</TableCell>
                    <TableCell className="text-sm">{tool.permission}</TableCell>
                    <TableCell>
                      <Badge variant="outline" className={tool.risk === "低" ? "bg-green-50 text-green-700 border-green-200" : tool.risk === "中" ? "bg-yellow-50 text-yellow-700 border-yellow-200" : "bg-red-50 text-red-700 border-red-200"}>{tool.risk}</Badge>
                    </TableCell>
                    <TableCell><Badge variant="outline" className="bg-green-50 text-green-700 border-green-200">{tool.status}</Badge></TableCell>
                    <TableCell><div className="flex justify-end"><Button variant="ghost" size="sm">编辑</Button></div></TableCell>
                  </TableRow>
                ))}
              </TableBody>
            </Table>
          </div>
        )}

        {activeTab === "调用记录" && (
          <div className="bg-white rounded-lg border border-gray-200">
            <Table>
              <TableHeader><TableRow>
                <TableHead>时间</TableHead><TableHead>用户</TableHead><TableHead>问题</TableHead>
                <TableHead>使用工具</TableHead><TableHead>使用数据集</TableHead><TableHead>状态</TableHead>
                <TableHead className="text-right">操作</TableHead>
              </TableRow></TableHeader>
              <TableBody>
                {mockAgentCalls.map(call => (
                  <TableRow key={call.id}>
                    <TableCell>{call.time}</TableCell>
                    <TableCell>{call.user}</TableCell>
                    <TableCell className="max-w-xs"><div className="truncate">{call.question}</div></TableCell>
                    <TableCell className="text-sm">{call.tools}</TableCell>
                    <TableCell className="text-sm">{call.datasets}</TableCell>
                    <TableCell>
                      {call.status === "成功"
                        ? <Badge variant="outline" className="bg-green-50 text-green-700 border-green-200">成功</Badge>
                        : <Badge variant="outline" className="bg-red-50 text-red-700 border-red-200">{call.status}</Badge>}
                    </TableCell>
                    <TableCell><div className="flex justify-end"><Button variant="ghost" size="sm">查看详情</Button></div></TableCell>
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
