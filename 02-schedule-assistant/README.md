# 行程管理助手

這個模組預設只使用本地 Markdown。沒有 Calendar 或 Gmail Connector 也能完成任務拆解、
待辦管理、今日清單與排程草案。

## 核心檔案

| 檔案 | 用途 |
|---|---|
| `preferences.yaml` | 本機工作習慣；由 bootstrap 建立，不提交 Git |
| `project_types.md` | 常見專案的錨點與回推步驟 |
| `pending_items.md` | 未完成事項 source of truth |
| `plans/` | 尚未同步外部 Calendar 的本地排程草案 |
| `templates/daily-brief.template.md` | 每日摘要格式 |

## 初始化

請先確認 Codex 目前工作資料夾正是 `02-schedule-assistant`，再執行：

```powershell
python scripts/bootstrap.py
```

Windows 沒有 Python 時可執行 `powershell -ExecutionPolicy Bypass -File scripts/bootstrap.ps1`。

## 第一次使用

```text
幫我設定行程助手。我在 Asia/Taipei，週一到週五 09:30–18:00 工作，
每個專注區塊 50 分鐘。
```

接著可以說：

```text
列出目前待辦。
把「完成課程作業」拆成三個工作區塊，週五前完成。
依 project_types.md 幫我回推課程作業。
```

## 外部同步

只有在使用者明確要求、目前 Codex 工作階段已提供並授權對應 Connector 時，
才把已確認的草案寫入外部 Calendar。未同步時，Codex 必須明確標示。

