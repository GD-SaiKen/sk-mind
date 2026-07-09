import { useState } from "react";
import { Link } from "react-router";
import { Button } from "../components/ui/button";
import { Input } from "../components/ui/input";
import { Badge } from "../components/ui/badge";
import { Card } from "../components/ui/card";
import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "../components/ui/table";
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "../components/ui/select";
import { Search, Eye, Edit, Shield, Brain, Table2, Bot, BarChart2, AlertTriangle } from "lucide-react";
import { mockTables, statusTypes } from "../data/mockData";

export function DataTableList() {
  const [searchTerm, setSearchTerm] = useState("");
  const [layerFilter, setLayerFilter] = useState("all");
  const [qualityFilter, setQualityFilter] = useState("all");

  const filteredTables = mockTables.filter((table) => {
    const matchesSearch = table.name.toLowerCase().includes(searchTerm.toLowerCase()) ||
      table.displayName.toLowerCase().includes(searchTerm.toLowerCase());
    const matchesLayer = layerFilter === "all" || table.layer === layerFilter;
    const matchesQuality = qualityFilter === "all" || table.quality === qualityFilter;
    return matchesSearch && matchesLayer && matchesQuality;
  });

  const counts = {
    total: mockTables.length,
    agentEnabled: mockTables.filter(t => t.agentEnabled).length,
    totalRecords: mockTables.reduce((sum, t) => sum + t.records, 0),
    errorCount: mockTables.filter(t => t.quality === "error").length,
  };

  const getQualityBadge = (quality: string) => {
    const statusInfo = statusTypes[quality as keyof typeof statusTypes];
    const colorClasses = {
      green: "bg-green-50 text-green-700 border-green-200",
      yellow: "bg-yellow-50 text-yellow-700 border-yellow-200",
      red: "bg-red-50 text-red-700 border-red-200",
      blue: "bg-blue-50 text-blue-700 border-blue-200",
      gray: "bg-gray-50 text-gray-700 border-gray-200",
    };
    return (
      <Badge variant="outline" className={colorClasses[statusInfo.color as keyof typeof colorClasses]}>
        {statusInfo.label}
      </Badge>
    );
  };

  return (
    <div className="flex flex-col h-full">

      <div className="flex-1 overflow-auto p-6 flex flex-col gap-4">
        {/* 筛选栏 */}
        <div className="flex items-center gap-3">
          <div className="relative flex-1 max-w-sm">
            <Search className="absolute left-3 top-1/2 -translate-y-1/2 size-4 text-gray-400" />
            <Input
              placeholder="搜索表名或显示名..."
              value={searchTerm}
              onChange={(e) => setSearchTerm(e.target.value)}
              className="pl-10"
            />
          </div>
          <Select value={layerFilter} onValueChange={setLayerFilter}>
            <SelectTrigger className="w-28">
              <SelectValue placeholder="数据层级" />
            </SelectTrigger>
            <SelectContent>
              <SelectItem value="all">全部层级</SelectItem>
              <SelectItem value="Raw">Raw</SelectItem>
              <SelectItem value="Clean">Clean</SelectItem>
              <SelectItem value="Serving">Serving</SelectItem>
            </SelectContent>
          </Select>
          <Select value={qualityFilter} onValueChange={setQualityFilter}>
            <SelectTrigger className="w-32">
              <SelectValue placeholder="质量状态" />
            </SelectTrigger>
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
                <div className="p-2 bg-blue-100 rounded-lg shrink-0"><Table2 className="size-4 text-blue-600" /></div>
                <span className="text-sm text-gray-500 truncate">总数据表</span>
              </div>
              <span className="text-xs text-gray-500 bg-gray-100 px-1.5 py-0.5 rounded shrink-0 whitespace-nowrap">已接入</span>
            </div>
            <div className="flex items-baseline gap-2">
              <span className="text-3xl font-bold text-gray-800 truncate min-w-0">{counts.total}</span>
              <span className="text-xs text-gray-400 bg-gray-100 px-1.5 py-0.5 rounded shrink-0 whitespace-nowrap">较昨日持平</span>
            </div>
            <div className="text-xs text-gray-400">Raw · Clean · Serving</div>
          </Card>
          <Card className="p-5 flex flex-col justify-between h-[160px]">
            <div className="flex items-center justify-between gap-2">
              <div className="flex items-center gap-2 min-w-0">
                <div className="p-2 bg-indigo-100 rounded-lg shrink-0"><Bot className="size-4 text-indigo-600" /></div>
                <span className="text-sm text-gray-500 truncate">Agent 可用</span>
              </div>
              <span className="text-xs text-indigo-600 bg-indigo-50 px-1.5 py-0.5 rounded shrink-0 whitespace-nowrap">已授权</span>
            </div>
            <div className="flex items-baseline gap-2">
              <span className="text-3xl font-bold text-indigo-600 truncate min-w-0">{counts.agentEnabled}</span>
              <span className="text-xs text-gray-400 bg-gray-100 px-1.5 py-0.5 rounded shrink-0 whitespace-nowrap">较昨日持平</span>
            </div>
            <div className="flex items-center gap-2 text-xs text-gray-400">
              <span className="whitespace-nowrap">覆盖率</span>
              <div className="flex-1 h-1 bg-gray-100 rounded-full overflow-hidden"><div className="h-full bg-indigo-400 rounded-full" style={{width: `${counts.total > 0 ? counts.agentEnabled / counts.total * 100 : 0}%`}} /></div>
              <span className="whitespace-nowrap">{counts.total > 0 ? Math.round(counts.agentEnabled / counts.total * 100) : 0}%</span>
            </div>
          </Card>
          <Card className="p-5 flex flex-col justify-between h-[160px]">
            <div className="flex items-center justify-between gap-2">
              <div className="flex items-center gap-2 min-w-0">
                <div className="p-2 bg-purple-100 rounded-lg shrink-0"><BarChart2 className="size-4 text-purple-600" /></div>
                <span className="text-sm text-gray-500 truncate">总记录数</span>
              </div>
              <span className="text-xs text-green-600 bg-green-50 px-1.5 py-0.5 rounded shrink-0 whitespace-nowrap">正常</span>
            </div>
            <div className="flex items-baseline gap-2">
              <span className="text-3xl font-bold text-gray-800 truncate min-w-0">{counts.totalRecords.toLocaleString()}</span>
              <span className="text-xs text-green-600 bg-green-50 px-1.5 py-0.5 rounded shrink-0 whitespace-nowrap">↑ 5%</span>
            </div>
            <div className="text-xs text-gray-400">最近同步: 今日 10:00</div>
          </Card>
          <Card className="p-5 flex flex-col justify-between h-[160px]">
            <div className="flex items-center justify-between gap-2">
              <div className="flex items-center gap-2 min-w-0">
                <div className="p-2 bg-orange-100 rounded-lg shrink-0"><AlertTriangle className="size-4 text-orange-500" /></div>
                <span className="text-sm text-gray-500 truncate">质量异常</span>
              </div>
              <span className="text-xs text-orange-600 bg-orange-50 border border-orange-200 px-1.5 py-0.5 rounded shrink-0 whitespace-nowrap">{counts.errorCount > 0 ? "⚠ 需修复" : "质量良好"}</span>
            </div>
            <div className="flex items-baseline gap-2">
              <span className="text-3xl font-bold text-orange-500 truncate min-w-0">{counts.errorCount}</span>
              <span className="text-xs text-gray-400 bg-gray-100 px-1.5 py-0.5 rounded shrink-0 whitespace-nowrap">较昨日持平</span>
            </div>
            <div className="text-xs text-gray-400">{counts.errorCount > 0 ? "请查看质量报告" : "所有表质量正常"}</div>
          </Card>
        </div>

        {/* 表格 */}
        <div className="bg-white rounded-lg border border-gray-200">
          <Table>
            <TableHeader>
              <TableRow>
                <TableHead>表名</TableHead>
                <TableHead>显示名</TableHead>
                <TableHead>层级</TableHead>
                <TableHead>来源数据源</TableHead>
                <TableHead>记录数</TableHead>
                <TableHead>字段数</TableHead>
                <TableHead>质量状态</TableHead>
                <TableHead>Agent 可用</TableHead>
                <TableHead>更新时间</TableHead>
                <TableHead className="text-right">操作</TableHead>
              </TableRow>
            </TableHeader>
            <TableBody>
              {filteredTables.map((table) => (
                <TableRow key={table.id}>
                  <TableCell>
                    <Link to={`/tables/${table.id}`} className="hover:text-blue-600 font-mono text-sm">
                      {table.name}
                    </Link>
                  </TableCell>
                  <TableCell>{table.displayName}</TableCell>
                  <TableCell><Badge variant="outline">{table.layer}</Badge></TableCell>
                  <TableCell>
                    <Link to="/datasources/1" className="text-blue-600 hover:underline">{table.source}</Link>
                  </TableCell>
                  <TableCell>{table.records.toLocaleString()}</TableCell>
                  <TableCell>{table.fields}</TableCell>
                  <TableCell>{getQualityBadge(table.quality)}</TableCell>
                  <TableCell>
                    {table.agentEnabled ? (
                      <Badge variant="outline" className="bg-blue-50 text-blue-700 border-blue-200">是</Badge>
                    ) : (
                      <Badge variant="outline" className="bg-gray-50 text-gray-700 border-gray-200">否</Badge>
                    )}
                  </TableCell>
                  <TableCell>{table.updatedAt}</TableCell>
                  <TableCell>
                    <div className="flex items-center justify-end gap-1">
                      <Link to={`/tables/${table.id}`}>
                        <Button variant="ghost" size="sm"><Eye className="size-4" /></Button>
                      </Link>
                      <Button variant="ghost" size="sm"><Edit className="size-4" /></Button>
                      <Button variant="ghost" size="sm"><Shield className="size-4" /></Button>
                      <Button variant="ghost" size="sm"><Brain className="size-4" /></Button>
                    </div>
                  </TableCell>
                </TableRow>
              ))}
            </TableBody>
          </Table>
          {filteredTables.length === 0 && (
            <div className="text-center py-12">
              <p className="text-gray-500 mb-3">没有找到匹配的数据表</p>
              <Button variant="outline" onClick={() => { setSearchTerm(""); setQualityFilter("all"); setActiveTab("全部"); }}>清除筛选</Button>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}
