---
module: "Sys"
name_zh: "系统主页"
database: "E10_3.0.0.2_CHS"
server: "SQLEXPRESS"
tables: 15
columns: 266
category: system
tags: ["ERP", "E10", "system"]
created: 2026-06-25 10:52
---

# Sys (系统主页)

> [!info] Database Info
> Database: E10_3.0.0.2_CHS | **Server**: .\SQLEXPRESS | **Tables**: 1,989 | **Columns**: 90599
> Tables: 15 | Columns: 266

## Related Modules

- [[ADMIN (行政组织)|ADMIN (行政组织)]]
- [[AUTH (权限控制)|AUTH (权限控制)]]
- [[DATA (数据管理)|DATA (数据管理)]]
- [[EASYFLOW (签核流程)|EASYFLOW (签核流程)]]
- [[FUNCTION (功能信息)|FUNCTION (功能信息)]]
- [[HISTORY (历史记录)|HISTORY (历史记录)]]
- [[MENU (菜单管理)|MENU (菜单管理)]]
- [[NOTE (备忘录)|NOTE (备忘录)]]

---

## Tables


- **Sys_Hp_Applications (Sys_Hp_Applications)**
- **Sys_Hp_Message (实时消息)**
- **Sys_Hp_News (公告新闻)**
- **Sys_Hp_News_AuthUser (可下载附件用户集合)**
- **Sys_Hp_Paths (Sys_Hp_Paths)**
- **Sys_Hp_Personalizations (Sys_Hp_Personalizations)**
- **Sys_Hp_Receiver (接收用户集合)**
- **Sys_Hp_Schedule (个人行事历)**
- **Sys_Hp_Tabpages (用户页签管理)**
- **Sys_MessageQuota (用户消息配额)**
- **Sys_MessageSetting (消息系统参数)**
- **SYS_QUERY (公用查询方案)**
- **Sys_ReceivedMessage (收件箱)**
- **Sys_SendedMessage (发件箱)**
- **Sys_SendedMessageReceiver**


---


---


> Tables: 15

### Sys_Hp_Applications (Sys_Hp_Applications)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | ApplicationId | 主键 | GUID | Y | Y |
| 2 | ApplicationName |  | string(512) | Y |  |
| 3 | LoweredApplicationName |  | string(512) | Y |  |
| 4 | Description |  | string(512) | Y |  |
| 5 | CreateDate | 创建日期 | date | Y |  |
| 6 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 7 | ModifiedDate | 修改日期 | date | Y |  |
| 8 | CreateBy | 创建者 | GUID | Y |  |
| 9 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 10 | ModifiedBy | 修改者 | GUID | Y |  |
| 11 | Attachments | 附件 | string | Y |  |
| 12 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 13 | Version | 版本号，不要随意更改 | binary | Y |  |

### Sys_Hp_Message (实时消息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | MessageId | 主键 | GUID | Y | Y |
| 2 | Content | 消息内容 | string(2000) | Y |  |
| 3 | ContentType | 消息类型 | string(100) | Y |  |
| 4 | UserId | 发送者Id | string(80) | Y |  |
| 5 | SendDate | 发布时间 | date | Y |  |
| 6 | IsSendToAll | 是否给所有人 | number(0/1) | Y |  |
| 7 | CreateDate | 创建日期 | date | Y |  |
| 8 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 9 | ModifiedDate | 修改日期 | date | Y |  |
| 10 | CreateBy | 创建者 | GUID | Y |  |
| 11 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 12 | ModifiedBy | 修改者 | GUID | Y |  |
| 13 | Attachments | 附件 | string | Y |  |
| 14 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 15 | Version | 版本号，不要随意更改 | binary | Y |  |

### Sys_Hp_News (公告新闻)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | NewsId | 主键 | GUID | Y | Y |
| 2 | Title | 消息标题 | string(160) | Y |  |
| 3 | Content | 消息内容 | string | Y |  |
| 4 | UserId | 发布者Id | string(80) | Y |  |
| 5 | PublishDate | 发布时间 | date | Y |  |
| 6 | Category | 分类 | string(20) | Y |  |
| 7 | IsLapsed | 是否已失效 | number(0/1) | Y |  |
| 8 | IsPublic | 是否是公共下载的附件 | number(0/1) | Y |  |
| 9 | Attachments | 附件 | string | Y |  |
| 10 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 11 | Version | 版本号，不要随意更改 | binary | Y |  |
| 12 | CreateDate | 创建日期 | date | Y |  |
| 13 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 14 | ModifiedDate | 修改日期 | date | Y |  |
| 15 | CreateBy | 创建者 | GUID | Y |  |
| 16 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 17 | ModifiedBy | 修改者 | GUID | Y |  |

### Sys_Hp_News_AuthUser (可下载附件用户集合)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | AuthUserId | 主键 | GUID | Y | Y |
| 2 | UserId | 下载者Id | string(80) | Y |  |
| 3 | DownloadDate | 下载时间 | date | Y |  |
| 4 | Version | 版本号，不要随意更改 | binary | Y |  |
| 5 | CreateDate | 创建日期 | date | Y |  |
| 6 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 7 | ModifiedDate | 修改日期 | date | Y |  |
| 8 | CreateBy | 创建者 | GUID | Y |  |
| 9 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 10 | ModifiedBy | 修改者 | GUID | Y |  |
| 11 | NewsId |  | GUID | Y |  |

### Sys_Hp_Paths (Sys_Hp_Paths)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | PathId | 主键 | GUID | Y | Y |
| 2 | ApplicationId | ApplicationId | GUID | Y |  |
| 3 | Path |  | string(512) | Y |  |
| 4 | LoweredPath |  | string(512) | Y |  |
| 5 | CreateDate | 创建日期 | date | Y |  |
| 6 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 7 | ModifiedDate | 修改日期 | date | Y |  |
| 8 | CreateBy | 创建者 | GUID | Y |  |
| 9 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 10 | ModifiedBy | 修改者 | GUID | Y |  |
| 11 | Attachments | 附件 | string | Y |  |
| 12 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 13 | Version | 版本号，不要随意更改 | binary | Y |  |

### Sys_Hp_Personalizations (Sys_Hp_Personalizations)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | PersonalizationId | 主键 | GUID | Y | Y |
| 2 | PathId | PathId | GUID | Y |  |
| 3 | UserId | UserId | string(80) | Y |  |
| 4 | PageSettings |  | binary |  |  |
| 5 | LastUpdatedDate |  | date | Y |  |
| 6 | CreateDate | 创建日期 | date | Y |  |
| 7 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 8 | ModifiedDate | 修改日期 | date | Y |  |
| 9 | CreateBy | 创建者 | GUID | Y |  |
| 10 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 11 | ModifiedBy | 修改者 | GUID | Y |  |
| 12 | Attachments | 附件 | string | Y |  |
| 13 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 14 | Version | 版本号，不要随意更改 | binary | Y |  |

### Sys_Hp_Receiver (接收用户集合)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | ReceiverId | 主键 | GUID | Y | Y |
| 2 | UserId | 发送者Id | string(80) | Y |  |
| 3 | ReceiveDate | 接收读取时间 | date | Y |  |
| 4 | IsRead | 是否读取过 | number(0/1) | Y |  |
| 5 | CreateDate | 创建日期 | date | Y |  |
| 6 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 7 | ModifiedDate | 修改日期 | date | Y |  |
| 8 | CreateBy | 创建者 | GUID | Y |  |
| 9 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 10 | ModifiedBy | 修改者 | GUID | Y |  |
| 11 | Version | 版本号，不要随意更改 | binary | Y |  |
| 12 | MessageId |  | GUID | Y |  |

### Sys_Hp_Schedule (个人行事历)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | ScheduleId | 主键 | GUID | Y | Y |
| 2 | Subject | 主题 | string(160) | Y |  |
| 3 | Description | 任务说明 | string(3200) | Y |  |
| 4 | Location | 关联位置 | string(160) | Y |  |
| 5 | EventType | 任务类型 | string(160) | Y |  |
| 6 | Label | 任务归类 | string(80) | Y |  |
| 7 | Status | 状态 | string(80) | Y |  |
| 8 | ResourceId | 关联资源ID | string(80) | Y |  |
| 9 | StartTime | 开始时间 | date | Y |  |
| 10 | EndTime | 结束时间 | date | Y |  |
| 11 | AllDay | 是否整日任务 | number(0/1) | Y |  |
| 12 | RecurrenceInfo | 任务重复信息 | string(400) | Y |  |
| 13 | ReminderInfo | 任务提醒 | string(400) | Y |  |
| 14 | UserId | 关联用户ID | string(80) | Y |  |
| 15 | CreateDate | 创建日期 | date | Y |  |
| 16 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 17 | ModifiedDate | 修改日期 | date | Y |  |
| 18 | CreateBy | 创建者 | GUID | Y |  |
| 19 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 20 | ModifiedBy | 修改者 | GUID | Y |  |
| 21 | Attachments | 附件 | string | Y |  |
| 22 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 23 | Version | 版本号，不要随意更改 | binary | Y |  |

### Sys_Hp_Tabpages (用户页签管理)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | TabId | 主键 | GUID | Y | Y |
| 2 | TabCode | 标签编码 | string(80) | Y |  |
| 3 | TabName | 标签名称 | string(80) | Y |  |
| 4 | TabTitle | 标签标题 | string(80) | Y |  |
| 5 | ZoneColumnCount | 标签列数 | number | Y |  |
| 6 | ZoneColumnType | 标签列数版式 | number | Y |  |
| 7 | UserId | ID | string(80) | Y |  |
| 8 | TabCreateDate | TabCreateDate | date | Y |  |
| 9 | CreateDate | 创建日期 | date | Y |  |
| 10 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 11 | ModifiedDate | 修改日期 | date | Y |  |
| 12 | CreateBy | 创建者 | GUID | Y |  |
| 13 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 14 | ModifiedBy | 修改者 | GUID | Y |  |
| 15 | Attachments | 附件 | string | Y |  |
| 16 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 17 | Version | 版本号，不要随意更改 | binary | Y |  |

### Sys_MessageQuota (用户消息配额)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Sys_MessageQuota_ID | 主键 | GUID | Y | Y |
| 2 | LogOnName | 用户登录名 | string(80) | Y |  |
| 3 | UserId | 引用User表主键 | GUID | Y |  |
| 4 | Quota | 配额 | number(8,2) | Y |  |
| 5 | Used | 已用额度 | number(18,2) | Y |  |
| 6 | CreateDate | 创建日期 | date | Y |  |
| 7 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 8 | ModifiedDate | 修改日期 | date | Y |  |
| 9 | CreateBy | 创建者 | GUID | Y |  |
| 10 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 11 | ModifiedBy | 修改者 | GUID | Y |  |
| 12 | Attachments | 附件 | string | Y |  |
| 13 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 14 | Version | 版本号，不要随意更改 | binary | Y |  |
| 15 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 16 | ApproveDate | 修改日期 | date | Y |  |
| 17 | ApproveBy | 修改人 | GUID | Y |  |

### Sys_MessageSetting (消息系统参数)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Sys_MessageSetting_ID | 主键 | GUID | Y | Y |
| 2 | DefaultQuota | 默认配额 | number(18,0) | Y |  |
| 3 | RefreshSecond | 刷新时间 | number | Y |  |
| 4 | IsForwardToPortal | 是否转发至Portal | number(0/1) | Y |  |
| 5 | Attachments | 附件 | string | Y |  |
| 6 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 7 | Version | 版本号，不要随意更改 | binary | Y |  |
| 8 | CreateDate | 创建日期 | date | Y |  |
| 9 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 10 | ModifiedDate | 修改日期 | date | Y |  |
| 11 | CreateBy | 创建者 | GUID | Y |  |
| 12 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 13 | ModifiedBy | 修改者 | GUID | Y |  |
| 14 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 15 | ApproveDate | 修改日期 | date | Y |  |
| 16 | ApproveBy | 修改人 | GUID | Y |  |

### SYS_QUERY (公用查询方案)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SYS_QUERY_ID | 主键 | GUID | Y | Y |
| 2 | SYS_QUERY_CODE | 编号 | string(20) | Y |  |
| 3 | SYS_QUERY_NAME | 名称 | string(120) | Y |  |
| 4 | CreateDate | 创建日期 | date | Y |  |
| 5 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 6 | ModifiedDate | 修改日期 | date | Y |  |
| 7 | CreateBy | 创建者 | GUID | Y |  |
| 8 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 9 | ModifiedBy | 修改者 | GUID | Y |  |
| 10 | Attachments | 附件 | string | Y |  |
| 11 | UDF001 | 自定义字段0 | number(23,8) | Y |  |
| 12 | UDF002 | 自定义字段1 | number(23,8) | Y |  |
| 13 | UDF003 | 自定义字段2 | number(23,8) | Y |  |
| 14 | UDF011 | 自定义字段3 | number(16,6) | Y |  |
| 15 | UDF012 | 自定义字段4 | number(16,6) | Y |  |
| 16 | UDF013 | 自定义字段5 | number(16,6) | Y |  |
| 17 | UDF021 | 自定义字段6 | string(510) | Y |  |
| 18 | UDF022 | 自定义字段7 | string(510) | Y |  |
| 19 | UDF023 | 自定义字段8 | string(510) | Y |  |
| 20 | UDF024 | 自定义字段9 | string(510) | Y |  |
| 21 | UDF025 | 自定义字段10 | string(510) | Y |  |
| 22 | UDF026 | 自定义字段11 | string(510) | Y |  |
| 23 | UDF041 | 自定义字段12 | date | Y |  |
| 24 | UDF042 | 自定义字段13 | date | Y |  |
| 25 | UDF051 | 自定义字段14 | GUID | Y |  |
| 26 | UDF052 | 自定义字段15 | GUID | Y |  |
| 27 | UDF053 | 自定义字段16 | GUID | Y |  |
| 28 | UDF054 | 自定义字段17 | GUID | Y |  |
| 29 | ProcessInstanceId | 表单所在的流程实例的编号 | GUID | Y |  |
| 30 | Version | 版本号，不要随意更改 | binary | Y |  |
| 31 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 32 | ApproveDate | 修改日期 | date | Y |  |
| 33 | ApproveBy | 修改人 | GUID | Y |  |

### Sys_ReceivedMessage (收件箱)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Sys_ReceivedMessage_ID | 主键 | GUID | Y | Y |
| 2 | PureText | 消息内容纯文本 | string(8000) | Y |  |
| 3 | Format | 消息格式：Html/Rtf | number | Y |  |
| 4 | Content | 消息内容富文本 | string | Y |  |
| 5 | Source | 消息来源：E10System/E10User/BEP | string(400) | Y |  |
| 6 | MessageType | 消息类型：异常/警告/普通 | number | Y |  |
| 7 | EventCode | 消息分类编号（可存放BEP事件编号） | string(400) | Y |  |
| 8 | EventName | 消息分类名称（可存放BEP事件名称） | string(400) | Y |  |
| 9 | Sender | 发送人LogOnName | string(80) | Y |  |
| 10 | SenderName | 发送人UserName | string(400) | Y |  |
| 11 | Size | 消息内容富文本大小，单位字节 | number | Y |  |
| 12 | Owner | 所有者，引用User表主键 | GUID | Y |  |
| 13 | ReceiveTime | 接收时间 | date | Y |  |
| 14 | IsRead | 是否已读 | number | Y |  |
| 15 | CreateDate | 创建日期 | date | Y |  |
| 16 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 17 | ModifiedDate | 修改日期 | date | Y |  |
| 18 | CreateBy | 创建者 | GUID | Y |  |
| 19 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 20 | ModifiedBy | 修改者 | GUID | Y |  |
| 21 | Attachments | 附件 | string | Y |  |
| 22 | Version | 版本号，不要随意更改 | binary | Y |  |
| 23 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 24 | ApproveDate | 修改日期 | date | Y |  |
| 25 | ApproveBy | 修改人 | GUID | Y |  |

### Sys_SendedMessage (发件箱)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Sys_SendedMessage_ID | 主键 | GUID | Y | Y |
| 2 | PureText | 消息内容纯文本 | string(8000) | Y |  |
| 3 | Format | 消息格式：Html/Rtf | number | Y |  |
| 4 | Content | 消息内容富文本 | string | Y |  |
| 5 | Source | 消息来源：E10System/E10User/BEP | string(400) | Y |  |
| 6 | MessageType | 消息类型：异常/警告/普通 | number | Y |  |
| 7 | EventCode | 消息分类编号（可存放BEP事件编号） | string(400) | Y |  |
| 8 | EventName | 消息分类名称（可存放BEP事件名称） | string(400) | Y |  |
| 9 | Status | 收发标志:发送成功/发送失败/草稿 | number | Y |  |
| 10 | Sender | 发送人LogOnName | string(80) | Y |  |
| 11 | SenderName | 发送人UserName | string(400) | Y |  |
| 12 | Size | 消息内容富文本大小，单位字节 | number | Y |  |
| 13 | Owner | 所有者，引用User表主键 | GUID | Y |  |
| 14 | CreateTime | 创建消息时间 | date | Y |  |
| 15 | SendTime | 发送时间 | date | Y |  |
| 16 | Receivers | 冗余字段收件人 | string(8000) | Y |  |
| 17 | ReceiverNames | 冗余字段收件人名 | string(8000) | Y |  |
| 18 | FailureReason | 发送失败原因 | string(8000) | Y |  |
| 19 | CreateDate | 创建日期 | date | Y |  |
| 20 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 21 | ModifiedDate | 修改日期 | date | Y |  |
| 22 | CreateBy | 创建者 | GUID | Y |  |
| 23 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 24 | ModifiedBy | 修改者 | GUID | Y |  |
| 25 | Attachments | 附件 | string | Y |  |
| 26 | Version | 版本号，不要随意更改 | binary | Y |  |
| 27 | ApproveStatus | 单据状态属性 | string(2) | Y |  |
| 28 | ApproveDate | 修改日期 | date | Y |  |
| 29 | ApproveBy | 修改人 | GUID | Y |  |

### Sys_SendedMessageReceiver

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | ReceiverId |  | GUID | Y | Y |
| 2 | Receiver | 接收人LogOnName | string(80) | Y |  |
| 3 | ReceiverName | 接收人UserName | string(400) | Y |  |
| 4 | CreateDate | 创建日期 | date | Y |  |
| 5 | LastModifiedDate | 最后修改日期 | date | Y |  |
| 6 | ModifiedDate | 修改日期 | date | Y |  |
| 7 | CreateBy | 创建者 | GUID | Y |  |
| 8 | LastModifiedBy | 最后修改者 | GUID | Y |  |
| 9 | ModifiedBy | 修改者 | GUID | Y |  |
| 10 | Version | 版本号，不要随意更改 | binary | Y |  |
| 11 | Sys_SendedMessage_ID |  | GUID | Y |  |