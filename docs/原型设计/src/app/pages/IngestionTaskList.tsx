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
import { Plus, Search, Eye, Play, RotateCcw, Power, ListTodo, CheckCircle2, AlertTriangle, XCircle } from "lucide-react";
import { mockTasks, statusTypes } from "../data/mockData";

export function IngestionTaskList() {
  const [searchTerm, setSearchTerm] = useState("");
  const [statusFilter, setStatusFilter] = useState("all");

  const filteredTasks = mockTasks.filter((task) => {
    const matchesSearch = task.name.toLowerCase().includes(searchTerm.toLowerCase()) ||
      task.dataSource.toLowerCase().includes(searchTerm.toLowerCase());
    const matchesStatus = statusFilter === "all" || task.status === statusFilter;
    return matchesSearch && matchesStatus;
  });

  const counts = {
    total: mockTasks.length,
    success: mockTasks.filter(t => t.status === "success").length,
    warning: mockTasks.filter(t => t.status === "warning").length,
    error: mockTasks.filter(t => t.status === "error").length,
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
              placeholder="搜索任务名称或数据源..."
              value={searchTerm}
              onChange={(e) => setSearchTerm(e.target.value)}
              className="pl-10"
            />
          </div>
          <Select value={statusFilter} onValueChange={setStatusFilter}>
            <SelectTrigger className="w-32">
              <SelectValue placeholder="状态" />
            </SelectTrigger>
            <SelectContent>
              <SelectItem value="all">全部状态</SelectItem>
              <SelectItem value="success">成功</SelectItem>
              <SelectItem value="warning">部分成功</SelectItem>
              <SelectItem value="error">失败</SelectItem>
            </SelectContent>
          </Select>
          <div className="ml-auto">
            <Button>
              <Plus className="size-4 mr-2" />
              创建任务
            </Button>
          </div>
        </div>

        {/* 统计卡片 */}
        <div className="grid grid-cols-4 gap-4">
          <Card className="p-5 flex flex-col justify-between h-[160px]">
            <div className="flex items-center justify-between gap-2">
              <div className="flex items-center gap-2 min-w-0">
                <div className="p-2 bg-blue-100 rounded-lg shrink-0"><ListTodo className="size-4 text-blue-600" /></div>
                <span className="text-sm text-gray-500 truncate">任务总数</span>
              </div>
              <span className="text-xs text-gray-500 bg-gray-100 px-1.5 py-0.5 rounded shrink-0 whitespace-nowrap">已配置</span>
            </div>
            <div className="flex items-baseline gap-2">
              <span className="text-3xl font-bold text-gray-800 truncate min-w-0">{counts.total}</span>
              <span className="text-xs text-gray-400 bg-gray-100 px-1.5 py-0.5 rounded shrink-0 whitespace-nowrap">较昨日持平</span>
            </div>
            <div className="text-xs text-gray-400">最近执行: 10:30</div>
          </Card>
          <Card className="p-5 flex flex-col justify-between h-[160px]">
            <div className="flex items-center justify-between gap-2">
              <div className="flex items-center gap-2 min-w-0">
                <div className="p-2 bg-green-100 rounded-lg shrink-0"><CheckCircle2 className="size-4 text-green-600" /></div>
                <span className="text-sm text-gray-500 truncate">执行成功</span>
              </div>
              <span className="text-xs text-green-600 bg-green-50 px-1.5 py-0.5 rounded shrink-0 whitespace-nowrap">状态良好</span>
            </div>
            <div className="flex items-baseline gap-2">
              <span className="text-3xl font-bold text-green-600 truncate min-w-0">{counts.success}</span>
              <span className="text-xs text-green-600 bg-green-50 px-1.5 py-0.5 rounded shrink-0 whitespace-nowrap">↑ 较昨日</span>
            </div>
            <div className="flex items-center gap-2 text-xs text-gray-400">
              <span className="whitespace-nowrap">成功率</span>
              <div className="flex-1 h-1 bg-gray-100 rounded-full overflow-hidden"><div className="h-full bg-green-400 rounded-full" style={{width: `${counts.total > 0 ? counts.success / counts.total * 100 : 0}%`}} /></div>
              <span className="whitespace-nowrap">{counts.total > 0 ? Math.round(counts.success / counts.total * 100) : 0}%</span>
            </div>
          </Card>
          <Card className="p-5 flex flex-col justify-between h-[160px]">
            <div className="flex items-center justify-between gap-2">
              <div className="flex items-center gap-2 min-w-0">
                <div className="p-2 bg-yellow-100 rounded-lg shrink-0"><AlertTriangle className="size-4 text-yellow-500" /></div>
                <span className="text-sm text-gray-500 truncate">部分成功</span>
              </div>
              <span className="text-xs text-yellow-600 bg-yellow-50 px-1.5 py-0.5 rounded shrink-0 whitespace-nowrap">需关注</span>
            </div>
            <div className="flex items-baseline gap-2">
              <span className="text-3xl font-bold text-yellow-500 truncate min-w-0">{counts.warning}</span>
              <span className="text-xs text-gray-400 bg-gray-100 px-1.5 py-0.5 rounded shrink-0 whitespace-nowrap">较昨日持平</span>
            </div>
            <div className="text-xs text-gray-400">部分记录未导入</div>
          </Card>
          <Card className="p-5 flex flex-col justify-between h-[160px]">
            <div className="flex items-center justify-between gap-2">
              <div className="flex items-center gap-2 min-w-0">
                <div className="p-2 bg-red-100 rounded-lg shrink-0"><XCircle className="size-4 text-red-500" /></div>
                <span className="text-sm text-gray-500 truncate">执行失败</span>
              </div>
              <span className="text-xs text-red-600 bg-red-50 border border-red-200 px-1.5 py-0.5 rounded shrink-0 whitespace-nowrap">{counts.error > 0 ? "⚠ 需处理" : "正常"}</span>
            </div>
            <div className="flex items-baseline gap-2">
              <span className="text-3xl font-bold text-red-500 truncate min-w-0">{counts.error}</span>
              <span className="text-xs text-gray-400 bg-gray-100 px-1.5 py-0.5 rounded shrink-0 whitespace-nowrap">较昨日持平</span>
            </div>
            <div className="text-xs text-gray-400">{counts.error > 0 ? "请查看错误日志" : "暂无失败任务"}</div>
          </Card>
        </div>

        {/* 表格 */}
        <div className="bg-white rounded-lg border border-gray-200">
          <Table>
            <TableHeader>
              <TableRow>
                <TableHead>任务名称</TableHead>
                <TableHead>数据源</TableHead>
                <TableHead>接入方式</TableHead>
                <TableHead>状态</TableHead>
                <TableHead>最近执行时间</TableHead>
                <TableHead>最近结果</TableHead>
                <TableHead>成功数量</TableHead>
                <TableHead>失败数量</TableHead>
                <TableHead className="text-right">操作</TableHead>
              </TableRow>
            </TableHeader>
            <TableBody>
              {filteredTasks.map((task) => (
                <TableRow key={task.id}>
                  <TableCell>
                    <Link to={`/tasks/${task.id}`} className="hover:text-blue-600">{task.name}</Link>
                  </TableCell>
                  <TableCell>
                    <Link to="/datasources/1" className="text-blue-600 hover:underline">{task.dataSource}</Link>
                  </TableCell>
                  <TableCell>{task.method}</TableCell>
                  <TableCell>{getStatusBadge(task.status)}</TableCell>
                  <TableCell>{task.lastRun}</TableCell>
                  <TableCell>
                    <Badge variant="outline" className={
                      task.result === "成功" ? "bg-green-50 text-green-700 border-green-200"
                      : task.result === "失败" ? "bg-red-50 text-red-700 border-red-200"
                      : "bg-yellow-50 text-yellow-700 border-yellow-200"
                    }>{task.result}</Badge>
                  </TableCell>
                  <TableCell className="text-green-600">{task.successCount.toLocaleString()}</TableCell>
                  <TableCell className={task.failCount > 0 ? "text-red-600" : ""}>{task.failCount}</TableCell>
                  <TableCell>
                    <div className="flex items-center justify-end gap-1">
                      <Link to={`/tasks/${task.id}`}>
                        <Button variant="ghost" size="sm"><Eye className="size-4" /></Button>
                      </Link>
                      <Button variant="ghost" size="sm"><Play className="size-4" /></Button>
                      {task.status === "error" && (
                        <Button variant="ghost" size="sm"><RotateCcw className="size-4" /></Button>
                      )}
                      <Button variant="ghost" size="sm"><Power className="size-4" /></Button>
                    </div>
                  </TableCell>
                </TableRow>
              ))}
            </TableBody>
          </Table>
          {filteredTasks.length === 0 && (
            <div className="text-center py-12">
              <p className="text-gray-500 mb-3">没有找到匹配的接入任务</p>
              <Button variant="outline" onClick={() => { setSearchTerm(""); setStatusFilter("all"); setActiveTab("全部"); }}>清除筛选</Button>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}
