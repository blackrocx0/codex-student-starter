# 安裝流程

## 1. 必要條件

- Windows 10／11 或近期 macOS。
- Git 可從 Terminal 使用。
- Codex 能讀寫目前選定的 workspace。
- Python 3.9+ 是自動檢查的選用條件；所有 Python 腳本只用標準函式庫。

框架不會自動安裝 Git、Python、Node.js、Plugin 或 Connector。

## 2. 準備空白資料夾

先建立新的空白資料夾，並在 Codex 把它設為目前 workspace。clone 前必須確認連隱藏檔都不存在。macOS 若只有 `.DS_Store`，或 Windows 若只有 `desktop.ini`，Codex 必須先說明並取得使用者同意才能移除。

## 3. 直接 clone 到目前資料夾

Windows 與 macOS 使用相同指令：

```sh
git clone https://github.com/blackrocx0/codex-student-starter .
git remote -v
git status --short --branch
```

尾端的 `.` 代表直接下載到目前空白資料夾，不會再建立額外一層 repository 名稱資料夾。

## 4. 執行平台檢查

Windows PowerShell：

```powershell
powershell -ExecutionPolicy Bypass -File .\check.ps1
```

macOS Terminal：

```sh
sh ./check.sh
```

需要線上驗證外部文件連結時，先取得網路授權，再使用 Windows 的 `-Online` 或 macOS 的 `--online` 參數。找不到 Python 3.9+ 時，Codex 改做等價的唯讀人工檢查，不自行安裝。

## 5. 選擇專案

依下列順序選擇一個精確資料夾，並在 Codex 重新開啟成獨立 workspace：

1. `01-work-program`：工作程式
2. `02-presentation-design`：簡報設計
3. `03-llm-wiki`：LLM-WIKI

根目錄安裝任務到此停止。各專案的初始化與使用規則由該資料夾自己的 `AGENTS.md` 負責。
