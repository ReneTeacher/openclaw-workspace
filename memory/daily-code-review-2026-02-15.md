# Daily Code Review Report
Date: 2026-02-15

## 📋 Repo Status Summary

| Repo | Status | Last Commit |
|------|--------|-------------|
| todo-list | ✅ Active | c4e75c4 (Update todos.json) |
| exam-system | ✅ Active | 1a98e15 (Simplify to Streamlit + Supabase) |

---

## 🔍 Issues Found

### 1. todo-list (本地JSON版本)
**問題:**
- ❌ ID重複風險: 用 `len(todos) + 1` 生成ID，刪除項目後會有重複
- ❌ 無錯誤處理: file I/O無try-catch
- ❌ 無數據驗證: 無檢查空輸入

**改進:**
- [已修復] ID改用timestamp生成

### 2. exam-system
**問題:**
- ❌ 考試時間限制得個field，無倒數計時器
- ❌ 老師睇唔到學生成绩
- ❌ 無題目編輯/刪除功能

**改進:**
- [建議] 加入倒數計時器
- [建議] 老師儀表板睇學生分數
- [建議] 題目管理CRUD

---

## 🛠️ 可添加功能

| 功能 | 複雜度 | 預計時間 |
|------|--------|----------|
| todo-list同步到Supabase | 中 | 30分鐘 |
| exam-system倒數計時器 | 低 | 15分鐘 |
| exam-system老師睇成績dashboard | 中 | 30分鐘 |
| exam-system題目編輯刪除 | 低 | 20分鐘 |

---

## ✅ Dependencies檢查

- streamlit>=1.28.0 ✅ (OK)
- supabase>=2.0.0 ✅ (OK)

---

## 📝 總結

兩個項目結構都幾好，無咩大問題。
主要係exam-system功能可以再丰富啲。

要整邊樣？話我知。
