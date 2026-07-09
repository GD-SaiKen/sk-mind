import { useState } from "react";
import { Link } from "react-router";
import { Button } from "../components/ui/button";
import { Input } from "../components/ui/input";
import { Badge } from "../components/ui/badge";
import { Card } from "../components/ui/card";
import {
  Select, SelectContent, SelectItem, SelectTrigger, SelectValue,
} from "../components/ui/select";
import { Search, BookOpen, Shield, Bot, Database, Building2, Clock, Rows3, Lock } from "lucide-react";
import { mockTables, statusTypes } from "../data/mockData";

const tabs = ["全部数据集", "财务数据", "销售数据", "生产数据", "人事数据"];

export function DataCatalog() {
  const [activeTab, setActiveTab] = useState("全部数据集");
  const [searchTerm, setSearchTerm] = useState("");
  const [qualityFilter, setQualityFilter] = useState("all");

  const filteredCatalog = mockTables.filter(table => {
    const matchesSearch = table.displayName.toLowerCase().includes(searchTerm.toLowerCase()) || table.name.toLowerCase().includes(searchTerm.toLowerCase());
    const matchesQuality = qualityFilter === "all" || table.quality === qualityFilter;
    return matchesSearch && matchesQuality;
  });

  const getQualityBadge = (quality: string) => {
    const statusInfo = statusTypes[quality as keyof typeof statusTypes];
    const colorClasses: Record<string, string> = {
      green: "bg-green-50 text-green-700 border-green-200",
      yellow: "bg-yellow-50 text-yellow-700 border-yellow-200",
      red: "bg-red-50 text-red-700 border-red-200",
      blue: "bg-blue-50 text-blue-700 border-blue-200",
      gray: "bg-gray-50 text-gray-700 border-gray-200",
    };
    return <Badge variant="outline" className={colorClasses[statusInfo.color]}>{statusInfo.label}</Badge>;
  };

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
        {/* 筛选区 */}
        <div className="flex items-center gap-3">
          <div className="relative max-w-sm flex-1">
            <Search className="absolute left-3 top-1/2 -translate-y-1/2 size-4 text-gray-400" />
            <Input placeholder="搜索数据集、字段、业务含义..." value={searchTerm} onChange={e => setSearchTerm(e.target.value)} className="pl-10" />
          </div>
          <Select value={qualityFilter} onValueChange={setQualityFilter}>
            <SelectTrigger className="w-32"><SelectValue placeholder="质量状态" /></SelectTrigger>
            <SelectContent>
              <SelectItem value="all">全部状态</SelectItem>
              <SelectItem value="success">正常</SelectItem>
              <SelectItem value="warning">警告</SelectItem>
              <SelectItem value="error">异常</SelectItem>
            </SelectContent>
          </Select>
        </div>

        {/* 统计卡片 */}
        <div className="grid grid-cols-4 gap-4">
          <Card className="p-5 flex flex-col justify-between h-[160px]">
            <div className="flex items-center justify-between gap-2">
              <div className="flex items-center gap-2 min-w-0">
                <div className="p-2 bg-blue-100 rounded-lg shrink-0"><Database className="size-4 text-blue-600" /></div>
                <span className="text-sm text-gray-500 truncate">数据集总数</span>
              </div>
              <span className="text-xs text-gray-500 bg-gray-100 px-1.5 py-0.5 rounded shrink-0 whitespace-nowrap">已接入</span>
            </div>
            <div className="flex items-baseline gap-2">
              <span className="text-3xl font-bold text-gray-800 truncate min-w-0">{mockTables.length}</span>
              <span className="text-xs text-blue-600 bg-blue-50 px-1.5 py-0.5 rounded shrink-0 whitespace-nowrap">+1 本周</span>
            </div>
            <div className="text-xs text-gray-400">全部数据集</div>
          </Card>
          <Card className="p-5 flex flex-col justify-between h-[160px]">
            <div className="flex items-center justify-between gap-2">
              <div className="flex items-center gap-2 min-w-0">
                <div className="p-2 bg-green-100 rounded-lg shrink-0"><BookOpen className="size-4 text-green-600" /></div>
                <span className="text-sm text-gray-500 truncate">质量正常</span>
              </div>
              <span className="text-xs text-green-600 bg-green-50 px-1.5 py-0.5 rounded shrink-0 whitespace-nowrap">数据健康</span>
            </div>
            <div className="flex items-baseline gap-2">
              <span className="text-3xl font-bold text-green-600 truncate min-w-0">{mockTables.filter(t => t.quality === "success").length}</span>
              <span className="text-xs text-gray-400 bg-gray-100 px-1.5 py-0.5 rounded shrink-0 whitespace-nowrap">较昨日持平</span>
            </div>
            <div className="flex items-center gap-2 text-xs text-gray-400">
              <span className="whitespace-nowrap">健康率</span>
              <div className="flex-1 h-1 bg-gray-100 rounded-full overflow-hidden"><div className="h-full bg-green-400 rounded-full" style={{width: `${mockTables.length > 0 ? mockTables.filter(t => t.quality === "success").length / mockTables.length * 100 : 0}%`}} /></div>
              <span className="whitespace-nowrap">{mockTables.length > 0 ? Math.round(mockTables.filter(t => t.quality === "success").length / mockTables.length * 100) : 0}%</span>
            </div>
          </Card>
          <Card className="p-5 flex flex-col justify-between h-[160px]">
            <div className="flex items-center justify-between gap-2">
              <div className="flex items-center gap-2 min-w-0">
                <div className="p-2 bg-purple-100 rounded-lg shrink-0"><Bot className="size-4 text-purple-600" /></div>
                <span className="text-sm text-gray-500 truncate">Agent 可用</span>
              </div>
              <span className="text-xs text-purple-600 bg-purple-50 px-1.5 py-0.5 rounded shrink-0 whitespace-nowrap">已授权</span>
            </div>
            <div className="flex items-baseline gap-2">
              <span className="text-3xl font-bold text-gray-800 truncate min-w-0">{mockTables.filter(t => t.agentEnabled).length}</span>
              <span className="text-xs text-gray-400 bg-gray-100 px-1.5 py-0.5 rounded shrink-0 whitespace-nowrap">较昨日持平</span>
            </div>
            <div className="flex items-center gap-2 text-xs text-gray-400">
              <span className="whitespace-nowrap">覆盖率</span>
              <div className="flex-1 h-1 bg-gray-100 rounded-full overflow-hidden"><div className="h-full bg-purple-400 rounded-full" style={{width: `${mockTables.length > 0 ? mockTables.filter(t => t.agentEnabled).length / mockTables.length * 100 : 0}%`}} /></div>
              <span className="whitespace-nowrap">{mockTables.length > 0 ? Math.round(mockTables.filter(t => t.agentEnabled).length / mockTables.length * 100) : 0}%</span>
            </div>
          </Card>
          <Card className="p-5 flex flex-col justify-between h-[160px]">
            <div className="flex items-center justify-between gap-2">
              <div className="flex items-center gap-2 min-w-0">
                <div className="p-2 bg-orange-100 rounded-lg shrink-0"><Shield className="size-4 text-orange-500" /></div>
                <span className="text-sm text-gray-500 truncate">受限访问</span>
              </div>
              <span className="text-xs text-gray-500 bg-gray-100 px-1.5 py-0.5 rounded shrink-0 whitespace-nowrap">权限保护</span>
            </div>
            <div className="flex items-baseline gap-2">
              <span className="text-3xl font-bold text-gray-800 truncate min-w-0">{mockTables.filter(t => !t.agentEnabled).length}</span>
              <span className="text-xs text-gray-400 bg-gray-100 px-1.5 py-0.5 rounded shrink-0 whitespace-nowrap">较昨日持平</span>
            </div>
            <div className="text-xs text-gray-400">需申请权限访问</div>
          </Card>
        </div>

        {/* 数据集卡片网格 */}
        {filteredCatalog.length > 0 ? (
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
            {filteredCatalog.map(dataset => {
              const isError = dataset.quality === "error";
              const isWarning = dataset.quality === "warning";
              const isEmpty = dataset.records === 0;
              const borderClass = isError ? "border-red-200" : isWarning ? "border-yellow-200" : "border-gray-200";
              const dotClass = isError ? "bg-red-500" : isWarning ? "bg-yellow-400" : "bg-green-500";
              const qualityBadge = isError
                ? <span className="text-xs text-red-600 bg-red-50 border border-red-200 px-1.5 py-0.5 rounded shrink-0">异常</span>
                : isWarning
                ? <span className="text-xs text-yellow-600 bg-yellow-50 border border-yellow-200 px-1.5 py-0.5 rounded shrink-0">警告</span>
                : <span className="text-xs text-green-600 bg-green-50 border border-green-200 px-1.5 py-0.5 rounded shrink-0">正常</span>;
              return (
                <Card key={dataset.id} className={`overflow-hidden hover:shadow-lg transition-shadow ${borderClass}`}>
                  <div className="p-5">
                    {/* 顶部：名称 + 质量徽章 */}
                    <div className="flex items-start justify-between gap-2 mb-1">
                      <div className="flex items-center gap-2 min-w-0">
                        <div className={`size-2 rounded-full shrink-0 mt-0.5 ${dotClass}`} />
                        <span className="font-semibold text-gray-800 truncate">{dataset.displayName}</span>
                      </div>
                      {qualityBadge}
                    </div>
                    <div className="flex items-center gap-2 pl-4 mb-4">
                      <p className="text-xs text-gray-400 font-mono">{dataset.name}</p>
                      {dataset.layer === "Serving" && (
                        <Badge variant="outline" className="bg-purple-50 text-purple-700 border-purple-200 text-xs shrink-0">语义: 订单</Badge>
                      )}
                    </div>

                    {/* 中部：元数据 2×2 */}
                    <div className="grid grid-cols-2 gap-x-4 gap-y-2 mb-4">
                      <div className="flex items-center gap-1.5 text-xs text-gray-500 min-w-0">
                        <Building2 className="size-3.5 shrink-0 text-gray-400" />
                        <span className="truncate">{dataset.source}</span>
                      </div>
                      <div className="flex items-center gap-1.5 text-xs text-gray-500">
                        <Clock className="size-3.5 shrink-0 text-gray-400" />
                        <span>{dataset.updatedAt.split(" ")[0]}</span>
                      </div>
                      <div className={`flex items-center gap-1.5 text-xs font-medium ${isEmpty ? "text-red-600" : "text-gray-700"}`}>
                        <Rows3 className={`size-3.5 shrink-0 ${isEmpty ? "text-red-400" : "text-gray-400"}`} />
                        <span>{isEmpty ? "0 条 — 空表" : dataset.records.toLocaleString() + " 条"}</span>
                      </div>
                      <div className="flex items-center gap-1.5 text-xs text-gray-500">
                        <BookOpen className="size-3.5 shrink-0 text-gray-400" />
                        <span>{dataset.fields} 个字段</span>
                      </div>
                    </div>

                    {/* 底部：操作 */}
                    <div className="flex items-center justify-between pt-3 border-t border-gray-100">
                      {dataset.agentEnabled ? (
                        isEmpty ? (
                          <span className="flex items-center gap-1 text-xs text-gray-400">
                            <Bot className="size-3.5" />暂无可查数据
                          </span>
                        ) : (
                          <Button size="sm" variant="outline" className="h-7 text-xs text-blue-600 border-blue-200 hover:bg-blue-50">
                            <Bot className="size-3.5 mr-1" />问问 Agent
                          </Button>
                        )
                      ) : (
                        <Button size="sm" variant="outline" className="h-7 text-xs text-gray-500">
                          <Lock className="size-3.5 mr-1" />申请权限
                        </Button>
                      )}
                      <Link to={`/tables/${dataset.id}`}>
                        <Button variant="ghost" size="sm" className="h-7 text-xs">
                          {isEmpty ? "查看表结构" : "查看详情"}
                        </Button>
                      </Link>
                    </div>
                  </div>
                </Card>
              );
            })}
          </div>
        ) : (
          <div className="text-center py-12 bg-white rounded-lg border border-gray-200">
            <BookOpen className="size-12 mx-auto mb-4 text-gray-400" />
            <p className="text-gray-500 mb-4">没有找到匹配的数据集</p>
            <Button variant="outline" onClick={() => { setSearchTerm(""); setQualityFilter("all"); }}>清除搜索条件</Button>
          </div>
        )}
      </div>
    </div>
  );
}
