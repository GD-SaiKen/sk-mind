---
module: "WF"
name_zh: "工作流引擎"
database: "E10_3.0.0.2_CHS"
server: "SQLEXPRESS"
tables: 46
columns: 533
category: system
tags: ["ERP", "E10", "system"]
created: 2026-06-25 10:52
---

# WF (工作流引擎)

> [!info] Database Info
> Database: E10_3.0.0.2_CHS | **Server**: .\SQLEXPRESS | **Tables**: 1,989 | **Columns**: 90599
> Tables: 46 | Columns: 533

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


- **WF_ActivityAttachmentInfo (活动上的附件信息)**
- **WF_ActivityDefRef (对活动定义的引用)**
- **WF_ActivityPerformer (表示对活动或者流程中参与者的定义引用)**
- **WF_AttachmentInstance (附件实例信息)**
- **WF_AttachmentInstanceLog (附件实例信息单身，记录操作日志)**
- **WF_CompositeActivity (组合活动定义)**
- **WF_CustomActivityDefRef (对活动定义的引用)**
- **WF_CustomOvertimeNotifyTarget (表示对活动或者流程中参与者的定义引用)**
- **WF_CustomProcessDefinition (自定义流程定义)**
- **WF_CustomProcessPackage (自定义流程包的定义，包含一个主流程和若干子流程)**
- **WF_CustomTransition (活动之间的转移)**
- **WF_DecisionLevelAttachmentInfo (核决层级上的附件信息)**
- **WF_DecisionLevelVariableRef (核决层级对变量的引用)**
- **WF_DecisionRuleActivityDef (核决权限活动定义)**
- **WF_DecisionRuleActivityIns**
- **WF_DecisionRuleCondition (核决权限条件)**
- **WF_DecisionRuleLevel (核决活动内部核决层级)**
- **WF_Gateway (分流或合流活动)**
- **WF_InvokeActivityDef (Invoke活动定义)**
- **WF_InvokeActivityIns**
- **WF_InvokedExpression (Invoke活动调用完成之后执行的脚本表达式)**
- **WF_InvokeParameterDef (Invoke活动执行时的参数定义)**
- **WF_Notification**
- **WF_NotificationDefinition (流程或活动的相关通知的定义)**
- **WF_OvertimeNotifyTarget (表示对活动或者流程中参与者的定义引用)**
- **WF_ParticipantActivityDef (参与者活动定义)**
- **WF_ParticipantActivityIns**
- **WF_ParticipantDefinition (活动或者流程中参与者的定义)**
- **WF_ProcessContext**
- **WF_ProcessDefinition (流程定义)**
- **WF_ProcessInstance (流程实例)**
- **WF_ProcessPackage (流程包的定义，包含一个主流程和若干子流程)**
- **WF_ProcessPackageCategory (流程包的分类)**
- **WF_Scope**
- **WF_SubflowActivity (子流程活动定义)**
- **WF_SubflowActivityIns**
- **WF_Transition (活动之间的转移)**
- **WF_UnreexcuteActivity (对活动定义的引用)**
- **WF_Variable**
- **WF_VariableDefinition (流程变量的定义)**
- **WF_VariableDefRef (对变量定义的引用)**
- **WF_VariableMapping (子流程变量与主流程变量之间的映射)**
- **WF_VariableRef**
- **WF_WorkAssignment**
- **WF_WorkItem**
- **WF_WorkStep**


---


---


> Tables: 46

### WF_ActivityAttachmentInfo (活动上的附件信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | AddPolicy | 添加的限制策略 | number |  |  |
| 2 | AddCount | 允许添加的数量 | number |  |  |
| 3 | ViewPolicy | 查看的限制策略 | number |  |  |
| 4 | Editable | 是否允许编辑 | number(0/1) |  |  |
| 5 | Deletable | 是否允许删除 | number(0/1) |  |  |
| 6 | ActivityDefinitionType | 引用变量的活动定义的TypeKey | string(400) |  |  |
| 7 | ActivityDefinitionId | 引用变量的活动定义的Id | GUID |  |  |
| 8 | VariableDefinitionId | 引用的变量定义的Id | GUID |  |  |
| 9 | SceneId | 如果是表单变量的话，记录表单的场景Id | GUID |  |  |
| 10 | EditState | 如果是表单变量的话，记录进入该表单的状态 | number |  |  |
| 11 | Id | 对象的主键 | GUID | Y | Y |
| 12 | Version | 对象的版本号 | binary | Y |  |
| 13 | F_Id |  | GUID | Y |  |

### WF_ActivityDefRef (对活动定义的引用)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | ActivityDefinitionType | 引用的活动定义的TypeKey | string(400) |  |  |
| 2 | ActivityDefinitionId | 引用的活动定义的Id | GUID |  |  |
| 3 | Id | 对象的主键 | GUID | Y | Y |
| 4 | Version | 对象的版本号 | binary | Y |  |
| 5 | F_Id |  | GUID | Y |  |

### WF_ActivityPerformer (表示对活动或者流程中参与者的定义引用)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | ParticipantDefinitionId | 要引用的参与者的定义的Id | GUID |  |  |
| 2 | Id | 对象的主键 | GUID | Y | Y |
| 3 | Version | 对象的版本号 | binary | Y |  |
| 4 | F_Id |  | GUID | Y |  |

### WF_AttachmentInstance (附件实例信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | AttachmentTypeId | 对应流程上附件变量的Id | GUID |  |  |
| 2 | ProcessInstanceId | 对应流程实例的Id | GUID |  |  |
| 3 | AttachmentId | 实际的BigObjectInfo的Id | GUID |  |  |
| 4 | Id | 对象的主键 | GUID | Y | Y |
| 5 | Version | 对象的版本号 | binary | Y |  |

### WF_AttachmentInstanceLog (附件实例信息单身，记录操作日志)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | ActivityInstanceId | 对附件进行操作的活动实例的Id | GUID |  |  |
| 2 | WorkItemId | 关联的工作项的Id | GUID |  |  |
| 3 | WorkAssignmentId | 关联的工作指派的Id | GUID |  |  |
| 4 | OperateType | 对附件进行的操作类型 | number |  |  |
| 5 | OperateTime | 对附件进行操作的时间点 | date |  |  |
| 6 | Temporary | 该附件是否是临时的 | number(0/1) |  |  |
| 7 | Id | 对象的主键 | GUID | Y | Y |
| 8 | Version | 对象的版本号 | binary | Y |  |
| 9 | F_Id |  | GUID | Y |  |

### WF_CompositeActivity (组合活动定义)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | OriginalDefinitionId | 原始容器定义Id | GUID |  |  |
| 2 | ProcessDefinitionId | 所属的流程定义的Id | GUID |  |  |
| 3 | OwnerId | 所属的上级定义的Id，当活动直接属于流程时，其上一级为流程，当活动属于组合活动（如核决活动）时，其上一级为组合活动 | GUID |  |  |
| 4 | OwnerType | 所属的上级定义的类型TypeKey，当活动直接属于流程时，其上一级为流程，当活动属于组合活动（如核决活动）时，其上一级为组合活动 | string(400) |  |  |
| 5 | DisplayName | 对象的显示名 | string(400) |  |  |
| 6 | Id | 对象的主键 | GUID | Y | Y |
| 7 | Version | 对象的版本号 | binary | Y |  |

### WF_CustomActivityDefRef (对活动定义的引用)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | ActivityDefinitionType | 引用的活动定义的TypeKey | string(400) |  |  |
| 2 | ActivityDefinitionId | 引用的活动定义的Id | GUID |  |  |
| 3 | Id | 对象的主键 | GUID | Y | Y |
| 4 | Version | 对象的版本号 | binary | Y |  |
| 5 | F_Id |  | GUID | Y |  |

### WF_CustomOvertimeNotifyTarget (表示对活动或者流程中参与者的定义引用)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | ParticipantDefinitionId | 要引用的参与者的定义的Id | GUID |  |  |
| 2 | Id | 对象的主键 | GUID | Y | Y |
| 3 | Version | 对象的版本号 | binary | Y |  |
| 4 | F_Id |  | GUID | Y |  |

### WF_CustomProcessDefinition (自定义流程定义)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | ProcessPackageId | 所属流程包的Id | GUID |  |  |
| 2 | Type | 流程定义的类别，是标准流程还是自定义流程 | number |  |  |
| 3 | AutoCoding | 流程是否自动编号，默认true | number(0/1) |  |  |
| 4 | Abortable | 流程是否可被撤销(抽单) | number(0/1) |  |  |
| 5 | AbortReasonNotEmpty | 流程被撤销时，撤销流程原因是否必填 | number(0/1) |  |  |
| 6 | CreatedTime | 流程的创建时间 | date |  |  |
| 7 | TimeLimit | 流程的处理时限，时间单位小时(工作日时间) | number(18,0) |  |  |
| 8 | OvertimeNotifyInterval | 流程超时时，发送超时警告的时间间隔，单位小时 | number(18,0) |  |  |
| 9 | OvertimeNotifyTimes | 流程超时时，发送超时警告的次数 | number |  |  |
| 10 | OvertimeNotify | 流程超时时，是否发送超时警告 | number(0/1) |  |  |
| 11 | OvertimeNotificationId | 超时警告的通知定义的Id | GUID |  |  |
| 12 | AbortedNotify | 流程被撤销时是否逐层通知 | number(0/1) |  |  |
| 13 | AbortedNotificationId | 流程被撤销时的通知定义Id | GUID |  |  |
| 14 | ClosedNotifyMode | 流程结案时逐层通知的方式 | number |  |  |
| 15 | ClosedNotificationId | 流程结案时的通知定义Id | GUID |  |  |
| 16 | TerminatedNotify | 流程终止时是否逐层通知 | number(0/1) |  |  |
| 17 | TerminatedNotificationId | 流程终止时的通知定义Id | GUID |  |  |
| 18 | RegainedNotify | 是否要在处理者撤签时逐级通知流程处理者 | number(0/1) |  |  |
| 19 | RegainedNotificationId | 处理者撤签时的通知定义Id | GUID |  |  |
| 20 | ReexecutedNotify | 是否要在处理者退回重办工作时逐级通知流程处理者 | number(0/1) |  |  |
| 21 | ReexecutedNotificationId | 处理者退回重办工作时的通知定义Id | GUID |  |  |
| 22 | CountersignedNotify | 是否在加签时通知发起人 | number(0/1) |  |  |
| 23 | CountersignedNotificationId | 处理者加签时的通知定义Id | GUID |  |  |
| 24 | RelationManDefId | 流程定义之关系人的参与者定义Id | GUID |  |  |
| 25 | Description | 流程定义的描述 | string(400) |  |  |
| 26 | OriginalDefinitionId | 原始容器定义Id | GUID |  |  |
| 27 | ProcessDefinitionId | 所属的流程定义的Id | GUID |  |  |
| 28 | OwnerId | 所属的上级定义的Id，当活动直接属于流程时，其上一级为流程，当活动属于组合活动（如核决活动）时，其上一级为组合活动 | GUID |  |  |
| 29 | OwnerType | 所属的上级定义的类型TypeKey，当活动直接属于流程时，其上一级为流程，当活动属于组合活动（如核决活动）时，其上一级为组合活动 | string(400) |  |  |
| 30 | DisplayName | 对象的显示名 | string(400) |  |  |
| 31 | Id | 对象的主键 | GUID | Y | Y |
| 32 | Version | 对象的版本号 | binary | Y |  |

### WF_CustomProcessPackage (自定义流程包的定义，包含一个主流程和若干子流程)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | MainProcessDefinitionId | 流程包中的主流程定义的Id | GUID |  |  |
| 2 | Code | 流程包的编码 | string(400) |  |  |
| 3 | CategoryId | 流程分类Id | GUID |  |  |
| 4 | SubjectTemplate | 流程主题的模板定义 | string(400) |  |  |
| 5 | SubjectDefineMode | 流程发起时用户对主题的定义方式 | number |  |  |
| 6 | CreatedTime | 流程包的创建时间 | date |  |  |
| 7 | CreatorId | 流程包的创建人 | GUID |  |  |
| 8 | PublicationState | 流程包的发行状态 | number |  |  |
| 9 | Vender | 流程供应商的名称 | string(400) |  |  |
| 10 | XpdlVersion | 流程定义符合的XPDL版本 | string(400) |  |  |
| 11 | Description | 流程包描述 | string(400) |  |  |
| 12 | VersionNumber | 流程的版本号码 | number |  |  |
| 13 | ValidFrom | 流程定义的有效期开始时间 | date |  |  |
| 14 | ValidTo | 流程定义的有效期结束时间 | date |  |  |
| 15 | NeedControlAuthority | 是否需要控制权限 | number(0/1) |  |  |
| 16 | DisplayName | 对象的显示名 | string(400) |  |  |
| 17 | Id | 对象的主键 | GUID | Y | Y |
| 18 | Version | 对象的版本号 | binary | Y |  |

### WF_CustomTransition (活动之间的转移)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | ConditionType | 转移上定义的条件的类别 | number |  |  |
| 2 | ConditionContent | 转移上定义的条件表达式 | string(6000) |  |  |
| 3 | FromActivityDefinitionType | 转移出发的活动定义的TypeKey | string(400) |  |  |
| 4 | FromActivityDefinitionId | 转移出发的活动定义的Id | GUID |  |  |
| 5 | ToActivityDefinitionType | 转移到达的活动定义的TypeKey | string(400) |  |  |
| 6 | ToActivityDefinitionId | 转移到达的活动定义的Id | GUID |  |  |
| 7 | DisplayName | 对象的显示名 | string(400) |  |  |
| 8 | Id | 对象的主键 | GUID | Y | Y |
| 9 | Version | 对象的版本号 | binary | Y |  |
| 10 | F_Id |  | GUID | Y |  |

### WF_DecisionLevelAttachmentInfo (核决层级上的附件信息)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | AddPolicy | 添加的限制策略 | number |  |  |
| 2 | AddCount | 允许添加的数量 | number |  |  |
| 3 | ViewPolicy | 查看的限制策略 | number |  |  |
| 4 | Editable | 是否允许编辑 | number(0/1) |  |  |
| 5 | Deletable | 是否允许删除 | number(0/1) |  |  |
| 6 | VariableDefinitionId | 引用的变量定义的Id | GUID |  |  |
| 7 | SceneId | 如果是表单变量的话，记录表单的场景Id | GUID |  |  |
| 8 | EditState | 如果是表单变量的话，记录进入该表单的状态 | number |  |  |
| 9 | Id | 对象的主键 | GUID | Y | Y |
| 10 | Version | 对象的版本号 | binary | Y |  |
| 11 | F_Id |  | GUID | Y |  |

### WF_DecisionLevelVariableRef (核决层级对变量的引用)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | VariableDefinitionId | 引用的变量定义的Id | GUID |  |  |
| 2 | SceneId | 如果是表单变量的话，记录表单的场景Id | GUID |  |  |
| 3 | EditState | 如果是表单变量的话，记录进入该表单的状态 | number |  |  |
| 4 | Id | 对象的主键 | GUID | Y | Y |
| 5 | Version | 对象的版本号 | binary | Y |  |
| 6 | F_Id |  | GUID | Y |  |

### WF_DecisionRuleActivityDef (核决权限活动定义)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | DecisionType | 核决层级类型 | number |  |  |
| 2 | Description | 核决权限活动描述 | string(400) |  |  |
| 3 | MustSignComment | 核决活动内部关卡处理人签核时是否必须填写审核意见 | number(0/1) |  |  |
| 4 | Secured | 核决活动内部关卡收到待处理的活动，需输入密码验证身份，才可进行处理 | number(0/1) |  |  |
| 5 | WorkNotificationId | 核决活动内部工作通知定义的Id，用于处理该活动时若需要发送相关通知的通知相关格式设定 | GUID |  |  |
| 6 | ReferParticipantId | 核决活动参考的参与者编号 | GUID |  |  |
| 7 | OriginalDefinitionId | 原始容器定义Id | GUID |  |  |
| 8 | ProcessDefinitionId | 所属的流程定义的Id | GUID |  |  |
| 9 | OwnerId | 所属的上级定义的Id，当活动直接属于流程时，其上一级为流程，当活动属于组合活动（如核决活动）时，其上一级为组合活动 | GUID |  |  |
| 10 | OwnerType | 所属的上级定义的类型TypeKey，当活动直接属于流程时，其上一级为流程，当活动属于组合活动（如核决活动）时，其上一级为组合活动 | string(400) |  |  |
| 11 | DisplayName | 对象的显示名 | string(400) |  |  |
| 12 | Id | 对象的主键 | GUID | Y | Y |
| 13 | Version | 对象的版本号 | binary | Y |  |

### WF_DecisionRuleActivityIns

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | ActivityDefinitionId |  | GUID |  |  |
| 2 | State |  | number |  |  |
| 3 | CreatedTime |  | date |  |  |
| 4 | ProcessId |  | GUID |  |  |
| 5 | ContextId |  | GUID |  |  |
| 6 | ScopeId |  | GUID |  |  |
| 7 | IsFirstActivity |  | number(0/1) |  |  |
| 8 | DisplayName | 对象的显示名 | string(400) |  |  |
| 9 | Id | 对象的主键 | GUID | Y | Y |
| 10 | Version | 对象的版本号 | binary | Y |  |

### WF_DecisionRuleCondition (核决权限条件)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Condition | 条件表达式 | string(400) |  |  |
| 2 | Priority | 条件优先级 | number |  |  |
| 3 | LevelMappingString | 当前条件选中的核决层级Id集合 | string(400) |  |  |
| 4 | Id | 对象的主键 | GUID | Y | Y |
| 5 | Version | 对象的版本号 | binary | Y |  |
| 6 | F_Id |  | GUID | Y |  |

### WF_DecisionRuleLevel (核决活动内部核决层级)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | LevelName | 核决层级名称 | string(400) |  |  |
| 2 | LevelIndex | 核决层级序号 | number |  |  |
| 3 | DecisionLevelId | 全局核决层级Id | GUID |  |  |
| 4 | Id | 对象的主键 | GUID | Y | Y |
| 5 | Version | 对象的版本号 | binary | Y |  |
| 6 | F_Id |  | GUID | Y |  |

### WF_Gateway (分流或合流活动)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Type | 区分是分支还是合并 | number |  |  |
| 2 | BranchRelation | 分支的逻辑关系是And还是Or | number |  |  |
| 3 | ProcessDefinitionId | 所属的流程定义的Id | GUID |  |  |
| 4 | OwnerId | 所属的上级定义的Id，当活动直接属于流程时，其上一级为流程，当活动属于组合活动（如核决活动）时，其上一级为组合活动 | GUID |  |  |
| 5 | OwnerType | 所属的上级定义的类型TypeKey，当活动直接属于流程时，其上一级为流程，当活动属于组合活动（如核决活动）时，其上一级为组合活动 | string(400) |  |  |
| 6 | DisplayName | 对象的显示名 | string(400) |  |  |
| 7 | Id | 对象的主键 | GUID | Y | Y |
| 8 | Version | 对象的版本号 | binary | Y |  |

### WF_InvokeActivityDef (Invoke活动定义)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | ServiceUrl | 要调用的WebService地址 | string(400) |  |  |
| 2 | ServiceTypeKey | 要调用的服务的TypeKey | string(400) |  |  |
| 3 | ServiceTypeName | 要调用的服务接口类型的程序集限定名，此处固定返回Digiwin.Common.Services.IPushDownService | string(400) |  |  |
| 4 | MethodName | 要调用的服务接口中的方法名，此处固定返回Push | string(400) |  |  |
| 5 | MethodParameterTypes | 要调用的服务方法的参数类型的程序集限定名，多个时用分号;隔开，此处固定返回Digiwin.Common.Services.PushDownContext | string(400) |  |  |
| 6 | ResultVariable | 调用完成之后返回值填写到哪个流程变量 | string(400) |  |  |
| 7 | ExceptionPerformer | Invoke活动执行出错后的处理人 | GUID |  |  |
| 8 | ProcessDefinitionId | 所属的流程定义的Id | GUID |  |  |
| 9 | OwnerId | 所属的上级定义的Id，当活动直接属于流程时，其上一级为流程，当活动属于组合活动（如核决活动）时，其上一级为组合活动 | GUID |  |  |
| 10 | OwnerType | 所属的上级定义的类型TypeKey，当活动直接属于流程时，其上一级为流程，当活动属于组合活动（如核决活动）时，其上一级为组合活动 | string(400) |  |  |
| 11 | DisplayName | 对象的显示名 | string(400) |  |  |
| 12 | Id | 对象的主键 | GUID | Y | Y |
| 13 | Version | 对象的版本号 | binary | Y |  |

### WF_InvokeActivityIns

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | ActivityDefinitionId |  | GUID |  |  |
| 2 | ExceptionName |  | string(400) |  |  |
| 3 | ExceptionStackTrace |  | string |  |  |
| 4 | ExceptionMessage |  | string(8000) |  |  |
| 5 | PerformerUserId |  | GUID |  |  |
| 6 | State |  | number |  |  |
| 7 | CreatedTime |  | date |  |  |
| 8 | ProcessId |  | GUID |  |  |
| 9 | ContextId |  | GUID |  |  |
| 10 | ScopeId |  | GUID |  |  |
| 11 | IsFirstActivity |  | number(0/1) |  |  |
| 12 | DisplayName | 对象的显示名 | string(400) |  |  |
| 13 | Id | 对象的主键 | GUID | Y | Y |
| 14 | Version | 对象的版本号 | binary | Y |  |

### WF_InvokedExpression (Invoke活动调用完成之后执行的脚本表达式)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Left | 表达式的左侧 | string(400) |  |  |
| 2 | Right | 表达式的右侧 | string(400) |  |  |
| 3 | DisplayName | 对象的显示名 | string(400) |  |  |
| 4 | Id | 对象的主键 | GUID | Y | Y |
| 5 | Version | 对象的版本号 | binary | Y |  |
| 6 | F_Id |  | GUID | Y |  |

### WF_InvokeParameterDef (Invoke活动执行时的参数定义)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | ParameterDefinitionType | 真实的参数定义的类型名，非空时从该类型的实例中获取参数值 | string(600) |  |  |
| 2 | ValueExpression | 参数值的表达式 | string |  |  |
| 3 | DisplayName | 对象的显示名 | string(400) |  |  |
| 4 | Id | 对象的主键 | GUID | Y | Y |
| 5 | Version | 对象的版本号 | binary | Y |  |
| 6 | F_Id |  | GUID | Y |  |

### WF_Notification

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | OwnerType |  | string(400) |  |  |
| 2 | OwnerId |  | GUID |  |  |
| 3 | ContentType |  | number |  |  |
| 4 | CreatedTime |  | date |  |  |
| 5 | Subject |  | string(400) |  |  |
| 6 | Message |  | string(400) |  |  |
| 7 | ReceiverId |  | GUID |  |  |
| 8 | Id | 对象的主键 | GUID | Y | Y |
| 9 | Version | 对象的版本号 | binary | Y |  |

### WF_NotificationDefinition (流程或活动的相关通知的定义)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | ProcessDefinitionId | 所属的流程定义的Id | GUID |  |  |
| 2 | SendMode | 通知的发送方式，可多选，默认为SystemNotice | number |  |  |
| 3 | ContentType | 通知的类型，如流程超时警告，活动工作派送等 | number |  |  |
| 4 | SubjectTemplate | 通知的主题的模板定义 | string(400) |  |  |
| 5 | MessageTemplate | 通知的内容的模板定义 | string(400) |  |  |
| 6 | LanguageName | 通知的语言别，如CHS | string(400) |  |  |
| 7 | Id | 对象的主键 | GUID | Y | Y |
| 8 | Version | 对象的版本号 | binary | Y |  |
| 9 | MailOptions_EnableFormAttachs | 是否允许将表单作为邮件的附件发送 | number(0/1) |  |  |

### WF_OvertimeNotifyTarget (表示对活动或者流程中参与者的定义引用)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | ParticipantDefinitionId | 要引用的参与者的定义的Id | GUID |  |  |
| 2 | Id | 对象的主键 | GUID | Y | Y |
| 3 | Version | 对象的版本号 | binary | Y |  |
| 4 | F_Id |  | GUID | Y |  |

### WF_ParticipantActivityDef (参与者活动定义)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | UnreexecuteType | 不可退回的活动列表的类型，是包含还是排除 | number |  |  |
| 2 | PerformType | 活动的处理方式，决定活动的处理者可以做的操作 | number |  |  |
| 3 | MultiUserMode | 当此活动由多人处理时，处理工作时的模式，是都要处理还是只要一人处理 | number |  |  |
| 4 | MustSignComment | 处理人签核时是否必须填写审核意见 | number(0/1) |  |  |
| 5 | Secured | 收到待处理的活动，需输入密码验证身份，才可进行处理 | number(0/1) |  |  |
| 6 | ManualBypassable | 该活动可否被手动bypass | number(0/1) |  |  |
| 7 | AutoBypassable | 该活动可否被系统自动进行bypass动作 | number(0/1) |  |  |
| 8 | BypassMode | 活动被bypass时的方式：给代理人或下一活动 | number |  |  |
| 9 | MustPerformed | 活动被bypass后是否必须被处理人处理流程才能结束 | number(0/1) |  |  |
| 10 | AllowCarbonCopy | 处理人是否可以将流程抄送给流程以外人员 | number(0/1) |  |  |
| 11 | Limits | 处理人收到待处理流程到完成处理的时间限定。单位小时 | number(18,0) |  |  |
| 12 | ExtraLimits | 处理人收到待处理流程到完成处理的可超出时间限定。单位小时 | number(18,0) |  |  |
| 13 | TipMessage | 处理人打开待处理流程时弹出的流程提示信息 | string(400) |  |  |
| 14 | BatchPerformable | 活动是否允许批次签核 | number(0/1) |  |  |
| 15 | AskReexecuteType | 处理者退回重办的方式 | number |  |  |
| 16 | Regainable | 活动是否允许处理者取回重办 | number(0/1) |  |  |
| 17 | RequireSpecifyOrgUnit | 活动是否需要使用者指定需要发送的组织单位 | number(0/1) |  |  |
| 18 | AllowAddPrecursor | 活动是否允许使用者增加前一活动(向前加签) | number(0/1) |  |  |
| 19 | AllowAddSuccessor | 活动是否允许使用者增加后一活动(向后加签) | number(0/1) |  |  |
| 20 | WorkNotificationId | 工作通知定义的Id，用于处理该活动时若需要发送相关通知的通知相关格式设定 | GUID |  |  |
| 21 | ProcessDefinitionId | 所属的流程定义的Id | GUID |  |  |
| 22 | OwnerId | 所属的上级定义的Id，当活动直接属于流程时，其上一级为流程，当活动属于组合活动（如核决活动）时，其上一级为组合活动 | GUID |  |  |
| 23 | OwnerType | 所属的上级定义的类型TypeKey，当活动直接属于流程时，其上一级为流程，当活动属于组合活动（如核决活动）时，其上一级为组合活动 | string(400) |  |  |
| 24 | DisplayName | 对象的显示名 | string(400) |  |  |
| 25 | Id | 对象的主键 | GUID | Y | Y |
| 26 | Version | 对象的版本号 | binary | Y |  |

### WF_ParticipantActivityIns

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | ActivityDefinitionId |  | GUID |  |  |
| 2 | PerformType |  | number |  |  |
| 3 | MultiUserMode |  | number |  |  |
| 4 | MustSignComment |  | number(0/1) |  |  |
| 5 | MustPerformed |  | number(0/1) |  |  |
| 6 | Secured |  | number(0/1) |  |  |
| 7 | AutoBypassable |  | number(0/1) |  |  |
| 8 | ManualBypassable |  | number(0/1) |  |  |
| 9 | BypassMode |  | number |  |  |
| 10 | AllowCarbonCopy |  | number(0/1) |  |  |
| 11 | Limits |  | number(18,0) |  |  |
| 12 | ExtraLimits |  | number(18,0) |  |  |
| 13 | TipMessage |  | string(400) |  |  |
| 14 | BatchPerformable |  | number(0/1) |  |  |
| 15 | AskReexecuteType |  | number |  |  |
| 16 | Regainable |  | number(0/1) |  |  |
| 17 | RequireSpecifyOrgUnit |  | number(0/1) |  |  |
| 18 | AllowAddPrecursor |  | number(0/1) |  |  |
| 19 | AllowAddSuccessor |  | number(0/1) |  |  |
| 20 | LockStamp |  | GUID |  |  |
| 21 | Drafted |  | number(0/1) |  |  |
| 22 | State |  | number |  |  |
| 23 | CreatedTime |  | date |  |  |
| 24 | ProcessId |  | GUID |  |  |
| 25 | ContextId |  | GUID |  |  |
| 26 | ScopeId |  | GUID |  |  |
| 27 | IsFirstActivity |  | number(0/1) |  |  |
| 28 | DisplayName | 对象的显示名 | string(400) |  |  |
| 29 | Id | 对象的主键 | GUID | Y | Y |
| 30 | Version | 对象的版本号 | binary | Y |  |

### WF_ParticipantDefinition (活动或者流程中参与者的定义)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | ProcessDefinitionId | 所属的流程定义的Id | GUID |  |  |
| 2 | ParticipantType | 参与者类型，如某个员工，还是某个群组等 | number |  |  |
| 3 | DepartmentCode | 参与者类型为部门相关时，此处记录部门的Id | string(400) |  |  |
| 4 | OrganizationCode | 参与者类型为虚拟组织相关时，此处记录虚拟组织的Id | string(400) |  |  |
| 5 | DepartmentPropertyId | 当参数者类型为部门属性时，此处记录属性的Id | GUID |  |  |
| 6 | OrganizationPropertyId | 当参数者类型为虚拟组织属性时，此处记录属性的Id | GUID |  |  |
| 7 | EmployeeId | 当参与者类型为员工时，记录员工Id | GUID |  |  |
| 8 | GroupId | 参与者类型为群组时，记录群组Id | GUID |  |  |
| 9 | ActivityDefinitionId | 参与者需要参照某一活动定义时，记录要参照的活动定义的Id | GUID |  |  |
| 10 | DutyDefinitionId | 参与者类型为部门职称时，记录职称Id | GUID |  |  |
| 11 | TitleDefinitionId | 参与者类型为部门职务时，记录职务Id | GUID |  |  |
| 12 | IsFormField | 参与者是否使用表单中的字段(一般为员工Id)作为条件 | number(0/1) |  |  |
| 13 | FormVariableName | 参与者参考表单字段时，记录表单的所属变量的Name | string(400) |  |  |
| 14 | FormPropertyName | 参与者参考表单字段时，记录表单的字段名（实体属性名） | string(400) |  |  |
| 15 | RelationshipId | 参与者类型为关系人时，记录关系名 | string(400) |  |  |
| 16 | IncludeSubUnit | 参与者类型为部门或虚拟组织时，是否包含部门或虚拟组织子单元 | number(0/1) |  |  |
| 17 | Script | 参与者类型为脚本解析时，通过此脚本解析出具体处理人 | string(400) |  |  |
| 18 | DisplayName | 对象的显示名 | string(400) |  |  |
| 19 | Id | 对象的主键 | GUID | Y | Y |
| 20 | Version | 对象的版本号 | binary | Y |  |

### WF_ProcessContext

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Id | 对象的主键 | GUID | Y | Y |
| 2 | Version | 对象的版本号 | binary | Y |  |

### WF_ProcessDefinition (流程定义)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Type | 流程定义的类别，是标准流程还是自定义流程 | number |  |  |
| 2 | AutoCoding | 流程是否自动编号，默认true | number(0/1) |  |  |
| 3 | Abortable | 流程是否可被撤销(抽单) | number(0/1) |  |  |
| 4 | AbortReasonNotEmpty | 流程被撤销时，撤销流程原因是否必填 | number(0/1) |  |  |
| 5 | CreatedTime | 流程的创建时间 | date |  |  |
| 6 | TimeLimit | 流程的处理时限，时间单位小时(工作日时间) | number(18,0) |  |  |
| 7 | OvertimeNotifyInterval | 流程超时时，发送超时警告的时间间隔，单位小时 | number(18,0) |  |  |
| 8 | OvertimeNotifyTimes | 流程超时时，发送超时警告的次数 | number |  |  |
| 9 | OvertimeNotify | 流程超时时，是否发送超时警告 | number(0/1) |  |  |
| 10 | OvertimeNotificationId | 超时警告的通知定义的Id | GUID |  |  |
| 11 | AbortedNotify | 流程被撤销时是否逐层通知 | number(0/1) |  |  |
| 12 | AbortedNotificationId | 流程被撤销时的通知定义Id | GUID |  |  |
| 13 | ClosedNotifyMode | 流程结案时逐层通知的方式 | number |  |  |
| 14 | ClosedNotificationId | 流程结案时的通知定义Id | GUID |  |  |
| 15 | TerminatedNotify | 流程终止时是否逐层通知 | number(0/1) |  |  |
| 16 | TerminatedNotificationId | 流程终止时的通知定义Id | GUID |  |  |
| 17 | RegainedNotify | 是否要在处理者撤签时逐级通知流程处理者 | number(0/1) |  |  |
| 18 | RegainedNotificationId | 处理者撤签时的通知定义Id | GUID |  |  |
| 19 | ReexecutedNotify | 是否要在处理者退回重办工作时逐级通知流程处理者 | number(0/1) |  |  |
| 20 | ReexecutedNotificationId | 处理者退回重办工作时的通知定义Id | GUID |  |  |
| 21 | CountersignedNotify | 是否在加签时通知发起人 | number(0/1) |  |  |
| 22 | CountersignedNotificationId | 处理者加签时的通知定义Id | GUID |  |  |
| 23 | ProcessPackageId | 所属流程包的Id | GUID |  |  |
| 24 | RelationManDefId | 流程定义之关系人的参与者定义Id | GUID |  |  |
| 25 | Description | 流程定义的描述 | string(400) |  |  |
| 26 | OriginalDefinitionId | 原始容器定义Id | GUID |  |  |
| 27 | ProcessDefinitionId | 所属的流程定义的Id | GUID |  |  |
| 28 | OwnerId | 所属的上级定义的Id，当活动直接属于流程时，其上一级为流程，当活动属于组合活动（如核决活动）时，其上一级为组合活动 | GUID |  |  |
| 29 | OwnerType | 所属的上级定义的类型TypeKey，当活动直接属于流程时，其上一级为流程，当活动属于组合活动（如核决活动）时，其上一级为组合活动 | string(400) |  |  |
| 30 | DisplayName | 对象的显示名 | string(400) |  |  |
| 31 | Id | 对象的主键 | GUID | Y | Y |
| 32 | Version | 对象的版本号 | binary | Y |  |

### WF_ProcessInstance (流程实例)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | AutoCoding |  | number(0/1) |  |  |
| 2 | SerialNumber |  | string(400) |  |  |
| 3 | Priority |  | number |  |  |
| 4 | Subject |  | string(400) |  |  |
| 5 | Abortable |  | number(0/1) |  |  |
| 6 | AbortReasonNotEmpty |  | number(0/1) |  |  |
| 7 | AbortReason |  | string(400) |  |  |
| 8 | AbortedNotificationId | 流程被撤销时的通知定义Id | GUID |  |  |
| 9 | TerminatedNotificationId | 流程终止时的通知定义Id | GUID |  |  |
| 10 | RegainedNotificationId | 处理者撤签时的通知定义Id | GUID |  |  |
| 11 | InvokeOrgUnitCode |  | string(400) |  |  |
| 12 | InvokeOrgUnitId |  | GUID |  |  |
| 13 | InvokeOrgUnitType |  | number |  |  |
| 14 | IsMain |  | number(0/1) |  |  |
| 15 | State | 流程实例状态 | number |  |  |
| 16 | ProcessDefinitionId |  | GUID |  |  |
| 17 | NewProcessDefinitionId |  | GUID |  |  |
| 18 | ContextId |  | GUID |  |  |
| 19 | CreatedTime |  | date |  |  |
| 20 | OvertimeNotifyTimes |  | number |  |  |
| 21 | OvertimeNotifiedTimes |  | number |  |  |
| 22 | ClosedNotifyMode |  | number |  |  |
| 23 | ClosedNotificationId | 流程结案时的通知定义Id | GUID |  |  |
| 24 | DueTime |  | date |  |  |
| 25 | CreatorCalendarId |  | GUID |  |  |
| 26 | CreatorId |  | GUID |  |  |
| 27 | RelationManId |  | GUID |  |  |
| 28 | FirstActivityDefinitionType |  | string(400) |  |  |
| 29 | FirstActivityDefinitionId |  | GUID |  |  |
| 30 | ParentProcessId |  | GUID |  |  |
| 31 | SigningStatus |  | number |  |  |
| 32 | SigningResult |  | number |  |  |
| 33 | DisplayName | 对象的显示名 | string(400) |  |  |
| 34 | Id | 对象的主键 | GUID | Y | Y |
| 35 | Version | 对象的版本号 | binary | Y |  |

### WF_ProcessPackage (流程包的定义，包含一个主流程和若干子流程)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Code | 流程包的编码 | string(400) |  |  |
| 2 | CategoryId | 流程分类Id | GUID |  |  |
| 3 | SubjectTemplate | 流程主题的模板定义 | string(400) |  |  |
| 4 | MainProcessDefinitionId | 流程包中的主流程定义的Id | GUID |  |  |
| 5 | SubjectDefineMode | 流程发起时用户对主题的定义方式 | number |  |  |
| 6 | CreatedTime | 流程包的创建时间 | date |  |  |
| 7 | CreatorId | 流程包的创建人 | GUID |  |  |
| 8 | PublicationState | 流程包的发行状态 | number |  |  |
| 9 | Vender | 流程供应商的名称 | string(400) |  |  |
| 10 | XpdlVersion | 流程定义符合的XPDL版本 | string(400) |  |  |
| 11 | Description | 流程包描述 | string(400) |  |  |
| 12 | VersionNumber | 流程的版本号码 | number |  |  |
| 13 | ValidFrom | 流程定义的有效期开始时间 | date |  |  |
| 14 | ValidTo | 流程定义的有效期结束时间 | date |  |  |
| 15 | NeedControlAuthority | 是否需要控制权限 | number(0/1) |  |  |
| 16 | DisplayName | 对象的显示名 | string(400) |  |  |
| 17 | Id | 对象的主键 | GUID | Y | Y |
| 18 | Version | 对象的版本号 | binary | Y |  |

### WF_ProcessPackageCategory (流程包的分类)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Code | 流程分类的编码 | string(400) |  |  |
| 2 | Description | 流程分类描述 | string(400) |  |  |
| 3 | AboveCategoryId | 流程分类的上级分类 | GUID |  |  |
| 4 | DisplayName | 对象的显示名 | string(400) |  |  |
| 5 | Id | 对象的主键 | GUID | Y | Y |
| 6 | Version | 对象的版本号 | binary | Y |  |

### WF_Scope

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | ActivityDefinitionId |  | GUID |  |  |
| 2 | ActivityDefinitionType |  | string(400) |  |  |
| 3 | State |  | number |  |  |
| 4 | AncestorId |  | GUID |  |  |
| 5 | ProcessInstanceId |  | GUID |  |  |
| 6 | ProcessContextId |  | GUID |  |  |
| 7 | SourceId |  | GUID |  |  |
| 8 | TransitionId |  | GUID |  |  |
| 9 | Id | 对象的主键 | GUID | Y | Y |
| 10 | Version | 对象的版本号 | binary | Y |  |

### WF_SubflowActivity (子流程活动定义)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | SubflowProcessDefinitionId | 子流程定义ID | GUID |  |  |
| 2 | ExecuteType | 子流程的执行类型 | number |  |  |
| 3 | ProcessDefinitionId | 所属的流程定义的Id | GUID |  |  |
| 4 | OwnerId | 所属的上级定义的Id，当活动直接属于流程时，其上一级为流程，当活动属于组合活动（如核决活动）时，其上一级为组合活动 | GUID |  |  |
| 5 | OwnerType | 所属的上级定义的类型TypeKey，当活动直接属于流程时，其上一级为流程，当活动属于组合活动（如核决活动）时，其上一级为组合活动 | string(400) |  |  |
| 6 | DisplayName | 对象的显示名 | string(400) |  |  |
| 7 | Id | 对象的主键 | GUID | Y | Y |
| 8 | Version | 对象的版本号 | binary | Y |  |

### WF_SubflowActivityIns

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | ActivityDefinitionId |  | GUID |  |  |
| 2 | SubflowProcessInstanceId |  | GUID |  |  |
| 3 | ExecuteStage | 子流程的执行阶段 | number |  |  |
| 4 | State |  | number |  |  |
| 5 | CreatedTime |  | date |  |  |
| 6 | ProcessId |  | GUID |  |  |
| 7 | ContextId |  | GUID |  |  |
| 8 | ScopeId |  | GUID |  |  |
| 9 | IsFirstActivity |  | number(0/1) |  |  |
| 10 | DisplayName | 对象的显示名 | string(400) |  |  |
| 11 | Id | 对象的主键 | GUID | Y | Y |
| 12 | Version | 对象的版本号 | binary | Y |  |

### WF_Transition (活动之间的转移)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | ConditionType | 转移上定义的条件的类别 | number |  |  |
| 2 | ConditionContent | 转移上定义的条件表达式 | string(6000) |  |  |
| 3 | FromActivityDefinitionType | 转移出发的活动定义的TypeKey | string(400) |  |  |
| 4 | FromActivityDefinitionId | 转移出发的活动定义的Id | GUID |  |  |
| 5 | ToActivityDefinitionType | 转移到达的活动定义的TypeKey | string(400) |  |  |
| 6 | ToActivityDefinitionId | 转移到达的活动定义的Id | GUID |  |  |
| 7 | DisplayName | 对象的显示名 | string(400) |  |  |
| 8 | Id | 对象的主键 | GUID | Y | Y |
| 9 | Version | 对象的版本号 | binary | Y |  |
| 10 | F_Id |  | GUID | Y |  |

### WF_UnreexcuteActivity (对活动定义的引用)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | ActivityDefinitionType | 引用的活动定义的TypeKey | string(400) |  |  |
| 2 | ActivityDefinitionId | 引用的活动定义的Id | GUID |  |  |
| 3 | Id | 对象的主键 | GUID | Y | Y |
| 4 | Version | 对象的版本号 | binary | Y |  |
| 5 | F_Id |  | GUID | Y |  |

### WF_Variable

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | DefinitionId |  | GUID |  |  |
| 2 | Name |  | string(400) |  |  |
| 3 | DataType |  | number |  |  |
| 4 | FormTypeKey |  | string(400) |  |  |
| 5 | ViewName |  | string(400) |  |  |
| 6 | Value |  | string(400) |  |  |
| 7 | ComplexValue |  | binary |  |  |
| 8 | DisplayName | 对象的显示名 | string(400) |  |  |
| 9 | Id | 对象的主键 | GUID | Y | Y |
| 10 | Version | 对象的版本号 | binary | Y |  |
| 11 | F_Id |  | GUID | Y |  |

### WF_VariableDefinition (流程变量的定义)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | Name | 变量名 | string(400) |  |  |
| 2 | DataType | 变量的数据类型 | number |  |  |
| 3 | FormTypeKey | 变量为表单类型时关联表单的TypeKey | string(400) |  |  |
| 4 | ViewName | 变量为表单类型时关联表单的ViewName | string(400) |  |  |
| 5 | DefaultValue | 变量的默认值 | string(400) |  |  |
| 6 | Restriction | 变量的约束 | string(400) |  |  |
| 7 | ReferenceFormNames | 关联的表单名称 | string(400) |  |  |
| 8 | DisplayName | 对象的显示名 | string(400) |  |  |
| 9 | Id | 对象的主键 | GUID | Y | Y |
| 10 | Version | 对象的版本号 | binary | Y |  |
| 11 | F_Id |  | GUID | Y |  |

### WF_VariableDefRef (对变量定义的引用)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | ActivityDefinitionType | 引用变量的活动定义的TypeKey | string(400) |  |  |
| 2 | ActivityDefinitionId | 引用变量的活动定义的Id | GUID |  |  |
| 3 | VariableDefinitionId | 引用的变量定义的Id | GUID |  |  |
| 4 | SceneId | 如果是表单变量的话，记录表单的场景Id | GUID |  |  |
| 5 | EditState | 如果是表单变量的话，记录进入该表单的状态 | number |  |  |
| 6 | Id | 对象的主键 | GUID | Y | Y |
| 7 | Version | 对象的版本号 | binary | Y |  |
| 8 | F_Id |  | GUID | Y |  |

### WF_VariableMapping (子流程变量与主流程变量之间的映射)

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | VariableMappingType | 变量映射的类型 | number |  |  |
| 2 | MainVariableDefinitionId | 主流程变量定义Id | GUID |  |  |
| 3 | SubVariableDefinitionId | 子流程变量定义Id | GUID |  |  |
| 4 | Id | 对象的主键 | GUID | Y | Y |
| 5 | Version | 对象的版本号 | binary | Y |  |
| 6 | F_Id |  | GUID | Y |  |

### WF_VariableRef

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | ActivityType |  | string(400) |  |  |
| 2 | ActivityId |  | GUID |  |  |
| 3 | VariableId |  | GUID |  |  |
| 4 | Id | 对象的主键 | GUID | Y | Y |
| 5 | Version | 对象的版本号 | binary | Y |  |
| 6 | F_Id |  | GUID | Y |  |

### WF_WorkAssignment

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | AssigneeId |  | GUID |  |  |
| 2 | ViewTimes |  | number |  |  |
| 3 | IsNotice |  | number(0/1) |  |  |
| 4 | AssignType |  | number |  |  |
| 5 | State |  | number |  |  |
| 6 | CreatedTime |  | date |  |  |
| 7 | FirstVisitTime |  | date |  |  |
| 8 | LastVisitTime |  | date |  |  |
| 9 | SourceAssignmentId |  | GUID |  |  |
| 10 | SigningStatus |  | number |  |  |
| 11 | SigningResult |  | number |  |  |
| 12 | Id | 对象的主键 | GUID | Y | Y |
| 13 | Version | 对象的版本号 | binary | Y |  |
| 14 | F_Id |  | GUID | Y |  |

### WF_WorkItem

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | ActivityId |  | GUID |  |  |
| 2 | ActivityType |  | string(400) |  |  |
| 3 | State |  | number |  |  |
| 4 | DispatchType |  | number |  |  |
| 5 | PerformerId |  | GUID |  |  |
| 6 | PerformerIP |  | string(400) |  |  |
| 7 | PerformerOrgUnitCode |  | string(400) |  |  |
| 8 | PerformerOrgUnitId |  | GUID |  |  |
| 9 | PerformerOrgUnitType |  | number |  |  |
| 10 | SignedComment |  | string(400) |  |  |
| 11 | CreatedTime |  | date |  |  |
| 12 | CompletedTime |  | date |  |  |
| 13 | ScopeId |  | GUID |  |  |
| 14 | Bypassed |  | number(0/1) |  |  |
| 15 | IsHistoryRecord |  | number(0/1) |  |  |
| 16 | DueTime |  | date |  |  |
| 17 | AskReexecuteActivityId |  | GUID |  |  |
| 18 | ReexecuteHistoryActId |  | GUID |  |  |
| 19 | ReexecuteHistoryActType |  | string(400) |  |  |
| 20 | UnlockStamp |  | GUID |  |  |
| 21 | WorkType |  | number |  |  |
| 22 | DisplayName | 对象的显示名 | string(400) |  |  |
| 23 | Id | 对象的主键 | GUID | Y | Y |
| 24 | Version | 对象的版本号 | binary | Y |  |

### WF_WorkStep

| # | Column | Description | Type | Required | PK |
|---|--------|-------------|------|----------|----|
| 1 | State |  | number |  |  |
| 2 | VariableId |  | GUID |  |  |
| 3 | WorkStepIndex |  | number |  |  |
| 4 | Id | 对象的主键 | GUID | Y | Y |
| 5 | Version | 对象的版本号 | binary | Y |  |
| 6 | F_Id |  | GUID | Y |  |