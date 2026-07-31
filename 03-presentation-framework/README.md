# YAML-first 簡報框架

這是從大型簡報系統精簡出的學員版本，只保留一個 Theme、一個 Layout、一個 Content
案例與一份完整 assembled YAML。目的是先理解「視覺、結構、內容分離」，再逐步擴充。

## 組裝關係

```text
Theme（看起來像什麼）
  + Layout（資訊怎麼放）
  + Content（這次要說什麼）
  = 7 段式 assembled YAML
```

## 試用

先驗證示範：

```powershell
python scripts/validate_slide_yaml.py examples/demo-process-flow.assembled.yaml
```

再告訴 Codex：

```text
用 warm-learning Theme 與 process-flow Layout，
做一張「從問題定義到測試」的單頁投影片 YAML，受眾是第一次做專題的學生。
```

輸出會放在 `output/`。沒有圖片生成工具時，完成的 YAML 本身就是本階段交付。

## 擴充順序

1. 先複製 Theme，調整色彩與字體。
2. 內容結構真的不同時才新增 Layout。
3. 增加第二個完整示範並通過 validator。
4. 確定要輸出圖片、HTML 或 PPTX 後，再為該 renderer 增加自己的契約與 QA。

不要把圖片、HTML 與 PPTX 當成同一條輸出管線；每個 renderer 都需要個別驗證。

