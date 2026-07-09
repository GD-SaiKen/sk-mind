import { useParams, Link } from "react-router";
import { Button } from "../components/ui/button";
import { Badge } from "../components/ui/badge";
import { Card } from "../components/ui/card";
import { Tabs, TabsContent, TabsList, TabsTrigger } from "../components/ui/tabs";
import {
  Breadcrumb,
  BreadcrumbItem,
  BreadcrumbLink,
  BreadcrumbList,
  BreadcrumbPage,
  BreadcrumbSeparator,
} from "../components/ui/breadcrumb";
import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "../components/ui/table";
import { Play, RotateCcw, Power, CheckCircle2, AlertCircle, XCircle } from "lucide-react";
import { mockTasks, statusTypes } from "../data/mockData";

export function IngestionTaskDetail() {
  const { id } = useParams();
  const task = mockTasks.find((t) => t.id === id);

  if (!task) {
    return <div className="p-8">接入任务不存在</div>;
  }

  const statusInfo = statusTypes[task.status as keyof typeof statusTypes];
  const colorClasses = {
    green: "bg-green-50 text-green-700 border-green-200",
    yellow: "bg-yellow-50 text-yellow-700 border-yellow-200",
    red: "bg-red-50 text-red-700 border-red-200",
    blue: "bg-blue-50 text-blue-700 border-blue-200",
    gray: "bg-gray-50 text-gray-700 border-gray-200",
  };

  const batches = [
    {
      id: "B-20260629-001",
      startTime: "2026-06-29 09:30:00",
      endTime: "2026-06-29 09:32:15",
      status: "success",
      records: 1250,
      errors: 0,
    },
    {
      id: "B-20260628-001",
      startTime: "2026-06-28 09:30:00",
      endTime: "2026-06-28 09:31:45",
      status: "success",
      records: 1180,
      errors: 0,
    },
    {
      id: "B-20260627-001",
      startTime: "2026-06-27 09:30:00",
      endTime: "2026-06-27 09:32:30",
      status: "warning",
      records: 1200,
      errors: 3,
    },
  ];

  const errors = task.status === 'error' ? [
    {
      file: "财务月报_2026年5月.xlsx",
      row: 15,
      field: "金额",
      type: "格式错误",
      message: "字段值包含货币符号,无法解析为数字",
      suggestion: "移除 ¥ 符号或调整解析规则",
    },
    {
      file: "财务月报_2026年5月.xlsx",
      row: 23,
      field: "日期",
      type: "类型错误",
      message: "日期格式不正确",
      suggestion: "使用 YYYY-MM-DD 格式",
    },
  ] : [];

  return (
    <div className="p-8">
      <Breadcrumb className="mb-6">
        <BreadcrumbList>
          <BreadcrumbItem>
            <BreadcrumbLink asChild>
              <Link to="/tasks">接入任务</Link>
            </BreadcrumbLink>
          </BreadcrumbItem>
          <BreadcrumbSeparator />
          <BreadcrumbItem>
            <BreadcrumbPage>{task.name}</BreadcrumbPage>
          </BreadcrumbItem>
        </BreadcrumbList>
      </Breadcrumb>

      <div className="mb-6">
        <div className="flex items-start justify-between">
          <div className="flex-1">
            <div className="flex items-center gap-3 mb-2">
              <h1>{task.name}</h1>
              <Badge variant="outline" className={colorClasses[statusInfo.color as keyof typeof colorClasses]}>
                {statusInfo.label}
              </Badge>
              <Badge
                variant="outline"
                className={
                  task.result === "成功"
                    ? "bg-green-50 text-green-700 border-green-200"
                    : task.result === "失败"
                    ? "bg-red-50 text-red-700 border-red-200"
                    : "bg-yellow-50 text-yellow-700 border-yellow-200"
                }
              >
                {task.result}
              </Badge>
            </div>
            <p className="text-gray-600">数据源: <Link to="/datasources/1" className="text-blue-600 hover:underline">{task.dataSource}</Link></p>
          </div>
          <div className="flex gap-2">
            <Button>
              <Play className="size-4 mr-2" />
              立即执行
            </Button>
            {task.status === 'error' && (
              <Button variant="outline">
                <RotateCcw className="size-4 mr-2" />
                重试失败记录
              </Button>
            )}
            <Button variant="outline">编辑配置</Button>
            <Button variant="outline">
              <Power className="size-4 mr-2" />
              停用
            </Button>
          </div>
        </div>
      </div>

      <div className="grid grid-cols-5 gap-4 mb-6">
        <Card className="p-4">
          <div className="text-sm text-gray-600 mb-1">接入方式</div>
          <div>{task.method}</div>
        </Card>
        <Card className="p-4">
          <div className="text-sm text-gray-600 mb-1">负责人</div>
          <div>{task.owner}</div>
        </Card>
        <Card className="p-4">
          <div className="text-sm text-gray-600 mb-1">最近执行</div>
          <div>{task.lastRun}</div>
        </Card>
        <Card className="p-4">
          <div className="text-sm text-gray-600 mb-1">成功数量</div>
          <div className="text-green-600">{task.successCount.toLocaleString()}</div>
        </Card>
        <Card className="p-4">
          <div className="text-sm text-gray-600 mb-1">失败数量</div>
          <div className={task.failCount > 0 ? "text-red-600" : ""}>{task.failCount}</div>
        </Card>
      </div>

      <Tabs defaultValue="config" className="space-y-4">
        <TabsList>
          <TabsTrigger value="config">当前配置</TabsTrigger>
          <TabsTrigger value="batches">批次列表 ({batches.length})</TabsTrigger>
          <TabsTrigger value="errors">错误清单 ({errors.length})</TabsTrigger>
          <TabsTrigger value="tables">产出数据表</TabsTrigger>
          <TabsTrigger value="logs">执行日志</TabsTrigger>
        </TabsList>

        <TabsContent value="config">
          <Card className="p-6">
            <h3 className="mb-4">任务配置</h3>
            <div className="grid grid-cols-2 gap-6">
              <div>
                <div className="text-sm text-gray-600 mb-1">任务名称</div>
                <div className="mb-4">{task.name}</div>

                <div className="text-sm text-gray-600 mb-1">数据源</div>
                <div className="mb-4">{task.dataSource}</div>

                <div className="text-sm text-gray-600 mb-1">接入方式</div>
                <div className="mb-4">{task.method}</div>

                <div className="text-sm text-gray-600 mb-1">执行频率</div>
                <div>每日 09:30 自动执行</div>
              </div>
              <div>
                <div className="text-sm text-gray-600 mb-1">负责人</div>
                <div className="mb-4">{task.owner}</div>

                <div className="text-sm text-gray-600 mb-1">创建时间</div>
                <div className="mb-4">2026-01-15 14:20</div>

                <div className="text-sm text-gray-600 mb-1">更新时间</div>
                <div className="mb-4">2026-06-01 10:15</div>

                <div className="text-sm text-gray-600 mb-1">目标表</div>
                <div>sales_orders</div>
              </div>
            </div>
          </Card>
        </TabsContent>

        <TabsContent value="batches">
          <Card className="p-6">
            <h3 className="mb-4">执行批次历史</h3>
            <Table>
              <TableHeader>
                <TableRow>
                  <TableHead>批次号</TableHead>
                  <TableHead>开始时间</TableHead>
                  <TableHead>结束时间</TableHead>
                  <TableHead>状态</TableHead>
                  <TableHead>数据量</TableHead>
                  <TableHead>错误数</TableHead>
                  <TableHead className="text-right">操作</TableHead>
                </TableRow>
              </TableHeader>
              <TableBody>
                {batches.map((batch) => (
                  <TableRow key={batch.id}>
                    <TableCell>{batch.id}</TableCell>
                    <TableCell>{batch.startTime}</TableCell>
                    <TableCell>{batch.endTime}</TableCell>
                    <TableCell>
                      {batch.status === "success" ? (
                        <Badge variant="outline" className="bg-green-50 text-green-700 border-green-200">
                          成功
                        </Badge>
                      ) : (
                        <Badge variant="outline" className="bg-yellow-50 text-yellow-700 border-yellow-200">
                          部分成功
                        </Badge>
                      )}
                    </TableCell>
                    <TableCell>{batch.records.toLocaleString()}</TableCell>
                    <TableCell className={batch.errors > 0 ? "text-red-600" : ""}>
                      {batch.errors}
                    </TableCell>
                    <TableCell className="text-right">
                      <Button variant="ghost" size="sm">
                        查看详情
                      </Button>
                    </TableCell>
                  </TableRow>
                ))}
              </TableBody>
            </Table>
          </Card>
        </TabsContent>

        <TabsContent value="errors">
          <Card className="p-6">
            <h3 className="mb-4">错误清单</h3>
            {errors.length > 0 ? (
              <div className="space-y-4">
                {errors.map((error, index) => (
                  <div key={index} className="p-4 bg-red-50 border border-red-200 rounded-lg">
                    <div className="flex items-start justify-between mb-2">
                      <div className="flex items-center gap-2">
                        <XCircle className="size-5 text-red-600" />
                        <span>{error.type}</span>
                      </div>
                      <Badge variant="destructive">错误</Badge>
                    </div>
                    <div className="grid grid-cols-2 gap-4 text-sm">
                      <div>
                        <div className="text-gray-600">文件名</div>
                        <div>{error.file}</div>
                      </div>
                      <div>
                        <div className="text-gray-600">位置</div>
                        <div>第 {error.row} 行 · {error.field} 字段</div>
                      </div>
                      <div className="col-span-2">
                        <div className="text-gray-600">错误说明</div>
                        <div>{error.message}</div>
                      </div>
                      <div className="col-span-2">
                        <div className="text-gray-600">建议处理方式</div>
                        <div className="text-blue-600">{error.suggestion}</div>
                      </div>
                    </div>
                  </div>
                ))}
              </div>
            ) : (
              <div className="text-center py-8 text-gray-500">
                <CheckCircle2 className="size-12 mx-auto mb-2 text-green-600" />
                <p>暂无错误记录</p>
              </div>
            )}
          </Card>
        </TabsContent>

        <TabsContent value="tables">
          <Card className="p-6">
            <h3 className="mb-4">产出的数据表</h3>
            <Link
              to="/tables/1"
              className="flex items-center justify-between p-4 border border-gray-200 rounded-lg hover:bg-gray-50"
            >
              <div>
                <div className="flex items-center gap-2">
                  <span>销售订单表</span>
                  <Badge variant="outline" className="text-xs">Raw</Badge>
                </div>
                <div className="text-sm text-gray-500">
                  sales_orders · {task.successCount.toLocaleString()} 条记录 · 28 个字段
                </div>
              </div>
              <Button variant="ghost" size="sm">查看详情</Button>
            </Link>
          </Card>
        </TabsContent>

        <TabsContent value="logs">
          <Card className="p-6">
            <h3 className="mb-4">执行日志</h3>
            <div className="space-y-2 font-mono text-sm">
              <div className="text-gray-500">[2026-06-29 09:30:00] 开始执行接入任务</div>
              <div className="text-blue-600">[2026-06-29 09:30:05] 连接数据源成功</div>
              <div className="text-blue-600">[2026-06-29 09:30:10] 开始拉取数据...</div>
              <div className="text-blue-600">[2026-06-29 09:31:45] 数据拉取完成: 1,250 条记录</div>
              <div className="text-blue-600">[2026-06-29 09:32:00] 开始写入目标表...</div>
              <div className="text-green-600">[2026-06-29 09:32:15] 任务执行成功</div>
            </div>
          </Card>
        </TabsContent>
      </Tabs>
    </div>
  );
}
