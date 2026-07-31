# 安裝流程

## 1. 準備空白資料夾

學員先建立一個新的空白資料夾，並在 Codex 把它設為目前 workspace。clone 前必須確認連隱藏檔都不存在。

## 2. 貼上 GitHub URL 與提示詞

使用根目錄 `INSTALL_PROMPT.txt` 的內容，把 `{{GITHUB_URL}}` 換成實際 repository URL。

Codex 應執行：

```powershell
git clone <GITHUB_URL> .
git remote -v
git status --short --branch
python doctor.py
python security_scan.py
python link_check.py
```

`git clone ... .` 代表直接下載到目前空白資料夾，不會再建立額外的 repository 名稱資料夾。

## 3. 權限原則

- clone：只需要 GitHub 網路存取。
- 安裝後檢查：只需要目前 workspace 讀取與暫時寫入測試。
- 不需要 Full access。
- 外部 Connector、圖片生成與發布都不是安裝必要條件。

## 4. 選擇專案

安裝檢查完成後，使用者從三個專案中選一個，並在 Codex 介面重新開啟該精確資料夾：

- `01-llm-wiki`
- `02-schedule-assistant`
- `03-presentation-framework`

根目錄安裝任務到此停止。各專案的初始化與使用規則由該資料夾自己的 `AGENTS.md` 負責。
