# 簡報設計模組規則

## 專案邊界

開始工作前確認目前資料夾名稱是 `02-presentation-design`。若不是，停止並請使用者在 Codex 重新選擇此資料夾。不得讀取 `01-work-program` 或 `03-llm-wiki` 兄弟資料夾。

## 架構

- `prompt_system/themes/`：視覺語彙，包括色彩、字體、材質與裝飾。
- `prompt_system/layouts/`：資訊角色、槽位、空間關係與 safe area。
- `examples/*-content.yaml`：本次內容，不是可永久套用的固定文案。
- `templates/assembled-slide.template.yaml`：七段式輸出形狀。
- `output/`：本機生成物。

Theme 與 Layout 必須分離。只因顏色、材質或氣氛不同，不新增 Layout。

## 七段式輸出

順序固定：

1. `page_type_and_mood`
2. `visual_base_2a`
3. `corner_decoration_2b`
4. `layout_description`
5. `content`
6. `safe_zone_constraints`
7. `closing_design_intent`

`content` 欄位依當次任務與 Layout 動態決定，不從示範照抄。

## 設計與 QA

- 主要內容保持在水平與垂直 10%–90% safe zone。
- 平行資訊使用相同視覺權重；只有語意主從存在時才做大小差。
- 標題區與內容區不得重疊，兩者之間保留清楚過渡空間。
- 先降低內容密度，不用極小字硬塞。
- Windows 使用 `py -3 scripts/validate_slide_yaml.py <yaml-path>`；macOS 使用 `python3 scripts/validate_slide_yaml.py <yaml-path>`。

## Renderer 邊界

- assembled YAML 不等於圖片已生成。
- 圖片不等於可編輯 HTML。
- HTML 不等於可編輯 PPTX。
- 工具缺少或未完成實際輸出 QA 時，必須清楚說明尚未完成，不得用其他格式冒充。
