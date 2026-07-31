---
name: wiki-ingest
description: 將文章、筆記、逐字稿或 raw 的新資料整理成這個 starter repository 的可維護 Markdown Wiki；使用者說加入知識庫、整理素材、ingest 或更新 Wiki 時使用。
---

# Wiki Ingest

目標是保留原始資料，建立可追溯、可更新、可交叉引用的 Wiki 頁面。

1. 完整讀取 `AGENTS.md` 與 `config.yaml`。
2. 確認輸入已存於 `raw/`。
   - 使用者只貼文字時，建立描述性檔名的新 raw 檔。
   - 不修改既有 raw；需要更正時新增更正檔並互相連結。
3. 讀取 `templates/wiki-page.template.md`。
4. 判斷應更新既有頁面或建立新頁面。
   - 同一核心主題優先更新既有頁面。
   - 新頁面檔名使用 kebab-case。
5. 只寫入輸入資料能支持的內容。
   - 不確定內容用 `> ⚠️ 待確認：`。
   - 衝突來源並列，不自行選一個當真。
6. 每頁加入來源清單，使用 repository 內相對路徑。
7. 更新 `wiki/index.md`。
8. 在 `wiki/log.md` 追加一筆 `INGEST` 或 `UPDATE`；不得改寫舊紀錄。
9. 回報新增／更新頁面、來源檔與待確認事項。

完成前檢查：

- raw 沒有被覆寫。
- 頁面有來源。
- index 有連結。
- log 有追加紀錄。
- 沒有把外部網路內容寫成已由本地來源證實。
