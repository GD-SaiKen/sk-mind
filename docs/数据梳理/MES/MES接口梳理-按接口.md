# MES 数据查询接口梳理

> 来源: `docs/数据梳理/MES/MES数据查询接口梳理.xlsx` + `MES开放接口.md`，共 25 个接口

---

## 1. 工单查询

### 基本信息

| 项目 | 内容 |
| --- | --- |
| 接口地址 | `/lightmesapi/open/workorderController/filterWorkorder` |
| 请求方式 | **POST** |
| 接口描述 | 通过此接口可以查询对应团队的所有工单，查询结果为一个工单列表集合，默认按工单创建时间倒序排列；单个客户账号调用该接口的每秒请求数（QPS）最大限制为10。 |

### 请求参数

| 参数名称 | 参数说明 | 是否必须 | 数据类型 |
| --- | --- | --- | --- |
| `pageNum` | 查询页 | true | integer(int32) |
| `pageSize` | 每页条数 | true | integer(int32) |
| `startDate` | 开始时间 | false | string(date-time) |
| `endDate` | 结束时间 | false | string(date-time) |
| `requireStartDate` | 要求完工时间查询开始时间 | false | string(date-time) |
| `requireEndDate` | 要求完工时间查询结束时间 | false | string(date-time) |
| `workOrderStatus` | 工单状态 1待确认 2异常 3已确认(工单进度中为 1未完成 2已完成) 4无产品 5部分排产 6未打印 | true | array[integer(int32)] |
| `workorderNo` | 工单号 | false | string |
| `materialNo` | 产品编号 | false | string |
| `materialDesc` | 品名 | false | string |
| `materialSpec` | 规格 | false | string |
| `workorderType` | 工单类型 | false | string |
| `material` | 物料编号或者物料名称或物料规格 | false | string |
| `planFollowWordNo` | 计划跟单号 | false | string |
| `orderMaster` | 跟单员姓名 | false | string |
| `customerRequirement` | 客户定制说明 | false | string |
| `remark` | 工单备注 | false | string |
| `urgentLevelList` | 是否加紧 1加急*/2非加急**/3加急***/0非紧急 | false | array[integer(int32)] |
| `customerRequirementNotNull` | 特殊要求排空 0可以为空 1排除空 | false | integer(int32) |
| `remarkNotNull` | 工单备注 0可以为空 1排除空 | false | integer(int32) |
| `customizationNo` | 客制代码 | false | string |
| `sales` | 业务员 | false | string |
| `customerNo` | 客户代码 | false | string |
| `query` | 搜索内容 | false | string |
| `appQuery` | APP搜索内容 | false | string |
| `startTime` | 开工日期开始时间 | false | string(date-time) |
| `endTime` | 开工日期结束时间 | false | string(date-time) |
| `startCreateTime` | 创建时间开始时间 | false | string(date-time) |
| `endCreateTime` | 创建日期结束时间 | false | string(date-time) |
| `minPlanQty` | 工单数量最小值 | false | number |
| `maxPlanQty` | 工单数量最大值 | false | number |
| `minOrderQty` | 订单数量最小值 | false | number |
| `maxOrderQty` | 订单数量最大值 | false | number |
| `actualStartTime` | 实际完成日期开始时间 | false | string(date-time) |
| `actualEndTime` | 实际完成日期结束时间 | false | string(date-time) |
| `customerNoNotNull` | 客户代码排空 0可以为空 1排除空 | false | integer(int32) |
| `statusList` | 是否完成 0未完成 1已完成 | false | array[integer(int32)] |
| `salesorderNo` | 销售单号 | false | string |
| `orderByDTOS` | 排序规则 | false | array OrderByDTO |
| `--orderByDTOS.grade` | 等级越大排序规则也优先 | false | integer(int32) |
| `--orderByDTOS.orderName` | 排序字段 | false | string |
| `--orderByDTOS.sort` | 排序规则 | false | string |

### 响应数据字段

| 字段名称 | 字段说明 | 数据类型 |
| --- | --- | --- |
| `woid` | 工单id | integer(int64) |
| `workorderNo` | 工单号 | string |
| `workorderType` | 工单类型 | string |
| `urgentLevel` | 0特别加急/1非常紧急/2紧急/9非紧急 | integer(int32) |
| `mtid` | 物料id | integer(int64) |
| `materialNo` | 料号 | string |
| `materialDesc` | 物料名称(品名) | string |
| `materialSpec` | 规格 | string |
| `unit` | 单位 | string |
| `rid` | 工艺路线id | integer(int64) |
| `planQty` | 工单数量(计划加工数量) | number |
| `completedQty` | 完工数量 | number |
| `progress` | 完工进度 | string |
| `requireEndTime` | 要求完工日期 | string(date-time) |
| `createTime` | 创建日期 | string(date-time) |
| `startTime` | 预计开工日期 | string(date-time) |
| `endTime` | 工单交期 | string(date-time) |
| `customerNo` | 客户代码 | string |
| `customizationNo` | 客制代码 | string |
| `customerRequirement` | 客户定制说明 | string |
| `remark` | 工单备注 | string |
| `orderMaster` | 跟单员 | string |
| `planFollowWordNo` | 计划跟踪号 | string |
| `status` | 工单状态：1待确认/2异常/3已确认/5部分确认/9已结产 | integer(int32) |
| `errorInfo` | 异常信息 | string |
| `notes` | 排产批注 | string |
| `estimatedStartTime` | 预计开始日期 | string(date-time) |
| `estimatedEndTime` | 预计结束日期 | string(date-time) |
| `routingsMaterialNo` | 工艺路线参考物料编号 | string |
| `materialStatus` | 物料状态 0存在 1不存在 2未确认 | integer(int32) |
| `sales` | 业务员 | string |
| `completeProgress` | 进度 | number |
| `actualCompleteTime` | 实际完成日期 | string(date-time) |
| `overdueCount` | 逾期天数 | integer(int64) |
| `salesorderNo` | 销售单号 | string |
| `currentProcedure` | 当前工序 | string |
| `nextProcedure` | 下一道工序 | string |
| `allProcedure` | 工艺路线 | string |
| `surplusQty` | 剩余数量 | number |
| `materialLedgerDesc` | 材料名称 | string |
| `materialLedgerSpec` | 材料规格 | string |
| `supplier` | 材料品牌 | string |
| `orderQty` | 订单数量 | number |
| `closeUid` | 结案人员 | integer(int64) |
| `closeTime` | 结案时间 | string(date-time) |
| `closeUserName` | 结案人员 | string |
| `createTuid` | 创建人id | integer(int64) |
| `createUserName` | 创建人 | string |
| `materialPrice` | 产品单价 | number |
| `materialTotalPrice` | 产品总价 | number |
| `standardWorkHours` | 标准工时 | number |
| `printNumber` | 打印次数 | integer(int32) |
| `portionQty` | 排产数量 | number |
| `customerMaterialCode` | 客户对应的物料代码 | string |
| `arrangedQty` | 排产数量 | number |
| `projectNumber` | 项目号 | string |
| `orderNumber` | 订单号 | string |
| `customerMaterialName` | 客户物料名称 | string |
| `closeRemark` | 结案备注 | string |
| `simpleProcedureVOS` | 工艺路线 | array SimpleProcedureVO |
| `--simpleProcedureVOS[].procedureContent` | 工序内容 | string |
| `--simpleProcedureVOS[].procedureName` | 工序名称 | string |
| `--simpleProcedureVOS[].procedureNo` | 工序编号 | string |
| `--simpleProcedureVOS[].procedureRemark` | 工序备注 | string |
| `--simpleProcedureVOS[].singleTripTime` | 单趟加工时长 | number |
| `--simpleProcedureVOS[].status` | 是否完成 0否 1是 | integer(int32) |
| `--simpleProcedureVOS[].timePreparation` | 准备时长 | number |
| `customFields` | 自定义字段值（fieldCode 为英文字段编码）；无自定义字段或未配置时不返回 | array EntityCustomFieldValueItemVO |
| `--customFields[].entityType` | 实体类型，如 WORKORDER | string |
| `--customFields[].fieldCode` | 字段英文名 | string |
| `--customFields[].fieldValue` | 字段值 | string |
| `--customFields[].required` | 是否必填 0否 1是 | integer(int32) |

---

## 2. 查询达成率报表

### 基本信息

| 项目 | 内容 |
| --- | --- |
| 接口地址 | `/lightmesapi/open/workorderController/selectComplishReport` |
| 请求方式 | **POST** |
| 接口描述 | 通过此接口可以查询达成率报表。单个客户账号调用该接口的每秒请求数（QPS）最大限制为10。 |

### 请求参数

| 参数名称 | 参数说明 | 是否必须 | 数据类型 |
| --- | --- | --- | --- |
| `pageNum` | 查询页 | true | integer(int32) |
| `pageSize` | 每页条数 | true | integer(int32) |
| `wcids` | 工作中心id | false | array[integer(int64)] |
| `did` | 部门id | false | integer(int64) |
| `shiftName` | 班次名称 | false | string |
| `startTime` | 开始时间 | true | string(date-time) |
| `endTime` | 结束时间 | true | string(date-time) |
| `status` | 状态 1任务维度 2数量维度 | true | integer(int32) |

### 响应数据字段

| 字段名称 | 字段说明 | 数据类型 |
| --- | --- | --- |
| `sid` | 班次id | integer(int64) |
| `shiftName` | 班次名称 | string |
| `workDate` | 日期 | string(date-time) |
| `departmentName` | 部门名称 | string |
| `taskCount` | 任务单数 | integer(int32) |
| `completedTaskCount` | 达成单数 | integer(int32) |
| `unCompletedTaskCount` | 未达成单数 | integer(int32) |
| `taskQty` | 任务数量 | number |
| `completedTaskQty` | 达成数量 | number |
| `unCompletedTaskQty` | 未达成数量 | number |
| `completeRate` | 达成率 | number |
| `qtyCompleteRate` | 数量达成率 | number |

---

## 3. 工序报工结果查询

### 基本信息

| 项目 | 内容 |
| --- | --- |
| 接口地址 | `/lightmesapi/open/workorderController/selectProceduresReportDataByTime` |
| 请求方式 | **POST** |
| 接口描述 | 通过此接口可以查询指定时间段内的所有工序报工结果信息，时间段最大1天。单个客户账号调用该接口的每秒请求数（QPS）最大限制为10。 |

### 请求参数

| 参数名称 | 参数说明 | 是否必须 | 数据类型 |
| --- | --- | --- | --- |
| `startTime` | 查询开始时间yyyy-MM-dd HH:mm:ss | true | string(date-time) |
| `endTime` | 查询结束时间yyyy-MM-dd HH:mm:ss | true | string(date-time) |

### 响应数据字段

| 字段名称 | 字段说明 | 数据类型 |
| --- | --- | --- |
| `goodQty` | 报工良品数 | number |
| `badQty` | 不良品总和 | number |
| `badQtyManufacturing` | 加工不良 | number |
| `badQtyIncoming` | 来料不良 | number |
| `woid` | 工单id | integer(int64) |
| `workorderNo` | 工单编号 | string |
| `workorderType` | 工单类型 | string |
| `salesorderNo` | 销售单号 | string |
| `planFollowWordNo` | 计划跟单号 | string |
| `materialNo` | 物料编号 | string |
| `materialDesc` | 物料名称 | string |
| `unit` | 单位 | string |
| `materialSpec` | 物料规格 | string |
| `warehouse` | 仓库 | string |
| `productionBatchNo` | 生产批号 | string |
| `materialQty` | 原料标识数量 | number |
| `weight` | 布头布尾KG | number |
| `materialUnit` | 原料标识单位 | string |
| `knifeWeight` | 栏刀口料KG | number |
| `materialWeight` | 原料重量 | number |
| `pieceWeight` | 产品单片重量 | number |
| `scrapWeight` | 角料重量 | number |
| `taskActionRemark` | 任务备注 | string |
| `inStockQty` | 入库数 | number |
| `transferCardNo` | 流转卡号 | string |
| `wtaid` | 工单任务id | integer(int64) |
| `tid` | 团队id | integer(int64) |
| `procedureNo` | 工序编号 | string |
| `procedureOrder` | 工序顺序 | integer(int32) |
| `procedureName` | 工序名称 | string |
| `actualTime` | 使用时长 | number |
| `earnedHours` | 产出工时 | number |
| `userNames` | 操作人员 | string |
| `employeeNos` | 人员工号 | string |
| `machineNo` | 设备编号 | string |
| `machineName` | 设备名称 | string |
| `workcenterNo` | 工作中心编号 | string |
| `workcenterName` | 工作中心名称 | string |
| `workshopName` | 车间 | string |
| `productLine` | 产线 | string |
| `taskStartTime` | 开始日期yyyy-MM-dd HH:mm:ss | string |
| `taskEndTime` | 结束时间 yyyy-MM-dd HH:mm:ss | string |
| `workorderPlanQty` | 工单数量 | number |
| `component` | 子件 | string |
| `materialCode` | 原料代码 | string |
| `materialBatchNo` | 原料批号 | string |
| `procedureRemark` | 工序备注 | string |
| `singleTripQty` | 单趟加工数量 | number |
| `singleTripTime` | 单趟加工时长(秒) | number |
| `frequencySize` | 脉冲次数 | integer(int32) |
| `oneLevelReason` | 一级审核 | string |
| `twoLevelReason` | 二级审核 | string |
| `threeLevelReason` | 三级审核 | string |
| `approverName` | 审核人员 | string |
| `approverTime` | 审核日期 | string |
| `workDate` | 生产日期 | string |
| `shiftName` | 班次名称 | string |
| `mouldNo` | 模具编号 | string |
| `mouldName` | 模具名称 | string |
| `planQty` | 工单数量 | number |
| `createTime` | 工单创建日期 | string(date-time) |
| `note` | 备注 | string |
| `completionStage` | 工单完工进度标识 | integer(int32) |
| `chassisNo` | 底盘号/盘底号 | string |
| `rearOutriggerCode` | 后支腿编码 | string |

---

## 4. 工序排产结果查询

### 基本信息

| 项目 | 内容 |
| --- | --- |
| 接口地址 | `/lightmesapi/open/workorderController/selectProductionBackParamsByTime` |
| 请求方式 | **POST** |
| 接口描述 | 通过此接口可以查询指定时间段内的所有工序排产结果信息，时间段最大1天。单个客户账号调用该接口的每秒请求数（QPS）最大限制为10。 |

### 请求参数

| 参数名称 | 参数说明 | 是否必须 | 数据类型 |
| --- | --- | --- | --- |
| `pageNum` | 查询页 | true | integer(int32) |
| `pageSize` | 每页条数 | true | integer(int32) |
| `startTime` | 查询开始时间yyyy-MM-dd HH:mm:ss | true | string(date-time) |
| `endTime` | 查询结束时间yyyy-MM-dd HH:mm:ss | true | string(date-time) |
| `query` | 搜索内容 | false | string |

### 响应数据字段

| 字段名称 | 字段说明 | 数据类型 |
| --- | --- | --- |
| `wopid` | 工序任务id | string |
| `workorderNo` | 工单编号 | string |
| `salesorderNo` | 销单号 | string |
| `materialNo` | 物料编号 | string |
| `materialDesc` | 物料名称 | string |
| `materialSpec` | 物料规格 | string |
| `procedureNo` | 工序编号 | string |
| `procedureName` | 工序名称 | string |
| `planFollowWordNo` | 计划跟踪号 | string |
| `planQty` | 计划数量 | number |
| `pendingQty` | 待排产数 | number |
| `arrangedQty` | 已排产数 | number |
| `completedQty` | 完工数 | number |
| `procedureOrder` | 工序序号 | integer(int32) |
| `completionStage` | 是否工单完结点 0非 1是 | integer(int32) |
| `productionBackWorkcenters` |  | array ProductionBackWorkcenter |
| `--productionBackWorkcenters[].departmentName` | 生产部门 | string |
| `--productionBackWorkcenters[].estimatedEndTime` | 预计结束时间 | string |
| `--productionBackWorkcenters[].estimatedStartTime` | 预计开始时间 | string |
| `--productionBackWorkcenters[].machineName` | 设备名称 | string |
| `--productionBackWorkcenters[].machineNo` | 设备编号 | string |
| `--productionBackWorkcenters[].planQty` | 计划数量 | number |
| `--productionBackWorkcenters[].workDate` | 排产时间 | string |
| `--productionBackWorkcenters[].workcenterName` | 工作中心名称 | string |
| `--productionBackWorkcenters[].workcenterNo` | 工作中心编号 | string |
| `--productionBackWorkcenters[].wtid` | 任务id | string |

---

## 5. 查询投料明细

### 基本信息

| 项目 | 内容 |
| --- | --- |
| 接口地址 | `/lightmesapi/open/workorderController/selectTaskUseMaterial` |
| 请求方式 | **POST** |
| 接口描述 | 通过此接口可以查询到指定时间段内的投料明细。单个客户账号调用该接口的每秒请求数（QPS）最大限制为10。 |

### 请求参数

| 参数名称 | 参数说明 | 是否必须 | 数据类型 |
| --- | --- | --- | --- |
| `pageNum` | 查询页 | true | integer(int32) |
| `pageSize` | 每页条数 | true | integer(int32) |
| `startTime` | 开始时间 | false | string(date-time) |
| `endTime` | 结束时间 | false | string(date-time) |
| `workorderNo` | 工单号 | false | string |
| `useMaterial` | 物料编码 | false | string |
| `materialBatchNo` | 物料批号 | false | string |

### 响应数据字段

| 字段名称 | 字段说明 | 数据类型 |
| --- | --- | --- |
| `workorderNo` | 工单号 | string |
| `taskNo` | 任务编号 | string |
| `did` | 产线id | integer(int64) |
| `workShop` | 车间 | string |
| `productLine` | 产线 | string |
| `wcid` | 工作中心id | integer(int64) |
| `workcenterNo` | 工作中心编号 | string |
| `workcenterName` | 工作中心名称 | string |
| `procedureNo` | 工序编号 | string |
| `procedureName` | 工序名称 | string |
| `useMaterial` | 物料编码 | string |
| `useMaterialDesc` | 物料名称 | string |
| `materialBatchNo` | 批号 | string |
| `useQty` | 投料数量 | number |
| `useUnit` | 单位 | string |
| `quantity` | 用量 | number |
| `useTime` | 投料时间 | string(date-time) |
| `uid` | 投料人员id | integer(int64) |
| `userName` | 投料人员姓名 | string |
| `urlStr` | 照片 | string |
| `urls` | 照片列表 | array[string] |

---

## 6. 工序任务查询

### 基本信息

| 项目 | 内容 |
| --- | --- |
| 接口地址 | `/lightmesapi/open/workorderController/selectWorkorderProcedure` |
| 请求方式 | **POST** |
| 接口描述 | 通过此接口可以查询到指定时间段内有变化的工序任务信息。单个客户账号调用该接口的每秒请求数（QPS）最大限制为10。 |

### 请求参数

| 参数名称 | 参数说明 | 是否必须 | 数据类型 |
| --- | --- | --- | --- |
| `pageNum` | 查询页 | true | integer(int32) |
| `pageSize` | 每页条数 | true | integer(int32) |
| `startTime` | 开始时间 | false | string(date-time) |
| `endTime` | 结束时间 | false | string(date-time) |

### 响应数据字段

| 字段名称 | 字段说明 | 数据类型 |
| --- | --- | --- |
| `wopid` | 工序任务id | integer(int64) |
| `workorderNo` | 工单编号 | string |
| `salesorderNo` | 销售单号 | string |
| `materialNo` | 产品编码 | string |
| `materialDesc` | 品名 | string |
| `materialSpec` | 规格 | string |
| `planFollowWordNo` | 计划跟踪号 | string |
| `procedureNo` | 工序任务编号 | string |
| `procedureName` | 工序任务名称 | string |
| `planQty` | 计划数 | number |
| `pendingQty` | 待排产数 | number |
| `arrangedQty` | 已排产数 | number |
| `completedQty` | 完工数 | number |

---

## 7. 工单报工结果查询

### 基本信息

| 项目 | 内容 |
| --- | --- |
| 接口地址 | `/lightmesapi/open/workorderController/selectWorkorderReportDataByTime` |
| 请求方式 | **POST** |
| 接口描述 | 通过此接口可以查询指定时间段内的所有工单报工结果信息，时间段最大1天。单个客户账号调用该接口的每秒请求数（QPS）最大限制为10。 |

### 请求参数

| 参数名称 | 参数说明 | 是否必须 | 数据类型 |
| --- | --- | --- | --- |
| `startTime` | 查询开始时间yyyy-MM-dd HH:mm:ss | true | string(date-time) |
| `endTime` | 查询结束时间yyyy-MM-dd HH:mm:ss | true | string(date-time) |

### 响应数据字段

| 字段名称 | 字段说明 | 数据类型 |
| --- | --- | --- |
| `goodQty` | 报工良品数 | number |
| `badQty` | 不良品总和 | number |
| `badQtyManufacturing` | 加工不良 | number |
| `badQtyIncoming` | 来料不良 | number |
| `woid` | 工单id | integer(int64) |
| `workorderNo` | 工单编号 | string |
| `workorderType` | 工单类型 | string |
| `salesorderNo` | 销售单号 | string |
| `planFollowWordNo` | 计划跟单号 | string |
| `materialNo` | 物料编号 | string |
| `materialDesc` | 物料名称 | string |
| `unit` | 单位 | string |
| `materialSpec` | 物料规格 | string |
| `warehouse` | 仓库 | string |
| `productionBatchNo` | 生产批号 | string |
| `materialQty` | 原料标识数量 | number |
| `weight` | 布头布尾KG | number |
| `materialUnit` | 原料标识单位 | string |
| `knifeWeight` | 栏刀口料KG | number |
| `materialWeight` | 原料重量 | number |
| `pieceWeight` | 产品单片重量 | number |
| `scrapWeight` | 角料重量 | number |
| `taskActionRemark` | 任务备注 | string |
| `inStockQty` | 入库数 | number |
| `transferCardNo` | 流转卡号 | string |
| `wtaid` | 工单任务id | integer(int64) |
| `tid` | 团队id | integer(int64) |
| `procedureNo` | 工序编号 | string |
| `procedureOrder` | 工序顺序 | integer(int32) |
| `procedureName` | 工序名称 | string |
| `actualTime` | 使用时长 | number |
| `earnedHours` | 产出工时 | number |
| `userNames` | 操作人员 | string |
| `employeeNos` | 人员工号 | string |
| `machineNo` | 设备编号 | string |
| `machineName` | 设备名称 | string |
| `workcenterNo` | 工作中心编号 | string |
| `workcenterName` | 工作中心名称 | string |
| `workshopName` | 车间 | string |
| `productLine` | 产线 | string |
| `taskStartTime` | 开始日期 | string |
| `taskEndTime` | 结束时间 | string |
| `workorderPlanQty` | 工单数量 | number |
| `component` | 子件 | string |
| `materialCode` | 原料代码 | string |
| `materialBatchNo` | 原料批号 | string |
| `procedureRemark` | 工序备注 | string |
| `singleTripQty` | 单趟加工数量 | number |
| `singleTripTime` | 单趟加工时长(秒) | number |
| `frequencySize` | 脉冲次数 | integer(int32) |
| `oneLevelReason` | 一级审核 | string |
| `twoLevelReason` | 二级审核 | string |
| `threeLevelReason` | 三级审核 | string |
| `approverName` | 审核人员 | string |
| `approverTime` | 审核日期 | string |
| `workDate` | 生产日期 | string |
| `shiftName` | 班次名称 | string |
| `mouldNo` | 模具编号 | string |
| `mouldName` | 模具名称 | string |
| `planQty` | 工单数量 | number |
| `createTime` | 工单创建日期 | string(date-time) |
| `note` | 备注 | string |
| `completionStage` | 工单完工进度标识 | integer(int32) |
| `chassisNo` | 底盘号/盘底号 | string |
| `rearOutriggerCode` | 后支腿编码 | string |

---

## 8. 报工明细查询

### 基本信息

| 项目 | 内容 |
| --- | --- |
| 接口地址 | `/lightmesapi/open/workorderController/selectWorkorderTaskActionStatistics` |
| 请求方式 | **POST** |
| 接口描述 | 通过此接口可以查询到报工明细。单个客户账号调用该接口的每秒请求数（QPS）最大限制为10。 |

### 请求参数

| 参数名称 | 参数说明 | 是否必须 | 数据类型 |
| --- | --- | --- | --- |
| `pageNum` | 查询页 | true | integer(int32) |
| `pageSize` | 每页条数 | true | integer(int32) |
| `did` | 产线id | true | integer(int64) |
| `departmentName` | 车间名称 | false | string |
| `startTime` | 开始时间 | false | string(date-time) |
| `endTime` | 结束时间 | false | string(date-time) |
| `wcidList` | 工作中心id列表 | false | array[integer(int64)] |
| `workorderNo` | 工单号 | false | string |
| `procedureNo` | 工序编号 | false | string |
| `materialNo` | 料号 | false | string |
| `machineNo` | 设备编号 | false | string |
| `shiftTimeName` | 班次名称 | false | string |
| `materialDesc` | 品名 | false | string |
| `materialSpec` | 规格 | false | string |
| `taskNo` | 生产任务单号 | false | string |
| `workcenterNo` | 工作中心编码或名称 | false | string |
| `startDate` | 开始时间 | false | string(date-time) |
| `endDate` | 结束时间 | false | string(date-time) |
| `query` | 搜索输入内容 | false | string |
| `employeeName` | 姓名 | false | string |
| `employeeNo` | 工号 | false | string |
| `productionBatchNo` | 生产批号 | false | string |
| `statusList` | 审批状态 0待审批 1已审批 | true | array[integer(int32)] |
| `shiftStartTime` | 班次开始时间 | true | string(date-time) |
| `shiftEndTime` | 班次结束时间 | true | string(date-time) |
| `startDateStr` | 开始日期 | false | string |
| `endDateStr` | 结束日期 | false | string |
| `workorderType` | 工单类型 | false | string |
| `sumType` | 合计类型 1获得工时 2产出时长 3综合工时 | false | integer(int32) |
| `exportType` | 1按获得工时导出 2导出 | false | integer(int32) |
| `workType` | 工种 1临时工 2正式工 | false | integer(int32) |
| `status` | 1进行中 2提交 3审核中 4完成 9挂起 | false | integer(int32) |
| `userName` | 生产人员 | false | string |
| `reportUserName` | 报工人员 | false | string |
| `reportUidList` | 报工人员id集合 | false | array[integer(int64)] |
| `tuidList` | 生产人员id集合 | false | array[integer(int64)] |
| `customerRequirement` | 客制特殊需求 | false | string |

### 响应数据字段

| 字段名称 | 字段说明 | 数据类型 |
| --- | --- | --- |
| `wtid` | 任务id | integer(int64) |
| `wtaid` | 任务执行id | integer(int64) |
| `endTime` | 报工时间 | string(date-time) |
| `woid` | 工单id | integer(int64) |
| `departmentName` | 车间名称 | string |
| `workorderNo` | 工单号 | string |
| `workorderType` | 工单类型 | string |
| `unit` | 单位 | string |
| `taskNo` | 任务编号 | string |
| `rpid` | 工序id | integer(int64) |
| `procedureNo` | 工序编号 | string |
| `procedureName` | 工序名称 | string |
| `mtid` | 物料id | integer(int64) |
| `materialNo` | 料号 | string |
| `materialDesc` | 品名 | string |
| `materialSpec` | 规格 | string |
| `mid` | 设备id | integer(int64) |
| `pulse` | 有无脉冲 0无脉冲 1有脉冲 | integer(int32) |
| `sid` | 工厂日历表主键 | integer(int64) |
| `shiftTimeName` | 班次时间以及日期 | string |
| `machineNo` | 设备编号 | string |
| `machineName` | 设备名称 | string |
| `planQty` | 计划数量 | number |
| `productionQty` | 未完成数量 | number |
| `goodQty` | 良品数量 | number |
| `theoreticalQty` | 理论产出数量 | number |
| `perHourOutput` | 标准时产量 | number |
| `badQtyManufacturing` | 加工不良 | number |
| `badQtyIncoming` | 来料不良 | number |
| `produceHours` | 产出工时 | number |
| `machineHours` | 机器用时 | number |
| `peopleHours` | 人员工时 | number |
| `mouldStartTime` | 开始换模时间 | string(date-time) |
| `mouldEndTime` | 结束换模时间 | string(date-time) |
| `startTime` | 开始加工时间 | string(date-time) |
| `operatorList` | 操作人员 | string |
| `mouldList` | 换模人员 | string |
| `timeMouldChange` | 换模时长 | number |
| `actualTimeMouldChange` | 实际换模时长 | number |
| `earnedHours` | 获得工时 | number |
| `compensateHours` | 奖惩工时 | number |
| `materialBatchNo` | 原材料批次号 | string |
| `greenDuration` | 绿灯时长 | number |
| `yellowDuration` | 黄灯时长 | number |
| `redDuration` | 红灯时长 | number |
| `closeDuration` | 关灯时长 | number |
| `andonDuration` | 安灯时长 | number |
| `taskCount` | 实际模次 | integer(int64) |
| `taskActionRemark` | 备注 | string |
| `routingsMaterialNo` | 工艺路线参考物料编号 | string |
| `picUrl` | 报工图片或地址 | string |
| `picType` | 1图片 2视频 | integer(int32) |
| `inStockQty` | 入库数 | number |
| `inStockRate` | 入库率 | number |
| `materialQty` | 原料标识数量 | number |
| `weight` | 布头布尾KG | number |
| `materialUnit` | 原料标识单位 | string |
| `productionBatchNo` | 生产批号 | string |
| `isolationBadQty` | 隔离不良数 | number |
| `knifeWeight` | 栏刀口料KG | number |
| `materialWeight` | 原材料重量 | number |
| `pieceWeight` | 产品单片重量 | number |
| `scrapWeight` | 角料重量 | number |
| `effectiveDuration` | 不计考核的异常时长 | number |
| `freeTime` | 休息时长 | number |
| `theoreticalDuration` | 理论产出 | number |
| `planCompleteRate` | 计划达成率 | number |
| `standardCompleteRate` | 标准达成率 | number |
| `productionRate` | 生产效率 | number |
| `greenRate` | 绿灯率 | number |
| `goodRate` | 良品率 | number |
| `oeeRate` | OEE | number |
| `unitPrice` | 件工费 | number |
| `amount` | 金额 | number |
| `operationCount` | 作业人数 | integer(int32) |
| `workorderPlanQty` | 工单数量 | number |
| `actualMoldCavity` | 实际使用模穴 | number |
| `singleTripQty` | 标准取数 | number |
| `actualSingleTripQty` | 实际取数 | number |
| `singleTripQtyRate` | 取出率 | number |
| `moldCavityRate` | 模穴率 | number |
| `singleTripTime` | 标准单趟加工时长 | number |
| `actualSingleTripTime` | 实际单趟加工时长 | number |
| `workcenterNo` | 工作中心编码 | string |
| `workcenterName` | 工作中心名称 | string |
| `conversionCoefficient` | 转换系数 | number |
| `shiftCapacity` | 当班标准产能 | number |
| `startMouldTime` | 开始换模时刻 | string(date-time) |
| `endMouldTime` | 结束换模时刻 | string(date-time) |
| `planFollowWordNo` | 计划跟踪号 | string |
| `materialLedgerDesc` | 材料名称 | string |
| `materialLedgerSpec` | 材料规格 | string |
| `auxiliaryUnit` | 辅助单位 | string |
| `auxiliaryQty` | 辅助单位数量 | number |
| `coefficient` | 主辅单位系数 | string |
| `supplier` | 供应商 | string |
| `orderQty` | 订单数量 | number |
| `salesorderNo` | 销单号 | string |
| `manOutputRate` | 人工产出达成率 | number |
| `approveStatus` | 审批状态 | string |
| `actualPeopleHours` | 实际人工用时 | number |
| `compensateWorkHours` | 补偿工时 | number |
| `compensateNotes` | 补偿工时原因 | string |
| `actualSingleOutputTime` | 实际单趟产出时长 | number |
| `customizationNo` | 客制代码 | string |
| `customerRequirement` | 客户定制说明 | string |
| `userName` | 报工人员 | string |
| `materialLedgerWeight` | 材料重量 | number |
| `procedureRemark` | 工序备注 | string |
| `theoreticalScrapWeight` | 理论角料重量 | number |
| `utilizationRate` | 产品利用率 | number |
| `workorderRemark` | 工单备注 | string |
| `checkQty` | 检查数量 | number |
| `transferCardNo` | 流转卡号 | string |
| `totalCompleteQty` | 总完成数 | number |
| `auxiliaryReport` | 是否以辅助单位报工 0否 1是 | integer(int32) |
| `secondCoefficient` | 辅助单位系数 | number |
| `mainCoefficient` | 主单位系数 | number |
| `planWorkTime` | 计划用时 | number |
| `boxQty` | 箱数 | number |
| `errorRemark` | 异常备注 | string |
| `mainBadQty` | 主单位不良数 | number |
| `secondBadQty` | 辅助单位不良数 | number |
| `hasMedia` | 照片/视频标识筛选 | string |
| `chassisNo` | 底盘号/盘底号 | string |
| `rearOutriggerCode` | 后支腿编码 | string |
| `outputRate` | 产出率 | number |
| `auxiliaryMetering` | 辅助计量 | number |
| `productSpecificationQtyVOS` | 品规数量 | array ProductSpecificationQtyVO |
| `--productSpecificationQtyVOS[].completeQty` | 累计报工数量 | number |
| `--productSpecificationQtyVOS[].goodQty` | 当前报工数量 | number |
| `--productSpecificationQtyVOS[].planQty` | 计划数 | number |
| `--productSpecificationQtyVOS[].psqId` | 品规id | integer(int64) |
| `--productSpecificationQtyVOS[].specificationNo` | 品规编号 | string |

---

## 9. 安灯报表

### 基本信息

| 项目 | 内容 |
| --- | --- |
| 接口地址 | `/lightmesapi/open/trilightSummary/andonApiController` |
| 请求方式 | **POST** |
| 接口描述 | 通过此接口可以查询指定时间内的安灯情况。单个客户账号调用该接口的每秒请求数（QPS）最大限制为10。 |

### 请求参数

| 参数名称 | 参数说明 | 是否必须 | 数据类型 |
| --- | --- | --- | --- |
| `pageNum` | 查询页 | true | integer(int32) |
| `pageSize` | 每页条数 | true | integer(int32) |
| `did` | 部门did | false | integer(int64) |
| `didList` | 部门id集合 | false | array[integer(int64)] |
| `pidList` | 产线id | false | array[integer(int64)] |
| `startDate` | 开始时间 | true | string(date-time) |
| `endDate` | 结束时间 | true | string(date-time) |
| `workorderNo` | 工单号 | false | string |
| `materialNo` | 料号/产品编码 | false | string |
| `materialDesc` | 品名 | false | string |
| `materialSpec` | 规格 | false | string |
| `procedureNo` | 工序编号 | false | string |
| `procedureName` | 工序名称 | false | string |
| `taskNo` | 生产任务号 | false | string |
| `ngReason` | 不良原因 | false | string |
| `query` | 搜索输入内容 | false | string |
| `startTime` | 要求开工日期开始时间 | false | string(date-time) |
| `endTime` | 要求开工日期结束时间 | false | string(date-time) |
| `mid` | 设备id | false | integer(int64) |
| `userName` | 人员姓名 | false | string |
| `machineNo` | 设备编号 | false | string |
| `andonTitle` | 安灯类型 | false | string |
| `statusList` | 状态 0未完成 1已完成 | true | array[integer(int32)] |

### 响应数据字段

| 字段名称 | 字段说明 | 数据类型 |
| --- | --- | --- |
| `arId` | 安灯主键id | integer(int64) |
| `machineNo` | 设备编号 | string |
| `createDate` | 发生时间 | string(date-time) |
| `andonTitle` | 安灯类型 | string |
| `receiveDate` | 响应时间 | string(date-time) |
| `receiveTime` | 响应时长 | number |
| `finishDate` | 处理完成时间 | string(date-time) |
| `finishTime` | 处理时长 | number |
| `allTime` | 总时长 | number |
| `submitName` | 发起人 | string |
| `finishName` | 关闭人 | string |
| `mesExplain` | 处理结果备注 | string |
| `remark` | 其它备注 | string |
| `mesUrl` | 处理结果图片/视频 | string |
| `urlType` | 上传文件类型（1图片 2视频） | integer(int32) |
| `note` | 补充说明 | string |
| `noteUrl` | 补充图片/视频 | string |
| `noteType` | 补充文件类型 | integer(int32) |
| `userNames` | 处理人姓名 | array[string] |
| `taskRemark` | 工单备注 | string |
| `andonStatus` | 请求状态：1创建等待接手 2接手人员接手 3接手人完成 | integer(int32) |
| `standardDuration` | 标准安灯时长 | number |
| `standardResponseTime` | 标准响应时长 | number |
| `standardProcessingTime` | 标准处理时长 | number |
| `responseTimeout` | 响应超时 | number |
| `processingTimeout` | 处理超时 | number |
| `canPrintOa` | 是否可以打印OA流 0否 1是 | integer(int32) |

---

## 10. 获取三色灯指定时间段内的脉冲计数详情

### 基本信息

| 项目 | 内容 |
| --- | --- |
| 接口地址 | `/lightmesapi/open/trilightSummary/getTimecountMessagesByTimeSim` |
| 请求方式 | **POST** |
| 接口描述 | 通过此接口可以获取指定三色灯指定时间段内的脉冲计数详情。 |

### 请求参数

| 参数名称 | 参数说明 | 是否必须 | 数据类型 |
| --- | --- | --- | --- |
| `sim` | 三色灯sim号 | true | string |
| `startTime` | 查询开始时间yyyy-MM-dd HH:mm:ss | true | string(date-time) |
| `endTime` | 查询结束时间yyyy-MM-dd HH:mm:ss | true | string(date-time) |
| `date` | 查询的指定日期格式(yyyy-MM-dd) | false | string(date-time) |

### 响应数据字段

| 字段名称 | 字段说明 | 数据类型 |
| --- | --- | --- |
| `sim` | SIM卡 | string |
| `countMessages` | 三色灯计数详情 | array CountMessage |
| `--countMessages[].count` | 计数详细，该List有10条数据，每条代表三秒内的计数总和 | array[integer] |
| `--countMessages[].duration` | 脉冲计数持续时间 | integer(int64) |
| `--countMessages[].endtime` | 当前脉冲计数结束时间戳 | integer(int64) |
| `--countMessages[].sno` | 三色灯序号 | integer(int32) |

---

## 11. 获取三色灯指定时间段内的脉冲计数之和

### 基本信息

| 项目 | 内容 |
| --- | --- |
| 接口地址 | `/lightmesapi/open/trilightSummary/getTrilightCountByTimeSim` |
| 请求方式 | **POST** |
| 接口描述 | 通过此接口可以获取指定三色灯指定时间段内的脉冲计数之和。 |

### 请求参数

| 参数名称 | 参数说明 | 是否必须 | 数据类型 |
| --- | --- | --- | --- |
| `sim` | 三色灯sim号 | true | string |
| `startTime` | 查询开始时间yyyy-MM-dd HH:mm:ss | true | string(date-time) |
| `endTime` | 查询结束时间yyyy-MM-dd HH:mm:ss | true | string(date-time) |
| `date` | 查询的指定日期格式(yyyy-MM-dd) | false | string(date-time) |

### 响应数据字段

| 字段名称 | 字段说明 | 数据类型 |
| --- | --- | --- |
| `sim` | SIM卡 | string |
| `countSize` | 三色灯计数次数 | integer(int64) |

---

## 12. 通过sim卡号查询对应三色灯状态

### 基本信息

| 项目 | 内容 |
| --- | --- |
| 接口地址 | `/lightmesapi/open/trilightSummary/getTrilightCurrentColor` |
| 请求方式 | **POST** |
| 接口描述 | 通过sim卡号查询对应三色灯状态。单个客户账号调用该接口的每秒请求数（QPS）最大限制为10。 |

### 请求参数

| 参数名称 | 参数说明 | 是否必须 | 数据类型 |
| --- | --- | --- | --- |
| `sim` | 三色灯sim | true | string |

### 响应数据字段

| 字段名称 | 字段说明 | 数据类型 |
| --- | --- | --- |
| `sim` | 当前sim卡号 | string |
| `currentState` | 三色灯状态码：001-绿灯 010-黄灯 100-红灯 000-关灯 | string |
| `updateDate` | 上次状态修改时间 | string(date-time) |
| `onLineStatus` | 当前是否在线 | boolean |

---

## 13. 批量获取三色灯状态

### 基本信息

| 项目 | 内容 |
| --- | --- |
| 接口地址 | `/lightmesapi/open/trilightSummary/getTrilightCurrentColorList` |
| 请求方式 | **POST** |
| 接口描述 | 通过sim卡号集合批量获取三色灯状态。单个客户账号调用该接口的每秒请求数（QPS）最大限制为10。 |

### 请求参数

| 参数名称 | 参数说明 | 是否必须 | 数据类型 |
| --- | --- | --- | --- |
| `simList` | 三色灯sim号 | true | array[string] |

### 响应数据字段

| 字段名称 | 字段说明 | 数据类型 |
| --- | --- | --- |
| `sim` | 当前sim卡号 | string |
| `currentState` | 三色灯状态码：001-绿灯 010-黄灯 100-红灯 000-关灯 | string |
| `updateDate` | 上次状态修改时间 | string(date-time) |
| `onLineStatus` | 当前是否在线 | boolean |

---

## 14. 三色灯指定时间段颜色汇总

### 基本信息

| 项目 | 内容 |
| --- | --- |
| 接口地址 | `/lightmesapi/open/trilightSummary/getTrilightEfficiencyDurationTime` |
| 请求方式 | **POST** |
| 接口描述 | 三色灯指定时间段颜色汇总。单个客户账号调用该接口的每秒请求数（QPS）最大限制为10。 |

### 请求参数

| 参数名称 | 参数说明 | 是否必须 | 数据类型 |
| --- | --- | --- | --- |
| `sim` | 三色灯sim号 | true | string |
| `startTime` | 查询开始时间yyyy-MM-dd HH:mm:ss | true | string(date-time) |
| `endTime` | 查询结束时间yyyy-MM-dd HH:mm:ss | true | string(date-time) |
| `date` | 查询的指定日期格式(yyyy-MM-dd) | false | string(date-time) |

### 响应数据字段

| 字段名称 | 字段说明 | 数据类型 |
| --- | --- | --- |
| `sim` | 设备主键 | string |
| `redTime` | 红灯时长,单位为秒 | integer(int64) |
| `greenTime` | 绿灯时长,单位为秒 | integer(int64) |
| `yellowTime` | 黄灯时长,单位为秒 | integer(int64) |
| `closeTime` | 关灯时长,单位为秒 | integer(int64) |

---

## 15. 指定日期一天颜色汇总

### 基本信息

| 项目 | 内容 |
| --- | --- |
| 接口地址 | `/lightmesapi/open/trilightSummary/getTrilightEfficiencyOneDay` |
| 请求方式 | **POST** |
| 接口描述 | 查询某一天指定三色灯的颜色变化信息。单个客户账号调用该接口的每秒请求数（QPS）最大限制为10。 |

### 请求参数

| 参数名称 | 参数说明 | 是否必须 | 数据类型 |
| --- | --- | --- | --- |
| `sim` | 三色灯sim号 | true | string |
| `startTime` | 查询开始时间yyyy-MM-dd HH:mm:ss | false | string(date-time) |
| `endTime` | 查询结束时间yyyy-MM-dd HH:mm:ss | false | string(date-time) |
| `date` | 查询的指定日期格式(yyyy-MM-dd) | true | string(date-time) |

### 响应数据字段

| 字段名称 | 字段说明 | 数据类型 |
| --- | --- | --- |
| `sim` | 设备主键 | string |
| `redTime` | 红灯时长,单位为秒 | integer(int64) |
| `greenTime` | 绿灯时长,单位为秒 | integer(int64) |
| `yellowTime` | 黄灯时长,单位为秒 | integer(int64) |
| `closeTime` | 关灯时长,单位为秒 | integer(int64) |

---

## 16. 查询指定时间段三色灯的颜色变化信息

### 基本信息

| 项目 | 内容 |
| --- | --- |
| 接口地址 | `/lightmesapi/open/trilightSummary/getTrilightSummaryDurationTime` |
| 请求方式 | **POST** |
| 接口描述 | 查询某一天指定三色灯的颜色变化信息。单个客户账号调用该接口的每秒请求数（QPS）最大限制为10。 |

### 请求参数

| 参数名称 | 参数说明 | 是否必须 | 数据类型 |
| --- | --- | --- | --- |
| `sim` | 三色灯sim号 | true | string |
| `startTime` | 查询开始时间yyyy-MM-dd HH:mm:ss | true | string(date-time) |
| `endTime` | 查询结束时间yyyy-MM-dd HH:mm:ss | true | string(date-time) |

### 响应数据字段

| 字段名称 | 字段说明 | 数据类型 |
| --- | --- | --- |
| `startTime` | 当前三色灯状态开始时间 | string(date-time) |
| `endTime` | 当前三色灯状态结束时间 | string(date-time) |
| `color` | 三色灯状态码：001-绿灯 010-黄灯 100-红灯 000-关灯 | string |

---

## 17. 设备OEE报表

### 基本信息

| 项目 | 内容 |
| --- | --- |
| 接口地址 | `/lightmesapi/open/trilightSummary/selectOeeReport` |
| 请求方式 | **POST** |
| 接口描述 | 通过此接口可以查询对应团队指定时间段的设备OEE信息。单个客户账号调用该接口的每秒请求数（QPS）最大限制为10。 |

### 请求参数

| 参数名称 | 参数说明 | 是否必须 | 数据类型 |
| --- | --- | --- | --- |
| `pageNum` | 查询页 | true | integer(int32) |
| `pageSize` | 每页条数 | true | integer(int32) |
| `startDate` | 日期（yyyy-MM-dd） | true | string |
| `endDate` | 日期（yyyy-MM-dd） | true | string |
| `shiftName` | 班次名称（不填查询所有班次） | false | string |

### 响应数据字段

| 字段名称 | 字段说明 | 数据类型 |
| --- | --- | --- |
| `mid` | 设备id | integer(int64) |
| `departmentName` | 车间/产线 | string |
| `machineNo` | 设备编号 | string |
| `machineName` | 设备名称 | string |
| `simDate` | 记录日期 | string(date-time) |
| `shiftName` | 班次名称 | string |
| `startTime` | 班次上班时间 | string(date-time) |
| `endTime` | 班次下班时间 | string(date-time) |
| `redTime` | 红灯时长,单位为小时 | number |
| `greenTime` | 绿灯时长,单位为小时 | number |
| `yellowTime` | 黄灯时长,单位为小时 | number |
| `closeTime` | 关灯时长,单位为小时 | number |
| `greenTotalTime` | 总绿灯时长,单位小时 | number |
| `redRate` | 红灯率 | number |
| `greenRate` | 绿灯率 | number |
| `yellowRate` | 黄灯率 | number |
| `closeRate` | 关灯率 | number |
| `userName` | 当班人员 | string |
| `greenCompensation` | 绿灯补偿 | number |
| `waitCount` | 等待次数 | integer(int64) |
| `faultCount` | 故障次数 | integer(int64) |
| `actualRate` | 实动率 | number |
| `goodQty` | 报工数量 | number |
| `effectiveYellowTime` | 有效黄灯,单位小时 | number |
| `effectiveGreenRate` | 有效绿灯率 | number |
| `actualYellowRate` | 实际黄灯率 | number |
| `performanceRate` | 设备性能表现指数 | number |
| `oeeRate` | 设备性能表现OEE | number |
| `stopTime` | 停用时长,单位小时 | number |
| `stopGreen` | 停用绿灯时长 | number |
| `stopFree` | 停用休息时长 | number |
| `runOeeRate` | 设备运行OEE | number |
| `standardRate` | 标准利用率 | number |
| `andonTime` | 装夹时长,单位小时 | number |
| `andonRate` | 装夹率 | number |
| `redHour` | 红灯时长(广濑) | number |
| `greenHour` | 绿灯时长(广濑) | number |
| `yellowHour` | 黄灯时长(广濑) | number |
| `closeHour` | 关灯时长(广濑) | number |
| `greenTotalHour` | 总绿灯时长(广濑) | number |
| `greenCompensationHour` | 绿灯补偿(广濑) | number |
| `effectiveYellowHour` | 有效黄灯(广濑) | number |
| `stopHour` | 停用时长(广濑) | number |
| `andonHour` | 装夹时长(广濑) | number |
| `onlineTime` | 在线时间 | number |
| `shiftGreenRate` | 班次绿灯率 | number |
| `shiftGreenTime` | 班次绿灯时长 | number |

---

## 18. 查询团队下设备数量

### 基本信息

| 项目 | 内容 |
| --- | --- |
| 接口地址 | `/lightmesapi/open/machine/getMachineCount` |
| 请求方式 | **POST** |
| 接口描述 | 查询团队下设备的数量。单个客户账号调用该接口的每秒请求数（QPS）最大限制为10。 |

### 请求参数

| 参数名称 | 参数说明 | 是否必须 | 数据类型 |
| --- | --- | --- | --- |
| `tid` | 团队id | false | integer(int64) |
| `machineNo` | 设备编码 | false | string |
| `machineName` | 设备名称 | false | string |

### 响应数据字段

| 字段名称 | 字段说明 | 数据类型 |
| --- | --- | --- |
| `data` | 设备数量（直接返回整数） | integer(int32) |

---

## 19. 通过mid或者sim查询设备详情

### 基本信息

| 项目 | 内容 |
| --- | --- |
| 接口地址 | `/lightmesapi/open/machine/getMachineDetailById` |
| 请求方式 | **POST** |
| 接口描述 | 通过此接口可以通过设备的mid查询设备的详情，或者通过三色灯sim查询绑定的设备详情。单个客户账号调用该接口的每秒请求数（QPS）最大限制为10。 |

### 请求参数

| 参数名称 | 参数说明 | 是否必须 | 数据类型 |
| --- | --- | --- | --- |
| `tid` | 团队id | false | integer(int64) |
| `mid` | 设备id（与sim任选一个查询） | true | integer(int64) |
| `sim` | 三色灯sim号（与mid任选一个查询） | true | string |

### 响应数据字段

| 字段名称 | 字段说明 | 数据类型 |
| --- | --- | --- |
| `mid` | 设备主键 | integer(int64) |
| `machineNo` | 设备编码 | string |
| `machineName` | 设备名称 | string |
| `sim` | 三色灯sim | string |
| `status` | 设备状态,1表示启用，0表示未启用 | integer(int32) |
| `machineBrand` | 设备品牌 | string |
| `machineModel` | 设备型号 | string |
| `machineFunction` | 概要 | string |
| `machineImage` | 设备图片 | string |
| `serialNumber` | 序列号 | string |
| `fixedAssetsCode` | 固定资产编码 | string |
| `supplier` | 供应商 | string |
| `manufacturer` | 制造商 | string |
| `productionDate` | 出厂日期 | string(date-time) |
| `receiveDate` | 安装验收日期 | string(date-time) |
| `firstDate` | 启用日期 | string(date-time) |
| `documents` | 设备档案 | string |
| `useTime` | 使用时间 | string |
| `departmentName` | 车间/产线 | string |

---

## 20. 查询团队下的设备信息

### 基本信息

| 项目 | 内容 |
| --- | --- |
| 接口地址 | `/lightmesapi/open/machine/getMachineList` |
| 请求方式 | **POST** |
| 接口描述 | 批量查询团队下设备信息。单个客户账号调用该接口的每秒请求数（QPS）最大限制为10。 |

### 请求参数

| 参数名称 | 参数说明 | 是否必须 | 数据类型 |
| --- | --- | --- | --- |
| `pageNum` | 查询页 | true | integer(int32) |
| `pageSize` | 每页条数 | true | integer(int32) |
| `tid` | 团队id | false | integer(int64) |
| `machineNo` | 设备编码 | false | string |
| `machineName` | 设备名称 | false | string |

### 响应数据字段

| 字段名称 | 字段说明 | 数据类型 |
| --- | --- | --- |
| `mid` | 设备主键 | integer(int64) |
| `machineNo` | 设备编码 | string |
| `machineName` | 设备名称 | string |
| `sim` | 三色灯sim | string |
| `status` | 设备状态,1表示启用，0表示未启用 | integer(int32) |
| `departmentName` | 车间/产线 | string |

---

## 21. 查询自定义字段定义列表

### 基本信息

| 项目 | 内容 |
| --- | --- |
| 接口地址 | `/lightmesapi/open/entityCustomFieldDefController/listDefs` |
| 请求方式 | **POST** |
| 接口描述 | 通过此接口可查询指定实体类型下的自定义字段定义列表。实体类型可选值：WORKORDER（工单）、WORKORDER_PROCEDURE（工单工序）。单个客户账号调用该接口的每秒请求数（QPS）最大限制为10。 |

### 请求参数

| 参数名称 | 参数说明 | 是否必须 | 数据类型 |
| --- | --- | --- | --- |
| `entityType` | 实体类型，如 WORKORDER | true | string |
| `enabledOnly` | 仅启用 1是 0否 | false | integer(int32) |
| `required` | 必填 1是 0否 | false | integer(int32) |

### 响应数据字段

| 字段名称 | 字段说明 | 数据类型 |
| --- | --- | --- |
| `ecfdId` | 自定义字段主键 | integer(int64) |
| `entityType` | 实体类型，如 WORKORDER | string |
| `webId` | 列表列配置 web_id | integer(int64) |
| `fieldCode` | 字段编码（如 wo_cf_1） | string |
| `fieldLabel` | 显示名称 | string |
| `fieldType` | 字段类型 | string |
| `required` | 是否必填 0否 1是 | integer(int32) |
| `sortNo` | 排序序号 | integer(int32) |
| `maxLength` | 字段最大长度 | integer(int32) |
| `optionsJson` | 扩展配置（如枚举项 JSON 数组） | string |
| `enabled` | 是否启用 0否 1是 | integer(int32) |

---

## 22. 仅查询可选、启用自定义字段列表

### 基本信息

| 项目 | 内容 |
| --- | --- |
| 接口地址 | `/lightmesapi/open/entityCustomFieldDefController/listOptionalCustomFieldCodes` |
| 请求方式 | **POST** |
| 接口描述 | 返回非必填且已启用的自定义字段编码与显示名，常用于导入等场景。实体类型可选值：WORKORDER（工单）、WORKORDER_PROCEDURE（工单工序）。单个客户账号调用该接口的每秒请求数（QPS）最大限制为10。 |

### 请求参数

| 参数名称 | 参数说明 | 是否必须 | 数据类型 |
| --- | --- | --- | --- |
| `entityType` | 实体类型，如 WORKORDER | true | string |
| `enabledOnly` | 仅启用 1是 0否 | false | integer(int32) |
| `required` | 必填 1是 0否 | false | integer(int32) |

### 响应数据字段

| 字段名称 | 字段说明 | 数据类型 |
| --- | --- | --- |
| `fieldCode` | 字段英文名/编码 | string |
| `fieldLabel` | 字段中文显示名 | string |

---

## 23. 物料查询

### 基本信息

| 项目 | 内容 |
| --- | --- |
| 接口地址 | `/lightmesapi/open/material/queryCraftHours` |
| 请求方式 | **POST** |
| 接口描述 | 通过此接口可以查询对应团队所有的物料简要信息，查询结果为一个物料列表集合，按创建日期倒序。单个客户账号调用该接口的每秒请求数（QPS）最大限制为10。 |

### 请求参数

| 参数名称 | 参数说明 | 是否必须 | 数据类型 |
| --- | --- | --- | --- |
| `pageNum` | 查询页 | true | integer(int32) |
| `pageSize` | 每页条数 | true | integer(int32) |
| `materialDescOrNo` | 物料描述或者物料编号用于模糊查询 | false | string |
| `startTime` | 模糊查询起始时间 | false | string(date-time) |
| `endTime` | 模糊查询结束时间 | false | string(date-time) |
| `combination` | 是否是组合物料 0非组合 1组合 | false | integer(int32) |
| `confirm` | 物料是否确认 0待确认 1已确认 | false | integer(int32) |
| `procedureName` | 工序 | false | string |
| `materialNo` | 物料编号模糊查询 | false | string |
| `materialDesc` | 物料描述模糊查询 | false | string |
| `materialSpec` | 物料规格模糊查询 | false | string |
| `materialNature` | 产品性质 0成品 1半成品 | false | integer(int32) |

### 响应数据字段

| 字段名称 | 字段说明 | 数据类型 |
| --- | --- | --- |
| `mtid` | 物料主键 | integer(int64) |
| `materialNo` | 物料编码 | string |
| `materialDesc` | 物料描述 | string |
| `materialSpec` | 规格 | string |
| `unit` | 单位 | string |
| `auxiliaryUnit` | 辅助单位 | string |
| `conversionCoefficient` | 转换系数 | number |
| `createTime` | 创建日期 | string(date-time) |
| `updateTime` | 修改日期 | string(date-time) |
| `updateUserName` | 修改人 | string |
| `createUserName` | 创建人 | string |
| `procedureName` | 工序名称 | array[string] |
| `materialNature` | 产品性质 0成品 1半成品 | integer(int32) |
| `confirm` | 物料是否确认 0待确认 1已确认 | integer(int32) |
| `materialLedgerDesc` | 材料名称 | string |
| `materialLedgerSpec` | 材料规格 | string |
| `updateQty` | 修改次数 | integer(int32) |
| `ganttColor` | 甘特图颜色 | string |
| `bindSop` | 绑定SOP 0否 1是 | integer(int32) |
| `bindFirstInspectScheme` | 绑定首检方案 0否 1是 | integer(int32) |
| `bindSelfInspectScheme` | 绑定巡检方案 0否 1是 | integer(int32) |
| `bindFinalInspectScheme` | 绑定末检方案 0否 1是 | integer(int32) |
| `bindProcessSupervisionScheme` | 绑定工艺监督方案 0否 1是 | integer(int32) |

---

## 24. 物料查询详情

### 基本信息

| 项目 | 内容 |
| --- | --- |
| 接口地址 | `/lightmesapi/open/material/queryCraftHoursDetails` |
| 请求方式 | **POST** |
| 接口描述 | 通过此接口可以查询物料的详细信息，包含物料下的工艺路线、工序以及工时参数等等。单个客户账号调用该接口的每秒请求数（QPS）最大限制为10。 |

### 请求参数

| 参数名称 | 参数说明 | 是否必须 | 数据类型 |
| --- | --- | --- | --- |
| `mtid` | 物料id | true | integer(int64) |
| `tid` | 团队id | false | integer(int64) |

### 响应数据字段

| 字段名称 | 字段说明 | 数据类型 |
| --- | --- | --- |
| `rid` | 路线主键 | integer(int64) |
| `materialNo` | 物料编码 | string |
| `materialDesc` | 物料描述 | string |
| `materialSpec` | 规格 | string |
| `unit` | 单位 | string |
| `materialLedgerDesc` | 材料名称 | string |
| `materialLedgerSpec` | 材料规格 | string |
| `materialLedgerBrand` | 材料品牌 | string |
| `remark` | 备注 | string |
| `conversionCoefficient` | 转化系数 | number |
| `auxiliaryUnit` | 辅助单位 | string |
| `materialWeight` | 产品单重 | number |
| `materialPrice` | 产品单价 | number |
| `routingsName` | 物料工艺路线名称 | string |
| `customizationNo` | 客制代码 | string |
| `customizationName` | 客制产品名称 | string |
| `customerRequirement` | 客户定制说明 | string |
| `completiongStatge` | 工单进度标识索引位置 | integer(int32) |
| `fileUrl` | 产品图片 | string |
| `ganttColor` | 甘特图颜色 | string |
| `utilizationRate` | 产品利用率 | number |
| `customerMaterialNo` | 客户料号 | string |
| `materialNature` | 产品性质 0成品 1半成品 | integer(int32) |
| `sopPathList` | sop路径集合 | array[string] |
| `psfId` | 产品系列系数id | integer(int64) |
| `seriesName` | 系列名称 | string |
| `seriesCode` | 系列系数代码 | string |
| `routingsProcedureMsgList` | 工序列表 | array RoutingsProcedureMsg |
| `--routingsProcedureMsgList[].component` | 子件 | string |
| `--routingsProcedureMsgList[].difficultyRate` | 难度系数 | number |
| `--routingsProcedureMsgList[].mould` | 模具 | string |
| `--routingsProcedureMsgList[].procedureName` | 工序名称 | string |
| `--routingsProcedureMsgList[].procedureNo` | 工序编号 | string |
| `--routingsProcedureMsgList[].procedureOrder` | 位置 | integer(int32) |
| `--routingsProcedureMsgList[].remark` | 备注 | string |
| `--routingsProcedureMsgList[].rpid` | 工序主键 | integer(int64) |
| `--routingsProcedureMsgList[].unitPrice` | 计件单价 | number |

---

## 25. 异常上报记录列表

### 基本信息

| 项目 | 内容 |
| --- | --- |
| 接口地址 | `/lightmesapi/open/errorReportAPIController/selectErrorReport` |
| 请求方式 | **POST** |
| 接口描述 | 查询异常上报记录列表。 |

### 请求参数

| 参数名称 | 参数说明 | 是否必须 | 数据类型 |
| --- | --- | --- | --- |
| `pageNum` | 页面 | true | integer(int32) |
| `pageSize` | 每页大小 | true | integer(int32) |
| `date` | 日期(yyyy-MM-dd HH:mm:ss) | true | string |
| `shiftName` | 班次名称(不填查询所有班次) | false | string |

### 响应数据字段

| 字段名称 | 字段说明 | 数据类型 |
| --- | --- | --- |
| `lwlId` | 异常列表Id | integer(int64) |
| `mid` | 设备主键 | integer(int64) |
| `machineNo` | 设备编号 | string |
| `machineName` | 设备名称 | string |
| `machineStatusName` | 设备状态 | string |
| `workDate` | 日期 | string(date-time) |
| `shiftName` | 班次名称 | string |
| `shiftStartDate` | 班次开始日期 | string(date-time) |
| `shiftEndDate` | 班次结束日期 | string(date-time) |
| `color` | 灯的颜色 | string |
| `reasonCode` | 异常代码 | string |
| `waitReason` | 异常原因 | string |
| `reasonClassification` | 异常原因分类 | string |
| `waitStartTime` | 开始时间 | string(date-time) |
| `waitEndTime` | 结束时间 | string(date-time) |
| `duration` | 持续时长 | number |
| `workorderNo` | 工单号 | string |
| `materialNo` | 物料号 | string |
| `userName` | 备注人员姓名 | string |
| `picUrls` | 图片地址 | array[string] |
| `description` | 异常说明 | string |
| `openUserName` | 开机人员 | string |
| `updateTime` | 上报时间 | string(date-time) |
