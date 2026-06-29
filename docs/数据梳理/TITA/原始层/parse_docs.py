"""
TITA API Documentation Parser v7 - Handles both single and double quoted _v()
+ bracket-depth tracking for tables and code blocks.
"""

import re, os

def unescape(s):
    s = s.replace('\\n', '\n').replace('\\t', '\t')
    s = s.replace('\\"', '"').replace("\\'", "'")
    s = s.replace('\\\\', '\\')
    s = s.replace('\\x3e', '>').replace('\\x3c', '<')
    return re.sub(r'\\u([0-9a-fA-F]{4})', lambda m: chr(int(m.group(1), 16)), s)


def extract_v_text(js_snippet):
    """Extract text from all _v("...") and _v('...') in a snippet."""
    texts = []
    for m in re.finditer(r"""\w\._v\("((?:[^"\\]|\\.)*)"\)""", js_snippet):
        texts.append(unescape(m.group(1)))
    for m in re.finditer(r"""\w\._v\('((?:[^'\\]|\\.)*)'\)""", js_snippet):
        texts.append(unescape(m.group(1)))
    return texts


def find_block_end(text, start, open_char, close_char):
    """Find matching close for block starting at `start`. Depth already at 1."""
    depth = 0
    i = start
    while i < len(text):
        c = text[i]
        if c == open_char:
            depth += 1
        elif c == close_char:
            depth -= 1
            if depth < 0:
                return i
        i += 1
    return i


def process_chunk(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()
    
    elements = []  # (start, end, kind, value)
    
    # ---- HEADINGS: _(“hN”,[X._v(“text”)]) ----
    for m in re.finditer(
        r'\w\("(h[1-6])",\s*\[\w\._v\("((?:[^"\\]|\\.)*)"\)\]\)\)',
        text
    ):
        elements.append((m.start(), m.end(), 'heading',
                        (int(m.group(1)[1]), unescape(m.group(2)))))
    
    # ---- CODE BLOCKS (pre>code): find via depth tracking ----
    for m in re.finditer(r'\w\("pre"', text):
        start_pos = m.end()  # position right after tag name, before attrs
        end = find_block_end(text, start_pos, '(', ')')
        block_text = text[m.start():end+1]
        v_texts = extract_v_text(block_text)
        if v_texts:
            elements.append((m.start(), end+1, 'code', '\n'.join(v_texts)))
    
    # ---- TABLES: find via depth tracking ----
    for m in re.finditer(r'\w\("table",\s*\[', text):
        end = find_block_end(text, m.end(), '[', ']')
        # Now one more ) for n( close
        if end+1 < len(text) and text[end+1] == ')':
            end += 1
        table_text = text[m.start():end+1]
        rows = []
        # Find tr blocks using depth tracking (tr contains nested td elements)
        for tr_m in re.finditer(r'\w\("tr",\s*\[', table_text):
            tr_end = find_block_end(table_text, tr_m.end(), '[', ']')
            # n() closes with one more )
            if tr_end+1 < len(table_text) and table_text[tr_end+1] == ')':
                tr_end += 1
            tr_block = table_text[tr_m.start():tr_end+1]
            cells = []
            # Find td/th blocks using depth tracking
            for cell_m in re.finditer(r'\w\("t[hd]",\s*\[', tr_block):
                cell_end = find_block_end(tr_block, cell_m.end(), '[', ']')
                if cell_end+1 < len(tr_block) and tr_block[cell_end+1] == ')':
                    cell_end += 1
                cell_block = tr_block[cell_m.start():cell_end+1]
                cell_text = ''.join(extract_v_text(cell_block))
                cells.append(cell_text.strip())
            if cells:
                rows.append(cells)
        if rows:
            elements.append((m.start(), end+1, 'table', rows))
    
    # ---- PARAGRAPHS ----
    for m in re.finditer(
        r'\w\("p",\s*\[\w\._v\("((?:[^"\\]|\\.)*)"\)\]\)\)',
        text
    ):
        content = unescape(m.group(1)).strip()
        if content:
            elements.append((m.start(), m.end(), 'para', content))
    
    # ---- BLOCKQUOTES ----
    for m in re.finditer(r'\w\("blockquote"', text):
        end = find_block_end(text, m.end(), '(', ')')
        bq_text = text[m.start():end+1]
        bq_parts = [t.strip() for t in extract_v_text(bq_text) if t.strip()]
        if bq_parts:
            elements.append((m.start(), end+1, 'blockquote', bq_parts))
    
    # ---- HR ----
    for m in re.finditer(r'\w\("hr"\)\)\)', text):
        elements.append((m.start(), m.end(), 'hr', None))
    
    # ---- BR ----
    for m in re.finditer(r'\w\("br"\)\)\)', text):
        elements.append((m.start(), m.end(), 'br', None))
    
    # ---- LINKS ----
    for m in re.finditer(
        r'\w\("a",\{attrs:\{href:"([^"]*)"\}\},\[\w\._v\("((?:[^"\\]|\\.)*)"\)\]\)',
        text
    ):
        elements.append((m.start(), m.end(), 'link',
                        (unescape(m.group(2)), m.group(1))))
    
    # ---- FONT with color ----
    for m in re.finditer(
        r'\w\("font",\{attrs:\{color:"([^"]*)"\}\},\[\w\._v\("((?:[^"\\]|\\.)*)"\)\]\)',
        text
    ):
        elements.append((m.start(), m.end(), 'font',
                        (m.group(1), unescape(m.group(2)))))
    
    # ---- EM ----
    for m in re.finditer(
        r'\w\("em",\s*\[\w\._v\("((?:[^"\\]|\\.)*)"\)\]\)',
        text
    ):
        elements.append((m.start(), m.end(), 'em', unescape(m.group(1))))
    
    # ---- STRONG ----
    for m in re.finditer(
        r'\w\("strong",\s*\[\w\._v\("((?:[^"\\]|\\.)*)"\)\]\)',
        text
    ):
        elements.append((m.start(), m.end(), 'strong', unescape(m.group(1))))
    
    # ---- INLINE CODE ----
    for m in re.finditer(
        r'\w\("code",\{[^}]*?\},\[\w\._v\("((?:[^"\\]|\\.)*)"\)\]\)',
        text
    ):
        elements.append((m.start(), m.end(), 'icode', unescape(m.group(1))))
    
    # ---- Exclusion zones ----
    exclude = sorted([(s, e) for s, e, k, v in elements])
    def excluded(pos):
        for s, e in exclude:
            if s <= pos < e: return True
        return False
    
    # ---- Standalone _v() text ----
    for m in re.finditer(r"""\w\._v\("((?:[^"\\]|\\.)*)"\)""", text):
        if not excluded(m.start()):
            content = unescape(m.group(1)).strip()
            if content and content != ' ':
                elements.append((m.start(), m.end(), 'text', content))
    
    elements.sort(key=lambda x: x[0])
    
    # ---- Render to markdown ----
    lines = []
    for start, end, kind, value in elements:
        if kind == 'heading':
            lines.append('\n\n' + '#' * value[0] + ' ' + value[1] + '\n')
        elif kind == 'code':
            lines.append('\n\n```\n' + value.strip() + '\n```\n\n')
        elif kind == 'table':
            rows = value
            if rows:
                md = '| ' + ' | '.join(rows[0]) + ' |\n'
                md += '| ' + ' | '.join(['---'] * len(rows[0])) + ' |\n'
                for row in rows[1:]:
                    padded = row + [''] * (len(rows[0]) - len(row))
                    md += '| ' + ' | '.join(padded[:len(rows[0])]) + ' |\n'
                lines.append('\n\n' + md + '\n')
        elif kind == 'para':
            lines.append(value + '\n')
        elif kind == 'blockquote':
            for p in value:
                lines.append('> ' + p + '\n')
            lines.append('')
        elif kind == 'hr':
            lines.append('\n\n---\n')
        elif kind == 'br':
            lines.append('<br>\n')
        elif kind == 'link':
            lines.append(f'[{value[0]}]({value[1]})')
        elif kind == 'font':
            lines.append(f'<font color="{value[0]}">{value[1]}</font>')
        elif kind == 'em':
            lines.append('*' + value + '*')
        elif kind == 'strong':
            lines.append('**' + value + '**')
        elif kind == 'icode':
            lines.append('`' + value + '`')
        elif kind == 'text':
            lines.append(value)
    
    result = ''.join(lines)
    result = re.sub(r'\n{3,}', '\n\n', result)
    return result.strip()


# ---- Module names ----
MODULE_NAMES = {
    "sso-ssoapi-page": "免登录集成 - 接口文档",
    "sso-sdk-page": "免登录集成 - Demo/SDK",
    "sso-certificate-page": "免登录集成 - 证书",
    "server-sso-page": "服务端 - SSO",
    "server-page": "服务端 - 首页",
    "server-paas-paas-page": "PaaS API - PaaS接口",
    "server-paas-Readme-page": "PaaS API - 概述",
    "server-overview-page": "概览",
    "server-oauth2-ResourceOwnerPasswordCredentials-page": "OAuth2 - 密码模式",
    "server-oauth2-RefreshToken-page": "OAuth2 - 刷新令牌",
    "server-oauth2-Readme-page": "OAuth2 - 概述",
    "server-oauth2-ClientCredentials-page": "OAuth2 - Client Credentials",
    "server-oauth2-AuthorizationCode-page": "OAuth2 - Authorization Code",
    "server-crm-search-page": "CRM - 查询接口",
    "server-crm-sales-page": "CRM - 销售线索",
    "server-crm-receivables-page": "CRM - 回款",
    "server-crm-objinfo-page": "CRM - 业务对象字段信息",
    "server-crm-modify-page": "CRM - 修改接口",
    "server-crm-item-page": "CRM - 字典接口",
    "server-crm-invoice-page": "CRM - 发票",
    "server-crm-error-page": "CRM - 错误码",
    "server-crm-delete-page": "CRM - 删除接口",
    "server-crm-customer-page": "CRM - 客户",
    "server-crm-contract-page": "CRM - 合同",
    "server-crm-business-page": "CRM - 商机",
    "server-crm-add-page": "CRM - 新增接口",
    "server-crm-Readme-page": "CRM - 概述",
    "server-connection-page": "获取授权",
    "server-apilist-workset-page": "项目集接口",
    "server-apilist-work-page": "项目接口",
    "server-apilist-todo-page": "待办接口",
    "server-apilist-task-page": "任务接口",
    "server-apilist-survey-page": "360评估接口",
    "server-apilist-staff-page": "员工接口",
    "server-apilist-review-page": "复盘接口",
    "server-apilist-position-page": "职级/职务/标签",
    "server-apilist-performance-page": "绩效接口",
    "server-apilist-paas-page": "API列表-PaaS",
    "server-apilist-okr-page": "OKR接口",
    "server-apilist-milestone-page": "项目里程碑接口",
    "server-apilist-message-page": "消息/待办接口",
    "server-apilist-kpi-page": "KPI接口",
    "server-apilist-group-page": "群组接口",
    "server-apilist-department-page": "部门接口",
    "server-apilist-daily-page": "总结接口",
    "server-apilist-code-page": "错误返回码",
    "server-apilist-Readme-page": "API列表 - 概述",
    "server-apilist-Interview-page": "面谈接口",
}

CATEGORIES = [
    ("OAuth2 授权", ["server-oauth2"]),
    ("CRM API", ["server-crm"]),
    ("业务API", ["server-apilist"]),
    ("PaaS API", ["server-paas"]),
    ("免登录集成(SSO)", ["sso-"]),
    ("基础说明", ["server-connection", "server-page", "server-sso", "server-overview"]),
]


def main():
    SRC = "docs/数据梳理/TITA/原始层"
    OUT = os.path.join(SRC, "TITA_原始文档.md")
    
    all_docs = {}
    
    for filename in sorted(os.listdir(SRC)):
        if not filename.endswith('.chunk.js'):
            continue
        name = filename.replace('.chunk.js', '')
        filepath = os.path.join(SRC, filename)
        
        try:
            md = process_chunk(filepath)
            if md and len(md.strip()) > 20:
                display_name = MODULE_NAMES.get(name, name)
                all_docs[name] = (display_name, md)
                codes = md.count('```')
                tables = md.count('| ---')
                print(f"OK  [{name:50s}] {len(md):6d} chars  codes:{codes//2:2d}  tables:{tables:2d}")
            else:
                print(f"ERR [{name:50s}] short ({len(md) if md else 0})")
        except Exception as e:
            print(f"ERR [{name:50s}] {e}")
    
    with open(OUT, 'w', encoding='utf-8') as f:
        f.write("# TITA 开放API 文档\n\n")
        f.write(f"> 来源: https://oapi.tita.com/#/\n")
        f.write(f"> 共 {len(all_docs)} 个文档模块\n\n")
        f.write("---\n\n")
        
        for cat_name, prefixes in CATEGORIES:
            f.write(f"# {cat_name}\n\n")
            for name in sorted(all_docs):
                if any(name.startswith(p) for p in prefixes):
                    display_name, md = all_docs[name]
                    f.write(f"## {display_name}\n\n")
                    f.write(md)
                    f.write('\n\n---\n\n')
    
    print(f"\nDone! {OUT}, {len(all_docs)} modules")


if __name__ == '__main__':
    main()
