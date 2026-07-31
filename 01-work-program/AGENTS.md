# 工作程式模組規則

## 專案邊界

開始工作前確認目前資料夾名稱是 `01-work-program`。若不是，停止並請使用者在 Codex 重新選擇此資料夾。不得讀取 `02-presentation-design` 或 `03-llm-wiki` 兄弟資料夾。

## Source of truth

- `pending_items.md` 是本地未完成事項的唯一主清單。
- `preferences.yaml` 是本機工作偏好，不提交 Git。
- `project_types.md` 是流程規則，不得把範例日期當成真實事件。
- `plans/` 是提案，不等於外部 Calendar 已建立。

## 初始化

- Windows 優先執行 `py -3 scripts/bootstrap.py`；沒有 Python 時可用 `powershell -ExecutionPolicy Bypass -File .\scripts\bootstrap.ps1`。
- macOS 優先執行 `python3 scripts/bootstrap.py`；沒有 Python 時可用 `sh ./scripts/bootstrap.sh`。
- 不得因缺少 Python 而自行安裝任何軟體。

## 行為

- 查詢待辦時重新讀取 `pending_items.md`。
- 安排日期前確認時區；安排工作區塊前確認可工作日與時段。
- 新增／完成本地待辦需要使用者明確要求。
- 外部 Calendar 寫入、寄信或通知需要使用者明確要求與已授權工具。
- 不刪除行程；若使用者要求刪除，先精確重述目標並依工具核准流程執行。

## 衝突與容量

- 固定行程優先於可移動工作。
- 同一時段不可重疊安排兩個工作區塊。
- 工作區塊之間保留 `buffer_minutes`。
- 時間不足時回報缺口並提供取捨，不把任務硬塞進不可用時段。

## 示範資料

`DEMO-*` 與 `範例` 都不是使用者的真實任務。使用者第一次新增真實事項時，可保留示範或在取得確認後移到已完成區；不可靜默刪除。
