# 資安與隱私

## Repository 不可包含

- API key、OAuth token、App Password、Session cookie。
- 私人信箱、電話、住址、證件或付款資料。
- 真實客戶名單、未公開行程、會議連結或郵件內容。
- 個人電腦的絕對路徑。
- 講師歷史成品、部署帳號與 runtime log。

## 安裝時

- clone 前確認資料夾空白，避免覆蓋或混入既有資料。
- 使用 `git remote -v` 核對下載來源。
- 執行 `python security_scan.py` 掃描剛下載的完整框架。
- 執行 `python link_check.py` 檢查本地文件連結。
- 外部網址預設只列出；需要線上存取測試時另外請求權限。

## 日後使用

每個實際專案都有自己的 `scripts/security_scan.py`。發布前先開啟精確專案資料夾，再執行掃描與人工 Git diff 檢查。
