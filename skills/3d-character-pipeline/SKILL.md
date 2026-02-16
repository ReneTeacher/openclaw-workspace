---
name: 3d-character-pipeline
description: Midjourney + Three.js 3D角色生成Pipeline - 生成角色圖→變做遊戲Sprite→放入3D場景
metadata:
  updated: "2026-02-15"
  emoji: 🎨
---

# 3D Character Pipeline

完整既3D角色生成工作流

---

## 🎯 流程

```
1. Midjourney生成角色圖
        ↓
2. 生成Office背景
        ↓
3. 用Three.js整3D場景
        ↓
4. 角色放入場景
        ↓
5. 加入互動同動畫
```

---

## 📊 Midjourney Prompts

### 角色設計 (Portrait)
```
anthropomorphic [動物], Disney Zootopia 3D CGI, 
Pixar animation style, [服裝], [配件], 
professional, front view portrait, high quality 3d render
```

### 角色工作Pose
```
anthropomorphic [動物], Disney Zootopia 3D CGI,
[動作描述], office environment, full body,
pixar quality, 3d render
```

### Office背景
```
empty modern 3D office interior, Disney Pixar style,
cozy startup office, wooden desks, warm lighting,
large windows, plants, volumetric lighting,
wide shot, cinematic, no characters
```

### 統一風格關鍵詞
```
consistent lighting, cohesive art style, 
volumetric lighting, pixar quality
```

---

## 🎮 Three.js Implementation

### 優化Loading
1. **用簡單3D形狀** - 秒load
2. **Lazy Load** - click先load大圖
3. **Sprite Sheet** - 多幀動畫

### 基本結構
```python
# Streamlit + Three.js
import streamlit.components.v1 as components

html = """
<script src="three.min.js">
// Three.js code here
</script>
"""

components.html(html, height=700)
```

---

## 📁 相關檔案

- `anime-office-dashboard/app_3d_optimized.py` - 優化版3D Dashboard
- `anime-office-dashboard/characters/` - 角色圖
- `anime-office-dashboard/reference/` - 參考圖

---

## 🔧 常用命令

```bash
# Generate characters
curl -X POST "https://mymidjourneyapi.zeabur.app/imagine" \
  -d '{"prompt":"你的prompt"}'

# Upscale
curl -X POST "https://mymidjourneyapi.zeabur.app/upscale" \
  -d '{"index": 1}'
```

---

## ⚠️ 註意

1. **Discord CDN過期快** - 生成後要立即download
2. **Midjourney多人難一致** - 建議分開生成角色
3. **Ready Player Me** - 可以整真正3D Avatar

---

*最後更新: 2026-02-15*
