import { useState } from "react";
import { Card } from "../components/ui/card";
import { Badge } from "../components/ui/badge";
import { Button } from "../components/ui/button";
import { Input } from "../components/ui/input";
import {
  Table, TableBody, TableCell, TableHead, TableHeader, TableRow,
} from "../components/ui/table";
import { Shield, Users, Building2, Lock, Eye, FileText, Search, Plus } from "lucide-react";

const tabs = ["用户管理", "角色管理", "数据集权限", "敏感字段", "审计日志"];

const auditLogs = [
  { id: "1", time: "2026-06-29 10:15", user: "张三", role: "管理员", operation: "数据查询", object: "销售订单表", range: "全部字段", tool: "Agent 查询", result: "成功", ip: "192.168.1.100" },
  { id: "2", time: "2026-06-29 10:10", user: "李四", role: "财务部门", operation: "数据导出", object: "财务月报表", range: "500 条记录", tool: "手动导出", result: "成功", ip: "192.168.1.101" },
  { id: "3", time: "2026-06-29 10:05", user: "王五", role: "普通用户", operation: "数据查询", object: "每日考勤表", range: "特定记录", tool: "Agent 查询", result: "权限不足", ip: "192.168.1.102" },
];

const sensitiveFields = [
  { id: "1", field: "employee_salary", dataset: "员工信息表", type: "薪资", masking: "脱敏显示(前缀)", roles: "管理员, HR部门" },
  { id: "2", field: "phone_number", dataset: "客户信息表", type: "个人信息", masking: "部分隐藏", roles: "管理员, 销售部门" },
  { id: "3", field: "bank_account", dataset: "财务信息表", type: "金融信息", masking: "完全隐藏", roles: "管理员" },
];

export function PermissionAudit() {
  const [activeTab, setActiveTab] = useState("用户管理");
  const [searchTerm, setSearchTerm] = useState("");

  const actionLabel: Record<string, string> = {
    "用户管理": "添加用户", "角色管理": "创建角色", "数据集权限": "配置权限", "敏感字段": "标记敏感字段",
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
        {/* 筛选区 + 操作区 */}
        <div className="flex items-center gap-3">
          <div className="relative max-w-sm flex-1">
            <Search className="absolute left-3 top-1/2 -translate-y-1/2 size-4 text-gray-400" />
            <Input placeholder="搜索..." value={searchTerm} onChange={e => setSearchTerm(e.target.value)} className="pl-10" />
          </div>
          <div className="ml-auto flex gap-2">
            {activeTab === "审计日志" ? (
              <Button variant="outline"><Eye className="size-4 mr-2" />导出日志</Button>
            ) : actionLabel[activeTab] ? (
              <Button><Plus className="size-4 mr-2" />{actionLabel[activeTab]}</Button>
            ) : null}
          </div>
        </div>

        {/* 统计卡片 */}
        <div className="grid grid-cols-4 gap-4">
          <Card className="p-5 flex flex-col justify-between h-[160px]">
            <div className="flex items-center justify-between gap-2">
              <div className="flex items-center gap-2 min-w-0">
                <div className="p-2 bg-blue-100 rounded-lg shrink-0"><Users className="size-4 text-blue-600" /></div>
                <span className="text-sm text-gray-500 truncate">活跃用户</span>
              </div>
              <span className="text-xs text-green-600 bg-green-50 px-1.5 py-0.5 rounded shrink-0 whitespace-nowrap">在线</span>
            </div>
            <div className="flex items-baseline gap-2">
              <span className="text-3xl font-bold text-gray-800 truncate min-w-0">45</span>
              <span className="text-xs text-green-600 bg-green-50 px-1.5 py-0.5 rounded shrink-0 whitespace-nowrap">↑ 3 较昨日</span>
            </div>
            <div className="text-xs text-gray-400">在线用户</div>
          </Card>
          <Card className="p-5 flex flex-col justify-between h-[160px]">
            <div className="flex items-center justify-between gap-2">
              <div className="flex items-center gap-2 min-w-0">
                <div className="p-2 bg-purple-100 rounded-lg shrink-0"><Shield className="size-4 text-purple-600" /></div>
                <span className="text-sm text-gray-500 truncate">角色数量</span>
              </div>
              <span className="text-xs text-gray-500 bg-gray-100 px-1.5 py-0.5 rounded shrink-0 whitespace-nowrap">持平</span>
            </div>
            <div className="flex items-baseline gap-2">
              <span className="text-3xl font-bold text-gray-800 truncate min-w-0">8</span>
              <span className="text-xs text-gray-400 bg-gray-100 px-1.5 py-0.5 rounded shrink-0 whitespace-nowrap">较昨日持平</span>
            </div>
            <div className="text-xs text-gray-400">管理员 · 财务 · 销售 等</div>
          </Card>
          <Card className="p-5 flex flex-col justify-between h-[160px]">
            <div className="flex items-center justify-between gap-2">
              <div className="flex items-center gap-2 min-w-0">
                <div className="p-2 bg-orange-100 rounded-lg shrink-0"><Lock className="size-4 text-orange-500" /></div>
                <span className="text-sm text-gray-500 truncate">敏感字段</span>
              </div>
              <span className="text-xs text-gray-500 bg-gray-100 px-1.5 py-0.5 rounded shrink-0 whitespace-nowrap">权限保护</span>
            </div>
            <div className="flex items-baseline gap-2">
              <span className="text-3xl font-bold text-gray-800 truncate min-w-0">{sensitiveFields.length}</span>
              <span className="text-xs text-orange-600 bg-orange-50 px-1.5 py-0.5 rounded shrink-0 whitespace-nowrap">+1 本月</span>
            </div>
            <div className="text-xs text-gray-400">PII · 金融 · 商业机密</div>
          </Card>
          <Card className="p-5 flex flex-col justify-between h-[160px]">
            <div className="flex items-center justify-between gap-2">
              <div className="flex items-center gap-2 min-w-0">
                <div className="p-2 bg-green-100 rounded-lg shrink-0"><FileText className="size-4 text-green-600" /></div>
                <span className="text-sm text-gray-500 truncate">今日访问</span>
              </div>
              <span className="text-xs text-green-600 bg-green-50 px-1.5 py-0.5 rounded shrink-0 whitespace-nowrap">正常</span>
            </div>
            <div className="flex items-baseline gap-2">
              <span className="text-3xl font-bold text-gray-800 truncate min-w-0">156</span>
              <span className="text-xs text-green-600 bg-green-50 px-1.5 py-0.5 rounded shrink-0 whitespace-nowrap">↑ 12%</span>
            </div>
            <div className="text-xs text-gray-400">访问次数</div>
          </Card>
        </div>

        {/* 内容区 */}
        {activeTab === "用户管理" && (
          <div className="bg-white rounded-lg border border-gray-200">
            <Table>
              <TableHeader>
                <TableRow>
                  <TableHead>用户名</TableHead><TableHead>姓名</TableHead><TableHead>部门</TableHead>
                  <TableHead>角色</TableHead><TableHead>状态</TableHead><TableHead>最近登录</TableHead>
                  <TableHead className="text-right">操作</TableHead>
                </TableRow>
              </TableHeader>
              <TableBody>
                <TableRow>
                  <TableCell>admin</TableCell><TableCell>管理员</TableCell><TableCell>IT部门</TableCell>
                  <TableCell><Badge variant="outline" className="bg-blue-50 text-blue-700 border-blue-200">管理员</Badge></TableCell>
                  <TableCell><Badge variant="outline" className="bg-green-50 text-green-700 border-green-200">活跃</Badge></TableCell>
                  <TableCell>2026-06-29 10:00</TableCell>
                  <TableCell className="text-right"><Button variant="ghost" size="sm">编辑</Button></TableCell>
                </TableRow>
                <TableRow>
                  <TableCell>zhangsan</TableCell><TableCell>张三</TableCell><TableCell>财务部门</TableCell>
                  <TableCell><Badge variant="outline">财务部门</Badge></TableCell>
                  <TableCell><Badge variant="outline" className="bg-green-50 text-green-700 border-green-200">活跃</Badge></TableCell>
                  <TableCell>2026-06-29 09:45</TableCell>
                  <TableCell className="text-right"><Button variant="ghost" size="sm">编辑</Button></TableCell>
                </TableRow>
              </TableBody>
            </Table>
          </div>
        )}

        {activeTab === "角色管理" && (
          <div className="space-y-3">
            {[
              { icon: Shield, color: "text-blue-600", bg: "bg-blue-50", name: "管理员", count: 5, desc: "拥有所有数据和功能的访问权限" },
              { icon: Building2, color: "text-purple-600", bg: "bg-purple-50", name: "财务部门", count: 12, desc: "可访问财务相关数据表和报表" },
              { icon: Building2, color: "text-green-600", bg: "bg-green-50", name: "销售部门", count: 18, desc: "可访问销售订单和客户信息" },
            ].map(role => (
              <div key={role.name} className="p-4 bg-white border border-gray-200 rounded-lg flex items-center justify-between">
                <div className="flex items-center gap-3">
                  <div className={`p-2 ${role.bg} rounded-lg`}><role.icon className={`size-4 ${role.color}`} /></div>
                  <div>
                    <div className="font-medium">{role.name}</div>
                    <div className="text-sm text-gray-500">{role.desc}</div>
                  </div>
                </div>
                <div className="flex items-center gap-3">
                  <Badge variant="outline">{role.count} 人</Badge>
                  <Button variant="ghost" size="sm">编辑</Button>
                  <Button variant="ghost" size="sm">查看成员</Button>
                </div>
              </div>
            ))}
          </div>
        )}

        {activeTab === "数据集权限" && (
          <div className="bg-white rounded-lg border border-gray-200">
            <Table>
              <TableHeader>
                <TableRow>
                  <TableHead>数据集名称</TableHead><TableHead>可访问角色</TableHead><TableHead>可访问部门</TableHead>
                  <TableHead>字段限制</TableHead><TableHead>Agent 继承</TableHead><TableHead className="text-right">操作</TableHead>
                </TableRow>
              </TableHeader>
              <TableBody>
                <TableRow>
                  <TableCell>销售订单表</TableCell>
                  <TableCell><div className="flex gap-1"><Badge variant="outline" className="text-xs">管理员</Badge><Badge variant="outline" className="text-xs">销售部门</Badge></div></TableCell>
                  <TableCell><Badge variant="outline" className="text-xs">全部</Badge></TableCell>
                  <TableCell>无限制</TableCell>
                  <TableCell><Badge variant="outline" className="bg-blue-50 text-blue-700 border-blue-200">是</Badge></TableCell>
                  <TableCell className="text-right"><Button variant="ghost" size="sm">编辑</Button></TableCell>
                </TableRow>
                <TableRow>
                  <TableCell>每日考勤表</TableCell>
                  <TableCell><div className="flex gap-1"><Badge variant="outline" className="text-xs">管理员</Badge><Badge variant="outline" className="text-xs">HR部门</Badge></div></TableCell>
                  <TableCell><Badge variant="outline" className="text-xs">仅本部门</Badge></TableCell>
                  <TableCell>隐藏薪资字段</TableCell>
                  <TableCell><Badge variant="outline" className="bg-blue-50 text-blue-700 border-blue-200">是</Badge></TableCell>
                  <TableCell className="text-right"><Button variant="ghost" size="sm">编辑</Button></TableCell>
                </TableRow>
              </TableBody>
            </Table>
          </div>
        )}

        {activeTab === "敏感字段" && (
          <div className="bg-white rounded-lg border border-gray-200">
            <Table>
              <TableHeader>
                <TableRow>
                  <TableHead>字段名</TableHead><TableHead>所属数据集</TableHead><TableHead>敏感类型</TableHead>
                  <TableHead>脱敏方式</TableHead><TableHead>可访问角色</TableHead><TableHead className="text-right">操作</TableHead>
                </TableRow>
              </TableHeader>
              <TableBody>
                {sensitiveFields.map(field => (
                  <TableRow key={field.id}>
                    <TableCell className="font-mono text-sm">{field.field}</TableCell>
                    <TableCell>{field.dataset}</TableCell>
                    <TableCell><Badge variant="outline" className="bg-red-50 text-red-700 border-red-200">{field.type}</Badge></TableCell>
                    <TableCell>{field.masking}</TableCell>
                    <TableCell>{field.roles}</TableCell>
                    <TableCell className="text-right"><Button variant="ghost" size="sm">编辑</Button></TableCell>
                  </TableRow>
                ))}
              </TableBody>
            </Table>
          </div>
        )}

        {activeTab === "审计日志" && (
          <div className="bg-white rounded-lg border border-gray-200">
            <Table>
              <TableHeader>
                <TableRow>
                  <TableHead>时间</TableHead><TableHead>用户</TableHead><TableHead>角色</TableHead>
                  <TableHead>操作类型</TableHead><TableHead>操作对象</TableHead><TableHead>数据范围</TableHead>
                  <TableHead>使用工具</TableHead><TableHead>结果</TableHead><TableHead>IP地址</TableHead>
                </TableRow>
              </TableHeader>
              <TableBody>
                {auditLogs.map(log => (
                  <TableRow key={log.id}>
                    <TableCell>{log.time}</TableCell>
                    <TableCell>{log.user}</TableCell>
                    <TableCell><Badge variant="outline" className="text-xs">{log.role}</Badge></TableCell>
                    <TableCell>{log.operation}</TableCell>
                    <TableCell>{log.object}</TableCell>
                    <TableCell className="text-sm">{log.range}</TableCell>
                    <TableCell>{log.tool}</TableCell>
                    <TableCell>
                      {log.result === "成功"
                        ? <Badge variant="outline" className="bg-green-50 text-green-700 border-green-200">成功</Badge>
                        : <Badge variant="outline" className="bg-red-50 text-red-700 border-red-200">{log.result}</Badge>}
                    </TableCell>
                    <TableCell className="font-mono text-xs">{log.ip}</TableCell>
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
