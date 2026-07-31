# 資安與示範資料原則

## Repository 不應包含

- `.env`、API key、OAuth token、Cookie、私人金鑰。
- 真實信箱、電話、地址、Calendar ID 或付款資訊。
- 個人課程、客戶或公司內部資料。
- 固定的 Windows 磁碟路徑或 macOS 使用者目錄。
- 可識別原作者個人成品的大型輸出或歷史 archive。

## 發布前檢查

Windows：

```powershell
powershell -ExecutionPolicy Bypass -File .\check.ps1
```

macOS：

```sh
sh ./check.sh
```

另外人工檢查 `.gitignore`、Git staged diff 與大型檔案。若發現真實憑證，不能只刪檔；先撤銷或輪換，再處理 Git 歷史。

所有 sample 使用 `DEMO-*`、`example.com`、固定假日期或明確的 placeholder。AI 不得把示範資料當成學員的真實偏好或工作內容。
