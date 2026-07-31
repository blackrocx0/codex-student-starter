# Windows 與 macOS 支援

## 支援範圍

| 項目 | Windows | macOS |
|---|---|---|
| clone 到空白資料夾 | Git／PowerShell | Git／Terminal |
| 根目錄檢查入口 | `check.ps1` | `check.sh` |
| Python 優先指令 | `py -3`、`python`、`python3` | `python3`、`python` |
| 工作程式初始化 | `bootstrap.py` 或 `bootstrap.ps1` | `bootstrap.py` 或 `bootstrap.sh` |
| 路徑處理 | Python `pathlib` | Python `pathlib` |

## 相容性原則

- Python 3.9+；不需要第三方套件。
- 所有 Python 程式使用 `pathlib` 與相對於腳本位置的路徑，不依賴磁碟代號或固定使用者目錄。
- `.sh` 使用 POSIX `sh` 語法與 LF 換行；不依賴 Homebrew 或 Bash 專用功能。
- `.ps1` 相容 Windows PowerShell 5.1+，包含空白或中文的路徑均使用完整引號處理。
- 使用者本機產生的偏好、初始化標記與輸出都由 `.gitignore` 排除。`git clone <URL> .` 仍要求安裝前資料夾完全空白；`.DS_Store` 或 `desktop.ini` 必須先經使用者同意移除。

## 沒有 Python 時

不要自動安裝。Codex 應人工確認三個專案資料夾、根目錄文件、Git remote、敏感檔名、明顯憑證字串與 Markdown 本地連結，再請使用者決定是否自行安裝 Python。

本文件保證的是 repository 安裝與本地腳本的 Windows／macOS 相容性；外部 Connector 是否可用仍取決於使用者的 Codex 環境與授權狀態。
