# 學員框架安裝規則

Repository 根目錄只負責安裝後檢查與專案選擇，不承接 Wiki、行程或簡報內容工作。

## GitHub 安裝後流程

1. 確認 repository 是以 `git clone <URL> .` 直接下載到使用者原本的空白資料夾。
2. 讀取 `README.md`、`INSTALL.md`、`PERMISSIONS.md` 與 `PROJECTS.md`。
3. 執行：

   ```powershell
   python doctor.py
   python security_scan.py
   python link_check.py
   ```

4. Python 不存在時，做等價的唯讀人工檢查；不得自行安裝 Python、Node.js、Plugin 或改變全域權限。
5. 顯示 Git remote、目前資料夾、檢查結果與缺少的選用工具。
6. 請使用者選擇一個專案：
   - `01-llm-wiki`
   - `02-schedule-assistant`
   - `03-presentation-framework`
7. 請使用者在 Codex 介面把選定資料夾開成新的專案／workspace。
8. 使用者尚未切換資料夾前停止，不讀取或修改任何專案內容。

## 安全限制

- clone 前先用包含隱藏檔的方式確認目前資料夾完全空白；非空就停止並詢問。
- 只為 GitHub clone 請求必要的網路權限，不要求 Full access。
- `link_check.py` 預設只驗證本地連結；外部網址的線上檢查必須另外取得網路授權。
- 根目錄不建立共用 Skills、student profile、偏好或 output。
- 三個專案的 `AGENTS.md` 與 `.agents/skills/` 只在各自資料夾工作時使用。
