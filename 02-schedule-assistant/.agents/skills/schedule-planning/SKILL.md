---
name: schedule-planning
description: 使用 目前專案資料夾 的本地偏好、專案類型與 pending_items.md 拆解任務、安排工作區塊、列出今日待辦或偵測衝突；使用者要求排程、代辦、行程或專案回推時使用。
---

# Schedule Planning

1. 完整讀取 `目前專案資料夾/AGENTS.md`。
2. 讀取 `preferences.yaml`；不存在時先執行 bootstrap 或由
   `preferences.example.yaml` 建立。
3. 只詢問會影響本次結果的缺失欄位：
   - 涉及日期：時區必填。
   - 安排工作區塊：工作日與可工作時段必填。
   - 套用固定流程：錨點日期與專案類型必填。
4. 讀取 `project_types.md` 與 `pending_items.md`。
5. 將需求分類為：
   - 查詢：只讀並回覆。
   - 草擬：寫入 `plans/YYYY-MM-DD-<slug>.md`，不改外部服務。
   - 更新本地待辦：使用者明確要求新增／完成時，更新 `pending_items.md`。
   - 外部同步：只有使用者明確要求且目前工作階段有已授權 Connector 時執行。
6. 排程時尊重：
   - 時區與工作時段。
   - 固定行程與不可用時段。
   - 專注區塊長度、緩衝與 deadline。
   - 不把同一時間安排兩件工作。
7. Connector 缺少時提供本地可執行方案，不要求 Token。
8. 外部寫入完成後列出實際建立／修改的事件；未執行就明確說「尚未同步」。

禁止：

- 猜測 Calendar ID、信箱或私人時段。
- 在一般規劃請求中自動寄信、建外部事件或刪除行程。
- 把示範資料誤認為使用者真實待辦。

