import { Card } from "../components/ui/card";
import { Badge } from "../components/ui/badge";
import { Button } from "../components/ui/button";
import { Link } from "react-router";
import {
  Database,
  ListTodo,
  Table2,
  ShieldCheck,
  Brain,
  Bot,
  AlertCircle,
  CheckCircle2,
  Clock,
  ChevronRight,
} from "lucide-react";

export function HomePage() {
  return (
    <div className="flex flex-col h-full">
      {/* 标签页 */}
      <div className="px-6 mt-3 border-b border-gray-200">
        <div className="flex gap-0">
          {["运行状态", "待处理事项", "最近任务"].map((tab) => (
            <button
              key={tab}
              className={`px-4 py-2.5 text-sm border-b-2 transition-colors ${
                tab === "运行状态"
                  ? "border-blue-600 text-blue-600 font-medium"
                  : "border-transparent text-gray-500 hover:text-gray-800"
              }`}
            >
              {tab}
            </button>
          ))}
        </div>
      </div>

      <div className="flex-1 overflow-auto p-6">

      {/* 状态总览卡片 */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 mb-8">
        <Card className="p-5 flex flex-col justify-between h-[180px]">
          {/* 第一层：认知层 */}
          <div className="flex items-center justify-between">
            <div className="flex items-center gap-2">
              <div className="p-2 bg-blue-100 rounded-lg">
                <Database className="size-4 text-blue-600" />
              </div>
              <span className="font-medium text-sm">数据源</span>
            </div>
            <span className="flex items-center gap-1 text-xs text-green-700 bg-green-50 border border-green-200 rounded-full px-2 py-0.5">
              <span className="size-1.5 rounded-full bg-green-500 inline-block" />
              正常
            </span>
          </div>
          {/* 第二层：数据层 */}
          <div className="grid grid-cols-3 gap-2 text-center">
            <div>
              <div className="text-2xl font-bold text-gray-800">—</div>
              <div className="text-xs text-gray-400 mt-0.5 whitespace-nowrap">⚙️ 运行状态</div>
            </div>
            <div>
              <div className="text-2xl font-bold text-gray-800">正常</div>
              <div className="text-xs text-gray-400 mt-0.5 whitespace-nowrap">✅ 当前状态</div>
            </div>
            <div>
              <div className="text-2xl font-bold text-gray-800">10:00</div>
              <div className="text-xs text-gray-400 mt-0.5 whitespace-nowrap">🕐 最后同步</div>
            </div>
          </div>
          {/* 第三层：元数据+操作层 */}
          <div className="flex items-center justify-between">
            <span className="text-xs text-gray-400">连接池 5/10</span>
            <Link to="/datasources" className="ml-auto">
              <Button variant="link" className="p-0 h-auto text-xs text-blue-600 flex items-center gap-0.5 hover:gap-1.5 transition-all">查看详情<ChevronRight className="size-3" /></Button>
            </Link>
          </div>
        </Card>

        {/* 接入任务 */}
        <Card className="p-5 flex flex-col justify-between h-[180px]">
          <div className="flex items-center justify-between">
            <div className="flex items-center gap-2">
              <div className="p-2 bg-purple-100 rounded-lg">
                <ListTodo className="size-4 text-purple-600" />
              </div>
              <span className="font-medium text-sm">接入任务</span>
            </div>
            <span className="flex items-center gap-1 text-xs text-yellow-700 bg-yellow-50 border border-yellow-200 rounded-full px-2 py-0.5">
              <span className="size-1.5 rounded-full bg-yellow-400 inline-block" />
              部分异常
            </span>
          </div>
          <div className="grid grid-cols-3 gap-2 text-center">
            <div>
              <div className="text-2xl font-bold text-green-600">2</div>
              <div className="text-xs text-gray-400 mt-0.5">✅ 成功</div>
            </div>
            <div>
              <div className="text-2xl font-bold text-yellow-500">1</div>
              <div className="text-xs text-gray-400 mt-0.5">⏳ 部分</div>
            </div>
            <div>
              <div className="text-2xl font-bold text-red-500">1</div>
              <div className="text-xs text-gray-400 mt-0.5">❌ 失败</div>
            </div>
          </div>
          <div className="flex items-center justify-between">
            <span className="text-xs text-gray-400">上次执行：10:30</span>
            <Link to="/tasks">
              <Button variant="link" className="p-0 h-auto text-xs text-blue-600 flex items-center gap-0.5 hover:gap-1.5 transition-all">查看详情<ChevronRight className="size-3" /></Button>
            </Link>
          </div>
        </Card>

        {/* 数据表 */}
        <Card className="p-5 flex flex-col justify-between h-[180px]">
          <div className="flex items-center justify-between">
            <div className="flex items-center gap-2">
              <div className="p-2 bg-green-100 rounded-lg">
                <Table2 className="size-4 text-green-600" />
              </div>
              <span className="font-medium text-sm">数据表</span>
            </div>
            <span className="flex items-center gap-1 text-xs text-green-700 bg-green-50 border border-green-200 rounded-full px-2 py-0.5">
              <span className="size-1.5 rounded-full bg-green-500 inline-block" />
              正常
            </span>
          </div>
          <div className="grid grid-cols-3 gap-2 text-center">
            <div>
              <div className="text-2xl font-bold text-gray-800">2</div>
              <div className="text-xs text-gray-400 mt-0.5 whitespace-nowrap">🤖 Agent 可用</div>
            </div>
            <div>
              <div className="text-2xl font-bold text-gray-800">4</div>
              <div className="text-xs text-gray-400 mt-0.5 whitespace-nowrap">📋 总表数</div>
            </div>
            <div>
              <div className="text-2xl font-bold text-gray-800">50%</div>
              <div className="text-xs text-gray-400 mt-0.5 whitespace-nowrap">📈 可用率</div>
            </div>
          </div>
          <div className="flex items-center justify-between">
            <span className="text-xs text-gray-400">更新时间：今日</span>
            <Link to="/tables">
              <Button variant="link" className="p-0 h-auto text-xs text-blue-600 flex items-center gap-0.5 hover:gap-1.5 transition-all">查看详情<ChevronRight className="size-3" /></Button>
            </Link>
          </div>
        </Card>

        {/* 数据质量 */}
        <Card className="p-5 flex flex-col justify-between h-[180px]">
          <div className="flex items-center justify-between">
            <div className="flex items-center gap-2">
              <div className="p-2 bg-orange-100 rounded-lg">
                <ShieldCheck className="size-4 text-orange-600" />
              </div>
              <span className="font-medium text-sm">数据质量</span>
            </div>
            <span className="flex items-center gap-1 text-xs text-red-700 bg-red-50 border border-red-200 rounded-full px-2 py-0.5">
              <span className="size-1.5 rounded-full bg-red-500 inline-block" />
              异常
            </span>
          </div>
          <div className="grid grid-cols-3 gap-2 text-center">
            <div>
              <div className="text-2xl font-bold text-green-600">2</div>
              <div className="text-xs text-gray-400 mt-0.5">✅ 通过</div>
            </div>
            <div>
              <div className="text-2xl font-bold text-yellow-500">1</div>
              <div className="text-xs text-gray-400 mt-0.5">⚠️ 警告</div>
            </div>
            <div>
              <div className="text-2xl font-bold text-red-500">1</div>
              <div className="text-xs text-gray-400 mt-0.5">❌ 异常</div>
            </div>
          </div>
          <div className="flex items-center justify-between">
            <span className="text-xs text-gray-400">最后检测：10:45</span>
            <Link to="/quality">
              <Button variant="link" className="p-0 h-auto text-xs text-blue-600 flex items-center gap-0.5 hover:gap-1.5 transition-all">查看详情<ChevronRight className="size-3" /></Button>
            </Link>
          </div>
        </Card>

        {/* 语义模型 */}
        <Card className="p-5 flex flex-col justify-between h-[180px]">
          <div className="flex items-center justify-between">
            <div className="flex items-center gap-2">
              <div className="p-2 bg-indigo-100 rounded-lg">
                <Brain className="size-4 text-indigo-600" />
              </div>
              <span className="font-medium text-sm">语义模型</span>
            </div>
            <span className="flex items-center gap-1 text-xs text-green-700 bg-green-50 border border-green-200 rounded-full px-2 py-0.5">
              <span className="size-1.5 rounded-full bg-green-500 inline-block" />
              健康
            </span>
          </div>
          <div className="grid grid-cols-3 gap-2 text-center">
            <div>
              <div className="text-2xl font-bold text-gray-800">3</div>
              <div className="text-xs text-gray-400 mt-0.5 whitespace-nowrap">📦 业务对象</div>
            </div>
            <div>
              <div className="text-2xl font-bold text-gray-800">42</div>
              <div className="text-xs text-gray-400 mt-0.5">🔗 映射数</div>
            </div>
            <div>
              <div className="text-2xl font-bold text-gray-800">—</div>
              <div className="text-xs text-gray-400 mt-0.5 whitespace-nowrap">🔥 引用热度</div>
            </div>
          </div>
          <div className="flex items-center justify-between">
            <span className="text-xs text-gray-400">版本：v2.1</span>
            <Link to="/semantic">
              <Button variant="link" className="p-0 h-auto text-xs text-blue-600 flex items-center gap-0.5 hover:gap-1.5 transition-all">查看详情<ChevronRight className="size-3" /></Button>
            </Link>
          </div>
        </Card>

        {/* Agent 服务 */}
        <Card className="p-5 flex flex-col justify-between h-[180px]">
          <div className="flex items-center justify-between">
            <div className="flex items-center gap-2">
              <div className="p-2 bg-pink-100 rounded-lg">
                <Bot className="size-4 text-pink-600" />
              </div>
              <span className="font-medium text-sm">Agent 服务</span>
            </div>
            <span className="flex items-center gap-1 text-xs text-green-700 bg-green-50 border border-green-200 rounded-full px-2 py-0.5">
              <span className="size-1.5 rounded-full bg-green-500 inline-block" />
              正常
            </span>
          </div>
          <div className="grid grid-cols-3 gap-2 text-center">
            <div>
              <div className="text-2xl font-bold text-gray-800">96%</div>
              <div className="text-xs text-gray-400 mt-0.5 whitespace-nowrap">🎯 成功率</div>
            </div>
            <div>
              <div className="text-2xl font-bold text-gray-800">156</div>
              <div className="text-xs text-gray-400 mt-0.5 whitespace-nowrap">📊 今日查询</div>
            </div>
            <div>
              <div className="text-2xl font-bold text-gray-800">—</div>
              <div className="text-xs text-gray-400 mt-0.5 whitespace-nowrap">⏱️ 平均耗时</div>
            </div>
          </div>
          <div className="flex items-center justify-between">
            <span className="text-xs text-gray-400">峰值 QPS：12</span>
            <Link to="/agent">
              <Button variant="link" className="p-0 h-auto text-xs text-blue-600 flex items-center gap-0.5 hover:gap-1.5 transition-all">查看详情<ChevronRight className="size-3" /></Button>
            </Link>
          </div>
        </Card>
      </div>

      {/* 快捷操作 */}
      <div className="mb-6">
        <h2 className="mb-3 text-sm font-medium text-gray-500">快捷操作</h2>
        <div className="grid grid-cols-5 gap-3">
          <Link to="/datasources">
            <Button variant="outline" className="w-full">
              <Database className="size-4 mr-2" />
              新增数据源
            </Button>
          </Link>
          <Link to="/tasks">
            <Button variant="outline" className="w-full">
              <ListTodo className="size-4 mr-2" />
              创建任务
            </Button>
          </Link>
          <Link to="/catalog">
            <Button variant="outline" className="w-full">
              <Table2 className="size-4 mr-2" />
              数据目录
            </Button>
          </Link>
          <Link to="/quality">
            <Button variant="outline" className="w-full">
              <ShieldCheck className="size-4 mr-2" />
              质量检查
            </Button>
          </Link>
          <Link to="/agent">
            <Button variant="outline" className="w-full">
              <Bot className="size-4 mr-2" />
              Agent 查询
            </Button>
          </Link>
        </div>
      </div>

      {/* 数据质量概览 */}
      <Card className="mb-8">
        <div className="border-b border-gray-200 px-4 py-3">
          <h2 className="flex items-center gap-2">
            <ShieldCheck className="size-5 text-orange-600" />
            数据质量概览
          </h2>
        </div>
        <div className="p-4">
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-5 gap-4 mb-4">
            <div className="text-center">
              <div className="text-2xl font-bold text-green-600">66.7%</div>
              <div className="text-xs text-gray-400 mt-1">质量通过率</div>
            </div>
            <div className="text-center">
              <div className="text-2xl font-bold text-gray-800">3</div>
              <div className="text-xs text-gray-400 mt-1">问题类型</div>
              <div className="text-[10px] text-gray-400">完整性/格式/枚举</div>
            </div>
            <div className="text-center">
              <div className="text-2xl font-bold text-red-500">1</div>
              <div className="text-xs text-gray-400 mt-1">异常数据集</div>
            </div>
            <div className="text-center">
              <div className="text-2xl font-bold text-gray-800">10:45</div>
              <div className="text-xs text-gray-400 mt-1">最近检查</div>
            </div>
            <div className="text-center">
              <div className="text-2xl font-bold text-yellow-500">持平</div>
              <div className="text-xs text-gray-400 mt-1">趋势 vs 上周期</div>
            </div>
          </div>
          <div className="text-xs text-gray-500 mb-3">异常数据集 TOP 5</div>
          <div className="space-y-1.5">
            {[
              { name: "每日考勤记录", problems: 12, type: "完整性" },
              { name: "采购订单明细", problems: 5, type: "格式" },
              { name: "物料主数据", problems: 3, type: "枚举" },
            ].map((ds) => (
              <Link key={ds.name} to="/quality" className="flex items-center justify-between p-2 bg-red-50 border border-red-100 rounded hover:bg-red-100 transition-colors">
                <div className="flex items-center gap-2">
                  <AlertCircle className="size-3.5 text-red-500" />
                  <span className="text-sm text-red-800">{ds.name}</span>
                  <Badge variant="outline" className="text-[10px] h-4 px-1 bg-red-100 text-red-600 border-red-200">{ds.type}</Badge>
                </div>
                <span className="text-sm font-medium text-red-600">{ds.problems} 个问题</span>
              </Link>
            ))}
          </div>
        </div>
      </Card>

      {/* Agent 使用概览 */}
      <Card className="mb-8">
        <div className="border-b border-gray-200 px-4 py-3">
          <h2 className="flex items-center gap-2">
            <Bot className="size-5 text-pink-600" />
            Agent 使用概览
          </h2>
        </div>
        <div className="p-4">
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-6 gap-4 mb-4">
            <div className="text-center">
              <div className="text-2xl font-bold text-gray-800">156</div>
              <div className="text-xs text-gray-400 mt-1">今日查询</div>
            </div>
            <div className="text-center">
              <div className="text-2xl font-bold text-green-600">96.2%</div>
              <div className="text-xs text-gray-400 mt-1">成功率</div>
            </div>
            <div className="text-center">
              <div className="text-2xl font-bold text-gray-800">数据查询</div>
              <div className="text-xs text-gray-400 mt-1">最常用工具</div>
            </div>
            <div className="text-center">
              <div className="text-2xl font-bold text-gray-800">销售订单</div>
              <div className="text-xs text-gray-400 mt-1">最常用数据集</div>
            </div>
            <div className="text-center">
              <div className="text-2xl font-bold text-red-500">权限不足</div>
              <div className="text-xs text-gray-400 mt-1">主要失败原因</div>
            </div>
            <div className="text-center">
              <div className="text-2xl font-bold text-gray-800">11:02</div>
              <div className="text-xs text-gray-400 mt-1">最近查询</div>
            </div>
          </div>
          <div className="grid grid-cols-2 gap-4">
            <div>
              <div className="text-xs text-gray-500 mb-2">常用工具 TOP 5</div>
              <div className="space-y-1">
                {[
                  { name: "受控数据查询", count: 89, pct: "57%" },
                  { name: "数据目录检索", count: 34, pct: "22%" },
                  { name: "权限检查", count: 15, pct: "10%" },
                  { name: "语义检索", count: 10, pct: "6%" },
                  { name: "质量状态查询", count: 8, pct: "5%" },
                ].map((tool) => (
                  <div key={tool.name} className="flex items-center justify-between text-sm">
                    <span className="text-gray-700">{tool.name}</span>
                    <span className="flex items-center gap-2">
                      <span className="text-gray-400">{tool.count}次</span>
                      <span className="text-gray-400 w-8 text-right">{tool.pct}</span>
                    </span>
                  </div>
                ))}
              </div>
            </div>
            <div>
              <div className="text-xs text-gray-500 mb-2">失败原因分布</div>
              <div className="space-y-1">
                {[
                  { reason: "权限不足", count: 4, color: "bg-red-500" },
                  { reason: "数据不可用", count: 1, color: "bg-orange-500" },
                  { reason: "查询超时", count: 1, color: "bg-yellow-500" },
                ].map((item) => (
                  <div key={item.reason} className="flex items-center gap-2 text-sm">
                    <span className={`size-2 rounded-full ${item.color}`} />
                    <span className="text-gray-700 flex-1">{item.reason}</span>
                    <span className="text-gray-400">{item.count}次</span>
                  </div>
                ))}
              </div>
            </div>
          </div>
        </div>
      </Card>

      {/* 待处理事项 */}
      <Card className="mb-8">
        <div className="border-b border-gray-200 px-4 py-3">
          <h2 className="flex items-center gap-2">
            <AlertCircle className="size-5 text-orange-600" />
            待处理事项
          </h2>
        </div>
        <div className="p-3">
          <div className="space-y-2">
            <Link to="/tasks/4" className="flex items-center justify-between p-3 bg-red-50 border border-red-200 rounded-lg hover:bg-red-100 transition-colors">
              <div className="flex items-center gap-3">
                <AlertCircle className="size-5 text-red-600" />
                <div>
                  <div className="text-red-900">接入任务失败: 财务月报导入</div>
                  <div className="text-sm text-red-700">Excel 解析失败，12 个文件无法导入</div>
                </div>
              </div>
              <Badge variant="destructive">紧急</Badge>
            </Link>

            <Link to="/quality" className="flex items-center justify-between p-3 bg-yellow-50 border border-yellow-200 rounded-lg hover:bg-yellow-100 transition-colors">
              <div className="flex items-center gap-3">
                <Clock className="size-5 text-yellow-600" />
                <div>
                  <div className="text-yellow-900">待确认质量问题</div>
                  <div className="text-sm text-yellow-700">每日考勤表存在 5 条空值记录</div>
                </div>
              </div>
              <Badge variant="outline" className="bg-yellow-100 text-yellow-700 border-yellow-300">
                待处理
              </Badge>
            </Link>
          </div>
        </div>
      </Card>

      {/* 最近接入任务 */}
      <Card>
        <div className="border-b border-gray-200 px-4 py-3">
          <h2>最近接入任务</h2>
        </div>
        <div className="p-3">
          <div className="space-y-2">
            <div className="flex items-center justify-between p-3 border border-gray-200 rounded-lg">
              <div className="flex items-center gap-3">
                <CheckCircle2 className="size-5 text-green-600" />
                <div>
                  <div>SAP 销售订单同步</div>
                  <div className="text-sm text-gray-500">2026-06-29 09:30 · 成功导入 1,250 条记录</div>
                </div>
              </div>
              <Badge variant="outline" className="bg-green-50 text-green-700 border-green-200">
                成功
              </Badge>
            </div>

            <div className="flex items-center justify-between p-3 border border-gray-200 rounded-lg">
              <div className="flex items-center gap-3">
                <CheckCircle2 className="size-5 text-green-600" />
                <div>
                  <div>MES 生产记录拉取</div>
                  <div className="text-sm text-gray-500">2026-06-29 09:00 · 成功导入 856 条记录</div>
                </div>
              </div>
              <Badge variant="outline" className="bg-green-50 text-green-700 border-green-200">
                成功
              </Badge>
            </div>

            <div className="flex items-center justify-between p-3 border border-gray-200 rounded-lg">
              <div className="flex items-center gap-3">
                <AlertCircle className="size-5 text-yellow-600" />
                <div>
                  <div>考勤数据日同步</div>
                  <div className="text-sm text-gray-500">2026-06-28 18:00 · 成功 320 条，失败 5 条</div>
                </div>
              </div>
              <Badge variant="outline" className="bg-yellow-50 text-yellow-700 border-yellow-200">
                部分成功
              </Badge>
            </div>
          </div>
        </div>
      </Card>

      </div>
    </div>
  );
}
