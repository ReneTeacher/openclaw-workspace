# Supabase 數據庫備份報告
**日期**: 2026年2月23日 上午12:00 (Asia/Hong_Kong)
**狀態**: 自動備份任務

---

## 📋 項目概覽

### 1. MyClawOffice (anime-office-dashboard)
- **數據庫平台**: Supabase
- **URL**: https://czolesxhhfiwzubvbmab.supabase.co
- **狀態**: ⚠️ 無法直接訪問（缺少 API Key）

**已知 Schema 表結構**:
- `agent_status` - Agent 狀態追蹤
- `cron_jobs` - Cron 任務配置
- `system_metrics` - 系統指標
- `activity_log` - 活動日誌

### 2. todo-list-prod
- **數據庫平台**: Supabase  
- **位置**: `/home/node/.openclaw/workspace/temp_todo_list/`
- **狀態**: ⚠️ 無法直接訪問（缺少 API Key）
- **備註**: 目錄名有 "temp_" 前綴，可能已棄用

**已知 Schema 表結構**:
- `public.todos` - 待辦事項

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
| Supabase API 直接訪問 | ❌ 需要 API Key | 需要 supabase_url + supabase_key |
| 環境變數中的 Supabase Key | ❌ 未找到 | 系統中無儲存的憑證 |
| psql 客戶端 | ❌ 未安裝 | 無法直接連接數據庫 |
| Node.js 環境 | ✅ 可用 | 可嘗試使用 pg 連接 |
| Zeabur PostgreSQL (本地) | ✅ 可用 | OpenClaw 自身數據庫 |

---

## 📁 已保存的 Schema 文件

所有項目的 Schema 定義已在此工作區保存:

1. ✅ `/home/node/.openclaw/workspace/anime-office-dashboard/supabase_schema.sql`
2. ✅ `/home/node/.openclaw/workspace/temp_todo_list/supabase-schema.sql`
3. ✅ `/home/node/.openclaw/workspace/exam-system-backend/schema.sql`

---

## 💡 備份建議

### 1. Supabase 項目（MyClawOffice + todo-list）

**推薦備份方法**:

```bash
# 方法 A: 使用 Supabase CLI（需要安裝）
npx supabase db dump --db-url "postgres://postgres:[PASSWORD]@db.[REF].supabase.co:5432/postgres" > backup.sql

# 方法 B: 手動 SQL 導出
# 1. 登入 https://app.supabase.com
# 2. 進入項目 → SQL Editor
# 3. 執行: SELECT * FROM table_name;
# 4. 導出為 CSV/SQL

# 方法 C: 使用 pg_dump
pg_dump "postgres://postgres:[PASSWORD]@db.czolesxhhfiwzubvbmab.supabase.co:5432/postgres" > backup.sql
```

**需要用戶提供**:
- [ ] Supabase Service Role Key
- [ ] Database Password
- [ ] 確認各項目是否仍在使用

### 2. Exam System（Zeabur PostgreSQL）

**推薦備份方法**:
```bash
# 使用 pg_dump（如果 Zeabur 允許外部連接）
pg_dump "postgres://[USER]:[PASSWORD]@[HOST]:5432/[DB]" > exam-system-backup.sql

# 或通過 Zeabur Dashboard
# 1. 登入 Zeabur
# 2. 進入項目 → PostgreSQL → Backups
# 3. 創建手動備份
```

---

## 🎯 結論

**無法完成自動備份** - 缺少 Supabase API Key/密碼

### 需要用戶協助:
1. **提供 Supabase API Key** - 用於訪問 MyClawOffice 和 todo-list 數據庫
2. **確認項目狀態** - 哪些項目仍在使用，哪些已棄用
3. **檢查 exam-system** - 確認 Zeabur PostgreSQL 的連接資訊

### 現有資源:
- ✅ 所有 Schema 定義已保存為 SQL 文件
- ✅ 可通過 Supabase Dashboard 手動備份
- ✅ 上次備份報告: 2026-02-20（位於 `/backups/supabase-backup-report-2026-02-20.md`）

---

*報告生成時間: 2026-02-23 00:00*
*任務類型: cron:88decc06-28f3-467f-9314-fbcc0e671db2*
