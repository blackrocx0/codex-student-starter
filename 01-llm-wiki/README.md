# LLM Wiki

把原始資料保留下來，再由 AI 整理成可追溯、可交叉引用的 Markdown Wiki。

## 三層架構

```text
raw/                 原始資料，只新增、不覆寫
wiki/                AI 整理的主題頁、索引與操作紀錄
templates/           Wiki 頁面格式
config.yaml          命名與維護規則
```

## 試用

```text
Wiki 目前有哪些主題？
把 raw/demo-source.md 整理成 Wiki。
根據 Wiki 說明間隔複習的三個步驟。
```

`demo-source.md` 與對應 Wiki 頁是框架自製的簡短示範，不是第三方全文。

## 新增自己的資料

把 `.md`、`.txt` 或整理過的筆記放進 `raw/`，再告訴 Codex：

```text
請把 raw 裡的新資料整理進 Wiki。
```

若來源是網頁，建議在 raw 檔開頭保留原始 URL、擷取日期與授權／引用說明。

