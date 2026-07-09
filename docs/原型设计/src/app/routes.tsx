import { createBrowserRouter } from "react-router";
import { RootLayout } from "./components/RootLayout";
import { HomePage } from "./pages/HomePage";
import { DataSourceList } from "./pages/DataSourceList";
import { DataSourceDetail } from "./pages/DataSourceDetail";
import { IngestionTaskList } from "./pages/IngestionTaskList";
import { IngestionTaskDetail } from "./pages/IngestionTaskDetail";
import { DataTableList } from "./pages/DataTableList";
import { DataTableDetail } from "./pages/DataTableDetail";
import { DataCatalog } from "./pages/DataCatalog";
import { DataQuality } from "./pages/DataQuality";
import { PermissionAudit } from "./pages/PermissionAudit";
import { SemanticModel } from "./pages/SemanticModel";
import { RelationGraph } from "./pages/RelationGraph";
import { AgentService } from "./pages/AgentService";
import { SystemSettings } from "./pages/SystemSettings";

export const router = createBrowserRouter([
  {
    path: "/",
    Component: RootLayout,
    children: [
      { index: true, Component: HomePage },
      { path: "datasources", Component: DataSourceList },
      { path: "datasources/:id", Component: DataSourceDetail },
      { path: "tasks", Component: IngestionTaskList },
      { path: "tasks/:id", Component: IngestionTaskDetail },
      { path: "tables", Component: DataTableList },
      { path: "tables/:id", Component: DataTableDetail },
      { path: "catalog", Component: DataCatalog },
      { path: "quality", Component: DataQuality },
      { path: "permissions", Component: PermissionAudit },
      { path: "semantic", Component: SemanticModel },
      { path: "graph", Component: RelationGraph },
      { path: "agent", Component: AgentService },
      { path: "settings", Component: SystemSettings },
    ],
  },
]);
