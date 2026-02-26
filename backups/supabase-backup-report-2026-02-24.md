# Supabase 數據庫備份報告
**日期**: 2026年2月24日 上午12:00 (Asia/Hong_Kong)
**狀態**: 自動備份任務

---

## 📋 項目概覽

### 1. MyClawOffice (anime-office-dashboard)
- **數據庫平台**: Supabase
- **URL**: https://czolesxhhfiwzubvbmab.supabase.co
- **狀態**: ❌ **無法訪問** - DNS 解析失敗，項目可能已刪除或 URL 錯誤
- **API Key**: sb_publishable_UB5d3pLNUYjX7eEryltBNg_S_4Tibew (僅讀取權限)

**已知 Schema 表結構**:
- `agent_status` - Agent 狀態追蹤
- `cron_jobs` - Cron 任務配置  
- `system_metrics` - 系統指標
- `activity_log` - 活動日誌

### 2. todo-list-prod
- **數據庫平台**: Supabase  
- **位置**: `/home/node/.openclaw/workspace/temp_todo_list/`
- **狀態**: ❌ 無法訪問（項目可能已棄用）
- **備註**: 目錄名有 "temp_" 前綴，強烈建議確認是否仍在使用

**已知 Schema 表結構**:
- `public.todos` - 待辦事項 (id, title, completed, created_at)

### 3. exam-system-prod
- **數據庫平台**: **Zeabur PostgreSQL** ⚠️
- **狀態**: ❌ 非 Supabase 項目
- **架構**: Express + React 前端, PostgreSQL 後端

**已知 Schema 表結構**:
- `users` - 用戶 (student/teacher)
- `exams` - 考試
- `questions` - 問題
- `submissions` - 提交記錄

---

## 🔍 訪問測試結果

| 項目 | 結果 | 備註 |
|------|------|------|
| Supabase URL DNS 解析 | ❌ 失敗 | czolesxhhfiwzubvbmab.supabase.co 無法解析 |
| Supabase API 直接訪問 | ❌ 連接失敗 | 項目可能已刪除 |
| 環境變數中的 Supabase Key | ❌ 未找到 | 系統中無儲存的 service role key |
| Schema 文件 | ✅ 存在 | 結構定義已保存 |

---

## 📁 已保存的 Schema 文件

所有項目的 Schema 定義已在此工作區保存:

1. ✅ `/home/node/.openclaw/workspace/anime-office-dashboard/supabase_schema.sql`
2. ✅ `/home/node/.openclaw/workspace/temp_todo_list/supabase-schema.sql`
3. ✅ `/home/node/.openclaw/workspace/exam-system-backend/schema.sql`

---

## ⚠️ 重要發現

### MyClawOffice (anime-office-dashboard)
- **Supabase 項目可能已被刪除**
- URL `czolesxhhfiwzubvbmab.supabase.co` 無法解析
- 強烈建議登入 Supabase Dashboard 確認項目狀態

### todo-list-prod  
- 目錄前綴為 `temp_`，表示可能已棄用
- 需確認項目是否仍需要此

### exam-system-prod  
- **不是 Supabase 項目**
- 使用 Zeabur 托管的 PostgreSQL
- 需透過 Zeabur 進行備份

---

## 💡 備份建議

### 1. 確認項目狀態 (立即行動)

```bash
# 登入 Supabase Dashboard 檢查
https://app.supabase.com

# 檢查項目是否仍存在
# 如果不存在，需要重建或遷移
```

### 2. 若項目仍存在，備份方法:

```bash
# 方法 A: 使用 Supabase CLI
npx supabase db dump --db-url "postgres://postgres:[PASSWORD]@db.[REF].supabase.co:5432/postgres" > backup.sql

# 方法 B: 透過 Dashboard 手動備份
# 1. 登入 https://app.supabase.com
# 2. 進入項目 → SQL Editor
# 3. 執行: SELECT * FROM table_name;
# 4. 導出為 CSV/SQL

# 方法 C: 使用 pg_dump
pg_dump "postgres://postgres:[PASSWORD]@db.czolesxhhfiwzubvbmab.supabase.co:5432/postgres" > backup.sql
```

### 3. Exam System (Zeabur):

```bash
# 透過 Zeabur Dashboard 備份
# 1. 登入 https://zeabur.com
# 2. 進入 PostgreSQL 服務 → Backups
# 3. 創建手動備份
```

---

## 🎯 結論

**無法完成自動備份** - Supabase 項目無法訪問

### 需要用戶協助:
1. **登入 Supabase Dashboard** 確認 MyClawOffice 項目是否仍存在
2. **提供正確的 Supabase URL** 如果項目已遷移
3. **提供 Service Role Key** 如果需要 API 訪問
4. **確認 todo-list 是否仍需使用**
5. **確認 exam-system 的 Zeabur 連接資訊**

### 現有資源:
- ✅ 所有 Schema 定義已保存為 SQL 文件
- ⚠️ 需要用戶確認項目狀態

---

*報告生成時間: 2026-02-24 00:00*
*任務類型: cron:88decc06-28f3-467f-9314-fbcc0e671db2*
