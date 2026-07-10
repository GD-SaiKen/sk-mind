#!/usr/bin/env python3
"""Git 进度同步辅助脚本 — 扫描近期 commit 中的任务引用，生成与追踪表的差异报告。

用法:
    python scripts/sync_git_progress.py [--days 7] [--json]

输出:
    - 列出每个任务编号在近期 commit 中的出现次数
    - 标记哪些任务有 commit 但可能需要更新追踪文档
    - --json 模式输出机器可读的 JSON，供 AI Skill 直接消费
"""

import argparse
import json
import re
import subprocess
import sys
from collections import defaultdict
from datetime import datetime, timedelta

# ── 任务编号正则 ──────────────────────────────
TASK_PATTERN = re.compile(r'\bT(\d{2})\b', re.IGNORECASE)

# ── 任务编号 -> 任务名称映射（与 02-团队开发任务.md 一致）───
TASK_NAMES = {
    "00": "客户数据盘点与试点范围确认",
    "01": "工程骨架与本地开发环境",
    "02": "数据库模型、迁移与测试基座",
    "03": "用户、角色、权限与审计基础",
    "04": "数据源管理后端",
    "05": "数据源管理前端",
    "06": "接入任务、批次与错误清单后端",
    "07": "文件扫描与 Excel 样本解析",
    "08": "Excel 批量导入与 Raw 层落库",
    "09": "Clean / Serving 生成与字段元数据",
    "10": "数据目录后端与查询 API",
    "11": "数据质量规则与检查",
    "12": "基础平台前端页面串联",
    "13": "私有化部署与运行检查",
    "14": "阶段 1 集成验收",
    "15": "语义对象、属性、关系模型后端",
    "16": "DataMapping 与语义目录后端",
    "17": "对象行动策略后端",
    "18": "BusinessGraphEdge 模型与查询服务",
    "19": "关系边生成与人工确认",
    "20": "语义与图谱前端页面",
    "21": "阶段 2 集成验收",
    "22": "Agent 会话、消息、工具调用与依据模型",
    "23": "指标、规则与口径管理后端",
    "24": "Agent 工具注册与目录/质量/指标工具",
    "25": "图谱查询工具与对象行动策略检查",
    "26": "Agent 问题规划、回答生成与审计",
    "27": "Agent 查询与审计前端页面",
    "28": "阶段 3 集成验收",
    "29": "Agent 建议与预警草稿后端",
    "30": "协同待办与人工确认闭环后端",
    "31": "建议、预警与协同前端页面",
    "32": "阶段 4 集成验收",
    "33": "全链路验收、样例数据与交付整理",
}


def get_recent_commits(days: int) -> list[dict]:
    """获取最近 N 天的 git commit 记录。"""
    since_date = (datetime.now() - timedelta(days=days)).isoformat()
    cmd = [
        "git", "log",
        f"--since={since_date}",
        "--format=%H%n%an%n%aI%n%s%n---",
    ]
    try:
        result = subprocess.run(
            cmd, capture_output=True, text=True, encoding="utf-8", check=True,
            errors="replace",
        )
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] git log 执行失败: {e.stderr}", file=sys.stderr)
        sys.exit(1)

    commits = []
    for block in result.stdout.strip().split("\n---"):
        if not block.strip():
            continue
        lines = block.strip().split("\n")
        if len(lines) >= 4:
            commits.append({
                "hash": lines[0][:7],
                "author": lines[1],
                "date": lines[2][:10],
                "message": lines[3],
            })
    return commits


def parse_task_refs(commits: list[dict]) -> dict[str, list[dict]]:
    """从 commit 中解析任务引用。"""
    task_refs = defaultdict(list)
    for c in commits:
        seen = set()
        for m in TASK_PATTERN.finditer(c["message"]):
            task_id = m.group(1)
            if task_id not in seen:
                seen.add(task_id)
                task_refs[task_id].append(c)
    return task_refs


def safe_print(text: str) -> None:
    """安全打印，替换无法编码的字符。"""
    try:
        print(text)
    except UnicodeEncodeError:
        print(text.encode("ascii", errors="replace").decode("ascii"))


def print_report(
    commits: list[dict],
    task_refs: dict[str, list[dict]],
    days: int,
):
    """打印人类可读的报告。"""
    print(f"Git 进度同步报告 - 最近 {days} 天 ({len(commits)} 个 commit)")
    print("=" * 60)

    if not task_refs:
        print()
        print("[!] 近期 commit 中未检测到任务引用 (T00-T33)。")
        print("   建议在 commit message 中加入任务编号，例如：")
        print('   feat(T06): 完成接入任务批次查询和错误清单端点')
        return

    print()
    print("[TASK] 检测到任务引用的 commit：")
    print()
    for task_id in sorted(task_refs.keys(), key=lambda x: int(x)):
        name = TASK_NAMES.get(task_id, "未知任务")
        refs = task_refs[task_id]
        print(f"  T{task_id} - {name} ({len(refs)} 次提交)")
        for c in refs:
            print(f"    [{c['date']}] {c['hash']} {c['author']}")
            print(f"    {c['message']}")

    print()
    print("[ACTION] 建议更新追踪表以下任务：")
    print("-" * 40)
    for task_id in sorted(task_refs.keys(), key=lambda x: int(x)):
        name = TASK_NAMES.get(task_id, "未知任务")
        refs = task_refs[task_id]
        print(f"  T{task_id} - {name}")
        print(f"    最近提交: {refs[-1]['date']} ({refs[-1]['author']})")
        print(f"    提交摘要: {refs[-1]['message'][:80]}")
    print()


def print_json(commits: list[dict], task_refs: dict[str, list[dict]]):
    """输出 JSON 格式，供 AI Skill 消费。"""
    result = {
        "total_commits": len(commits),
        "tasks_with_refs": {
            tid: {
                "name": TASK_NAMES.get(tid, "未知"),
                "commit_count": len(refs),
                "latest_commit": {
                    "hash": refs[-1]["hash"],
                    "author": refs[-1]["author"],
                    "date": refs[-1]["date"],
                    "message": refs[-1]["message"],
                },
            }
            for tid, refs in task_refs.items()
        },
    }
    # 输出到 stdout 时使用 utf-8，避免 gbk 编码错误
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    print(json.dumps(result, ensure_ascii=False, indent=2))


def main():
    parser = argparse.ArgumentParser(
        description="Git 进度同步辅助脚本"
    )
    parser.add_argument(
        "--days", type=int, default=7,
        help="扫描最近多少天的 commit（默认 7）"
    )
    parser.add_argument(
        "--json", action="store_true",
        help="以 JSON 格式输出（供 AI 消费）"
    )
    args = parser.parse_args()

    commits = get_recent_commits(args.days)
    task_refs = parse_task_refs(commits)

    if args.json:
        print_json(commits, task_refs)
    else:
        print_report(commits, task_refs, args.days)


if __name__ == "__main__":
    main()
