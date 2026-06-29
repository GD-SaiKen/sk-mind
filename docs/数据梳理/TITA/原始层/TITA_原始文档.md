# TITA 开放API 文档

> 来源: https://oapi.tita.com/#/
> 共 47 个文档模块

---

# OAuth2 授权

## OAuth2 - Authorization Code

授权方式 Authorization Code授权流程获取Authorization Code请求地址请求参数请求示例响应页面使用Authorization Code换取Token请求参数请求地址请求参数参数示例响应报文使用授权令牌请求API> 已获得授权后可参考
> AccessToken 过期刷新方法
> OAuth2.0 令牌刷新
> 点击链接查看
> 注：开发文档内所有涉及编码处均以UTF-8形式编码！！！
[OAuth2.0 令牌刷新](/#/server/oauth2/RefreshToken)<font color="#dd0000">注：开发文档内所有涉及编码处均以UTF-8形式编码！！！</font>

```
+----------+
     | Resource |
     |   Owner  |
     |          |
     +----------+
          ^
          |
         (B)
     +----|-----+          Client Identifier      +---------------+
     |         -+----(A)-- & Redirection URI ---->|               |
     |  User-   |                                 | Authorization |
     |  Agent  -+----(B)-- User authenticates --->|     Server    |
     |          |                                 |               |
     |         -+----(C)-- Authorization Code ---<|               |
     +-|----|---+                                 +---------------+
       |    |                                         ^      v
      (A)  (C)                                        |      |
       |    |                                         |      |
       ^    v                                         |      |
     +---------+                                      |      |
     |         |>---(D)-- Authorization Code ---------'      |
     |  Client |          & Redirection URI                  |
     |         |                                             |
     |         |<---(E)----- Access Token -------------------'
     +---------+       (w/ Optional Refresh Token)

   Note: The lines illustrating steps (A), (B), and (C) are broken into
   two parts as they pass through the user-agent.

                     Figure 3: Authorization Code Flow
```

> 流程说明：
> A 租户响应授权请求到浏览器，浏览器加载授权服务页面
> B 用户同意授权请求，授权服务器获得授权信息
> C 授权服务器颁发授权码转向到用户回调地址
> D 租户使用授权码到授权服务器换取授权令牌
> E 授权服务器响应授权令牌
> 此种场景需要引导用户请求
> 授权地址(地址拼装方法查看)
> 接入方需开发用于接收授权服务器返回Authorization Code的接口，接口得到Authorization Code后使用Code在授权服务器换取授权令牌
[授权地址(地址拼装方法查看)](/#/server/oauth2/AuthorizationCode)

```
https://oapi.tita.com/OAuth/Authorize
```

```
Request Method： HTTP GET 
Request Params： tenant_id：必须，租户id。
                 app_id：必须。应用id。
                 user_id：用户id。
                 login_name：登录名，与user_id 至少一个不为空。
                 grant_type：必须。此模式下为authorization_code。
                 secret：必须。授权信息。
                 scope：非必须。当包含openid时 为OIDC方式授权。
                 response_type：必须。相应类型，此模式下为code固定值。                 
                 state：必须。Client提供的一个字符串，服务器会原样返回给Client。
                 redirect_uri：必须。用于接收返回code信息的地址。
```

```
https://oapi.tita.com/OAuth/Authorize?tenant_id=2343&app_id=1&user_id=101013063&login_name=&grant_type=authorization_code&response_type=code&state=custom_state_info&secret=4c00f8a7e00744be99548e0fcc62a118&scope=openid&redirect_uri=http%3A%2F%2Flocalhost%3A1722%2FHome%2FValidationCode
```

*提交授权信息到授权服务器后，服务器会响应授权页面给用户，用户提交授权信息后会重定向到redirect_uri并携带code参数。**注：需开发接收Authorization Code 的接口地址即redirect_uri 参数，用于授权后接收授权服务器响应的Code参数，获取Code后应当校验state与请求时是否一致并使用Code立即换取授权 Token（换取方法请参考以下文档）。*

```
https://oapi.tita.com/OAuth/Token
```

```
Request Method： HTTP POST 
Request Header： Content-Type:application/x-www-form-urlencoded
Request Params： tenant_id：必须，租户id。
                 app_id：必须。应用id。
                 user_id：用户id。
                 login_name：登录名，与user_id 至少一个不为空。
                 grant_type：必须。此模式下为authorization_code。
                 secret：必须。授权信息。
                 scope：非必须。当包含openid时 为OIDC方式授权。                 
                 state：必须。Client提供的一个字符串，服务器会原样返回给Client。
                 redirect_uri：必须。用于接收返回code信息的地址。
                 code：必须。授权服务器返回的code信息。
```

```
参数使用submit form 形式提交，请勿使用json形式。
tenant_id=1111&app_id=100&user_id=1111&grant_type=authorization_code&secret=XXXXXXX&state=customer_string&redirect_uri=xxxxx&code=code
```

```
响应内容以json格式输出
示例：
      {
        "access_token":"access_token_string",
        "expires_in":"1541329215",
        "user_id":"user_id_string",
        "tenant_id":"tenant_id_string",
        "refresh_token":"refresh_token_string",
        "id_token":"id_token_string"
      }
参数说明：
access_token    OAuth2.0 授权令牌
expires_in      过期时间UnixTime
tenant_id       租户ID
user_id         用户ID
refresh_token   刷新令牌，当Access_token过期后可使用refresh_token刷新
id_token        OIDC授权令牌信息，当授权请求时scope内包含openid时响应
```

[获取授权-页面下方](/#/server/oauth2/Readme)

---

## OAuth2 - Client Credentials

授权方式 Client Credentials授权流程请求地址请求参数参数示例响应报文使用授权令牌请求API在请求报文头中新加Authorization，值为Bearer+空格+access_token
例如：
Authorization: Bearer O-bb46_JZaiAzf4RyACluK-1JoESigRnRKHsvvslSSE61yaK-chWKA> 已获得授权后可参考
> AccessToken 过期刷新方法
> OAuth2.0 令牌刷新
> 点击链接查看
> 注：开发文档内所有涉及编码处均以UTF-8形式编码！！！
[OAuth2.0 令牌刷新](/#/server/oauth2/RefreshToken)<font color="#dd0000">注：开发文档内所有涉及编码处均以UTF-8形式编码！！！</font>

```
+---------+                                  +---------------+
     |         |                                  |               |
     |         |>--(A)- Client Authentication --->| Authorization |
     | Client  |                                  |     Server    |
     |         |<--(B)---- Access Token ---------<|               |
     |         |                                  |               |
     +---------+                                  +---------------+

                     Figure 6: Client Credentials Flow
```

> 流程说明：
> A 租户服务器使用客户端授权请求授权服务器获取授权
> B 授权服务器颁发授权令牌
> 此种场景适合租户直接通过服务器及授权信息访问用户资源

```
https://oapi.tita.com/OAuth/Token
```

```
Request Method： HTTP POST 
Request Header： Content-Type:application/x-www-form-urlencoded
Request Params： tenant_id：必须，租户id。
                 app_id：必须。应用id。
                 grant_type：必须。此模式下为client_credentials。
                 secret：必须。授权信息。
上述参数咨询Tita售后同学，提供接收秘钥的邮件号，并告知获取秘钥为获取Tita数据。申请成功后，会将秘钥和其他需要的参数通过邮件发送给您，售后反馈后请注意查收
```

```
参数使用submit form 形式提交，请勿使用json形式。
tenant_id=1111&grant_type=client_credentials&secret=XXXXXXXX&app_id=1
```

```
响应内容以json格式输出
示例：
      {
        "access_token":"access_token_string",
        "expires_in":"1541329215",
        "tenant_id":"tenant_id_string",
        "refresh_token":"refresh_token_string",
      }
参数说明：
access_token    OAuth2.0 授权令牌
expires_in      过期时间(秒)
tenant_id       租户ID
refresh_token   刷新令牌，当Access_token过期后可使用refresh_token刷新
```

[获取授权-页面下方](/#/server/oauth2/Readme)

---

## OAuth2 - 概述

OAuth 2.0 授权 OIDC(OpenID Connect)适用场景授权流程授权流程授权流程第一步 获取Secret第二步 使用Secret获取授权第三步 使用授权令牌调用API> AccessToken 过期刷新方法
> OAuth2.0 令牌刷新
> 点击链接查看
> 注：开发文档内所有涉及编码处均以UTF-8形式编码！！！
[OAuth2.0 令牌刷新](/#/server/oauth2/RefreshToken)<font color="#dd0000">注：开发文档内所有涉及编码处均以UTF-8形式编码！！！</font>> OAuth（开放授权）是一个开放标准，允许用户让第三方应用访问该用户在某一网站上存储的私密的资源（如照片，视频，联系人列表），而无需将用户名和密码提供给第三方应用。
> OAuth 2.0 协议官方说明
> OIDC是OpenID Connect的简称，OIDC=(Identity, Authentication) + OAuth 2.0。它在OAuth2上构建了一个身份层，是一个基于OAuth2协议的身份认证标准协议。
> 获取OIDC IDToken 只需在原有OAuth授权基础上，请求授权参数scope节点内增加openid即可获得IDToken。
[OAuth 2.0 协议官方说明](https://oauth.net/2/)

```
平台提供了消息、待办、基础数据对接等API，通过OAuth2.0授权模式提供给需要接入的租户使用。
```

```
+--------+                               +---------------+
     |        |--(A)- Authorization Request ->|   Resource    |
     |        |                               |     Owner     |
     |        |<-(B)-- Authorization Grant ---|               |
     |        |                               +---------------+
     |        |
     |        |                               +---------------+
     |        |--(C)-- Authorization Grant -->| Authorization |
     | Client |                               |     Server    |
     |        |<-(D)----- Access Token -------|               |
     |        |                               +---------------+
     |        |
     |        |                               +---------------+
     |        |--(E)----- Access Token ------>|    Resource   |
     |        |                               |     Server    |
     |        |<-(F)--- Protected Resource ---|               |
     +--------+                               +---------------+
              Figure 1: Abstract Protocol Flow
```

[Authorization Code](/#/server/oauth2/AuthorizationCode)授权模式

```
+----------+
     | Resource |
     |   Owner  |
     |          |
     +----------+
          ^
          |
         (B)
     +----|-----+          Client Identifier      +---------------+
     |         -+----(A)-- & Redirection URI ---->|               |
     |  User-   |                                 | Authorization |
     |  Agent  -+----(B)-- User authenticates --->|     Server    |
     |          |                                 |               |
     |         -+----(C)-- Authorization Code ---<|               |
     +-|----|---+                                 +---------------+
       |    |                                         ^      v
      (A)  (C)                                        |      |
       |    |                                         |      |
       ^    v                                         |      |
     +---------+                                      |      |
     |         |>---(D)-- Authorization Code ---------'      |
     |  Client |          & Redirection URI                  |
     |         |                                             |
     |         |<---(E)----- Access Token -------------------'
     +---------+       (w/ Optional Refresh Token)

   Note: The lines illustrating steps (A), (B), and (C) are broken into
   two parts as they pass through the user-agent.

                     Figure 3: Authorization Code Flow
```

> 流程说明：
> A 租户响应授权请求到浏览器，浏览器加载授权服务页面
> B 用户同意授权请求，授权服务器获得授权信息
> C 授权服务器颁发授权码转向到用户回调地址
> D 租户使用授权码到授权服务器换取授权令牌
> E 授权服务器响应授权令牌
> 此种场景需要引导用户请求
> 授权地址(地址拼装方法查看)
> 接入方需开发用于接收授权服务器返回Authorization Code的接口，接口得到Authorization Code后使用Code在授权服务器换取授权令牌
[授权地址(地址拼装方法查看)](/#/server/oauth2/AuthorizationCode)[Client Credentials](/#/server/oauth2/ClientCredentials)授权模式

```
+---------+                                  +---------------+
     |         |                                  |               |
     |         |>--(A)- Client Authentication --->| Authorization |
     | Client  |                                  |     Server    |
     |         |<--(B)---- Access Token ---------<|               |
     |         |                                  |               |
     +---------+                                  +---------------+

                     Figure 6: Client Credentials Flow
```

> 流程说明：
> A 租户服务器使用客户端授权请求授权服务器获取授权
> B 授权服务器颁发授权令牌
> 此种场景适合租户直接通过服务器及授权信息访问用户资源

```
租户可联系对接人员申请应用Secret的开通。
```

```
平台对外提供 Authorization Code、 Client Credentials 授权模式，租户可根据自己的使用场景选择，详情点击链接查看。
```

> 快速访问入口：
> Authorization Code
> 、
> Client Credentials
[Authorization Code](/#/server/oauth2/AuthorizationCode)[Client Credentials](/#/server/oauth2/ClientCredentials)

```
基于OAuth2 AccessToken的Api请求
在请求报文头中新加Authorization，值为Bearer+空格+access_token
示例：
      Connection: keep-alive
      Accept-Encoding: gzip, deflate, sdch
      Accept-Language: zh-CN,zh;q=0.8
      Authorization: Bearer O-bb46_JZaiAzf4RyACluK-1JoESigRnRKHsvvslSSE61yaK-chWKA
      
      
基于OIDC IDToken的Api请求
可将id_token作为HTTP GET 请求参数传递或在请求头中加入id_token。
示例：
    1、url get
    http://xxxx.com/demoapi?id_token=id_token_string
    2、Request Header内添加
    Connection: keep-alive
    Accept-Encoding: gzip, deflate, sdch
    Accept-Language: zh-CN,zh;q=0.8
    id_token:id_token_string
    
使用授权令牌调用API前应判断授权是否过期，未过期授权可连续使用，有效期内重新获取会导致原有授权失效。
使用OAuth2.0 AccessToken时如令牌过期，使用RefreshToken刷新即可，无需重新获取。OIDC IDToken暂不支持刷新功能。
```

---

## OAuth2 - 刷新令牌

OAuth2.0 Access Token 刷新

```
同获取令牌规则一样
```

---

## OAuth2 - 密码模式

授权方式 Resource Owner Password Credentials Grant授权流程图例请求地址

```
https://oapi.tita.com/OAuth/Token
```

请求参数

```
Request Method： HTTP POST 
Request Header： Content-Type:application/x-www-form-urlencoded
Request Params： tenant_id：必须，租户id。
                 app_id：必须。应用id。
                 username：必须。登录名。
                 password：必须。登录密码。
                 grant_type：必须。此模式下为password。
                 secret：必须。授权信息。
                 scope：非必须。当包含openid时 为OIDC方式授权。
```

响应报文

```
响应内容以json格式输出
示例：
      {
        "access_token":"access_token_string",
        "expires_in":"1541329215",
        "user_id":"user_id_string",
        "tenant_id":"tenant_id_string",
        "refresh_token":"refresh_token_string",
        "id_token":"id_token_string"
      }
参数说明：
access_token    OAuth2.0 授权令牌
expires_in      过期时间UnixTime
tenant_id       租户ID
user_id         用户ID
refresh_token   刷新令牌，当Access_token过期后可使用refresh_token刷新
id_token        OIDC授权令牌信息，当授权请求时scope内包含openid时响应
```

使用授权令牌请求API已获得授权后可参考[获取授权-页面下方](/#/server/oauth2/Readme)

---

# CRM API

## CRM - 概述

概述> 平台提供了基于OAuth2.0授权保护的API资源，使用这些 API 可以帮助企业灵活地对接现有的IT系统，API调用前必须现获取授权令牌，
> 授权令牌获取方法
> 。
[授权令牌获取方法](/#/server/oauth2/ClientCredential)Open API 说明> Open API 提供主动调用的连接方式。当你的应用调用开放平台接口时，需使遵守文档开发标准，文档内编码统一使用
> UTF-8编码
> 。
> 使用授权令牌调用API前应判断授权令牌是否过期，未过期授权可连续使用，有效期内重新获取会导致原有授权失效。
> 使用OAuth2.0 AccessToken时如令牌过期，使用RefreshToken刷新即可
> OAuth2.0 令牌刷新
> 点击链接查看
*UTF-8编码*[OAuth2.0 令牌刷新](/#/server/oauth2/RefreshToken)

---

## CRM - 新增接口

CRM新增接口请求地址https://oapi.tita.com/crm/api/add?tenantId=?&objType=?&formCode=?&needApproval=?&accountType=?&deptType=?请求url例子https://oapi.tita.com/crm/api/add?tenantId=10086&objType=customer&formCode=Crm.Customer.CreateForm&needApproval=2&accountType=0&deptType=1&operatorUser=13111111111请求方式POSTContent-TypeContent-Type application/json请求body

```
示例1：无关联产品子表的情况
[
  {
    "metaObjectCode": "Crm.Customer",
    "fields": [
      {
        "name": "PrincipalUserId",
        "value": "9638c0f3-5569-4230-a175-4562b8274c71@tita-weixin.com"
      },
      {
        "name": "Name",
        "value": "客户名称"
      },
      {
        "name": "Mobile",
        "value": "13112345678"
      }
    ]
  }
]
```

```
示例2：有关联产品子表的情况,数组里面传多条，第一条记录为主对象数据，后续为关联产品子对象数据
[
  {
    "metaObjectCode": "Crm.Business",
    "fields": [
      {
        "name": "Stage",
        "value": "1"
      },
      {
        "name": "FinishDealTime",
        "value": "2025/7/28"
      },
      {
        "name": "PrincipalUserId",
        "value": "600108734"
      },
      {
        "name": "Name",
        "value": "关联字段商机"
      },
      {
        "name": "CustomerId",
        "value": "278b8a0a-725c-4327-8658-3fe78f2f00c7"
      },
      {
        "name": "Amount",
        "value": "0.00"
      }
    ]
  },
  {
    "metaObjectCode": "Crm.BusinessProduct",
    "fields": [
      {
        "name": "ProductId",
        "value": "d9b0d5a6-178d-4317-8ee3-adc79db8a76f"
      },
      {
        "name": "BarCode",
        "value": ""
      },
      {
        "name": "Unit",
        "value": ""
      },
      {
        "name": "ProductNumber",
        "value": 1
      },
      {
        "name": "Price",
        "value": "22"
      },
      {
        "name": "SellPrice",
        "value": "0.00"
      },
      {
        "name": "SellPriceTotal",
        "value": "0.00"
      },
      {
        "name": "Name",
        "value": "西红柿"
      },
      {
        "name": "Code",
        "value": "23"
      }
    ]
  }
]
```

url地址中参数说明：

| 名称 | 类型 | 说明 | 必填 |
| --- | --- | --- | --- |
| tenantId | int | 租户id | 是 |
| objType | string | 对象类型 (合同：contract 客户: customer 发票：invoice 联系人：contacts 产品：product 回款：receivables 产品类别：productClassification 商机：business 线索：salesLeads 跟进记录：record) | 是 |
| formCode | string | 表单编码( 合同：Crm.Contract.CreateForm 客户：Crm.Customer.CreateForm 发票：Crm.Invoice.CreateForm 联系人：Crm.Contacts.CreateForm 产品：Crm.Product.CreateForm 回款：Crm.Receivables.CreateForm 产品类别：Crm.ProductClassification.CreateForm 商机：Crm.Business.CreateForm 线索：Crm.SalesLeads.CreateForm 跟进记录：Crm.Record.CreateForm) | 是 |
| needApproval | string | 是否需要经过审批 (1:需要（租户配置了审批流，则经过审批，否则不经过） 2 ：不需要（租户即使配置了审批流也不执行审批）  3：不干预，以tita系统逻辑为主) | 是 |
| accountType | int | 用户id类型（0:手机号或邮箱或姓名） | 是 |
| deptType | int | 部门id类型（0:使用tita系统部门编码  1：使用三方corpid） | 是 |
| operatorUser | string | 操作人(手机号或邮箱或姓名) | 是 |

请求body参数说明：

| 名称 | 类型 | 说明 | 必填 |
| --- | --- | --- | --- |
| metaObjectCode | string | 对象编码：(客户：Crm.Customer 联系人：Crm.Contacts  合同：Crm.Contract  发票：Crm.Invoice  回款：Crm.Receivables  产品：Crm.Product  产品类别：Crm.ProductClassification 商机：Crm.Business 线索：Crm.SalesLeads 关联产品子表：Crm.BusinessProduct 跟进记录：Crm.Record) | 是 |
| fields | 数组 | 参数集合，请参考业务对象字段信息页面，注意:业务表单所有必填字段必传，举例：比如新增客户，客户名称字段在tita系统是必填，因此此字段必传 | 是 |

返回结果示例

```
{
    "code": 0,
    "data": db77ba6e-393e-4bcc-94df-657e8264f6d3,
    "errorMsg": "操作成功"

}
```

返回结果说明：

| 返回值 | 类型 | 说明 |
| --- | --- | --- |
| code | int | 状态码（0成功，其他值表示异常） |
| errorMsg | string | 错误信息 |

新增跟进记录接口传参说明说明：
下面表格中的id字段需要调用crm查询接口，根据名称查询出对应的id值，例如，要想拿到客户id需要根据客户名称查询出客户信息，然后从中得到Id字段的值作为客户id。
跟进方式需要调用crm字典接口，得到跟进方式的所有字典项，从中选择你需要的编码作为跟进方式的传参；

| 跟进记录类型 | 必填项 | 选填项 | 说明 |
| --- | --- | --- | --- |
| 客户 | 跟进内容、客户id、跟进方式编码 | 联系人id、下次跟进时间 | 联系人必须是客户下的联系人、下次跟进时间不能早于当前时间 |
| 线索 | 跟进内容、线索id、跟进方式编码 | 下次跟进时间 | 下次跟进时间不能早于当前时间 |
| 访客计划 | 跟进内容、客户id、访客计划id、跟进方式编码 | 联系人id、下次跟进时间 | 访客计划必须是所选的客户下的访客计划、联系人必须是客户下的联系人、下次跟进时间不能早于当前时间 |
| 商机 | 跟进内容、客户id、商机id、跟进方式编码 | 联系人id、下次跟进时间 | 商机必须是所选的客户下的商机、联系人必须是客户下的联系人、下次跟进时间不能早于当前时间 |
| 报价单 | 跟进内容、客户id、报价单id、跟进方式编码 | 联系人id、下次跟进时间 | 报价单必须是所选的客户下的报价单、联系人必须是客户下的联系人、下次跟进时间不能早于当前时间 |
| 回款计划 | 跟进内容、客户id、回款计划id、跟进方式编码 | 联系人id、下次跟进时间 | 回款计划必须是所选的客户下的回款计划、联系人必须是客户下的联系人、下次跟进时间不能早于当前时间 |
| 联系人 | 跟进内容、客户id、联系人id、跟进方式编码 | 下次跟进时间 | 联系人必须是客户下的联系人、下次跟进时间不能早于当前时间 |

---

## CRM - 商机

商机接口新增商机请求地址https://oapi.tita.com/crm/api/{tenantId}/business/add请求方式POSTContent-TypeContent-Type application/json请求body

```
{
"accountType":"0",
"principalAccount":"89899988@qq.com",
"name":"商机名称",
"customerId":"ff3d1eae-0fff-4803-b067-0a904e677c13",
"stage":"2",
"amount":"168880",
"finishDealTime":"2024/05/05",
"competitors":"对手名称",
"remark":"备注信息",
customProperties:[
    {
    "key":"department",
    "value":"111122"
    }
]
}
```

参数说明：

| 名称 | 类型 | 说明 | 必填 |
| --- | --- | --- | --- |
| accountType | int | 账号类型 （0:手机号或邮箱或姓名） | 是 |
| principalAccount | string | 负责人账号（根据account_type不同进行赋值） | 是 |
| name | string | 商机名称 | 是 |
| customerId | string | 关联客户id | 是 |
| stage | string | 商机阶段，字典 | 是 |
| amount | string | 预计金额 | 是 |
| finishDealTime | string | 预计成交日期(yyyy/MM/dd) | 是 |
| competitors | string | 竞争对手 | 否 |
| remark | string | 备注 | 否 |
| customProperties | array | 数组对象，自定义字段放到这个里面，看下面自定义字段说句 | 否 |

自定义参数说明：

| 字段 | 说明 |
| --- | --- |
| key | 具体字段比如 部门是自定义字段 department |
| value | 字段中的具体值（如：研发部） |

返回结果示例

```
{
    "code": 0,
    "errorMsg": null,
    "data": {
        "objData": 2458586
    }
}
```

返回结果说明：

| 返回值 | 类型 | 说明 |
| --- | --- | --- |
| code | int | 状态码（0成功） |
| errorMsg | string | 错误信息 |
| data.objData | string | 商机主键id |

修改商机请求地址https://oapi.tita.com/crm/api/{tenantId}/business/update请求方式POSTContent-TypeContent-Type application/json请求body

```
{
"id":"ff3d1eae-0877-4803-b6557-0a904e6ee452",
"accountType":"0",
"principalAccount":"89899988@qq.com",
"name":"商机名称",
"customerId":"ff3d1eae-0fff-4803-b067-0a904e677c13",
"stage":"2",
"amount":"168880",
"finishDealTime":"2024/05/05",
"competitors":"对手名称",
"remark":"备注信息",
customProperties:[
    {
    "key":"department",
    "value":"111122"
    }
]
}
```

参数说明：

| 名称 | 类型 | 说明 | 必填 |
| --- | --- | --- | --- |
| id | string | 主键id | 是 |
| accountType | int | 账号类型 （0:手机号或邮箱或姓名） | 是 |
| principalAccount | string | 负责人账号（根据account_type不同进行赋值） | 是 |
| name | string | 商机名称 | 是 |
| customerId | string | 关联客户id | 是 |
| stage | string | 商机阶段，字典 | 是 |
| amount | string | 预计金额 | 是 |
| finishDealTime | string | 预计成交日期(yyyy/MM/dd) | 是 |
| competitors | string | 竞争对手 | 否 |
| remark | string | 备注 | 否 |
| customProperties | array | 数组对象，自定义字段放到这个里面，看下面自定义字段说句 | 否 |

自定义参数说明：

| 字段 | 说明 |
| --- | --- |
| key | 具体字段比如 部门是自定义字段 department |
| value | 字段中的具体值（如：研发部） |

返回结果示例

```
{
    "code": 0,
    "errorMsg": null,
    "data": {
        "objData": 2458586
    }
}
```

返回结果说明：

| 返回值 | 类型 | 说明 |
| --- | --- | --- |
| code | int | 状态码（0成功） |
| errorMsg | string | 错误信息 |
| data.objData | string | 线索主键id |

查询商机请求地址https://oapi.tita.com/crm/api/{tenantId}/business/search请求方式GetContent-TypeContent-Type application/json请求body

```
{
  "pageNum":1,
  "pageSize":10,
  "items": [
    {
      "name": "name",
      "value": "小明",
      "conditionType": 1,
      "operatorType": 1
    }
  ]
}
```

参数说明：

| 名称 | 类型 | 说明 | 必填 |
| --- | --- | --- | --- |
| pageNum | int | 第几页 | 是 |
| pageSize | int | 每页几条数据 | 是 |
| name | string | 字段名称 | 否 |
| items | object | 条件列表 | 否 |
| value | string | 字段具体值 | 否 |
| conditionType | int | 1等于、2大于等于、3小于等于、4大于、5小于、6范围、7为空、8不为空、9不等于、10开头等于、11结尾等于、12包含、14模糊 | 否 |
| operatorType | int | 1且  2或 | 否 |

返回结果示例

```
{
    "code": 0,
    "data": {
        "records": [
            {
                "id": "5068fb5f-7c5f-4da2-a4bd-b29b6b88c307",
                "documentIds": null,
                "loseDescription": null,
                "winRate": null,
                "lastUpdateStageTime": null,
                "lastRecordTime": null,
                "principalUserId": "600095451",
                "remark": null,
                "finishDealTime": "Fri Jun 07 00:00:00 CST 2024",
                "competitor": null,
                "amount": 1.0000000001E8,
                "channel": null,
                "stage": 1,
                "customerId": "5e066650-0556-4bd5-a70a-c3b937608bc9",
                "name": "11",
                "competitors": null,
                "createdBy": 600095451,
                "createdTime": "2024-06-07T15:13:19",
                "modifiedBy": 600095451,
                "modifiedTime": "2024-06-07T15:13:19",
                "orderTotal": null
            }
        ],
        "total": 29,
        "size": 2,
        "current": 1,
        "pages": 29
    },
    "errorMsg": "操作成功"
}
```

返回结果说明1、

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| code | int | 状态码0成功 |
| errorMsg | string | 错误信息，默认空 |
| data | Object | 对象 |

2、

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| total | int | 总条数 |
| records | list | 数据列表 |

3、

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| id | string | 主键id |
| documentIds | string | 文件id，多个用逗号隔开 |
| loseDescription | string | 输单描述 |
| winRate | int | 赢率 |
| lastUpdateStageTime | string | 更改商机阶段时间  yyyy/MM/dd |
| lastRecordTime | string | 最后跟进记录时间 |
| principalUserId | string | 负责人id |
| remark | string | 备注 |
| finishDealTime | string | 预计成交时间 |
| competitor | string | 竞品信息 |
| amount | double | 预计金额 |
| channel | string | 渠道 |
| stage | string | 商机阶段 字典 |
| customerId | string | 客户id |
| name | string | 商机名称 |
| competitors | string | 对手名称 |
| createdBy | string | 创建人id |
| createdTime | string | 创建时间 |
| modifiedBy | string | 修改人id |
| modifiedTime | string | 修改时间 |

---

## CRM - 合同

合同接口新增合同请求地址https://oapi.tita.com/crm/api/{tenantId}/contract/add请求方式POSTContent-TypeContent-Type application/json请求body

```
{
    "accountType": "0",
    "principalAccount": "15500000001",
    "customSignAccount": "组织人事测试测试测试测试测试测试测试测试测试测试测试测试测试",
    "companySignAccount": "组织人事测试测试测试测试测试测试测试测试测试测试测试测试测试",
    "customerId": "9e394cda-9f82-4811-95fb-724c04eed6b8",
    "code": "SO.202506240001",
    "name": "888888pppp",
    "signTime": "2024/06/27",
    "startTime": "2024/06/26",
    "endTime": "2024/06/30",
    "amount": "5656",
    "businessId":"asdafdsafaa333",
    "remark": "serwrew"
    customProperties:[
        {
        "key":"department",
        "value":"111122"
        }
    ]
}
```

参数说明：

| 名称 | 类型 | 说明 | 必填 |
| --- | --- | --- | --- |
| accountType | int | 账号类型 （0:手机号或邮箱或姓名） | 是 |
| principalAccount | string | 负责人账号（根据account_type不同进行赋值） | 是 |
| customSignAccount | string | 客户签订人账号（根据accountType不同进行赋值） | 是 |
| companySignAccount | string | 公司签订人账号（根据accountType不同进行赋值） | 是 |
| customerId | string | 关联客户id | 是 |
| name | string | 合同名称 | 是 |
| businessId | string | 关联商机id | 否 |
| code | string | 预计合同编码 | 是 |
| signTime | string | 合同签订时间 | 是 |
| startTime | string | 合同开始时间 | 是 |
| endTime | string | 合同结束时间 | 是 |
| amount | BigDecimal | 合同金额 | 是 |
| remark | string | 备注 | 否 |
| customProperties | array | 数组对象，自定义字段放到这个里面，看下面自定义字段说句 | 否 |

自定义参数说明：

| 字段 | 说明 |
| --- | --- |
| key | 具体字段比如 部门是自定义字段 department |
| value | 字段中的具体值（如：研发部） |

返回结果示例

```
{
    "code": 0,
    "errorMsg": null,
    "data": {
        "objData": 2458586
    }
}
```

返回结果说明：

| 返回值 | 类型 | 说明 |
| --- | --- | --- |
| code | int | 状态码（0成功） |
| errorMsg | string | 错误信息 |
| data.objData | string | 合同主键id |

查询合同请求地址https://oapi.tita.com/crm/api/{tenantId}/contract/search请求方式GetContent-TypeContent-Type application/json请求body

```
{
  "pageNum":1,
  "pageSize":10,
  "items": [
    {
      "name": "name",
      "value": "小明",
      "conditionType": 1,
      "operatorType": 1
    }
  ]
}
```

参数说明：

| 名称 | 类型 | 说明 | 必填 |
| --- | --- | --- | --- |
| pageNum | int | 第几页 | 是 |
| pageSize | int | 每页几条数据 | 是 |
| name | string | 字段名称 | 否 |
| items | object | 条件列表 | 否 |
| value | string | 字段具体值 | 否 |
| conditionType | int | 1等于、2大于等于、3小于等于、4大于、5小于、6范围、7为空、8不为空、9不等于、10开头等于、11结尾等于、12包含、14模糊 | 否 |
| operatorType | int | 1且  2或 | 否 |

返回结果示例

```
{
    "code": 0,
    "data": {
        "records": [
            {
                "id": "c51660f6-a44c-4e40-a11d-d9a548cfc6e9",
                "accountType": null,
                "principalAccount": "600095451",
                "customSignAccount": "600095451",
                "companySignAccount": "600095451",
                "customerId": "9e394cda-9f82-4811-95fb-724c04eed6b8",
                "businessId": null,
                "code": "SO.202506240001",
                "name": "888888pppp",
                "signTime": "2024/06/26",
                "endTime": "2024-06-30T00:00",
                "startTime": "2024-06-26T00:00",
                "contractType": null,
                "remark": "serwrew",
                "createdBy": 600095451,
                "createdTime": "2024/08/13 18:57:35",
                "modifiedTime": "2024/06/30",
                "customProperties": null,
                "amount": 5656,
                "modifiedBy": null
            }
        ],
        "total": 29,
        "size": 2,
        "current": 1,
        "pages": 29
    },
    "errorMsg": "操作成功"
}
```

返回结果说明1、

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| code | int | 状态码0成功 |
| errorMsg | string | 错误信息，默认空 |
| data | Object | 对象 |

2、

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| total | int | 总条数 |
| records | list | 数据列表 |

3、

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| id | string | 主键id |
| principalAccount | string | 负责人id |
| customSignAccount | string | 客户签订人id |
| companySignAccount | string | 公司签订人id |
| customerId | string | 关联客户id |
| businessId | string | 关联商机id |
| code | string | 合同编码 |
| name | string | 合同名称 |
| signTime | string | 合同签订时间 格式（yyyy/MM/dd） |
| startTime | string | 合同开始时间 |
| endTime | string | 合同结束时间 |
| contractType | string | 合同类型  字典项 |
| remark | string | 合同备注 |
| amount | double | 合同金额 |
| createdBy | string | 创建人id |
| createdTime | string | 创建时间 |
| modifiedBy | string | 修改人id |
| modifiedTime | string | 修改时间 |

---

## CRM - 客户

客户接口新增客户请求地址https://oapi.tita.com/crm/api/{tenantId}/customer/add请求方式POSTContent-TypeContent-Type application/json请求body

```
{
    "accountType": "0",
    "principalAccount": "组织人事测试1111",
    "name": "北京黑镜科技有限公司",
    "telephone": "6716150",
    "region": "2",
    "address": "详细地址",
    "status": "3",
    "stage": "4",
     "industry": "2",
    "employeeTotal": "2",
    "customerSource": "1",
    "customProperties": [
        {
            "key": "department",
            "value": "111122"
        }
    ]
}
```

参数说明：

| 名称 | 类型 | 说明 | 必填 |
| --- | --- | --- | --- |
| accountType | int | 账号类型 （0:手机号或邮箱或姓名） | 是 |
| principalAccount | string | 负责人账号（根据account_type不同进行赋值） | 是 |
| name | string | 客户名称 | 是 |
| telephone | string | 客户电话 | 否 |
| region | string | 所属地区编码，字典 | 是 |
| address | string | 详细地址 | 否 |
| status | string | 客户状态 参考字段 | 否 |
| stage | string | 客户阶段 参考字段 | 否 |
| industry | string | 所属行业 参考字段 | 否 |
| employeeTotal | string | 企业规模  参考字段 | 否 |
| customerSource | string | 客户来源  参考字段 | 否 |
| customProperties | array | 数组对象，自定义字段放到这个里面，看下面自定义字段说句 | 否 |

自定义参数说明：

| 字段 | 说明 |
| --- | --- |
| key | 具体字段比如 部门是自定义字段 department |
| value | 字段中的具体值（如：研发部） |

返回结果示例

```
{
    "code": 0,
    "errorMsg": null,
    "data": {
        "objData": 2458586
    }
}
```

返回结果说明：

| 返回值 | 类型 | 说明 |
| --- | --- | --- |
| code | int | 状态码（0成功） |
| errorMsg | string | 错误信息 |
| data.objData | string | 线索主键id |

查询客户请求地址https://oapi.tita.com/crm/api/{tenantId}/customer/search请求方式GetContent-TypeContent-Type application/json请求body

```
{
  "pageNum":1,
  "pageSize":10,
  "items": [
    {
      "name": "name",
      "value": "小明",
      "conditionType": 1,
      "operatorType": 1
    }
  ]
}
```

参数说明：

| 名称 | 类型 | 说明 | 必填 |
| --- | --- | --- | --- |
| pageNum | int | 第几页 | 是 |
| pageSize | int | 每页几条数据 | 是 |
| name | string | 字段名称 | 否 |
| items | object | 条件列表 | 否 |
| value | string | 字段具体值 | 否 |
| conditionType | int | 1等于、2大于等于、3小于等于、4大于、5小于、6范围、7为空、8不为空、9不等于、10开头等于、11结尾等于、12包含、14模糊 | 否 |
| operatorType | int | 1且  2或 | 否 |

返回结果示例

```
{
    "code": 0,
    "data": {
        "records": [
            {
                "id": "664d716b-d18b-41fb-b132-e2068f429605",
                "businessCount": null,
                "name": "测试刻画啊啊",
                "stage": 2,
                "customerTenantId": null,
                "industry": 2,
                "employeeTotal": null,
                "estimateOrderTotal": null,
                "channel": null,
                "installApp": null,
                "mobile": null,
                "telephone": null,
                "region": "3",
                "address": null,
                "status": null,
                "principalUserId": null,
                "lastRecordTime": null,
                "description": null,
                "participant": null,
                "oldPrincipalUserId": "600095451",
                "customerAvatar": null,
                "salesLeadsId": "664d716b-d18b-41fb-b132-e2068f429605",
                "importanceNew": "3",
                "documentIds": null,
                "createdBy": 600095451,
                "createdTime": "2024/07/17 17:02:41",
                "modifiedBy": 600095451,
                "modifiedTime": "2024/07/19 00:05:01",
                "AllocationTime": null,
                "Remark": null,
                "CustomerSource": null,
                "WorkId": null,
                "LastRecordContent": null
            }
        ],
        "total": 1,
        "size": 10,
        "current": 1,
        "pages": 1
    },
    "errorMsg": "操作成功"
}
```

返回结果说明1、

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| code | int | 状态码0成功 |
| errorMsg | string | 错误信息，默认空 |
| data | Object | 对象 |

2、

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| total | int | 总条数 |
| records | list | 数据列表 |

3、

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| id | string | 主键id |
| businessCount | int | 商机个数 |
| name | string | 客户名称 |
| stage | int | 客户阶段 |
| customerTenantId | int | 租户id |
| industry | string | 所属行业  字典 |
| employeeTotal | string | 客户规模  字典 |
| estimateOrderTotal | string | 预计购买人数 |
| channel | string | 渠道  字典 |
| installApp | string | 安装应用 |
| mobile | string | 客户手机 |
| telephone | string | 客户电话 |
| region | string | 所属地区 字典 |
| address | string | 详细地址 |
| status | string | 客户状态  字典 |
| principalUserId | string | 负责人 |
| lastRecordTime | string | 最后跟进时间 |
| description | string | 客户简介 |
| participant | string | 协同负责人 |
| oldPrincipalUserId | string | 前负责人 |
| customerAvatar | string | 客户头像 |
| salesLeadsId | string | 线索id |
| importanceNew | string | 重要度  字典 |
| documentIds | string | 文件 |
| createdBy | string | 创建人id |
| createdTime | string | 创建时间 |
| modifiedBy | string | 修改人id |
| modifiedTime | string | 修改时间 |
| allocationTime | string | 分配时间 |
| remark | string | 备注 |
| customerSource | string | 客户来源  字典 |
| workId | string | 项目id |
| lastRecordContent | string | 最后跟进内容 |

---

## CRM - 删除接口

CRM删除接口请求地址https://oapi.tita.com/crm/api/{tenantId}/delete请求url例子https://oapi.tita.com/crm/api/10086/delete请求方式POSTContent-TypeContent-Type application/json请求body

```
{
    "id": "c58441d8-4456-4980-b99c-f059ac34e30a",
    "metaObjectCode": "Crm.Customer",
    "objType":"customer"
  }
```

请求body参数说明：

| 名称 | 类型 | 说明 | 必填 |
| --- | --- | --- | --- |
| metaObjectCode | string | 对象编码：(客户：Crm.Customer 联系人：Crm.Contacts  合同：Crm.Contract  发票：Crm.Invoice  回款：Crm.Receivables  产品：Crm.Product  产品类别：Crm.ProductClassification 商机：Crm.Business 线索：Crm.SalesLeads) | 是 |
| id | string | 此记录在tita系统中主键id，可通过查询结果获取 | 是 |
| objType | 业务对象类型  (客户：customer 联系人：contacts  合同：contract  发票：invoice  回款：receivables  产品：product  产品类别：productClassification 商机: business 线索：salesLeads) | 是 |  |

返回结果示例

```
{
    "code": 0,
    "data": null,
    "errorMsg": "操作成功"

}
```

返回结果说明：

| 返回值 | 类型 | 说明 |
| --- | --- | --- |
| code | int | 状态码（0成功，其他值表示异常） |
| errorMsg | string | 错误信息 |

---

## CRM - 错误码

错误码参数说明：

| code | 提示内容 |
| --- | --- |
| 503001 | 商机名称不能为空 |
| 503002 | 商机关联客户不能为空 |
| 503003 | 商机阶段不能为空 |
| 503004 | 商机负责人不能为空 |
| 503005 | 商机预计金额不能为空 |
| 503006 | 商机预计成交日期不能为空 |
| 503007 | 客户名称不能为空 |
| 503008 | 客户所在地区不能为空 |
| 503009 | 客户负责人不能为空 |
| 503010 | 线索名称不能为空 |
| 503011 | 线索来源不能为空 |
| 503012 | 线索负责人不能为空 |
| 503022 | 回款名称关联客户不能为空 |
| 503023 | 回款金额不能为空 |
| 503024 | 回款日期不能为空 |
| 503025 | 回款负责人不能为空 |
| 503026 | 发票关联客户不能为空 |
| 503027 | 发票关联合同不能为空 |
| 503028 | 发票金额不能为空 |
| 503029 | 开票日期不能为空 |
| 503030 | 发票申请人不能为空 |

---

## CRM - 发票

发票接口新增发票请求地址https://oapi.tita.com/crm/api/{tenantId}/invoice/add请求方式POSTContent-TypeContent-Type application/json请求body

```
{
"code":"invoice_88999888",
"accountType":"0",
"principalAccount":"17690000001",
"customerId":"e9758038-4922-408a-87a6-e20732d31eac",
"orderId":"e93183b9-b5f2-460c-a15a-3a720dc9f110",
"invoiceAmount":"100.11",
"invoiceDate":"2024/10/22",
"invoiceType":"2",
"remark":"备注lllladfdf",
"invoiceTitleType":"2",
"invoiceTitle":"发票title",
"taxpayerNumber":"纳税人识别号",
"bank":"中关村银行",
"bankAccount":"bank_099933433",
"invoiceAddress":"北京市海淀区",
"phone":"6777777",
"receiver":"小明",
"receiverMobile":"19999988888",
"region":"1",
"receiveAddress":"昌平区北七家镇"
customProperties:[
    {
    "key":"department",
    "value":"111122"
    }
]
}
```

参数说明：

| 名称 | 类型 | 说明 | 必填 |
| --- | --- | --- | --- |
| accountType | int | 账号类型 （0:手机号或邮箱或姓名） | 是 |
| principalAccount | string | 负责人账号（根据account_type不同进行赋值） | 是 |
| code | string | 发票编号，不传的话，自动生成 | 否 |
| customerId | string | 关联客户id | 是 |
| orderId | string | 关联合同id | 是 |
| invoiceAmount | BigDecimal | 开票金额 | 是 |
| invoiceDate | string | 开票日期(yyyy/MM/dd) | 是 |
| invoiceType | string | 发票类型 字典 | 否 |
| remark | string | 备注 | 否 |
| invoiceTitleType | Integer | 抬头类型 | 否 |
| invoiceTitle | string | 发票抬头 | 否 |
| taxpayerNumber | string | 纳税人识别号 | 否 |
| bank | string | 开户行 | 否 |
| bankAccount | string | 开户账号 | 否 |
| invoiceAddress | string | 开票地址 | 否 |
| phone | string | 电话 | 否 |
| receiver | string | 联系人 | 否 |
| receiverMobile | string | 联系电话 | 否 |
| region | string | 地区 字典 | 否 |
| receiveAddress | string | 地址详情 | 否 |

自定义参数说明：

| 字段 | 说明 |
| --- | --- |
| key | 具体字段比如 部门是自定义字段 department |
| value | 字段中的具体值（如：研发部） |

返回结果示例

```
{
    "code": 0,
    "errorMsg": null,
    "data": {
        "objData": 2458586
    }
}
```

返回结果说明：

| 返回值 | 类型 | 说明 |
| --- | --- | --- |
| code | int | 状态码（0成功） |
| errorMsg | string | 错误信息 |
| data.objData | string | 商机主键id |

查询发票请求地址https://oapi.tita.com/crm/api/{tenantId}/invoice/search请求方式GetContent-TypeContent-Type application/json请求body

```
{
  "pageNum":1,
  "pageSize":10,
  "items": [
    {
      "name": "name",
      "value": "小明",
      "conditionType": 1,
      "operatorType": 1
    }
  ]
}
```

参数说明：

| 名称 | 类型 | 说明 | 必填 |
| --- | --- | --- | --- |
| pageNum | int | 第几页 | 是 |
| pageSize | int | 每页几条数据 | 是 |
| name | string | 字段名称 | 否 |
| items | object | 条件列表 | 否 |
| value | string | 字段具体值 | 否 |
| conditionType | int | 1等于、2大于等于、3小于等于、4大于、5小于、6范围、7为空、8不为空、9不等于、10开头等于、11结尾等于、12包含、14模糊 | 否 |
| operatorType | int | 1且  2或 | 否 |

返回结果示例

```
{
    "code": 0,
    "data": {
        "records": [
            {
                "id": "dde9b6fa-c6da-4509-9c03-ceea293708e6",
                "code": "invoice_88999888",
                "customerId": "e9758038-4922-408a-87a6-e20732d31eac",
                "orderId": "e93183b9-b5f2-460c-a15a-3a720dc9f110",
                "principalUserId": 600107545,
                "invoiceAmount": 100.11,
                "invoiceDate": "2024/10/22",
                "invoiceType": 2,
                "remark": "备注lllladfdf",
                "invoiceTitleType": 2,
                "invoiceTitle": "发票title",
                "taxpayerNumber": "纳税人识别号",
                "bank": "中关村银行",
                "bankAccount": "bank_099933433",
                "invoiceAddress": "北京市海淀区",
                "phone": "6777777",
                "receiver": null,
                "receiverMobile": "19999988888",
                "region": "1",
                "receiveAddress": "昌平区北七家镇",
                "createdBy": 600107545,
                "createdTime": "2024/10/23 16:38:12",
                "modifiedBy": 600107545,
                "modifiedTime": "2024/10/23 16:38:12"
            }
        ],
        "total": 29,
        "size": 2,
        "current": 1,
        "pages": 29
    },
    "errorMsg": "操作成功"
}
```

返回结果说明1、

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| code | int | 状态码0成功 |
| errorMsg | string | 错误信息，默认空 |
| data | Object | 对象 |

2、

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| total | int | 总条数 |
| records | list | 数据列表 |

3、

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| accountType | int | 账号类型 （0:手机号或邮箱或姓名） |
| principalAccount | string | 负责人账号（根据account_type不同进行赋值） |
| code | string | 发票编号，不传的话，自动生成 |
| customerId | string | 关联客户id |
| orderId | string | 关联合同id |
| invoiceAmount | BigDecimal | 开票金额 |
| invoiceDate | string | 开票日期(yyyy/MM/dd) |
| invoiceType | string | 发票类型 字典 |
| remark | string | 备注 |
| invoiceTitleType | Integer | 抬头类型 |
| invoiceTitle | string | 发票抬头 |
| taxpayerNumber | string | 纳税人识别号 |
| bank | string | 开户行 |
| bankAccount | string | 开户账号 |
| invoiceAddress | string | 开票地址 |
| phone | string | 电话 |
| receiver | string | 联系人 |
| receiverMobile | string | 联系电话 |
| region | string | 地区 字典 |
| receiveAddress | string | 地址详情 |
| createdBy | string | 创建人id |
| createdTime | string | 创建时间 |
| modifiedBy | string | 修改人id |
| modifiedTime | string | 修改时间 |

---

## CRM - 字典接口

字典项接口请求地址https://oapi.tita.com/crm/api/{tenant_id}/datasource/get?code=xxxxx请求方式GETContent-TypeContent-Type application/json参数说明：

| 名称 | code | 说明 |
| --- | --- | --- |
| 地区 | People.NativeRegion | 查询地区字典列表 |
| 线索来源 | Crm.SalesLeadsSource | 线索来源字典列表 |
| 客户状态 | Crm.CustomerStatus | 客户状态列表 |
| 客户阶段 | Crm.CustomerStage | 客户阶段列表 |
| 所属行业 | Crm.Industry | 所属行业列表 |
| 规模 | Crm.EmployeeTotal | 规模列表 |
| 客户来源 | Crm.CustomerSource | 客户来源列表 |
| 商机阶段 | Crm.SalesStage | 商机阶段列表 |
| 客户规模 | Crm.EmployeeTotal | 客户规模列表 |
| 渠道 | Crm.Channel | 渠道字典列表 |
| 客户重要度 | Crm.Importance | 客户重要度列表 |
| 回款方式 | Crm.ReceivableType | 回款方式字典列表 |
| 发票类型 | Crm.InvoiceType | 发票类型字典列表 |
| 发票抬头类型 | Crm.InvoiceTitleType | 发票抬头字典列表 |
| 跟进方式 | Crm.RecordType | 跟进方式字典列表 |

返回结果示例

```
{
    "code": 1,
    "errorMsg": null
    "data": {
    [
    {
        "key": "未发送",
        "value": "1"
      },
      {
        "key": "已发送",
        "value": "2"
      }
    ]
  }
}
```

---

## CRM - 修改接口

CRM修改接口请求地址https://oapi.tita.com/crm/api/modify?tenantId=?&objType=?&formCode=?&needApproval=?&accountType=?&deptType=?&operatorUser=?请求url例子https://oapi.tita.com/crm/api/modify?tenantId=10086&objType=customer&formCode=Crm.Customer.CreateForm&needApproval=2&accountType=0&deptType=1&operatorUser=13111111111请求方式POSTContent-TypeContent-Type application/json请求body

```
[
  {
    "metaObjectCode": "Crm.Customer",
    "id": "0a0f27f8-ab0e-4a63-a4d5-27c90fc6da47",
    "fields": [
      {
        "name": "PrincipalUserId",
        "value": "9638c0f3-5569-4230-a175-4562b8274c71@tita-weixin.com"
      },
      {
        "name": "Name",
        "value": "客户名称"
      },
      {
        "name": "Mobile",
        "value": "13112345678"
      }
    ]
  }
]
```

url地址中参数说明：

| 名称 | 类型 | 说明 | 必填 |
| --- | --- | --- | --- |
| tenantId | int | 租户id | 是 |
| objType | string | 对象类型 (合同：contract 客户: customer 发票：invoice 联系人：contacts 产品：product 回款：receivables 产品类别：productClassification 商机：business 线索：salesLeads) | 是 |
| formCode | string | 表单编码( 合同：Crm.Contract.CreateForm 客户：Crm.Customer.CreateForm 发票：Crm.Invoice.CreateForm 联系人：Crm.Contacts.CreateForm 产品：Crm.Product.CreateForm 回款：Crm.Receivables.CreateForm 产品类别：Crm.ProductClassification.CreateForm 商机：Crm.Business.CreateForm  线索：Crm.SalesLeads.CreateForm) | 是 |
| needApproval | string | 是否需要经过审批 (1:需要（租户配置了审批流，则经过审批，否则不经过） 2 ：不需要（租户即使配置了审批流也不执行审批）  3：不干预，以tita系统逻辑为主) | 是 |
| accountType | int | 用户id类型（0:手机号或邮箱或姓名） | 是 |
| deptType | int | 部门id类型（0:使用tita系统部门编码  1：使用三方corpid） | 是 |
| operatorUser | string | 操作人(手机号或邮箱或姓名) | 是 |

请求body参数说明：

| 名称 | 类型 | 说明 | 必填 |
| --- | --- | --- | --- |
| metaObjectCode | string | 对象编码：(客户：Crm.Customer 联系人：Crm.Contacts  合同：Crm.Contract  发票：Crm.Invoice  回款：Crm.Receivables  产品：Crm.Product  产品类别：Crm.ProductClassification 线索：Crm.SalesLeads 商机：Crm.Business) | 是 |
| id | string | 此记录在tita系统中主键id，可通过查询结果获取 | 是 |
| fields | 数组 | 参数集合，请参考业务对象字段信息页面 | 是 |

返回结果示例

```
{
    "code": 0,
    "data": null,
    "errorMsg": "操作成功"

}
```

返回结果说明：

| 返回值 | 类型 | 说明 |
| --- | --- | --- |
| code | int | 状态码（0成功，其他值表示异常） |
| errorMsg | string | 错误信息 |

---

## CRM - 业务对象字段信息

各业务对象字段属性列表客户参数说明：

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| Name | string | 客户名称 |
| Stage | string | 客户阶段 |
| Industry | string | 所属行业 |
| Channel | string | 渠道 |
| EmployeeTotal | string | 客户规模 |
| Mobile | string | 客户手机号 |
| Region | string | 所属地区 |
| Address | string | 详细地址 |
| Status | string | 客户状态 |
| PrincipalUserId | string | 负责人 |
| Participant | string | 协同负责人 |
| Remark | string | 备注 |
| ParticipantUserId | string | 协同人 |

合同参数说明：

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| FinishReceivablesAmount | BigDecimal | 已回款金额 |
| NoReceivablesAmount | BigDecimal | 未回款金额 |
| PrincipalUserId | string | 负责人 |
| DealPeriod | string | 成交周期 |
| Name | string | 合同名称 |
| CustomerId | string | 关联客户id |
| StartTime | string | 开始时间 |
| EndTime | string | 到期时间 |
| Amount | string | 合同金额 |
| OrderType | string | 订单类型 |
| SignUserId | string | 公司签约人 |
| SignTime | string | 签订日期 |
| ContractType | string | 合同类型 |
| ParticipantUserId | string | 协同人 |
| SignContactId | string | 客户签订人 |

发票参数说明：

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| OrderId | string | 关联合同id |
| InvoiceDate | string | 开票日期 |
| InvoiceAmount | string | 开票金额 |
| InvoiceType | string | 发票类型 |
| InvoiceTitleType | string | 发票抬头类型 |
| CustomerId | string | 关联客户id |
| InvoiceTitle | string | 发票抬头 |
| TaxpayerNumber | string | 纳税人识别号 |
| Bank | string | 开户行 |
| receiver | string | 邮寄联系人 |
| BankAccount | string | 开户账号 |
| ReceiverMobile | string | 收件人电话 |
| ReceiveAddress | string | 收件人地址 |
| Remark | string | 备注 |
| PrincipalUserId | string | 负责人 |
| InvoiceAddress | string | 开票地址 |
| Phone | string | 电话 |

产品参数说明：

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| Name | string | 产品名称 |
| ProductClassificationId | string | 产品分类id |
| Persons | string | 可见人员id |
| Departments | string | 可见部门id |
| Standards | string | 规格 |
| BarCode | string | 产品条码 |
| CostPrice | string | 成本 |
| Price | string | 单价 |
| Code | string | 产品编号 |
| Remark | string | 产品简介 |
| Unit | string | 产品单位 |

产品分类参数说明：

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| Name | string | 分类名称 |
| ParentId | string | 上级分类id |

联系人参数说明：

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| Name | string | 姓名 |
| Mobile | string | 手机号 |
| Position | string | 职务 |
| Telephone | string | 电话 |
| Email | string | 邮箱 |
| Remark | string | 备注 |
| PrincipalUserId | string | 负责人 |
| CustomerId | string | 关联客户id |
| Sex | string | 性别 |
| DecisionMakingRelationships | string | 决策关系 |
| InteractiveStyle | string | 互动风格 |
| Intimacy | string | 亲密度 |
| ParticipantUserId | string | 协同人 |

回款参数说明：

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| OrderId | string | 关联合同id |
| CustomerId | string | 关联客户id |
| Amount | string | 回款金额 |
| ParticipantUserId | string | 协同人 |
| ReceivableModel | string | 回款方式 |
| PrincipalUserId | string | 负责人 |
| Remark | string | 备注 |
| ReceivablesType | string | 回款类型 |
| Name | string | 回款名称 |
| ReturnedMoneyTime | string | 回款日期 |

商机参数说明：

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| Name | string | 商机名称 |
| CustomerId | string | 关联客户id |
| Stage | int | 商机阶段 |
| Channel | string | 渠道 |
| OrderTotal | string | 购买人数 |
| Amount | string | 购买金额 |
| Competitor | string | 竞品信息 |
| PrincipalUserId | string | 负责人 |
| Remark | string | 备注 |
| FinishDealTime | string | 预计成交时间 |
| ParticipantUserId | string | 协同人 |

线索参数说明：

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| Name | string | 线索名称 |
| Mobile | string | 手机号 |
| Telephone | string | 电话 |
| Source | int | 线索来源 |
| PrincipalUserId | string | 负责人 |
| ParticipantUserId | string | 协同人 |
| Remark | string | 备注 |

关联产品对象参数说明：

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| Name | string | 产品名称（必填） |
| ProductId | string | 产品id（必填） |
| BarCode | string | 产品条码 |
| Unit | string | 产品单位 |
| ProductNumber | string | 数量（必填） |
| Price | string | 单价（元）（必填） |
| SellPrice | string | 售价（元）（必填） |
| SellPriceTotal | string | 售价小计（元）（必填） |
| Code | string | 产品编码 |
| BusinessId | string | 所属商机id |

跟进记录参数说明：

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| RecordType | string | 类型（必填） |
| CustomerId | string | 客户 |
| SalesLeadsId | string | 线索 |
| VisitId | string | 访客计划 |
| BusinessId | string | 商机 |
| QuotationId | string | 报价单 |
| PaymentCollectionId | string | 回款计划 |
| ContactsId | string | 联系人 |
| CecordType | string | 跟进方式（必填） |
| Content | string | 跟进内容（必填） |
| NextRecordTimeNew | string | 下次跟进时间 |

报价单参数说明：

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| Code | string | 报价单编号 |
| Name | string | 报价单名称 |
| CustomerId | string | 关联客户id |
| BusinessId | string | 关联商机id |
| ProductId | string | 关联产品id |
| PrincipalUserId | Integer | 负责人 |
| VersionNumber | Integer | 版本 |
| QuotationUserId | Integer | 报价人 |
| QuotationDate | Date | 报价日期 |
| QuotationInvalidDate | Date | 失效日期 |
| Amount | BigDecimal | 报价金额 |
| contacts | string | 联系人 |

访客计划参数说明：

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| CustomerId | string | 关联客户id |
| VisitTime | string | 执行时间 |
| Name | string | 计划名称 |
| PrincipalUserId | Integer | 负责人 |
| BusinessId | string | 关联商机id |
| AssociatedContactId | string | 关联联系人id |

回款计划参数说明：

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| PlanNo | string | 计划编号 |
| AssociatedCustomer | string | 关联客户id |
| AssociatedContract | string | 关联合同id |
| CollectionAmount | BigDecimal | 计划回款金额 |
| CollectionDate | Date | 计划回款日期 |
| PrincipalUserId | Integer | 负责人 |
| ReceivedAmount | BigDecimal | 已回款金额 |
| UnpaidAmount | BigDecimal | 未回款金额 |

---

## CRM - 回款

回款接口新增回款请求地址https://oapi.tita.com/crm/api/{tenantId}/receivables/add请求方式POSTContent-TypeContent-Type application/json请求body

```
{
"accountType":"0",
"principalAccount":"89899988@qq.com",
"code":"回款编号",
"customerId":"ff3d1eae-0fff-4803-b067-0a904e677c13",
"orderId":"dd3d1eae-0fff-4803-b067-0a904e677cc5",
"amount":"100.11",
"returnedMoneyTime":"2024/05/05",
"receivableModel":"2",
"remark":"备注信息",
customProperties:[
    {
    "key":"department",
    "value":"111122"
    }
]
}
```

参数说明：

| 名称 | 类型 | 说明 | 必填 |
| --- | --- | --- | --- |
| accountType | int | 账号类型 （0:手机号或邮箱或姓名） | 是 |
| principalAccount | string | 负责人账号（根据account_type不同进行赋值） | 是 |
| code | string | 回款编号 | 否 |
| customerId | string | 关联客户id | 是 |
| orderId | string | 关联合同id | 否 |
| amount | BigDecimal | 回款金额 | 是 |
| returnedMoneyTime | string | 回款日期(yyyy/MM/dd) | 是 |
| receivableModel | string | 回款方式 字典 | 否 |
| remark | string | 备注 | 否 |
| customProperties | array | 数组对象，自定义字段放到这个里面，看下面自定义字段说句 | 否 |

自定义参数说明：

| 字段 | 说明 |
| --- | --- |
| key | 具体字段比如 部门是自定义字段 department |
| value | 字段中的具体值（如：研发部） |

返回结果示例

```
{
    "code": 0,
    "errorMsg": null,
    "data": {
        "objData": 2458586
    }
}
```

返回结果说明：

| 返回值 | 类型 | 说明 |
| --- | --- | --- |
| code | int | 状态码（0成功） |
| errorMsg | string | 错误信息 |
| data.objData | string | 商机主键id |

查询回款请求地址https://oapi.tita.com/crm/api/{tenantId}/receivables/search请求方式GetContent-TypeContent-Type application/json请求body

```
{
  "pageNum":1,
  "pageSize":10,
  "items": [
    {
      "name": "name",
      "value": "小明",
      "conditionType": 1,
      "operatorType": 1
    }
  ]
}
```

参数说明：

| 名称 | 类型 | 说明 | 必填 |
| --- | --- | --- | --- |
| pageNum | int | 第几页 | 是 |
| pageSize | int | 每页几条数据 | 是 |
| name | string | 字段名称 | 否 |
| items | object | 条件列表 | 否 |
| value | string | 字段具体值 | 否 |
| conditionType | int | 1等于、2大于等于、3小于等于、4大于、5小于、6范围、7为空、8不为空、9不等于、10开头等于、11结尾等于、12包含、14模糊 | 否 |
| operatorType | int | 1且  2或 | 否 |

返回结果示例

```
{
    "code": 0,
    "data": {
        "records": [
            {
                "id": "f0757476-c9c7-4ca9-98fc-f9eaf71ca00d",
                "principalUserId": 600107545,
                "customerId": "e9758038-4922-408a-87a6-e20732d31eac",
                "orderId": "e93183b9-b5f2-460c-a15a-3a720dc9f110",
                "amount": 100.11,
                "returnedMoneyTime": "2024/10/22",
                "receivableModel": 2,
                "remark": "备注lllladfdf",
                "code": "RMO.202410230003",
                "createdBy": 600107545,
                "createdTime": "2024/10/23 15:57:53",
                "modifiedBy": 600107545,
                "modifiedTime": "2024/10/23 15:57:53"
            }
        ],
        "total": 29,
        "size": 2,
        "current": 1,
        "pages": 29
    },
    "errorMsg": "操作成功"
}
```

返回结果说明1、

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| code | int | 状态码0成功 |
| errorMsg | string | 错误信息，默认空 |
| data | Object | 对象 |

2、

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| total | int | 总条数 |
| records | list | 数据列表 |

3、

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| id | string | 主键id |
| principalUserId | string | 负责人id |
| customerId | string | 客户id |
| orderId | string | 合同id |
| amount | BigDecimal | 回款金额 |
| returnedMoneyTime | String | 回款日期 |
| receivableModel | string | 回款类型  字典 |
| remark | string | 备注 |
| code | string | 回款编号 |
| createdBy | string | 创建人id |
| createdTime | string | 创建时间 |
| modifiedBy | string | 修改人id |
| modifiedTime | string | 修改时间 |

---

## CRM - 销售线索

线索接口新增线索请求地址https://oapi.tita.com/crm/api/{tenantId}/salesleads/add请求方式POSTContent-TypeContent-Type application/json请求body

```
{
"accountType":"0",
"principalAccount":"19922322222",
"name":"小明",
"mobile":"19933211111",
"telephone":"6716150",
"region":"2",
"address":"详细地址",
"sourceType":"3",
"remark":"备注信息",
customProperties:[
    {
    "key":"department",
    "value":"111122"
    }
]
}
```

参数说明：

| 名称 | 类型 | 说明 | 必填 |
| --- | --- | --- | --- |
| accountType | int | 账号类型 （0:手机号或邮箱或姓名） | 是 |
| principalAccount | string | 负责人账号（根据account_type不同进行赋值） | 是 |
| name | string | 线索名称 | 是 |
| mobile | string | 手机号 | 否 |
| telephone | string | 电话 | 否 |
| region | string | 所属地区编码，字典 | 否 |
| address | string | 详细地址 | 否 |
| sourceType | string | 线索来源参考字典 | 否 |
| remark | string | 备注 | 否 |
| customProperties | array | 数组对象，自定义字段放到这个里面，看下面自定义字段说句 | 否 |

自定义参数说明：

| 字段 | 说明 |
| --- | --- |
| key | 具体字段比如 部门是自定义字段 department |
| value | 字段中的具体值（如：研发部） |

返回结果示例

```
{
    "code": 0,
    "errorMsg": null,
    "data": {
        "objData": 2458586
    }
}
```

返回结果说明：

| 返回值 | 类型 | 说明 |
| --- | --- | --- |
| code | int | 状态码（0成功） |
| errorMsg | string | 错误信息 |
| data.objData | string | 线索主键id |

修改线索请求地址https://oapi.tita.com/crm/api/{tenantId}/salesleads/update请求方式POSTContent-TypeContent-Type application/json请求body

```
{
"id":"111111111111",
"accountType":"0",
"principalAccount":"19922322222",
"name":"小明",
"mobile":"19933211111",
"telephone":"6716150",
"region":"2",
"address":"详细地址",
"sourceType":"3",
"remark":"备注信息",
customProperties:[
    {
    "key":"department",
    "value":"111122"
    }
]
}
```

参数说明：

| 名称 | 类型 | 说明 | 必填 |
| --- | --- | --- | --- |
| id | int | 主键id | 是 |
| accountType | int | 账号类型 （0:手机号或邮箱或姓名） | 是 |
| principalAccount | string | 负责人账号（根据account_type不同进行赋值） | 是 |
| name | string | 线索名称 | 是 |
| mobile | string | 手机号 | 否 |
| telephone | string | 电话 | 否 |
| region | string | 所属地区编码，字典 | 否 |
| address | string | 详细地址 | 否 |
| sourceType | string | 线索来源参考字典 | 否 |
| remark | string | 备注 | 否 |
| customProperties | array | 数组对象，自定义字段放到这个里面，看下面自定义字段说句 | 否 |

自定义参数说明：

| 字段 | 说明 |
| --- | --- |
| key | 具体字段比如 部门是自定义字段 department |
| value | 字段中的具体值（如：研发部） |

返回结果示例

```
{
    "code": 0,
    "errorMsg": null,
    "data": {
        "objData": 2458586
    }
}
```

返回结果说明：

| 返回值 | 类型 | 说明 |
| --- | --- | --- |
| code | int | 状态码（0成功） |
| errorMsg | string | 错误信息 |
| data.objData | string | 线索主键id |

查询线索请求地址https://oapi.tita.com/crm/api/{tenantId}/salesleads/search请求方式GetContent-TypeContent-Type application/json请求body

```
{
  "pageNum":1,
  "pageSize":10,
  "items": [
    {
      "name": "name",
      "value": "小明",
      "conditionType": 1,
      "operatorType": 1
    }
  ]
}
```

参数说明：

| 名称 | 类型 | 说明 | 必填 |
| --- | --- | --- | --- |
| pageNum | int | 第几页 | 是 |
| pageSize | int | 每页几条数据 | 是 |
| name | string | 字段名称 | 否 |
| items | object | 条件列表 | 否 |
| value | string | 字段具体值 | 否 |
| conditionType | int | 1等于、2大于等于、3小于等于、4大于、5小于、6范围、7为空、8不为空、9不等于、10开头等于、11结尾等于、12包含、14模糊 | 否 |
| operatorType | int | 1且  2或 | 否 |

返回结果示例

```
{
    "code": 0,
    "data": {
        "records": [
            {
                "id": "2dc08b2d-dc06-4340-b9ad-beded1e8d554",
                "feedId": null,
                "industry": null,
                "principalUserId": 600095451,
                "remark": null,
                "address": null,
                "status": 4,
                "telephone": null,
                "email": null,
                "mobile": null,
                "name": "附件测试",
                "region": null,
                "documentIds": "18638",
                "sourceType": "1",
                "allocationTime": "2024-06-13 10:52:32",
                "customerId": null,
                "createdBy": 600095451,
                "createdTime": "2024-06-07 13:59:59",
                "modifiedBy": 600095451,
                "modifiedTime": "2024-06-13 10:52:32"
            }
        ],
        "total": 19,
        "size": 1,
        "current": 1,
        "pages": 2
    },
    "errorMsg": "操作成功"
}
```

返回结果说明1、

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| code | int | 状态码0成功 |
| errorMsg | string | 错误信息，默认空 |
| data | Object | 对象 |

2、

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| total | int | 总条数 |
| records | list | 数据列表 |

3、

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| id | string | 主键id |
| feedId | string | feedId |
| industry | int | 所属行业 |
| principalUserId | string | 负责人id |
| remark | string | 备注 |
| address | string | 地址 |
| status | int | 线索状态字典 1待跟进 2 跟进中 3已转换 4无效 |
| telephone | string | 电话 |
| email | string | 邮箱 |
| mobile | string | 手机号 |
| name | string | 线索名称 |
| region | string | 地区字典 |
| sourceType | string | 来源字典 |
| allocationTime | string | 分配时间	yyyy/M/d H:mm:ss |
| documentIds | string | 附件id，多个用逗号隔开 |
| customerId | string | 客户id |
| createdBy | string | 创建人id |
| createdTime | string | 创建时间 |
| modifiedBy | string | 修改人id |
| modifiedTime | string | 修改时间 |

---

## CRM - 查询接口

CRM查询接口请求地址https://oapi.tita.com/crm/api/{tenantId}/search请求url例子https://oapi.tita.com/crm/api/10086/search请求方式POSTContent-TypeContent-Type application/json请求body

```
{
  "pageNum":1,
  "pageSize":10,
  "items": [
    {
      "name": "name",
      "value": "张三",
      "conditionType": 12,
      "operatorType": 1
    }
  ],
  "metaObjectCode":"Crm.Customer"
}
```

请求body参数说明：

| 名称 | 类型 | 说明 | 必填 |
| --- | --- | --- | --- |
| pageNum | int | 第几页 | 是 |
| pageSize | int | 每页几条数据 | 是 |
| name | string | 字段名称 | 否 |
| items | object | 条件列表 | 否 |
| value | string | 字段具体值 | 否 |
| operatorType | int | 1等于 2大于等于、3小于等于、4大于、5小于、6范围、7为空、8不为空、9不等于、10开头等于、11结尾等于、12包含、14模糊 | 否 |
| conditionType | int | 1且  2或 | 否 |
| metaObjectCode | string | 对象编码：(关联产品对象:Crm.BusinessProduct 客户：Crm.Customer 联系人：Crm.Contacts  合同：Crm.Contract  发票：Crm.Invoice  回款：Crm.Receivables  产品：Crm.Product  产品类别：Crm.ProductClassification 线索：Crm.SalesLeads) | 是 |

返回结果示例

```
{
    "code": 0,
    "data": [
        {
            "fields": [
                {
                    "name": "AllocationTime",
                    "value": "2024/07/10 16:48:20"
                },
                {
                    "name": "BusinessCount",
                    "value": "0"
                },
                {
                    "name": "CreatedBy",
                    "value": "600108074"
                },
                {
                    "name": "CreatedTime",
                    "value": "2024/07/10 16:43:59"
                },
                {
                    "name": "CustomerSource",
                    "value": "2"
                },
                {
                    "name": "EmployeeTotal",
                    "value": "2"
                },
                {
                    "name": "FeedId",
                    "value": "600201_4918_36_8_638562266390000000"
                },
                {
                    "name": "ImportanceNew",
                    "value": "4"
                },
                {
                    "name": "Industry",
                    "value": "5"
                },
                {
                    "name": "IsDelete",
                    "value": "False"
                },
                {
                    "name": "IsOpenPool",
                    "value": "True"
                },
                {
                    "name": "ModifiedBy",
                    "value": "10000"
                },
                {
                    "name": "ModifiedTime",
                    "value": "2024/07/11 18:12:12"
                },
                {
                    "name": "Name",
                    "value": "客户A00000001"
                },
                {
                    "name": "OldPrincipalUserId",
                    "value": "600108074"
                },
                {
                    "name": "Owner",
                    "value": "600108074"
                },
                {
                    "name": "PoolId",
                    "value": "8fd1140b-9d3d-4ddc-988a-0158bd30bb9c"
                },
                {
                    "name": "PutPoolTime",
                    "value": "2024/07/11 15:10:39"
                },
                {
                    "name": "Region",
                    "value": "12"
                },
                {
                    "name": "Stage",
                    "value": "3"
                },
                {
                    "name": "Status",
                    "value": "3"
                },
                {
                    "name": "id",
                    "value": "db77ba6e-393e-4bcc-94df-657e8264f6d3"
                }
            ]
        }
    ],
    "errorMsg": "操作成功"
}
```

返回结果说明：

| 返回值 | 类型 | 说明 |
| --- | --- | --- |
| code | int | 状态码（0成功，其他值表示异常） |
| errorMsg | string | 错误信息 |

---

# 业务API

## 面谈接口

获取指定时间段内面谈列表2.InterviewListModel3.InterviewModel4.UserModel获取指定面谈信息详情返回结果：1.InterviewRecordModel2.UserModel<font color="#dd0000">注：开发文档内所有涉及编码处均已UTF-8形式编码！！！</font>https://oapi.tita.com/api/{tenant_id}/interview/searchGet请求参数

| 参数名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| tenant_id | int | 是 | 租户标识 |
| page_num | int | 是 | 页码 |
| page_size | int | 是 | 单页数量 |
| start_date | string | 是 | 开始时间 |
| end_date | string | 是 | 截止时间 |

返回结果示例

```
{
	"code": 0,
	"errorMsg": null,
	"data": {
		"total": 2,
		"interviews": [{
			"name": 面谈标题,
			"interview_date": "2020/10/01 00:00:00",
			"user": {
				"userId": 200149381,
				"name": "",
				"email": "",
				"mobile": "",
				"wx_userId": "",
				"departmentName": "技术部"
			},
			"toUser": {
				"userId": 200149381,
				"name": "",
				"email": "",
				"mobile": "",
				"wx_userId": "",
				"departmentName": "技术部"
			}
		}]
	}
}
```

返回结果说明

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| code | int | 状态码 |
| message | string | 错误信息 |
| data | InterviewListModel | 面谈集合 |

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| total | int | 面谈条数 |
| interviews | List<InterviewModel> | 面谈列表 |

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| interview_id | string | 面谈标识 |
| name | string | 面谈标题 |
| user | UserModel | 面谈人 |
| toUser | UserModel | 被面谈人 |
| interview_date | string | 面谈时间 |

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| userId | int | 人员Id |
| name | string | 人员名称 |
| email | string | 邮箱 |
| mobile | string | 手机号 |
| departmentName | string | 部门名称 |
| wx_userId | string | 企业微信ID |

https://oapi.tita.com/api/{tenant_id}/interview/getInterviewRecordsPostContent-Type	application/json请求Body

```
{
    "interview_ids":["288736760009048064","288751639271137280"]
}
```

参数说明

| 参数名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| tenant_id | int | 是 | 租户标识 |
| interview_ids | List<string> | 是 | 面谈标识 |

```
{
	"code": 0,
	"errorMsg": null,
	"data": [
		{
			"user": {
				"userId": 500000048,
				"name": "Bazahey",
				"email": "zhangjiajia123@tita.com",
				"mobile": "13366131331",
				"wxUserId": "",
				"departmentName": "默认部门",
				"staffCode": "lvshou0021"
			},
			"toUser": {
				"userId": 500000057,
				"name": "张一一",
				"email": "zhang01@b.com",
				"mobile": "13990000001",
				"wxUserId": "",
				"departmentName": "一级部门A",
				"staffCode": "2017040029"
			},
			"name": "面谈名称",
			"id": "288771559271276544",
			"interviewTime": "2022/01/01 19:30:00",
			"interviewType": null,
			"content": "{\"doc\":{\"type\":\"doc\",\"content\":[{\"type\":\"heading\",\"attrs\":{\"level\":1,\"textAlign\":\"left\"},\"content\":[{\"type\":\"text\",\"marks\":[{\"type\":\"backgroundColor\",\"attrs\":{\"color\":\"transparent\"}}],\"text\":\"🛫过程\"}]},{\"type\":\"bulletList\",\"content\":[{\"type\":\"listItem\",\"content\":[{\"type\":\"paragraph\",\"attrs\":{\"textAlign\":\"left\"},\"content\":[{\"type\":\"text\",\"marks\":[{\"type\":\"backgroundColor\",\"attrs\":{\"color\":\"transparent\"}}],\"text\":\"上一阶段的 OKR 完成的怎么样？\"}]}]},{\"type\":\"listItem\",\"content\":[{\"type\":\"paragraph\",\"attrs\":{\"textAlign\":\"left\"},\"content\":[{\"type\":\"text\",\"marks\":[{\"type\":\"backgroundColor\",\"attrs\":{\"color\":\"transparent\"}}],\"text\":\"有哪些成功的经验或者是失败的教训？\"}]}]},{\"type\":\"listItem\",\"content\":[{\"type\":\"paragraph\",\"attrs\":{\"textAlign\":\"left\"},\"content\":[{\"type\":\"text\",\"marks\":[{\"type\":\"backgroundColor\",\"attrs\":{\"color\":\"transparent\"}}],\"text\":\"是否做出一些以前没有使用过的新方法？\"}]}]},{\"type\":\"listItem\",\"content\":[{\"type\":\"paragraph\",\"attrs\":{\"textAlign\":\"left\"},\"content\":[{\"type\":\"text\",\"marks\":[{\"type\":\"backgroundColor\",\"attrs\":{\"color\":\"transparent\"}}],\"text\":\"你遇到了哪些难以解决的障碍？\"}]}]},{\"type\":\"listItem\",\"content\":[{\"type\":\"paragraph\",\"attrs\":{\"textAlign\":\"left\"},\"content\":[{\"type\":\"text\",\"marks\":[{\"type\":\"backgroundColor\",\"attrs\":{\"color\":\"transparent\"}}],\"text\":\"你是如何进行调整的？\"}]}]},{\"type\":\"listItem\",\"content\":[{\"type\":\"paragraph\",\"attrs\":{\"textAlign\":\"left\"},\"content\":[{\"type\":\"text\",\"marks\":[{\"type\":\"backgroundColor\",\"attrs\":{\"color\":\"transparent\"}}],\"text\":\"如果能重来，你会重点关注哪个环节？\"}]}]}]},{\"type\":\"heading\",\"attrs\":{\"level\":1,\"textAlign\":\"left\"},\"content\":[{\"type\":\"text\",\"marks\":[{\"type\":\"backgroundColor\",\"attrs\":{\"color\":\"transparent\"}}],\"text\":\"🌅展望\"}]},{\"type\":\"bulletList\",\"content\":[{\"type\":\"listItem\",\"content\":[{\"type\":\"paragraph\",\"attrs\":{\"textAlign\":\"left\"},\"content\":[{\"type\":\"text\",\"marks\":[{\"type\":\"backgroundColor\",\"attrs\":{\"color\":\"transparent\"}}],\"text\":\"下一阶段你的目标是什么？\"}]}]},{\"type\":\"listItem\",\"content\":[{\"type\":\"paragraph\",\"attrs\":{\"textAlign\":\"left\"},\"content\":[{\"type\":\"text\",\"marks\":[{\"type\":\"backgroundColor\",\"attrs\":{\"color\":\"transparent\"}}],\"text\":\"具体的关键结果是什么？\"}]}]},{\"type\":\"listItem\",\"content\":[{\"type\":\"paragraph\",\"attrs\":{\"textAlign\":\"left\"},\"content\":[{\"type\":\"text\",\"marks\":[{\"type\":\"backgroundColor\",\"attrs\":{\"color\":\"transparent\"}}],\"text\":\"你确定这就是你未来的OKR吗？\"}]}]},{\"type\":\"listItem\",\"content\":[{\"type\":\"paragraph\",\"attrs\":{\"textAlign\":\"left\"},\"content\":[{\"type\":\"text\",\"marks\":[{\"type\":\"backgroundColor\",\"attrs\":{\"color\":\"transparent\"}}],\"text\":\"你可能会遇到什么样的风险？\"}]}]},{\"type\":\"listItem\",\"content\":[{\"type\":\"paragraph\",\"attrs\":{\"textAlign\":\"left\"},\"content\":[{\"type\":\"text\",\"marks\":[{\"type\":\"backgroundColor\",\"attrs\":{\"color\":\"transparent\"}}],\"text\":\"你需要得到什么样的资源？\"}]}]},{\"type\":\"listItem\",\"content\":[{\"type\":\"paragraph\",\"attrs\":{\"textAlign\":\"left\"},\"content\":[{\"type\":\"text\",\"marks\":[{\"type\":\"backgroundColor\",\"attrs\":{\"color\":\"transparent\"}}],\"text\":\"为了达成，你是否有一些新的方法可以尝试？\"}]}]},{\"type\":\"listItem\",\"content\":[{\"type\":\"paragraph\",\"attrs\":{\"textAlign\":\"left\"},\"content\":[{\"type\":\"text\",\"marks\":[{\"type\":\"backgroundColor\",\"attrs\":{\"color\":\"transparent\"}}],\"text\":\"除此之外，还有哪些方法？\"}]}]}]}]},\"selection\":{\"type\":\"text\",\"anchor\":134,\"head\":253}}"
		}
	]
}
```

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| interview_id | string | 面谈标识 |
| name | string | 面谈标题 |
| user | UserModel | 面谈人 |
| toUser | UserModel | 被面谈人 |
| interview_date | string | 面谈时间 |
| content | string | 面谈内容 |

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| userId | int | 人员Id |
| name | string | 人员名称 |
| email | string | 邮箱 |
| mobile | string | 手机号 |
| departmentName | string | 部门名称 |
| wx_userId | string | 企业微信ID |

---

## API列表 - 概述

概述> 平台提供了基于OAuth2.0授权保护的API资源，使用这些 API 可以帮助企业灵活地对接现有的IT系统，API调用前必须现获取授权令牌，
> 授权令牌获取方法
> 。
[授权令牌获取方法](/#/server/oauth2/ClientCredential)Open API 说明> Open API 提供主动调用的连接方式。当你的应用调用开放平台接口时，需使遵守文档开发标准，文档内编码统一使用
> UTF-8编码
> 。
> 使用授权令牌调用API前应判断授权令牌是否过期，未过期授权可连续使用，有效期内重新获取会导致原有授权失效。
> 使用OAuth2.0 AccessToken时如令牌过期，使用RefreshToken刷新即可
> OAuth2.0 令牌刷新
> 点击链接查看
*UTF-8编码*[OAuth2.0 令牌刷新](/#/server/oauth2/RefreshToken)

---

## 错误返回码

错误返回码信息1、系统级

| 错误码 | 注释说明 |
| --- | --- |
| 10001 | 系统内部错误 |
| 10002 | 服务不可用 |
| 10003 | IP限制不能请求该资源 |
| 10004 | 该资源需要appkey拥有授权 |
| 10005 | 缺少appkey参数 |
| 10006 | 任务超时 |
| 10007 | 参数错误 |
| 10008 | 接口不存在 |
| 10009 | HTTP METHOD不支持 |
| 10010 | url参数的tenant_id非法 |
| 10011 | url参数的use_id非法 |
| 10012 | 超过最大值 |
| 10013 | 批量修改的用户类型不能混合 |

2、目标

| 错误码 | 注释说明 |
| --- | --- |
| 12001 | 参数错误 |
| 12003 | 编辑状态失败 |
| 12004 | 目标不存在 |
| 12005 | 关键成果 kr不存在 |

3、任务

| 错误码 | 注释说明 |
| --- | --- |
| 13001 | 参数错误 |
| 13002 | 任务添加失败 |
| 13003 | 编辑状态失败 |
| 13004 | 任务不存在 |
| 13005 | 任务删除失败 |
| 13006 | 任务量化值不存在 |
| 13007 | 任务编辑失败 |
| 13008 | 任务附件参数错误 |

4、项目、里程碑

| 错误码 | 注释说明 |
| --- | --- |
| 14001 | 参数错误 |
| 14003 | 编辑状态失败 |
| 14004 | 项目不存在 |
| 14005 | 项目更新失败 |
| 14006 | 里程碑更新失败 |
| 14007 | 里程碑已存在（第三方ID重复创建） |
| 14008 | 里程碑不存在 |

5、关键成果

| 错误码 | 注释说明 |
| --- | --- |
| 15001 | 参数错误 |

6、人员组织架构

| 错误码 | 注释说明 |
| --- | --- |
| 16001 | 部门参数错误 |
| 16002 | 部门添加编辑删除逻辑失败 |
| 16003 | 人员参数错误 |
| 16004 | 人员添加失败 |
| 16005 | 部门不存在 |
| 16006 | 邮箱被占用 |
| 16007 | 手机号被占用 |
| 16008 | 上级账号不存在 |
| 16009 | 账号不存在 |
| 16010 | 账号修改失败 |
| 16011 | 账号离职失败 |

7、职位

| 错误码 | 注释说明 |
| --- | --- |
| 17001 | 职位编码已经存在 |
| 17002 | 创建职位失败 |
| 17003 | 编辑职位失败 |
| 17004 | 删除职位失败 |
| 17005 | 参数错误 |
| 17006 | 职位不存在 |

---

## 总结接口

添加总结①summary_date 总结所属日期 ， 日报：2020/11/18     周报（2020年11月第1周周报）：2020/11/1     周报（2020年11月第2周周报）：2020/11/2   月报（2020年11月月报）：2020/11/01   月报（2020年12月月报）：2020/12/01）
*目前只支持纯文本写总结编辑总结①summary_date 总结所属日期 ， 日报：2020/11/18     周报（2020年11月第1周周报）：2020/11/1     周报（2020年11月第2周周报）：2020/11/2   月报（2020年11月月报）：2020/11/01   月报（2020年12月月报）：2020/12/01）
*目前只支持纯文本写总结，会覆盖对应文本内容，其他组件信息不影响获取指定时间段内创建的总结2.PlanDailyListModel3.PlanDailyModel①daily_date 总结所属日期 ， 日报：2020/11/18     周报（2020年11月第1周周报）：2020/11/1     周报（2020年11月第2周周报）：2020/11/2   月报（2020年11月月报）：2020/11/01   月报（2020年12月月报）：2020/12/01）4.UserModel5.UserModel获取指定时间段内创建的总结ID集合-返回结果示例2.PlanDailyIdListModel

| ids | List | Id |
| --- | --- | --- |

https://oapi.tita.com/api/{tenant_id}/daily/addPostContent-Type	application/json请求Body

| 参数名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| tenant_id | int | 是 | 租户标识 |
| account_type | int | 是 | 账号类型 （0:手机号或邮箱 1：企业微信账号 2：钉钉账号） |
| account_name | string | 是 | 创建人账号（根据account_type不同进行赋值） |
| template_name | string | 是 | 总结模板名称 |
| summary_type | int | 是 | 总结类型,默认是全部 （8：日报 26：周报 27：月报） |
| summary_date | string | 是 | 总结日期① |
| modules | List<Module> | 是 | 组件内容 |
| name | string | 是 | 组件名称 |
| content | string | 是 | 组件内容 |

请求示例

```
{
    "template_name":"日报",
    "account_name":"",
    "summary_type":"8",
    "summary_date":"2025/10/7",
    "modules":[{
        "name":"下一步工作计划",
        "content":"下一步工作计划77777777"
    }]
}
```

https://oapi.tita.com/api/{tenant_id}/daily/updatePostContent-Type	application/json请求Body

| 参数名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| tenant_id | int | 是 | 租户标识 |
| account_type | int | 是 | 账号类型 （0:手机号或邮箱 1：企业微信账号 2：钉钉账号） |
| account_name | string | 是 | 创建人账号（根据account_type不同进行赋值） |
| summary_type | int | 是 | 总结类型,默认是全部 （8：日报 26：周报 27：月报） |
| summary_date | string | 是 | 总结日期① |
| modules | List<Module> | 是 | 组件内容 |
| name | string | 是 | 组件名称 |
| content | string | 是 | 组件内容 |

请求示例

```
{
    "account_name":"",
    "summary_type":"8",
    "summary_date":"2025/10/7",
    "modules":[{
        "name":"下一步工作计划",
        "content":"下一步工作计划77777777"
    }]
}
```

https://oapi.tita.com/api/{tenant_id}/daily/searchGet请求参数

| 参数名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| tenant_id | int | 是 | 租户标识 |
| page_num | int | 是 | 页码 |
| page_size | int | 是 | 单页数量 |
| daily_type | int | 否 | 总结类型,默认是全部 （8：日报 26：周报 27：月报） |
| start_date | string | 是 | 开始时间 |
| end_date | string | 是 | 截止时间 |
| date_type | int | 是 | 查询的时间类型（0：总结周期时间  1：总结创建时间） |
| is_content | bool | 否 | 是否包括总结内容 |

返回结果示例

```
{
    "code": 0,
    "errorMsg": null,
    "data": {
        "total": 3,
        "dailys": [
            {
                "daily_name": "2020年11月18日日报（星期三）",
                "daily_id": 0,
                "daily_date": "2020/11/18",
                "submit_type": 1,
                "smmary": null,
                "work_plan": null,
                "submit_date": "2020/11/18 18:31:54",
                "daily_type": 8,
                "create_user": {
                    "userId": ,
                    "name": "",
                    "email": "",
                    "mobile": "",
                    "wx_userId": "",
                    "departmentName": "技术部"
                }
            }
        ]
    }
}
```

返回结果说明

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| code | int | 状态码 |
| message | string | 错误信息 |
| data | PlanDailyListModel | 总结集合 |

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| total | int | 数量 |
| dailys | List<PlanDailyModel> | 总结列表 |

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| daily_id | int | Id |
| daily_name | string | 名称 |
| create_user | UserModel | 创建人 |
| submit_date | string | 总结提交时间 |
| daily_date | string① | 总结所属日期（例如  日报：2020/11/18  周报：2020/11/1  月报：2020/11/01） |
| daily_type | int | 总结类型 （8：日报 26：周报 27：月报） |
| smmary | string | 总结内容 |
| work_plan | string | 下一步计划 |
| submit_type | int | 状态（1：按时提交 2：补交） |
| daily_text | List<PlanDailyTextModel> | 总结富文本内容 |

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| Name | string | 富文本名称 |
| Content | string | 富文本内容 |

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| userId | int | 人员Id |
| name | string | 人员名称 |
| email | string | 邮箱 |
| mobile | string | 手机号 |
| departmentName | string | 部门名称 |
| wx_userId | string | 企业微信ID |

https://oapi.tita.com/api/{tenant_id}/daily/search/idsGet请求参数

| 参数名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| tenant_id | int | 是 | 租户标识 |
| start_date | string | 是 | 开始时间 |
| end_date | string | 是 | 截止时间 |

```
{
    "code": 0,
    "errorMsg": null,
    "data": {
        "total": 3,
        "ids": [1,2,3]
    }
}
```

返回结果说明

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| code | int | 状态码 |
| message | string | 错误信息 |
| data | PlanDailyIdListModel | Id集合 |

参数名称类型说明totalint数量

---

## 部门接口

创建部门返回结果：修改部门删除部门获取所有部门1.DepartmentModel2.UserModel<font color="#dd0000">注：开发文档内所有涉及编码处均已UTF-8形式编码！！！</font>https://oapi.tita.com/api/{tenant_id}/department/addPostContent-Type	application/json请求Body

```
{
    "name": "销售部",
    "code": "1",
    "order": 1,
    "parent_code": "1",
    "leader_accounts":["18976546654","17765431234"],
    "hrbp_accounts":["18976546654","17765431234"],
    "account_type":0,
}
```

参数说明

| 参数名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| tenant_id | int | 是 | 租户标识 |
| name | string | 是 | 部门名称 |
| code | string | 是 | 部门编码(企业内唯一) |
| order | int | 否 | 排序 |
| parent_code | string | 否 | 父部门编码 |
| leader_accounts | List<string> | 否 | 部门负责人账号列表(邮箱/手机号/企业微信账号/工号) |
| hrbp_accounts | List<string> | 否 | 部门HRBP账号列表(邮箱/手机号/企业微信账号/工号) |
| account_type | int | 否 | 部门负责人账号类型（默认0.手机号或邮箱，1.企业微信账号，4.工号） |

```
{
    "code": 0,
    "errorMsg": null,
}
```

参数说明

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| code | int | 状态码 (0:成功) |
| message | string | 错误信息 |

https://oapi.tita.com/api/{tenant_id}/department/updatePostContent-Type  application/json请求Body

```
{
    "name": "销售部",
    "code": "1",
    "order": 1,
    "parent_code": "1",
    "leader_accounts":["18976546654","17765431234"],
    "hrbp_accounts":["18976546654","17765431234"],
    "account_type":0,
}
```

参数说明

| 参数名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| tenant_id | int | 是 | 租户标识 |
| name | string | 是 | 部门名称 |
| code | string | 是 | 部门编码 |
| order | int | 否 | 排序 |
| parent_code | string | 否 | 父部门编码 |
| leader_accounts | List<string> | 否 | 部门负责人账号列表(邮箱/手机号/企业微信账号/工号) |
| hrbp_accounts | List<string> | 否 | 部门HRBP账号列表(邮箱/手机号/企业微信账号/工号) |
| account_type | int | 否 | 部门负责人账号类型（默认0.手机号或邮箱，1.企业微信账号，4.工号） |

返回结果

```
{
    "code": 0,
    "errorMsg": null,
}
```

参数说明

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| code | int | 状态码 (0:成功) |
| message | string | 错误信息 |

https://oapi.tita.com/api/{tenant_id}/department/delete?code=PostContent-Type  application/json参数说明

| 参数名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| tenant_id | int | 是 | 租户标识 |
| code | string | 是 | 部门编码 |

返回结果示例

```
{
    "code": 0,
    "errorMsg": null,
}
```

返回结果说明

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| code | int | 状态码 (0:成功) |
| message | string | 错误信息 |

https://oapi.tita.com/api/{tenant_id}/department/get/allGetContent-Type  application/json返回结果示例

```
{
    "code": 0,
    "errorMsg": null,
    "data": [{
            "id": 1,
            "name": "销售部",
            "code": "1",
            "parent_id": 0,
            "order": 1,
            "leader_users": [
                        {
                    "userId": 200149381,
                    "name": "",
                    "email": "",
                    "mobile": "",
                    "wx_userId": "",
                    "departmentName": "技术部"
                    }
            ],
            "hrbp_users": [
                        {
                    "userId": 200149381,
                    "name": "",
                    "email": "",
                    "mobile": "",
                    "wx_userId": "",
                    "departmentName": "技术部"
                    }
            ],

        }]
}
```

返回结果说明

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| code | int | 状态码 (0:成功) |
| message | string | 错误信息 |
| data | DepartmentModel | 部门集合 |

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| id | int | 部门Id |
| name | string | 部门名称 |
| code | string | 部门编码 |
| parent_id | int | 父部门 |
| order | int | 排序 |
| leader_users | List<UserModel> | 部门负责人 |
| hrbp_users | List<UserModel> | 部门HRBP |

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| userId | int | 人员Id |
| name | string | 人员名称 |
| email | string | 邮箱 |
| mobile | string | 手机号 |
| departmentName | string | 部门名称 |
| wx_userId | string | 企业微信ID |

---

## 群组接口

创建群组添加群组下人员删除群组删除群组下人员获取租户所有群组2.GroupInfoModel3.GroupModel4.GroupUserModel获取群组下人员2.GroupUserModel<font color="#dd0000">注：开发文档内所有涉及编码处均已UTF-8形式编码！！！</font>https://oapi.tita.com/api/{tenant_id}/group/addPostContent-Type	application/json请求Body

```
{
     "name": "群组1",
     "visiblity": 1,
     "level": 1,
     "user_accounts":  ["18373773171","18373773172"],
     "department_codes": ["Tita-D3-01","Tita-D3-02"],
     "group_ids":["1122","2244"],
     "account_name":"18373773171",
     "account_type": 0,
}
```

| 参数名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| name | string | 是 | 群组名称 |
| tenant_id | int | 是 | 租户ID |
| visiblity | int | 否 | 群组可见范围（默认0全部人员，1.指定人员，部门或群组） |
| level | int | 否 | 维度级别（默认0租户级，1.用户级） |
| account_name | string | 是 | 创建人（手机号、邮箱、企业微信、工号） |
| user_accounts | List<string> | 否 | 可见范围人员（手机号、邮箱、企业微信、工号） |
| department_codes | List<string> | 否 | 可见范围部门编码 |
| group_ids | List<int> | 否 | 可见范围群组ID |
| account_type | int | 否 | 人员账号类型（默认0.手机号或邮箱 1.企业微信账号 2.钉钉账号 4.员工工号） |

返回结果示例

```
{
       "code": 0,
    "errorMsg": null,
    "data": {
        "objData": "2618"
    }
}
```

返回结果说明

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| code | int | 状态码 |
| message | string | 错误信息 |
| data.objData | int | 群组Id |

https://oapi.tita.com/api/{tenant_id}/group/addusersPostContent-Type	application/json请求Body

```
{
     "group_id":2603,
      "users_account":  ["18373773171","18373773172"],
     "department_codes": ["Tita-D3-01","Tita-D3-02"],
     "group_ids":["1122","2244"],
     "account_name":"18373773171",
     "account_type": 0,
}
```

| 参数名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| group_id | int | 是 | 群组ID |
| tenant_id | int | 是 | 租户ID |
| account_name | string | 是 | 操作人（手机号、邮箱、企业微信、工号） |
| users_account | List<string> | 否 | 被添加人员（手机号、邮箱、企业微信、工号） |
| department_codes | List<string> | 否 | 添加部门下人员 |
| group_ids | List<int> | 否 | 添加群组下人员 |
| account_type | int | 否 | 人员账号类型（默认0.手机号或邮箱 1.企业微信账号 2.钉钉账号 4.员工工号） |

返回结果示例

```
{
       "code": 0,
    "errorMsg": null,
}
```

返回结果说明

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| code | int | 状态码 |
| message | string | 错误信息 |

https://oapi.tita.com/api/{tenant_id}/group/deletePost请求参数

| 参数名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| tenant_id | int | 是 | 租户ID |
| group_id | int | 是 | 群组ID |

返回结果示例

```
{
       "code": 0,
    "errorMsg": null,
}
```

返回结果说明

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| code | int | 状态码 |
| message | string | 错误信息 |

https://oapi.tita.com/api/{tenant_id}/group/delete/usersPostContent-Type	application/json请求Body

```
{
     "group_id":2603,
    "user_accounts":  ["18373773171","18373773172"],
     "account_name":"18373773171",
     "account_type": 0,
}
```

| 参数名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| group_id | int | 是 | 群组ID |
| tenant_id | int | 是 | 租户ID |
| account_name | string | 是 | 操作人（手机号、邮箱、企业微信、工号） |
| users_account | List<string> | 否 | 被删除人员（手机号、邮箱、企业微信、工号） |
| account_type | int | 否 | 人员账号类型（默认0.手机号或邮箱 1.企业微信账号 2.钉钉账号 4.员工工号） |

返回结果示例

```
{
       "code": 0,
    "errorMsg": null,
}
```

返回结果说明

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| code | int | 状态码 |
| message | string | 错误信息 |

https://oapi.tita.com/api/{tenant_id}/group/searchGet请求参数

| 参数名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| tenant_id | int | 是 | 租户ID |

返回结果示例

```
{
    "code": 0,
    "errorMsg": null,
    "data": {
        "total": 2,
        "groups": [
            {
                "id": 3107,
                "name": "群组测试",
                "create_date": "2023-04-06T13:43:23.553",
                "create_user": {
                    "userId": 600003154,
                    "name": "米花",
                    "email": "1807777@tita.com",
                    "mobile": "15622846831",
                    "wx_userId": null,
                    "departmentName": "默认部门",
                    "groupId": 3107,
                    "groupName": "群组测试",
                    "staff_code": "tita_0003"
                }
            },
            {
                "id": 3111,
                "name": "测试群组2",
                "create_date": "2023-04-11T19:36:55.893",
                "create_user": {
                    "userId": 600003154,
                    "name": "米花",
                    "email": "1807777@tita.com",
                    "mobile": "15622846831",
                    "wx_userId": null,
                    "departmentName": "默认部门",
                    "groupId": 3111,
                    "groupName": "测试群组2",
                    "staff_code": "tita_0003"
                }
            }
        ]
    }
}
```

返回结果说明

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| code | int | 状态码 |
| message | string | 错误信息 |
| data | GroupInfoModel | 群组集合 |

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| total | int | 群组条数 |
| groups | List<GroupModel> | 群组列表 |

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| id | int | 群组ID |
| name | string | 群组名称 |
| create_date | string | 创建时间 |
| create_user | GroupUserModel | 创建人信息 |

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| userId | int | 人员ID |
| name | string | 人员名称 |
| email | string | 邮箱 |
| mobile | string | 手机号 |
| wx_userId | string | 企业微信ID |
| departmentName | string | 所属部门名称 |
| groupId | int | 所属群组ID |
| groupName | string | 所属群组名称 |
| staff_code | string | 员工工号 |

https://oapi.tita.com/api/{tenant_id}/group/search/userGet请求参数

| 参数名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| tenant_id | int | 是 | 租户ID |
| group_id | int | 是 | 群组ID |

返回结果示例

```
{
    "code": 0,
    "errorMsg": null,
    "data": {
        
        {
    "code": 0,
    "errorMsg": null,
    "data": [
        {
            "userId": 600003165,
            "name": "鲍勃",
            "email": "baobo@tita.com",
            "mobile": "18373778392",
            "wx_userId": null,
            "departmentName": "默认部门",
            "groupId": 3107,
            "groupName": "群组测试",
            "staff_code": "tita_0002"
        },
        {
            "userId": 600003154,
            "name": "米花",
            "email": "1807777@tita.com",
            "mobile": "15622846831",
            "wx_userId": null,
            "departmentName": "默认部门",
            "groupId": 3107,
            "groupName": "群组测试",
            "staff_code": "tita_0003"
        }
    ]
    }
    }
}
```

返回结果说明

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| code | int | 状态码 |
| message | string | 错误信息 |
| data | List<GroupUserModel> | 人员集合 |

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| userId | int | 人员ID |
| name | string | 人员名称 |
| email | string | 邮箱 |
| mobile | string | 手机号 |
| wx_userId | string | 企业微信ID |
| departmentName | string | 所属部门名称 |
| groupId | int | 所属群组ID |
| groupName | string | 所属群组名称 |
| staff_code | string | 员工工号 |

---

## KPI接口

添加KPI进展https://oapi.tita.com/api/{tenant_id}/kpi/progress/updatePostContent-Type	application/json请求Body

```
{
	"plan_name": "目标计划名称",
	"kpi_name": "KPI目标名称",
	"account_name": "18373773171",
	"account_type": 0,
	"achievevalue": 90,
	"estimate_achievevalue": 100,
	"progress_description": "目标进展描述"
}
```

参数说明

| 参数名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| tenant_id | int | 是 | 租户标识 |
| plan_name | string | 否 | 目标计划名称 |
| kpi_name | string | 是 | KPI目标名称 |
| account_type | int | 是 | 目标负责人账号类型 （0:手机号或邮箱 1：企业微信账号 2：钉钉账号） |
| account_name | string | 是 | 目标负责人账号（根据account_type不同进行赋值） |
| achievevalue | int | 否 | 完成值 |
| estimate_achievevalue | int | 否 | 预估完成值 |
| progress_description | string | 否 | 进展描述 |

返回结果示例

```
{
    "code": 0,
    "errorMsg": null,
    "data": null
}
```

返回结果说明

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| code | int | 状态码 (0:成功) |
| message | string | 错误信息 |

变更员工目标量化值https://oapi.tita.com/api/{tenant_id}/kpi/target/quantifyvalue/updatePostContent-Type	application/json请求Body

```
{
	"kpi_name": "KPI目标名称",
	"account_name": "18373773171",
	"account_type": 0,
	"achievevalue": 90,
	"data_time": "2023-09-06"
}
```

参数说明

| 参数名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| tenant_id | int | 是 | 租户标识 |
| kpi_name | string | 是 | KPI目标名称（支持模糊查询） |
| account_type | int | 是 | 目标负责人账号类型 （0:手机号或邮箱 1：企业微信账号 2：钉钉账号） |
| account_name | string | 是 | 目标负责人账号（根据account_type不同进行赋值） |
| achievevalue | decimal | 是 | 完成值 |
| data_time | int | 是 | 数据操作时间 |
| add_type | int | 否 | 数据操作类型（0累加 1覆盖 默认累加） |

返回结果示例

```
{
    "code": 0,
    "errorMsg": null,
    "data": null
}
```

返回结果说明

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| code | int | 状态码 (0:成功) |
| message | string | 错误/成功信息 |

---

## 消息/待办接口

按时间获取待办https://oapi.tita.com/api/v1/{tenantId}/todo/get说明：获取待办列表Method Post请求参数

| 参数名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| tenantId | int | 是 | 租户标识 |
| status | int | 否 | 状态（1：未读 2：已读 默认全部0） |
| page_num | int | 是 | 页码 |
| page_size | int | 是 | 每页数量 单页最大数据100条 |
| begin_time | long | 是 | 开始时间(毫秒时间戳) |
| last_time | long | 是 | 结束时间(毫秒时间戳) |

返回值

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| total | int | 数量 |
| messages | List | 消息(Todo对象)集合 |

Todo对象

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| fromUser | UserInfo | 消息发送人 |
| title | string | 消息标题 |
| SubTitle | string | 消息子标题 |
| content | string | 消息内容(含富文本) |
| objUrl | string | 地址 |
| todo_id | string | 待办标识 |
| createDate | string | 创建时间 |

UserInfo

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| userId | int | 人员Id |
| name | string | 人员名称 |
| email | string | 邮箱 |
| mobile | string | 手机号 |
| departmentName | string | 部门名称 |
| wx_userId | string | 企业微信ID |

按时间获取消息https://oapi.tita.com/api/v1/{tenantId}/message/get说明：获取消息列表Method Post请求参数

| 参数名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| tenantId | int | 是 | 租户标识 |
| status | int | 是 | 状态（1：未读 2：已读 默认全部0） |
| page_num | int | 是 | 页码 |
| page_size | int | 是 | 每页数量 单页最大数据100条 |
| begin_time | long | 是 | 开始时间(毫秒时间戳) |
| last_time | long | 是 | 结束时间(毫秒时间戳) |

返回值

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| total | int | 数量 |
| messages | List | 消息(Message对象)集合 |

Message对象

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| fromUser | UserInfo | 消息发送人 |
| title | string | 消息标题 |
| content | string | 消息内容(含富文本) |
| url | string | 地址 |
| messageId | string | 消息标识 |
| createDate | string | 创建时间 |

UserInfo

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| userId | int | 人员Id |
| name | string | 人员名称 |
| email | string | 邮箱 |
| mobile | string | 手机号 |
| departmentName | string | 部门名称 |
| wx_userId | string | 企业微信ID |

---

## 项目里程碑接口

创建项目里程碑https://oapi.tita.com/api/{tenant_id}/milestone/addPostContent-Type	application/json请求Body

```
{
     "name": "里程碑1",
     "work_id": 93056,
     "account_type": 0,
     "account_name": "18373773171",
     "principal_account": "18373773171",
     "start_date": "2024-11-22",
     "end_date": "2024-11-30",
     "description": "描述",
     "relation_id": "111",
}
```

参数说明

| 参数名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| tenant_id | int | 是 | 租户标识 |
| name | string | 是 | 里程碑名称 |
| work_id | int | 是 | 里程碑归属项目ID |
| relation_id | string | 否 | 第三方ID（而可以通过该值查询或更新） |
| account_type | int | 是 | 账号类型 （0:手机号或邮箱 1：企业微信账号 2：钉钉账号） |
| account_name | string | 是 | 创建人账号（根据account_type不同进行赋值） |
| principal_account | string | 是 | 负责人账号（根据account_type不同进行赋值） |
| start_date | string | 是 | 开始时间 |
| end_date | string | 是 | 截止时间 |
| description | string | 否 | 描述 |

返回结果示例

```
{
    "code": 0,
    "errorMsg": null,
    "data": {
        "objData": 2458588
    }
}
```

返回结果说明

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| code | int | 状态码 |
| message | string | 错误信息 |
| data | string | 里程碑标识 |

修改里程碑https://oapi.tita.com/api/{tenant_id}/milestone/updatePostContent-Type  application/json请求Body

```
{
     "name": "里程碑1",
     "id": 30012,
     "relation_id": "111",
     "account_type": 0,
     "account_name": "18373773171",
     "principal_account": "18373773171",
     "start_date": "2024-11-22",
     "end_date": "2024-11-30",
     "description": "描述",
}
```

参数说明

| 参数名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| tenant_id | int | 是 | 租户标识 |
| name | string | 是 | 里程碑名称 |
| id | int | 是 | 里程碑ID(优先通过第三方ID，其次里程碑ID，默认0) |
| relation_id | string | 否 | 第三方ID（可以通过该值查询或更新） |
| account_type | int | 是 | 账号类型 （0:手机号或邮箱 1：企业微信账号 2：钉钉账号） |
| account_name | string | 是 | 创建人账号（根据account_type不同进行赋值） |
| principal_account | string | 是 | 负责人账号（根据account_type不同进行赋值） |
| start_date | string | 是 | 开始时间 |
| end_date | string | 是 | 截止时间 |
| description | string | 否 | 描述 |

返回结果示例

```
{
    "code": 0,
    "errorMsg": null,
}
```

返回结果说明

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| code | int | 状态码 |
| message | string | 错误信息 |

删除里程碑https://oapi.tita.com/api/{tenant_id}/milestone/deletePostContent-Type  application/json请求Body

```
{
     "id": 30012,
     "relation_id": "111",
     "account_type": 0,
     "account_name": "18373773171"
}
```

参数说明

| 参数名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| tenant_id | int | 是 | 租户标识 |
| id | int | 是 | 里程碑ID(优先通过第三方ID，其次里程碑ID，默认0) |
| relation_id | string | 否 | 第三方ID（可以通过该值查询或更新） |
| account_type | int | 是 | 账号类型 （0:手机号或邮箱 1：企业微信账号 2：钉钉账号） |
| account_name | string | 是 | 创建人账号（根据account_type不同进行赋值） |

返回结果示例

```
{
    "code": 0,
    "errorMsg": null
}
```

返回结果说明

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| code | int | 状态码 |
| message | string | 错误信息 |

获取项目里程碑https://oapi.tita.com/api/{tenant_id}/milestone/searchPostContent-Type  application/json请求Body

```
{
     "work_id": 93056,
     "relation_id":"111"
}
```

| 参数名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| tenant_id | int | 是 | 租户标识 |
| work_id | int | 是 | 里程碑归属项目id |
| relation_id | string | 否 | 第三方ID（而可以通过该值查询或更新） |

返回结果示例

```
{
    "code": 0,
    "errorMsg": null,
    "data": {
        "total": 1,
        "milestones": [
            {
                "id": 30012,
                "name": "里程碑1",
                "work_id": 93056,
                "relation_id": "111",
                "status": 0,
                "description": "描述",
                "start_date": "2024/11/20",
                "end_date": "2024/11/30",
                "create_date": "2024/11/27",
                "visibility": 0,
                "create_user": null,
                "principal_user": {
                    "userId": 100011113,
                    "name": "用户name",
                    "email": "l@tita.com",
                    "mobile": "18373773171",
                    "wx_userId": "",
                    "departmentName": "测试部门",
                    "staff_code": "Tita0001"
                },
                "participators": null,
            }
        ]
    }
}
```

返回结果说明

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| code | int | 状态码 |
| message | string | 错误信息 |
| data | MilestoneListModel | 项目的里程碑集合 |

2.MilestoneListModel

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| total | int | 项目条数 |
| milestones | List<MilestoneModel> | 里程碑列表 |

3.MilestoneModel

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| id | int | 里程碑ID |
| name | int | 里程碑名称 |
| work_id | int | 里程碑归属项目ID |
| relation_id | string | 第三方ID |
| principal_user | UserModel | 负责人 |
| start_date | string | 开始时间 |
| end_date | string | 截止时间 |
| status | int | 状态(1:进行中 2:完成) |
| description | string | 描述 |

4.UserModel

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| userId | int | 人员Id |
| name | string | 人员名称 |
| email | string | 邮箱 |
| mobile | string | 手机号 |
| departmentName | string | 部门名称 |
| wx_userId | string | 企业微信ID |

---

## OKR接口

创建目标创建关键成果QuantifyValue添加关键成果进展获取指定时间段内创建的目标① 默认值：false② 默认值：1（1、获取O创建时间在指定时间段内的数据，2、获取O更新时间在指定时间段内的数据，3、获取O开始时间在指定时间段内的数据）③注：如填了kr_ids或okr_ids其他字段非必填④注：date_type=0时start_date与end_date字段非必填④cycle_Type=2，yqm_Num=1 第一季度,yqm_Num=2 第二季度...④cycle_Type=3，yqm_Num=1 一月,yqm_Num=2 二月...④cycle_Type=4，yqm_Num=1 1-2双月,yqm_Num=2 3-4双月...④cycle_Type=5，yqm_Num=1 上半年,yqm_Num=2 下半年2.OkrListModel3.OkrModel4.KrModel5.ProgressModel6.RelationOkrModel7.UserModel8.RelationModel9.QuantifyValue获取指定时间段内创建的目标（可根据OKR负责人、部门编码进行筛选查询）① 默认值：false② 默认值：1（1、获取O创建时间在指定时间段内的数据，2、获取O更新时间在指定时间段内的数据，3、获取O开始时间在指定时间段内的数据）③注：如填了kr_ids或okr_ids其他字段非必填④注：date_type=0时start_date与end_date字段非必填④cycle_Type=2，yqm_Num=1 第一季度,yqm_Num=2 第二季度...④cycle_Type=3，yqm_Num=1 一月,yqm_Num=2 二月...④cycle_Type=4，yqm_Num=1 1-2双月,yqm_Num=2 3-4双月...④cycle_Type=5，yqm_Num=1 上半年,yqm_Num=2 下半年2.OkrListModel3.OkrModel4.KrModel5.ProgressModel6.RelationOkrModel7.UserModel8.RelationModel9.QuantifyValue获取OKR分类2.OkrLabelListModel3.OkrLabelModel上传附件<font color="#dd0000">注：开发文档内所有涉及编码处均已UTF-8形式编码！！！</font>https://oapi.tita.com/api/{tenant_id}/okr/addPostContent-Type	application/json请求Body

```
{
	 "name": "目标1",
	 "account_type": 0,
	 "account_name": "18373773171",
	 "principal_account": "18373773171",
	 "okr_type": 1,
	 "cycle_type": 2,
	 "cycle_num": 2,
	 "visibility": 1,
	 "start_date": "2020-01-01",
     "end_date": "2020-01-30",
     "description": "描述",
     "relation_id": "111",
}
```

参数说明

| 参数名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| tenant_id | int | 是 | 租户标识 |
| name | string | 是 | OKR名称 |
| account_type | int | 是 | 账号类型 （0:手机号或邮箱 1：企业微信账号 2：钉钉账号） |
| account_name | string | 是 | 创建人账号（根据account_type不同进行赋值） |
| principal_account | string | 是 | 负责人账号（根据account_type不同进行赋值） |
| okr_type | int | 否 | 目标类型(1：个人 2：部门 3：公司) |
| cycle_type | int | 否 | 周期类型(0:自定义 1：年度 2：季度 3：月度) |
| cycle_num | int | 否 | 具体的月份和季度 |
| participant_account | List<string> | 是 | 参与人（根据account_type不同进行赋值) |
| visibility | int | 是 | 是否私密(1:公开 2：私密) |
| start_date | string | 是 | 开始时间 |
| end_date | string | 是 | 截止时间 |
| description | string | 否 | 描述 |
| relation_id | string | 否 | 第三方ID（而可以通过该值查询或更新） |

返回结果示例

```
{
    "code": 0,
    "errorMsg": null,
    "data": {
        "objData": 2458586
    }
}
```

返回结果说明

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| code | int | 状态码 (0:成功) |
| message | string | 错误信息 |
| data.objData | string | 目标ID |

https://oapi.tita.com/api/{tenant_id}/kr/addPostContent-Type	application/json请求Body

```
{
	 "name": "目标1",
	 "account_type": 0,
	 "account_name": "18373773171",
	 "principal_account": "18373773171",
	 "okr_id": 1,
	 "start_date": "2020-01-01",
     "end_date": "2020-01-30",
     "description": "描述",

}
```

参数说明

| 参数名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| tenant_id | int | 是 | 租户标识 |
| name | string | 是 | OKR名称 |
| account_type | int | 是 | 账号类型 （0:手机号或邮箱 1：企业微信账号 2：钉钉账号） |
| account_name | string | 是 | 创建人账号（根据account_type不同进行赋值） |
| principal_account | string | 是 | 负责人账号（根据account_type不同进行赋值） |
| ork_id | int | 是 | 目标ID |
| start_date | string | 是 | 开始时间 |
| end_date | string | 是 | 截止时间 |
| description | string | 否 | 描述 |
| quantify_values | List<QuantifyValue> | 否 | 关键成果量化值 |

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| field_code | string | 字段编码（startValue 初始值;targetValue 目标值;achieveValue 完成值） |
| field_name | string | 字段名称 |
| field_value | decimal | 字段值 |

返回结果示例

```
{
    "code": 0,
    "errorMsg": null,
    "data": {
        "objData": 2458586
    }
}
```

返回结果说明

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| code | int | 状态码 (0:成功) |
| message | string | 错误信息 |
| data.objData | string | 关键成果ID |

https://oapi.tita.com/api/{tenant_id}/kr/progressDescription/addPostContent-Type  application/json请求Body

```
{
     "kr_id": "111111",
     "progress_description": "关键成果进展测试",
     "start_date": "进展的开始时间",
     "end_date": "进展的截止时间"
}
```

参数说明

| 参数名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| kr_id | string | 是 | 关键成果ID |
| progress_description | string | 是 | 进展内容 |
| start_date | date | 否 | 进展的开始时间 |
| end_date | date | 否 | 进展的截止时间 |
| achieve_value | decimal | 否 | 关键成果的完成值 |

返回结果示例

```
{
    "code": 0,
    "errorMsg": null
    "data": {
        "objData": "300284_6674544_7_20_637201520763717781"
    }
}
```

返回结果说明

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| code | int | 状态码 |
| message | string | 错误信息 |
| data.objData | string | 进展ID |

https://oapi.tita.com/api/{tenant_id}/okr/searchGet请求参数

| 参数名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| tenant_id | int | 是 | 租户标识 |
| page_num | int | 是 | 页码 |
| page_size | int | 是 | 单页数量 |
| start_date | string | 是 | 开始时间 |
| end_date | string | 是 | 截止时间 |
| fetch_kr | bool | 否① | 是否查询目标下的关键成果 |
| fetch_progress | bool | 否① | 是否查询目标下的进展 |
| fetch_krprogress | bool | 否① | 是否查询关键成果的进展 |
| date_type | int | 否② | 返回数据类型 |
| okr_ids | string | 否③ | OKRId（如有多个请用逗号分割） |
| kr_ids | string | 否③ | KRId（如有多个请用逗号分割） |
| cycle_Type | int | 否④ | 周期（0:自定义 1：年度 2：季度 3：月度 4:双月 5:半年度） |
| year_Num | int | 否④ | 年度 |
| yqm_Num | int | 否④ | 月份扩展 |
| fetch_relation | bool | 否 | 是否展示关联信息 |

返回结果示例

```
{
	"code": 0,
	"errorMsg": null,
	"data": {
		"total": 2,
		"okrs": [
			{
				"relation_id": "",
				"status": 1,
				"description": "",
				"start_date": "2020/10/01 00:00:00",
				"end_date": "2020/12/31 23:59:00",
				"create_date": "2020/11/09 18:55:14",
				"create_user": {
					"userId": 200149381,
					"name": "",
					"email": "",
					"mobile": "",
					"wx_userId": "",
					"departmentName": "技术部"
				},
				"principal_user": {
					"userId": 200149381,
					"name": "",
					"email": "",
					"mobile": "",
					"wx_userId": "",
					"departmentName": "技术部"
				},
				"participators": [],
				"okr_id": ,
				"okr_name": "测试目标",
				"progress": 0,
				"evaluate_score": 0.0,
				"okr_classify": 0,
				"okr_type": 1,
				"cycle_type": 2,
				"cycle_year": 2020,
				"cycle_num": 4,
				"cycle_name": "2020年4季度目标",
				"progressUpdateDate": "2020/11/09 18:55:14",
				"progress_grow": -110.0,
			    "risk_Level": 6，
			    "department_id": 0，
			    "okr_progress": [{
					"comment_Id": "",
					"content": "更新目标完成度为 123% ,进展：3123123",
					"create_date": "2022/03/04 20:22:44",
					"create_user": {
						"userId": 200149381,
						"name": "",
						"email": "",
						"mobile": "",
						"wx_userId": "",
						"departmentName": "技术部"
					},
					"progress_description": "3123123",
					"progress": "123"
				},
				{
					"comment_Id": "",
					"content": "更新目标完成度为 13%",
					"create_date": "2022/03/04 20:28:43",
					"create_user": {
						"userId": 200149381,
						"name": "",
						"email": "",
						"mobile": "",
						"wx_userId": "",
						"departmentName": "技术部"
					},
					"progress_description": "",
					"progress": "13"
				}
			],
				"krs": [
					{
						"kr_id": ,
						"kr_name": "",
						"confidenceIndex": 5,
						"progress": 0,
						"evaluate_score": 0.0,
						"start_date": "2020/10/01 00:00:00",
						"end_date": "2020/12/31 00:00:00",
						"principal_user": {
							"userId": "",
							"name": "",
							"email": "",
							"mobile": "",
							"wx_userId": "",
							"departmentName": "技术部"
						},
						"create_user": {
							"userId": ,
							"name": "",
							"email": "",
							"mobile": "",
							"wx_userId": "",
							"departmentName": "技术部"
						},
						"progress_grow": 19.00,
				        "risk_level": 2",
				        kr_progress": [{
					        "comment_Id": "",
					        "content": "新建了进展：fvcdsfasf",
					        "create_date": "2022/03/04 20:22:59",
					        "create_user": {
						        "userId": "",
						        "name": "",
						        "email": "",
						        "mobile": "",
						        "wx_userId": "",
						        "departmentName": "技术部"
					    },
					        "progress_description": "fvcdsfasf",
					        "progress": "19"
				}],
					}
				]
			}
		]
	}
}
```

返回结果说明

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| code | int | 状态码 |
| message | string | 错误信息 |
| data | OkrListModel | OKR集合 |

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| total | int | 目标条数 |
| okrs | List<OkrModel> | 目标列表 |

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| okr_id | int | 目标Id |
| okr_name | string | 目标名称 |
| label_id | int | 目标分类Id |
| label_name | string | 目标分类名称 |
| create_user | UserModel | 创建人 |
| principal_user | UserModel | 负责人 |
| participants | List<UserModel> | 参与人 |
| followers | List<UserModel> | 关注人 |
| progress | int | 进度 |
| okr_type | int | 目标类型(1：个人 2：部门 3：公司 4：团队) |
| department_id | int | 部门Id |
| department_name | int | 部门名称 |
| group_id | int | 团队Id |
| group_name | int | 团队名称 |
| cycle_type | int | 周期类型(0:自定义 1：年度 2：季度 3：月度) |
| cycle_num | int | 具体月份和季度 |
| cycle_year | int | 周期年份 |
| cycle_name | string | 周期全称（例如：2021年1季度目标） |
| start_date | string | 开始时间 |
| end_date | string | 截止时间 |
| progressUpdateDate | string | 更新进度时间 |
| status | int | 状态(1:进行中 2:完成) |
| evaluate_score | decimal | 评分 |
| description | string | 描述 |
| visibility | int | 是否私密(1:公开 2：私密) |
| department_id | int | 所属部门ID |
| okr_classify | int | 类别(1:承诺 2：愿景) |
| relation_id | string | 第三方Id |
| krs | List<KrModel> | 关键成果 |
| okr_progress | List<ProgressModel> | 进展 |
| progress_grow | decimal | 进度变化 |
| risk_level | string | OKR状态（2：有风险 3：已延期 6：正常） |
| parent_okr | List<RelationOkrModel> | 对齐的目标 |
| weight | string | OKR权重 |
| p_weight | string | 对齐OKR权重 |
| kr_pWeight | string | 对齐KR权重 |
| relation_models | List<RelationModel> | 关联信息 |

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| kr_id | int | 关键成果Id |
| okr_id | int | 目标Id |
| kr_name | string | 关键成果名称 |
| create_user | UserModel | 创建人 |
| principal_user | UserModel | 负责人 |
| progress | int | 进度 |
| confidenceIndex | int | 信心指数 |
| start_date | string | 开始时间 |
| end_date | string | 结束时间 |
| progressUpdateDate | string | 更新进度时间 |
| evaluate_score | decimal | 评分 |
| kr_progress | List<ProgressModel> | 进展 |
| progress_grow | decimal | 进度变化 |
| unit_name | string | 单位 |
| risk_Level | string | KR状态（2：有风险 3：已延期 6：正常） |
| quantify_values | List<QuantifyValue> | 量化值 |

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| progress_Id | string | 进展Id |
| create_user | UserModel | 创建人 |
| create_date | string | 创建时间 |
| content | string | 信息内容 |
| progress_description | string | 进展描述 |
| progress | string | 进度 |

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| okr_id | int | 对齐的目标Id |
| kr_id | int | 对齐的KrId |

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| userId | int | 人员Id |
| name | string | 人员名称 |
| email | string | 邮箱 |
| mobile | string | 手机号 |
| departmentName | string | 部门名称 |
| wx_userId | string | 企业微信ID |

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| relation_id | int | 关联对象id |
| object_type | int | 关联对象类型（4 项目 7 任务） |

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| quantifyField_name | string | 量化值名称 |
| quantifyField_code | string | 量化值编码 |
| value | decimal | 值 |

https://oapi.tita.com/api/{tenant_id}/okr/searchByUserPost请求参数

| 参数名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| tenant_id | int | 是 | 租户标识 |
| page_num | int | 是 | 页码 |
| page_size | int | 是 | 单页数量 |
| start_date | string | 是 | 开始时间 |
| end_date | string | 是 | 截止时间 |
| fetch_kr | bool | 否① | 是否查询目标下的关键成果 |
| fetch_progress | bool | 否① | 是否查询目标下的进展 |
| fetch_krprogress | bool | 否① | 是否查询关键成果的进展 |
| date_type | int | 否② | 返回数据类型 |
| account_type | int | 否 | 账号类型 （0:手机号或邮箱（默认为0） 1：企业微信账号 4:员工工号 5：TitaUserId） |
| accounts | List<string> | 否 | OKR负责人 |
| department_codes | List<string> | 否 | 部门编码 |
| status | int | 否 | 状态(1:进行中 2:完成) |
| risk_level | int | 否 | OKR状态（1：正常推进 2：有风险 3：已延期 4.完成 5.延期完成 6：正常） |
| okr_ids | string | 否③ | OKRId（如有多个请用逗号分割） |
| kr_ids | string | 否③ | KRId（如有多个请用逗号分割） |
| cycle_Type | int | 否④ | 周期（0:自定义 1：年度 2：季度 3：月度 4:双月 5:半年度） |
| year_Num | int | 否④ | 年度 |
| yqm_Num | int | 否④ | 月份扩展 |
| fetch_relation | bool | 否 | 是否展示关联信息 |

返回结果示例

```
{
	"code": 0,
	"errorMsg": null,
	"data": {
		"total": 2,
		"okrs": [
			{
				"relation_id": "",
				"status": 1,
				"description": "",
				"start_date": "2020/10/01 00:00:00",
				"end_date": "2020/12/31 23:59:00",
				"create_date": "2020/11/09 18:55:14",
				"create_user": {
					"userId": 200149381,
					"name": "",
					"email": "",
					"mobile": "",
					"wx_userId": "",
					"departmentName": "技术部"
				},
				"principal_user": {
					"userId": 200149381,
					"name": "",
					"email": "",
					"mobile": "",
					"wx_userId": "",
					"departmentName": "技术部"
				},
				"participators": [],
				"okr_id": ,
				"okr_name": "测试目标",
				"progress": 0,
				"evaluate_score": 0.0,
				"okr_classify": 0,
				"okr_type": 1,
				"cycle_type": 2,
				"cycle_year": 2020,
				"cycle_num": 4,
				"cycle_name": "2020年4季度目标",
				"progressUpdateDate": "2020/11/09 18:55:14",
				"progress_Grow": -110.0,
			    "risk_Level": 6，
			    "okr_progress": [{
					"comment_Id": "",
					"content": "更新目标完成度为 123% ,进展：3123123",
					"create_date": "2022/03/04 20:22:44",
					"create_user": {
						"userId": 200149381,
						"name": "",
						"email": "",
						"mobile": "",
						"wx_userId": "",
						"departmentName": "技术部"
					},
					"progress_description": "3123123",
					"progress": "123"
				},
				{
					"comment_Id": "",
					"content": "更新目标完成度为 13%",
					"create_date": "2022/03/04 20:28:43",
					"create_user": {
						"userId": 200149381,
						"name": "",
						"email": "",
						"mobile": "",
						"wx_userId": "",
						"departmentName": "技术部"
					},
					"progress_description": "",
					"progress": "13"
				}
			],
				"krs": [
					{
						"kr_id": ,
						"kr_name": "",
						"confidenceIndex": 5,
						"progress": 0,
						"evaluate_score": 0.0,
						"start_date": "2020/10/01 00:00:00",
						"end_date": "2020/12/31 00:00:00",
						"principal_user": {
							"userId": "",
							"name": "",
							"email": "",
							"mobile": "",
							"wx_userId": "",
							"departmentName": "技术部"
						},
						"create_user": {
							"userId": ,
							"name": "",
							"email": "",
							"mobile": "",
							"wx_userId": "",
							"departmentName": "技术部"
						},
						"progress_Grow": 19.00,
				        "risk_Level": 2",
				        kr_progress": [{
					        "comment_Id": "",
					        "content": "新建了进展：fvcdsfasf",
					        "create_date": "2022/03/04 20:22:59",
					        "create_user": {
						        "userId": "",
						        "name": "",
						        "email": "",
						        "mobile": "",
						        "wx_userId": "",
						        "departmentName": "技术部"
					    },
					        "progress_description": "fvcdsfasf",
					        "progress": "19"
				}],
					}
				]
			}
		]
	}
}
```

返回结果说明

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| code | int | 状态码 |
| message | string | 错误信息 |
| data | OkrListModel | OKR集合 |

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| total | int | 目标条数 |
| okrs | List<OkrModel> | 目标列表 |

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| okr_id | int | 目标Id |
| okr_name | string | 目标名称 |
| label_id | int | 目标分类Id |
| label_name | string | 目标分类名称 |
| create_user | UserModel | 创建人 |
| principal_user | UserModel | 负责人 |
| participants | List<UserModel> | 参与人 |
| followers | List<UserModel> | 关注人 |
| progress | int | 进度 |
| okr_type | int | 目标类型(1：个人 2：部门 3：公司 4：团队) |
| department_id | int | 部门Id |
| department_name | int | 部门名称 |
| group_id | int | 团队Id |
| group_name | int | 团队名称 |
| cycle_type | int | 周期类型(0:自定义 1：年度 2：季度 3：月度) |
| cycle_num | int | 具体月份和季度 |
| cycle_year | int | 周期年份 |
| cycle_name | string | 周期全称（例如：2021年1季度目标） |
| start_date | string | 开始时间 |
| end_date | string | 截止时间 |
| progressUpdateDate | string | 更新进度时间 |
| status | int | 状态(1:进行中 2:完成) |
| evaluate_score | decimal | 评分 |
| description | string | 描述 |
| visibility | int | 是否私密(1:公开 2：私密) |
| okr_classify | int | 类别(1:承诺 2：愿景) |
| relation_id | string | 第三方Id |
| krs | List<KrModel> | 关键成果 |
| okr_progress | List<ProgressModel> | 进展 |
| progress_Grow | decimal | 进度变化 |
| risk_Level | string | OKR状态（2：有风险 3：已延期 6：正常） |
| parent_okr | List<RelationOkrModel> | 对齐的目标 |
| weight | string | OKR权重 |
| p_weight | string | 对齐OKR权重 |
| kr_pWeight | string | 对齐KR权重 |
| relation_models | List<RelationModel> | 关联信息 |

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| kr_id | int | 关键成果Id |
| okr_id | int | 目标Id |
| kr_name | string | 关键成果名称 |
| create_user | UserModel | 创建人 |
| principal_user | UserModel | 负责人 |
| progress | int | 进度 |
| confidenceIndex | int | 信心指数 |
| start_date | string | 开始时间 |
| end_date | string | 结束时间 |
| progressUpdateDate | string | 更新进度时间 |
| evaluate_score | decimal | 评分 |
| kr_progress | List<ProgressModel> | 进展 |
| progress_Grow | decimal | 进度变化 |
| unit_name | string | 单位 |
| risk_Level | string | KR状态（2：有风险 3：已延期 6：正常） |
| quantify_values | List<QuantifyValue> | 量化值 |

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| progress_Id | string | 进展Id |
| create_user | UserModel | 创建人 |
| create_date | string | 创建时间 |
| content | string | 信息内容 |
| progress_description | string | 进展描述 |
| progress | string | 进度 |

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| okr_id | int | 对齐的目标Id |
| kr_id | int | 对齐的KrId |

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| userId | int | 人员Id |
| name | string | 人员名称 |
| email | string | 邮箱 |
| mobile | string | 手机号 |
| departmentName | string | 部门名称 |
| wx_userId | string | 企业微信ID |

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| relation_id | int | 关联对象id |
| object_type | int | 关联对象类型（4 项目 7 任务） |

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| quantifyField_name | string | 量化值名称 |
| quantifyField_code | string | 量化值编码 |
| value | decimal | 值 |

https://oapi.tita.com/api/{tenant_id}/okr/label/getGet参数说明

| 参数名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| tenant_id | int | 是 | 租户标识 |

返回结果示例

```
{
	"code": 0,
	"errorMsg": null,
	"data": {
		"lables": [{
			"name": "分类2",
			"id": 3624,
			"status": "启用"
		}, {
			"name": "分类三",
			"id": 3625,
			"status": "启用"
		}, {
			"name": "分类1",
			"id": 3623,
			"status": "停用"
		}],
		"total": 3
	}
}
```

返回结果说明

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| code | int | 状态码 (0:成功) |
| message | string | 错误信息 |
| data | OkrLabelListModel | 目标分类集合 |

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| total | int | 标签分类条数 |
| lables | List<OkrLabelModel> | 目标分类列表 |

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| id | int | 目标分类Id |
| name | string | 目标分类名称 |
| status | string | 停启用状态 |

https://oapi.tita.com/api/{tenant_id}/file/uploadGet参数说明

| 参数名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| tenant_id | int | 是 | 租户标识 |
| file_name | string | 是 | 文件名称 |
| content | byte[] | 是 | 文件二进制 |

返回结果示例

```
{
	"code": 0,
	"errorMsg": null,
	"data": {
		"objData": ""
	}
}

## 新建OKR互动

- https://oapi.tita.com/api/{tenant_id}/comment/save
- Get

- 参数说明

参数名称 | 类型 | 必填 | 说明
---|---|---|---
tenant_id | int| 是| 租户标识
okr_id | int | 是| OKR标识
content | string | 否| 互动内容
file_url | string | 否| 互动附件
account_name | string | 是| 创建人账号
account_type | int | 是| 创建人类型
- 返回结果示例
```

---

## API列表-PaaS

新增接口请求地址https://oapi.tita.com/general/api/paas/add?tenantId=?&accountType=?&deptType=?&appName=?&operatorUser=?请求url例子https://oapi.tita.com/general/api/paas/add?tenantId=10086&accountType=0&deptType=1&appName=test&operatorUser=13111111111请求方式POSTContent-TypeContent-Type application/json请求body

```
示例
[
  {
    "metaObjectCode": "Crm.Customer",
    "fields": [
      {
        "name": "PrincipalUserId",
        "value": "9638c0f3-5569-4230-a175-4562b8274c71@tita-weixin.com"
      },
      {
        "name": "Name",
        "value": "我是客户名称"
      },
      {
        "name": "Mobile",
        "value": "13112345678"
      }
    ]
  }
]
```

url地址中参数说明：

| 名称 | 类型 | 说明 | 必填 |
| --- | --- | --- | --- |
| tenantId | int | 租户id | 是 |
| accountType | int | 用户id类型（0:手机号或邮箱或姓名） | 是 |
| deptType | int | 部门id类型（0:使用tita系统部门编码  1：使用三方corpid） | 是 |
| operatorUser | string | 操作人(手机号或邮箱或姓名) | 是 |
| appName | string | 应用名称（参考页面底部说明，根据真实业务填写） | 是 |

请求body参数说明：

| 名称 | 类型 | 说明 | 必填 |
| --- | --- | --- | --- |
| metaObjectCode | string | 对象编码（参考页面底部说明，根据真实业务填写） | 是 |
| fields | 数组 | 参数集合 | 是 |

返回结果示例

```
{
    "code": 0,
    "data": db77ba6e-393e-4bcc-94df-657e8264f6d3,
    "errorMsg": "操作成功"

}
```

返回结果说明：

| 返回值 | 类型 | 说明 |
| --- | --- | --- |
| code | int | 状态码（0成功，其他值表示异常） |
| errorMsg | string | 错误信息 |

修改接口请求地址https://oapi.tita.com/general/api/paas/modify?tenantId=?&accountType=?&deptType=?&appName=?&operatorUser=?请求url例子https://oapi.tita.com/general/api/paas/modify?tenantId=10086&accountType=0&deptType=1&appName=test&operatorUser=13111111111请求方式POSTContent-TypeContent-Type application/json请求body

```
[
  {
    "metaObjectCode": "Crm.Customer",
    "id": "0a0f27f8-ab0e-4a63-a4d5-27c90fc6da47",
    "fields": [
      {
        "name": "PrincipalUserId",
        "value": "9638c0f3-5569-4230-a175-4562b8274c71@tita-weixin.com"
      },
      {
        "name": "Name",
        "value": "客户名称"
      },
      {
        "name": "Mobile",
        "value": "13112345678"
      }
    ]
  }
]
```

url地址中参数说明：

| 名称 | 类型 | 说明 | 必填 |
| --- | --- | --- | --- |
| tenantId | int | 租户id | 是 |
| accountType | int | 用户id类型（0:手机号或邮箱或姓名） | 是 |
| deptType | int | 部门id类型（0:使用tita系统部门编码  1：使用三方corpid） | 是 |
| operatorUser | string | 操作人(手机号或邮箱或姓名) | 是 |
| appName | string | 应用名称 | 是 |

请求body参数说明：

| 名称 | 类型 | 说明 | 必填 |
| --- | --- | --- | --- |
| metaObjectCode | string | 对象编码 | 是 |
| id | string | 此记录在tita系统中主键id，调用新增接口的时候会返回此id，也可通过查询接口获取 | 是 |
| fields | 数组 | 参数集合 | 是 |

返回结果示例

```
{
    "code": 0,
    "data": null,
    "errorMsg": "操作成功"

}
```

返回结果说明：

| 返回值 | 类型 | 说明 |
| --- | --- | --- |
| code | int | 状态码（0成功，其他值表示异常） |
| errorMsg | string | 错误信息 |

删除接口请求地址https://oapi.tita.com/general/api/paas/{tenantId}/delete请求url例子https://oapi.tita.com/general/api/paas/10086/delete请求方式POSTContent-TypeContent-Type application/json请求body

```
{
    "id": "c58441d8-4456-4980-b99c-f059ac34e30a",
    "metaObjectCode": "Crm.Customer",
  }
```

请求body参数说明：

| 名称 | 类型 | 说明 | 必填 |
| --- | --- | --- | --- |
| metaObjectCode | string | 对象编码 | 是 |
| id | string | 调用新增接口的时候会返回此id，也可通过查询接口获取 | 是 |

返回结果示例

```
{
    "code": 0,
    "data": null,
    "errorMsg": "操作成功"

}
```

返回结果说明：

| 返回值 | 类型 | 说明 |
| --- | --- | --- |
| code | int | 状态码（0成功，其他值表示异常） |
| errorMsg | string | 错误信息 |

查询接口请求地址https://oapi.tita.com/general/api/paas/{tenantId}/search请求url例子https://oapi.tita.com/general/api/paas/10086/search请求方式POSTContent-TypeContent-Type application/json请求body

```
{
  "pageNum":1,
  "pageSize":10,
  "items": [
    {
      "name": "name",
      "value": "张三",
      "conditionType": 1,
      "operatorType": 12
    }
  ],
  "metaObjectCode":"Crm.Customer"
}
```

请求body参数说明：

| 名称 | 类型 | 说明 | 必填 |
| --- | --- | --- | --- |
| pageNum | int | 第几页 | 是 |
| pageSize | int | 每页几条数据 | 是 |
| name | string | 字段名称 | 否 |
| items | object | 条件列表 | 否 |
| value | string | 字段具体值 | 否 |
| operatorType | int | 1等于 2大于等于、3小于等于、4大于、5小于、6范围、7为空、8不为空、9不等于、10开头等于、11结尾等于、12包含、14模糊 | 否 |
| conditionType | int | 1且  2或 | 否 |
| metaObjectCode | string | 对象编码 | 是 |

返回结果示例

```
{
    "code": 0,
    "data": [
        {
            "fields": [
                {
                    "name": "AllocationTime",
                    "value": "2024/07/10 16:48:20"
                },
                {
                    "name": "BusinessCount",
                    "value": "0"
                },
                {
                    "name": "CreatedBy",
                    "value": "600108074"
                },
                {
                    "name": "CreatedTime",
                    "value": "2024/07/10 16:43:59"
                },
                {
                    "name": "CustomerSource",
                    "value": "2"
                },
                {
                    "name": "EmployeeTotal",
                    "value": "2"
                },
                {
                    "name": "FeedId",
                    "value": "600201_4918_36_8_638562266390000000"
                },
                {
                    "name": "ImportanceNew",
                    "value": "4"
                },
                {
                    "name": "Industry",
                    "value": "5"
                },
                {
                    "name": "IsDelete",
                    "value": "False"
                },
                {
                    "name": "IsOpenPool",
                    "value": "True"
                },
                {
                    "name": "ModifiedBy",
                    "value": "10000"
                },
                {
                    "name": "ModifiedTime",
                    "value": "2024/07/11 18:12:12"
                },
                {
                    "name": "Name",
                    "value": "客户A00000001"
                },
                {
                    "name": "OldPrincipalUserId",
                    "value": "600108074"
                },
                {
                    "name": "Owner",
                    "value": "600108074"
                },
                {
                    "name": "PoolId",
                    "value": "8fd1140b-9d3d-4ddc-988a-0158bd30bb9c"
                },
                {
                    "name": "PutPoolTime",
                    "value": "2024/07/11 15:10:39"
                },
                {
                    "name": "Region",
                    "value": "12"
                },
                {
                    "name": "Stage",
                    "value": "3"
                },
                {
                    "name": "Status",
                    "value": "3"
                },
                {
                    "name": "id",
                    "value": "db77ba6e-393e-4bcc-94df-657e8264f6d3"
                }
            ]
        }
    ],
    "errorMsg": "操作成功"
}
```

返回结果说明：

| 返回值 | 类型 | 说明 |
| --- | --- | --- |
| code | int | 状态码（0成功，其他值表示异常） |
| errorMsg | string | 错误信息 |

应用名称（根据具体业务持续更新）参数说明：

| 应用名称 | 说明 |
| --- | --- |
| Test | 测试应用 |

对象列表(根据具体业务持续更新)用户对象编码：Test.User字段参数说明：

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| Name | string | 名称 |

部门对象编码：Test.Department字段参数说明：

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| Name | string | 名称 |

---

## 绩效接口

获取指定时间段内绩效考核列表2.AssessFormListModel3.AssessFormModel4.NodeModel5.UserModel获取指定绩效表单评价详情返回结果：1.AssessFormEvaluationModel 表单2.AssessModuleModel 维度3.AssessItemModel 指标4.AssessFormEvaluationTotalModel 总评4.1.AssessEvaluateContentModel 总评5.AssessAppealRecordModel  申诉6.AssessSubjectAppealRecordList  主题申诉列表7.AssessSubjectResultModel  多主题评价结果列表考核活动列表查询返回结果：1.activity活动考核结果列表查询返回结果：1.AssessForm考核表单<font color="#dd0000">注：开发文档内所有涉及编码处均已UTF-8形式编码！！！</font>https://oapi.tita.com/api/{tenant_id}/performance/searchGet请求参数

| 参数名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| tenant_id | int | 是 | 租户标识 |
| page_num | int | 是 | 页码 |
| page_size | int | 是 | 单页数量 |
| start_date | string | 是 | 开始时间 |
| end_date | string | 是 | 截止时间 |

返回结果示例

```
{
    "code": 0,
    "errorMsg": null,
    "data": {
        "total": 19,
        "assess_forms": [{
            "user": {
                "userId": 123,
                "name": "Kidd",
                "email": "zyn@163.com",
                "mobile": "155123234324",
                "wx_userId": "",
                "departmentName": "技术部",
                "staff_code": ""
            },
            "name": "fffff",
            "assess_formId": "33947719-79a2-41f4-b288-03004afc4bd3",
            "assess_templateId": "8fdd19a2-3928-4155-be30-fb6d078470be",
            "assess_template_name": "23年主题权限测试模板",
            "assess_template_category": 192,
            "assess_template_category_name": "2023模板",
            "assess_activityId": "77c1119f-b6a3-45aa-a595-46277f0c52ee",
            "current_nodeName": "员工自评",
            "start_date": "2021/01/01",
            "create_date": "2/8/2021 1:10:49 PM",
            "end_date": "2021/03/31",
            "score": 0.00,
            "rank": "",
            "is_End": false,
            "cycle_type": 1,
            "cycle_name": "2023年 年度",
            "cycle_year": 2023,
            "cycle_month": 0，
            "nodes": [{
                "name": "员工自评",
                "status": 2,
                "weight": 0.0,
                "node_type": 1,
                "users": [{
                    "userId": 200362069,
                    "name": "Kidd",
                    "email": "zyn0401@163.com",
                    "mobile": "15510102651",
                    "wx_userId": "",
                    "departmentName": "技术部"
                }]
            },
            {
                "process_id": "fc5c71e7-dd20-4dad-bb3e-c192801049c7",
                "order_num": 5,
                "interview_record": 1522927654414241792,
                "name": "绩效面谈II",
                "status": 1,
                "weight": 0.0,
                "node_type": 11,
                "users": [
                    {
                        "userId": 500000063,
                        "name": "杜燕明",
                        "email": "aef6dcbd-68ec-4851-b046-570f84246f6c_220222_150944@virtual.account",
                        "mobile": "18000000001",
                        "wx_userId": "",
                        "departmentName": "默认部门",
                        "staff_code": ""
                    }
                ]
            }, {
                "name": "上级评价",
                "status": 3,
                "weight": 0.0,
                "node_type": 3,
                "users": [{
                    "userId": 200149381,
                    "name": "张",
                    "email": "zynx@163.com",
                    "mobile": "13466734600",
                    "wx_userId": "",
                    "departmentName": "技术部"
                    }]
            }, {
                "name": "绩效校准",
                "status": 3,
                "weight": 0.0,
                "node_type": 4,
                "users": [{
                    "userId": 200388086,
                    "name": "李",
                    "email": "zyc@613.com",
                    "mobile": "13911095351",
                    "wx_userId": "",
                    "departmentName": "默认部门"
                }]
            }, {
                "name": "结束",
                "status": 3,
                "weight": 0.0,
                "node_type": 5,
                "users": []
            }]
        }]
    }
}
```

返回结果说明

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| code | int | 状态码 |
| message | string | 错误信息 |
| data | AssessFormListModel | 考核列表集合 |

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| total | int | 总数 |
| assess_forms | List<AssessFormModel> | 考核列表 |

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| assess_formId | string | 考核Id |
| assess_templateId | string | 考核模板标识 |
| assess_template_name | string | 考核模板名称 |
| assess_template_category | int | 考核模板分类标识 |
| assess_template_category_name | string | 考核模板分类名称 |
| assess_activityId | string | 考核活动Id |
| name | string | 考核名称 |
| user | UserModel | 被考核人 |
| current_nodeName | UserModel | 当前考核流程节点 |
| start_date | string | 开始时间 |
| end_date | string | 截止时间 |
| score | decimal | 考核分数 |
| rank | string | 考核等级 |
| is_end | bool | 是否结束 |
| cycle_type | int | 周期类型 （-1： 全部周期 0：自定义 1：年度 2：季度 3：月度 4：?月 - ?+1月 5：上/下半年 ） |
| cycle_name | string | 考核周期 |
| cycle_year | int | 考核周期设置的年份 |
| cycle_month | int | 考核周期设置的月份/季度/半年度 |
| nodes | List<NodeModel> | 流程节点集合 |

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| process_id | string | 流程节点标识 |
| order_num | int | 流程节点排序号 |
| interview_record | string | 面谈记录标识 |
| name | string | 流程节点名称 |
| status | int | 状态（1:已完成 2：进行中 3:未开始） |
| weight | decimal | 权重 |
| node_type | int | 流程节点类型（1：自评，2：同事评价 3：上级评价 4：绩效校准 6：指标制定 7：指标确认 8：执行期  9：结果确认 10：指标填写 11：绩效面谈 ） |
| users | List<UserModel> | 流程节点执行人 |

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| userId | int | 人员Id |
| name | string | 人员名称 |
| email | string | 邮箱 |
| mobile | string | 手机号 |
| departmentName | string | 部门名称 |
| wx_userId | string | 企业微信ID |
| staff_code | string | 工号 |

https://oapi.tita.com/api/{tenant_id}/performance/getevaluationsPostContent-Type	application/json请求Body

```
{
    "assessFormIds":["D4FCE45F-5DAC-4432-BB55-1479ECA55BD6","6868469D-18C9-4C24-B7BF-A6F65902213E"]
}
```

参数说明

| 参数名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| tenant_id | int | 是 | 租户标识 |
| assessFormIds | List<string> | 是 | 表单标识 |

```
{
    "code": 0,
    "errorMsg": null,
    "data": [
        {
            "id": "d4fce45f-5dac-4432-bb55-1479eca55bd6",
            "assessTemplateId": "b71748e0-a6f4-4fa1-b563-bf1de0a18675",
            "assessTemplateName": "多主题-0227",
            "assessTemplateCategory": 230,
            "assessTemplateCategoryName": "多主题",
            "user": {
                "userId": 500118572,
                "name": "18000000020",
                "email": "20c@tita.com",
                "mobile": "18000000020",
                "wx_userId": "",
                "departmentName": "默认部门",
                "staff_code": null
            },
            "name": "多主题-结果呈现",
            "currentNodeName": "结束",
            "createDate": "2023/2/28 15:08:44",
            "isEnd": true,
            "score": 5.00,
            "rank": "A",
            "modules": [
                {
                    "id": "382c3dfa-a84f-451a-90ba-d2fb07df7609",
                    "name": "KPI",
                    "type": "Quantify",
                    "weight": 0.00,
                    "assessItems": [
                        {
                            "extendedData": {
                                "superiorEvaluate-8b4bdd04-aac2-4ffc-80da-ece2170ef32b-500000063": "2",
                                "superiorScore-8b4bdd04-aac2-4ffc-80da-ece2170ef32b-500000063": "2"
                            },
                            "id": "a7eaba95-2f20-4e47-be4e-fe83a084d3ee",
                            "name": "1",
                            "finishDescription": null,
                            "evaluateStandard": "2",
                            "targetValue": "",
                            "actualValue": null,
                            "objType": 0,
                            "objId": "1",
                            "assessModuleId": "382c3dfa-a84f-451a-90ba-d2fb07df7609",
                            "assessModelType": 1,
                            "weight": 100.0,
                            "isSystem": true,
                            "scoreType": "Manual",
                            "parentId": "00000000-0000-0000-0000-000000000000",
                            "child": [],
                            "customFieldDatas": [
                                {
                                    "key": "zdy_WenBenZiDuan",
                                    "name": "自定义文本字段",
                                    "value": "自定义字段的值"
                                },
                                {
                                    "key": "zdy_ShuZhiZiDuan",
                                    "name": "自定义数值字段",
                                    "value": "100"
                                }
                            ]
                        }
                    ]
                }
            ],
            "evaluationTotals": [
                {
                    "id": 32993,
                    "user": {
                        "userId": 500000063,
                        "name": "杜燕明",
                        "email": "aef6dcbd-68ec-4851-b046-570f84246f6c_220222_150944@virtual.account",
                        "mobile": "18000000001",
                        "wx_userId": "",
                        "departmentName": "默认部门",
                        "staff_code": ""
                    },
                    "assessFormId": "d4fce45f-5dac-4432-bb55-1479eca55bd6",
                    "processId": "8b4bdd04-aac2-4ffc-80da-ece2170ef32b",
                    "evaluateType": 3,
                    "score": 2.00,
                    "rank": null,
                    "rankDescribe": null,
                    "evaluate": "2",
                    "createDate": "2023-02-28T15:09:24.01",
                    "motifyDate": "2023-02-28T15:09:39.31"，
                    "evaluateContents": [
                        {
                            "id": 2994,
                            "title": "高级评语1标题",
                            "description": "高级评语1描述",
                            "isRequired": true,
                            "content": "这是高级评语1的评语内容"
                        },{
                            "id": 2995,
                            "title": "高级评语2标题",
                            "description": "高级评语2描述",
                            "isRequired": true,
                            "content": "这是高级评语2的评语内容"
                        }
                    ]
                }
            ],
            "is_Appeal": false,
            "assessAppealRecordModels": [],
            "subjectResults": [
                {
                    "assessFormId": "d4fce45f-5dac-4432-bb55-1479eca55bd6",
                    "id": 2366,
                    "subjectId": "4f9c620a-c642-4faa-aaa3-13fc6172bdc0",
                    "subjectName": "价值观",
                    "rank": "D"
                },
                {
                    "assessFormId": "d4fce45f-5dac-4432-bb55-1479eca55bd6",
                    "id": 2367,
                    "subjectId": "06505af0-21cd-42bc-bb24-923da125009a",
                    "subjectName": "危机挑战",
                    "rank": "D"
                }
            ]
        },
        {
            "id": "6868469d-18c9-4c24-b7bf-a6f65902213e",
            "assessTemplateId": "b71748e0-a6f4-4fa1-b563-bf1de0a18675",
            "assessTemplateName": "多主题-0227",
            "assessTemplateCategory": 230,
            "assessTemplateCategoryName": "多主题",
            "user": {
                "userId": 500118570,
                "name": "18000000019",
                "email": "19d@tita.com",
                "mobile": "18000000019",
                "wx_userId": "",
                "departmentName": "默认部门",
                "staff_code": null
            },
            "name": "多主题-结果呈现",
            "currentNodeName": "结束",
            "createDate": "2023/2/28 15:08:44",
            "isEnd": true,
            "score": 5.00,
            "rank": "A",
            "modules": [
                {
                    "id": "382c3dfa-a84f-451a-90ba-d2fb07df7609",
                    "name": "KPI",
                    "type": "Quantify",
                    "weight": 0.00,
                    "assessItems": [
                        {
                            "extendedData": {
                                "superiorEvaluate-8b4bdd04-aac2-4ffc-80da-ece2170ef32b-500000063": "1",
                                "superiorScore-8b4bdd04-aac2-4ffc-80da-ece2170ef32b-500000063": "1"
                            },
                            "id": "133f1c61-0383-49f0-b908-0acacb5e990a",
                            "name": "1",
                            "finishDescription": null,
                            "evaluateStandard": "2",
                            "targetValue": "",
                            "actualValue": null,
                            "objType": 0,
                            "objId": "1",
                            "assessModuleId": "382c3dfa-a84f-451a-90ba-d2fb07df7609",
                            "assessModelType": 1,
                            "weight": 100.0,
                            "isSystem": true,
                            "scoreType": "Manual",
                            "parentId": "00000000-0000-0000-0000-000000000000",
                            "child": []
                        }
                    ]
                }
            ],
            "evaluationTotals": [
                {
                    "id": 32992,
                    "user": {
                        "userId": 500000063,
                        "name": "杜燕明",
                        "email": "aef6dcbd-68ec-4851-b046-570f84246f6c_220222_150944@virtual.account",
                        "mobile": "18000000001",
                        "wx_userId": "",
                        "departmentName": "默认部门",
                        "staff_code": ""
                    },
                    "assessFormId": "6868469d-18c9-4c24-b7bf-a6f65902213e",
                    "processId": "8b4bdd04-aac2-4ffc-80da-ece2170ef32b",
                    "evaluateType": 3,
                    "score": 1.00,
                    "rank": null,
                    "rankDescribe": null,
                    "evaluate": "1",
                    "createDate": "2023-02-28T15:08:49.503",
                    "motifyDate": "2023-02-28T15:09:00.61",
                    "evaluateContents": [
                        {
                            "id": 2998,
                            "title": "高级评语1标题",
                            "description": "高级评语1描述",
                            "isRequired": true,
                            "content": "这是高级评语1的评语内容"
                        },{
                            "id": 2999,
                            "title": "高级评语2标题",
                            "description": "高级评语2描述",
                            "isRequired": true,
                            "content": "这是高级评语2的评语内容"
                        }
                    ]
                }
            ],
            "is_Appeal": false,
            "assessAppealRecordModels": [],
            "subjectResults": [
                {
                    "assessFormId": "6868469d-18c9-4c24-b7bf-a6f65902213e",
                    "id": 2364,
                    "subjectId": "4f9c620a-c642-4faa-aaa3-13fc6172bdc0",
                    "subjectName": "价值观",
                    "rank": "D"
                },
                {
                    "assessFormId": "6868469d-18c9-4c24-b7bf-a6f65902213e",
                    "id": 2365,
                    "subjectId": "06505af0-21cd-42bc-bb24-923da125009a",
                    "subjectName": "危机挑战",
                    "rank": "D"
                }
            ]
        }
    ]
}
```

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| id | string | 表单标识 |
| assessTemplateId | string | 表单使用模板标识 |
| assessTemplateName | string | 表单使用模板名称 |
| assessTemplateCategory | int | 表单使用模板分类标识 |
| assessTemplateCategoryName | string | 表单使用模板分类名称 |
| user | UserModel | 用户 |
| name | string | 考核名称 |
| currentNodeName | string | 当前考核流程节点 |
| createDate | date | 创建时间 |
| isEnd | bool | 流程是否结束 |
| score | decimal | 考核分数 |
| rank | string | 考核等级 |
| modules | List<AssessModuleModel> | 考核维度 |
| evaluationTotals | List<AssessFormEvaluationTotalModel> | 考核总评 |
| is_Appeal | bool | 是否存在绩效校准 |
| assessAppealRecordModels | List<AssessAppealRecordModel> | 绩效校准集合 |
| subjectResults | List<AssessSubjectResultModel> | 多主题评价结果 |

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| id | string | 维度标识 |
| name | string | 维度名称 |
| type | string | 维度类型 |
| weight | decimal | 维度权重 |
| assessItems | List<AssessItemModel> | 考核总评 |

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| id | string | 指标标识 |
| extendedData | string | 指标评价数据 |
| customFieldDatas | string | 自定义字段数据 |
| name | string | 指标名称 |
| finishDescription | string | 完成说明 |
| evaluateStandard | string | 评价标准 |
| targetValue | string | 目标值 |
| actualValue | string | 完成值 |
| objType | string | 对象类型 62 目标、65 KR |
| objId | string | 对象标识 |
| assessModuleId | string | 维度标识 |
| assessModelType | string | 维度类型 |
| weight | decimal | 维度权重 |
| isSystem | bool | 是否模板指标 |
| scoreType | string | 评分类型 Manual 手动、Auto 根据公式自动计算 |
| parentId | string | 父指标标识 |
| child | List<AssessItemModel> | 子指标 |

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| id | int | 总评标识 |
| assessFormId | string | 表单标识 |
| processId | string | 流程标识 |
| evaluateType | string | 评价类型 |
| score | string | 评分 |
| rank | string | 评级 |
| rankDescribe | string | 评级描述 |
| evaluate | string | 评语 |
| createDate | string | 创建时间 |
| motifyDate | string | 修改时间, |
| evaluateContents | List<AssessEvaluateContentModel> | 高级评语 |

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| id | int | 高级评语Id标识 |
| title | string | 评语标题 |
| description | string | 评语描述 |
| isRequired | bool | 是否必填 |
| content | string | 评语内容 |

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| id | int | 申诉编号 |
| appealNum | string | 申诉次数 |
| appealUser | UserModel | 申诉人 |
| appealDate | DateTime | 申诉时间 |
| appealReasons | string | 申诉理由 |
| originScore | decimal | 申诉前分数 |
| originRank | decimal | 申诉前等级 |
| score | decimal | 申诉后分数 |
| rank | decimal | 申诉后等级 |
| updateBy | UserModel | 处理人 |
| updateTime | DateTime | 处理时间 |
| reasons | string | 处理理由 |
| typeId | int | 申诉标签 |
| typeName | string | 申诉标签 |
| assessFormId | string | 考核表编码 |
| assessActivityId | string | 考核活动Id |

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| SubjectId | string | 主题编码 |
| SubjectName | string | 主题名称 |
| OriginRank | string | 申诉前等级 |
| Rank | string | 申诉后等级 |

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| assessFormId | string | 表单标识 |
| id | int | 多主题评价标识 |
| SubjectId | string | 主题编码 |
| SubjectName | string | 主题名称 |
| Rank | string | 等级 |

https://oapi.tita.com/api/{tenant_id}/performance/activity/listPostContent-Type	application/json请求Body

```
{
    "beginTime": "2025-01-01",
    "endTime": "2025-06-01",
    "activityName": "考核名称1",
    "activityStatus": 1,
    "pageNum": 1,
    "pageSize": 10
}
```

参数说明

| 参数名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| tenant_id | int | 是 | 租户标识 |
| beginTime | string | 否 | 根据活动创建时间查询（闭区间） |
| endTime | string | 否 | 根据活动创建时间查询（开区间） |
| activityName | string | 否 | 活动名称，模糊查询 |
| pageNum | int | 是 | 页号 |
| pageSize | int | 是 | 页码 |

```
{
    "code": 0,
    "errorMsg": null,
    "data": {
        "total": 10,
        "activities": [
            {
                "tenantId": 500023,
                "userId": 500000157,
                "id": "fcf41e9d-1f60-4802-88d4-353ef48aee14",
                "category": 595,
                "name": "活动名称1",
                "departmentId": 52,
                "shareToSub": true,
                "assessType": 0,
                "assessTrialType": 0,
                "organizationFixedType": 2,
                "organizationFixedTime": "2025-05-14T00:00:00",
                "cycleType": 1,
                "cycleYear": 2025,
                "cycleMonth": 0,
                "userTotal": 3,
                "startDate": "2025/01/01",
                "endDate": "2025/12/31",
                "description": "",
                "status": 1,
                "createTime": "2025/05/14 20:27:53",
                "isAutoAddition": false,
                "isAutoNotification": false,
                "okrGradeSetting": 1
            }
		]
	}
}
```

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| id | string | 表单标识 |
| tenantId | int | 租户Id |
| userId | int | 活动发起人 |
| id | string | 活动id |
| category | int | 所属分类 |
| name | string | 活动名称 |
| departmentId | int | 所属部门 |
| shareToSub | bool | 是否向下共享 |
| assessType | int | 考核类型：0正式考核，1试用期考核 |
| assessTrialType | int | 试用期考核类型：1试用中考核，2转正考核 |
| organizationFixedType | int | 锁定类型：0不锁定，1考核结束锁定，2指定时间锁定 |
| organizationFixedTime | datetime | 锁定时间 |
| cycleType | int | 周期类型：1年度，2季度，3月度，4双月，5半年度 |
| cycleName | string | 周期名称 |
| cycleYear | int | 年 |
| cycleMonth | int | 月 |
| userTotal | int | 被考核人数 |
| startDate | string | 活动开始时间 |
| endDate | string | 活动结束时间 |
| status | int | 活动状态：1进行中，2结束，3未开始 |
| createTime | string | 活动创建时间 |
| okrGradeSetting | int | 是否开启kr评分：1表示开启 |

https://oapi.tita.com/api/{tenant_id}/performance/getAssessFormResultsPostContent-Type	application/json请求Body

```
{
    "activityId": "a6ccf4f9-e0a8-430d-926b-70bbaa7dd01e",
    "pageNum": 1,
    "pageSize": 10
}
```

参数说明

| 参数名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| tenant_id | int | 是 | 租户标识 |
| activityId | string | 是 | 考核活动Id |
| pageNum | int | 是 | 页号 |
| pageSize | int | 是 | 页码 |

```
{
    "code": 0,
    "errorMsg": null,
    "data": {
        "total": 2,
        "assessForms": [
            {
                "user": {
                    "userId": 500000158,
                    "name": "张三",
                    "email": "zhangsan@163.com",
                    "mobile": "18931930000",
                    "wxUserId": "",
                    "departmentName": "部门1",
                    "staffCode": "B01101"
                },
                "name": "考核活动1",
                "assessFormId": "ca833b32-581c-4567-96db-1dc1d6449fe5",
                "assessTemplateId": "346b1f49-c105-4af4-8836-a21ebe15fce7",
                "assessActivityId": "a6ccf4f9-e0a8-430d-926b-70bbaa7dd01e",
                "createDate": "2023/11/20 11:46:38",
                "score": 172.30,
                "rank": "A",
                "factor": null,
                "isEnd": true,
                "cycleType": 1,
                "cycleName": "2025年 年度",
                "cycleYear": 2025,
                "cycleMonth": 0
            }
		]
	}
}
```

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| id | string | 表单标识 |
| assessFormId | string | 考核id |
| name | string | 活动名称 |
| assessTemplateId | string | 模板id |
| assessActivityId | string | 活动id |
| createDate | string | 创建时间 |
| score | decimal | 考核得分 |
| rank | string | 等级 |
| factor | decimal | 绩效系数 |
| isEnd | bool | 考核是否结束 |
| cycleType | int | 周期类型：1年度，2季度，3月度，4双月，5半年度 |
| cycleName | string | 周期名称 |
| cycleYear | int | 年 |
| cycleMonth | int | 月 |

---

## 职级/职务/标签

获取人员职务列表2.PositionListModel3.PositionModel添加职务2.PositionModel编辑职务删除职务获取人员职级列表2.RankListModel3.RankModel添加职级2.RankModel编辑职级删除职级获取人员标签列表2.LabelListModel3.LabelModel添加标签2.LabelModel编辑标签删除标签<font color="#dd0000">注：开发文档内所有涉及编码处均已UTF-8形式编码！！！</font>https://oapi.tita.com/api/{tenant_id}/position/searchGet请求参数

| 参数名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| tenant_id | int | 是 | 租户标识 |
| page_num | int | 是 | 页码 |
| page_size | int | 是 | 单页数量 |

返回结果示例

```
{
	"code": 0,
	"errorMsg": null,
	"data": {
		"total": 7,
		"positions": [{
			"id": 2118,
			"code": "00011",
			"name": "高级工程师修改了",
			"description": null
		}]
	}
}
```

返回结果说明

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| code | int | 状态码 |
| message | string | 错误信息 |
| data | PositionListModel | 职务列表集合 |

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| total | int | 总数 |
| positions | List<PositionModel> | 职务列表 |

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| id | int | 职务标识 |
| code | string | 职务编码 |
| name | string | 职务名称 |
| description | string | 职务描述 |

https://oapi.tita.com/api/{tenant_id}/position/addPostContent-Type  application/json请求Body

```
{
	"code": "Service2",
	"name": "接口测",
	"description": "接口测试2"
}
```

参数说明

| 参数名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| code | string | 是 | 职务编码 |
| name | string | 是 | 职务名称 |
| description | string | 否 | 职务描述 |

返回结果示例

```
{
    "code": 0,
    "errorMsg": null,
    "data": {
        "id": 6896,
        "code": "Service2",
        "name": "接口测",
        "description": "接口测试2"
    }
}
```

返回结果说明

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| code | int | 状态码 |
| message | string | 错误信息 |
| data | PositionModel | 职务信息 |

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| id | int | 职务标识 |
| code | string | 职务编码 |
| name | string | 职务名称 |
| description | string | 职务描述 |

https://oapi.tita.com/api/{tenant_id}/position/updatePostContent-Type  application/json请求Body

```
{
	"code": "Service2",
	"name": "接口测",
	"description": "接口测试2"
}
```

参数说明

| 参数名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| code | string | 是 | 职务编码 |
| name | string | 是 | 职务名称 |
| description | string | 否 | 职务描述 |

返回结果示例

```
{
    "code": 0,
    "errorMsg": null,
    "data": null
}
```

返回结果说明

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| code | int | 状态码 |
| message | string | 错误信息 |
| data | object |  |

https://oapi.tita.com/api/{tenant_id}/position/deletePostContent-Type  application/json请求Body

```
{
	"code": "Service2"
}
```

参数说明

| 参数名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| code | string | 是 | 职务编码 |

返回结果示例

```
{
    "code": 0,
    "errorMsg": null,
    "data": null
}
```

返回结果说明

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| code | int | 状态码 |
| message | string | 错误信息 |
| data | object |  |

https://oapi.tita.com/api/{tenant_id}/rank/searchGet请求参数

| 参数名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| tenant_id | int | 是 | 租户标识 |
| page_num | int | 是 | 页码 |
| page_size | int | 是 | 单页数量 |

返回结果示例

```
{
	"code": 0,
	"errorMsg": null,
	"data": {
		"total": 7,
		"ranks": [{
			"rank_id": 2118,
			"rank_name": "P3",
		}]
	}
}
```

返回结果说明

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| code | int | 状态码 |
| message | string | 错误信息 |
| data | RankListModel | 职级列表集合 |

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| total | int | 总数 |
| ranks | List<RankModel> | 职级列表 |

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| rank_id | int | 职级标识 |
| rank_name | string | 职级名称 |

https://oapi.tita.com/api/{tenant_id}/rank/addPostContent-Type  application/json请求Body

```
{
	"rank_name": "P3",
}
```

参数说明

| 参数名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| rank_name | string | 是 | 职级名称 |

返回结果示例

```
{
    "code": 0,
    "errorMsg": null,
    "data": {
        "rank_id": 6896,
        "rank_name": "P3"
    }
}
```

返回结果说明

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| code | int | 状态码 |
| message | string | 错误信息 |
| data | RankModel | 职级信息 |

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| rank_id | int | 职级标识 |
| rank_name | string | 职级名称 |

https://oapi.tita.com/api/{tenant_id}/rank/updatePostContent-Type  application/json请求Body

```
{
	 "rank_id": 6896,
     "rank_name": "P3"
}
```

参数说明

| 参数名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| rank_id | int | 职级标识 |  |
| rank_name | string | 职级名称 |  |

返回结果示例

```
{
    "code": 0,
    "errorMsg": null,
    "data": null
}
```

返回结果说明

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| code | int | 状态码 |
| message | string | 错误信息 |
| data | object |  |

https://oapi.tita.com/api/{tenant_id}/rank/deletePostContent-Type  application/json请求Body

```
{
	 "rank_id": 6896
}
```

参数说明

| 参数名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| rank_id | string | 是 | 职级标识 |

返回结果示例

```
{
    "code": 0,
    "errorMsg": null,
    "data": null
}
```

返回结果说明

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| code | int | 状态码 |
| message | string | 错误信息 |
| data | object |  |

https://oapi.tita.com/api/{tenant_id}/label/searchGet请求参数

| 参数名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| tenant_id | int | 是 | 租户标识 |
| page_num | int | 是 | 页码 |
| page_size | int | 是 | 单页数量 |

返回结果示例

```
{
	"code": 0,
	"errorMsg": null,
	"data": {
		"total": 7,
		"labels": [{
			"label_id": 2118,
			"label_name": "P3",
		}]
	}
}
```

返回结果说明

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| code | int | 状态码 |
| message | string | 错误信息 |
| data | LabelListModel | 标签列表集合 |

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| total | int | 总数 |
| labels | List<LabelModel> | 标签列表 |

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| label_id | int | 标签标识 |
| label_name | string | 标签名称 |

https://oapi.tita.com/api/{tenant_id}/label/addPostContent-Type  application/json请求Body

```
{
	"label_name": "P3",
}
```

参数说明

| 参数名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| label_name | string | 是 | 标签名称 |

返回结果示例

```
{
    "code": 0,
    "errorMsg": null,
    "data": {
        "label_id": 6896,
        "label_name": "P3"
    }
}
```

返回结果说明

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| code | int | 状态码 |
| message | string | 错误信息 |
| data | LabelModel | 标签信息 |

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| label_id | int | 标签标识 |
| label_name | string | 标签名称 |

https://oapi.tita.com/api/{tenant_id}/label/updatePostContent-Type  application/json请求Body

```
{
	 "label_id": 6896,
     "label_name": "P3"
}
```

参数说明

| 参数名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| label_id | int | 标签标识 |  |
| label_name | string | 标签名称 |  |

返回结果示例

```
{
    "code": 0,
    "errorMsg": null,
    "data": null
}
```

返回结果说明

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| code | int | 状态码 |
| message | string | 错误信息 |
| data | object |  |

https://oapi.tita.com/api/{tenant_id}/label/deletePostContent-Type  application/json请求Body

```
{
	 "label_id": 6896
}
```

参数说明

| 参数名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| label_id | string | 是 | 标签标识 |

返回结果示例

```
{
    "code": 0,
    "errorMsg": null,
    "data": null
}
```

返回结果说明

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| code | int | 状态码 |
| message | string | 错误信息 |
| data | object |  |

---

## 复盘接口

获取复盘https://oapi.tita.com/api/{tenant_id}/review/searchGet请求参数

| 参数名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| tenant_id | int | 是 | 租户标识 |
| page_num | int | 是 | 页码 |
| page_size | int | 是 | 单页数量 |
| start_date | string | 是 | 开始时间 |
| end_date | string | 是 | 截止时间 |
| review_type | string | 否 | 复盘类型逗号隔开，默认全部（87：单OKR复盘 88：周期OKR复盘 89：单项目复盘 90：自定义复盘） |

返回结果示例

```
{
    "code": 1,
    "errorMsg": null,
    "data": {
        "total": 6946,
        "reviews": [
            {
                "review_id": "123",
                "review_name": "复盘名称",
                "review_type": 87,
                "create_date": "2019/04/25 08:00:00",
                "create_user": {
                    "userId": 123456789,
                    "name": "tita",
                    "email": "tita@tita.com"
                },
                "obj_id": "12345",
                "obj_type": 0,
                "details": [
                {
	                "module_type": "",
	                "module_name": "目标复盘",
	                "module_value": "测试"
                }

                ]
            }
        ]
    }
}
```

返回结果说明

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| code | int | 状态码 |
| message | string | 错误信息 |
| data | ReviewListModel | 复盘集合 |

2.ReviewListModel

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| total | int | 数量 |
| reviews | List<ReviewModel> | 复盘列表 |

3.TaskModel

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| review_name | string | 复盘名称 |
| review_id | string | 复盘ID |
| review_type | int | 复盘类型 |
| create_user | UserModel | 发起人 |
| create_date | string | 创建时间 |
| obj_id | string | 复盘关联的对象ID |
| obj_type | int | 复盘关联的对象类型 |
| details | List<ReviewModuleModel> | 复盘组件里详情信息 |

5.ReviewModuleModel

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| module_type | string | 复盘组件类型 |
| module_name | string | 复盘组件名称 |
| module_value | string | 复盘组件内容 |

5.UserModel

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| userId | int | 人员Id |
| name | string | 人员名称 |
| email | string | 邮箱 |
| mobile | string | 手机号 |
| departmentName | string | 部门名称 |
| wx_userId | string | 企业微信ID |

---

## 员工接口

创建员工返回结果：修改员工批量修改员工离职修改直接上级获取用户列表2.UserListModel3.UserDetailModel获取工号为空的用户列表2.UserListModel3.UserDetailModel获取用户详情2.UserDetailModel<font color="#dd0000">注：开发文档内所有涉及编码处均已UTF-8形式编码！！！</font>https://oapi.tita.com/api/{tenant_id}/staff/addPostContent-Type	application/json请求Body

```
{
    "name": "张",
    "mobile": "18383736132",
    "email": "ceshi@tita.com",
    "position": "总经理",
    "rank": "P2",
    "label": "试用期",
    "department_code": "销售部",
    "lineManager_acccountName": "18383736132",
    "dottedlineManager_acccountName": ["138383736134"],
    "sex": 1,
    "employed_Date": "2019/04/25",
    "birthDay": "2019/04/25" ,
    "account_type": 0 ,
}
```

参数说明

| 参数名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| tenant_id | int | 是 | 租户标识 |
| name | string | 是 | 姓名 |
| mobile | string | 是 | 手机号（作为登录账号） |
| email | string | 否 | 邮箱 |
| staff_code | string | 否 | 工号 |
| position | string | 否 | 职务 |
| rank | string | 否 | 职级名称 |
| label | string | 否 | 标签名称（多标签用英文,分割） |
| department_code | string | 否 | 所属部门编码 |
| lineManager_acccountName | string | 否 | 上级账号（邮箱 、手机号、工号） |
| dottedlineManager_acccountName | List<string> | 否 | 虚线上级账号（邮箱 、手机号、工号） |
| sex | string | 否 | 性别（0:男 1:女 2:未知） |
| employed_Date | date | 否 | 入职时间 |
| birthDay | date | 否 | 生日 |
| account_type | int | 否 | 账号类型（0.邮箱或手机号（默认为0），1.企业微信账号，4.工号） |

```
{
    "code": 0,
    "errorMsg": null,
    "data": {
        "objData": 2458586
    }
}
```

参数说明

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| code | int | 状态码 (0:成功) |
| message | string | 错误信息 |
| data | string | 用户ID |

https://oapi.tita.com/api/{tenant_id}/staff/updatePostContent-Type  application/json请求Body

```
{
    "acccount_name": "18383736132",
    "name": "张",
    "mobile": "18383736132",
    "email": "ceshi@tita.com",
    "position": "总经理",
    "rank": "P2",
    "label": "试用期",
    "department_code": "销售部",
    "lineManager_acccountName": "18383736132",
    "dottedlineManager_acccountName": ["138383736134"],
    "sex": 1,
    "employed_Date": 2019/04/25,
    "birthDay": 2019/04/25 ,
    "account_type":0,
}
```

参数说明

| 参数名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| tenant_id | int | 是 | 租户标识 |
| acccount_name | string | 是 | 账号（邮箱或手机号） |
| name | string | 是 | 姓名 |
| mobile | string | 否 | 手机号（作为登录账号） |
| email | string | 否 | 邮箱 |
| position | string | 否 | 职务 |
| rank | string | 否 | 职级名称 |
| label | string | 否 | 标签名称（多标签用英文,分割） |
| department_code | string | 否 | 所属部门编码 |
| staff_code | string | 否 | 员工工号 |
| lineManager_acccountName | string | 否 | 上级账号（邮箱 、手机号、工号，TitaUserId） |
| dottedlineManager_acccountName | List<string> | 否 | 虚线上级账号（邮箱 、手机号、工号，TitaUserId） |
| sex | string | 否 | 性别（0:男 1:女 2:未知） |
| employed_Date | date | 否 | 入职时间 |
| birthDay | date | 否 | 生日 |
| account_type | int① | 否 | 账号类型（0:手机号或邮箱（默认为0） 1：企业微信账号 4:员工工号 5：TitaUserId） |

返回结果

```
{
    "code": 0,
    "errorMsg": null,
}
```

参数说明

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| code | int | 状态码 (0:成功) |
| message | string | 错误信息 |

https://oapi.tita.com/api/{tenant_id}/staff/batch/updatePostContent-Type  application/json请求Body

```
[{
    "acccount_name": "18383736132",
    "name": "张",
    "mobile": "18383736132",
    "email": "ceshi@tita.com",
    "position": "总经理",
    "department_code": "销售部",
    "lineManager_acccountName": "18383736132",
      "dottedlineManager_acccountName": ["138383736134"],
    "account_type":0,
},
{
    "acccount_name": "18383736132",
    "name": "张",
    "mobile": "18383736132",
    "email": "ceshi@tita.com",
    "position": "总经理",
    "department_code": "销售部",
    "lineManager_acccountName": "18383736132",
    "dottedlineManager_acccountName": ["138383736134"],
    "account_type":1,
}
]
```

参数说明

| 参数名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| tenant_id | int | 是 | 租户标识 |
| acccount_name | string | 是 | 账号（邮箱或手机号） |
| wx_userId | string | 是 | 企业微信账号 |
| name | string | 是 | 姓名 |
| mobile | string | 否 | 手机号（作为登录账号） |
| email | string | 否 | 邮箱 |
| position | string | 否 | 职务 |
| department_code | string | 否 | 所属部门编码 |
| staff_code | string | 否 | 员工工号 |
| lineManager_acccountName | string | 否 | 上级账号（（邮箱 、手机号、工号，TitaUserId） |
| lineManager_wxUserId | string | 否 | 上级企业微信账号 |
| dottedlineManager_acccountName | List<string> | 否 | 虚线上级账号（邮箱 、手机号、工号，TitaUserId） |
| sex | string | 否 | 性别（0:男 1:女 2:未知） |
| employed_Date | date | 否 | 入职时间 |
| birthDay | date | 否 | 生日 |
| account_type | int① | 否 | 账号类型（0:手机号或邮箱（默认为0） 1：企业微信账号 4.员工工号 5：TitaUserId） |

返回结果

```
{
    "code": 0,
    "errorMsg": null,
    "data":[{"acccount_name":"11","wx_userId":"11","update_result":true,"error_message":"错误"}]
}
```

参数说明

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| code | int | 状态码 (0:成功) |
| message | string | 错误信息 |

https://oapi.tita.com/api/{tenant_id}/staff/leavePostContent-Type  application/json请求Body

```
{
    "acccount_name": "187363621622",
    "account_type":0,
}
```

参数说明

| 参数名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| tenant_id | int | 是 | 租户标识 |
| acccount_name | string | 是 | 账号（邮箱或手机号） |
| account_type | string | 否 | 账号类型（0:手机号或邮箱（默认为0） 1：企业微信账号 4:员工工号 5：TitaUserId） |

返回结果：

```
{
    "code": 0,
    "errorMsg": null,
}
```

参数说明

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| code | int | 状态码 (0:成功) |
| message | string | 错误信息 |

https://oapi.tita.com/api/{tenant_id}/staff/lineManager/updatePostContent-Type  application/json请求Body

```
{
    "acccount_name": "187363621622",
    "lineManager_acccountName": "187363621632",
    "account_type":0,
}
```

参数说明

| 参数名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| tenant_id | int | 是 | 租户标识 |
| acccount_name | string | 是 | 被修改人账号（邮箱或手机号） |
| lineManager_acccountName | string | 是 | 上级账号（邮箱或手机号） |
| account_type | int① | 否 | 账号类型（0:手机号或邮箱（默认为0） 1：企业微信账号 4:员工工号 5：TitaUserId） |

返回结果示例

```
{
    "code": 0,
    "errorMsg": null,
}
```

返回结果说明

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| code | int | 状态码 (0:成功) |
| message | string | 错误信息 |
| data | string | OKR标识 |

https://oapi.tita.com/api/{tenant_id}/staff/searchGet请求参数

| 参数名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| tenant_id | int | 是 | 租户标识 |
| page_num | int | 是 | 页码 |
| page_size | int | 是 | 单页数量 |
| content | string | 否 | 关键词 |
| department_code | string | 否 | 所属部门编码 |

返回结果示例

```
{
	"code": 0,
	"errorMsg": null,
	"data": {
		"total": 62,
		"users": [{
			"userId": 200149001,
			"name": "测试人员",
			"email": "ceshi@163.com",
			"mobile": "12345678900",
			"position": "运营总监",
			"staff_code": "",
			"position_code": "2951",
			"department_id": 70290,
			"department_name": "技术部",
			"department_code": "TITA-DEPT-c96c497e-01b3-41fc-a30e-b06a07c8a349",
			"birthday": null,
			"employed_Date": null,
			"sex": null,
			"jobState": 0,
            "rank_name": 职级,
            "labels": ["标签1","标签2"],
			"lineManger_name": "",
			"lineManger_userId": 0,
			"dottedLine_superior": [],
			"dottedLine_superiorUsers": []
		}]
	}
}
```

返回结果说明

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| code | int | 状态码 |
| message | string | 错误信息 |
| data | UserListModel | 人员集合 |

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| total | int | 人员信息条数 |
| users | List<UserDetailModel> | 人员列表 |

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| userId | int | 用户Id |
| name | string | 用户姓名 |
| email | string | 邮箱 |
| mobile | string | 手机号 |
| position | string | 职务 |
| staff_code | string | 人员编码 |
| position_code | string | 职务编码 |
| department_id | int | 部门Id |
| department_name | string | 部门名称 |
| department_code | string | 部门编码 |
| birthday | string | 生日 |
| employed_Date | string | 入职时间 |
| sex | string | 性别 |
| jobState | int | 人员状态（1、在职，0、离职） |
| rank_name | string | 职级 |
| labels | List<string> | 标签集合 |
| lineManger_name | string | 上级人员名称 |
| lineManger_userId | string | 上级人员UserId |
| dottedLine_superior | List<string> | 虚线上级人员姓名 |
| dottedLine_superiorUsers | List<UserDetailModel> | 虚线上级人员信息 |

https://oapi.tita.com/api/{tenant_id}/staff/emptyStaffCodeGet请求参数

| 参数名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| tenant_id | int | 是 | 租户标识 |
| page_num | int | 是 | 页码 |
| page_size | int | 是 | 单页数量 |

返回结果示例

```
{
	"code": 0,
	"errorMsg": null,
	"data": {
		"total": 62,
		"users": [{
			"userId": 200149001,
			"name": "测试人员",
			"email": "ceshi@163.com",
			"mobile": "12345678900",
			"position": "运营总监",
			"staff_code": "",
			"position_code": "2951",
			"department_id": 70290,
			"department_name": "技术部",
			"department_code": "TITA-DEPT-c96c497e-01b3-41fc-a30e-b06a07c8a349",
			"birthday": null,
			"employed_Date": null,
			"sex": null,
			"jobState": 0,
            "rank_name": 职级,
            "labels": ["标签1","标签2"],
			"lineManger_name": "",
			"lineManger_userId": 0,
			"dottedLine_superior": [],
			"dottedLine_superiorUsers": []
		}]
	}
}
```

返回结果说明

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| code | int | 状态码 |
| message | string | 错误信息 |
| data | UserListModel | 人员集合 |

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| total | int | 人员信息条数 |
| users | List<UserDetailModel> | 人员列表 |

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| userId | int | 用户Id |
| name | string | 用户姓名 |
| email | string | 邮箱 |
| mobile | string | 手机号 |
| position | string | 职务 |
| staff_code | string | 人员编码 |
| position_code | string | 职务编码 |
| department_id | int | 部门Id |
| department_name | string | 部门名称 |
| department_code | string | 部门编码 |
| birthday | string | 生日 |
| employed_Date | string | 入职时间 |
| sex | string | 性别 |
| jobState | int | 人员状态（1、在职，0、离职） |
| rank_name | string | 职级 |
| labels | List<string> | 标签集合 |
| lineManger_name | string | 上级人员名称 |
| lineManger_userId | string | 上级人员UserId |
| dottedLine_superior | List<string> | 虚线上级人员姓名 |
| dottedLine_superiorUsers | List<UserDetailModel> | 虚线上级人员信息 |

https://oapi.tita.com/api/{tenant_id}/staff/getGet请求参数

| 参数名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| tenant_id | int | 是 | 租户标识 |
| acccount_name | string | 是 | 账号（邮箱或手机号） |
| account_type | int① | 否 | 账号类型（0:手机号或邮箱（默认为0） 1：企业微信账号 4:工号 5：TitaUserId） |

返回结果示例

```
{
    "code": 0,
    "errorMsg": null,
    "data": {
        "userId": 200149001,
			"name": "测试人员",
			"email": "ceshi@163.com",
			"mobile": "12345678900",
			"position": "运营总监",
			"staff_code": "",
			"position_code": "2951",
			"department_id": 70290,
			"department_name": "技术部",
			"department_code": "TITA-DEPT-c96c497e-01b3-41fc-a30e-b06a07c8a349",
			"birthday": null,
			"employed_Date": null,
			"sex": null,
			"jobState": 0,
            "rank_name": 职级,
            "labels": ["标签1","标签2"],
			"lineManger_name": "",
			"lineManger_userId": 0,
			"dottedLine_superior": [],
			"dottedLine_superiorUsers": []
    }
}
```

返回结果说明

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| code | int | 状态码 |
| message | string | 错误信息 |
| data | UserDetailModel | 人员详情 |

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| userId | int | 用户Id |
| name | string | 用户姓名 |
| email | string | 邮箱 |
| mobile | string | 手机号 |
| position | string | 职务 |
| staff_code | string | 人员编码 |
| position_code | string | 职务编码 |
| department_id | int | 部门Id |
| department_name | string | 部门名称 |
| department_code | string | 部门编码 |
| birthday | string | 生日 |
| employed_Date | string | 入职时间 |
| sex | string | 性别 |
| jobState | int | 人员状态（1、在职，0、离职） |
| rank_name | string | 职级 |
| labels | List<string> | 标签集合 |
| lineManger_name | string | 上级人员名称 |
| lineManger_userId | string | 上级人员UserId |
| dottedLine_superior | List<string> | 虚线上级人员姓名 |
| dottedLine_superiorUsers | List<UserDetailModel> | 虚线上级人员信息 |

---

## 360评估接口

获取指定时间段内360评估结果列表2.SurveyPageModel3.SurveyModel4.UserModel<font color="#dd0000">注：开发文档内所有涉及编码处均已UTF-8形式编码！！！</font>https://oapi.tita.com/api/{tenant_id}/survey/getSurveyByCycleGet请求参数

| 参数名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| tenant_id | int | 是 | 租户标识 |
| page_num | int | 是 | 页码 |
| page_size | int | 是 | 单页数量 |
| start_date | string | 是 | 开始时间 |
| end_date | string | 是 | 截止时间 |

返回结果示例

```
{
    "code": 0,
    "errorMsg": null,
    "data": {
        "total": 2565,
        "surveyInfos": [
            {
                "surveyName": "选项分值一样",
                "surveyYear": 2023,
                "surveyCycle": "2023年 年度",
                "startTime": "2023-01-01T00:00:00",
                "endTime": "2023-12-31T00:00:00",
                "userModel": {
                    "userId": 500000057,
                    "name": "张一一",
                    "email": "zhang01@b.com",
                    "mobile": "13990000001",
                    "wx_userId": "",
                    "departmentName": "一级部门A",
                    "staff_code": "2017040029"
                },
                "score": 0.0
            },
            {
                "surveyName": "选项分值一样",
                "surveyYear": 2023,
                "surveyCycle": "2023年 年度",
                "startTime": "2023-01-01T00:00:00",
                "endTime": "2023-12-31T00:00:00",
                "userModel": {
                    "userId": 500000057,
                    "name": "张一一",
                    "email": "zhang01@b.com",
                    "mobile": "13990000001",
                    "wx_userId": "",
                    "departmentName": "一级部门A",
                    "staff_code": "2017040029"
                },
                "score": 0.0
            }
        ]
    }
}
```

返回结果说明

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| code | int | 状态码 |
| message | string | 错误信息 |
| data | SurveyPageModel | 360评估结果集合 |

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| total | int | 总数 |
| surveyInfos | List<SurveyModel> | 考核列表 |

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| surveyName | string | 评估活动名称 |
| surveyYear | string | 评估年度 |
| surveyCycle | string | 评估周期 |
| startTime | string | 活动开始时间 |
| endTime | string | 活动结束时间 |
| userModel | UserModel | 被评人信息 |
| score | decimal | 评估分数 |

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| userId | int | 人员Id |
| name | string | 人员名称 |
| email | string | 邮箱 |
| mobile | string | 手机号 |
| departmentName | string | 部门名称 |
| wx_userId | string | 企业微信ID |
| staff_code | string | 工号 |

---

## 任务接口

创建任务信息https://oapi.tita.com/api/{tenant_id}/task/addPostContent-Type	application/json请求Body

```
{
     "name": "目标1",
     "account_name": "18373773171",
     "principal_account": "18373773171",
     "participant_account": ["18373773171","18373773172"],
    "apply_account": "18373773171",
     "visibility": 1,
     "start_date": "2020-01-01",
     "end_date": "2020-01-30",
     "description": "描述",
     "work_id": 10000,
     "okr_id": 10001,
     "kr_id": 10002,
     "milestone_id":10003,
     "parent_taskid": "",
}
```

参数说明

| 参数名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| tenant_id | int | 是 | 租户标识 |
| name | string | 是 | 任务名称 |
| relation_id | string | 否 | 第三方ID（而可以通过该值查询或更新） |
| account_type | int | 是 | 账号类型 （0:手机号或邮箱 1：企业微信账号 2：钉钉账号） |
| account_name | string | 是 | 创建人账号（根据account_type不同进行赋值） |
| principal_account | string | 是 | 负责人账号（根据account_type不同进行赋值） |
| participant_account | List<string> | 是 | 参与人账号（根据account_type不同进行赋值) |
| apply_account | string | 否 | 审批人账号（根据account_type不同进行赋值） |
| visibility | int | 是① | 是否私密(1:公开 2：私密) |
| start_date | string | 是 | 开始时间 |
| end_date | string | 是 | 截止时间 |
| description | string | 否 | 描述 |
| work_id | int | 否 | 所属项目ID |
| okr_id | int | 否 | 关联得目标ID |
| kr_id | int | 否 | 关联得关键成果ID |
| milestone_id | int | 否 | 关联的里程碑ID |
| parent_taskid | string | 否 | 母任务ID |
| status | int | 否 | 任务状态 |
| target_value | decimal | 否 | 目标值 |
| unit_name | string | 否 | 单位 |

①：Visibility(是否私密)默认值：1返回结果示例

```
{
    "code": 0,
    "errorMsg": null,
    "data": {
        "objData": "300283_6674544_7_20_637201520763717781"
    }
}
```

返回结果说明

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| code | int | 状态码 |
| message | string | 错误信息 |
| data.objData | string | 任务ID |

修改任务信息https://oapi.tita.com/api/{tenant_id}/task/updatePostContent-Type  application/json请求Body

```
{
     "task_id": "600037_62369_7_20_638168330922933490",
     "name":"任务",
     "account_name": "18373773171",
     "principal_account": "18373773171",
     "participant_account": ["18373773171","18373773172"],
     "visibility": 1,
     "start_date": "2020-01-01",
     "end_date": "2020-01-30",
     "description": "描述",
     "work_id": "10000",
     "okr_id": "10001",
     "kr_id": "10002",
}
```

参数说明

| 参数名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| tenant_id | int | 是 | 租户标识 |
| task_id | string | 是 | 任务ID |
| account_name | string | 是 | 操作人账号（根据account_type不同进行赋值） |
| name | string | 否 | 任务名称 |
| account_type | int | 否 | 账号类型 （0:手机号或邮箱 1：企业微信账号 2：钉钉账号 4：员工工号） |
| principal_account | string | 否 | 负责人账号（根据account_type不同进行赋值） |
| participant_account | List<string> | 否 | 参与人账号（根据account_type不同进行赋值) |
| visibility | int | 否① | 是否私密(1:公开 2：私密) |
| start_date | string | 否 | 开始时间 |
| end_date | string | 否 | 截止时间 |
| description | string | 否 | 描述 |
| work_id | string | 否 | 所属项目ID |
| okr_id | string | 否 | 关联得目标ID |
| kr_id | string | 否 | 关联得关键成果ID |

①：Visibility(是否私密)默认值：1返回结果示例

```
{
    "code": 0,
    "errorMsg": null,
    "data": {
        "objData": "300283_6674544_7_20_637201520763717781"
    }
}
```

返回结果说明

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| code | int | 状态码 |
| message | string | 错误信息 |
| data.objData | string | 任务ID |

修改任务状态https://oapi.tita.com/api/{tenant_id}/task/statusPostContent-Type  application/json请求Body

```
{
     "task_id": "111111",
     "status": 2,
}
```

参数说明

| 参数名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| task_id | string | 是 | 任务ID |
| status | int | 是 | 状态（1：进行中 2：完成 3：延迟 4：取消 6：暂停） |

返回结果示例

```
{
    "code": 0,
    "errorMsg": null
}
```

返回结果说明

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| code | int | 状态码 |
| message | string | 错误信息 |

删除任务https://oapi.tita.com/api/{tenant_id}/task/deletePostContent-Type  application/json请求Body

```
{
     "task_id": "111111"
}
```

参数说明

| 参数名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| task_id | string | 是 | 任务ID |

返回结果示例

```
{
    "code": 0,
    "errorMsg": null
}
```

返回结果说明

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| code | int | 状态码 |
| message | string | 错误信息 |

修改任务进度https://oapi.tita.com/api/{tenant_id}/task/progress/updatePostContent-Type  application/json请求Body

```
{
     "task_id": "111111",
     "progress": 20,
}
```

参数说明

| 参数名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| task_id | string | 是 | 任务ID |
| progress | decimal | 是 | 进度值 |

返回结果示例

```
{
    "code": 0,
    "errorMsg": null
}
```

返回结果说明

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| code | int | 状态码 |
| message | string | 错误信息 |

添加任务进展https://oapi.tita.com/api/{tenant_id}/task/progressDescription/addPostContent-Type  application/json请求Body

```
{
     "task_id": "111111",
     "progress_description": "完成了20%",
     "start_date": "进展的开始时间",
     "end_date": "进展的截止时间%",
}
```

参数说明

| 参数名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| task_id | string | 是 | 任务ID |
| progress_description | string | 是 | 进展内容 |
| start_date | date | 否 | 进展的开始时间 |
| end_date | date | 否 | 进展的截止时间 |

返回结果示例

```
{
    "code": 0,
    "errorMsg": null
    "data": {
        "objData": "300283_6674544_7_20_637201520763717781"
    }
}
```

返回结果说明

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| code | int | 状态码 |
| message | string | 错误信息 |
| data.objData | string | 进展ID |

添加任务量化值https://oapi.tita.com/api/{tenant_id}/task/addtargetvaluePostContent-Type  application/json请求Body

```
{
     "unit_name": "个",
     "target_value":122,
     "task_id":"xxxxxxxxx"
}
```

参数说明

| 参数名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| task_id | string | 是 | 任务ID |
| unit_name | string | 是 | 单位 |
| target_value | decimal | 是 | 目标值 |

返回结果示例

```
{
    "code": 0,
    "errorMsg": null
}
```

返回结果说明

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| code | int | 状态码 |
| message | string | 错误信息 |

修改任务量化值单位https://oapi.tita.com/api/{tenant_id}/task/updateunitPostContent-Type  application/json请求Body

```
{
     "unit_name": "个",
     "task_id":"xxxxxxxxx"
}
```

参数说明

| 参数名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| task_id | string | 是 | 任务ID |
| unit_name | string | 是 | 单位 |

返回结果示例

```
{
    "code": 0,
    "errorMsg": null
}
```

返回结果说明

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| code | int | 状态码 |
| message | string |  |

修改任务量化值https://oapi.tita.com/api/{tenant_id}/task/updatetargetvaluePostContent-Type  application/json请求Body

```
{
     "target_value": "100",
     "task_id":"xxxxxxxxx"
}
```

参数说明

| 参数名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| task_id | string | 是 | 任务ID |
| target_value | decimal | 是 | 目标值 |

返回结果示例

```
{
    "code": 0,
    "errorMsg": null
}
```

返回结果说明

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| code | int | 状态码 |
| message | string | 错误信息 |

修改任务实际值https://oapi.tita.com/api/{tenant_id}/task/updateactualvaluePostContent-Type  application/json请求Body

```
{
     "actual_value": "100",
     "task_id":"xxxxxxxxx"
}
```

参数说明

| 参数名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| task_id | string | 是 | 任务ID |
| actual_value | decimal | 是 | 实际值 |

返回结果示例

```
{
    "code": 0,
    "errorMsg": null
}
```

返回结果说明

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| code | int | 状态码 |
| message | string | 错误信息 |

修改任务评价https://oapi.tita.com/api/{tenant_id}/task/evalutePostContent-Type  application/json请求Body

```
{
     account_name = "123456789",
     account_type = 0,
     evaluate_type = 1,
     task_id = "xxxxxxx",
     value = 2,
     remark = "测试评价"
}
```

参数说明

| 参数名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| task_id | string | 是 | 任务ID |
| remark | string | 是 | 评语① |
| evaluate_type | string | 是 | 评分类型① |
| value | string | 是 | 评分① |
| account_name | string | 是 | 操作人账号（根据account_type不同进行赋值） |
| account_type | int | 否 | 账号类型 （0:手机号或邮箱 1：企业微信账号 2：钉钉账号 4：员工工号） |

①：evaluate_type   0 默认评价  remark 为必填项   value 非必填
evaluate_type   1 综合评价  value 为必填项（最大值5，代表5个小星星，每个小星星分值为2）   remark 非必填
evaluate_type   2 奖章评价  value 为必填项（最大值3， 1 太棒了! 2 干得不错! 3 再接再厉!）   remark 非必填返回结果示例

```
{
    "code": 0,
    "errorMsg": null
}
```

返回结果说明

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| code | int | 状态码 |
| message | string | 错误信息 |

获取指定时间段内创建的任务https://oapi.tita.com/api/{tenant_id}/task/searchPost请求Body

```
{
     "page_num": 1,
     "page_size": 20,
     "start_date": "2020-01-01",
     "end_date": "2020-01-30",
     "obj_ids": [123,456],
     "obj_type": 4,
     "task_ids":"593080_24419772_7_20_638065388438370841,593080_24785780_7_20_638169182048718577",
}
```

参数说明

| 参数名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| tenant_id | int | 是 | 租户标识 |
| page_num | int | 是 | 页码（默认1） |
| page_size | int | 是 | 单页数量（默认20，不能超过500） |
| start_date | string | 是 | 开始时间 |
| end_date | string | 是 | 截止时间 |
| obj_ids | List<string> | 否 | 所属对象ID(目标ID,项目ID) |
| obj_type | int | 否 | 所属对象类型（项目：4  目标：62） |
| is_getQuantifyValues | bool | 否 | 是否返回任务定量信息 |
| task_ids | string① | 否 | 任务ID（填写任务ID后，其他字段非必填） |
| is_getEvalute | bool | 否 | 是否返回任务评价信息 |

① 注：任务ID如有多个请用逗号进行分割返回结果示例

```
{
    "code": 1,
    "errorMsg": null,
    "data": {
        "total": 6946,
        "tasks": [
            {
                "relation_id": "",
                "status": 1,
                "description": "",
                "start_date": "2019/04/25 08:00:00",
                "end_date": "2019/04/25 18:00:00",
                "create_date": "2019/04/30 08:00:00",
                "visibility": 2,
                "create_user": {
                    "userId": 123456789,
                    "name": "tita",
                    "email": "tita@tita.com",
                    "mobile": "123456789",
                    "wx_userId": "",
                    "departmentName": "默认部门",
                    "staff_code": "GH000"
                },
                "principal_user": {
                    "userId": 123456789,
                    "name": "tita",
                    "email": "tita@tita.com",
                    "mobile": "123456789",
                    "wx_userId": "",
                    "departmentName": "默认部门",
                    "staff_code": "GH000"
                },
                "participators": [
                    {
                        "userId": 123456789,
                        "name": "tita",
                        "email": "tita@tita.com"
                    }
                ],
                "task_id": "593080_24419772_7_20_638065388438370841",
                "task_name": "12345",
                "progress": 0,
                "is_cycle": false,
                "modify_date": "2019/04/30 08:00:00",
                "target_value": 0.0,
                "actual_value": 0.0,
                "parent_taskId": "",
                "progress_udateDate": "2019/04/30 08:00:00",
                "is_applying": false,
                "approval_user": {
                    "userId": 123456789,
                    "name": "tita",
                    "email": "tita@tita.com",
                    "mobile": "123456789",
                    "wx_userId": "",
                    "departmentName": "默认部门",
                    "staff_code": "GH000"
                },
                "relation_works": [
                    {
                        "work_id": 105451,
                        "kr_id": 44363
                    }
                ],
                "relation_okrs": null,
                "evaluate_model": null,
                "finish_date": 2019/04/25 18:00:00,
                "estimate_hours": 1000.00,
                "worktime_hours": 660.0
            },
            {
                "relation_id": "",
                "status": 1,
                "description": "",
                "start_date": "2019/04/25 08:00:00",
                "end_date": "2019/04/25 18:00:00",
                "create_date": "2019/04/30 08:00:00",
                "visibility": 2,
                "create_user": {
                    "userId": 123456789,
                    "name": "tita",
                    "email": "tita@tita.com",
                    "mobile": "123456789",
                    "wx_userId": "",
                    "departmentName": "默认部门",
                    "staff_code": "GH000"
                },
                "principal_user": {
                    "userId": 123456789,
                    "name": "tita",
                    "email": "tita@tita.com",
                    "mobile": "123456789",
                    "wx_userId": "",
                    "departmentName": "默认部门",
                    "staff_code": "GH000"
                },
                "participators": [
                    {
                        "userId": 123456789,
                        "name": "tita",
                        "email": "tita@tita.com"
                    }
                ],
                "task_id": "593080_24785780_7_20_638169182048718577",
                "task_name": "qwey",
                "progress": 50,
                "is_cycle": false,
                "modify_date": "2019/04/30 08:00:00",
                "target_value": 100,
                "actual_value": 80,
                "progress": 50,
                "parent_taskId": "",
                "progress_udateDate": "2019/04/30 08:00:00",
                "is_applying": false,
                "approval_user": {
                    "userId": 123456789,
                    "name": "tita",
                    "email": "tita@tita.com",
                    "mobile": "123456789",
                    "wx_userId": "",
                    "departmentName": "默认部门",
                    "staff_code": "GH000"
                },
                "relation_works": [
                    {
                        "work_id": 105451,
                        "kr_id": 44363
                    }
                ],
                "relation_okrs": null,
                "evaluate_model": null,
                "finish_date": 2019/04/25 18:00:00,
                "estimate_hours": 300.00,
                "worktime_hours": 150.0
            }
        ]
    }
}
```

返回结果说明

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| code | int | 状态码 |
| message | string | 错误信息 |
| data | TaskListModel | 任务集合 |

2.TaskListModel

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| total | int | 任务条数 |
| tasks | List<TaskModel> | 任务列表 |

3.TaskModel

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| task_name | string | 任务名称 |
| task_id | string | 任务ID |
| description | string | 描述 |
| progress | int | 任务进度 |
| relation_id | string | 第三方Id |
| principal_user | UserModel | 负责人 |
| create_user | UserModel | 发起人 |
| approval_user | UserModel | 审批人 |
| participators | List<UserModel> | 参与人 |
| is_applying | bool | 是否是审批中 |
| is_cycle | bool | 是否是循环任务 |
| modify_date | string | 修改时间 |
| start_date | string | 开始时间 |
| end_date | string | 截止时间 |
| create_date | string | 创建时间 |
| status | int | 状态(1:进行中 2:完成 3:延迟 4:取消 5:未接受 6:暂停) |
| visibility | int | 是否私密(1:公开 2：私密) |
| description | string | 描述 |
| target_value | decimal | 目标值 |
| actual_value | decimal | 实际值 |
| work_id | int | 所属项目ID |
| okr_id | int | 所属目标ID |
| parent_taskId | string | 父任务ID |
| progress_udateDate | string | 进度更新时间 |
| relation_okrs | List<TaskRelationWorkInfoModel> | 任务OKR关系列表 |
| relation_works | List<TaskRelationWorkInfoModel> | 任务项目关系列表 |
| evaluate_model | List<EvaluateModel> | 任务评价列表 |
| finish_date | string | 完成时间 |
| estimate_hours | decimal | 预估工时 |
| worktime_hours | double | 实际工时 |
| tita_objId | double | 归属id |
| tita_objName | double | 归属名称 |
| tita_objType | double | 归属对象类型（4 项目  62 OKR） |
| tita_subObjId | double | 归属子对象id |
| tita_subObjName | double | 归属子对象名称 |
| priority | double | 等级 |
| progress_comment | List<ProgressModel> | 最新进展 |
| customize_fields | List<CustomizeFields> | 自定义字段 |

4.TaskRelationWorkInfoModel

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| work_id | int | 项目/OKR Id |
| kr_id | int | 里程碑/KR Id |

5.ProgressModel

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| progress_Id | string | 进展Id |
| create_user | UserModel | 创建人 |
| create_date | string | 创建时间 |
| content | string | 信息内容 |
| progress_description | string | 进展描述 |
| progress | string | 进度 |

6.EvaluateModel

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| type | int | 类型（0 默认评价 1综合评分 2 奖章评分） |
| value | int | 分值 |
| remark | string | 评分说明 |
| name | string | 综合评分/奖章评分的名称 |

7.UserModel

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| userId | int | 人员Id |
| name | string | 人员名称 |
| email | string | 邮箱 |
| mobile | string | 手机号 |
| departmentName | string | 部门名称 |
| wx_userId | string | 企业微信ID |

8.CustomizeFields

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| label | string | 字段名称 |
| text | string | 字段值 |
| name | string | 字段Key |
| value | string | 字段数据值 |

获取任务进展https://oapi.tita.com/api/{tenant_id}/task/progressDescription/getGet请求参数

| 参数名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| tenant_id | int | 是 | 租户标识 |
| task_Id | string | 是 | 任务ID |
| start_date | string | 否 | 开始时间 |
| end_date | string | 否 | 截止时间 |

-返回结果示例

```
{
    "code": 0,
    "errorMsg": null,
    "data": {
        "total": 1,
        "evolves": [
            {
                "create_user": {
                    "userId": 600003154,
                    "name": "测试人员",
                    "email": "tita@tita.com",
                    "mobile": "15622854666",
                    "wx_userId": null,
                    "departmentName": "默认部门",
                    "staff_code": "CheShi001"
                },
                "progress_description": "<p>测试任务进展接口</p>",
                "create_date": "2023/8/30 10:06:04",
                "start_date": "2023/8/30 8:00:00",
                "end_date": "2023/8/30 18:00:00"
            }
        ]
    }
}
```

返回结果说明

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| code | int | 状态码 |
| message | string | 错误信息 |
| data | TaskEvolveModel | 任务进展集合 |

2.TaskEvolveModel

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| total | int | 数量 |
| evolves | List<EvolveModel> | 进展信息 |

3.EvolveModel

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| create_user | UserModel | 进展创建人信息 |
| progress_description | string | 进展描述 |
| create_date | string | 进展创建时间 |
| start_date | string | 进展开始时间 |
| end_date | string | 进展结束时间 |
| progress_id | string | 进展标识 |

4.UserModel

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| userId | int | 人员Id |
| name | string | 人员名称 |
| email | string | 邮箱 |
| mobile | string | 手机号 |
| departmentName | string | 部门名称 |
| wx_userId | string | 企业微信ID |

获取任务工时https://oapi.tita.com/api/{tenant_id}/task/worktime/getGet请求参数

| 参数名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| tenant_id | int | 是 | 租户标识 |
| task_Id | string | 是 | 任务ID |

-返回结果示例

```
{
    "code": 0,
    "errorMsg": null,
    "data": {
        "total": 2,
        "work_Times": [
            {
                "create_user": {
                    "userId": 600003006,
                    "name": "斯洛伐克-酷酷酷",
                    "email": "",
                    "mobile": "",
                    "wx_userId": null,
                    "departmentName": "国内营销",
                    "staff_code": "Tita0001"
                },
                "description": "f阿萨德",
                "time": "2026/02/04",
                "progress_id": "600003006_11_1079_639058148181227600",
                "hours": 3.0,
                "attachments": null
            }
        ]
    }
}
```

返回结果说明

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| code | int | 状态码 |
| message | string | 错误信息 |
| data | TaskWorkTimeModel | 任务工时集合 |

2.TaskWorkTimeModel

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| total | int | 数量 |
| work_Times | List<WorkTimeModel> | 工时信息 |

3.WorkTimeModel

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| create_user | UserModel | 创建人信息 |
| description | string | 工时描述 |
| hours | decimal | 工时 |
| time | string | 时间 |
| progress_id | string | 进展标识 |

4.UserModel

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| userId | int | 人员Id |
| name | string | 人员名称 |
| email | string | 邮箱 |
| mobile | string | 手机号 |
| departmentName | string | 部门名称 |
| wx_userId | string | 企业微信ID |

添加任务附件https://oapi.tita.com/api/{tenant_id}/task/addAttachmentPost请求Body

```
{
     "task_id": "593080_24419772_7_20_638065388438370841",
     "account_type": 0,
     "account_name": "1999999999",
     "files": [
        {
            "file_name":"新建文档.doc",
            "file_type":".doc",
            "content":"aHR0cHM6Ly9vcGVuLndvc...",
        }
     ],
}
```

请求参数

| 参数名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| tenant_id | int | 是 | 租户标识 |
| task_Id | string | 是 | 任务ID |
| account_type | int | 是 | 账号类型 （0:手机号或邮箱 1：企业微信账号 2：钉钉账号） |
| account_name | string | 是 | 操作人账号（根据account_type不同进行赋值） |
| files | List<AddDocumentBase64Model> | 是 | 任务附件列表 |

2.AddDocumentBase64Model

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| file_name | string | 文件名 |
| file_type | string | 扩展名（如.doc） |
| content | string | 文件内容（base64格式） |

-返回结果示例

```
{
    "code": 0,
    "errorMsg": null,
    "data": {
        "task_id": "593080_24419772_7_20_638065388438370841",
        "task_name": "任务1",
        "files": [
            {
                "fileName": "新建文档.doc",
                "downloadUrl": "...",
                "previewUrl": "...",
            }
        ]
    }
}
```

返回结果说明

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| code | int | 状态码 |
| message | string | 错误信息 |
| data | TaskAttachmentsModel | 任务添加的附件集合 |

2.TaskAttachmentsModel

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| task_id | string | 任务ID |
| task_name | string | 任务名称 |
| files | List<FeedDocumentModel> | 添加的附件集合 |

3.FeedDocumentModel

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| fileName | string | 文档名称 |
| downloadUrl | string | 文档下载地址 |
| previewUrl | string | 文档预览地址 |

---

## 待办接口

获取待办https://oapi.tita.com/api/v1/{tenantId}/{userId}/todo?status=&pageNum=&pageSize=说明：获取消息列表，单个用户每分钟调用频次不超过20次Method Get请求参数

| 参数名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| tenantId | int | 是 | 租户标识 |
| userId | int | 是 | 用户标识 |
| status | int | 是 | 状态（1：未处理 2：已处理） |
| pageNum | int | 是 | 页码（未读状态不用传值） |
| pageSize | int | 是 | 每页数量 |

返回值

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| total | int | 数量 |
| todos | List | 待办(Todo对象)集合 |

Todo对象

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| fromUser | object | 待办发起人(UserInfo对象) |
| title | string | 标题 |
| content | string | 内容 |
| url | string | 跳转地址（先做单点登录www.italent，地址才能正常跳转） |
| status | int | 状态1：未处理 2：已处理 |
| appName | string | 产品线名称 |
| createDate | string | 创建时间 |

UserInfo

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| userId | int | 用户id |
| name | string | 用户名称 |
| email | string | 用户邮件 |

返回结构体

---

## 项目接口

创建项目https://oapi.tita.com/api/{tenant_id}/work/addPostContent-Type	application/json请求Body

```
{
     "name": "项目1",
     "account_name": "18373773171",
     "principal_account": "18373773171",
     "participant_account": ["18373773171","18373773172"],
     "visibility": 1,
     "start_date": "2020-01-01",
     "end_date": "2020-01-30",
     "description": "描述",
     "relation_id": "111",
     "work_set_id": "123456"
}
```

参数说明

| 参数名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| tenant_id | int | 是 | 租户标识 |
| name | string | 是 | 项目名称 |
| relation_id | string | 否 | 第三方ID（而可以通过该值查询或更新） |
| account_type | int | 是 | 账号类型 （0:手机号或邮箱 1：企业微信账号 2：钉钉账号） |
| account_name | string | 是 | 创建人账号（根据account_type不同进行赋值） |
| principal_account | string | 是 | 负责人账号（根据account_type不同进行赋值） |
| participant_account | List<string> | 是 | 参与人（根据account_type不同进行赋值) |
| visibility | int | 是① | 是否私密(1:公开 2：私密) |
| start_date | string | 是 | 开始时间 |
| end_date | string | 是 | 截止时间 |
| description | string | 否 | 描述 |
| work_set_id | string | 否 | 项目集Id（将项目关联到指定项目集） |

①：Visibility(是否私密)默认值：1返回结果示例

```
{
    "code": 0,
    "errorMsg": null,
    "data": {
        "objData": 2458588
    }
}
```

返回结果说明

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| code | int | 状态码 |
| message | string | 错误信息 |
| data | string | 项目标识 |

修改项目https://oapi.tita.com/api/{tenant_id}/work/updatePostContent-Type  application/json请求Body

```
{
     "work_id": 123,
     "name": "项目1",
     "account_name": "18373773171",
     "principal_account": "18373773171",
     "participant_account": ["18373773171","18373773172"],
     "start_date": "2020-01-01",
     "end_date": "2020-01-30",
     "description": "描述",
     "relation_id": "111",
     "work_set_id": "123456"
}
```

参数说明

| 参数名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| work_id | int | 是 | 项目ID |
| tenant_id | int | 是 | 租户标识 |
| name | string | 是 | 项目名称 |
| relation_id | string | 否 | 第三方ID（而可以通过该值查询或更新） |
| account_type | int | 是 | 账号类型 （0:手机号或邮箱 1：企业微信账号 2：钉钉账号） |
| account_name | string | 是 | 创建人账号（根据account_type不同进行赋值） |
| principal_account | string | 是 | 负责人账号（根据account_type不同进行赋值） |
| participant_account | List<string> | 是 | 参与人（根据account_type不同进行赋值) |
| start_date | string | 是 | 开始时间 |
| end_date | string | 是 | 截止时间 |
| description | string | 否 | 描述 |
| work_set_id | string | 否 | 项目集Id（将项目关联到指定项目集） |

返回结果示例

```
{
    "code": 0,
    "errorMsg": null,
}
```

返回结果说明

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| code | int | 状态码 |
| message | string | 错误信息 |

修改项目状态https://oapi.tita.com/api/{tenant_id}/work/statusPostContent-Type  application/json请求Body

```
{
     "work_id": 123,
     "status": 2,
}
```

参数说明

| 参数名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| work_id | int | 是 | 项目ID |
| status | int | 是 | 状态（1：进行中 2：完成 ） |

返回结果示例

```
{
    "code": 0,
    "errorMsg": null
}
```

返回结果说明

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| code | int | 状态码 |
| message | string | 错误信息 |

获取项目进展https://oapi.tita.com/api/{tenant_id}/work/progress/getPostContent-Type  application/json请求Body

```
{
    "work_id":37748,
    "relation_id":"78980"
}
```

参数说明

| 参数名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| tenant_id | int | 是 | 租户标识 |
| work_id | int | 是 | 项目ID |

返回结果示例

```
{
    "code": 0,
    "errorMsg": null,
    "data": {
        "progress": [{
            "content": "更新项目进度为 10% ,进度说明：进展描述",
            "progress_description": "进展描述",
            "old_progress": "0",
            "progress": "10",
            "create_date": "2024-04-22 15:25:55",
            "create_user": {
                "userId": 600095449,
                "name": "XXXX",
                "email": null,
                "mobile": null,
                "wx_userId": null,
                "departmentName": null,
                "staff_code": null
            }
        }, {
            "content": "更新项目进度为 20% ,进度说明：进展描述",
            "progress_description": "进展描述",
            "old_progress": "10",
            "progress": "20",
            "create_date": "2024-04-22 15:32:00",
            "create_user": {
                "userId": 600095449,
                "name": "XXXX",
                "email": null,
                "mobile": null,
                "wx_userId": null,
                "departmentName": null,
                "staff_code": null
            }
        }, {
            "content": "更新项目进度为 30% ,进度说明：进展描述",
            "progress_description": "进展描述",
            "old_progress": "20",
            "progress": "30",
            "create_date": "2024-04-22 15:32:12",
            "create_user": {
                "userId": 600095449,
                "name": "XXX",
                "email": null,
                "mobile": null,
                "wx_userId": null,
                "departmentName": null,
                "staff_code": null
            }
        }],
        "total": 0
    }
}
```

返回结果说明

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| code | int | 状态码 |
| message | string | 错误信息 |
| data | WorkProgressModelList | 项目进展集合 |

2.WorkProgressModelList

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| total | int | 项目进展条数 |
| progress | List<WorkProgressModel> | 项目进展列表 |

3.WorkProgressModel

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| content | string | 项目进展内容 |
| progress_description | string | 项目进展 |
| old_progress | string | 旧的进度 |
| progress | string | 新的进度 |
| create_date | string | 进展添加日期 |
| create_user | UserModel | 进展添加人 |

4.UserModel

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| userId | int | 人员Id |
| name | string | 人员名称 |
| email | string | 邮箱 |
| mobile | string | 手机号 |
| departmentName | string | 部门名称 |
| wx_userId | string | 企业微信ID |

修改项目进度进展https://oapi.tita.com/api/{tenant_id}/work/progress/updatePostContent-Type  application/json请求Body

```
{
     "work_id": 123,
     "progress": 20,
     "progress_description": "进展",
}
```

参数说明

| 参数名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| work_id | int | 是 | 项目ID |
| progress | decimal | 是 | 进度 |
| progress_description | string | 否 | 进展 |

返回结果示例

```
{
    "code": 0,
    "errorMsg": null
}
```

返回结果说明

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| code | int | 状态码 |
| message | string | 错误信息 |

删除项目https://oapi.tita.com/api/{tenant_id}/work/deletePostContent-Type  application/json请求Body

```
{
     "work_id": 123
}
```

参数说明

| 参数名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| work_id | int | 是 | 项目ID |

返回结果示例

```
{
    "code": 0,
    "errorMsg": null
}
```

返回结果说明

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| code | int | 状态码 |
| message | string | 错误信息 |

获取指定时间段内创建的项目https://oapi.tita.com/api/{tenant_id}/work/searchGet请求参数

| 参数名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| tenant_id | int | 是 | 租户标识 |
| page_num | int | 是 | 页码 |
| page_size | int | 是 | 单页数量 |
| start_date | string | 是 | 开始时间 |
| end_date | string | 是 | 截止时间 |

返回结果示例

```
{
    "code": 0,
    "errorMsg": null,
    "data": {
        "total": 1,
        "works": [
            {
                "relation_id": "",
                "status": 1,
                "description": "",
                "start_date": "2020/01/01 00:00:00",
                "end_date": "2020/03/31 23:59:00",
                "principal_user": {
                    "userId": 200149381,
                    "name": "",
                    "email": "",
                    "mobile": "",
                    "wx_userId": "",
                    "departmentName": "技术部"
                    },
                "participators": [{
                    "userId": 200149381,
                    "name": "",
                    "email": "",
                    "mobile": "",
                    "wx_userId": "",
                    "departmentName": "技术部"
                    }],
                "work_name": "参与部门&lt;&gt;&lt;i&gt;12345&lt;/i&gt;",
                "progress": 0
            }
        ]
    }
}
```

返回结果说明

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| code | int | 状态码 |
| message | string | 错误信息 |
| data | WorkListModel | 项目集合 |

2.WorkListModel

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| total | int | 项目条数 |
| works | List<WorkModel> | 项目列表 |

3.WorkModel

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| work_name | string | 项目名称 |
| progress | int | 进度 |
| relation_id | string | 第三方Id |
| principal_user | UserModel | 负责人 |
| start_date | string | 开始时间 |
| end_date | string | 截止时间 |
| status | int | 状态(1:进行中 2:完成 7 暂停中 8 已取消) |
| visibility | int | 是否私密(1:公开 2：私密) |
| description | string | 描述 |
| participants | List<UserModel> | 参与人 |
| followers | List<UserModel> | 关注人 |
| lable_id | int | 分类id |
| lable_name | string | 分类名称 |
| department_id | int | 所属部门id |
| department_id | string | 所属部门名称 |
| workForm_name | string | 项目类型 |
| relation_okrIds | List<string> | 关联OKRid |
| relation_taskIds | List<string> | 关联任务id |
| progress_comment | List<ProgressModel> | 最新进展 |
| customize_fields | List<CustomizeFields> | 自定义字段 |
| work_set_ids | List<string> | 所属项目集Id列表 |
| work_sets | List<WorkSetSimpleModel> | 所属项目集列表（含名称） |

4.UserModel

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| userId | int | 人员Id |
| name | string | 人员名称 |
| email | string | 邮箱 |
| mobile | string | 手机号 |
| departmentName | string | 部门名称 |
| wx_userId | string | 企业微信ID |

5.ProgressModel

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| progress_Id | string | 进展Id |
| create_user | UserModel | 创建人 |
| create_date | string | 创建时间 |
| content | string | 信息内容 |
| progress_description | string | 进展描述 |
| progress | string | 进度 |

6.CustomizeFields

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| label | string | 字段名称 |
| text | string | 字段值 |
| name | string | 字段Key |
| value | string | 字段数据值 |

7.WorkSetSimpleModel

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| work_set_id | string | 项目集Id |
| work_set_name | string | 项目集名称 |

示例

---

## 项目集接口

搜索项目集（GET方式）https://oapi.tita.com/api/{tenant_id}/workset/searchGet请求参数

| 参数名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| tenant_id | int | 是 | 租户标识 |
| page_num | int | 否 | 页码，默认1 |
| page_size | int | 否 | 每页数量，默认20，最大500 |
| work_set_id | string | 否 | 项目集Id（查询指定项目集时传入） |
| key_words | string | 否 | 搜索关键字 |

返回结果示例

```
{
    "code": 0,
    "errorMsg": null,
    "data": {
        "total": 1,
        "work_sets": [
            {
                "work_set_id": "123456",
                "work_set_name": "项目集1",
                "parent_id": null,
                "has_child": true,
                "work_count": 5,
                "user_count": 10,
                "manager_ids": [100001, 100002],
                "participator_ids": [100003, 100004],
                "created_by": 100001,
                "created_time": "2025-01-01 10:00:00",
                "modified_time": "2025-06-01 15:30:00"
            }
        ]
    }
}
```

返回结果说明

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| code | int | 状态码 |
| message | string | 错误信息 |
| data | WorkSetListModel | 项目集集合 |

2.WorkSetListModel

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| total | int | 项目集条数 |
| work_sets | List<WorkSetModel> | 项目集列表 |

3.WorkSetModel

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| work_set_id | string | 项目集Id |
| work_set_name | string | 项目集名称 |
| parent_id | string | 父级项目集Id |
| has_child | bool | 是否有子项目集 |
| work_count | int | 关联项目数量 |
| user_count | int | 人员数量（管理员+成员） |
| manager_ids | List<int> | 管理员用户Id列表 |
| participator_ids | List<int> | 成员用户Id列表 |
| created_by | int | 创建人Id |
| created_time | string | 创建时间 |
| modified_time | string | 修改时间 |

项目集关联项目（添加/移除）https://oapi.tita.com/api/{tenant_id}/workset/linkWorksPostContent-Type  application/json请求Body

```
{
    "work_set_id": "123456",
    "add_work_ids": [1001, 1002],
    "remove_work_ids": [1003]
}
```

参数说明

| 参数名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| tenant_id | int | 是 | 租户标识 |
| work_set_id | string | 是 | 项目集Id |
| add_work_ids | List<int> | 否 | 添加的项目Id列表 |
| remove_work_ids | List<int> | 否 | 移除的项目Id列表 |

返回结果示例

```
{
    "code": 0,
    "errorMsg": null
}
```

返回结果说明

| 参数名称 | 类型 | 说明 |
| --- | --- | --- |
| code | int | 状态码 |
| message | string | 错误信息 |

---

# PaaS API

## PaaS API - 概述

概述> 通用Paas接口，提供基础的CRUD操作

---

## PaaS API - PaaS接口

新增接口请求地址https://oapi.tita.com/general/api/paas/add?tenantId=?&accountType=?&deptType=?&appName=?&operatorUser=?请求url例子https://oapi.tita.com/general/api/paas/add?tenantId=10086&accountType=0&deptType=1&appName=test&operatorUser=13111111111请求方式POSTContent-TypeContent-Type application/json请求body

```
示例
[
  {
    "metaObjectCode": "Crm.Customer",
    "fields": [
      {
        "name": "PrincipalUserId",
        "value": "9638c0f3-5569-4230-a175-4562b8274c71@tita-weixin.com"
      },
      {
        "name": "Name",
        "value": "我是客户名称"
      },
      {
        "name": "Mobile",
        "value": "13112345678"
      }
    ]
  }
]
```

url地址中参数说明：

| 名称 | 类型 | 说明 | 必填 |
| --- | --- | --- | --- |
| tenantId | int | 租户id | 是 |
| accountType | int | 用户id类型（0:手机号或邮箱或姓名） | 是 |
| deptType | int | 部门id类型（0:使用tita系统部门编码  1：使用三方corpid） | 是 |
| operatorUser | string | 操作人(手机号或邮箱或姓名) | 是 |
| appName | string | 应用名称（参考页面底部说明，根据真实业务填写） | 是 |

请求body参数说明：

| 名称 | 类型 | 说明 | 必填 |
| --- | --- | --- | --- |
| metaObjectCode | string | 对象编码（参考页面底部说明，根据真实业务填写） | 是 |
| fields | 数组 | 参数集合 | 是 |

返回结果示例

```
{
    "code": 0,
    "data": db77ba6e-393e-4bcc-94df-657e8264f6d3,
    "errorMsg": "操作成功"

}
```

返回结果说明：

| 返回值 | 类型 | 说明 |
| --- | --- | --- |
| code | int | 状态码（0成功，其他值表示异常） |
| errorMsg | string | 错误信息 |

修改接口请求地址https://oapi.tita.com/general/api/paas/modify?tenantId=?&accountType=?&deptType=?&appName=?&operatorUser=?请求url例子https://oapi.tita.com/general/api/paas/modify?tenantId=10086&accountType=0&deptType=1&appName=test&operatorUser=13111111111请求方式POSTContent-TypeContent-Type application/json请求body

```
[
  {
    "metaObjectCode": "Crm.Customer",
    "id": "0a0f27f8-ab0e-4a63-a4d5-27c90fc6da47",
    "fields": [
      {
        "name": "PrincipalUserId",
        "value": "9638c0f3-5569-4230-a175-4562b8274c71@tita-weixin.com"
      },
      {
        "name": "Name",
        "value": "客户名称"
      },
      {
        "name": "Mobile",
        "value": "13112345678"
      }
    ]
  }
]
```

url地址中参数说明：

| 名称 | 类型 | 说明 | 必填 |
| --- | --- | --- | --- |
| tenantId | int | 租户id | 是 |
| accountType | int | 用户id类型（0:手机号或邮箱或姓名） | 是 |
| deptType | int | 部门id类型（0:使用tita系统部门编码  1：使用三方corpid） | 是 |
| operatorUser | string | 操作人(手机号或邮箱或姓名) | 是 |
| appName | string | 应用名称 | 是 |

请求body参数说明：

| 名称 | 类型 | 说明 | 必填 |
| --- | --- | --- | --- |
| metaObjectCode | string | 对象编码 | 是 |
| id | string | 此记录在tita系统中主键id，调用新增接口的时候会返回此id，也可通过查询接口获取 | 是 |
| fields | 数组 | 参数集合 | 是 |

返回结果示例

```
{
    "code": 0,
    "data": null,
    "errorMsg": "操作成功"

}
```

返回结果说明：

| 返回值 | 类型 | 说明 |
| --- | --- | --- |
| code | int | 状态码（0成功，其他值表示异常） |
| errorMsg | string | 错误信息 |

删除接口请求地址https://oapi.tita.com/general/api/paas/{tenantId}/delete请求url例子https://oapi.tita.com/general/api/paas/10086/delete请求方式POSTContent-TypeContent-Type application/json请求body

```
{
    "id": "c58441d8-4456-4980-b99c-f059ac34e30a",
    "metaObjectCode": "Crm.Customer",
  }
```

请求body参数说明：

| 名称 | 类型 | 说明 | 必填 |
| --- | --- | --- | --- |
| metaObjectCode | string | 对象编码 | 是 |
| id | string | 调用新增接口的时候会返回此id，也可通过查询接口获取 | 是 |

返回结果示例

```
{
    "code": 0,
    "data": null,
    "errorMsg": "操作成功"

}
```

返回结果说明：

| 返回值 | 类型 | 说明 |
| --- | --- | --- |
| code | int | 状态码（0成功，其他值表示异常） |
| errorMsg | string | 错误信息 |

查询接口请求地址https://oapi.tita.com/general/api/paas/{tenantId}/search请求url例子https://oapi.tita.com/general/api/paas/10086/search请求方式POSTContent-TypeContent-Type application/json请求body

```
{
  "pageNum":1,
  "pageSize":10,
  "items": [
    {
      "name": "name",
      "value": "张三",
      "conditionType": 1,
      "operatorType": 1
    }
  ],
  "metaObjectCode":"Crm.Customer"
  "appName":"Test"
}
```

请求body参数说明：

| 名称 | 类型 | 说明 | 必填 |
| --- | --- | --- | --- |
| pageNum | int | 第几页 | 是 |
| pageSize | int | 每页几条数据 | 是 |
| name | string | 字段名称 | 否 |
| items | object | 条件列表 | 否 |
| value | string | 字段具体值 | 否 |
| operatorType | int | 1等于 2大于等于、3小于等于、4大于、5小于、6范围、7为空、8不为空、9不等于、10开头等于、11结尾等于、12包含、14模糊 | 否 |
| conditionType | int | 1且  2或 | 否 |
| metaObjectCode | string | 对象编码 | 是 |
| appName | string | 应用名称 | 是 |

返回结果示例

```
{
    "code": 0,
    "data": [
        {
            "fields": [
                {
                    "name": "AllocationTime",
                    "value": "2024/07/10 16:48:20"
                },
                {
                    "name": "BusinessCount",
                    "value": "0"
                },
                {
                    "name": "CreatedBy",
                    "value": "600108074"
                },
                {
                    "name": "CreatedTime",
                    "value": "2024/07/10 16:43:59"
                },
                {
                    "name": "CustomerSource",
                    "value": "2"
                },
                {
                    "name": "EmployeeTotal",
                    "value": "2"
                },
                {
                    "name": "FeedId",
                    "value": "600201_4918_36_8_638562266390000000"
                },
                {
                    "name": "ImportanceNew",
                    "value": "4"
                },
                {
                    "name": "Industry",
                    "value": "5"
                },
                {
                    "name": "IsDelete",
                    "value": "False"
                },
                {
                    "name": "IsOpenPool",
                    "value": "True"
                },
                {
                    "name": "ModifiedBy",
                    "value": "10000"
                },
                {
                    "name": "ModifiedTime",
                    "value": "2024/07/11 18:12:12"
                },
                {
                    "name": "Name",
                    "value": "客户A00000001"
                },
                {
                    "name": "OldPrincipalUserId",
                    "value": "600108074"
                },
                {
                    "name": "Owner",
                    "value": "600108074"
                },
                {
                    "name": "PoolId",
                    "value": "8fd1140b-9d3d-4ddc-988a-0158bd30bb9c"
                },
                {
                    "name": "PutPoolTime",
                    "value": "2024/07/11 15:10:39"
                },
                {
                    "name": "Region",
                    "value": "12"
                },
                {
                    "name": "Stage",
                    "value": "3"
                },
                {
                    "name": "Status",
                    "value": "3"
                },
                {
                    "name": "id",
                    "value": "db77ba6e-393e-4bcc-94df-657e8264f6d3"
                }
            ]
        }
    ],
    "errorMsg": "操作成功"
}
```

返回结果说明：

| 返回值 | 类型 | 说明 |
| --- | --- | --- |
| code | int | 状态码（0成功，其他值表示异常） |
| errorMsg | string | 错误信息 |

应用名称（根据具体业务持续更新）参数说明：

| 应用名称 | 说明 |
| --- | --- |
| Test | 测试应用 |
| Sign | 签到打卡应用 |

对象列表(根据具体业务持续更新)用户对象编码：Test.User字段参数说明：

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| Name | string | 名称 |

签到对象编码：	Sign.Attendance字段参数说明：

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| FeedId | string | 动态ID |
| SignOutRemark_NRichText | string | 签退备注 |
| SignInRemark_NRichText | string | 签到备注 |
| VisitAbnormal | string | 异常类型 |
| VisitDuration | string | 拜访时长 |
| SignOutAddress | string | 签退地址 |
| SignOutTime | string | 签退时间 |
| SignInAddress | string | 签到地址 |
| SignInTime | string | 签到时间 |
| VisitState | string | 拜访状态 |
| VisitId | string | 访客计划 |
| CustomerId | string | 客户 |
| SignUserId | string | 签到人 |
| id | string | 数据id |

---

# 免登录集成(SSO)

## 免登录集成 - 证书

免登录集成适用场景接入方案对接流程图接入流程说明<font color="#dd0000">注：开发文档内所有涉及编码处均以UTF-8形式编码！！！</font>接入方可根据自己系统开发语言选择响应的[Demo/SDK](/#/sso/sdk)进行集成，也可根据文档自行实现。

```
适用于有自主研发能力的或自有系统支持适配对接的租户，在原有系统内提供免登录链接到平台的接入方案。
```

> 接口采用OIDC（OpenID Connect）方式共享登录人身份信息进行免登录接入。
> OIDC是OpenID Connect的简称。OIDC=(Identity, Authentication) + Authorization【OAuth 】 即 OIDC=身份+验证+授权。
OIDC的IDToken使用的是JWT格式（
> JWT官网
> ）
JSON Web Tokens are an open, industry standard RFC 7519 method for representing claims securely between two parties。
[JWT官网](https://jwt.io/#debugger-io)

```
A:租户申请接入平台免登录        B:平台颁发密钥证书，以邮件发送给租户
+-------------------------+     +-------------------------+        +--------------+  C:获取Demo/SDK，参考
|                         |     |                         |        |              |  示例代码集成到自有系
|           A             +----->             B           +-------->              |  统内。当点击跳转时，
|                         |     |                         |        |              |  使用平台颁发的密钥证书
+-------------------------+     +-------------------------+        |              |  签算IDToken并按照规则
                                                                   |              |  拼接重定向地址到平台
                                                                   |              |  SSO服务接口。
                                                                   |              |  url 示例：
+-------------------------+                                        |              |  https://oapi.tita.com/
|                         |                                        |       C      |  SSO/AuthCenter?idtoken=
|          Success        <--True--+-----Validate IDtoken----------+              |  id_token_url_safe_base64
|                         |        |                               |              |  _string&return_url=目标
+-------------------------+        |                               |              |  详情地址，需url encode。
                                   |                               |              |
+-------------------------+        |                               |              |
|                         |        |                               |              |
|          Failure        <--False-+                               |              |
|                         |                                        |              |
+-------------------------+                                        +--------------+
SSO 服务接口得到IDToken 进行验签，如果验签成功会设置登录状态，并转向待访问详情页面
IDToken 进行验签失败返回登录错误提示页面。
```

```
1、租户申请使用SSO免登录接口服务，获得由Tita颁发的、用于生成OIDC签算所使用的密钥证书，流程可以咨询产品顾问。

2、获取由平台提供的x509 证书密钥对。
3、下载Demo/SDK，参考demo集成SDK到系统，签算IDToken
4、得到用于登录的 IDToken，并拼接完整的请求URL，使用HTTP 302方式转向到生成好的链接地址即可(文档末附Demo/SDK下载地址)。
```

---

## 免登录集成 - Demo/SDK

Demo/SDK获取及使用说明（可联系销售顾问）当前提供两种语言版本的SDK下载  有关编码一律使用UTF-8！！！！Demo/SDK 目录结构/说明<font color="#dd0000">注：示例代码为通用代码，免登录集成只使用以下目录结构部分    </font>Asp.Net 示例代码及SDK结构说明Java 示例代码项目/SDK结构及说明<font color="#dd0000">注：开发文档内所有涉及编码处均以UTF-8形式编码！！！</font>

```
JAVA版本
Demo 基于SpringBoot 2 + Java 8 
SDK Java 6+版本

ASP.NET版本
.NET Framework 4.5+
.NET MVC 5

下载SDK后 .NET 需使用Nuget还原依赖编译成功后运行，JAVA版本使用Maven下载依赖包。
运行Demo 在浏览器访问demo站点，可看到【id_token生成】导航，点击后可查看生成所需相关参数/描述信息，具体SDK调用代码可设置断点自行跟踪查看。
项目结构在本页末尾，免登录集成部分只需使用id_token生成、id_token验证、使用id_token登录其他系统三个示例。
开发者应 查阅如何生成id_token，并集成该部分代码到自有系统内，生成Token后到demo中验证，成功后可按照id_token登录其他系统页面示例方式拼接登录URL供用户登录平台。
```

```
ROOT   Demo/SDK运行需安装MVC5.0+/.NET Framework4.5+版本
│  Beisen.OIDC.Demo.sln                      解决方案文件
│              
├─Beisen.OIDC.Demo                           示例项目
│  │  AppConst.cs                            常量 
│  │  packages.config                        Nuget配置文件，引用依赖
│  │       
│  ├─Controllers                             控制器
│  │      HomeController.cs                  示例控制器，Token签署/SDK调用逻辑
│  │      
│  └─Views
│      └─Home
│              GenerateOpenId.cshtml         签署Token示例页面
│              LoginTo.cshtml                拼装登录请求示例页面
│              ValidationOpenId.cshtml       验证Token有效性示例页面
│              
├─Beisen.OIDC.SDK                            SDK项目，可直接编译后引用或迁移代码到自有项目内
│  │  BeisenTokenProvider.cs                 生成TDToken使用的代码逻辑
│  │  packages.config                        Nuget项目依赖包配置
│  │  
│  ├─General                                 扩展/签名/加密等通用算法
│  │          
│  └─Model                                   业务实体定义 JWT相关
│      │  
│      └─Constant                            常量定义
└─packages                                   Nuget还原依赖包位置
```

```
ROOT    项目基于 Spring Boot2.0 /Java 8+ 版本编写，构建依赖Maven SDK最低使用版本 JAVA 6.0+测试通过
   │  pom.xml                                           Maven依赖配置
   │          
   └─src
        ├─java
        │  └─com
        │      └─beisen
        │          ├─demo
        │          │  │      
        │          │  └─web
        │          │          HomeController.java        控制器，Token签算/SDK调用逻辑
        │          │          
        │          └─oidcsdk                             SDK代码
        │              ├─crypto                          加密算法
        │              │      Crypto.java
        │              │      RC4.java
        │              │      
        │              ├─models                          JWT实体定义
        │              │      
        │              ├─provider
        │              │      BeisenTokenProvider.java   Token签算逻辑
        │              │      
        │              └─utility
        │                      SafeTools.java            自定义工具包
        │                      
        └─resources
            └─templates
                    GenerateOpenId.html                  签算Token页面模板
                    LoginTo.html                         拼装请求页面模板
                    ValidationOpenId.html                验签Token页面模板
```

---

## 免登录集成 - 接口文档

SSO集成开发文档接口地址请求方式参数示例参数说明上述参数咨询Tita售后同学，提供接收秘钥的邮件号，并告知获取密钥证书为单点。申请成功后，会将秘钥和其他需要的参数通过邮件发送给您，售后反馈后请注意查收IDToken 生成方式<font color="#dd0000">注：开发文档内所有涉及编码处均以UTF-8形式编码！！！</font>

```
https://oapi.tita.com/SSO/AuthCenter
```

```
HTTP GET
```

```
https://oapi.tita.com/SSO/AuthCenter?id_token=eyJhbGciOiJSUzI1NiIsImtpZCI6IjFCM0I1ODFCNkNFMkI0MTBEQTk2RTEwRTlCRjFFMTAzNkIxNTdCM0Q3ODMwNkNFNDg3RENBNzI1NTFFNDY1MkYifQ.eyJpc3MiOiJvYS55b3VyLXdlYnNpdGUuY29tIiwic3ViIjoiemhhbmdzYW5AcHAuY29tIiwiYXVkIjoiMjM0NTkzIiwiZXhwIjoxNTMyNTIyNDk3LCJpYXQiOjE1MzI1MjE1OTcsImNscyI6eyJhcHBpZCI6IjEwMCIsInV0eSI6ImVtYWlsIiwidXJsX3R5cGUiOiIwIiwiaXN2X3R5cGUiOiIwIn19.PZTjsQEhfp09yMKl6Q5jXm5pKFB3Y1o9QRLecWBn3VgidabJxzfPiOEfUxQE9d2cg2XTI9c-iZoxyJQ7RHL1uQ133jTZ6JPTPjeEtVY_ClTulmgycuvb0ARDajR8AYSm6M5aNZrK89QIdHuQfta3-XYQCwMIfzwgbQlK3m83S_7VVY_tE-P0e7oldyePOvQiUZWPSPKQgPIywmDUuA_uLktVTGOMLC-d30tBweJ-nFSwVqO2P-1RwvthWfML73C76ZaNoOIPN2SwseEVgYLnvgGnbdQ0ollFQeS71-2Vn_CrWV1P-kKP-rklJcw_o3p6A5Z0LOBlASJPonMbZectlQ&return_url=http%3A%2F%2Foapi.tita.com%2F
```

| 参数名称 | 字段类型 | 必填项目 | 字段涵义 |
| --- | --- | --- | --- |
| return_url | string | 否 | 需查看的目标详情页面地址，为空时默认访问应用主页（需urlencode） |
| id_token | string | 是 | 使用Tita颁发的2048位X509密钥证书生成的OIDC IDToken |

```
拼装JWT ： JWT官方网站 https://jwt.io/#debugger-io
HEADER 部分示例：
{
 "alg": "RS256",
 "kid": "1B3B581B6CE2B410DA96E10E9BF1E1036B157B3D78306CE487DCA72551E4652F"
}
字段说明:
参数名称  字段类型 必填项目  字段涵义 
alg      string   是       固定值RS256，JWT的签算方式
kid      string   是       签算使用私钥对应公钥的SHA256HASH值（计算时需取公钥证书内完整内容去掉\r\
字表符）  

PAYLOAD部分示例：

{
    "iss": "oa.your-website.com",
    "sub": "zhangsan@pp.com",
    "aud": "234593",
    "exp": 1532526388,
    "iat": 1532525488,
    "cls": {
        "appid": "100",
        "uty": "email",
        "url_type": "0",
        "isv_type": "0"
    }
}
字段说明  
参数名称  字段类型 必填项目 字段涵义 
 iss      string  是        接入方站点domian，无需协议头/端口号/path/hash等其他信息 
 sub      string  是        用户在Tita的唯一标识email/id 
 aud      string  是        租户id  
 exp      long    是        过期时间，Unix Time  
 iat      long    是        生成时间，Unix Time   
 cls      json    是        用户自定义扩展信息 json 
 appid    string  是        需登录应用ID 【appid=1】 
 uty      string  是        sub传递用户标识类型，当sub内使用用户邮箱时uty=email否则uty=id  
 url_type string  是        访问的目标地址类型，url_type=0 PC端站点 url_type=2 移动端站点  
 isv_type string  是        固定值，isv_type=0 

SIGNATURE部分示例说明： 使用标准的RSASHA512算法签名，签名内容为header与payload进行base64编码后，使用引文句号分割链接的字符串。
RSASHA512( base64UrlEncode(header) + "." +  base64UrlEncode(payload),  Tita颁发的密钥证书内完整的字符串信息且无需加工格式)；
JWT 标准是使用base64编码，由于Tita场景要求，故使用urlsafebase64编码，请开发时注意。
最终结果 :
URLSAFEBASE64Encode（header）+ "." + URLSAFEBASE64Encode（payload）+ "."+  URLSAFEBASE64Encode（SIGNATURE）
示例：
eyJhbGciOiJSUzI1NiIsImtpZCI6IjFCM0I1ODFCNkNFMkI0MTBEQTk2RTEwRTlCRjFFMTAzNkIxNTdCM0Q3ODMwNkNFNDg3RENBNzI1NTFFNDY1MkYifQ.eyJpc3MiOiJvYS55b3VyLXdlYnNpdGUuY29tIiwic3ViIjoiemhhbmdzYW5AcHAuY29tIiwiYXVkIjoiMjM0NTkzIiwiZXhwIjoxNTMyNTI2Mzg4LCJpYXQiOjE1MzI1MjU0ODgsImNscyI6eyJhcHBpZCI6IjEwMCIsInV0eSI6ImVtYWlsIiwidXJsX3R5cGUiOiIwIiwiaXN2X3R5cGUiOiIwIn19.CcF05ZhskoPAhsEWsXhz4hyWnVD5Jx3yFLZssRMw_3XX9rLLjNKeP-vGblgCkOsSAWxZzZ0B-Cp2skJdt4-p2czmBNqQLjiLlhLzo0oAK4TDkAnSjCHJ7lWrT8Su7ZdxNUx1uTegMsP2mNWSmXK1uPN_l6msWG4PuiemadGaIqBUxg37PVX7pTCHstPMLXi3AalRK23OvgOMtqresm5l5DdrrztkYTs6ZS4LZef6X2OoAPPSxYT0bST4m1SOedaa13daTN58jni88Tx4m0_wr_PBmd1Tr_hjqh-T5-Oz2_2AtLqXvLwWICiGkEGC5eFlcVUuI9jPDVPkOcpwjzujYw
```

---

# 基础说明

## 获取授权

接入流程获取AccessTokenAccessToken是企业应用访问相应公司数据的全局唯一票据AccessToken分为租户级和用户级,根据业务场景选择。正常情况下企业需要保存AccessToken信息，不要频繁申请AccessToken,在快过期或者过期后在重新获取Step1 申请密钥申请密钥Secret，用于获取授权令牌AccesTokenStep2 获取授权令牌AccesToken请求地址https://oapi.tita.com/OAuth/Token请求方式POSTContent-Typeapplication/x-www-form-urlencoded请求body> 租户级(Body)
> tenant_id=&grant_type=client_credentials&secret=&app_id=1
参数说明：

| 名称 | 类型 | 说明 | 必填 |
| --- | --- | --- | --- |
| tenant_id | int | 租户ID | 是 |
| grant_type | string | 授权类型 | 是 |
| secret | string | 申请的secret | 是 |
| app_id | int | app标识 | 是 |

响应报文> {"access_token":"","expires_in":"","tenant_id":"","user_id":""}
参数说明：

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| access_token | string | token |
| expires_in | int | 过期时间（秒） |
| tenant_id | int | 租户ID |
| user_id | int | 用户ID |

Step3 访问接口在请求报文头中新加Authorization，值为Bearer+空格+access_token例如：> Connection: keep-alive
> Accept-Encoding: gzip, deflate, sdch
> Accept-Language: zh-CN,zh;q=0.8
> Authorization: Bearer O-bb46_JZaiAzf4RyACluK-1JoESigRnRKHsvvslSSE61yaK-chWKA

---

## 服务端 - 首页

接入流程获取AccessTokenAccessToken是企业应用访问相应公司数据的全局唯一票据AccessToken分为租户级和用户级,根据业务场景选择。正常情况下企业需要保存AccessToken信息，不要频繁申请AccessToken,在快过期或者过期后在重新获取Step1 申请密钥申请密钥Secret，用于获取授权令牌AccesTokenStep2 获取授权令牌AccesToken请求地址https://oapi.tita.com/OAuth/Token请求方式POSTContent-Typeapplication/x-www-form-urlencoded请求body> 租户级(Body)
> tenant_id=&grant_type=client_credentials&secret=&app_id=1
参数说明：

| 名称 | 类型 | 说明 | 必填 |
| --- | --- | --- | --- |
| tenant_id | int | 租户ID | 是 |
| grant_type | string | 授权类型 | 是 |
| secret | string | 申请的secret | 是 |
| app_id | int | app标识 | 是 |

响应报文> {"access_token":"5N3w5J5_oTjVXQrIQ0Y1MfG-qQ9S6waDUtBGeqJ-DVBgNs41QqOCsQ","expires_in":"1479202744","tenant_id":"204402","user_id":"0"}
参数说明：

| 名称 | 类型 | 说明 |
| --- | --- | --- |
| access_token | string | token |
| expires_in | int | 过期时间（秒） |
| tenant_id | int | 租户ID |
| user_id | int | 用户ID |

Step3 访问接口在请求报文头中新加Authorization，值为Bearer+空格+access_token例如：> Connection: keep-alive
> Accept-Encoding: gzip, deflate, sdch
> Accept-Language: zh-CN,zh;q=0.8
> Authorization: Bearer O-bb46_JZaiAzf4RyACluK-1JoESigRnRKHsvvslSSE61yaK-chWKA

---

## 服务端 - SSO

概述企业内部系统(移动端app)单点登录到Italent的pc端(移动端)。方式1：签名方式Step1 申请AppKey做签名认证使用,用于签名Step2 请求地址地址：https://oapi.tita.com/v2/sso/sign?tenant_id=&user_id=&time_stamp=&sign=&sign_type=2&url_type=请求方式：Get

| 参数名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| tenant_id | int | 是 | 租户标识 |
| user_id | int | 是 | 用户标识 |
| time_stamp | long | 是 | 签名时间戳(60秒) |
| sign_type | int | 是 | 默认是2 |
| sign | string | 是 | 签名内容（tenant_id+user_id+AppKey+time_stamp+sign_type 利用md5 算法生成） |
| url_type | int | 否 | 0：pc端首页 2：移动端首页 |
| return_url | string | 否 | 不为空则跳转到return_url定义地址，否则根据url_type跳转 |

方式2：AccessToken认证Step1 换取换取AccessToken具体方式参考 建立连接Step2地址：https://oapi.tita.com/v2/sso/token?access_token=&url_type=请求方式：Get

| 参数名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| access_token | string | 是 | AccessToken |
| url_type | int | 是 | 0：pc端首页 2：移动端首页 |
| return_url | string | 否 | 不为空则跳转到return_url定义地址，否则根据url_type跳转 |

---

