import { useState, useEffect } from "react";
import { Outlet, Link, useLocation, useNavigate } from "react-router";
import {
  Home, Database, ListTodo, Table2, BookOpen,
  ShieldCheck, Settings, Brain, Network, Bot,
  Search, Bell, HelpCircle, User, PanelLeftClose, PanelLeftOpen, X, ChevronRight
} from "lucide-react";
import { Input } from "./ui/input";
import { Button } from "./ui/button";
import { Badge } from "./ui/badge";

const navItems = [
  { path: "/", icon: Home, label: "首页" },
  { path: "/datasources", icon: Database, label: "数据源" },
  { path: "/tasks", icon: ListTodo, label: "接入任务" },
  { path: "/tables", icon: Table2, label: "数据表" },
  { path: "/catalog", icon: BookOpen, label: "数据目录" },
  { path: "/quality", icon: ShieldCheck, label: "数据质量" },
  { path: "/permissions", icon: User, label: "权限审计" },
  { path: "/semantic", icon: Brain, label: "语义模型" },
  { path: "/graph", icon: Network, label: "关系图谱" },
  { path: "/agent", icon: Bot, label: "Agent 服务" },
  { path: "/settings", icon: Settings, label: "系统设置" },
];

function getNavItem(pathname: string) {
  // match most specific first
  return navItems.slice().reverse().find(item =>
    item.path === "/" ? pathname === "/" : pathname === item.path || pathname.startsWith(item.path + "/")
  ) ?? navItems[0];
}

interface BrowserTab {
  path: string;
  label: string;
  icon: typeof Home;
}

export function RootLayout() {
  const location = useLocation();
  const navigate = useNavigate();
  const [sidebarOpen, setSidebarOpen] = useState(true);
  const [tabs, setTabs] = useState<BrowserTab[]>(() => {
    const item = getNavItem(location.pathname);
    return [{ path: item.path, label: item.label, icon: item.icon }];
  });

  // When navigating, open a new tab or activate existing
  useEffect(() => {
    const item = getNavItem(location.pathname);
    setTabs(prev => {
      const exists = prev.find(t => t.path === item.path);
      if (exists) return prev;
      return [...prev, { path: item.path, label: item.label, icon: item.icon }];
    });
  }, [location.pathname]);

  const activeTabPath = getNavItem(location.pathname).path;

  function closeTab(e: React.MouseEvent, tabPath: string) {
    e.preventDefault();
    e.stopPropagation();
    if (tabs.length === 1) return; // keep at least one tab
    const idx = tabs.findIndex(t => t.path === tabPath);
    const next = tabs.filter(t => t.path !== tabPath);
    setTabs(next);
    if (tabPath === activeTabPath) {
      // navigate to adjacent tab
      const target = next[Math.min(idx, next.length - 1)];
      navigate(target.path);
    }
  }

  return (
    <div className="flex h-screen bg-gray-50">
      {/* 左侧导航 */}
      <aside className={`${sidebarOpen ? "w-64" : "w-16"} bg-white border-r border-gray-200 flex flex-col transition-all duration-200`}>
        <div className={`p-4 border-b border-gray-200 flex items-center ${sidebarOpen ? "justify-between" : "justify-center"}`}>
          {sidebarOpen && <h1 className="font-semibold">AI 数据平台</h1>}
        </div>
        <nav className="flex-1 overflow-y-auto p-2">
          <ul className="space-y-1">
            {navItems.map((item) => {
              const Icon = item.icon;
              const isActive = location.pathname === item.path ||
                (item.path !== "/" && location.pathname.startsWith(item.path));

              return (
                <li key={item.path}>
                  <Link
                    to={item.path}
                    title={!sidebarOpen ? item.label : undefined}
                    className={`flex items-center gap-3 px-3 py-2 rounded-lg transition-colors ${
                      isActive
                        ? "bg-blue-50 text-blue-600"
                        : "text-gray-700 hover:bg-gray-50"
                    } ${!sidebarOpen ? "justify-center" : ""}`}
                  >
                    <Icon className="size-5 shrink-0" />
                    {sidebarOpen && <span>{item.label}</span>}
                  </Link>
                </li>
              );
            })}
          </ul>
        </nav>
      </aside>

      {/* 主内容区 */}
      <div className="flex-1 flex flex-col overflow-hidden">
        {/* 顶部栏 */}
        <header className="bg-white border-b border-gray-200 px-6 py-3">
          <div className="flex items-center justify-between">
            <div className="flex items-center gap-4 flex-1 max-w-xl">
              <Button variant="ghost" size="icon" onClick={() => setSidebarOpen(!sidebarOpen)} title={sidebarOpen ? "收起侧边栏" : "展开侧边栏"}>
                {sidebarOpen ? <PanelLeftClose className="size-5" /> : <PanelLeftOpen className="size-5" />}
              </Button>
              <div className="relative flex-1">
                <Search className="absolute left-3 top-1/2 -translate-y-1/2 size-4 text-gray-400" />
                <Input
                  placeholder="搜索数据源、数据表、数据集、字段..."
                  className="pl-10"
                />
              </div>
            </div>
            <div className="flex items-center gap-3">
              <Badge variant="outline" className="bg-yellow-50 text-yellow-700 border-yellow-200">
                测试环境
              </Badge>
              <Button variant="ghost" size="icon">
                <Bell className="size-5" />
              </Button>
              <Button variant="ghost" size="icon">
                <HelpCircle className="size-5" />
              </Button>
              <div className="flex items-center gap-2 pl-3 border-l border-gray-200">
                <div className="size-8 bg-blue-100 rounded-full flex items-center justify-center">
                  <User className="size-4 text-blue-600" />
                </div>
                <div className="text-sm">
                  <div>管理员</div>
                  <div className="text-gray-500 text-xs">admin@company.com</div>
                </div>
              </div>
            </div>
          </div>
        </header>

        {/* 面包屑 + 浏览器式标签栏（同一容器） */}
        <div className="bg-gray-100 border-b border-gray-200 flex flex-col">
          {/* 面包屑 */}
          <div className="pl-3 pr-4 pt-2 pb-0 flex items-center gap-1.5 text-xs text-gray-400">
            <Link to="/" className="hover:text-gray-600 transition-colors">首页</Link>
            {activeTabPath !== "/" && (
              <>
                <ChevronRight className="size-3" />
                <span className="text-gray-500">
                  {tabs.find(t => t.path === activeTabPath)?.label}
                </span>
              </>
            )}
          </div>

          {/* 标签行 */}
          <div className="flex items-end pl-0 pr-2 pt-1 gap-0.5 overflow-x-auto overflow-y-hidden">
            {tabs.map((tab) => {
              const Icon = tab.icon;
              const isActive = tab.path === activeTabPath;
              return (
                <Link
                  key={tab.path}
                  to={tab.path}
                  className={`group relative flex items-center gap-1.5 px-3 py-1.5 text-sm min-w-0 max-w-[180px] shrink-0 transition-all select-none ${
                    isActive
                      ? "bg-white text-gray-800 rounded-t border border-b-0 border-gray-200"
                      : "bg-transparent text-gray-500 hover:text-gray-700 hover:bg-white/50 rounded-t"
                  }`}
                >
                  <Icon className="size-3.5 shrink-0 opacity-60" />
                  <span className="truncate">{tab.label}</span>
                  {tabs.length > 1 && (
                    <button
                      onClick={(e) => closeTab(e, tab.path)}
                      className={`ml-1 rounded p-0.5 shrink-0 transition-colors ${
                        isActive
                          ? "text-gray-400 hover:text-gray-600 hover:bg-gray-100"
                          : "opacity-0 group-hover:opacity-100 text-gray-400 hover:text-gray-600"
                      }`}
                    >
                      <X className="size-3" />
                    </button>
                  )}
                  {isActive && <span className="absolute bottom-[-1px] left-0 right-0 h-px bg-white" />}
                </Link>
              );
            })}
          </div>
        </div>

        {/* 页面内容 */}
        <main className="flex-1 overflow-auto bg-white">
          <Outlet />
        </main>
      </div>
    </div>
  );
}
