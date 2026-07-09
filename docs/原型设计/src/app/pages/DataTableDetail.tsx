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
import { Edit, Shield, Brain, CheckCircle2, Lock } from "lucide-react";
import { mockTables, statusTypes } from "../data/mockData";

export function DataTableDetail() {
  const { id } = useParams();
  const table = mockTables.find((t) => t.id === id);

  if (!table) {
    return <div className="p-8">数据表不存在</div>;
  }

  const qualityInfo = statusTypes[table.quality as keyof typeof statusTypes];
  const colorClasses = {
    green: "bg-green-50 text-green-700 border-green-200",
    yellow: "bg-yellow-50 text-yellow-700 border-yellow-200",
    red: "bg-red-50 text-red-700 border-red-200",
    blue: "bg-blue-50 text-blue-700 border-blue-200",
    gray: "bg-gray-50 text-gray-700 border-gray-200",
  };

  const fields = [
    { name: "order_id", displayName: "订单ID", type: "VARCHAR(50)", nullable: false, sample: "SO-2026-001234", description: "订单唯一标识", sensitive: false, isPK: true, queryable: true, mapped: true },
    { name: "customer_id", displayName: "客户ID", type: "VARCHAR(50)", nullable: false, sample: "CUST-8856", description: "客户唯一标识", sensitive: false, isPK: false, queryable: true, mapped: true },
    { name: "order_date", displayName: "订单日期", type: "DATE", nullable: false, sample: "2026-06-29", description: "订单创建日期", sensitive: false, isPK: false, queryable: true, mapped: true },
    { name: "amount", displayName: "订单金额", type: "DECIMAL(15,2)", nullable: false, sample: "12,580.50", description: "订单总金额", sensitive: false, isPK: false, queryable: true, mapped: true },
    { name: "status", displayName: "订单状态", type: "VARCHAR(20)", nullable: false, sample: "已确认", description: "订单处理状态", sensitive: false, isPK: false, queryable: true, mapped: true },
  ];

  const sampleData = [
    { order_id: "SO-2026-001234", customer_id: "CUST-8856", order_date: "2026-06-29", amount: "12,580.50", status: "已确认" },
    { order_id: "SO-2026-001233", customer_id: "CUST-7745", order_date: "2026-06-29", amount: "8,350.00", status: "处理中" },
    { order_id: "SO-2026-001232", customer_id: "CUST-9123", order_date: "2026-06-28", amount: "15,200.00", status: "已发货" },
  ];

  return (
    <div className="p-8">
      <Breadcrumb className="mb-6">
        <BreadcrumbList>
          <BreadcrumbItem>
            <BreadcrumbLink asChild>
              <Link to="/tables">数据表</Link>
            </BreadcrumbLink>
          </BreadcrumbItem>
          <BreadcrumbSeparator />
          <BreadcrumbItem>
            <BreadcrumbPage>{table.displayName}</BreadcrumbPage>
          </BreadcrumbItem>
        </BreadcrumbList>
      </Breadcrumb>

      <div className="mb-6">
        <div className="flex items-start justify-between">
          <div className="flex-1">
            <div className="flex items-center gap-3 mb-2">
              <h1>{table.displayName}</h1>
              <Badge variant="outline" className={colorClasses[qualityInfo.color as keyof typeof colorClasses]}>
                {qualityInfo.label}
              </Badge>
              <Badge variant="outline">{table.layer}</Badge>
              {table.agentEnabled && (
                <Badge variant="outline" className="bg-blue-50 text-blue-700 border-blue-200">
                  Agent 可用
                </Badge>
              )}
            </div>
            <p className="text-gray-600 font-mono text-sm">{table.name}</p>
          </div>
          <div className="flex gap-2">
            <Button variant="outline">
              <Edit className="size-4 mr-2" />
              编辑说明
            </Button>
            <Button variant="outline">
              <Shield className="size-4 mr-2" />
              配置权限
            </Button>
            <Button variant="outline">
              <Brain className="size-4 mr-2" />
              建立映射
            </Button>
          </div>
        </div>
      </div>

      <div className="grid grid-cols-5 gap-4 mb-6">
        <Card className="p-4">
          <div className="text-sm text-gray-600 mb-1">来源数据源</div>
          <Link to="/datasources/1" className="text-blue-600 hover:underline">
            {table.source}
          </Link>
        </Card>
        <Card className="p-4">
          <div className="text-sm text-gray-600 mb-1">负责人</div>
          <div>{table.owner}</div>
        </Card>
        <Card className="p-4">
          <div className="text-sm text-gray-600 mb-1">记录数</div>
          <div>{table.records.toLocaleString()}</div>
        </Card>
        <Card className="p-4">
          <div className="text-sm text-gray-600 mb-1">字段数</div>
          <div>{table.fields}</div>
        </Card>
        <Card className="p-4">
          <div className="text-sm text-gray-600 mb-1">更新时间</div>
          <div>{table.updatedAt}</div>
        </Card>
      </div>

      <Tabs defaultValue="sample" className="space-y-4">
        <TabsList>
          <TabsTrigger value="sample">样例数据</TabsTrigger>
          <TabsTrigger value="fields">字段列表 ({fields.length})</TabsTrigger>
          <TabsTrigger value="source">来源和批次</TabsTrigger>
          <TabsTrigger value="quality">质量结果</TabsTrigger>
          <TabsTrigger value="permissions">权限</TabsTrigger>
          <TabsTrigger value="mapping">语义映射</TabsTrigger>
          <TabsTrigger value="usage">使用记录</TabsTrigger>
        </TabsList>

        <TabsContent value="sample">
          <Card className="p-6">
            <h3 className="mb-4">样例数据 (前 3 条记录)</h3>
            <div className="overflow-x-auto">
              <Table>
                <TableHeader>
                  <TableRow>
                    <TableHead>order_id</TableHead>
                    <TableHead>customer_id</TableHead>
                    <TableHead>order_date</TableHead>
                    <TableHead>amount</TableHead>
                    <TableHead>status</TableHead>
                  </TableRow>
                </TableHeader>
                <TableBody>
                  {sampleData.map((row, index) => (
                    <TableRow key={index}>
                      <TableCell className="font-mono text-sm">{row.order_id}</TableCell>
                      <TableCell className="font-mono text-sm">{row.customer_id}</TableCell>
                      <TableCell>{row.order_date}</TableCell>
                      <TableCell>{row.amount}</TableCell>
                      <TableCell>
                        <Badge variant="outline">{row.status}</Badge>
                      </TableCell>
                    </TableRow>
                  ))}
                </TableBody>
              </Table>
            </div>
          </Card>
        </TabsContent>

        <TabsContent value="fields">
          <Card className="p-6">
            <div className="flex items-center justify-between mb-4">
              <h3>字段列表</h3>
              <div className="flex gap-2">
                <Button variant="outline" size="sm">批量补充说明</Button>
                <Button variant="outline" size="sm">批量标记敏感字段</Button>
              </div>
            </div>
            <Table>
              <TableHeader>
                <TableRow>
                  <TableHead>字段名</TableHead>
                  <TableHead>显示名</TableHead>
                  <TableHead>类型</TableHead>
                  <TableHead>样例值</TableHead>
                  <TableHead>字段说明</TableHead>
                  <TableHead>主键</TableHead>
                  <TableHead>敏感</TableHead>
                  <TableHead>可查询</TableHead>
                  <TableHead>已映射</TableHead>
                </TableRow>
              </TableHeader>
              <TableBody>
                {fields.map((field) => (
                  <TableRow key={field.name}>
                    <TableCell className="font-mono text-sm">{field.name}</TableCell>
                    <TableCell>{field.displayName}</TableCell>
                    <TableCell className="text-xs">{field.type}</TableCell>
                    <TableCell className="text-sm">{field.sample}</TableCell>
                    <TableCell className="text-sm">{field.description}</TableCell>
                    <TableCell>
                      {field.isPK && <CheckCircle2 className="size-4 text-green-600" />}
                    </TableCell>
                    <TableCell>
                      {field.sensitive && <Lock className="size-4 text-red-600" />}
                    </TableCell>
                    <TableCell>
                      {field.queryable && <CheckCircle2 className="size-4 text-green-600" />}
                    </TableCell>
                    <TableCell>
                      {field.mapped && <CheckCircle2 className="size-4 text-blue-600" />}
                    </TableCell>
                  </TableRow>
                ))}
              </TableBody>
            </Table>
          </Card>
        </TabsContent>

        <TabsContent value="source">
          <Card className="p-6">
            <h3 className="mb-4">数据来源</h3>
            <div className="space-y-4">
              <div className="p-4 bg-gray-50 rounded-lg">
                <div className="text-sm text-gray-600 mb-1">来源数据源</div>
                <Link to="/datasources/1" className="text-blue-600 hover:underline">
                  {table.source}
                </Link>
              </div>
              <div className="p-4 bg-gray-50 rounded-lg">
                <div className="text-sm text-gray-600 mb-1">接入任务</div>
                <Link to="/tasks/1" className="text-blue-600 hover:underline">
                  SAP 销售订单同步
                </Link>
              </div>
              <div className="p-4 bg-gray-50 rounded-lg">
                <div className="text-sm text-gray-600 mb-1">最近批次</div>
                <div>B-20260629-001 · 2026-06-29 09:32:15 · 成功</div>
              </div>
            </div>
          </Card>
        </TabsContent>

        <TabsContent value="quality">
          <Card className="p-6">
            <div className="flex items-center justify-between mb-4">
              <h3>数据质量状态</h3>
              <Badge variant="outline" className={colorClasses[qualityInfo.color as keyof typeof colorClasses]}>
                {qualityInfo.label}
              </Badge>
            </div>
            <div className="space-y-4">
              <div className="p-4 bg-green-50 border border-green-200 rounded-lg">
                <div className="flex items-center gap-2 mb-2">
                  <CheckCircle2 className="size-5 text-green-600" />
                  <span>完整性检查 - 通过</span>
                </div>
                <div className="text-sm text-gray-600">所有主键字段无空值</div>
              </div>
              <div className="p-4 bg-green-50 border border-green-200 rounded-lg">
                <div className="flex items-center gap-2 mb-2">
                  <CheckCircle2 className="size-5 text-green-600" />
                  <span>唯一性检查 - 通过</span>
                </div>
                <div className="text-sm text-gray-600">order_id 字段无重复值</div>
              </div>
              <div className="p-4 bg-green-50 border border-green-200 rounded-lg">
                <div className="flex items-center gap-2 mb-2">
                  <CheckCircle2 className="size-5 text-green-600" />
                  <span>格式检查 - 通过</span>
                </div>
                <div className="text-sm text-gray-600">日期和金额格式正确</div>
              </div>
            </div>
          </Card>
        </TabsContent>

        <TabsContent value="permissions">
          <Card className="p-6">
            <div className="flex items-center justify-between mb-4">
              <h3>权限配置</h3>
              <Button>编辑权限</Button>
            </div>
            <div className="space-y-4">
              <div>
                <div className="text-sm text-gray-600 mb-2">可访问角色</div>
                <div className="flex gap-2">
                  <Badge variant="outline">管理员</Badge>
                  <Badge variant="outline">财务部门</Badge>
                  <Badge variant="outline">销售部门</Badge>
                </div>
              </div>
              <div>
                <div className="text-sm text-gray-600 mb-2">可访问部门</div>
                <div className="flex gap-2">
                  <Badge variant="outline">总部</Badge>
                  <Badge variant="outline">华东区</Badge>
                </div>
              </div>
              <div>
                <div className="text-sm text-gray-600 mb-2">Agent 权限</div>
                <div className="flex items-center gap-2">
                  <Badge variant="outline" className="bg-blue-50 text-blue-700 border-blue-200">
                    继承用户权限
                  </Badge>
                  <span className="text-sm text-gray-500">Agent 查询时需检查用户权限</span>
                </div>
              </div>
            </div>
          </Card>
        </TabsContent>

        <TabsContent value="mapping">
          <Card className="p-6">
            <div className="flex items-center justify-between mb-4">
              <h3>语义映射</h3>
              <Button>创建映射</Button>
            </div>
            <div className="space-y-3">
              <div className="p-4 border border-blue-200 bg-blue-50 rounded-lg">
                <div className="flex items-center justify-between mb-2">
                  <span>映射到业务对象: 订单 (ORDER)</span>
                  <Badge variant="outline" className="bg-green-50 text-green-700 border-green-200">
                    已确认
                  </Badge>
                </div>
                <div className="text-sm text-gray-600">
                  order_id → 订单ID, customer_id → 客户ID, amount → 订单金额
                </div>
              </div>
            </div>
          </Card>
        </TabsContent>

        <TabsContent value="usage">
          <Card className="p-6">
            <h3 className="mb-4">使用记录</h3>
            <div className="space-y-3">
              <div className="p-3 border border-gray-200 rounded-lg">
                <div className="flex items-center justify-between mb-1">
                  <div className="text-sm">Agent 查询</div>
                  <div className="text-sm text-gray-500">2026-06-29 10:15</div>
                </div>
                <div className="text-sm text-gray-600">
                  用户: 张三 · 问题: "上个月销售额最高的前10个客户是谁?"
                </div>
              </div>
              <div className="p-3 border border-gray-200 rounded-lg">
                <div className="flex items-center justify-between mb-1">
                  <div className="text-sm">数据导出</div>
                  <div className="text-sm text-gray-500">2026-06-28 15:30</div>
                </div>
                <div className="text-sm text-gray-600">
                  用户: 李四 · 导出 500 条订单记录
                </div>
              </div>
            </div>
          </Card>
        </TabsContent>
      </Tabs>
    </div>
  );
}
