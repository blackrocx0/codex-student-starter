# 工作程式

用本地 Markdown 管理待辦、拆解工作、製作今日清單與行程草案。沒有 Calendar 或 Gmail Connector 也能使用；只有使用者明確要求且工具已授權時，才同步外部服務。

## 核心檔案

| 檔案 | 用途 |
|---|---|
| `preferences.yaml` | 本機工作習慣；由 bootstrap 建立，不提交 Git |
| `project_types.md` | 常見專案的錨點與回推步驟 |
| `pending_items.md` | 未完成事項 source of truth |
| `plans/` | 尚未同步外部 Calendar 的本地排程草案 |
| `templates/daily-brief.template.md` | 每日摘要格式 |

## 初始化

請先確認 Codex 目前工作資料夾正是 `01-work-program`。

Windows 有 Python：

```powershell
py -3 scripts/bootstrap.py
```

Windows 沒有 Python：

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\bootstrap.ps1
```

macOS 有 Python：

```sh
python3 scripts/bootstrap.py
```

macOS 沒有 Python：

```sh
sh ./scripts/bootstrap.sh
```

四種入口都只會在目前專案建立 `preferences.yaml`、`.schedule-init.json` 與 `plans/`，不會寫入外部 Calendar。

## 第一次使用

```text
幫我設定工作程式。我在 Asia/Taipei，週一到週五 09:30–18:00 工作，
每個專注區塊 50 分鐘。
```

接著可以說：

```text
列出目前待辦。
把「完成課程作業」拆成三個工作區塊，週五前完成。
依 project_types.md 幫我回推課程作業。
```

## 外部同步

只有在使用者明確要求、目前 Codex 工作階段已提供並授權對應 Connector 時，才把已確認的草案寫入外部 Calendar。未同步時，Codex 必須明確標示。
