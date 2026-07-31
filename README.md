# Codex 學員框架

學員從一個完全空白的資料夾開始，只需要把 GitHub URL 與一段固定提示詞貼給 Codex。Codex 會把 repository 直接下載到目前資料夾、檢查安裝結果、資安與文件連結，再請學員選擇一個專案資料夾。

## 可直接複製的提示詞

```text
請在「目前這個完全空白的資料夾」中安裝以下 GitHub repository：
https://github.com/blackrocx0/codex-student-starter

請依序執行：
1. 先顯示目前資料夾，並用包含隱藏檔的方式確認它完全空白；如果不是空白資料夾，停止並詢問我，不可覆蓋。
2. 取得只限 GitHub clone 所需的網路授權後，執行 git clone https://github.com/blackrocx0/codex-student-starter .，直接下載到目前資料夾，不要多包一層資料夾。
3. 完整讀取根目錄 AGENTS.md、README.md、INSTALL.md、PERMISSIONS.md、PROJECTS.md。
4. 顯示 git remote -v 與 git status，確認來源網址及下載狀態。
5. 執行 python doctor.py、python security_scan.py、python link_check.py。若沒有 Python，不要自行安裝，改做等價的唯讀人工檢查。
6. 說明必要工具、選用工具、目前 workspace 權限，以及哪些 Connector 尚未連接；不要要求 Full access，也不要叫我把 Token 或密碼貼進對話。
7. 列出 01-llm-wiki、02-schedule-assistant、03-presentation-framework 的用途，讓我選一個。
8. 我選擇後，請引導我在 Codex 介面把該資料夾開成新的專案／workspace；在我完成切換前停止，不要同時讀取三個專案。
9. 不要自動安裝套件、登入外部帳號、建立外部行程、上傳或發布任何內容，除非我後續明確要求。
```

純文字版本在 [`INSTALL_PROMPT.txt`](INSTALL_PROMPT.txt)。

## 三個獨立專案

| 資料夾 | 用途 |
|---|---|
| `01-llm-wiki` | 匯入原始資料、建立與查詢 Markdown Wiki |
| `02-schedule-assistant` | 管理待辦、專案步驟與本地行程草案 |
| `03-presentation-framework` | 建立 Theme／Layout／Content 分離的投影片 YAML |

三個專案各自擁有 `AGENTS.md`、repo-local Skills、設定與輸出，不使用共用 student profile。

詳細安裝步驟見 [`INSTALL.md`](INSTALL.md)。
