## VMI库存看板

**修订历史记录**

| **日期**   | **版本** | **说明** | **作者** |
| ---------- | -------- | -------- | -------- |
| 2024/07/19 | V1.0.0   | 初稿     | 熊有进   |


  此API用于查询携客云平台的VMI库存看板相关数据，包括1个API接口：

###   [列表查询](https://openapi.xiekeyun.com/doc/docpull/order/vmivendorboard.html#1-VMI库存看板列表查询)

​     **调用场景：**

​       此查询API接口是VMI库存看板列表查询

## 1 VMI库存看板列表查询

此查询API接口是VMI库存看板列表查询

## 1.1 请求

### 1.1.1 请求地址

https://openapi.xiekeyun.com/vmiVendorBoard/queryList.json

### 1.1.2 请求公传参数（commonParam）

 **请求时对应的公传参数定义如【[公传参数](https://openapi.xiekeyun.com/doc/doccommon/description.html#公传参数)】所述**

### 1.1.3 业务请求参数（body）

| 参数名称    | 参数描述                   | 参数类型   | 说明                                                         | 要求     |
| ----------- | -------------------------- | ---------- | ------------------------------------------------------------ | -------- |
| startDate   | 单据更新时间范围的开始时间 | **Number** | 开始时间对应的**毫秒**时间戳数值; 查询时为开区间（即 >startDate），开始时间和结束时间相差不得大于60天 | **必填** |
| endDate     | 单据更新时间范围的结束时间 | **Number** | 结束时间对应的**毫秒**时间戳数值; 查询时为闭区间（即 <=endDate），开始时间和结束时间相差不得大于60天 | **必填** |
| erpCode     | 请求者用户ERP帐号          | **String** | 对应数据操作公司中，员工档案里“ERP帐户”的值，主要做数据鉴权使用，返回此员工有权限的数据 | **必填** |
| customerKey | 内部客户编码或名称         | **String** | 客户档案中的客户编码或名称，如果传此值，只返回此客户相关的数据 | **选填** |

### 1.1.4 请求参数示例

Demo

```
{
    "commonParam": {
        "operateCompanyCode": "94563778",
        "timestamps": 1721359760,
        "sign": "2cf8dec6d4a3f13bd47fe5ccc8c7b8e9",
        "appKey": "2505309c9757c3246ed317775a861441",
        "ownerCompanyCode": "94563778",
        "version": "1.0"
    },
    "body": {
        "erpCode": "8088",
        "startDate":1716262010000,
        "endDate":1721359610338,
        "customerKey": "205"
    }
}
     
```

### 1.1.5 说明

  \1. 本接口访问频率不能低于 **3** 分钟；

## 1.2 结果返回

### 1.2.1 描述

结果数据以Json格式返回

### 1.2.2 返回结果

### 1.2.2.1 返回结果公共字段定义

| 字段名称  | 描述                                                         | 类型         |
| --------- | ------------------------------------------------------------ | ------------ |
| result    | 返回结果状态 1:成功；9:失败                                  | **Number**   |
| errorCode | 接口错误编码（失败时有值），详细参考“[**错误编码规范定义**](https://openapi.xiekeyun.com/doc/doccommon/description.html#错误编码规范定义)” | **String**   |
| errorMsg  | 接口错误信息（失败时有值）                                   | **String**   |
| data      | VMI库存看板数据列表                                          | **JSON数组** |

### 1.2.2.2 data中一个Json数据明细字段定义

| 字段名称            | 描述                           | 类型       |
| ------------------- | ------------------------------ | ---------- |
| cProdCode           | 客户物料编码                   | **String** |
| cProdName           | 客户物料名称                   | **String** |
| cProdScale          | 客户物料规格                   | **String** |
| innerCustomerCode   | 内部客户编码                   | **String** |
| innerCustomerName   | 内部客户名称                   | **String** |
| plantCode           | 工厂编码                       | **String** |
| plantName           | 工厂名称                       | **String** |
| currentInventoryQty | 当前库存量                     | **Number** |
| safeInventoryQty    | 安全库存量                     | **Number** |
| highestInventoryQty | 最高库存量                     | **Number** |
| status              | 状态 0：无效；1：有效；默认值1 | **Number** |
| storeCode           | 仓库编码                       | **String** |
| storeName           | 仓库名称                       | **String** |
| locationCode        | 库位编码                       | **String** |
| locationName        | 库位名称                       | **String** |
| erpCategoryCode     | ERP中分类编码                  | **String** |
| erpCategoryName     | ERP中分类名称                  | **String** |
| erpStorageDate      | 入库日期                       | **Number** |
| extendN01           | 自定义字段                     | **String** |
| extendN02           | 自定义字段                     | **String** |
| extendN03           | 自定义字段                     | **String** |
| prodFeature         | 产品特征                       | **String** |
| storeUnitCode       | 库存单位编码                   | **String** |
| storeUnitName       | 库存单位名称                   | **String** |
| batchNo             | 批次号                         | **String** |
| lateDeliveryDate    | 最近送货时间                   | **Number** |
| lateDeliveryQty     | 最近送货数量                   | **Number** |
| dnXkNo              | 送货单号                       | **String** |

### 1.2.3 查询返回示例

Demo

```
    
{
    "result": 1,
    "data": [
        {
            "cProdCode": "0418001",
            "cProdName": "品名",
            "cProdScale": "测试1801",
            "innerCustomerCode": "205",
            "innerCustomerName": "百度深圳-205",
            "plantCode": null,
            "plantName": null,
            "currentInventoryQty": 0.00000000,
            "safeInventoryQty": 1.00000000,
            "highestInventoryQty": 10000.00000000,
            "status": null,
            "storeCode": "001",
            "storeName": null,
            "locationCode": null,
            "locationName": null,
            "erpCategoryCode": null,
            "erpCategoryName": null,
            "erpStorageDate": null,
            "extendN01": null,
            "extendN02": null,
            "extendN03": null,
            "prodFeature": null,
            "storeUnitCode": null,
            "storeUnitName": null,
            "batchNo": null
        },
        {
            "cProdCode": "0418001",
            "cProdName": "品名",
            "cProdScale": "测试1801",
            "innerCustomerCode": "205",
            "innerCustomerName": "百度深圳-205",
            "plantCode": null,
            "plantName": null,
            "currentInventoryQty": 2.00000000,
            "safeInventoryQty": 2.00000000,
            "highestInventoryQty": 400.00000000,
            "status": null,
            "storeCode": "007",
            "storeName": null,
            "locationCode": null,
            "locationName": null,
            "erpCategoryCode": null,
            "erpCategoryName": null,
            "erpStorageDate": null,
            "extendN01": null,
            "extendN02": null,
            "extendN03": null,
            "prodFeature": null,
            "storeUnitCode": null,
            "storeUnitName": null,
            "batchNo": null
        }
    ]
}
    
```

