/**
 * 时间格式化工具。
 *
 * 后端所有时间字段均为 UTC（timestamptz，isoformat 输出带 `+00:00`）。
 * 前端过去用 `iso.slice(0, 19)` 截字符串，会把 UTC 当北京时间显示，导致 8 小时偏差。
 * 这里统一转换为北京时间（UTC+8）后再格式化，不依赖浏览器所在时区。
 */

const BEIJING_OFFSET_MS = 8 * 60 * 60 * 1000

/** 判断字符串是否已带时区标记（Z 或 ±HH:MM / ±HHMM）。 */
function hasTimezone(s: string): boolean {
  return /[zZ]$|[+-]\d{2}:?\d{2}$/.test(s)
}

/**
 * 把后端返回的 ISO 时间字符串格式化为北京时间。
 *
 * @param iso 后端返回的时间字符串（带或不带时区标记均可）
 * @param withSeconds 是否包含秒，默认 true
 * @returns 形如 `2026-07-25 21:17:58`；空值返回 ''
 */
export function fmtDateTime(iso?: string | null, withSeconds = true): string {
  if (!iso) return ''
  let s = String(iso).trim()
  // 不带时区标记的一律按 UTC 处理（后端存的就是 UTC）
  if (!hasTimezone(s)) s = s.replace(' ', 'T') + 'Z'
  const d = new Date(s)
  if (isNaN(d.getTime())) {
    // 解析失败时退回到原始截断，避免显示 Invalid Date
    return String(iso).slice(0, 19).replace('T', ' ')
  }
  // 转北京时间：加 8h 后取 UTC 各字段，结果与运行环境时区无关
  const bj = new Date(d.getTime() + BEIJING_OFFSET_MS)
  const p = (n: number) => String(n).padStart(2, '0')
  const date = `${bj.getUTCFullYear()}-${p(bj.getUTCMonth() + 1)}-${p(bj.getUTCDate())}`
  const time = withSeconds
    ? `${p(bj.getUTCHours())}:${p(bj.getUTCMinutes())}:${p(bj.getUTCSeconds())}`
    : `${p(bj.getUTCHours())}:${p(bj.getUTCMinutes())}`
  return `${date} ${time}`
}

/** 仅日期（北京时间），形如 `2026-07-25`。 */
export function fmtDate(iso?: string | null): string {
  const s = fmtDateTime(iso)
  return s ? s.slice(0, 10) : ''
}
