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
import { Plus, Search, Eye, Edit, Play, Power, Database, CheckCircle2, AlertTriangle, XCircle } from "lucide-react";
import { mockDataSources, dataSourceTypes, statusTypes } from "../data/mockData";

export function DataSourceList() {
  const [searchTerm, setSearchTerm] = useState("");
  const [typeFilter, setTypeFilter] = useState("all");
  const [statusFilter, setStatusFilter] = useState("all");

  const filteredSources = mockDataSources.filter((source) => {
    const matchesSearch = source.name.toLowerCase().includes(searchTerm.toLowerCase()) ||
      source.description.toLowerCase().includes(searchTerm.toLowerCase());
    const matchesType = typeFilter === "all" || source.type === typeFilter;
    const matchesStatus = statusFilter === "all" || source.status === statusFilter;
    return matchesSearch && matchesType && matchesStatus;
  });

  const counts = {
    total: mockDataSources.length,
    normal: mockDataSources.filter(s => s.status === "success").length,
    warning: mockDataSources.filter(s => s.status === "warning").length,
    error: mockDataSources.filter(s => s.status === "error").length,
  };

  const getStatusBadge = (status: string) => {
    const statusInfo = statusTypes[status as keyof typeof statusTypes];
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
        {/* 筛选栏 + 操作按钮 */}
        <div className="flex items-center gap-3">
          <div className="relative flex-1 max-w-sm">
            <Search className="absolute left-3 top-1/2 -translate-y-1/2 size-4 text-gray-400" />
            <Input
              placeholder="搜索数据源名称或描述..."
              value={searchTerm}
              onChange={(e) => setSearchTerm(e.target.value)}
              className="pl-10"
            />
          </div>
          <Select value={typeFilter} onValueChange={setTypeFilter}>
            <SelectTrigger className="w-36">
              <SelectValue placeholder="数据源类型" />
            </SelectTrigger>
            <SelectContent>
              <SelectItem value="all">全部类型</SelectItem>
              {dataSourceTypes.map((type) => (
                <SelectItem key={type} value={type}>{type}</SelectItem>
              ))}
            </SelectContent>
          </Select>
          <Select value={statusFilter} onValueChange={setStatusFilter}>
            <SelectTrigger className="w-28">
              <SelectValue placeholder="状态" />
            </SelectTrigger>
            <SelectContent>
              <SelectItem value="all">全部状态</SelectItem>
              <SelectItem value="success">正常</SelectItem>
              <SelectItem value="warning">警告</SelectItem>
              <SelectItem value="error">异常</SelectItem>
              <SelectItem value="inactive">停用</SelectItem>
            </SelectContent>
          </Select>
          <div className="ml-auto">
            <Button>
              <Plus className="size-4 mr-2" />
              新增数据源
            </Button>
          </div>
        </div>

        {/* 统计卡片 */}
        <div className="grid grid-cols-4 gap-4">
          <Card className="p-5 flex flex-col justify-between h-[160px]">
            <div className="flex items-center justify-between gap-2">
              <div className="flex items-center gap-2 min-w-0">
                <div className="p-2 bg-blue-100 rounded-lg shrink-0"><Database className="size-4 text-blue-600" /></div>
                <span className="text-sm text-gray-500 truncate">数据源总数</span>
              </div>
              <span className="text-xs text-gray-500 bg-gray-100 px-1.5 py-0.5 rounded shrink-0 whitespace-nowrap">已配置</span>
            </div>
            <div className="flex items-baseline gap-2">
              <span className="text-3xl font-bold text-gray-800 truncate min-w-0">{counts.total}</span>
              <span className="text-xs text-blue-600 bg-blue-50 px-1.5 py-0.5 rounded shrink-0 whitespace-nowrap">+1 本月</span>
            </div>
            <div className="text-xs text-gray-400">ERP · MES · Excel</div>
          </Card>
          <Card className="p-5 flex flex-col justify-between h-[160px]">
            <div className="flex items-center justify-between gap-2">
              <div className="flex items-center gap-2 min-w-0">
                <div className="p-2 bg-green-100 rounded-lg shrink-0"><CheckCircle2 className="size-4 text-green-600" /></div>
                <span className="text-sm text-gray-500 truncate">运行正常</span>
              </div>
              <span className="text-xs text-green-600 bg-green-50 px-1.5 py-0.5 rounded shrink-0 whitespace-nowrap">状态良好</span>
            </div>
            <div className="flex items-baseline gap-2">
              <span className="text-3xl font-bold text-green-600 truncate min-w-0">{counts.normal}</span>
              <span className="text-xs text-green-600 bg-green-50 px-1.5 py-0.5 rounded shrink-0 whitespace-nowrap">↑ 较昨日</span>
            </div>
            <div className="flex items-center gap-2 text-xs text-gray-400">
              <span className="whitespace-nowrap">健康率</span>
              <div className="flex-1 h-1 bg-gray-100 rounded-full overflow-hidden"><div className="h-full bg-green-400 rounded-full" style={{width: `${counts.total > 0 ? counts.normal / counts.total * 100 : 0}%`}} /></div>
              <span className="whitespace-nowrap">{counts.total > 0 ? Math.round(counts.normal / counts.total * 100) : 0}%</span>
            </div>
          </Card>
          <Card className="p-5 flex flex-col justify-between h-[160px]">
            <div className="flex items-center justify-between gap-2">
              <div className="flex items-center gap-2 min-w-0">
                <div className="p-2 bg-yellow-100 rounded-lg shrink-0"><AlertTriangle className="size-4 text-yellow-500" /></div>
                <span className="text-sm text-gray-500 truncate">警告</span>
              </div>
              <span className="text-xs text-yellow-600 bg-yellow-50 px-1.5 py-0.5 rounded shrink-0 whitespace-nowrap">需关注</span>
            </div>
            <div className="flex items-baseline gap-2">
              <span className="text-3xl font-bold text-yellow-500 truncate min-w-0">{counts.warning}</span>
              <span className="text-xs text-gray-400 bg-gray-100 px-1.5 py-0.5 rounded shrink-0 whitespace-nowrap">较昨日持平</span>
            </div>
            <div className="text-xs text-gray-400">上次告警: 2h 前</div>
          </Card>
          <Card className="p-5 flex flex-col justify-between h-[160px]">
            <div className="flex items-center justify-between gap-2">
              <div className="flex items-center gap-2 min-w-0">
                <div className="p-2 bg-red-100 rounded-lg shrink-0"><XCircle className="size-4 text-red-500" /></div>
                <span className="text-sm text-gray-500 truncate">异常</span>
              </div>
              <span className="text-xs text-red-600 bg-red-50 border border-red-200 px-1.5 py-0.5 rounded shrink-0 whitespace-nowrap">{counts.error > 0 ? "⚠ 需处理" : "正常"}</span>
            </div>
            <div className="flex items-baseline gap-2">
              <span className="text-3xl font-bold text-red-500 truncate min-w-0">{counts.error}</span>
              <span className="text-xs text-gray-400 bg-gray-100 px-1.5 py-0.5 rounded shrink-0 whitespace-nowrap">较昨日持平</span>
            </div>
            <div className="text-xs text-gray-400">{counts.error > 0 ? "请立即排查" : "暂无异常"}</div>
          </Card>
        </div>

        {/* 表格 */}
        <div className="bg-white rounded-lg border border-gray-200">
          <Table>
            <TableHeader>
              <TableRow>
                <TableHead>数据源名称</TableHead>
                <TableHead>类型</TableHead>
                <TableHead>接入方式</TableHead>
                <TableHead>状态</TableHead>
                <TableHead>业务负责人</TableHead>
                <TableHead>技术负责人</TableHead>
                <TableHead>最近接入时间</TableHead>
                <TableHead>关联任务数</TableHead>
                <TableHead className="text-right">操作</TableHead>
              </TableRow>
            </TableHeader>
            <TableBody>
              {filteredSources.map((source) => (
                <TableRow key={source.id}>
                  <TableCell>
                    <Link to={`/datasources/${source.id}`} className="hover:text-blue-600">
                      <div>{source.name}</div>
                      <div className="text-sm text-gray-500">{source.description}</div>
                    </Link>
                  </TableCell>
                  <TableCell><Badge variant="outline">{source.type}</Badge></TableCell>
                  <TableCell>{source.method}</TableCell>
                  <TableCell>{getStatusBadge(source.status)}</TableCell>
                  <TableCell>{source.businessOwner}</TableCell>
                  <TableCell>{source.techOwner}</TableCell>
                  <TableCell>{source.lastSync}</TableCell>
                  <TableCell>{source.taskCount}</TableCell>
                  <TableCell>
                    <div className="flex items-center justify-end gap-1">
                      <Link to={`/datasources/${source.id}`}>
                        <Button variant="ghost" size="sm"><Eye className="size-4" /></Button>
                      </Link>
                      <Button variant="ghost" size="sm"><Edit className="size-4" /></Button>
                      <Button variant="ghost" size="sm"><Play className="size-4" /></Button>
                      <Button variant="ghost" size="sm"><Power className="size-4" /></Button>
                    </div>
                  </TableCell>
                </TableRow>
              ))}
            </TableBody>
          </Table>
          {filteredSources.length === 0 && (
            <div className="text-center py-12">
              <p className="text-gray-500 mb-3">没有找到匹配的数据源</p>
              <Button variant="outline" onClick={() => { setSearchTerm(""); setTypeFilter("all"); setActiveTab("全部"); }}>清除筛选</Button>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}
