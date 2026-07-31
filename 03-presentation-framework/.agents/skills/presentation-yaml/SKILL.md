---
name: presentation-yaml
description: 依目前專案的 Theme、Layout 與當次內容，建立或檢查單張七段式 assembled presentation YAML；使用者要求投影片 YAML、版型 prompt 或簡報設計規格時使用。
---

# Presentation YAML

本 Skill 只負責單張 YAML-first 設計規格。圖片、HTML 與 PPTX 是不同 renderer，
除非使用者明確要求且對應工具可用，不得宣稱已完成其他格式。

1. 完整讀取 `AGENTS.md`。
2. 取得當次必要輸入：
   - 受眾。
   - 這一頁要完成的溝通目的。
   - 可用內容或要傳達的主張。
3. Theme／Layout 未指定時可用 starter 預設：
   - Theme：`warm-learning`
   - Layout：`process-flow`
4. 完整讀取選定的 Theme、Layout 與
   `templates/assembled-slide.template.yaml`。
5. 依當次任務建立 content contract，不把示範文案當固定格式。
6. 輸出必須維持七個 top-level 區段與順序：
   1. `page_type_and_mood`
   2. `visual_base_2a`
   3. `corner_decoration_2b`
   4. `layout_description`
   5. `content`
   6. `safe_zone_constraints`
   7. `closing_design_intent`
7. 將檔案寫入 `output/<slug>.assembled.yaml`。
8. 執行：

   ```powershell
   python scripts/validate_slide_yaml.py output/<slug>.assembled.yaml
   ```

9. 驗證失敗時修正 YAML；不得跳過後宣稱完成。
10. 若使用者要求生圖：
    - 先確認目前工作階段真的有圖片生成 Skill／工具。
    - 使用完整 YAML 作為設計規格。
    - 工具缺少或未授權時停在 YAML，清楚說明缺少什麼。

設計底線：

- Theme 定義視覺語彙；Layout 定義資訊結構；Content 是本次材料。
- 平行項目維持相同視覺權重。
- 標題與主要內容區需有清楚間隔。
- 主要內容留在 10%–90% safe zone。
- 不用純裝飾犧牲可讀性。

