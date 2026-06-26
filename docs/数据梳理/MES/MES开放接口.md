# 开放API文档


**简介**:开放API文档


**HOST**:https://a.lightmes.cn/lightmesapi


**联系人**:RD@Lightmes


**Version**:1.0


**接口路径**:/lightmesapi/v3/api-docs/开放接口


[TOC]






# 工单相关操作文档


## 删除工单


**接口地址**:`/lightmesapi/open/workorderController/deleteWorkorderByNo`


**请求方式**:`POST`


**请求数据类型**:`application/x-www-form-urlencoded,application/json`


**响应数据类型**:`*/*`


**接口描述**:<p>通过此接口可以删除单个工单或者批量删除多个工单，删除工单会同时删除掉工单对应的工序和生产任务，如果工单已经有加工中或完成的生产任务，则不允许删除;
    单个客户账号调用该接口的每秒请求数（QPS）最大限制为10。</p>



**请求示例**:


```javascript
{
  "workorderNos": [],
  "tid": 0
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|AccessKeyId|AccessKeyId|header|true|string||
|AccessKeySecret|AccessKeySecret|header|true|string||
|workorderNosDTO|WorkorderNosDTO|body|true|WorkorderNosDTO|WorkorderNosDTO|
|&emsp;&emsp;workorderNos|工单编号集合||false|array|string|
|&emsp;&emsp;tid|||false|integer(int64)||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|ResultDataApiReturnVO|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|success|成功与否|boolean||
|code|状态码|integer(int32)|integer(int32)|
|message|消息|string||
|data||ApiReturnVO|ApiReturnVO|
|&emsp;&emsp;successTotal|成功的条数|integer(int32)||
|&emsp;&emsp;errorTotal|失败的条数|integer(int32)||
|&emsp;&emsp;errorList|失败的错误信息|array|string|


**响应示例**:
```javascript
{
	"success": true,
	"code": 1000,
	"message": "success",
	"data": {
		"successTotal": 0,
		"errorTotal": 0,
		"errorList": []
	}
}
```


## 出库单删除


**接口地址**:`/lightmesapi/open/workorderController/erpGoodsTakeOutDelete`


**请求方式**:`POST`


**请求数据类型**:`application/x-www-form-urlencoded,application/json`


**响应数据类型**:`*/*`


**接口描述**:<p>通过此接口可以根据计划跟踪号和出库单号删除出库单数据。
    单个客户账号调用该接口的每秒请求数（QPS）最大限制为10</p>



**请求示例**:


```javascript
{
  "planFollowWordNo": "",
  "salesorderTakeOutNo": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|AccessKeyId|AccessKeyId|header|true|string||
|AccessKeySecret|AccessKeySecret|header|true|string||
|ordersDeletedDTO|OrdersDeletedDTO|body|true|OrdersDeletedDTO|OrdersDeletedDTO|
|&emsp;&emsp;planFollowWordNo|计划跟踪号||true|string||
|&emsp;&emsp;salesorderTakeOutNo|销售出库单单号||true|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|出参|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|success|成功与否|boolean||
|code|状态码|integer(int32)|integer(int32)|
|message|消息|string||


**响应示例**:
```javascript
{
	"success": true,
	"code": 1000,
	"message": "success"
}
```


## 出库单导入


**接口地址**:`/lightmesapi/open/workorderController/erpGoodsTakeOutInsert`


**请求方式**:`POST`


**请求数据类型**:`application/x-www-form-urlencoded,application/json`


**响应数据类型**:`*/*`


**接口描述**:<p>通过此接口可以导入出库单数据。
    单个客户账号调用该接口的每秒请求数（QPS）最大限制为10</p>



**请求示例**:


```javascript
{
  "planFollowWordNo": "",
  "salesorderTakeOutNo": "",
  "goodsTakeOutTime": "",
  "outQty": 0
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|AccessKeyId|AccessKeyId|header|true|string||
|AccessKeySecret|AccessKeySecret|header|true|string||
|erpGoodsTakeOutDTO|ErpGoodsTakeOutDTO|body|true|ErpGoodsTakeOutDTO|ErpGoodsTakeOutDTO|
|&emsp;&emsp;planFollowWordNo|计划跟踪号||true|string||
|&emsp;&emsp;salesorderTakeOutNo|销售出库单单号||true|string||
|&emsp;&emsp;goodsTakeOutTime|出库日期,格式(yyyy-MM-dd)||true|string(date-time)||
|&emsp;&emsp;outQty|出库数据量||true|number||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|出参|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|success|成功与否|boolean||
|code|状态码|integer(int32)|integer(int32)|
|message|消息|string||


**响应示例**:
```javascript
{
	"success": true,
	"code": 1000,
	"message": "success"
}
```


## 工单查询


**接口地址**:`/lightmesapi/open/workorderController/filterWorkorder`


**请求方式**:`POST`


**请求数据类型**:`application/x-www-form-urlencoded,application/json`


**响应数据类型**:`*/*`


**接口描述**:<p>通过此接口可以查询对应团队的所有工单，查询结果为一个工单列表集合，默认按工单创建时间倒序排列；
   单个客户账号调用该接口的每秒请求数（QPS）最大限制为10。</p>



**请求示例**:


```javascript
{
  "pageNum": 0,
  "pageSize": 0,
  "startDate": "",
  "endDate": "",
  "requireStartDate": "",
  "requireEndDate": "",
  "workOrderStatus": [],
  "workorderNo": "",
  "materialNo": "",
  "materialDesc": "",
  "materialSpec": "",
  "workorderType": "",
  "material": "",
  "planFollowWordNo": "",
  "orderMaster": "",
  "customerRequirement": "",
  "remark": "",
  "urgentLevelList": [],
  "customerRequirementNotNull": 0,
  "remarkNotNull": 0,
  "orderByDTOS": [
    {
      "orderName": "",
      "sort": "",
      "grade": 0
    }
  ],
  "customizationNo": "",
  "sales": "",
  "customerNo": "",
  "query": "",
  "appQuery": "",
  "startTime": "",
  "endTime": "",
  "startCreateTime": "",
  "endCreateTime": "",
  "minPlanQty": 0,
  "maxPlanQty": 0,
  "minOrderQty": 0,
  "maxOrderQty": 0,
  "actualStartTime": "",
  "actualEndTime": "",
  "customerNoNotNull": 0,
  "statusList": [],
  "salesorderNo": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|AccessKeyId|AccessKeyId|header|true|string||
|AccessKeySecret|AccessKeySecret|header|true|string||
|filterWorkorderDTO|FilterWorkorderDTO|body|true|FilterWorkorderDTO|FilterWorkorderDTO|
|&emsp;&emsp;pageNum|查询页||true|integer(int32)||
|&emsp;&emsp;pageSize|每页条数||true|integer(int32)||
|&emsp;&emsp;startDate|开始时间||false|string(date-time)||
|&emsp;&emsp;endDate|结束时间||false|string(date-time)||
|&emsp;&emsp;requireStartDate|要求完工时间查询开始时间||false|string(date-time)||
|&emsp;&emsp;requireEndDate|要求完工时间查询结束时间||false|string(date-time)||
|&emsp;&emsp;workOrderStatus|工单状态 1待确认 2异常 3已确认(工单进度中为 1、未完成 2、已完成) 4无产品 5部分排产 6未打印||true|array|integer(int32)|
|&emsp;&emsp;workorderNo|工单号||false|string||
|&emsp;&emsp;materialNo|产品编号||false|string||
|&emsp;&emsp;materialDesc|品名||false|string||
|&emsp;&emsp;materialSpec|规格||false|string||
|&emsp;&emsp;workorderType|工单类型||false|string||
|&emsp;&emsp;material|物料编号或者物料名称或物料规格||false|string||
|&emsp;&emsp;planFollowWordNo|计划跟单号||false|string||
|&emsp;&emsp;orderMaster|跟单员姓名||false|string||
|&emsp;&emsp;customerRequirement|客户定制说明||false|string||
|&emsp;&emsp;remark|工单备注||false|string||
|&emsp;&emsp;urgentLevelList|是否加紧 1加急*/2非加急**/3加急***/0非紧急||false|array|integer(int32)|
|&emsp;&emsp;customerRequirementNotNull|特殊要求排空 0 可以为空 1 排除空||false|integer(int32)||
|&emsp;&emsp;remarkNotNull|工单备注 0 可以为空 1 排除空||false|integer(int32)||
|&emsp;&emsp;orderByDTOS|排序规则||false|array|OrderByDTO|
|&emsp;&emsp;&emsp;&emsp;orderName|排序字段||false|string||
|&emsp;&emsp;&emsp;&emsp;sort|排序规则||false|string||
|&emsp;&emsp;&emsp;&emsp;grade|等级越大,排序规则也优先||false|integer(int32)||
|&emsp;&emsp;customizationNo|客制代码||false|string||
|&emsp;&emsp;sales|业务员||false|string||
|&emsp;&emsp;customerNo|客户代码||false|string||
|&emsp;&emsp;query|搜索内容||false|string||
|&emsp;&emsp;appQuery|APP搜索内容||false|string||
|&emsp;&emsp;startTime|开工日期开始时间||false|string(date-time)||
|&emsp;&emsp;endTime|开工日期结束时间||false|string(date-time)||
|&emsp;&emsp;startCreateTime|创建时间开始时间||false|string(date-time)||
|&emsp;&emsp;endCreateTime|创建日期结束时间||false|string(date-time)||
|&emsp;&emsp;minPlanQty|工单数量最小值||false|number||
|&emsp;&emsp;maxPlanQty|工单数量最大值||false|number||
|&emsp;&emsp;minOrderQty|订单数量最小值||false|number||
|&emsp;&emsp;maxOrderQty|订单数量最大值||false|number||
|&emsp;&emsp;actualStartTime|实际完成日期开始时间||false|string(date-time)||
|&emsp;&emsp;actualEndTime|实际完成日期结束时间||false|string(date-time)||
|&emsp;&emsp;customerNoNotNull|客户代码排空 0 可以为空 1 排除空||false|integer(int32)||
|&emsp;&emsp;statusList|是否完成 0未完成 1已完成||false|array|integer(int32)|
|&emsp;&emsp;salesorderNo|销售单号||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|ResultQueryWorkorderVO|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|success|成功与否|boolean||
|code|状态码|integer(int32)|integer(int32)|
|message|消息|string||
|totalItems|总条数|integer(int32)|integer(int32)|
|data||array|WorkorderVO|
|&emsp;&emsp;woid|工单id|integer(int64)||
|&emsp;&emsp;workorderNo|工单号|string||
|&emsp;&emsp;workorderType|工单类型|string||
|&emsp;&emsp;urgentLevel|0特别加急/1非常紧急/2紧急/9非紧急|integer(int32)||
|&emsp;&emsp;mtid|物料id|integer(int64)||
|&emsp;&emsp;materialNo|料号|string||
|&emsp;&emsp;materialDesc|物料名称(品名)|string||
|&emsp;&emsp;materialSpec|规格|string||
|&emsp;&emsp;unit|单位|string||
|&emsp;&emsp;rid|工艺路线id|integer(int64)||
|&emsp;&emsp;planQty|工单数量(计划加工数量)|number||
|&emsp;&emsp;completedQty|完工数量|number||
|&emsp;&emsp;progress|完工进度|string||
|&emsp;&emsp;requireEndTime|要求完工日期|string(date-time)||
|&emsp;&emsp;createTime|创建日期|string(date-time)||
|&emsp;&emsp;startTime|预计开工日期|string(date-time)||
|&emsp;&emsp;endTime|工单交期|string(date-time)||
|&emsp;&emsp;customerNo|客户代码|string||
|&emsp;&emsp;customizationNo|客制代码|string||
|&emsp;&emsp;customerRequirement|客户定制说明|string||
|&emsp;&emsp;remark|工单备注|string||
|&emsp;&emsp;orderMaster|跟单员|string||
|&emsp;&emsp;planFollowWordNo|计划跟踪号|string||
|&emsp;&emsp;status|工单状态：1 待确认/2异常/3已确认/5部分确认/9已结产（工单进度中状态为1、未完成 2、已完成 9、已完成（结案））|integer(int32)||
|&emsp;&emsp;errorInfo|异常信息 有异常的时候有值|string||
|&emsp;&emsp;notes|排产批注|string||
|&emsp;&emsp;estimatedStartTime|预计开始日期|string(date-time)||
|&emsp;&emsp;estimatedEndTime|预计结束日期|string(date-time)||
|&emsp;&emsp;routingsMaterialNo|工艺路线参考物料编号|string||
|&emsp;&emsp;materialStatus|物料状态 0存在 1不存在 2未确认|integer(int32)||
|&emsp;&emsp;sales|业务员|string||
|&emsp;&emsp;completeProgress|进度|number||
|&emsp;&emsp;actualCompleteTime|实际完成日期|string(date-time)||
|&emsp;&emsp;overdueCount|逾期天数|integer(int64)||
|&emsp;&emsp;salesorderNo|销售单号|string||
|&emsp;&emsp;currentProcedure|当前工序|string||
|&emsp;&emsp;nextProcedure|下一道工序|string||
|&emsp;&emsp;allProcedure|工艺路线|string||
|&emsp;&emsp;simpleProcedureVOS|工艺路线|array|SimpleProcedureVO|
|&emsp;&emsp;&emsp;&emsp;procedureNo|工序编号|string||
|&emsp;&emsp;&emsp;&emsp;procedureName|工序名称|string||
|&emsp;&emsp;&emsp;&emsp;status|是否完成 0否 1是|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;procedureRemark|工序备注|string||
|&emsp;&emsp;&emsp;&emsp;procedureContent|工序内容|string||
|&emsp;&emsp;&emsp;&emsp;timePreparation|准备时长|number||
|&emsp;&emsp;&emsp;&emsp;singleTripTime|单趟加工时长|number||
|&emsp;&emsp;surplusQty|剩余数量|number||
|&emsp;&emsp;materialLedgerDesc|材料名称|string||
|&emsp;&emsp;materialLedgerSpec|材料规格|string||
|&emsp;&emsp;supplier|材料品牌|string||
|&emsp;&emsp;orderQty|订单数量|number||
|&emsp;&emsp;closeUid|结案人员|integer(int64)||
|&emsp;&emsp;closeTime|结案时间|string(date-time)||
|&emsp;&emsp;closeUserName|结案人员|string||
|&emsp;&emsp;createTuid|创建人id|integer(int64)||
|&emsp;&emsp;createUserName|创建人|string||
|&emsp;&emsp;materialPrice|产品单价|number||
|&emsp;&emsp;materialTotalPrice|产品总价|number||
|&emsp;&emsp;standardWorkHours|标准工时|number||
|&emsp;&emsp;printNumber|打印次数|integer(int32)||
|&emsp;&emsp;portionQty|排产数量|number||
|&emsp;&emsp;customerMaterialCode|客户对应的物料代码|string||
|&emsp;&emsp;arrangedQty||number||
|&emsp;&emsp;projectNumber|项目号|string||
|&emsp;&emsp;orderNumber|订单号|string||
|&emsp;&emsp;customerMaterialName|客户物料名称|string||
|&emsp;&emsp;closeRemark|结案备注|string||
|&emsp;&emsp;customFields|自定义字段值（fieldCode 为英文字段编码）；无自定义字段或未配置时不返回|array|EntityCustomFieldValueItemVO|
|&emsp;&emsp;&emsp;&emsp;entityType|实体类型，如 WORKORDER|string||
|&emsp;&emsp;&emsp;&emsp;fieldCode|字段英文名（field_code，如 wo_cf_1）|string||
|&emsp;&emsp;&emsp;&emsp;fieldValue|字段值，未填写时为空字符串|string||
|&emsp;&emsp;&emsp;&emsp;required|是否必填，对应 entity_custom_field_def.required：0否 1是|integer(int32)||


**响应示例**:
```javascript
{
	"success": true,
	"code": 1000,
	"message": "success",
	"totalItems": 12,
	"data": [
		{
			"woid": 0,
			"workorderNo": "",
			"workorderType": "",
			"urgentLevel": 0,
			"mtid": 0,
			"materialNo": "",
			"materialDesc": "",
			"materialSpec": "",
			"unit": "",
			"rid": 0,
			"planQty": 0,
			"completedQty": 0,
			"progress": "",
			"requireEndTime": "",
			"createTime": "",
			"startTime": "",
			"endTime": "",
			"customerNo": "",
			"customizationNo": "",
			"customerRequirement": "",
			"remark": "",
			"orderMaster": "",
			"planFollowWordNo": "",
			"status": 0,
			"errorInfo": "",
			"notes": "",
			"estimatedStartTime": "",
			"estimatedEndTime": "",
			"routingsMaterialNo": "",
			"materialStatus": 0,
			"sales": "",
			"completeProgress": 0,
			"actualCompleteTime": "",
			"overdueCount": 0,
			"salesorderNo": "",
			"currentProcedure": "",
			"nextProcedure": "",
			"allProcedure": "",
			"simpleProcedureVOS": [
				{
					"procedureNo": "",
					"procedureName": "",
					"status": 0,
					"procedureRemark": "",
					"procedureContent": "",
					"timePreparation": 0,
					"singleTripTime": 0
				}
			],
			"surplusQty": 0,
			"materialLedgerDesc": "",
			"materialLedgerSpec": "",
			"supplier": "",
			"orderQty": 0,
			"closeUid": 0,
			"closeTime": "",
			"closeUserName": "",
			"createTuid": 0,
			"createUserName": "",
			"materialPrice": 0,
			"materialTotalPrice": 0,
			"standardWorkHours": 0,
			"printNumber": 0,
			"portionQty": 0,
			"customerMaterialCode": "",
			"arrangedQty": 0,
			"projectNumber": "",
			"orderNumber": "",
			"customerMaterialName": "",
			"closeRemark": "",
			"customFields": [
				{
					"entityType": "",
					"fieldCode": "",
					"fieldValue": "",
					"required": 0
				}
			]
		}
	]
}
```


## 小报工工单导入


**接口地址**:`/lightmesapi/open/workorderController/importReportWorkorder`


**请求方式**:`POST`


**请求数据类型**:`application/x-www-form-urlencoded,application/json`


**响应数据类型**:`*/*`


**接口描述**:<p>通过此接口可以批量导入工单数据，通过一个list列表导入，导入生成工单的同时会生成工单对应的工序和工序参数，导入成功后会返回一个成功条数、失败条数以及失败原因列表。
    单个客户账号调用该接口的每秒请求数（QPS）最大限制为10</p>



**请求示例**:


```javascript
{
  "reportWorkorderParams": [
    {
      "workorderNo": "",
      "materialNo": "",
      "materialDesc": "",
      "materialSpec": "",
      "drawingNo": "",
      "planQty": 0,
      "unit": "",
      "customerNo": "",
      "endTime": "",
      "startTime": "",
      "receiptTime": "",
      "materialName": "",
      "procedureNames": ""
    }
  ]
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|AccessKeyId|AccessKeyId|header|true|string||
|AccessKeySecret|AccessKeySecret|header|true|string||
|reportWorkorderApiDTO|ReportWorkorderApiDTO|body|true|ReportWorkorderApiDTO|ReportWorkorderApiDTO|
|&emsp;&emsp;reportWorkorderParams|工单相关数据||true|array|ReportWorkorderParam|
|&emsp;&emsp;&emsp;&emsp;workorderNo|工单号||true|string||
|&emsp;&emsp;&emsp;&emsp;materialNo|产品编码||true|string||
|&emsp;&emsp;&emsp;&emsp;materialDesc|产品名称||true|string||
|&emsp;&emsp;&emsp;&emsp;materialSpec|规格||false|string||
|&emsp;&emsp;&emsp;&emsp;drawingNo|图号||false|string||
|&emsp;&emsp;&emsp;&emsp;planQty|计划数量||true|number||
|&emsp;&emsp;&emsp;&emsp;unit|单位||false|string||
|&emsp;&emsp;&emsp;&emsp;customerNo|客户代码||false|string||
|&emsp;&emsp;&emsp;&emsp;endTime|要求开工日期，时间戳格式||true|string(date-time)||
|&emsp;&emsp;&emsp;&emsp;startTime|要求开工日期，时间戳格式||true|string(date-time)||
|&emsp;&emsp;&emsp;&emsp;receiptTime|接单日期||false|string(date-time)||
|&emsp;&emsp;&emsp;&emsp;materialName|机友圈产品名||false|string||
|&emsp;&emsp;&emsp;&emsp;procedureNames|工序数据,多个工序以逗号隔开:工序名(加工时间-工价),工序名(加工时间-工价)||true|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|ResultDataApiReturnVO|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|success|成功与否|boolean||
|code|状态码|integer(int32)|integer(int32)|
|message|消息|string||
|data||ApiReturnVO|ApiReturnVO|
|&emsp;&emsp;successTotal|成功的条数|integer(int32)||
|&emsp;&emsp;errorTotal|失败的条数|integer(int32)||
|&emsp;&emsp;errorList|失败的错误信息|array|string|


**响应示例**:
```javascript
{
	"success": true,
	"code": 1000,
	"message": "success",
	"data": {
		"successTotal": 0,
		"errorTotal": 0,
		"errorList": []
	}
}
```


## 工单导入


**接口地址**:`/lightmesapi/open/workorderController/importWorkorder`


**请求方式**:`POST`


**请求数据类型**:`application/x-www-form-urlencoded,application/json`


**响应数据类型**:`*/*`


**接口描述**:<p>通过此接口可以批量导入工单数据，通过一个list列表导入，导入成功后会返回一个成功条数、失败条数以及失败原因列表。
  单个客户账号调用该接口的每秒请求数（QPS）最大限制为10。</p>



**请求示例**:


```javascript
{
  "workorderParams": [
    {
      "workorderNo": "",
      "workorderType": "",
      "urgentLevel": 0,
      "salesorderNo": "",
      "materialNo": "",
      "materialDesc": "",
      "materialSpec": "",
      "unit": "",
      "planQty": 0,
      "startTime": "",
      "endTime": "",
      "planFollowWordNo": "",
      "orderMaster": "",
      "sales": "",
      "customizationNo": "",
      "customerRequirement": "",
      "remark": "",
      "customerNo": "",
      "routingsMaterialNo": "",
      "materialLedgerDesc": "",
      "materialLedgerSpec": "",
      "supplier": "",
      "orderQty": 0,
      "receiveQty": 0,
      "arrivalTime": "",
      "purchaseQty": 0,
      "conformityRate": "",
      "productSpecification": "",
      "pictureUrl": "",
      "workorderExtraInfoList": [
        {
          "seq": 0,
          "fieldName": "",
          "fieldValue": "",
          "isdelete": 0
        }
      ],
      "customerMaterialCode": "",
      "projectNumber": "",
      "orderNumber": "",
      "customerMaterialName": "",
      "workcenterNo": "",
      "customFields": [
        {
          "fieldCode": "",
          "fieldValue": ""
        }
      ]
    }
  ]
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|AccessKeyId|AccessKeyId|header|true|string||
|AccessKeySecret|AccessKeySecret|header|true|string||
|workorderApiDTO|WorkorderApiDTO|body|true|WorkorderApiDTO|WorkorderApiDTO|
|&emsp;&emsp;workorderParams|工单相关数据||true|array|WorkorderParam|
|&emsp;&emsp;&emsp;&emsp;workorderNo|工单编号||true|string||
|&emsp;&emsp;&emsp;&emsp;workorderType|工单类型||false|string||
|&emsp;&emsp;&emsp;&emsp;urgentLevel|紧急状态,1加急*/2非加急**/3加急***/9非紧急||false|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;salesorderNo|销售单号||false|string||
|&emsp;&emsp;&emsp;&emsp;materialNo|产品编码||true|string||
|&emsp;&emsp;&emsp;&emsp;materialDesc|产品名称||false|string||
|&emsp;&emsp;&emsp;&emsp;materialSpec|规格||false|string||
|&emsp;&emsp;&emsp;&emsp;unit|单位||false|string||
|&emsp;&emsp;&emsp;&emsp;planQty|计划数量||true|number||
|&emsp;&emsp;&emsp;&emsp;startTime|要求开工日期，时间戳格式||false|string(date-time)||
|&emsp;&emsp;&emsp;&emsp;endTime|工单交期，时间戳格式||true|string(date-time)||
|&emsp;&emsp;&emsp;&emsp;planFollowWordNo|计划跟踪单号||false|string||
|&emsp;&emsp;&emsp;&emsp;orderMaster|跟单员||false|string||
|&emsp;&emsp;&emsp;&emsp;sales|业务员||false|string||
|&emsp;&emsp;&emsp;&emsp;customizationNo|客制代码||false|string||
|&emsp;&emsp;&emsp;&emsp;customerRequirement|客制特殊需求||false|string||
|&emsp;&emsp;&emsp;&emsp;remark|工单备注||false|string||
|&emsp;&emsp;&emsp;&emsp;customerNo|客户代码||false|string||
|&emsp;&emsp;&emsp;&emsp;routingsMaterialNo|工艺参考物料||false|string||
|&emsp;&emsp;&emsp;&emsp;materialLedgerDesc|物料台账描述||false|string||
|&emsp;&emsp;&emsp;&emsp;materialLedgerSpec|物料台账规格||false|string||
|&emsp;&emsp;&emsp;&emsp;supplier|供应商||false|string||
|&emsp;&emsp;&emsp;&emsp;orderQty|订单数量||false|number||
|&emsp;&emsp;&emsp;&emsp;receiveQty|收货数量||false|number||
|&emsp;&emsp;&emsp;&emsp;arrivalTime|收货时间，时间戳格式||false|string(date-time)||
|&emsp;&emsp;&emsp;&emsp;purchaseQty|采购数量||false|number||
|&emsp;&emsp;&emsp;&emsp;conformityRate|||false|string||
|&emsp;&emsp;&emsp;&emsp;productSpecification|||false|string||
|&emsp;&emsp;&emsp;&emsp;pictureUrl|图片备注||false|string||
|&emsp;&emsp;&emsp;&emsp;workorderExtraInfoList|工单额外字段集合,已存在为修改逻辑||false|array|WorkorderExtraInfoDTO|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;seq|序号,排序用(升序)||false|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;fieldName|字段名称||true|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;fieldValue|字段值||true|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;isdelete|0未删除 1已删除,默认未删除||false|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;customerMaterialCode|客户对应的物料代码||false|string||
|&emsp;&emsp;&emsp;&emsp;projectNumber|项目号||false|string||
|&emsp;&emsp;&emsp;&emsp;orderNumber|订单号||false|string||
|&emsp;&emsp;&emsp;&emsp;customerMaterialName|客户物料名称||false|string||
|&emsp;&emsp;&emsp;&emsp;workcenterNo|工作中心编号||false|string||
|&emsp;&emsp;&emsp;&emsp;customFields|自定义字段值列表（fieldCode + fieldValue）||false|array|EntityCustomFieldValueItemDTO|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;fieldCode|字段英文名（field_code，如 wo_cf_1）||true|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;fieldValue|字段值||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|ResultDataApiReturnVO|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|success|成功与否|boolean||
|code|状态码|integer(int32)|integer(int32)|
|message|消息|string||
|data||ApiReturnVO|ApiReturnVO|
|&emsp;&emsp;successTotal|成功的条数|integer(int32)||
|&emsp;&emsp;errorTotal|失败的条数|integer(int32)||
|&emsp;&emsp;errorList|失败的错误信息|array|string|


**响应示例**:
```javascript
{
	"success": true,
	"code": 1000,
	"message": "success",
	"data": {
		"successTotal": 0,
		"errorTotal": 0,
		"errorList": []
	}
}
```


## 查询达成率报表


**接口地址**:`/lightmesapi/open/workorderController/selectComplishReport`


**请求方式**:`POST`


**请求数据类型**:`application/x-www-form-urlencoded,application/json`


**响应数据类型**:`*/*`


**接口描述**:<p>通过此接口可以查询达成率报表。
单个客户账号调用该接口的每秒请求数（QPS）最大限制为10。</p>



**请求示例**:


```javascript
{
  "pageNum": 0,
  "pageSize": 0,
  "wcids": [],
  "did": 0,
  "shiftName": "",
  "startTime": "",
  "endTime": "",
  "status": 0
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|AccessKeyId|AccessKeyId|header|true|string||
|AccessKeySecret|AccessKeySecret|header|true|string||
|complishReportDTO|ComplishReportDTO|body|true|ComplishReportDTO|ComplishReportDTO|
|&emsp;&emsp;pageNum|查询页||true|integer(int32)||
|&emsp;&emsp;pageSize|每页条数||true|integer(int32)||
|&emsp;&emsp;wcids|工作中心id||false|array|integer(int64)|
|&emsp;&emsp;did|部门id||false|integer(int64)||
|&emsp;&emsp;shiftName|班次名称||false|string||
|&emsp;&emsp;startTime|开始时间||true|string(date-time)||
|&emsp;&emsp;endTime|结束时间||true|string(date-time)||
|&emsp;&emsp;status|状态 1任务维度 2数量维度||true|integer(int32)||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|ResultQueryComplishReportVO|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|success|成功与否|boolean||
|code|状态码|integer(int32)|integer(int32)|
|message|消息|string||
|totalItems|总条数|integer(int32)|integer(int32)|
|data||array|ComplishReportVO|
|&emsp;&emsp;sid|班次id|integer(int64)||
|&emsp;&emsp;shiftName|班次名称|string||
|&emsp;&emsp;workDate|日期|string(date-time)||
|&emsp;&emsp;departmentName|部门名称|string||
|&emsp;&emsp;taskCount|任务单数|integer(int32)||
|&emsp;&emsp;completedTaskCount|达成单数|integer(int32)||
|&emsp;&emsp;unCompletedTaskCount|未达成单数|integer(int32)||
|&emsp;&emsp;taskQty|任务数量|number||
|&emsp;&emsp;completedTaskQty|达成数量|number||
|&emsp;&emsp;unCompletedTaskQty|未达成数量|number||
|&emsp;&emsp;completeRate|达成率|number||
|&emsp;&emsp;qtyCompleteRate|数量达成率|number||


**响应示例**:
```javascript
{
	"success": true,
	"code": 1000,
	"message": "success",
	"totalItems": 12,
	"data": [
		{
			"sid": 0,
			"shiftName": "",
			"workDate": "",
			"departmentName": "",
			"taskCount": 0,
			"completedTaskCount": 0,
			"unCompletedTaskCount": 0,
			"taskQty": 0,
			"completedTaskQty": 0,
			"unCompletedTaskQty": 0,
			"completeRate": 0,
			"qtyCompleteRate": 0
		}
	]
}
```


## 工序报工结果查询


**接口地址**:`/lightmesapi/open/workorderController/selectProceduresReportDataByTime`


**请求方式**:`POST`


**请求数据类型**:`application/x-www-form-urlencoded,application/json`


**响应数据类型**:`*/*`


**接口描述**:<p>通过此接口可以查询指定时间段内的所有工序报工结果信息，时间段最大1天，这里的时间是指工序任务加工完成并通过审核的时间；
    单个客户账号调用该接口的每秒请求数（QPS）最大限制为10。</p>



**请求示例**:


```javascript
{
  "startTime": "",
  "endTime": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|AccessKeyId|AccessKeyId|header|true|string||
|AccessKeySecret|AccessKeySecret|header|true|string||
|selectByDataTimeDTO|SelectByDataTimeDTO|body|true|SelectByDataTimeDTO|SelectByDataTimeDTO|
|&emsp;&emsp;startTime|查询开始时间yyyy-MM-dd HH:mm:ss||true|string(date-time)||
|&emsp;&emsp;endTime|查询结束时间yyyy-MM-dd HH:mm:ss||true|string(date-time)||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|ResultDataListProcedureReportWriteBackParams|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|success|成功与否|boolean||
|code|状态码|integer(int32)|integer(int32)|
|message|消息|string||
|data||array|ProcedureReportWriteBackParams|
|&emsp;&emsp;goodQty|报工良品数|number||
|&emsp;&emsp;badQty|不良品总和|number||
|&emsp;&emsp;badQtyManufacturing|加工不良|number||
|&emsp;&emsp;badQtyIncoming|来料不良|number||
|&emsp;&emsp;woid||integer(int64)||
|&emsp;&emsp;workorderNo|工单编号|string||
|&emsp;&emsp;workorderType|工单类型|string||
|&emsp;&emsp;salesorderNo|销售单号|string||
|&emsp;&emsp;planFollowWordNo|计划跟单号|string||
|&emsp;&emsp;materialNo|物料编号|string||
|&emsp;&emsp;materialDesc|物料名称|string||
|&emsp;&emsp;unit|单位|string||
|&emsp;&emsp;materialSpec|物料规格|string||
|&emsp;&emsp;warehouse|仓库|string||
|&emsp;&emsp;productionBatchNo|生产批号|string||
|&emsp;&emsp;materialQty|原料标识数量|number||
|&emsp;&emsp;weight|布头布尾KG|number||
|&emsp;&emsp;materialUnit|原料标识单位|string||
|&emsp;&emsp;knifeWeight|栏刀口料KG|number||
|&emsp;&emsp;materialWeight||number||
|&emsp;&emsp;pieceWeight||number||
|&emsp;&emsp;scrapWeight||number||
|&emsp;&emsp;taskActionRemark||string||
|&emsp;&emsp;inStockQty|入库数|number||
|&emsp;&emsp;transferCardNo|流转卡号|string||
|&emsp;&emsp;wtaid|工单任务id|integer(int64)||
|&emsp;&emsp;tid||integer(int64)||
|&emsp;&emsp;procedureNo|工序编号|string||
|&emsp;&emsp;procedureOrder|工序顺序|integer(int32)||
|&emsp;&emsp;procedureName|工序名称|string||
|&emsp;&emsp;actualTime|使用时长|number||
|&emsp;&emsp;earnedHours|产出工时|number||
|&emsp;&emsp;userNames|操作人员|string||
|&emsp;&emsp;employeeNos|人员工号|string||
|&emsp;&emsp;machineNo|设备编号|string||
|&emsp;&emsp;machineName|设备名称|string||
|&emsp;&emsp;workcenterNo|工作中心编号|string||
|&emsp;&emsp;workcenterName|工作中心名称|string||
|&emsp;&emsp;workshopName|车间|string||
|&emsp;&emsp;productLine|产线|string||
|&emsp;&emsp;taskStartTime|开始日期yyyy-MM-dd HH:mm:ss|string||
|&emsp;&emsp;taskEndTime|结束时间 yyyy-MM-dd HH:mm:ss|string||
|&emsp;&emsp;workorderPlanQty|工单数量|number||
|&emsp;&emsp;component|子件|string||
|&emsp;&emsp;materialCode|原料代码|string||
|&emsp;&emsp;materialBatchNo|原料批号|string||
|&emsp;&emsp;procedureRemark|工序备注|string||
|&emsp;&emsp;singleTripQty|单趟加工数量(必填) '单趟加工数量'|number||
|&emsp;&emsp;singleTripTime|单趟加工时长(秒)|number||
|&emsp;&emsp;frequencySize|脉冲次数|integer(int32)||
|&emsp;&emsp;oneLevelReason|一级审核|string||
|&emsp;&emsp;twoLevelReason|二级审核|string||
|&emsp;&emsp;threeLevelReason|三级审核|string||
|&emsp;&emsp;approverName|审核人员|string||
|&emsp;&emsp;approverTime|审核日期|string||
|&emsp;&emsp;workDate|生产日期|string||
|&emsp;&emsp;shiftName|班次名称|string||
|&emsp;&emsp;mouldNo|模具编号|string||
|&emsp;&emsp;mouldName|模具名称|string||
|&emsp;&emsp;planQty|工单数量|number||
|&emsp;&emsp;createTime|工单创建日期|string(date-time)||
|&emsp;&emsp;note|备注|string||
|&emsp;&emsp;completionStage|工单完工进度标识|integer(int32)||
|&emsp;&emsp;chassisNo|底盘号/盘底号|string||
|&emsp;&emsp;rearOutriggerCode|后支腿编码|string||


**响应示例**:
```javascript
{
	"success": true,
	"code": 1000,
	"message": "success",
	"data": [
		{
			"goodQty": 0,
			"badQty": 0,
			"badQtyManufacturing": 0,
			"badQtyIncoming": 0,
			"woid": 0,
			"workorderNo": "",
			"workorderType": "",
			"salesorderNo": "",
			"planFollowWordNo": "",
			"materialNo": "",
			"materialDesc": "",
			"unit": "",
			"materialSpec": "",
			"warehouse": "",
			"productionBatchNo": "",
			"materialQty": 0,
			"weight": 0,
			"materialUnit": "",
			"knifeWeight": 0,
			"materialWeight": 0,
			"pieceWeight": 0,
			"scrapWeight": 0,
			"taskActionRemark": "",
			"inStockQty": 0,
			"transferCardNo": "",
			"wtaid": 0,
			"tid": 0,
			"procedureNo": "",
			"procedureOrder": 0,
			"procedureName": "",
			"actualTime": 0,
			"earnedHours": 0,
			"userNames": "",
			"employeeNos": "",
			"machineNo": "",
			"machineName": "",
			"workcenterNo": "",
			"workcenterName": "",
			"workshopName": "",
			"productLine": "",
			"taskStartTime": "",
			"taskEndTime": "",
			"workorderPlanQty": 0,
			"component": "",
			"materialCode": "",
			"materialBatchNo": "",
			"procedureRemark": "",
			"singleTripQty": 0,
			"singleTripTime": 0,
			"frequencySize": 0,
			"oneLevelReason": "",
			"twoLevelReason": "",
			"threeLevelReason": "",
			"approverName": "",
			"approverTime": "",
			"workDate": "",
			"shiftName": "",
			"mouldNo": "",
			"mouldName": "",
			"planQty": 0,
			"createTime": "",
			"note": "",
			"completionStage": 0,
			"chassisNo": "",
			"rearOutriggerCode": ""
		}
	]
}
```


## 工序排产结果查询


**接口地址**:`/lightmesapi/open/workorderController/selectProductionBackParamsByTime`


**请求方式**:`POST`


**请求数据类型**:`application/x-www-form-urlencoded,application/json`


**响应数据类型**:`*/*`


**接口描述**:<p>通过此接口可以查询指定时间段内的所有工序排产结果信息，时间段最大1天，这里的时间是指工序任务排产的时间；
    单个客户账号调用该接口的每秒请求数（QPS）最大限制为10。</p>



**请求示例**:


```javascript
{
  "pageNum": 0,
  "pageSize": 0,
  "startTime": "",
  "endTime": "",
  "query": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|AccessKeyId|AccessKeyId|header|true|string||
|AccessKeySecret|AccessKeySecret|header|true|string||
|querySelectByDataTimeDTO|QuerySelectByDataTimeDTO|body|true|QuerySelectByDataTimeDTO|QuerySelectByDataTimeDTO|
|&emsp;&emsp;pageNum|查询页||true|integer(int32)||
|&emsp;&emsp;pageSize|每页条数||true|integer(int32)||
|&emsp;&emsp;startTime|查询开始时间yyyy-MM-dd HH:mm:ss||true|string(date-time)||
|&emsp;&emsp;endTime|查询结束时间yyyy-MM-dd HH:mm:ss||true|string(date-time)||
|&emsp;&emsp;query|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|ResultQueryProductionBackParams|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|success|成功与否|boolean||
|code|状态码|integer(int32)|integer(int32)|
|message|消息|string||
|totalItems|总条数|integer(int32)|integer(int32)|
|data||array|ProductionBackParams|
|&emsp;&emsp;wopid|工序任务id|string||
|&emsp;&emsp;workorderNo|工单编号|string||
|&emsp;&emsp;salesorderNo|销单号|string||
|&emsp;&emsp;materialNo|物料编号|string||
|&emsp;&emsp;materialDesc|物料名称|string||
|&emsp;&emsp;materialSpec|物料规格|string||
|&emsp;&emsp;procedureNo|工序编号|string||
|&emsp;&emsp;procedureName|工序名称|string||
|&emsp;&emsp;planFollowWordNo|计划跟踪号|string||
|&emsp;&emsp;planQty|计划数量|number||
|&emsp;&emsp;pendingQty|待排产数|number||
|&emsp;&emsp;arrangedQty|已排产数|number||
|&emsp;&emsp;completedQty|完工数|number||
|&emsp;&emsp;procedureOrder|工序序号|integer(int32)||
|&emsp;&emsp;completionStage|是否工单完结点 0非 1是|integer(int32)||
|&emsp;&emsp;productionBackWorkcenters||array|ProductionBackWorkcenter|
|&emsp;&emsp;&emsp;&emsp;wtid|任务id|string||
|&emsp;&emsp;&emsp;&emsp;workcenterNo|工作中心编号|string||
|&emsp;&emsp;&emsp;&emsp;workcenterName|工作中心名称|string||
|&emsp;&emsp;&emsp;&emsp;machineNo|设备编号|string||
|&emsp;&emsp;&emsp;&emsp;machineName|设备名称|string||
|&emsp;&emsp;&emsp;&emsp;planQty|计划数量|number||
|&emsp;&emsp;&emsp;&emsp;departmentName|生产部门|string||
|&emsp;&emsp;&emsp;&emsp;workDate|排产时间|string||
|&emsp;&emsp;&emsp;&emsp;estimatedStartTime|预计开始时间|string||
|&emsp;&emsp;&emsp;&emsp;estimatedEndTime|预计结束时间|string||


**响应示例**:
```javascript
{
	"success": true,
	"code": 1000,
	"message": "success",
	"totalItems": 12,
	"data": [
		{
			"wopid": "",
			"workorderNo": "",
			"salesorderNo": "",
			"materialNo": "",
			"materialDesc": "",
			"materialSpec": "",
			"procedureNo": "",
			"procedureName": "",
			"planFollowWordNo": "",
			"planQty": 0,
			"pendingQty": 0,
			"arrangedQty": 0,
			"completedQty": 0,
			"procedureOrder": 0,
			"completionStage": 0,
			"productionBackWorkcenters": [
				{
					"wtid": "",
					"workcenterNo": "",
					"workcenterName": "",
					"machineNo": "",
					"machineName": "",
					"planQty": 0,
					"departmentName": "",
					"workDate": "",
					"estimatedStartTime": "",
					"estimatedEndTime": ""
				}
			]
		}
	]
}
```


## 查询投料明细


**接口地址**:`/lightmesapi/open/workorderController/selectTaskUseMaterial`


**请求方式**:`POST`


**请求数据类型**:`application/x-www-form-urlencoded,application/json`


**响应数据类型**:`*/*`


**接口描述**:<p>通过此接口可以查询到指定时间段内的查询投料明细。
    单个客户账号调用该接口的每秒请求数（QPS）最大限制为10。</p>



**请求示例**:


```javascript
{
  "pageNum": 0,
  "pageSize": 0,
  "startTime": "",
  "endTime": "",
  "workorderNo": "",
  "useMaterial": "",
  "materialBatchNo": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|AccessKeyId|AccessKeyId|header|true|string||
|AccessKeySecret|AccessKeySecret|header|true|string||
|apiTaskUseMaterialDTO|ApiTaskUseMaterialDTO|body|true|ApiTaskUseMaterialDTO|ApiTaskUseMaterialDTO|
|&emsp;&emsp;pageNum|查询页||true|integer(int32)||
|&emsp;&emsp;pageSize|每页条数||true|integer(int32)||
|&emsp;&emsp;startTime|||false|string(date-time)||
|&emsp;&emsp;endTime|||false|string(date-time)||
|&emsp;&emsp;workorderNo|工单号||false|string||
|&emsp;&emsp;useMaterial|物料编码||false|string||
|&emsp;&emsp;materialBatchNo|物料批号||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|ResultQueryTaskUseMaterialVO|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|success|成功与否|boolean||
|code|状态码|integer(int32)|integer(int32)|
|message|消息|string||
|totalItems|总条数|integer(int32)|integer(int32)|
|data||array|TaskUseMaterialVO|
|&emsp;&emsp;workorderNo|工单号|string||
|&emsp;&emsp;taskNo|任务编号|string||
|&emsp;&emsp;did|产线id|integer(int64)||
|&emsp;&emsp;workShop|车间|string||
|&emsp;&emsp;productLine|产线|string||
|&emsp;&emsp;wcid|工作中心id|integer(int64)||
|&emsp;&emsp;workcenterNo|工作中心编号|string||
|&emsp;&emsp;workcenterName|工作中心名称|string||
|&emsp;&emsp;procedureNo|工序编号|string||
|&emsp;&emsp;procedureName|工序名称|string||
|&emsp;&emsp;useMaterial|物料编码|string||
|&emsp;&emsp;useMaterialDesc|物料名称|string||
|&emsp;&emsp;materialBatchNo|批号|string||
|&emsp;&emsp;useQty|投料数量|number||
|&emsp;&emsp;useUnit|单位|string||
|&emsp;&emsp;quantity|用量|number||
|&emsp;&emsp;useTime|投料时间|string(date-time)||
|&emsp;&emsp;uid|投料人员id|integer(int64)||
|&emsp;&emsp;userName|投料人员姓名|string||
|&emsp;&emsp;urlStr|照片|string||
|&emsp;&emsp;urls|照片|array|string|


**响应示例**:
```javascript
{
	"success": true,
	"code": 1000,
	"message": "success",
	"totalItems": 12,
	"data": [
		{
			"workorderNo": "",
			"taskNo": "",
			"did": 0,
			"workShop": "",
			"productLine": "",
			"wcid": 0,
			"workcenterNo": "",
			"workcenterName": "",
			"procedureNo": "",
			"procedureName": "",
			"useMaterial": "",
			"useMaterialDesc": "",
			"materialBatchNo": "",
			"useQty": 0,
			"useUnit": "",
			"quantity": 0,
			"useTime": "",
			"uid": 0,
			"userName": "",
			"urlStr": "",
			"urls": []
		}
	]
}
```


## 工序任务查询


**接口地址**:`/lightmesapi/open/workorderController/selectWorkorderProcedure`


**请求方式**:`POST`


**请求数据类型**:`application/x-www-form-urlencoded,application/json`


**响应数据类型**:`*/*`


**接口描述**:<p>通过此接口可以查询到指定时间段内有变化的工序任务信息；
    单个客户账号调用该接口的每秒请求数（QPS）最大限制为10。</p>



**请求示例**:


```javascript
{
  "pageNum": 0,
  "pageSize": 0,
  "startTime": "",
  "endTime": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|AccessKeyId|AccessKeyId|header|true|string||
|AccessKeySecret|AccessKeySecret|header|true|string||
|apiWorkorderProcedureDTO|ApiWorkorderProcedureDTO|body|true|ApiWorkorderProcedureDTO|ApiWorkorderProcedureDTO|
|&emsp;&emsp;pageNum|查询页||true|integer(int32)||
|&emsp;&emsp;pageSize|每页条数||true|integer(int32)||
|&emsp;&emsp;startTime|开始时间||false|string(date-time)||
|&emsp;&emsp;endTime|结束时间||false|string(date-time)||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|ResultQueryApiWorkorderProcedureVO|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|success|成功与否|boolean||
|code|状态码|integer(int32)|integer(int32)|
|message|消息|string||
|totalItems|总条数|integer(int32)|integer(int32)|
|data||array|ApiWorkorderProcedureVO|
|&emsp;&emsp;wopid|工序任务id|integer(int64)||
|&emsp;&emsp;workorderNo|工单编号|string||
|&emsp;&emsp;salesorderNo|销售单号|string||
|&emsp;&emsp;materialNo|产品编码|string||
|&emsp;&emsp;materialDesc|品名|string||
|&emsp;&emsp;materialSpec|规格|string||
|&emsp;&emsp;planFollowWordNo|计划跟踪号|string||
|&emsp;&emsp;procedureNo|工序任务编号|string||
|&emsp;&emsp;procedureName|工序任务名称|string||
|&emsp;&emsp;planQty|计划数|number||
|&emsp;&emsp;pendingQty|待排产数|number||
|&emsp;&emsp;arrangedQty|已排产数|number||
|&emsp;&emsp;completedQty|完工数|number||


**响应示例**:
```javascript
{
	"success": true,
	"code": 1000,
	"message": "success",
	"totalItems": 12,
	"data": [
		{
			"wopid": 0,
			"workorderNo": "",
			"salesorderNo": "",
			"materialNo": "",
			"materialDesc": "",
			"materialSpec": "",
			"planFollowWordNo": "",
			"procedureNo": "",
			"procedureName": "",
			"planQty": 0,
			"pendingQty": 0,
			"arrangedQty": 0,
			"completedQty": 0
		}
	]
}
```


## 工单报工结果查询


**接口地址**:`/lightmesapi/open/workorderController/selectWorkorderReportDataByTime`


**请求方式**:`POST`


**请求数据类型**:`application/x-www-form-urlencoded,application/json`


**响应数据类型**:`*/*`


**接口描述**:<p>通过此接口可以查询指定时间段内的所有工单报工结果信息，时间段最大1天，工单完成以系统设置的最后一道工序为标准，这里的时间是指工单最后工序任务加工完成并通过审核的时间。
    单个客户账号调用该接口的每秒请求数（QPS）最大限制为10</p>



**请求示例**:


```javascript
{
  "startTime": "",
  "endTime": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|AccessKeyId|AccessKeyId|header|true|string||
|AccessKeySecret|AccessKeySecret|header|true|string||
|selectByDataTimeDTO|SelectByDataTimeDTO|body|true|SelectByDataTimeDTO|SelectByDataTimeDTO|
|&emsp;&emsp;startTime|查询开始时间yyyy-MM-dd HH:mm:ss||true|string(date-time)||
|&emsp;&emsp;endTime|查询结束时间yyyy-MM-dd HH:mm:ss||true|string(date-time)||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|ResultDataListProcedureReportWriteBackParams|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|success|成功与否|boolean||
|code|状态码|integer(int32)|integer(int32)|
|message|消息|string||
|data||array|ProcedureReportWriteBackParams|
|&emsp;&emsp;goodQty|报工良品数|number||
|&emsp;&emsp;badQty|不良品总和|number||
|&emsp;&emsp;badQtyManufacturing|加工不良|number||
|&emsp;&emsp;badQtyIncoming|来料不良|number||
|&emsp;&emsp;woid||integer(int64)||
|&emsp;&emsp;workorderNo|工单编号|string||
|&emsp;&emsp;workorderType|工单类型|string||
|&emsp;&emsp;salesorderNo|销售单号|string||
|&emsp;&emsp;planFollowWordNo|计划跟单号|string||
|&emsp;&emsp;materialNo|物料编号|string||
|&emsp;&emsp;materialDesc|物料名称|string||
|&emsp;&emsp;unit|单位|string||
|&emsp;&emsp;materialSpec|物料规格|string||
|&emsp;&emsp;warehouse|仓库|string||
|&emsp;&emsp;productionBatchNo|生产批号|string||
|&emsp;&emsp;materialQty|原料标识数量|number||
|&emsp;&emsp;weight|布头布尾KG|number||
|&emsp;&emsp;materialUnit|原料标识单位|string||
|&emsp;&emsp;knifeWeight|栏刀口料KG|number||
|&emsp;&emsp;materialWeight||number||
|&emsp;&emsp;pieceWeight||number||
|&emsp;&emsp;scrapWeight||number||
|&emsp;&emsp;taskActionRemark||string||
|&emsp;&emsp;inStockQty|入库数|number||
|&emsp;&emsp;transferCardNo|流转卡号|string||
|&emsp;&emsp;wtaid|工单任务id|integer(int64)||
|&emsp;&emsp;tid||integer(int64)||
|&emsp;&emsp;procedureNo|工序编号|string||
|&emsp;&emsp;procedureOrder|工序顺序|integer(int32)||
|&emsp;&emsp;procedureName|工序名称|string||
|&emsp;&emsp;actualTime|使用时长|number||
|&emsp;&emsp;earnedHours|产出工时|number||
|&emsp;&emsp;userNames|操作人员|string||
|&emsp;&emsp;employeeNos|人员工号|string||
|&emsp;&emsp;machineNo|设备编号|string||
|&emsp;&emsp;machineName|设备名称|string||
|&emsp;&emsp;workcenterNo|工作中心编号|string||
|&emsp;&emsp;workcenterName|工作中心名称|string||
|&emsp;&emsp;workshopName|车间|string||
|&emsp;&emsp;productLine|产线|string||
|&emsp;&emsp;taskStartTime|开始日期yyyy-MM-dd HH:mm:ss|string||
|&emsp;&emsp;taskEndTime|结束时间 yyyy-MM-dd HH:mm:ss|string||
|&emsp;&emsp;workorderPlanQty|工单数量|number||
|&emsp;&emsp;component|子件|string||
|&emsp;&emsp;materialCode|原料代码|string||
|&emsp;&emsp;materialBatchNo|原料批号|string||
|&emsp;&emsp;procedureRemark|工序备注|string||
|&emsp;&emsp;singleTripQty|单趟加工数量(必填) '单趟加工数量'|number||
|&emsp;&emsp;singleTripTime|单趟加工时长(秒)|number||
|&emsp;&emsp;frequencySize|脉冲次数|integer(int32)||
|&emsp;&emsp;oneLevelReason|一级审核|string||
|&emsp;&emsp;twoLevelReason|二级审核|string||
|&emsp;&emsp;threeLevelReason|三级审核|string||
|&emsp;&emsp;approverName|审核人员|string||
|&emsp;&emsp;approverTime|审核日期|string||
|&emsp;&emsp;workDate|生产日期|string||
|&emsp;&emsp;shiftName|班次名称|string||
|&emsp;&emsp;mouldNo|模具编号|string||
|&emsp;&emsp;mouldName|模具名称|string||
|&emsp;&emsp;planQty|工单数量|number||
|&emsp;&emsp;createTime|工单创建日期|string(date-time)||
|&emsp;&emsp;note|备注|string||
|&emsp;&emsp;completionStage|工单完工进度标识|integer(int32)||
|&emsp;&emsp;chassisNo|底盘号/盘底号|string||
|&emsp;&emsp;rearOutriggerCode|后支腿编码|string||


**响应示例**:
```javascript
{
	"success": true,
	"code": 1000,
	"message": "success",
	"data": [
		{
			"goodQty": 0,
			"badQty": 0,
			"badQtyManufacturing": 0,
			"badQtyIncoming": 0,
			"woid": 0,
			"workorderNo": "",
			"workorderType": "",
			"salesorderNo": "",
			"planFollowWordNo": "",
			"materialNo": "",
			"materialDesc": "",
			"unit": "",
			"materialSpec": "",
			"warehouse": "",
			"productionBatchNo": "",
			"materialQty": 0,
			"weight": 0,
			"materialUnit": "",
			"knifeWeight": 0,
			"materialWeight": 0,
			"pieceWeight": 0,
			"scrapWeight": 0,
			"taskActionRemark": "",
			"inStockQty": 0,
			"transferCardNo": "",
			"wtaid": 0,
			"tid": 0,
			"procedureNo": "",
			"procedureOrder": 0,
			"procedureName": "",
			"actualTime": 0,
			"earnedHours": 0,
			"userNames": "",
			"employeeNos": "",
			"machineNo": "",
			"machineName": "",
			"workcenterNo": "",
			"workcenterName": "",
			"workshopName": "",
			"productLine": "",
			"taskStartTime": "",
			"taskEndTime": "",
			"workorderPlanQty": 0,
			"component": "",
			"materialCode": "",
			"materialBatchNo": "",
			"procedureRemark": "",
			"singleTripQty": 0,
			"singleTripTime": 0,
			"frequencySize": 0,
			"oneLevelReason": "",
			"twoLevelReason": "",
			"threeLevelReason": "",
			"approverName": "",
			"approverTime": "",
			"workDate": "",
			"shiftName": "",
			"mouldNo": "",
			"mouldName": "",
			"planQty": 0,
			"createTime": "",
			"note": "",
			"completionStage": 0,
			"chassisNo": "",
			"rearOutriggerCode": ""
		}
	]
}
```


## 报工明细查询


**接口地址**:`/lightmesapi/open/workorderController/selectWorkorderTaskActionStatistics`


**请求方式**:`POST`


**请求数据类型**:`application/x-www-form-urlencoded,application/json`


**响应数据类型**:`*/*`


**接口描述**:<p>通过此接口可以查询到报工明细。
    单个客户账号调用该接口的每秒请求数（QPS）最大限制为10。</p>



**请求示例**:


```javascript
{
  "pageNum": 0,
  "pageSize": 0,
  "did": 0,
  "departmentName": "",
  "startTime": "",
  "endTime": "",
  "wcidList": [],
  "orderByDTOS": [
    {
      "orderName": "",
      "sort": "",
      "grade": 0
    }
  ],
  "workorderNo": "",
  "procedureNo": "",
  "materialNo": "",
  "machineNo": "",
  "shiftTimeName": "",
  "materialDesc": "",
  "materialSpec": "",
  "taskNo": "",
  "workcenterNo": "",
  "startDate": "",
  "endDate": "",
  "query": "",
  "employeeName": "",
  "employeeNo": "",
  "productionBatchNo": "",
  "statusList": [],
  "shiftStartTime": "",
  "shiftEndTime": "",
  "startDateStr": "",
  "endDateStr": "",
  "workorderType": "",
  "sumType": 0,
  "exportType": 0,
  "workType": 0,
  "status": 0,
  "userName": "",
  "reportUserName": "",
  "reportUidList": [],
  "tuidList": [],
  "customerRequirement": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|AccessKeyId|AccessKeyId|header|true|string||
|AccessKeySecret|AccessKeySecret|header|true|string||
|工时统计|工时统计|body|true|工时统计|工时统计|
|&emsp;&emsp;pageNum|查询页||true|integer(int32)||
|&emsp;&emsp;pageSize|每页条数||true|integer(int32)||
|&emsp;&emsp;did|产线id||true|integer(int64)||
|&emsp;&emsp;departmentName|车间名称||false|string||
|&emsp;&emsp;startTime|开始时间||false|string(date-time)||
|&emsp;&emsp;endTime|结束时间||false|string(date-time)||
|&emsp;&emsp;wcidList|||false|array|integer(int64)|
|&emsp;&emsp;orderByDTOS|排序规则||false|array|OrderByDTO|
|&emsp;&emsp;&emsp;&emsp;orderName|排序字段||false|string||
|&emsp;&emsp;&emsp;&emsp;sort|排序规则||false|string||
|&emsp;&emsp;&emsp;&emsp;grade|等级越大,排序规则也优先||false|integer(int32)||
|&emsp;&emsp;workorderNo|工单号||false|string||
|&emsp;&emsp;procedureNo|工序编号||false|string||
|&emsp;&emsp;materialNo|料号||false|string||
|&emsp;&emsp;machineNo|设备编号||false|string||
|&emsp;&emsp;shiftTimeName|班次名称||false|string||
|&emsp;&emsp;materialDesc|品名||false|string||
|&emsp;&emsp;materialSpec|规格||false|string||
|&emsp;&emsp;taskNo|生产任务单号||false|string||
|&emsp;&emsp;workcenterNo|工作中心编码或名称||false|string||
|&emsp;&emsp;startDate|开始时间||false|string(date-time)||
|&emsp;&emsp;endDate|结束时间||false|string(date-time)||
|&emsp;&emsp;query|搜索输入内容||false|string||
|&emsp;&emsp;employeeName|姓名||false|string||
|&emsp;&emsp;employeeNo|工号||false|string||
|&emsp;&emsp;productionBatchNo|生产批号||false|string||
|&emsp;&emsp;statusList|审批状态 0待审批 1已审批||true|array|integer(int32)|
|&emsp;&emsp;shiftStartTime|班次开始时间||true|string(date-time)||
|&emsp;&emsp;shiftEndTime|班次结束时间||true|string(date-time)||
|&emsp;&emsp;startDateStr|开始日期||false|string||
|&emsp;&emsp;endDateStr|结束日期||false|string||
|&emsp;&emsp;workorderType|工单类型||false|string||
|&emsp;&emsp;sumType|合计类型 1获得工时 2产出时长 3综合工时 ||false|integer(int32)||
|&emsp;&emsp;exportType|1按获得工时导出, 2导出||false|integer(int32)||
|&emsp;&emsp;workType|工种 1临时工 2正式工||false|integer(int32)||
|&emsp;&emsp;status|1进行中,2提交,3审核中,4完成,9挂起||false|integer(int32)||
|&emsp;&emsp;userName|生产人员||false|string||
|&emsp;&emsp;reportUserName|报工人员||false|string||
|&emsp;&emsp;reportUidList|报工人员id集合||false|array|integer(int64)|
|&emsp;&emsp;tuidList|生产人员id集合||false|array|integer(int64)|
|&emsp;&emsp;customerRequirement|客制特殊需求||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|ResultQuery报工统计vo|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|success|成功与否|boolean||
|code|状态码|integer(int32)|integer(int32)|
|message|消息|string||
|totalItems|总条数|integer(int32)|integer(int32)|
|data||array|报工统计vo|
|&emsp;&emsp;wtid|任务id|integer(int64)||
|&emsp;&emsp;wtaid|任务执行id|integer(int64)||
|&emsp;&emsp;endTime|报工时间|string(date-time)||
|&emsp;&emsp;woid|工单id|integer(int64)||
|&emsp;&emsp;departmentName|车间名称|string||
|&emsp;&emsp;workorderNo|工单号|string||
|&emsp;&emsp;workorderType|工单类型|string||
|&emsp;&emsp;unit|单位|string||
|&emsp;&emsp;taskNo|任务编号|string||
|&emsp;&emsp;rpid|工序id|integer(int64)||
|&emsp;&emsp;procedureNo|工序编号|string||
|&emsp;&emsp;procedureName|工序名称|string||
|&emsp;&emsp;mtid|物料id|integer(int64)||
|&emsp;&emsp;materialNo|料号|string||
|&emsp;&emsp;materialDesc|品名|string||
|&emsp;&emsp;materialSpec|规格|string||
|&emsp;&emsp;mid|设备id|integer(int64)||
|&emsp;&emsp;pulse|有无脉冲 0无脉冲 1有脉冲|integer(int32)||
|&emsp;&emsp;sid|工厂日历表主键|integer(int64)||
|&emsp;&emsp;shiftTimeName|班次时间以及日期|string||
|&emsp;&emsp;machineNo|设备编号|string||
|&emsp;&emsp;machineName|设备名称|string||
|&emsp;&emsp;planQty|计划数量|number||
|&emsp;&emsp;productionQty|未完成数量|number||
|&emsp;&emsp;goodQty|良品数量|number||
|&emsp;&emsp;theoreticalQty|理论产出数量|number||
|&emsp;&emsp;perHourOutput|标准时产量|number||
|&emsp;&emsp;badQtyManufacturing|加工不良|number||
|&emsp;&emsp;badQtyIncoming|来料不良|number||
|&emsp;&emsp;produceHours|产出工时|number||
|&emsp;&emsp;machineHours|机器用时|number||
|&emsp;&emsp;peopleHours|人员工时|number||
|&emsp;&emsp;mouldStartTime|开始换模时间|string(date-time)||
|&emsp;&emsp;mouldEndTime|结束换模时间|string(date-time)||
|&emsp;&emsp;startTime|开始加工时间|string(date-time)||
|&emsp;&emsp;operatorList|操作人员|string||
|&emsp;&emsp;mouldList|换模人员|string||
|&emsp;&emsp;timeMouldChange|换模时长|number||
|&emsp;&emsp;actualTimeMouldChange|实际换模时长|number||
|&emsp;&emsp;earnedHours|获得工时|number||
|&emsp;&emsp;compensateHours|奖惩工时|number||
|&emsp;&emsp;materialBatchNo|原材料批次号|string||
|&emsp;&emsp;greenDuration|绿灯时长|number||
|&emsp;&emsp;yellowDuration|黄灯时长|number||
|&emsp;&emsp;redDuration|红灯时长|number||
|&emsp;&emsp;closeDuration|关灯时长|number||
|&emsp;&emsp;andonDuration|安灯时长|number||
|&emsp;&emsp;taskCount|实际模次|integer(int64)||
|&emsp;&emsp;taskActionRemark|备注|string||
|&emsp;&emsp;routingsMaterialNo|工艺路线参考物料编号|string||
|&emsp;&emsp;picUrl|报工图片或地址|string||
|&emsp;&emsp;picType|1、图片 2、视频|integer(int32)||
|&emsp;&emsp;inStockQty|入库数|number||
|&emsp;&emsp;inStockRate|入库率|number||
|&emsp;&emsp;materialQty|原料标识数量|number||
|&emsp;&emsp;weight|布头布尾KG|number||
|&emsp;&emsp;materialUnit|原料标识单位|string||
|&emsp;&emsp;productionBatchNo|生产批号|string||
|&emsp;&emsp;isolationBadQty|隔离不良数|number||
|&emsp;&emsp;knifeWeight|栏刀口料KG|number||
|&emsp;&emsp;materialWeight|原材料重量|number||
|&emsp;&emsp;pieceWeight|产品单片重量|number||
|&emsp;&emsp;scrapWeight|角料重量|number||
|&emsp;&emsp;effectiveDuration|不计考核的异常时长|number||
|&emsp;&emsp;freeTime|休息时长|number||
|&emsp;&emsp;theoreticalDuration|理论产出|number||
|&emsp;&emsp;planCompleteRate|计划达成率|number||
|&emsp;&emsp;standardCompleteRate|标准达成率|number||
|&emsp;&emsp;productionRate|生产效率|number||
|&emsp;&emsp;greenRate|绿灯率|number||
|&emsp;&emsp;goodRate|良品率|number||
|&emsp;&emsp;oeeRate|OEE|number||
|&emsp;&emsp;unitPrice|件工费|number||
|&emsp;&emsp;amount|金额|number||
|&emsp;&emsp;operationCount|作业人数|integer(int32)||
|&emsp;&emsp;workorderPlanQty|工单数量|number||
|&emsp;&emsp;actualMoldCavity|实际使用模穴|number||
|&emsp;&emsp;singleTripQty|标准取数|number||
|&emsp;&emsp;actualSingleTripQty|实际取数|number||
|&emsp;&emsp;singleTripQtyRate|取出率|number||
|&emsp;&emsp;moldCavityRate|模穴率|number||
|&emsp;&emsp;singleTripTime|标准单趟加工时长|number||
|&emsp;&emsp;actualSingleTripTime|实际单趟加工时长|number||
|&emsp;&emsp;workcenterNo|工作中心编码|string||
|&emsp;&emsp;workcenterName|工作中心名称|string||
|&emsp;&emsp;conversionCoefficient|转换系数|number||
|&emsp;&emsp;shiftCapacity|当班标准产能|number||
|&emsp;&emsp;startMouldTime|开始换模时刻|string(date-time)||
|&emsp;&emsp;endMouldTime|结束换模时刻|string(date-time)||
|&emsp;&emsp;planFollowWordNo|计划跟踪号|string||
|&emsp;&emsp;materialLedgerDesc|材料名称|string||
|&emsp;&emsp;materialLedgerSpec|材料规格|string||
|&emsp;&emsp;auxiliaryUnit|辅助单位|string||
|&emsp;&emsp;auxiliaryQty|辅助单位数量|number||
|&emsp;&emsp;coefficient|主辅单位系数|string||
|&emsp;&emsp;supplier|供应商|string||
|&emsp;&emsp;orderQty|订单数量|number||
|&emsp;&emsp;salesorderNo|销单号|string||
|&emsp;&emsp;manOutputRate|人工产出达成率|number||
|&emsp;&emsp;approveStatus|审批状态 0审批中 1审批完成|string||
|&emsp;&emsp;actualPeopleHours|实际人工用时|number||
|&emsp;&emsp;compensateWorkHours|补偿工时|number||
|&emsp;&emsp;compensateNotes|补偿工时原因|string||
|&emsp;&emsp;actualSingleOutputTime|实际单趟产出时长|number||
|&emsp;&emsp;customizationNo|客制代码|string||
|&emsp;&emsp;customerRequirement|客户定制说明|string||
|&emsp;&emsp;userName|报工人员|string||
|&emsp;&emsp;materialLedgerWeight|材料重量|number||
|&emsp;&emsp;procedureRemark|工序备注|string||
|&emsp;&emsp;theoreticalScrapWeight|理论角料重量|number||
|&emsp;&emsp;utilizationRate|产品利用率|number||
|&emsp;&emsp;productSpecificationQtyVOS|品规数量|array|ProductSpecificationQtyVO|
|&emsp;&emsp;&emsp;&emsp;psqId|品规id|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;specificationNo|品规编号|string||
|&emsp;&emsp;&emsp;&emsp;planQty|计划数|number||
|&emsp;&emsp;&emsp;&emsp;completeQty|累计报工数量|number||
|&emsp;&emsp;&emsp;&emsp;goodQty|当前报工数量|number||
|&emsp;&emsp;workorderRemark|工单备注|string||
|&emsp;&emsp;checkQty|检查数量|number||
|&emsp;&emsp;transferCardNo|流转卡号|string||
|&emsp;&emsp;totalCompleteQty|总完成数|number||
|&emsp;&emsp;auxiliaryReport|是否以辅助单位报工 0否 1是(在辅助单位不存在时还是以主单位进行报工)|integer(int32)||
|&emsp;&emsp;secondCoefficient||number||
|&emsp;&emsp;mainCoefficient||number||
|&emsp;&emsp;planWorkTime|计划用时|number||
|&emsp;&emsp;boxQty|箱数|number||
|&emsp;&emsp;errorRemark|异常备注|string||
|&emsp;&emsp;mainBadQty|主单位不良数|number||
|&emsp;&emsp;secondBadQty|辅助单位不良数|number||
|&emsp;&emsp;hasMedia|照片/视频标识筛选|string||
|&emsp;&emsp;chassisNo|底盘号/盘底号|string||
|&emsp;&emsp;rearOutriggerCode|后支腿编码|string||
|&emsp;&emsp;outputRate||number||
|&emsp;&emsp;auxiliaryMetering||number||


**响应示例**:
```javascript
{
	"success": true,
	"code": 1000,
	"message": "success",
	"totalItems": 12,
	"data": [
		{
			"wtid": 0,
			"wtaid": 0,
			"endTime": "",
			"woid": 0,
			"departmentName": "",
			"workorderNo": "",
			"workorderType": "",
			"unit": "",
			"taskNo": "",
			"rpid": 0,
			"procedureNo": "",
			"procedureName": "",
			"mtid": 0,
			"materialNo": "",
			"materialDesc": "",
			"materialSpec": "",
			"mid": 0,
			"pulse": 0,
			"sid": 0,
			"shiftTimeName": "",
			"machineNo": "",
			"machineName": "",
			"planQty": 0,
			"productionQty": 0,
			"goodQty": 0,
			"theoreticalQty": 0,
			"perHourOutput": 0,
			"badQtyManufacturing": 0,
			"badQtyIncoming": 0,
			"produceHours": 0,
			"machineHours": 0,
			"peopleHours": 0,
			"mouldStartTime": "",
			"mouldEndTime": "",
			"startTime": "",
			"operatorList": "",
			"mouldList": "",
			"timeMouldChange": 0,
			"actualTimeMouldChange": 0,
			"earnedHours": 0,
			"compensateHours": 0,
			"materialBatchNo": "",
			"greenDuration": 0,
			"yellowDuration": 0,
			"redDuration": 0,
			"closeDuration": 0,
			"andonDuration": 0,
			"taskCount": 0,
			"taskActionRemark": "",
			"routingsMaterialNo": "",
			"picUrl": "",
			"picType": 0,
			"inStockQty": 0,
			"inStockRate": 0,
			"materialQty": 0,
			"weight": 0,
			"materialUnit": "",
			"productionBatchNo": "",
			"isolationBadQty": 0,
			"knifeWeight": 0,
			"materialWeight": 0,
			"pieceWeight": 0,
			"scrapWeight": 0,
			"effectiveDuration": 0,
			"freeTime": 0,
			"theoreticalDuration": 0,
			"planCompleteRate": 0,
			"standardCompleteRate": 0,
			"productionRate": 0,
			"greenRate": 0,
			"goodRate": 0,
			"oeeRate": 0,
			"unitPrice": 0,
			"amount": 0,
			"operationCount": 0,
			"workorderPlanQty": 0,
			"actualMoldCavity": 0,
			"singleTripQty": 0,
			"actualSingleTripQty": 0,
			"singleTripQtyRate": 0,
			"moldCavityRate": 0,
			"singleTripTime": 0,
			"actualSingleTripTime": 0,
			"workcenterNo": "",
			"workcenterName": "",
			"conversionCoefficient": 0,
			"shiftCapacity": 0,
			"startMouldTime": "",
			"endMouldTime": "",
			"planFollowWordNo": "",
			"materialLedgerDesc": "",
			"materialLedgerSpec": "",
			"auxiliaryUnit": "",
			"auxiliaryQty": 0,
			"coefficient": "",
			"supplier": "",
			"orderQty": 0,
			"salesorderNo": "",
			"manOutputRate": 0,
			"approveStatus": "",
			"actualPeopleHours": 0,
			"compensateWorkHours": 0,
			"compensateNotes": "",
			"actualSingleOutputTime": 0,
			"customizationNo": "",
			"customerRequirement": "",
			"userName": "",
			"materialLedgerWeight": 0,
			"procedureRemark": "",
			"theoreticalScrapWeight": 0,
			"utilizationRate": 0,
			"productSpecificationQtyVOS": [
				{
					"psqId": 0,
					"specificationNo": "",
					"planQty": 0,
					"completeQty": 0,
					"goodQty": 0
				}
			],
			"workorderRemark": "",
			"checkQty": 0,
			"transferCardNo": "",
			"totalCompleteQty": 0,
			"auxiliaryReport": 0,
			"secondCoefficient": 0,
			"mainCoefficient": 0,
			"planWorkTime": 0,
			"boxQty": 0,
			"errorRemark": "",
			"mainBadQty": 0,
			"secondBadQty": 0,
			"hasMedia": "",
			"chassisNo": "",
			"rearOutriggerCode": "",
			"outputRate": 0,
			"auxiliaryMetering": 0
		}
	]
}
```


## 工单修改


**接口地址**:`/lightmesapi/open/workorderController/updateWorkorder`


**请求方式**:`POST`


**请求数据类型**:`application/x-www-form-urlencoded,application/json`


**响应数据类型**:`*/*`


**接口描述**:<p>通过此接口可以修改单个工单的相关信息，工单号团队下不允许重复，已经开始生产的工单，产品编码和客制代码都无法修改，修改完成后会生成一条日志记录修改过的工单相关信息;
单个客户账号调用该接口的每秒请求数（QPS）最大限制为10。</p>



**请求示例**:


```javascript
{
  "woid": 0,
  "workorderNo": "",
  "workorderType": "",
  "urgentLevel": 0,
  "mtid": 0,
  "materialNo": "",
  "materialDesc": "",
  "materialSpec": "",
  "unit": "",
  "startTime": "",
  "endTime": "",
  "planFollowWordNo": "",
  "orderMaster": "",
  "customizationNo": "",
  "customerRequirement": "",
  "remark": "",
  "customerNo": "",
  "routingsMaterialNo": "",
  "sales": "",
  "productSpecification": "",
  "salesorderNo": "",
  "supplier": "",
  "orderQty": 0,
  "materialLedgerDesc": "",
  "materialLedgerSpec": "",
  "startSN": "",
  "endSN": "",
  "receiveQty": 0,
  "arrivalTime": "",
  "purchaseQty": 0,
  "pictureUrl": "",
  "procedureRateConfigDTOS": [
    {
      "procedureNo": "",
      "procedureName": "",
      "conformityRate": 0
    }
  ],
  "workorderExtraInfoList": [
    {
      "seq": 0,
      "fieldName": "",
      "fieldValue": "",
      "isdelete": 0
    }
  ],
  "projectNumber": "",
  "orderNumber": "",
  "customerMaterialName": "",
  "customFields": [
    {
      "fieldCode": "",
      "fieldValue": ""
    }
  ]
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|AccessKeyId|AccessKeyId|header|true|string||
|AccessKeySecret|AccessKeySecret|header|true|string||
|updateWorkorderDTO|UpdateWorkorderDTO|body|true|UpdateWorkorderDTO|UpdateWorkorderDTO|
|&emsp;&emsp;woid|工单id||true|integer(int64)||
|&emsp;&emsp;workorderNo|工单号||true|string||
|&emsp;&emsp;workorderType|工单类型||true|string||
|&emsp;&emsp;urgentLevel|1加急*/2非加急**/3加急***/0非紧急||false|integer(int32)||
|&emsp;&emsp;mtid|物料id||true|integer(int64)||
|&emsp;&emsp;materialNo|产品编码(物料编号)||true|string||
|&emsp;&emsp;materialDesc|产品名称(物料名称)||false|string||
|&emsp;&emsp;materialSpec|规格||false|string||
|&emsp;&emsp;unit|单位||false|string||
|&emsp;&emsp;startTime|预计开工日期||false|string(date-time)||
|&emsp;&emsp;endTime|工单交期||true|string(date-time)||
|&emsp;&emsp;planFollowWordNo|计划跟踪单号||false|string||
|&emsp;&emsp;orderMaster|跟单员||false|string||
|&emsp;&emsp;customizationNo|客制代码||false|string||
|&emsp;&emsp;customerRequirement|客户定制说明||false|string||
|&emsp;&emsp;remark|工单备注||false|string||
|&emsp;&emsp;customerNo|客户代码||false|string||
|&emsp;&emsp;routingsMaterialNo|工艺参考物料||false|string||
|&emsp;&emsp;sales|业务员||false|string||
|&emsp;&emsp;productSpecification|品规数量||false|string||
|&emsp;&emsp;salesorderNo|销售单号||false|string||
|&emsp;&emsp;supplier|供应商||false|string||
|&emsp;&emsp;orderQty|订单数量||false|number||
|&emsp;&emsp;materialLedgerDesc|材料名称||false|string||
|&emsp;&emsp;materialLedgerSpec|材料规格||false|string||
|&emsp;&emsp;startSN|初始序列号||false|string||
|&emsp;&emsp;endSN|结尾序列号||false|string||
|&emsp;&emsp;receiveQty|领料数量||false|number||
|&emsp;&emsp;arrivalTime|要求到料日期||false|string(date-time)||
|&emsp;&emsp;purchaseQty|采购数量||false|number||
|&emsp;&emsp;pictureUrl|图片备注||false|string||
|&emsp;&emsp;procedureRateConfigDTOS|良率||false|array|ProcedureRateConfigDTO|
|&emsp;&emsp;&emsp;&emsp;procedureNo|工序编号||false|string||
|&emsp;&emsp;&emsp;&emsp;procedureName|工序名称||false|string||
|&emsp;&emsp;&emsp;&emsp;conformityRate|良品率||false|number||
|&emsp;&emsp;workorderExtraInfoList|工单额外字段集合||false|array|WorkorderExtraInfoDTO|
|&emsp;&emsp;&emsp;&emsp;seq|序号,排序用(升序)||false|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;fieldName|字段名称||true|string||
|&emsp;&emsp;&emsp;&emsp;fieldValue|字段值||true|string||
|&emsp;&emsp;&emsp;&emsp;isdelete|0未删除 1已删除,默认未删除||false|integer(int32)||
|&emsp;&emsp;projectNumber|项目号||false|string||
|&emsp;&emsp;orderNumber|订单号||false|string||
|&emsp;&emsp;customerMaterialName|客户物料名称||false|string||
|&emsp;&emsp;customFields|自定义字段值列表（fieldCode + fieldValue），传 null 表示不修改自定义字段||false|array|EntityCustomFieldValueItemDTO|
|&emsp;&emsp;&emsp;&emsp;fieldCode|字段英文名（field_code，如 wo_cf_1）||true|string||
|&emsp;&emsp;&emsp;&emsp;fieldValue|字段值||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|出参|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|success|成功与否|boolean||
|code|状态码|integer(int32)|integer(int32)|
|message|消息|string||


**响应示例**:
```javascript
{
	"success": true,
	"code": 1000,
	"message": "success"
}
```


## 工单批量结案


**接口地址**:`/lightmesapi/open/workorderController/workorderClose`


**请求方式**:`POST`


**请求数据类型**:`application/x-www-form-urlencoded,application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "workorderNos": [],
  "tid": 0
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|AccessKeyId|AccessKeyId|header|true|string||
|AccessKeySecret|AccessKeySecret|header|true|string||
|workorderNosDTO|WorkorderNosDTO|body|true|WorkorderNosDTO|WorkorderNosDTO|
|&emsp;&emsp;workorderNos|工单编号集合||false|array|string|
|&emsp;&emsp;tid|||false|integer(int64)||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|出参|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|success|成功与否|boolean||
|code|状态码|integer(int32)|integer(int32)|
|message|消息|string||


**响应示例**:
```javascript
{
	"success": true,
	"code": 1000,
	"message": "success"
}
```


## 工单结案-反结案


**接口地址**:`/lightmesapi/open/workorderController/workorderCloseOrCancel`


**请求方式**:`POST`


**请求数据类型**:`application/x-www-form-urlencoded,application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "workorderNo": "",
  "status": 0,
  "closeRemark": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|AccessKeyId|AccessKeyId|header|true|string||
|AccessKeySecret|AccessKeySecret|header|true|string||
|workorderCloseOrCancelDTO|WorkorderCloseOrCancelDTO|body|true|WorkorderCloseOrCancelDTO|WorkorderCloseOrCancelDTO|
|&emsp;&emsp;workorderNo|工单编号||true|string||
|&emsp;&emsp;status|状态 0取消结案 1结案||true|integer(int32)||
|&emsp;&emsp;closeRemark|结案备注||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|出参|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|success|成功与否|boolean||
|code|状态码|integer(int32)|integer(int32)|
|message|消息|string||


**响应示例**:
```javascript
{
	"success": true,
	"code": 1000,
	"message": "success"
}
```


# 模具导入接口


## 导入模具主数据接口


**接口地址**:`/lightmesapi/open/mouldInfoController/apiImportMould`


**请求方式**:`POST`


**请求数据类型**:`application/x-www-form-urlencoded,application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
[
  {
    "mouldNo": "",
    "mouldName": "",
    "departmentName": "",
    "startUpTime": "",
    "estimateFrequency": 0,
    "warningFrequency": 0,
    "maintainDayCycle": 0,
    "mouldCavity": 0,
    "checkTime": "",
    "warehouseLocation": "",
    "nextMaintainCycle": 0,
    "mouldSpec": "",
    "moduleHole": 0,
    "moduleHeight": "",
    "structure": "",
    "hardness": "",
    "drawingNo": "",
    "customerName": "",
    "qty": "",
    "warehousingTime": "",
    "materialName": "",
    "materialBrand": "",
    "blankShape": "",
    "blankWeight": "",
    "reserveRubber": "",
    "addCondition": "",
    "remarks": "",
    "mouldCavityRemark": "",
    "machingCycle": 0,
    "maintenanceFrequency": 0,
    "moveFrequency": 0,
    "maintainCoefficient": 0,
    "responsibleName": "",
    "dayUseFrequency": 0,
    "responsibleUid": 0,
    "partDescription": "",
    "mouldMaterialDesc": "",
    "factoryMouldNo": "",
    "mouldWeight": "",
    "sku": ""
  }
]
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|AccessKeyId|AccessKeyId|header|true|string||
|AccessKeySecret|AccessKeySecret|header|true|string||
|mouldAPIDTOs|MouldAPIDTO|body|true|array|MouldAPIDTO|
|&emsp;&emsp;mouldNo|模具编号||false|string||
|&emsp;&emsp;mouldName|模具名称||false|string||
|&emsp;&emsp;departmentName|车间名称||false|string||
|&emsp;&emsp;startUpTime|启动时间||false|string(date-time)||
|&emsp;&emsp;estimateFrequency|设计模次||false|integer(int32)||
|&emsp;&emsp;warningFrequency|告警模次||false|integer(int32)||
|&emsp;&emsp;maintainDayCycle|保养天数||false|integer(int32)||
|&emsp;&emsp;mouldCavity|模具穴数||false|integer(int32)||
|&emsp;&emsp;checkTime|验收时间||false|string(date-time)||
|&emsp;&emsp;warehouseLocation|库位||false|string||
|&emsp;&emsp;nextMaintainCycle|保养间隔次数||false|integer(int32)||
|&emsp;&emsp;mouldSpec|模具规格||false|string||
|&emsp;&emsp;moduleHole|模孔||false|number||
|&emsp;&emsp;moduleHeight|模高||false|string||
|&emsp;&emsp;structure|结构||false|string||
|&emsp;&emsp;hardness|硬度||false|string||
|&emsp;&emsp;drawingNo|图号||false|string||
|&emsp;&emsp;customerName|客户名称||false|string||
|&emsp;&emsp;qty|数量||false|string||
|&emsp;&emsp;warehousingTime|入库时间||false|string(date-time)||
|&emsp;&emsp;materialName|胶料名称||false|string||
|&emsp;&emsp;materialBrand|胶料牌号||false|string||
|&emsp;&emsp;blankShape|胶胚形状||false|string||
|&emsp;&emsp;blankWeight|胶胚重量(ROB)||false|string||
|&emsp;&emsp;reserveRubber|备胶明细||false|string||
|&emsp;&emsp;addCondition|二次加硫条件||false|string||
|&emsp;&emsp;remarks|备注||false|string||
|&emsp;&emsp;mouldCavityRemark|模穴备注||false|string||
|&emsp;&emsp;machingCycle|加工周期||false|number||
|&emsp;&emsp;maintenanceFrequency|保养模次||false|integer(int32)||
|&emsp;&emsp;moveFrequency|移模前模次||false|integer(int32)||
|&emsp;&emsp;maintainCoefficient|保养系数||false|number||
|&emsp;&emsp;responsibleName|责任人||false|string||
|&emsp;&emsp;dayUseFrequency|每日使用模次||false|integer(int32)||
|&emsp;&emsp;responsibleUid|责任人id||false|integer(int64)||
|&emsp;&emsp;partDescription|零件描述||false|string||
|&emsp;&emsp;mouldMaterialDesc|产品名称||false|string||
|&emsp;&emsp;factoryMouldNo|本厂模具编号||false|string||
|&emsp;&emsp;mouldWeight|模具吨位||false|string||
|&emsp;&emsp;sku|SKU||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|ResultDataApiReturnVO|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|success|成功与否|boolean||
|code|状态码|integer(int32)|integer(int32)|
|message|消息|string||
|data||ApiReturnVO|ApiReturnVO|
|&emsp;&emsp;successTotal|成功的条数|integer(int32)||
|&emsp;&emsp;errorTotal|失败的条数|integer(int32)||
|&emsp;&emsp;errorList|失败的错误信息|array|string|


**响应示例**:
```javascript
{
	"success": true,
	"code": 1000,
	"message": "success",
	"data": {
		"successTotal": 0,
		"errorTotal": 0,
		"errorList": []
	}
}
```


# 三色灯相关操作文档


## 安灯报表


**接口地址**:`/lightmesapi/open/trilightSummary/andonApiController`


**请求方式**:`POST`


**请求数据类型**:`application/x-www-form-urlencoded,application/json`


**响应数据类型**:`*/*`


**接口描述**:<p>通过此接口可以查询指定时间内的安灯情况。
单个客户账号调用该接口的每秒请求数（QPS）最大限制为10。</p>



**请求示例**:


```javascript
{
  "pageNum": 0,
  "pageSize": 0,
  "did": 0,
  "didList": [],
  "pidList": [],
  "startDate": "",
  "endDate": "",
  "workorderNo": "",
  "materialNo": "",
  "materialDesc": "",
  "materialSpec": "",
  "procedureNo": "",
  "procedureName": "",
  "taskNo": "",
  "ngReason": "",
  "query": "",
  "startTime": "",
  "endTime": "",
  "mid": 0,
  "orderByDTOS": [
    {
      "orderName": "",
      "sort": "",
      "grade": 0
    }
  ],
  "userName": "",
  "machineNo": "",
  "andonTitle": "",
  "statusList": []
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|AccessKeyId|AccessKeyId|header|true|string||
|AccessKeySecret|AccessKeySecret|header|true|string||
|selectAndonDTO|SelectAndonDTO|body|true|SelectAndonDTO|SelectAndonDTO|
|&emsp;&emsp;pageNum|查询页||true|integer(int32)||
|&emsp;&emsp;pageSize|每页条数||true|integer(int32)||
|&emsp;&emsp;did|部门did||false|integer(int64)||
|&emsp;&emsp;didList|部门id集合||false|array|integer(int64)|
|&emsp;&emsp;pidList|产线id||false|array|integer(int64)|
|&emsp;&emsp;startDate|开始时间||true|string(date-time)||
|&emsp;&emsp;endDate|结束时间||true|string(date-time)||
|&emsp;&emsp;workorderNo|工单号||false|string||
|&emsp;&emsp;materialNo|料号/产品编码||false|string||
|&emsp;&emsp;materialDesc|品名||false|string||
|&emsp;&emsp;materialSpec|||false|string||
|&emsp;&emsp;procedureNo|||false|string||
|&emsp;&emsp;procedureName|||false|string||
|&emsp;&emsp;taskNo|生产任务号||false|string||
|&emsp;&emsp;ngReason|不良原因||false|string||
|&emsp;&emsp;query|搜索输入内容||false|string||
|&emsp;&emsp;startTime|要求开工日期开始时间||false|string(date-time)||
|&emsp;&emsp;endTime|要求开工日期结束时间||false|string(date-time)||
|&emsp;&emsp;mid|设备id||false|integer(int64)||
|&emsp;&emsp;orderByDTOS|排序||false|array|OrderByDTO|
|&emsp;&emsp;&emsp;&emsp;orderName|排序字段||false|string||
|&emsp;&emsp;&emsp;&emsp;sort|排序规则||false|string||
|&emsp;&emsp;&emsp;&emsp;grade|等级越大,排序规则也优先||false|integer(int32)||
|&emsp;&emsp;userName|人员姓名||false|string||
|&emsp;&emsp;machineNo|设备编号||false|string||
|&emsp;&emsp;andonTitle|安灯类型||false|string||
|&emsp;&emsp;statusList|状态 0未完成 1已完成||true|array|integer(int32)|


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|ResultQueryAndonRecordFromVO|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|success|成功与否|boolean||
|code|状态码|integer(int32)|integer(int32)|
|message|消息|string||
|totalItems|总条数|integer(int32)|integer(int32)|
|data||array|AndonRecordFromVO|
|&emsp;&emsp;arId|安灯主键id|integer(int64)||
|&emsp;&emsp;machineNo|设备编号|string||
|&emsp;&emsp;createDate|发生时间|string(date-time)||
|&emsp;&emsp;andonTitle|安灯类型|string||
|&emsp;&emsp;receiveDate|响应时间|string(date-time)||
|&emsp;&emsp;receiveTime|响应时长|number||
|&emsp;&emsp;finishDate|处理完成时间|string(date-time)||
|&emsp;&emsp;finishTime|处理时长|number||
|&emsp;&emsp;allTime|总时长|number||
|&emsp;&emsp;submitName|发起人|string||
|&emsp;&emsp;finishName|关闭人|string||
|&emsp;&emsp;mesExplain|处理结果备注|string||
|&emsp;&emsp;remark|其它备注|string||
|&emsp;&emsp;mesUrl|处理结果图片/视频|string||
|&emsp;&emsp;urlType|上传文件类型（1、图片 2、视频）|integer(int32)||
|&emsp;&emsp;finishUrlList|处理结果图片/视频列表|array|UrlAndTypeDTO|
|&emsp;&emsp;&emsp;&emsp;mesUrl|上传图片或视频地址|string||
|&emsp;&emsp;&emsp;&emsp;urlType|上传类型，1表示图片，2表示视频|integer(int32)||
|&emsp;&emsp;note|补充说明|string||
|&emsp;&emsp;supplementUrlList|补充图片/视频列表|array|UrlAndTypeDTO|
|&emsp;&emsp;&emsp;&emsp;mesUrl|上传图片或视频地址|string||
|&emsp;&emsp;&emsp;&emsp;urlType|上传类型，1表示图片，2表示视频|integer(int32)||
|&emsp;&emsp;noteUrl|补充图片/视频|string||
|&emsp;&emsp;noteType|补充文件类型|integer(int32)||
|&emsp;&emsp;userNames|处理人姓名|array|string|
|&emsp;&emsp;taskRemark|工单备注|string||
|&emsp;&emsp;andonStatus|请求状态 ：1：创建等待接手，2：接手人员接手，3：接手人完成|integer(int32)||
|&emsp;&emsp;standardDuration|标准安灯时长|number||
|&emsp;&emsp;standardResponseTime|标准响应时长|number||
|&emsp;&emsp;standardProcessingTime|标准处理时长|number||
|&emsp;&emsp;responseTimeout|响应超时|number||
|&emsp;&emsp;processingTimeout|处理超时|number||
|&emsp;&emsp;andonRecordLogList|安灯日志|array|AndonRecordLog|
|&emsp;&emsp;&emsp;&emsp;arlId||integer(int64)||
|&emsp;&emsp;&emsp;&emsp;remark||string||
|&emsp;&emsp;&emsp;&emsp;tid||integer(int64)||
|&emsp;&emsp;&emsp;&emsp;andonRecordId||integer(int64)||
|&emsp;&emsp;&emsp;&emsp;type||integer(int32)||
|&emsp;&emsp;&emsp;&emsp;changer||integer(int64)||
|&emsp;&emsp;&emsp;&emsp;operateRecord||string||
|&emsp;&emsp;&emsp;&emsp;mesUrl||string||
|&emsp;&emsp;&emsp;&emsp;urlType||integer(int32)||
|&emsp;&emsp;&emsp;&emsp;mesExplain||string||
|&emsp;&emsp;&emsp;&emsp;createTime||string(date-time)||
|&emsp;&emsp;&emsp;&emsp;updateTime||string(date-time)||
|&emsp;&emsp;&emsp;&emsp;isdelete||integer(int32)||
|&emsp;&emsp;canPrintOa|是否可以打印OA流 0否 1是|integer(int32)||


**响应示例**:
```javascript
{
	"success": true,
	"code": 1000,
	"message": "success",
	"totalItems": 12,
	"data": [
		{
			"arId": 0,
			"machineNo": "",
			"createDate": "",
			"andonTitle": "",
			"receiveDate": "",
			"receiveTime": 0,
			"finishDate": "",
			"finishTime": 0,
			"allTime": 0,
			"submitName": "",
			"finishName": "",
			"mesExplain": "",
			"remark": "",
			"mesUrl": "",
			"urlType": 0,
			"finishUrlList": [
				{
					"mesUrl": "",
					"urlType": 0
				}
			],
			"note": "",
			"supplementUrlList": [
				{
					"mesUrl": "",
					"urlType": 0
				}
			],
			"noteUrl": "",
			"noteType": 0,
			"userNames": [],
			"taskRemark": "",
			"andonStatus": 0,
			"standardDuration": 0,
			"standardResponseTime": 0,
			"standardProcessingTime": 0,
			"responseTimeout": 0,
			"processingTimeout": 0,
			"andonRecordLogList": [
				{
					"arlId": 0,
					"remark": "",
					"tid": 0,
					"andonRecordId": 0,
					"type": 0,
					"changer": 0,
					"operateRecord": "",
					"mesUrl": "",
					"urlType": 0,
					"mesExplain": "",
					"createTime": "",
					"updateTime": "",
					"isdelete": 0
				}
			],
			"canPrintOa": 0
		}
	]
}
```


## 获取三色灯指定时间段内的脉冲计数详情


**接口地址**:`/lightmesapi/open/trilightSummary/getTimecountMessagesByTimeSim`


**请求方式**:`POST`


**请求数据类型**:`application/x-www-form-urlencoded,application/json`


**响应数据类型**:`*/*`


**接口描述**:<p>通过此接口可以获取指定三色灯指定时间段内的脉冲计数详情</p>



**请求示例**:


```javascript
{
  "sim": "",
  "startTime": "",
  "endTime": "",
  "date": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|AccessKeyId|AccessKeyId|header|true|string||
|AccessKeySecret|AccessKeySecret|header|true|string||
|simAndDurationTimesDTO|SimAndDurationTimesDTO|body|true|SimAndDurationTimesDTO|SimAndDurationTimesDTO|
|&emsp;&emsp;sim|三色灯sim号||true|string||
|&emsp;&emsp;startTime|查询开始时间yyyy-MM-dd HH:mm:ss||true|string(date-time)||
|&emsp;&emsp;endTime|查询结束时间yyyy-MM-dd HH:mm:ss||true|string(date-time)||
|&emsp;&emsp;date|查询的指定日期格式(yyyy-MM-dd)||false|string(date-time)||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|ResultDataTrilightCountMessageVO|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|success|成功与否|boolean||
|code|状态码|integer(int32)|integer(int32)|
|message|消息|string||
|data||TrilightCountMessageVO|TrilightCountMessageVO|
|&emsp;&emsp;sim|SIM卡|string||
|&emsp;&emsp;countMessages|三色灯计数详情|array|CountMessage|
|&emsp;&emsp;&emsp;&emsp;count|计数详细，该List有10条数据，每条代表三秒内的计数总和|array|integer|
|&emsp;&emsp;&emsp;&emsp;duration|脉冲计数持续时间|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;endtime|当前脉冲计数结束时间戳|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;sno|三色灯序号|integer(int32)||


**响应示例**:
```javascript
{
	"success": true,
	"code": 1000,
	"message": "success",
	"data": {
		"sim": "",
		"countMessages": [
			{
				"count": [],
				"duration": 0,
				"endtime": 0,
				"sno": 0
			}
		]
	}
}
```


## 获取三色灯指定时间段内的脉冲计数之和


**接口地址**:`/lightmesapi/open/trilightSummary/getTrilightCountByTimeSim`


**请求方式**:`POST`


**请求数据类型**:`application/x-www-form-urlencoded,application/json`


**响应数据类型**:`*/*`


**接口描述**:<p>通过此接口可以获取指定三色灯指定时间段内的脉冲计数之和</p>



**请求示例**:


```javascript
{
  "sim": "",
  "startTime": "",
  "endTime": "",
  "date": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|AccessKeyId|AccessKeyId|header|true|string||
|AccessKeySecret|AccessKeySecret|header|true|string||
|simAndDurationTimesDTO|SimAndDurationTimesDTO|body|true|SimAndDurationTimesDTO|SimAndDurationTimesDTO|
|&emsp;&emsp;sim|三色灯sim号||true|string||
|&emsp;&emsp;startTime|查询开始时间yyyy-MM-dd HH:mm:ss||true|string(date-time)||
|&emsp;&emsp;endTime|查询结束时间yyyy-MM-dd HH:mm:ss||true|string(date-time)||
|&emsp;&emsp;date|查询的指定日期格式(yyyy-MM-dd)||false|string(date-time)||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|ResultDataTrilightCountVO|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|success|成功与否|boolean||
|code|状态码|integer(int32)|integer(int32)|
|message|消息|string||
|data||TrilightCountVO|TrilightCountVO|
|&emsp;&emsp;sim|SIM卡|string||
|&emsp;&emsp;countSize|三色灯计数次数|integer(int64)||


**响应示例**:
```javascript
{
	"success": true,
	"code": 1000,
	"message": "success",
	"data": {
		"sim": "",
		"countSize": 0
	}
}
```


## 通过sim卡号查询对应三色灯状态。


**接口地址**:`/lightmesapi/open/trilightSummary/getTrilightCurrentColor`


**请求方式**:`POST`


**请求数据类型**:`application/x-www-form-urlencoded,application/json`


**响应数据类型**:`*/*`


**接口描述**:<p>通过sim卡号查询对应三色灯状态。
单个客户账号调用该接口的每秒请求数（QPS）最大限制为10。</p>



**请求示例**:


```javascript
{
  "sim": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|AccessKeyId|AccessKeyId|header|true|string||
|AccessKeySecret|AccessKeySecret|header|true|string||
|getTrilightCurrentColorDTO|GetTrilightCurrentColorDTO|body|true|GetTrilightCurrentColorDTO|GetTrilightCurrentColorDTO|
|&emsp;&emsp;sim|三色灯sim||true|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|ResultDataTrilightApiVO|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|success|成功与否|boolean||
|code|状态码|integer(int32)|integer(int32)|
|message|消息|string||
|data||TrilightApiVO|TrilightApiVO|
|&emsp;&emsp;sim|当前sim卡号|string||
|&emsp;&emsp;currentState|三色灯状态码：001-绿灯，010-黄灯，100-红灯，000-关灯|string||
|&emsp;&emsp;updateDate|上次状态修改时间|string(date-time)||
|&emsp;&emsp;onLineStatus|当前是否在线|boolean||


**响应示例**:
```javascript
{
	"success": true,
	"code": 1000,
	"message": "success",
	"data": {
		"sim": "",
		"currentState": "",
		"updateDate": "",
		"onLineStatus": true
	}
}
```


## 批量获取三色灯状态


**接口地址**:`/lightmesapi/open/trilightSummary/getTrilightCurrentColorList`


**请求方式**:`POST`


**请求数据类型**:`application/x-www-form-urlencoded,application/json`


**响应数据类型**:`*/*`


**接口描述**:<p>通过sim卡号集合批量获取三色灯状态。
单个客户账号调用该接口的每秒请求数（QPS）最大限制为10。</p>



**请求示例**:


```javascript
{
  "simList": []
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|AccessKeyId|AccessKeyId|header|true|string||
|AccessKeySecret|AccessKeySecret|header|true|string||
|simListDTO|SimListDTO|body|true|SimListDTO|SimListDTO|
|&emsp;&emsp;simList|三色灯sim号||true|array|string|


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|ResultQueryTrilightApiVO|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|success|成功与否|boolean||
|code|状态码|integer(int32)|integer(int32)|
|message|消息|string||
|totalItems|总条数|integer(int32)|integer(int32)|
|data||array|TrilightApiVO|
|&emsp;&emsp;sim|当前sim卡号|string||
|&emsp;&emsp;currentState|三色灯状态码：001-绿灯，010-黄灯，100-红灯，000-关灯|string||
|&emsp;&emsp;updateDate|上次状态修改时间|string(date-time)||
|&emsp;&emsp;onLineStatus|当前是否在线|boolean||


**响应示例**:
```javascript
{
	"success": true,
	"code": 1000,
	"message": "success",
	"totalItems": 12,
	"data": [
		{
			"sim": "",
			"currentState": "",
			"updateDate": "",
			"onLineStatus": true
		}
	]
}
```


## 三色灯指定时间段颜色汇总


**接口地址**:`/lightmesapi/open/trilightSummary/getTrilightEfficiencyDurationTime`


**请求方式**:`POST`


**请求数据类型**:`application/x-www-form-urlencoded,application/json`


**响应数据类型**:`*/*`


**接口描述**:<p>三色灯指定时间段颜色汇总。
单个客户账号调用该接口的每秒请求数（QPS）最大限制为10。</p>



**请求示例**:


```javascript
{
  "sim": "",
  "startTime": "",
  "endTime": "",
  "date": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|AccessKeyId|AccessKeyId|header|true|string||
|AccessKeySecret|AccessKeySecret|header|true|string||
|simAndDurationTimesDTO|SimAndDurationTimesDTO|body|true|SimAndDurationTimesDTO|SimAndDurationTimesDTO|
|&emsp;&emsp;sim|三色灯sim号||true|string||
|&emsp;&emsp;startTime|查询开始时间yyyy-MM-dd HH:mm:ss||true|string(date-time)||
|&emsp;&emsp;endTime|查询结束时间yyyy-MM-dd HH:mm:ss||true|string(date-time)||
|&emsp;&emsp;date|查询的指定日期格式(yyyy-MM-dd)||false|string(date-time)||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|ResultDataTrilightEfficiencyVO|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|success|成功与否|boolean||
|code|状态码|integer(int32)|integer(int32)|
|message|消息|string||
|data||TrilightEfficiencyVO|TrilightEfficiencyVO|
|&emsp;&emsp;sim|设备主键|string||
|&emsp;&emsp;redTime|红灯时长,单位为秒|integer(int64)||
|&emsp;&emsp;greenTime|绿灯时长,单位为秒|integer(int64)||
|&emsp;&emsp;yellowTime|黄灯时长,单位为秒|integer(int64)||
|&emsp;&emsp;closeTime|关灯时长,单位为秒|integer(int64)||


**响应示例**:
```javascript
{
	"success": true,
	"code": 1000,
	"message": "success",
	"data": {
		"sim": "",
		"redTime": 0,
		"greenTime": 0,
		"yellowTime": 0,
		"closeTime": 0
	}
}
```


## 指定日期一天颜色汇总


**接口地址**:`/lightmesapi/open/trilightSummary/getTrilightEfficiencyOneDay`


**请求方式**:`POST`


**请求数据类型**:`application/x-www-form-urlencoded,application/json`


**响应数据类型**:`*/*`


**接口描述**:<p>查询某一天指定三色灯的颜色变化信息。
单个客户账号调用该接口的每秒请求数（QPS）最大限制为10。</p>



**请求示例**:


```javascript
{
  "sim": "",
  "startTime": "",
  "endTime": "",
  "date": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|AccessKeyId|AccessKeyId|header|true|string||
|AccessKeySecret|AccessKeySecret|header|true|string||
|getTrilightEfficiencyOneDayDTO|GetTrilightEfficiencyOneDayDTO|body|true|GetTrilightEfficiencyOneDayDTO|GetTrilightEfficiencyOneDayDTO|
|&emsp;&emsp;sim|三色灯sim号||true|string||
|&emsp;&emsp;startTime|查询开始时间yyyy-MM-dd HH:mm:ss||false|string(date-time)||
|&emsp;&emsp;endTime|查询结束时间yyyy-MM-dd HH:mm:ss||false|string(date-time)||
|&emsp;&emsp;date|查询的指定日期格式(yyyy-MM-dd)||true|string(date-time)||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|ResultDataTrilightEfficiencyVO|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|success|成功与否|boolean||
|code|状态码|integer(int32)|integer(int32)|
|message|消息|string||
|data||TrilightEfficiencyVO|TrilightEfficiencyVO|
|&emsp;&emsp;sim|设备主键|string||
|&emsp;&emsp;redTime|红灯时长,单位为秒|integer(int64)||
|&emsp;&emsp;greenTime|绿灯时长,单位为秒|integer(int64)||
|&emsp;&emsp;yellowTime|黄灯时长,单位为秒|integer(int64)||
|&emsp;&emsp;closeTime|关灯时长,单位为秒|integer(int64)||


**响应示例**:
```javascript
{
	"success": true,
	"code": 1000,
	"message": "success",
	"data": {
		"sim": "",
		"redTime": 0,
		"greenTime": 0,
		"yellowTime": 0,
		"closeTime": 0
	}
}
```


## 查询指定时间段三色灯的颜色变化信息


**接口地址**:`/lightmesapi/open/trilightSummary/getTrilightSummaryDurationTime`


**请求方式**:`POST`


**请求数据类型**:`application/x-www-form-urlencoded,application/json`


**响应数据类型**:`*/*`


**接口描述**:<p>查询某一天指定三色灯的颜色变化信息。
单个客户账号调用该接口的每秒请求数（QPS）最大限制为10。</p>



**请求示例**:


```javascript
{
  "sim": "",
  "startTime": "",
  "endTime": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|AccessKeyId|AccessKeyId|header|true|string||
|AccessKeySecret|AccessKeySecret|header|true|string||
|getTrilightSummaryDurationTimeDTO|GetTrilightSummaryDurationTimeDTO|body|true|GetTrilightSummaryDurationTimeDTO|GetTrilightSummaryDurationTimeDTO|
|&emsp;&emsp;sim|三色灯sim号||true|string||
|&emsp;&emsp;startTime|查询开始时间yyyy-MM-dd HH:mm:ss||true|string(date-time)||
|&emsp;&emsp;endTime|查询结束时间yyyy-MM-dd HH:mm:ss||true|string(date-time)||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|ResultQueryTrilightDurationDetailVO|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|success|成功与否|boolean||
|code|状态码|integer(int32)|integer(int32)|
|message|消息|string||
|totalItems|总条数|integer(int32)|integer(int32)|
|data||array|TrilightDurationDetailVO|
|&emsp;&emsp;startTime|当前三色灯状态开始时间|string(date-time)||
|&emsp;&emsp;endTime|当前三色灯状态结束时间|string(date-time)||
|&emsp;&emsp;color|三色灯状态码：001-绿灯，010-黄灯，100-红灯，000-关灯|string||


**响应示例**:
```javascript
{
	"success": true,
	"code": 1000,
	"message": "success",
	"totalItems": 12,
	"data": [
		{
			"startTime": "",
			"endTime": "",
			"color": ""
		}
	]
}
```


## 控制三色灯蓝灯


**接口地址**:`/lightmesapi/open/trilightSummary/releaseAndonHandleApi`


**请求方式**:`POST`


**请求数据类型**:`application/x-www-form-urlencoded,application/json`


**响应数据类型**:`*/*`


**接口描述**:<p>通过此接口可以控制指定三色灯蓝灯的快闪、慢闪、常亮和关闭蓝灯</p>



**请求示例**:


```javascript
{
  "sim": "",
  "flickers": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|AccessKeyId|AccessKeyId|header|true|string||
|AccessKeySecret|AccessKeySecret|header|true|string||
|blueControlParam|BlueControlParam|body|true|BlueControlParam|BlueControlParam|
|&emsp;&emsp;sim|三色灯sim号||true|string||
|&emsp;&emsp;flickers|三色灯蓝灯状态 0关闭 1常亮 2、慢闪 3、快闪||true|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|出参|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|success|成功与否|boolean||
|code|状态码|integer(int32)|integer(int32)|
|message|消息|string||


**响应示例**:
```javascript
{
	"success": true,
	"code": 1000,
	"message": "success"
}
```


## 控制反控灯颜色。


**接口地址**:`/lightmesapi/open/trilightSummary/reverseLightControlApi`


**请求方式**:`POST`


**请求数据类型**:`application/x-www-form-urlencoded,application/json`


**响应数据类型**:`*/*`


**接口描述**:<p>控制反控灯颜色。
单个客户账号调用该接口的每秒请求数（QPS）最大限制为10。</p>



**请求示例**:


```javascript
{
  "sim": "",
  "color": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|AccessKeyId|AccessKeyId|header|true|string||
|AccessKeySecret|AccessKeySecret|header|true|string||
|reverseLightControlApiDTO|ReverseLightControlApiDTO|body|true|ReverseLightControlApiDTO|ReverseLightControlApiDTO|
|&emsp;&emsp;sim|三色灯sim号||true|string||
|&emsp;&emsp;color|三色灯状态码：001-绿灯，010-黄灯，100-红灯，000-关灯||true|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|出参|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|success|成功与否|boolean||
|code|状态码|integer(int32)|integer(int32)|
|message|消息|string||


**响应示例**:
```javascript
{
	"success": true,
	"code": 1000,
	"message": "success"
}
```


## 设备OEE报表


**接口地址**:`/lightmesapi/open/trilightSummary/selectOeeReport`


**请求方式**:`POST`


**请求数据类型**:`application/x-www-form-urlencoded,application/json`


**响应数据类型**:`*/*`


**接口描述**:<p>通过此接口可以查询对应团队指定时间段的设备OEE信息。
单个客户账号调用该接口的每秒请求数（QPS）最大限制为10。</p>



**请求示例**:


```javascript
{
  "pageNum": 0,
  "pageSize": 0,
  "startDate": "",
  "endDate": "",
  "shiftName": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|AccessKeyId|AccessKeyId|header|true|string||
|AccessKeySecret|AccessKeySecret|header|true|string||
|apiOeeReportDTO|ApiOeeReportDTO|body|true|ApiOeeReportDTO|ApiOeeReportDTO|
|&emsp;&emsp;pageNum|查询页||true|integer(int32)||
|&emsp;&emsp;pageSize|每页条数||true|integer(int32)||
|&emsp;&emsp;startDate|日期（yyyy-MM-dd）||true|string||
|&emsp;&emsp;endDate|日期（yyyy-MM-dd）||true|string||
|&emsp;&emsp;shiftName|班次名称（与MES系统设置的班次相同，不填查询所有班次）||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|ResultQueryOeeReportVO|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|success|成功与否|boolean||
|code|状态码|integer(int32)|integer(int32)|
|message|消息|string||
|totalItems|总条数|integer(int32)|integer(int32)|
|data||array|OeeReportVO|
|&emsp;&emsp;mid|设备id|integer(int64)||
|&emsp;&emsp;departmentName|车间/产线|string||
|&emsp;&emsp;machineNo|设备编号|string||
|&emsp;&emsp;machineName|设备名称|string||
|&emsp;&emsp;simDate|记录日期|string(date-time)||
|&emsp;&emsp;shiftName|班次名称|string||
|&emsp;&emsp;startTime|班次上班时间|string(date-time)||
|&emsp;&emsp;endTime|班次下班时间|string(date-time)||
|&emsp;&emsp;redTime|红灯时长,单位为小时|number||
|&emsp;&emsp;greenTime|绿灯时长,单位为小时|number||
|&emsp;&emsp;yellowTime|黄灯时长,单位为小时|number||
|&emsp;&emsp;closeTime|关灯时长,单位为小时|number||
|&emsp;&emsp;greenTotalTime|总绿灯时长,单位小时|number||
|&emsp;&emsp;redRate|红灯率|number||
|&emsp;&emsp;greenRate|绿灯率|number||
|&emsp;&emsp;yellowRate|黄灯率|number||
|&emsp;&emsp;closeRate|关灯率|number||
|&emsp;&emsp;userName|当班人员|string||
|&emsp;&emsp;greenCompensation|绿灯补偿|number||
|&emsp;&emsp;waitCount|等待次数|integer(int64)||
|&emsp;&emsp;faultCount|故障次数|integer(int64)||
|&emsp;&emsp;actualRate|实动率|number||
|&emsp;&emsp;goodQty|报工数量|number||
|&emsp;&emsp;effectiveYellowTime|有效黄灯,单位小时|number||
|&emsp;&emsp;effectiveGreenRate|有效绿灯率|number||
|&emsp;&emsp;actualYellowRate|实际黄灯率|number||
|&emsp;&emsp;performanceRate|设备性能表现指数|number||
|&emsp;&emsp;oeeRate|设备性能表现OEE|number||
|&emsp;&emsp;stopTime|停用时长,单位小时|number||
|&emsp;&emsp;stopGreen|停用绿灯时长|number||
|&emsp;&emsp;stopFree|停用休息时长|number||
|&emsp;&emsp;runOeeRate|设备运行OEE|number||
|&emsp;&emsp;standardRate|标准利用率|number||
|&emsp;&emsp;andonTime|装夹时长,单位小时|number||
|&emsp;&emsp;andonRate|装夹率|number||
|&emsp;&emsp;oeeUserVOS|当班人员明细|array|OeeUserVO|
|&emsp;&emsp;&emsp;&emsp;uid|用户id|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;userName|姓名|string||
|&emsp;&emsp;&emsp;&emsp;startTime|开始时间|string(date-time)||
|&emsp;&emsp;&emsp;&emsp;endTime|结束时间|string(date-time)||
|&emsp;&emsp;redHour|红灯时长(广濑)|number||
|&emsp;&emsp;greenHour|绿灯时长(广濑)|number||
|&emsp;&emsp;yellowHour|黄灯时长(广濑)|number||
|&emsp;&emsp;closeHour|关灯时长(广濑)|number||
|&emsp;&emsp;greenTotalHour|总绿灯时长(广濑)|number||
|&emsp;&emsp;greenCompensationHour|绿灯补偿(广濑)|number||
|&emsp;&emsp;effectiveYellowHour|有效黄灯(广濑)|number||
|&emsp;&emsp;stopHour|停用时长(广濑)|number||
|&emsp;&emsp;andonHour|装夹时长(广濑)|number||
|&emsp;&emsp;onlineTime|在线时间|number||
|&emsp;&emsp;shiftGreenRate|班次绿灯率|number||
|&emsp;&emsp;shiftGreenTime|班次绿灯时长|number||


**响应示例**:
```javascript
{
	"success": true,
	"code": 1000,
	"message": "success",
	"totalItems": 12,
	"data": [
		{
			"mid": 0,
			"departmentName": "",
			"machineNo": "",
			"machineName": "",
			"simDate": "",
			"shiftName": "",
			"startTime": "",
			"endTime": "",
			"redTime": 0,
			"greenTime": 0,
			"yellowTime": 0,
			"closeTime": 0,
			"greenTotalTime": 0,
			"redRate": 0,
			"greenRate": 0,
			"yellowRate": 0,
			"closeRate": 0,
			"userName": "",
			"greenCompensation": 0,
			"waitCount": 0,
			"faultCount": 0,
			"actualRate": 0,
			"goodQty": 0,
			"effectiveYellowTime": 0,
			"effectiveGreenRate": 0,
			"actualYellowRate": 0,
			"performanceRate": 0,
			"oeeRate": 0,
			"stopTime": 0,
			"stopGreen": 0,
			"stopFree": 0,
			"runOeeRate": 0,
			"standardRate": 0,
			"andonTime": 0,
			"andonRate": 0,
			"oeeUserVOS": [
				{
					"uid": 0,
					"userName": "",
					"startTime": "",
					"endTime": ""
				}
			],
			"redHour": 0,
			"greenHour": 0,
			"yellowHour": 0,
			"closeHour": 0,
			"greenTotalHour": 0,
			"greenCompensationHour": 0,
			"effectiveYellowHour": 0,
			"stopHour": 0,
			"andonHour": 0,
			"onlineTime": 0,
			"shiftGreenRate": 0,
			"shiftGreenTime": 0
		}
	]
}
```


# 设备相关操作文档


## 查询团队下设备数量。


**接口地址**:`/lightmesapi/open/machine/getMachineCount`


**请求方式**:`POST`


**请求数据类型**:`application/x-www-form-urlencoded,application/json`


**响应数据类型**:`*/*`


**接口描述**:<p>单个客户账号调用该接口的每秒请求数（QPS）最大限制为10。</p>



**请求示例**:


```javascript
{
  "tid": 0,
  "machineNo": "",
  "machineName": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|AccessKeyId|AccessKeyId|header|true|string||
|AccessKeySecret|AccessKeySecret|header|true|string||
|getMachineCount|GetMachineCount|body|true|GetMachineCount|GetMachineCount|
|&emsp;&emsp;tid|团队id||false|integer(int64)||
|&emsp;&emsp;machineNo|设备编码||false|string||
|&emsp;&emsp;machineName|设备名称||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|ResultDataInteger|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|success|成功与否|boolean||
|code|状态码|integer(int32)|integer(int32)|
|message|消息|string||
|data||integer(int32)|integer(int32)|


**响应示例**:
```javascript
{
	"success": true,
	"code": 1000,
	"message": "success",
	"data": 0
}
```


## 通过mid或者sim查询设备详情


**接口地址**:`/lightmesapi/open/machine/getMachineDetailById`


**请求方式**:`POST`


**请求数据类型**:`application/x-www-form-urlencoded,application/json`


**响应数据类型**:`*/*`


**接口描述**:<p>通过此接口可以通过设备的mid查询设备的详情，或者通过三色灯sim查询绑定的设备详情。
单个客户账号调用该接口的每秒请求数（QPS）最大限制为10。</p>



**请求示例**:


```javascript
{
  "tid": 0,
  "mid": 0,
  "sim": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|AccessKeyId|AccessKeyId|header|true|string||
|AccessKeySecret|AccessKeySecret|header|true|string||
|midAndSimDTO|MidAndSimDTO|body|true|MidAndSimDTO|MidAndSimDTO|
|&emsp;&emsp;tid|团队id||false|integer(int64)||
|&emsp;&emsp;mid|设备id（与sim任选一个查询）||true|integer(int64)||
|&emsp;&emsp;sim|三色灯sim号（与mid任选一个查询）||true|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|ResultDataApiMachineDetailVO|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|success|成功与否|boolean||
|code|状态码|integer(int32)|integer(int32)|
|message|消息|string||
|data||ApiMachineDetailVO|ApiMachineDetailVO|
|&emsp;&emsp;mid|设备主键|integer(int64)||
|&emsp;&emsp;machineNo|设备编码|string||
|&emsp;&emsp;machineName|设备名称|string||
|&emsp;&emsp;sim|三色灯sim|string||
|&emsp;&emsp;status|设备状态,1表示启用，0表示未启用|integer(int32)||
|&emsp;&emsp;machineBrand|设备品牌|string||
|&emsp;&emsp;machineModel|设备型号|string||
|&emsp;&emsp;machineFunction|概要|string||
|&emsp;&emsp;machineImage|设备图片|string||
|&emsp;&emsp;serialNumber|序列号|string||
|&emsp;&emsp;fixedAssetsCode|固定资产编码|string||
|&emsp;&emsp;supplier|供应商|string||
|&emsp;&emsp;manufacturer|制造商|string||
|&emsp;&emsp;productionDate|出厂日期|string(date-time)||
|&emsp;&emsp;receiveDate|安装验收日期|string(date-time)||
|&emsp;&emsp;firstDate|启用日期|string(date-time)||
|&emsp;&emsp;documents|设备档案|string||
|&emsp;&emsp;useTime|使用时间|string||
|&emsp;&emsp;departmentName|车间/产线|string||


**响应示例**:
```javascript
{
	"success": true,
	"code": 1000,
	"message": "success",
	"data": {
		"mid": 0,
		"machineNo": "",
		"machineName": "",
		"sim": "",
		"status": 0,
		"machineBrand": "",
		"machineModel": "",
		"machineFunction": "",
		"machineImage": "",
		"serialNumber": "",
		"fixedAssetsCode": "",
		"supplier": "",
		"manufacturer": "",
		"productionDate": "",
		"receiveDate": "",
		"firstDate": "",
		"documents": "",
		"useTime": "",
		"departmentName": ""
	}
}
```


## 查询团队下的设备信息


**接口地址**:`/lightmesapi/open/machine/getMachineList`


**请求方式**:`POST`


**请求数据类型**:`application/x-www-form-urlencoded,application/json`


**响应数据类型**:`*/*`


**接口描述**:<p>批量查询团队下设备信息。
单个客户账号调用该接口的每秒请求数（QPS）最大限制为10。</p>



**请求示例**:


```javascript
{
  "pageNum": 0,
  "pageSize": 0,
  "tid": 0,
  "machineNo": "",
  "machineName": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|AccessKeyId|AccessKeyId|header|true|string||
|AccessKeySecret|AccessKeySecret|header|true|string||
|machineApiDTO|MachineApiDTO|body|true|MachineApiDTO|MachineApiDTO|
|&emsp;&emsp;pageNum|查询页||true|integer(int32)||
|&emsp;&emsp;pageSize|每页条数||true|integer(int32)||
|&emsp;&emsp;tid|团队id||false|integer(int64)||
|&emsp;&emsp;machineNo|设备编码||false|string||
|&emsp;&emsp;machineName|设备名称||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|ResultQueryApiMachineVO|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|success|成功与否|boolean||
|code|状态码|integer(int32)|integer(int32)|
|message|消息|string||
|totalItems|总条数|integer(int32)|integer(int32)|
|data||array|ApiMachineVO|
|&emsp;&emsp;mid|设备主键|integer(int64)||
|&emsp;&emsp;machineNo|设备编码|string||
|&emsp;&emsp;machineName|设备名称|string||
|&emsp;&emsp;sim|三色灯sim|string||
|&emsp;&emsp;status|设备状态,1表示启用，0表示未启用|integer(int32)||
|&emsp;&emsp;departmentName|车间/产线|string||


**响应示例**:
```javascript
{
	"success": true,
	"code": 1000,
	"message": "success",
	"totalItems": 12,
	"data": [
		{
			"mid": 0,
			"machineNo": "",
			"machineName": "",
			"sim": "",
			"status": 0,
			"departmentName": ""
		}
	]
}
```


# 实体自定义字段定义相关操作文档


## 批量删除自定义字段定义


**接口地址**:`/lightmesapi/open/entityCustomFieldDefController/deleteDef`


**请求方式**:`POST`


**请求数据类型**:`application/x-www-form-urlencoded,application/json`


**响应数据类型**:`*/*`


**接口描述**:<p>通过 ecfdIds 批量逻辑删除自定义字段定义。
单个客户账号调用该接口的每秒请求数（QPS）最大限制为10。</p>



**请求示例**:


```javascript
{
  "ecfdIds": []
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|AccessKeyId|AccessKeyId|header|true|string||
|AccessKeySecret|AccessKeySecret|header|true|string||
|entityCustomFieldDefDeleteDTO|EntityCustomFieldDefDeleteDTO|body|true|EntityCustomFieldDefDeleteDTO|EntityCustomFieldDefDeleteDTO|
|&emsp;&emsp;ecfdIds|字段定义主键列表||true|array|integer(int64)|


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|出参|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|success|成功与否|boolean||
|code|状态码|integer(int32)|integer(int32)|
|message|消息|string||


**响应示例**:
```javascript
{
	"success": true,
	"code": 1000,
	"message": "success"
}
```


## 查询自定义字段定义列表


**接口地址**:`/lightmesapi/open/entityCustomFieldDefController/listDefs`


**请求方式**:`POST`


**请求数据类型**:`application/x-www-form-urlencoded,application/json`


**响应数据类型**:`*/*`


**接口描述**:<p>通过此接口可查询指定实体类型下的自定义字段定义列表。
实体类型可选值：WORKORDER（工单）、WORKORDER_PROCEDURE（工单工序）。
单个客户账号调用该接口的每秒请求数（QPS）最大限制为10。</p>



**请求示例**:


```javascript
{
  "entityType": "",
  "enabledOnly": 0,
  "required": 0
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|AccessKeyId|AccessKeyId|header|true|string||
|AccessKeySecret|AccessKeySecret|header|true|string||
|entityCustomFieldDefQueryDTO|EntityCustomFieldDefQueryDTO|body|true|EntityCustomFieldDefQueryDTO|EntityCustomFieldDefQueryDTO|
|&emsp;&emsp;entityType|实体类型，如 WORKORDER||true|string||
|&emsp;&emsp;enabledOnly|仅启用 1是 0否||false|integer(int32)||
|&emsp;&emsp;required|必填 1是 0否||false|integer(int32)||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|ResultDataListEntityCustomFieldDefVO|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|success|成功与否|boolean||
|code|状态码|integer(int32)|integer(int32)|
|message|消息|string||
|data||array|EntityCustomFieldDefVO|
|&emsp;&emsp;ecfdId|自定义字段主键|integer(int64)||
|&emsp;&emsp;entityType|实体类型，如 WORKORDER|string||
|&emsp;&emsp;webId|列表列配置 web_id|integer(int64)||
|&emsp;&emsp;fieldCode|字段编码（如 wo_cf_1）|string||
|&emsp;&emsp;fieldLabel|显示名称|string||
|&emsp;&emsp;fieldType|字段类型|string||
|&emsp;&emsp;required|是否必填 0否 1是|integer(int32)||
|&emsp;&emsp;sortNo|排序序号|integer(int32)||
|&emsp;&emsp;maxLength|字段最大长度|integer(int32)||
|&emsp;&emsp;optionsJson|扩展配置（如枚举项 JSON 数组）|string||
|&emsp;&emsp;enabled|是否启用 0否 1是|integer(int32)||


**响应示例**:
```javascript
{
	"success": true,
	"code": 1000,
	"message": "success",
	"data": [
		{
			"ecfdId": 0,
			"entityType": "",
			"webId": 0,
			"fieldCode": "",
			"fieldLabel": "",
			"fieldType": "",
			"required": 0,
			"sortNo": 0,
			"maxLength": 0,
			"optionsJson": "",
			"enabled": 0
		}
	]
}
```


## 仅查询可选、启用自定义字段列表


**接口地址**:`/lightmesapi/open/entityCustomFieldDefController/listOptionalCustomFieldCodes`


**请求方式**:`POST`


**请求数据类型**:`application/x-www-form-urlencoded,application/json`


**响应数据类型**:`*/*`


**接口描述**:<p>返回非必填且已启用的自定义字段编码与显示名，常用于导入等场景。
实体类型可选值：WORKORDER（工单）、WORKORDER_PROCEDURE（工单工序）。
单个客户账号调用该接口的每秒请求数（QPS）最大限制为10。</p>



**请求示例**:


```javascript
{
  "entityType": "",
  "enabledOnly": 0,
  "required": 0
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|AccessKeyId|AccessKeyId|header|true|string||
|AccessKeySecret|AccessKeySecret|header|true|string||
|entityCustomFieldDefQueryDTO|EntityCustomFieldDefQueryDTO|body|true|EntityCustomFieldDefQueryDTO|EntityCustomFieldDefQueryDTO|
|&emsp;&emsp;entityType|实体类型，如 WORKORDER||true|string||
|&emsp;&emsp;enabledOnly|仅启用 1是 0否||false|integer(int32)||
|&emsp;&emsp;required|必填 1是 0否||false|integer(int32)||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|ResultDataListImportOptionalFieldVO|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|success|成功与否|boolean||
|code|状态码|integer(int32)|integer(int32)|
|message|消息|string||
|data||array|ImportOptionalFieldVO|
|&emsp;&emsp;fieldCode|字段英文名/编码|string||
|&emsp;&emsp;fieldLabel|字段中文显示名|string||


**响应示例**:
```javascript
{
	"success": true,
	"code": 1000,
	"message": "success",
	"data": [
		{
			"fieldCode": "",
			"fieldLabel": ""
		}
	]
}
```


## 新增或修改自定义字段定义


**接口地址**:`/lightmesapi/open/entityCustomFieldDefController/saveDef`


**请求方式**:`POST`


**请求数据类型**:`application/x-www-form-urlencoded,application/json`


**响应数据类型**:`*/*`


**接口描述**:<p>修改时需传入 ecfdId。
字段类型可选：string、int、decimal、date、datetime、bool、enum。
单个客户账号调用该接口的每秒请求数（QPS）最大限制为10。</p>



**请求示例**:


```javascript
{
  "ecfdId": 0,
  "entityType": "",
  "fieldLabel": "",
  "fieldType": "",
  "required": 0,
  "sortNo": 0,
  "maxLength": 0,
  "optionsJson": "",
  "enabled": 0
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|AccessKeyId|AccessKeyId|header|true|string||
|AccessKeySecret|AccessKeySecret|header|true|string||
|entityCustomFieldDefDTO|EntityCustomFieldDefDTO|body|true|EntityCustomFieldDefDTO|EntityCustomFieldDefDTO|
|&emsp;&emsp;ecfdId|主键，新增不传||false|integer(int64)||
|&emsp;&emsp;entityType|实体类型，如 WORKORDER||true|string||
|&emsp;&emsp;fieldLabel|显示名称||true|string||
|&emsp;&emsp;fieldType|字段类型 string|int|decimal|date|datetime|bool|enum||false|string||
|&emsp;&emsp;required|是否必填 0否 1是||false|integer(int32)||
|&emsp;&emsp;sortNo|排序||false|integer(int32)||
|&emsp;&emsp;maxLength|最大长度||false|integer(int32)||
|&emsp;&emsp;optionsJson|枚举等扩展配置 JSON||false|string||
|&emsp;&emsp;enabled|是否启用 0否 1是||false|integer(int32)||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|出参|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|success|成功与否|boolean||
|code|状态码|integer(int32)|integer(int32)|
|message|消息|string||


**响应示例**:
```javascript
{
	"success": true,
	"code": 1000,
	"message": "success"
}
```


# 物料相关操作文档


## 物料删除


**接口地址**:`/lightmesapi/open/material/deleteMaterial`


**请求方式**:`POST`


**请求数据类型**:`application/x-www-form-urlencoded,application/json`


**响应数据类型**:`*/*`


**接口描述**:<p>通过此接口可以删除团队下对应的单个物料数据。
    单个客户账号调用该接口的每秒请求数（QPS）最大限制为10。</p>



**请求示例**:


```javascript
{
  "pageNum": 0,
  "pageSize": 0,
  "mtid": 0,
  "mtids": [],
  "rid": 0
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|AccessKeyId|AccessKeyId|header|true|string||
|AccessKeySecret|AccessKeySecret|header|true|string||
|mtidDTO|MtidDTO|body|true|MtidDTO|MtidDTO|
|&emsp;&emsp;pageNum|查询页||true|integer(int32)||
|&emsp;&emsp;pageSize|每页条数||true|integer(int32)||
|&emsp;&emsp;mtid|物料主键||true|integer(int64)||
|&emsp;&emsp;mtids|多个物料主键||false|array|integer(int64)|
|&emsp;&emsp;rid|路线rid||false|integer(int64)||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|出参|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|success|成功与否|boolean||
|code|状态码|integer(int32)|integer(int32)|
|message|消息|string||


**响应示例**:
```javascript
{
	"success": true,
	"code": 1000,
	"message": "success"
}
```


## 物料导入


**接口地址**:`/lightmesapi/open/material/importMaterial`


**请求方式**:`POST`


**请求数据类型**:`application/x-www-form-urlencoded,application/json`


**响应数据类型**:`*/*`


**接口描述**:<p>通过此接口可以批量导入物料数据，通过一个list列表导入，相同物料名称视为同一物料，同一物料下相同路线名称视为同一个路线，同一物料下的同一路线下的工序编号相同视为同一工序，同一物料下的同一路线下的同一工序下的工序参数就单独视为一条工序参数数据。调用此接口会返回一个成功条数、失败条数以及失败原因列表。
单个客户账号调用该接口的每秒请求数（QPS）最大限制为10。</p>



**请求示例**:


```javascript
{
  "materialParams": [
    {
      "materialNo": "",
      "materialDesc": "",
      "materialSpec": "",
      "unit": "",
      "conversionCoefficient": 0,
      "auxiliaryUnit": "",
      "materialLedgerDesc": "",
      "materialLedgerSpec": "",
      "materialLedgerBrand": "",
      "materialLedgerRemark": "",
      "routingsName": "",
      "customizationNo": "",
      "customizationName": "",
      "customerRequirement": "",
      "procedureNo": "",
      "procedureName": "",
      "groupNo": "",
      "departmentName": "",
      "tdepartmentName": "",
      "workcenterNo": "",
      "mouldNo": "",
      "singleTripQty": 0,
      "singleTripTime": 0,
      "sgUnit": 0,
      "timeMouldChange": 0,
      "man": 0,
      "machine": 0,
      "conformityRate": 0,
      "badSuccessor": "",
      "singleTripGreentime": 0,
      "predecessor": "",
      "successor": "",
      "difficultyRate": 0,
      "unitPrice": 0,
      "mtid": 0,
      "tid": 0,
      "rid": 0,
      "rpid": 0,
      "groupRpid": 0,
      "procedureOrder": "",
      "rppid": 0,
      "manMachineRatio": "",
      "wdid": 0,
      "tdid": 0,
      "wcidList": "",
      "timePreparation": 0,
      "firstInspection": "",
      "inprocessInspection": "",
      "tailInspection": "",
      "component": "",
      "componentMultiple": 0,
      "materialCode": "",
      "completiongStatge": 0,
      "mould": "",
      "remark": "",
      "warehouse": "",
      "selfInspections": "",
      "finalInspections": "",
      "firstInspections": "",
      "firstQisid": "",
      "finalQisid": 0,
      "selfQisid": "",
      "auxiliaryUnits": "",
      "mainCoefficient": 0,
      "secondCoefficient": 0,
      "autoProduction": 0,
      "timeAuxiliaryWork": 0,
      "procedureContent": "",
      "machingDay": 0,
      "materialWeight": 0,
      "materialPrice": 0,
      "timeMachining": 0,
      "timeLabor": 0,
      "utilizationRate": 0,
      "customerMaterialNo": "",
      "machineUnitPrice": 0,
      "materialNature": 0,
      "schemeName": "",
      "tisId": 0,
      "auxiliaryReport": 0,
      "psfId": 0,
      "seriesCode": "",
      "processCheckSchemeCode": "",
      "pssid": "",
      "isdelete": 0
    }
  ],
  "ifOld": 0,
  "isOverwrite": 0,
  "tid": 0
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|AccessKeyId|AccessKeyId|header|true|string||
|AccessKeySecret|AccessKeySecret|header|true|string||
|materialApiDTO|MaterialApiDTO|body|true|MaterialApiDTO|MaterialApiDTO|
|&emsp;&emsp;materialParams|物料相关数据||true|array|MaterialParam|
|&emsp;&emsp;&emsp;&emsp;materialNo|物料编号||true|string||
|&emsp;&emsp;&emsp;&emsp;materialDesc|物料名称||true|string||
|&emsp;&emsp;&emsp;&emsp;materialSpec|物料规格||true|string||
|&emsp;&emsp;&emsp;&emsp;unit|单位||true|string||
|&emsp;&emsp;&emsp;&emsp;conversionCoefficient|辅助系数||false|number||
|&emsp;&emsp;&emsp;&emsp;auxiliaryUnit|辅助单位||false|string||
|&emsp;&emsp;&emsp;&emsp;materialLedgerDesc|材料名称||false|string||
|&emsp;&emsp;&emsp;&emsp;materialLedgerSpec|材料规格||false|string||
|&emsp;&emsp;&emsp;&emsp;materialLedgerBrand|材料品牌||false|string||
|&emsp;&emsp;&emsp;&emsp;materialLedgerRemark|材料备注||false|string||
|&emsp;&emsp;&emsp;&emsp;routingsName|工艺路线名称||false|string||
|&emsp;&emsp;&emsp;&emsp;customizationNo|客制代码(填写即为客制路线)||false|string||
|&emsp;&emsp;&emsp;&emsp;customizationName|客制产品名称||false|string||
|&emsp;&emsp;&emsp;&emsp;customerRequirement|客户定制说明||false|string||
|&emsp;&emsp;&emsp;&emsp;procedureNo|工序编号||true|string||
|&emsp;&emsp;&emsp;&emsp;procedureName|工序名称||true|string||
|&emsp;&emsp;&emsp;&emsp;groupNo|附属工序编号(填写后面参数都为空)||false|string||
|&emsp;&emsp;&emsp;&emsp;departmentName|车间名称||false|string||
|&emsp;&emsp;&emsp;&emsp;tdepartmentName|转序车间名称||false|string||
|&emsp;&emsp;&emsp;&emsp;workcenterNo|工作中心编号||false|string||
|&emsp;&emsp;&emsp;&emsp;mouldNo|模具编号||false|string||
|&emsp;&emsp;&emsp;&emsp;singleTripQty|单趟加工数量||false|number||
|&emsp;&emsp;&emsp;&emsp;singleTripTime|单趟加工时长||false|number||
|&emsp;&emsp;&emsp;&emsp;sgUnit|||false|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;timeMouldChange|换模时长||false|number||
|&emsp;&emsp;&emsp;&emsp;man|人机系数中的人的数量||false|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;machine|人机系数中的机器的数量||false|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;conformityRate|良品率||false|number||
|&emsp;&emsp;&emsp;&emsp;badSuccessor|不良品紧后工序||false|string||
|&emsp;&emsp;&emsp;&emsp;singleTripGreentime|单趟绿灯时长||false|number||
|&emsp;&emsp;&emsp;&emsp;predecessor|紧前工序||false|string||
|&emsp;&emsp;&emsp;&emsp;successor|紧后工序||false|string||
|&emsp;&emsp;&emsp;&emsp;difficultyRate|难度系数||false|number||
|&emsp;&emsp;&emsp;&emsp;unitPrice|计件单价||false|number||
|&emsp;&emsp;&emsp;&emsp;mtid|||false|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;tid|||false|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;rid|||false|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;rpid|||false|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;groupRpid|||false|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;procedureOrder|工序序号||false|string||
|&emsp;&emsp;&emsp;&emsp;rppid|||false|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;manMachineRatio|人机系数,如1-1||false|string||
|&emsp;&emsp;&emsp;&emsp;wdid|||false|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;tdid|||false|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;wcidList|||false|string||
|&emsp;&emsp;&emsp;&emsp;timePreparation|准备时长||false|number||
|&emsp;&emsp;&emsp;&emsp;firstInspection|||false|string||
|&emsp;&emsp;&emsp;&emsp;inprocessInspection|||false|string||
|&emsp;&emsp;&emsp;&emsp;tailInspection|||false|string||
|&emsp;&emsp;&emsp;&emsp;component|子件||false|string||
|&emsp;&emsp;&emsp;&emsp;componentMultiple|子件倍数||false|number||
|&emsp;&emsp;&emsp;&emsp;materialCode|原料代号||false|string||
|&emsp;&emsp;&emsp;&emsp;completiongStatge|工单完结点工序 0非完结的 1完结点||false|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;mould|模具||false|string||
|&emsp;&emsp;&emsp;&emsp;remark|工序备注||false|string||
|&emsp;&emsp;&emsp;&emsp;warehouse|仓库||false|string||
|&emsp;&emsp;&emsp;&emsp;selfInspections|自检编号||false|string||
|&emsp;&emsp;&emsp;&emsp;finalInspections|末检编号||false|string||
|&emsp;&emsp;&emsp;&emsp;firstInspections|首检编号||false|string||
|&emsp;&emsp;&emsp;&emsp;firstQisid|||false|string||
|&emsp;&emsp;&emsp;&emsp;finalQisid|||false|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;selfQisid|||false|string||
|&emsp;&emsp;&emsp;&emsp;auxiliaryUnits|辅助单位||false|string||
|&emsp;&emsp;&emsp;&emsp;mainCoefficient|主单位系数||false|number||
|&emsp;&emsp;&emsp;&emsp;secondCoefficient|辅助单位系数||false|number||
|&emsp;&emsp;&emsp;&emsp;autoProduction|下工序自动派工0否1是||false|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;timeAuxiliaryWork|辅助单位时长||false|number||
|&emsp;&emsp;&emsp;&emsp;procedureContent|工序内容||false|string||
|&emsp;&emsp;&emsp;&emsp;machingDay|加工天数||false|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;materialWeight|产品单重||false|number||
|&emsp;&emsp;&emsp;&emsp;materialPrice|||false|number||
|&emsp;&emsp;&emsp;&emsp;timeMachining|||false|number||
|&emsp;&emsp;&emsp;&emsp;timeLabor|||false|number||
|&emsp;&emsp;&emsp;&emsp;utilizationRate|||false|number||
|&emsp;&emsp;&emsp;&emsp;customerMaterialNo|||false|string||
|&emsp;&emsp;&emsp;&emsp;machineUnitPrice|设备件工费||false|number||
|&emsp;&emsp;&emsp;&emsp;materialNature|产品性质 0成品 1半成品||false|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;schemeName|机厂床方案名称||false|string||
|&emsp;&emsp;&emsp;&emsp;tisId|机床厂方案id||false|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;auxiliaryReport|是否以辅助单位报工 0否 1是||false|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;psfId|产品系列id||false|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;seriesCode|产品系列编号||false|string||
|&emsp;&emsp;&emsp;&emsp;processCheckSchemeCode|工艺检查方案代码||false|string||
|&emsp;&emsp;&emsp;&emsp;pssid|工艺监督方案id(逗号分隔)||false|string||
|&emsp;&emsp;&emsp;&emsp;isdelete|是否删除 0否 1是||false|integer(int32)||
|&emsp;&emsp;ifOld|||false|integer(int32)||
|&emsp;&emsp;isOverwrite|是否覆盖 0否 1是||false|integer(int32)||
|&emsp;&emsp;tid|||false|integer(int64)||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|ResultDataApiReturnVO|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|success|成功与否|boolean||
|code|状态码|integer(int32)|integer(int32)|
|message|消息|string||
|data||ApiReturnVO|ApiReturnVO|
|&emsp;&emsp;successTotal|成功的条数|integer(int32)||
|&emsp;&emsp;errorTotal|失败的条数|integer(int32)||
|&emsp;&emsp;errorList|失败的错误信息|array|string|


**响应示例**:
```javascript
{
	"success": true,
	"code": 1000,
	"message": "success",
	"data": {
		"successTotal": 0,
		"errorTotal": 0,
		"errorList": []
	}
}
```


## 物料用料导入


**接口地址**:`/lightmesapi/open/material/insertUseMaterial`


**请求方式**:`POST`


**请求数据类型**:`application/x-www-form-urlencoded,application/json`


**响应数据类型**:`*/*`


**接口描述**:<p>通过此接口可以导入物料相关工序的用料，如果物料或者相关工序不存在，系统会添加物料和相关工序；接口也可以导入或者同步折合系数，当传入折合系数时，系统会更改该物料的组装工序的工艺工时,如果该物料不存在组装工序,系统会添加组装工序。
单个客户账号调用该接口的每秒请求数（QPS）最大限制为20。</p>



**请求示例**:


```javascript
{
  "materialNo": "",
  "materialDesc": "",
  "materialSpec": "",
  "unit": "",
  "customizationNo": "",
  "customerRequirement": "",
  "equivalentNum": "",
  "useMaterials": [
    {
      "useMaterialNo": "",
      "useMaterialDesc": "",
      "useMaterialSpec": "",
      "useUnit": "",
      "quantity": 0,
      "procedureNo": "",
      "procedureName": ""
    }
  ],
  "tid": 0
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|AccessKeyId|AccessKeyId|header|true|string||
|AccessKeySecret|AccessKeySecret|header|true|string||
|useMaterialInfoDTO|UseMaterialInfoDTO|body|true|UseMaterialInfoDTO|UseMaterialInfoDTO|
|&emsp;&emsp;materialNo|物料编号||true|string||
|&emsp;&emsp;materialDesc|物料名称||false|string||
|&emsp;&emsp;materialSpec|物料规格||false|string||
|&emsp;&emsp;unit|单位||false|string||
|&emsp;&emsp;customizationNo|客制化代码||false|string||
|&emsp;&emsp;customerRequirement|客制化说明||false|string||
|&emsp;&emsp;equivalentNum|折合系数||false|string||
|&emsp;&emsp;useMaterials|物料相关数据||true|array|UseMaterialDTO|
|&emsp;&emsp;&emsp;&emsp;useMaterialNo|用料物料编号||true|string||
|&emsp;&emsp;&emsp;&emsp;useMaterialDesc|用料物料名称||false|string||
|&emsp;&emsp;&emsp;&emsp;useMaterialSpec|用料物料规格||false|string||
|&emsp;&emsp;&emsp;&emsp;useUnit|用料单位||false|string||
|&emsp;&emsp;&emsp;&emsp;quantity|用料数量||true|number||
|&emsp;&emsp;&emsp;&emsp;procedureNo|工序编号||false|string||
|&emsp;&emsp;&emsp;&emsp;procedureName|工序名称||false|string||
|&emsp;&emsp;tid|团队id||false|integer(int64)||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|出参|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|success|成功与否|boolean||
|code|状态码|integer(int32)|integer(int32)|
|message|消息|string||


**响应示例**:
```javascript
{
	"success": true,
	"code": 1000,
	"message": "success"
}
```


## 物料查询


**接口地址**:`/lightmesapi/open/material/queryCraftHours`


**请求方式**:`POST`


**请求数据类型**:`application/x-www-form-urlencoded,application/json`


**响应数据类型**:`*/*`


**接口描述**:<p>通过此接口可以查询对应团队所有的物料简要信息，查询结果为一个物料列表集合，按创建日期倒序。
单个客户账号调用该接口的每秒请求数（QPS）最大限制为10。</p>



**请求示例**:


```javascript
{
  "pageNum": 0,
  "pageSize": 0,
  "materialDescOrNo": "",
  "startTime": "",
  "endTime": "",
  "combination": 0,
  "confirm": 0,
  "procedureName": "",
  "materialNo": "",
  "materialDesc": "",
  "materialSpec": "",
  "materialNature": 0
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|AccessKeyId|AccessKeyId|header|true|string||
|AccessKeySecret|AccessKeySecret|header|true|string||
|craftHoursListDTO|CraftHoursListDTO|body|true|CraftHoursListDTO|CraftHoursListDTO|
|&emsp;&emsp;pageNum|查询页||true|integer(int32)||
|&emsp;&emsp;pageSize|每页条数||true|integer(int32)||
|&emsp;&emsp;materialDescOrNo|物料描述或者物料编号用于模糊查询||false|string||
|&emsp;&emsp;startTime|模糊查询起始时间||false|string(date-time)||
|&emsp;&emsp;endTime|模糊查询结束时间||false|string(date-time)||
|&emsp;&emsp;combination|是否是组合物料 0:非组合   1：组合||false|integer(int32)||
|&emsp;&emsp;confirm|物料是否确认 0:待确认   1:已确认||false|integer(int32)||
|&emsp;&emsp;procedureName|工序||false|string||
|&emsp;&emsp;materialNo|物料编号模糊查询||false|string||
|&emsp;&emsp;materialDesc|物料规格模糊查询||false|string||
|&emsp;&emsp;materialSpec|物料规格模糊查询||false|string||
|&emsp;&emsp;materialNature|产品性质 0成品 1半成品||false|integer(int32)||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|ResultQueryCraftHoursList|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|success|成功与否|boolean||
|code|状态码|integer(int32)|integer(int32)|
|message|消息|string||
|totalItems|总条数|integer(int32)|integer(int32)|
|data||array|CraftHoursList|
|&emsp;&emsp;mtid|物料主键|integer(int64)||
|&emsp;&emsp;materialNo|物料编码|string||
|&emsp;&emsp;materialDesc|物料描述|string||
|&emsp;&emsp;materialSpec|规格|string||
|&emsp;&emsp;unit|单位|string||
|&emsp;&emsp;auxiliaryUnit|辅助单位|string||
|&emsp;&emsp;conversionCoefficient|转换系数|number||
|&emsp;&emsp;createTime|创建日期|string(date-time)||
|&emsp;&emsp;updateTime|修改日期|string(date-time)||
|&emsp;&emsp;updateUserName|修改人|string||
|&emsp;&emsp;createUserName|创建人|string||
|&emsp;&emsp;procedureName|工序名称|array|string|
|&emsp;&emsp;materialNature|产品性质 0成品 1半成品|integer(int32)||
|&emsp;&emsp;confirm|物料是否确认 0:待确认   1:已确认|integer(int32)||
|&emsp;&emsp;materialLedgerDesc|材料名称|string||
|&emsp;&emsp;materialLedgerSpec|材料规格|string||
|&emsp;&emsp;updateQty|修改次数|integer(int32)||
|&emsp;&emsp;ganttColor|甘特图颜色|string||
|&emsp;&emsp;bindSop|绑定SOP 0否 1是|integer(int32)||
|&emsp;&emsp;bindFirstInspectScheme|绑定首检方案 0否 1是|integer(int32)||
|&emsp;&emsp;bindSelfInspectScheme|绑定巡检方案 0否 1是|integer(int32)||
|&emsp;&emsp;bindFinalInspectScheme|绑定末检方案 0否 1是|integer(int32)||
|&emsp;&emsp;bindProcessSupervisionScheme|绑定工艺监督方案 0否 1是|integer(int32)||


**响应示例**:
```javascript
{
	"success": true,
	"code": 1000,
	"message": "success",
	"totalItems": 12,
	"data": [
		{
			"mtid": 0,
			"materialNo": "",
			"materialDesc": "",
			"materialSpec": "",
			"unit": "",
			"auxiliaryUnit": "",
			"conversionCoefficient": 0,
			"createTime": "",
			"updateTime": "",
			"updateUserName": "",
			"createUserName": "",
			"procedureName": [],
			"materialNature": 0,
			"confirm": 0,
			"materialLedgerDesc": "",
			"materialLedgerSpec": "",
			"updateQty": 0,
			"ganttColor": "",
			"bindSop": 0,
			"bindFirstInspectScheme": 0,
			"bindSelfInspectScheme": 0,
			"bindFinalInspectScheme": 0,
			"bindProcessSupervisionScheme": 0
		}
	]
}
```


## 物料查询详情


**接口地址**:`/lightmesapi/open/material/queryCraftHoursDetails`


**请求方式**:`POST`


**请求数据类型**:`application/x-www-form-urlencoded,application/json`


**响应数据类型**:`*/*`


**接口描述**:<p>通过此接口可以查询物料的详细信息，包含物料下的工艺路线，工序以及工时参数等等。
单个客户账号调用该接口的每秒请求数（QPS）最大限制为10。</p>



**请求示例**:


```javascript
{
  "mtid": 0,
  "tid": 0
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|AccessKeyId|AccessKeyId|header|true|string||
|AccessKeySecret|AccessKeySecret|header|true|string||
|selectMaterialsDTO|SelectMaterialsDTO|body|true|SelectMaterialsDTO|SelectMaterialsDTO|
|&emsp;&emsp;mtid|物料id||true|integer(int64)||
|&emsp;&emsp;tid|团队id||false|integer(int64)||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|ResultDataListCraftHoursListDetailsVO|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|success|成功与否|boolean||
|code|状态码|integer(int32)|integer(int32)|
|message|消息|string||
|data||array|CraftHoursListDetailsVO|
|&emsp;&emsp;rid|路线主键|integer(int64)||
|&emsp;&emsp;materialNo|物料编码|string||
|&emsp;&emsp;materialDesc|物料描述|string||
|&emsp;&emsp;materialSpec|规格|string||
|&emsp;&emsp;unit|单位|string||
|&emsp;&emsp;materialLedgerDesc|材料名称|string||
|&emsp;&emsp;materialLedgerSpec|材料规格|string||
|&emsp;&emsp;materialLedgerBrand|材料品牌|string||
|&emsp;&emsp;remark|备注|string||
|&emsp;&emsp;conversionCoefficient|转化系数|number||
|&emsp;&emsp;auxiliaryUnit|辅助单位|string||
|&emsp;&emsp;materialWeight|产品单重|number||
|&emsp;&emsp;materialPrice|产品单价|number||
|&emsp;&emsp;routingsName|物料工艺路线名称|string||
|&emsp;&emsp;customizationNo|客制代码|string||
|&emsp;&emsp;customizationName|客制产品名称|string||
|&emsp;&emsp;customerRequirement|客户定制说明|string||
|&emsp;&emsp;completiongStatge|工单进度标识索引位置|integer(int32)||
|&emsp;&emsp;fileUrl|产品图片|string||
|&emsp;&emsp;ganttColor|甘特图颜色|string||
|&emsp;&emsp;utilizationRate|产品利用率|number||
|&emsp;&emsp;customerMaterialNo|客户料号|string||
|&emsp;&emsp;materialNature|产品性质 0:成品 1:半成品|integer(int32)||
|&emsp;&emsp;sopPathList|sop路径集合|array|string|
|&emsp;&emsp;psfId|产品系列系数id|integer(int64)||
|&emsp;&emsp;seriesName|系列名称|string||
|&emsp;&emsp;seriesCode|系列系数代码|string||
|&emsp;&emsp;routingsProcedureMsgList|工序列表|array|RoutingsProcedureMsg|
|&emsp;&emsp;&emsp;&emsp;rpid|工序主键|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;procedureNo|工序编号|string||
|&emsp;&emsp;&emsp;&emsp;procedureName|工序名称|string||
|&emsp;&emsp;&emsp;&emsp;groupRpid|附属工序|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;groupNo|附属工序编码|string||
|&emsp;&emsp;&emsp;&emsp;firstInspection|首检,如果存在传0，不存在传0或者null|string||
|&emsp;&emsp;&emsp;&emsp;inprocessInspection|巡检,如果存在传0，不存在传0或者null|string||
|&emsp;&emsp;&emsp;&emsp;tailInspection|尾检,如果存在传0，不存在传0或者null|string||
|&emsp;&emsp;&emsp;&emsp;conformityRate|良品率|number||
|&emsp;&emsp;&emsp;&emsp;predecessor|紧急工序编号|string||
|&emsp;&emsp;&emsp;&emsp;successor|紧后工序编号|string||
|&emsp;&emsp;&emsp;&emsp;badSuccessor|不良品紧后工序|string||
|&emsp;&emsp;&emsp;&emsp;procedureOrder|位置|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;difficultyRate|难度系数|number||
|&emsp;&emsp;&emsp;&emsp;unitPrice|计件单价|number||
|&emsp;&emsp;&emsp;&emsp;component|子件|string||
|&emsp;&emsp;&emsp;&emsp;mould|模具|string||
|&emsp;&emsp;&emsp;&emsp;remark|备注|string||
|&emsp;&emsp;&emsp;&emsp;componentMultiple|子件倍数|number||
|&emsp;&emsp;&emsp;&emsp;materialCode|原料代号|string||
|&emsp;&emsp;&emsp;&emsp;warehouse|仓库|string||
|&emsp;&emsp;&emsp;&emsp;firstQisid|首检主键|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;firstQisidList|首检主键集合|array|integer|
|&emsp;&emsp;&emsp;&emsp;selfQisidList|自检主键集合|array|integer|
|&emsp;&emsp;&emsp;&emsp;finalQisid|末检主键|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;selfQisid|自检主键|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;pssidList|工艺监督主键集合|array|integer|
|&emsp;&emsp;&emsp;&emsp;pssNameList|工艺监督方案名称|array|string|
|&emsp;&emsp;&emsp;&emsp;firstInspections|首检|string||
|&emsp;&emsp;&emsp;&emsp;firstInspectionNameList|首检方案名称集合|array|string|
|&emsp;&emsp;&emsp;&emsp;selfInspectionNameList|自检方案名称集合|array|string|
|&emsp;&emsp;&emsp;&emsp;finalInspections|末检|string||
|&emsp;&emsp;&emsp;&emsp;selfInspections|自检|string||
|&emsp;&emsp;&emsp;&emsp;tisId|机床厂方案id|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;schemeName|机床厂方案名称|string||
|&emsp;&emsp;&emsp;&emsp;schemeScore|方案分数|number||
|&emsp;&emsp;&emsp;&emsp;auxiliaryUnit|辅助单位|string||
|&emsp;&emsp;&emsp;&emsp;mainCoefficient|主单位系数|number||
|&emsp;&emsp;&emsp;&emsp;secondCoefficient|辅助单位系数|number||
|&emsp;&emsp;&emsp;&emsp;maintainProcedure|维修工序|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;autoProduction|下工序自动派工 0否 1是|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;autoProductionWcid|下工序自动派工默认工作中心id（兼容老字段，取列表第一个）|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;autoProductionWcidList|下工序自动派工默认工作中心id列表|array|integer|
|&emsp;&emsp;&emsp;&emsp;timeAuxiliaryWork|辅助作业时长|number||
|&emsp;&emsp;&emsp;&emsp;procedureContent|工艺内容|string||
|&emsp;&emsp;&emsp;&emsp;machingDay|加工天数|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;auxiliaryReport|是否以辅助单位报工 0否 1是|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;regeneratFlag||integer(int32)||
|&emsp;&emsp;&emsp;&emsp;difficultyDescription|难度说明|string||
|&emsp;&emsp;&emsp;&emsp;workControl|开工控制|number||
|&emsp;&emsp;&emsp;&emsp;routingsProcedureParameterMsgList|工艺工时列表|array|RoutingsProcedureParameterMsg|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;rppid|工序详情主键id  表routings_procedure_parameter|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;wdid|车间部门id|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;departmentName|车间部门名字|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;tdid|转序车间tdid|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;tdepartmentName|车间部门名字|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;singleTripQty|单趟加工数量 个|number||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;singleTripTime|单趟加工市场 秒|number||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;singleTripGreentime|单趟绿灯时长 秒|number||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;timeMouldChange|换膜时长 分|number||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;timePreparation|生产准备时长 分|number||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;manMachineRatio|人机匹配系数使用-分离，如 1-1,2-2|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;machineUnitPrice|设备件工费|number||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;man|人机系数中的人的数量|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;machine|人机系数中的机器的数量|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;timeMachining|机加工时(秒)|number||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;timeLabor|人工工时(秒)|number||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;sgUnit|时长单位|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;wcidList|工作中心(清单） 逗号隔开的全数字 字符串|array|integer|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;workCenterMsgs|工作中心|array|WorkCenterMsg|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;wcid|工作中心主键|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;workcenterNo|工作中心编号|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;workcenterName|工作中心名称|string||


**响应示例**:
```javascript
{
	"success": true,
	"code": 1000,
	"message": "success",
	"data": [
		{
			"rid": 0,
			"materialNo": "",
			"materialDesc": "",
			"materialSpec": "",
			"unit": "",
			"materialLedgerDesc": "",
			"materialLedgerSpec": "",
			"materialLedgerBrand": "",
			"remark": "",
			"conversionCoefficient": 0,
			"auxiliaryUnit": "",
			"materialWeight": 0,
			"materialPrice": 0,
			"routingsName": "",
			"customizationNo": "",
			"customizationName": "",
			"customerRequirement": "",
			"completiongStatge": 0,
			"fileUrl": "",
			"ganttColor": "",
			"utilizationRate": 0,
			"customerMaterialNo": "",
			"materialNature": 0,
			"sopPathList": [],
			"psfId": 0,
			"seriesName": "",
			"seriesCode": "",
			"routingsProcedureMsgList": [
				{
					"rpid": 0,
					"procedureNo": "",
					"procedureName": "",
					"groupRpid": 0,
					"groupNo": "",
					"firstInspection": "",
					"inprocessInspection": "",
					"tailInspection": "",
					"conformityRate": 0,
					"predecessor": "",
					"successor": "",
					"badSuccessor": "",
					"procedureOrder": 0,
					"difficultyRate": 0,
					"unitPrice": 0,
					"component": "",
					"mould": "",
					"remark": "",
					"componentMultiple": 0,
					"materialCode": "",
					"warehouse": "",
					"firstQisid": 0,
					"firstQisidList": [],
					"selfQisidList": [],
					"finalQisid": 0,
					"selfQisid": 0,
					"pssidList": [],
					"pssNameList": [],
					"firstInspections": "",
					"firstInspectionNameList": [],
					"selfInspectionNameList": [],
					"finalInspections": "",
					"selfInspections": "",
					"tisId": 0,
					"schemeName": "",
					"schemeScore": 0,
					"auxiliaryUnit": "",
					"mainCoefficient": 0,
					"secondCoefficient": 0,
					"maintainProcedure": 0,
					"autoProduction": 0,
					"autoProductionWcid": 0,
					"autoProductionWcidList": [],
					"timeAuxiliaryWork": 0,
					"procedureContent": "",
					"machingDay": 0,
					"auxiliaryReport": 0,
					"regeneratFlag": 0,
					"difficultyDescription": "",
					"workControl": 0,
					"routingsProcedureParameterMsgList": [
						{
							"rppid": 0,
							"wdid": 0,
							"departmentName": "",
							"tdid": 0,
							"tdepartmentName": "",
							"singleTripQty": 0,
							"singleTripTime": 0,
							"singleTripGreentime": 0,
							"timeMouldChange": 0,
							"timePreparation": 0,
							"manMachineRatio": "",
							"machineUnitPrice": 0,
							"man": 0,
							"machine": 0,
							"timeMachining": 0,
							"timeLabor": 0,
							"sgUnit": 0,
							"wcidList": [],
							"workCenterMsgs": [
								{
									"wcid": 0,
									"workcenterNo": "",
									"workcenterName": ""
								}
							]
						}
					]
				}
			]
		}
	]
}
```


## 物料修改


**接口地址**:`/lightmesapi/open/material/updateMaterial`


**请求方式**:`POST`


**请求数据类型**:`application/x-www-form-urlencoded,application/json`


**响应数据类型**:`*/*`


**接口描述**:<p>通过此接口可以修改团队下对应的物料数据。
    单个客户账号调用该接口的每秒请求数（QPS）最大限制为10。</p>



**请求示例**:


```javascript
{
  "mtid": 0,
  "tid": 0,
  "uid": 0,
  "materialNo": "",
  "materialDesc": "",
  "materialSpec": "",
  "unit": "",
  "conversionCoefficient": 0,
  "auxiliaryUnit": "",
  "materialLedgerDesc": "",
  "materialLedgerSpec": "",
  "materialLedgerBrand": "",
  "remark": "",
  "fileUrl": "",
  "combination": 0,
  "hoursCalculate": 0,
  "materialWeight": 0,
  "materialPrice": 0,
  "ganttColor": "",
  "utilizationRate": 0,
  "customerMaterialNo": "",
  "materialNature": 0,
  "psfId": 0,
  "routingsDTOS": [
    {
      "rid": 0,
      "mtid": 0,
      "routingsName": "",
      "customizationNo": "",
      "customizationName": "",
      "customerRequirement": "",
      "completiongStatge": 0,
      "routingsProcedureDTOS": [
        {
          "rpid": 0,
          "rid": 0,
          "procedureNo": "",
          "procedureName": "",
          "groupNo": "",
          "firstInspection": "",
          "inprocessInspection": "",
          "tailInspection": "",
          "conformityRate": 0,
          "predecessor": "",
          "successor": "",
          "badSuccessor": "",
          "procedureOrder": 0,
          "difficultyRate": 0,
          "unitPrice": 0,
          "component": "",
          "componentMultiple": 0,
          "materialCode": "",
          "mould": "",
          "warehouse": "",
          "remark": "",
          "firstQisid": 0,
          "finalQisid": 0,
          "selfQisid": 0,
          "firstQisidList": [],
          "selfQisidList": [],
          "pssidList": [],
          "auxiliaryUnit": "",
          "mainCoefficient": 0,
          "secondCoefficient": 0,
          "maintainProcedure": 0,
          "autoProduction": 0,
          "autoProductionWcid": 0,
          "autoProductionWcidList": [],
          "autoProductionWcids": "",
          "timeAuxiliaryWork": 0,
          "procedureContent": "",
          "machingDay": 0,
          "tisId": 0,
          "regeneratFlag": 0,
          "auxiliaryReport": 0,
          "workControl": 0,
          "difficultyDescription": "",
          "routingsProcedureParameterDTOS": [
            {
              "rppid": 0,
              "woppid": 0,
              "rpid": 0,
              "wdid": 0,
              "tdid": 0,
              "wcidList": [],
              "singleTripQty": 0,
              "singleTripTime": 0,
              "singleTripGreentime": 0,
              "timeMouldChange": 0,
              "timePreparation": 0,
              "man": 0,
              "machine": 0,
              "workCenterMsgs": [
                {
                  "wcid": 0,
                  "workcenterNo": "",
                  "workcenterName": ""
                }
              ],
              "departmentName": "",
              "timeMachining": 0,
              "machineUnitPrice": 0,
              "timeLabor": 0,
              "sgUnit": 0
            }
          ]
        }
      ]
    }
  ]
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|AccessKeyId|AccessKeyId|header|true|string||
|AccessKeySecret|AccessKeySecret|header|true|string||
|物料信息|物料信息|body|true|物料信息|物料信息|
|&emsp;&emsp;mtid|物料主键||true|integer(int64)||
|&emsp;&emsp;tid|团队主键||false|integer(int64)||
|&emsp;&emsp;uid|修改人id||false|integer(int64)||
|&emsp;&emsp;materialNo|物料编号||true|string||
|&emsp;&emsp;materialDesc|物料描述||true|string||
|&emsp;&emsp;materialSpec|物料规格||true|string||
|&emsp;&emsp;unit|单位||true|string||
|&emsp;&emsp;conversionCoefficient|转换系数||false|number||
|&emsp;&emsp;auxiliaryUnit|辅助单位||false|string||
|&emsp;&emsp;materialLedgerDesc|材料名称||false|string||
|&emsp;&emsp;materialLedgerSpec|材料规格||false|string||
|&emsp;&emsp;materialLedgerBrand|材料品牌||false|string||
|&emsp;&emsp;remark|备注||false|string||
|&emsp;&emsp;fileUrl|产品图片||false|string||
|&emsp;&emsp;combination|是否是组合物料 0:非组合   1：组合||false|integer(int32)||
|&emsp;&emsp;hoursCalculate|工时按单个产品工时/组合各类数量 0否 1是||false|integer(int32)||
|&emsp;&emsp;materialWeight|产品单重||false|number||
|&emsp;&emsp;materialPrice|产品单价||false|number||
|&emsp;&emsp;ganttColor|甘特图颜色||false|string||
|&emsp;&emsp;utilizationRate|产品利用率||false|number||
|&emsp;&emsp;customerMaterialNo|客户料号||false|string||
|&emsp;&emsp;materialNature|产品性质||false|integer(int32)||
|&emsp;&emsp;psfId|产品系列系数id||false|integer(int64)||
|&emsp;&emsp;routingsDTOS|工作路线列表||true|array|工艺路线信息|
|&emsp;&emsp;&emsp;&emsp;rid|路线主键||true|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;mtid|物料id||true|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;routingsName|物料工艺路线名称||true|string||
|&emsp;&emsp;&emsp;&emsp;customizationNo|客制代码||false|string||
|&emsp;&emsp;&emsp;&emsp;customizationName|客制产品名称||false|string||
|&emsp;&emsp;&emsp;&emsp;customerRequirement|客户定制说明||false|string||
|&emsp;&emsp;&emsp;&emsp;completiongStatge|工单进度标识位置||false|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;routingsProcedureDTOS|工序列表||true|array|工艺工序主数据|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;rpid|工序主键||true|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;rid|工艺路线id||true|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;procedureNo|工序编号||true|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;procedureName|工序名称||true|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;groupNo|附属工序编号||false|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;firstInspection|首检,如果存在传1，不存在传0或者null||false|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;inprocessInspection|巡检,如果存在传1，不存在传0或者null||false|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;tailInspection|尾检,如果存在传1，不存在传0或者null||false|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;conformityRate|良品率||false|number||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;predecessor|紧前工序编号||false|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;successor|紧后工序编号||false|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;badSuccessor|不良品紧后工序||false|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;procedureOrder|位置||false|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;difficultyRate|难度系数||false|number||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;unitPrice|计件单价||false|number||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;component|子件||false|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;componentMultiple|子件倍数||false|number||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;materialCode|原料代号||false|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;mould|模具||false|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;warehouse|仓库||false|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;remark|工序备注||false|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;firstQisid|首检主键||false|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;finalQisid|末检主键||false|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;selfQisid|自检主键||false|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;firstQisidList|首检主键集合||false|array|integer|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;selfQisidList|自检主键集合||false|array|integer|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;pssidList|工艺监督主键集合||false|array|integer|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;auxiliaryUnit|辅助单位||false|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;mainCoefficient|主单位系数||false|number||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;secondCoefficient|辅助单位系数||false|number||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;maintainProcedure|维修工序||false|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;autoProduction|下工序自动派工 0否 1是||false|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;autoProductionWcid|下工序自动派工默认工作中心id（兼容老字段，取列表第一个）||false|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;autoProductionWcidList|下工序自动派工默认工作中心id列表||false|array|integer|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;autoProductionWcids|下工序自动派工默认工作中心id字符串，逗号分隔存库用||false|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;timeAuxiliaryWork|辅助作业时长||false|number||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;procedureContent|工艺内容||false|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;machingDay|加工天数||false|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;tisId|机床厂方案id||false|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;regeneratFlag|再生工序标识 0否 1是||false|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;auxiliaryReport|是否以辅助单位报工 0否 1是||false|integer(int32)||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;workControl|开工控制||false|number||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;difficultyDescription|难度说明||false|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;routingsProcedureParameterDTOS|工艺工时列表||true|array|工艺工序中的工作中心信息|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;rppid|工作中心主键||true|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;woppid|工单工序参数ID||false|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;rpid|工序主键||true|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;wdid|车间部门id||true|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;tdid|工序转交车间部门id||true|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;wcidList|工作中心||false|array|integer|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;singleTripQty|单趟加工数量||false|number||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;singleTripTime|单趟加工时长(秒)||false|number||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;singleTripGreentime|单趟绿灯时长||false|number||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;timeMouldChange|换模时长（分钟），0指不用换模||false|number||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;timePreparation|生产准备时长(分钟)||false|number||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;man|人机系数中的人的数量||false|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;machine|人机系数中的机器的数量||false|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;workCenterMsgs|工作中心||false|array|WorkCenterMsg|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;wcid|工作中心主键||false|integer(int64)||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;workcenterNo|工作中心编号||false|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;workcenterName|工作中心名称||false|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;departmentName|车间名称||false|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;timeMachining|机加工时(秒)||false|number||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;machineUnitPrice|设备件工费||false|number||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;timeLabor|人工工时(秒)||false|number||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;sgUnit|时长单位||false|integer(int32)||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|出参|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|success|成功与否|boolean||
|code|状态码|integer(int32)|integer(int32)|
|message|消息|string||


**响应示例**:
```javascript
{
	"success": true,
	"code": 1000,
	"message": "success"
}
```


# 异常报表操作文档


## 异常上报记录列表


**接口地址**:`/lightmesapi/open/errorReportAPIController/selectErrorReport`


**请求方式**:`POST`


**请求数据类型**:`application/x-www-form-urlencoded,application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "pageNum": 0,
  "pageSize": 0,
  "date": "",
  "shiftName": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|AccessKeyId|AccessKeyId|header|true|string||
|AccessKeySecret|AccessKeySecret|header|true|string||
|dateTimeDTO|DateTimeDTO|body|true|DateTimeDTO|DateTimeDTO|
|&emsp;&emsp;pageNum|页面||true|integer(int32)||
|&emsp;&emsp;pageSize|每页大小||true|integer(int32)||
|&emsp;&emsp;date|日期(yyyy-MM-dd HH:mm:ss)||true|string||
|&emsp;&emsp;shiftName|班次名称(与MES系统设置的班次相同，不填查询所有班次)||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|ResultQueryErrorReportVO|


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|success|成功与否|boolean||
|code|状态码|integer(int32)|integer(int32)|
|message|消息|string||
|totalItems|总条数|integer(int32)|integer(int32)|
|data||array|ErrorReportVO|
|&emsp;&emsp;lwlId|异常列表Id|integer(int64)||
|&emsp;&emsp;mid|设备主键|integer(int64)||
|&emsp;&emsp;machineNo|设备编号|string||
|&emsp;&emsp;machineName|设备名称|string||
|&emsp;&emsp;machineStatusName|设备状态|string||
|&emsp;&emsp;workDate|日期|string(date-time)||
|&emsp;&emsp;shiftName|班次名称|string||
|&emsp;&emsp;shiftStartDate|班次开始日期|string(date-time)||
|&emsp;&emsp;shiftEndDate|班次结束日期|string(date-time)||
|&emsp;&emsp;color|灯的颜色|string||
|&emsp;&emsp;reasonCode|异常代码|string||
|&emsp;&emsp;waitReason|异常原因|string||
|&emsp;&emsp;reasonClassification|异常原因分类|string||
|&emsp;&emsp;waitStartTime|开始时间|string(date-time)||
|&emsp;&emsp;waitEndTime|结束时间|string(date-time)||
|&emsp;&emsp;duration|持续时长|number||
|&emsp;&emsp;workorderNo|工单号|string||
|&emsp;&emsp;materialNo|物料号|string||
|&emsp;&emsp;userName|备注人员姓名|string||
|&emsp;&emsp;picUrls|图片地址|array|string|
|&emsp;&emsp;description|异常说明|string||
|&emsp;&emsp;openUserName|开机人员|string||
|&emsp;&emsp;updateTime|上报时间|string(date-time)||


**响应示例**:
```javascript
{
	"success": true,
	"code": 1000,
	"message": "success",
	"totalItems": 12,
	"data": [
		{
			"lwlId": 0,
			"mid": 0,
			"machineNo": "",
			"machineName": "",
			"machineStatusName": "",
			"workDate": "",
			"shiftName": "",
			"shiftStartDate": "",
			"shiftEndDate": "",
			"color": "",
			"reasonCode": "",
			"waitReason": "",
			"reasonClassification": "",
			"waitStartTime": "",
			"waitEndTime": "",
			"duration": 0,
			"workorderNo": "",
			"materialNo": "",
			"userName": "",
			"picUrls": [],
			"description": "",
			"openUserName": "",
			"updateTime": ""
		}
	]
}
```