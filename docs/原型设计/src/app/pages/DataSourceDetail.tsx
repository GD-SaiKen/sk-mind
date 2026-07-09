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
import { Edit, Play, Power, CheckCircle2, AlertCircle } from "lucide-react";
import { mockDataSources, mockTasks, mockTables, statusTypes } from "../data/mockData";

export function DataSourceDetail() {
  const { id } = useParams();
  const dataSource = mockDataSources.find((ds) => ds.id === id);

  if (!dataSource) {
    return <div className="p-8">数据源不存在</div>;
  }

  const relatedTasks = mockTasks.filter((task) => task.dataSource === dataSource.name);
  const relatedTables = mockTables.filter((table) => table.source === dataSource.name);

  const statusInfo = statusTypes[dataSource.status as keyof typeof statusTypes];
  const colorClasses = {
    green: "bg-green-50 text-green-700 border-green-200",
    yellow: "bg-yellow-50 text-yellow-700 border-yellow-200",
    red: "bg-red-50 text-red-700 border-red-200",
    blue: "bg-blue-50 text-blue-700 border-blue-200",
    gray: "bg-gray-50 text-gray-700 border-gray-200",
  };

  return (
    <div className="p-8">
      <Breadcrumb className="mb-6">
        <BreadcrumbList>
          <BreadcrumbItem>
            <BreadcrumbLink asChild>
              <Link to="/datasources">数据源</Link>
            </BreadcrumbLink>
          </BreadcrumbItem>
          <BreadcrumbSeparator />
          <BreadcrumbItem>
            <BreadcrumbPage>{dataSource.name}</BreadcrumbPage>
          </BreadcrumbItem>
        </BreadcrumbList>
      </Breadcrumb>

      <div className="mb-6">
        <div className="flex items-start justify-between">
          <div className="flex-1">
            <div className="flex items-center gap-3 mb-2">
              <h1>{dataSource.name}</h1>
              <Badge variant="outline" className={colorClasses[statusInfo.color as keyof typeof colorClasses]}>
                {statusInfo.label}
              </Badge>
              <Badge variant="outline">{dataSource.type}</Badge>
            </div>
            <p className="text-gray-600">{dataSource.description}</p>
          </div>
          <div className="flex gap-2">
            <Button variant="outline">
              <Edit className="size-4 mr-2" />
              编辑
            </Button>
            <Button variant="outline">
              <Play className="size-4 mr-2" />
              创建任务
            </Button>
            <Button variant="outline">
              检测连接
            </Button>
            <Button variant="outline">
              <Power className="size-4 mr-2" />
              停用
            </Button>
          </div>
        </div>
      </div>

      <div className="grid grid-cols-4 gap-4 mb-6">
        <Card className="p-4">
          <div className="text-sm text-gray-600 mb-1">接入方式</div>
          <div>{dataSource.method}</div>
        </Card>
        <Card className="p-4">
          <div className="text-sm text-gray-600 mb-1">业务负责人</div>
          <div>{dataSource.businessOwner}</div>
        </Card>
        <Card className="p-4">
          <div className="text-sm text-gray-600 mb-1">技术负责人</div>
          <div>{dataSource.techOwner}</div>
        </Card>
        <Card className="p-4">
          <div className="text-sm text-gray-600 mb-1">最近接入时间</div>
          <div>{dataSource.lastSync}</div>
        </Card>
      </div>

      <Tabs defaultValue="info" className="space-y-4">
        <TabsList>
          <TabsTrigger value="info">基本信息</TabsTrigger>
          <TabsTrigger value="tasks">接入任务 ({relatedTasks.length})</TabsTrigger>
          <TabsTrigger value="tables">产出数据表 ({relatedTables.length})</TabsTrigger>
          <TabsTrigger value="risk">风险说明</TabsTrigger>
          <TabsTrigger value="logs">操作记录</TabsTrigger>
        </TabsList>

        <TabsContent value="info">
          <Card className="p-6">
            <h3 className="mb-4">基本信息</h3>
            <div className="grid grid-cols-2 gap-6">
              <div>
                <div className="text-sm text-gray-600 mb-1">数据源名称</div>
                <div className="mb-4">{dataSource.name}</div>

                <div className="text-sm text-gray-600 mb-1">数据源类型</div>
                <div className="mb-4">{dataSource.type}</div>

                <div className="text-sm text-gray-600 mb-1">接入方式</div>
                <div className="mb-4">{dataSource.method}</div>

                <div className="text-sm text-gray-600 mb-1">业务描述</div>
                <div>{dataSource.description}</div>
              </div>
              <div>
                <div className="text-sm text-gray-600 mb-1">业务负责人</div>
                <div className="mb-4">{dataSource.businessOwner}</div>

                <div className="text-sm text-gray-600 mb-1">技术负责人</div>
                <div className="mb-4">{dataSource.techOwner}</div>

                <div className="text-sm text-gray-600 mb-1">创建时间</div>
                <div className="mb-4">2026-01-15 10:30</div>

                <div className="text-sm text-gray-600 mb-1">更新时间</div>
                <div>{dataSource.lastSync}</div>
              </div>
            </div>
          </Card>
        </TabsContent>

        <TabsContent value="tasks">
          <Card className="p-6">
            <div className="flex items-center justify-between mb-4">
              <h3>关联的接入任务</h3>
              <Button>创建新任务</Button>
            </div>
            <div className="space-y-3">
              {relatedTasks.map((task) => (
                <Link
                  key={task.id}
                  to={`/tasks/${task.id}`}
                  className="flex items-center justify-between p-4 border border-gray-200 rounded-lg hover:bg-gray-50"
                >
                  <div className="flex items-center gap-3">
                    {task.status === 'success' ? (
                      <CheckCircle2 className="size-5 text-green-600" />
                    ) : task.status === 'error' ? (
                      <AlertCircle className="size-5 text-red-600" />
                    ) : (
                      <AlertCircle className="size-5 text-yellow-600" />
                    )}
                    <div>
                      <div>{task.name}</div>
                      <div className="text-sm text-gray-500">
                        最近执行: {task.lastRun} · {task.result}
                      </div>
                    </div>
                  </div>
                  <div className="text-sm text-gray-500">
                    成功 {task.successCount} / 失败 {task.failCount}
                  </div>
                </Link>
              ))}
            </div>
          </Card>
        </TabsContent>

        <TabsContent value="tables">
          <Card className="p-6">
            <h3 className="mb-4">产出的数据表</h3>
            <div className="space-y-3">
              {relatedTables.map((table) => (
                <Link
                  key={table.id}
                  to={`/tables/${table.id}`}
                  className="flex items-center justify-between p-4 border border-gray-200 rounded-lg hover:bg-gray-50"
                >
                  <div>
                    <div className="flex items-center gap-2">
                      <span>{table.displayName}</span>
                      <Badge variant="outline" className="text-xs">{table.layer}</Badge>
                    </div>
                    <div className="text-sm text-gray-500">
                      {table.name} · {table.records.toLocaleString()} 条记录 · {table.fields} 个字段
                    </div>
                  </div>
                  <div className="flex items-center gap-2">
                    {table.agentEnabled && (
                      <Badge variant="outline" className="bg-blue-50 text-blue-700 border-blue-200">
                        Agent 可用
                      </Badge>
                    )}
                  </div>
                </Link>
              ))}
            </div>
          </Card>
        </TabsContent>

        <TabsContent value="risk">
          <Card className="p-6">
            <h3 className="mb-4">风险说明</h3>
            <div className="space-y-4">
              <div>
                <div className="text-sm text-gray-600 mb-1">数据敏感度</div>
                <div>包含销售订单、客户信息等敏感业务数据</div>
              </div>
              <div>
                <div className="text-sm text-gray-600 mb-1">访问控制</div>
                <div>需要财务部门或管理层权限才能访问</div>
              </div>
              <div>
                <div className="text-sm text-gray-600 mb-1">影响范围</div>
                <div>该数据源停用将影响 {relatedTasks.length} 个接入任务和 {relatedTables.length} 个数据表</div>
              </div>
            </div>
          </Card>
        </TabsContent>

        <TabsContent value="logs">
          <Card className="p-6">
            <h3 className="mb-4">操作记录</h3>
            <div className="space-y-3">
              <div className="flex items-start gap-3 p-3 border-l-2 border-blue-200 bg-blue-50">
                <div className="text-sm text-gray-500 w-32">2026-06-29 09:30</div>
                <div className="flex-1">
                  <div>接入任务执行成功</div>
                  <div className="text-sm text-gray-500">SAP 销售订单同步 · 导入 1,250 条记录</div>
                </div>
              </div>
              <div className="flex items-start gap-3 p-3 border-l-2 border-gray-200">
                <div className="text-sm text-gray-500 w-32">2026-06-28 18:00</div>
                <div className="flex-1">
                  <div>编辑数据源配置</div>
                  <div className="text-sm text-gray-500">更新技术负责人为李四</div>
                </div>
              </div>
              <div className="flex items-start gap-3 p-3 border-l-2 border-gray-200">
                <div className="text-sm text-gray-500 w-32">2026-01-15 10:30</div>
                <div className="flex-1">
                  <div>创建数据源</div>
                  <div className="text-sm text-gray-500">由管理员创建</div>
                </div>
              </div>
            </div>
          </Card>
        </TabsContent>
      </Tabs>
    </div>
  );
}
