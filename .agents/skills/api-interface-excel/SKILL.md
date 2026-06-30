---
name: api-interface-excel
description: 按规范格式生成接口梳理Excel文档（总览表+子表），适用于MES/ERP数据梳理场景
---

# API接口梳理Excel模板 Skill

## 适用场景
当你需要将API接口梳理输出为结构化Excel文档时使用。生成一个包含**总览表 + 多个子表**的规范格式Excel文件。

## 输出规范

### 文件结构
- **1个总览表**（接口总览）：汇总所有接口清单，按分类分组
- **N个子表**：每个接口一个子表，包含该接口的完整信息

---

## 色彩体系（openpyxl PatternFill）

所有单元格必须显式设置 fill，**禁止** patternType=None（透明/无背景）：

| 色号 | 用途 | start_color / end_color |
|---|---|---|
| 深蓝 | 表头行（总览表 + 子表列标题） | `1F4E79` |
| 浅蓝 | 分类标题行（总览表 ▸ 行）、子表分区标题（请求参数/响应数据字段） | `D6E4F0` |
| 白色 | 子表基本信息区、数据行根级字段 | `FFFFFF` |
| 浅灰 | 总览表数据行 | `F2F2F2` |
| 嵌套L1 | 子表响应数据字段：一级嵌套（2空格缩进） | `F4F7FC` |
| 嵌套L2 | 子表响应数据字段：二级嵌套（4空格缩进） | `EBEFF7` |

### 嵌套层级背景规则

子表「响应数据字段」区的字段按缩进深度着色：
- **0 级**（无缩进，如 `result`、`data`）：白色 `FFFFFF`
- **1 级**（2 空格 `  xxx`，如 `  poXkNo`）：极淡蓝灰 `F4F7FC`
- **2 级**（4 空格 `    xxx`，如 `    lineNo`）：淡蓝灰 `EBEFF7`

请求参数区不使用嵌套背景（全部白色）。

---

## 总览表（接口总览）规范

| 列 | 宽度 | 内容 | 水平对齐 |
|---|---|---|---|
| A | 10 | 分类内序号（1,2,1,2...） | center |
| B | 36 | 接口名称 | left |
| C | 60 | 接口地址 | left |
| D | 12 | 请求方式（POST/GET） | center |
| E | 50 | 接口描述 | left |

### 逐行样式

| 行 | 合并 | 填充 | 字体 | 水平对齐 |
|---|---|---|---|---|
| 标题行 (Row 1) | A1:E1 | 无填充（可设白色） | 微软雅黑 14pt bold | center |
| 表头行 (Row 2) | 无合并 | `1F4E79` 深蓝 | 微软雅黑 10pt bold 白色 | center |
| 分类行 (`▸ xxx`) | A~E 合并 | `D6E4F0` 浅蓝 | 微软雅黑 11pt bold | **left** |
| 数据行 | 无合并 | `F2F2F2` 浅灰 | 微软雅黑 10pt | A/D=center, B/C/E=left |

- 分类行之后紧接该分类的数据行
- 分类行不占序号，序号列留空
- 行高：标题 30pt，表头 22pt，分类行 22pt，数据行 **不设固定高度**（自适应）

---

## 子表规范

### 列宽
| 列 | 宽度 |
|---|---|
| A（字段名/参数名） | 28 |
| B（说明） | 52 |
| C（是否必须/空） | 14 |
| D（数据类型） | 20 |

### 基本信息区（Row 1-3）

| 行 | A 列 | B~D 列（合并） | 填充 |
|---|---|---|---|
| 1 | **接口地址**（bold） | API URL | `FFFFFF` |
| 2 | **请求方式**（bold） | POST/GET | `FFFFFF` |
| 3 | **接口描述**（bold） | 功能说明 | `FFFFFF` |

- A 列：微软雅黑 10pt bold，水平 left
- B~D 合并：微软雅黑 10pt，水平 left
- 所有单元格 border=thin，垂直居中，wrap_text=True
- 行高：**不设固定高度**（自适应）

### 空行分隔 (Row 4)
- 行高 6pt，无边框，无填充
- ⚠️ 空行单元格也需要设置 fill=`FFFFFF`（避免透明）

### 请求参数区

| 行类型 | 合并 | 填充 | 字体 |
|---|---|---|---|
| 标题行 `请求参数` | A~D 合并 | `D6E4F0` | 11pt bold |
| 表头行（参数名称/参数说明/是否必须/数据类型） | 无 | `1F4E79` | 10pt bold 白色 |
| 数据行 | 无 | **`FFFFFF`** | 10pt |

- 标题行：水平 left
- 表头行：全部 center
- 数据行：A/B=left，C/D=center
- **数据行不设固定行高**（自适应）
- 无参数时合并 A~D 显示"（该接口无业务请求参数）"
- 行高：标题/表头=22pt，数据行=自适应

### 空行分隔（请求参数与响应字段之间）
- 行高 6pt，无边框，白色填充

### 响应数据字段区

| 行类型 | 合并 | 填充 | 字体 |
|---|---|---|---|
| 标题行 `响应数据字段` | A~D 合并 | `D6E4F0` | 11pt bold |
| 表头行（字段名称/字段说明/空/数据类型） | 无 | `1F4E79` | 10pt bold 白色 |
| 数据行（根级，无缩进） | 无 | **`FFFFFF`** | 10pt |
| 数据行（一级嵌套，2空格） | 无 | **`F4F7FC`** | 10pt |
| 数据行（二级嵌套，4空格） | 无 | **`EBEFF7`** | 10pt |

- 标题行：水平 left
- 表头行：全部 center
- 数据行：A/B=left，C/D=center
- **数据行不设固定行高**（自适应）
- 使用 `row_dimensions.group()` 添加 Excel 分组折叠（可选）
- B 列（字段说明）内容可能较长，列宽 52 + wrap_text 配合自适应行高

---

## 对齐规范速查表

| 位置 | A 列 | B 列 | C 列 | D 列 | E 列 |
|---|---|---|---|---|---|
| 总览表-表头 | center | center | center | center | center |
| 总览表-分类行 | **left** | —（合并） | — | — | — |
| 总览表-数据行 | center | left | left | center | left |
| 子表-基本信息标签 | left | — | — | — | — |
| 子表-基本信息值 | — | left（合并B:D） | — | — | — |
| 子表-分区标题 | **left** | —（合并） | — | — | — |
| 子表-数据表头 | center | center | center | center | — |
| 子表-请求参数数据 | left | left | center | center | — |
| 子表-响应字段数据 | left | left | center | center | — |

---

## 行高策略

| 行类型 | 高度 | 说明 |
|---|---|---|
| 总览标题 | 30pt | 固定 |
| 总览表头 | 22pt | 固定 |
| 总览分类行 | 22pt | 固定 |
| 总览数据行 | **不设（auto）** | 自适应，配合 wrap_text |
| 子表基本信息 | **不设（auto）** | 自适应 |
| 子表分区标题 | 22pt | 固定 |
| 子表数据表头 | 22pt | 固定 |
| 子表数据行 | **不设（auto）** | 自适应——这是关键！不能固定 20pt |
| 分隔空行 | 6pt | 固定 |

**重要**：数据行要配合 `wrap_text=True` + 不设固定高度，由 Excel 根据内容自动撑开。

---

## 统一常量定义（openpyxl 代码模板）

```python
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side

# ── Fills ──
DEEP_BLUE   = PatternFill(start_color='1F4E79', end_color='1F4E79', fill_type='solid')
LIGHT_BLUE  = PatternFill(start_color='D6E4F0', end_color='D6E4F0', fill_type='solid')
WHITE_FILL  = PatternFill(start_color='FFFFFF', end_color='FFFFFF', fill_type='solid')   # ← 必须显式设置！
LIGHT_GRAY  = PatternFill(start_color='F2F2F2', end_color='F2F2F2', fill_type='solid')
NEST_L1     = PatternFill(start_color='F4F7FC', end_color='F4F7FC', fill_type='solid')   # 一级嵌套
NEST_L2     = PatternFill(start_color='EBEFF7', end_color='EBEFF7', fill_type='solid')   # 二级嵌套

# ── Fonts ──
WHITE_BOLD  = Font(name='微软雅黑', size=10, bold=True, color='FFFFFF')
BOLD_10     = Font(name='微软雅黑', size=10, bold=True)
BOLD_11     = Font(name='微软雅黑', size=11, bold=True)
NORMAL_10   = Font(name='微软雅黑', size=10)
TITLE_14    = Font(name='微软雅黑', size=14, bold=True)

# ── Border ──
THIN_BORDER = Border(
    left=Side(style='thin', color='B0B0B0'),
    right=Side(style='thin', color='B0B0B0'),
    top=Side(style='thin', color='B0B0B0'),
    bottom=Side(style='thin', color='B0B0B0'),
)

# ── Alignments ──
ALIGN_LEFT   = Alignment(horizontal='left',   vertical='center', wrap_text=True)
ALIGN_CENTER = Alignment(horizontal='center', vertical='center', wrap_text=True)
# 合并单元格用（标题行水平未指定时）
ALIGN_VCENTER = Alignment(vertical='center', wrap_text=True)

# ── Column Widths ──
SUB_COL_WIDTHS  = {'A': 28, 'B': 52, 'C': 14, 'D': 20}
OV_COL_WIDTHS   = {'A': 10, 'B': 36, 'C': 60, 'D': 12, 'E': 50}
```

---

## 生成后验证清单

生成 Excel 后必须逐项检查：

- [ ] 总览表标题行 row 1：有 title，center 对齐，14pt bold
- [ ] 总览表表头 row 2：深蓝底 + 白字 + center
- [ ] 总览表分类行：浅蓝底 + left 对齐 + 11pt bold
- [ ] 总览表数据行：浅灰底 + A/D=center B/C/E=left
- [ ] 子表基本信息区：白色底 `FFFFFF` solid（**不是 None/透明**）
- [ ] 子表分区标题（请求参数/响应数据字段）：浅蓝底 + left 对齐
- [ ] 子表数据表头：深蓝底 + 白字 + center
- [ ] 子表请求参数数据行：白色底 + A/B=left C/D=center
- [ ] 子表响应字段嵌套行：L1=`F4F7FC`，L2=`EBEFF7`
- [ ] 所有数据行：**未设**固定高度（让 Excel 自适应）
- [ ] 所有非空单元格 border=thin
- [ ] 所有单元格 wrap_text=True

---

## 编号规则
- sheet标签名使用**分类内编号**：如 `1.企业物料供应商...` / `2.根据物料编码...`
- 总览表A列的序号与sheet标签保持一致
- 总览表的分类标题行（▸）不占用序号
- 同一分类下接口按 1, 2, 3... 从 1 重新编号

## Excel文件输出路径
输出到 `docs/数据梳理/{系统名}/梳理后/` 目录下。

## 处理步骤
1. 探查目标系统所有接口清单（来源可以是代码、API文档、需求文档）
2. 按业务模块对接口进行分组分类
3. 为每个接口创建子表，填写基本信息、请求参数、响应数据字段
4. 创建接口总览表汇总所有接口
5. 应用统一样式（列宽、字体、颜色、边框、合并单元格）——**参照本 SKILL.md 色彩体系和对齐规范**
6. 写入后对照「生成后验证清单」全量检查
