# Codex 學員框架

支援 Windows 與 macOS。學員從一個完全空白的資料夾開始，只需要把 GitHub URL 與下方固定提示詞貼給 Codex。Codex 會直接下載到目前資料夾、選用正確的作業系統指令、檢查安裝與資安，再請學員選擇一個專案資料夾。

## 可直接複製的提示詞

```text
請在「目前這個完全空白的資料夾」中安裝以下 GitHub repository：
https://github.com/blackrocx0/codex-student-starter

請依序執行：
1. 先顯示目前資料夾與作業系統，並用包含隱藏檔的方式確認資料夾完全空白；如果不是空白資料夾，停止並詢問我，不可覆蓋。若只有 macOS 的 `.DS_Store` 或 Windows 的 `desktop.ini`，先說明並取得我同意後才可移除。
2. 確認 Git 可用；若缺少就說明，不要自行安裝。取得只限 GitHub clone 所需的網路授權後，執行 git clone https://github.com/blackrocx0/codex-student-starter .，直接下載到目前資料夾，不要多包一層資料夾。
3. 完整讀取根目錄 AGENTS.md、README.md、INSTALL.md、PLATFORM_SUPPORT.md、PERMISSIONS.md、PROJECTS.md。
4. 顯示 git remote -v 與 git status，確認來源網址及下載狀態。
5. Windows 執行 powershell -ExecutionPolicy Bypass -File .\check.ps1；macOS 執行 sh ./check.sh。若找不到 Python 3.9+，不要自行安裝，改做等價的唯讀人工檢查。
6. 說明必要工具、選用工具、目前 workspace 權限，以及哪些 Connector 尚未連接；不要要求 Full access，也不要叫我把 Token 或密碼貼進對話。
7. 依序列出 01-work-program、02-presentation-design、03-llm-wiki 的用途，讓我選一個。
8. 我選擇後，請引導我在 Codex 介面把該資料夾開成新的專案／workspace；在我完成切換前停止，不要同時讀取三個專案。
9. 不要自動安裝套件、登入外部帳號、建立外部行程、上傳或發布任何內容，除非我後續明確要求。
```

純文字版本在 [`INSTALL_PROMPT.txt`](INSTALL_PROMPT.txt)。

## 三個獨立專案

| 順序 | 資料夾 | 用途 |
|---|---|---|
| 1. 工作程式 | `01-work-program` | 管理待辦、拆解工作、建立本地行程草案 |
| 2. 簡報設計 | `02-presentation-design` | 建立 Theme／Layout／Content 分離的投影片 YAML |
| 3. LLM-WIKI | `03-llm-wiki` | 匯入原始資料、建立與查詢 Markdown Wiki |

三個專案各自擁有 `AGENTS.md`、repo-local Skills、設定與輸出，不使用共用 student profile。

詳細安裝步驟見 [`INSTALL.md`](INSTALL.md)，平台差異見 [`PLATFORM_SUPPORT.md`](PLATFORM_SUPPORT.md)。
