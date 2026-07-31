# 工具與權限

## 安裝階段的最小權限

Sandbox 決定 Codex 可存取的檔案與網路範圍；Approval 決定跨越既有邊界前是否要停下詢問。兩者不是同一件事。

| 動作 | 需要 | 不需要 |
|---|---|---|
| clone GitHub repository | GitHub 網路存取、目前空白資料夾寫入 | Full access |
| 本地結構與連結檢查 | 目前 workspace 讀寫 | 外部帳號 |
| 線上驗證外部網址 | 使用者同意的網路存取 | 全磁碟存取 |
| 使用本地 Wiki／待辦／YAML | 選定專案 workspace 讀寫 | Connector |
| 同步 Calendar／Gmail | 對應 Plugin／Connector OAuth | 把密碼貼給 AI |
| 產生圖片或發布 | 使用者明確要求與對應工具 | 安裝時預先授權 |

Repository 不提供 `.codex/config.toml` 擴大權限，也不自動安裝依賴。

沒有 Connector 時仍可使用三個專案的本地功能。安裝 Plugin 或登入外部服務應延後到使用者選定專案並明確需要時。
## 官方延伸閱讀

- [Agent approvals and security](https://learn.chatgpt.com/docs/agent-approvals-security)
- [Permissions](https://learn.chatgpt.com/docs/permissions)
- [Skills](https://learn.chatgpt.com/docs/build-skills)
- [Plugins](https://learn.chatgpt.com/docs/plugins)
