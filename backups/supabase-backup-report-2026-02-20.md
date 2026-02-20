# Supabase 數據庫備份報告
**日期**: 2026年2月20日 上午12:01 (Asia/Hong_Kong)
**狀態**: 自動備份任務

---

## 📋 項目概覽

### 1. MyClawOffice (anime-office-dashboard)
- **數據庫平台**: Supabase
- **URL**: https://czolesxhhfiwzubvbmab.supabase.co
- **狀態**: ⚠️ 無法直接訪問（需要 API Key）

**已知 Schema 表結構**:
- `agent_status` - Agent 狀態追蹤
- `cron_jobs` - Cron 任務配置
- `system_metrics` - 系統指標
- `activity_log` - 活動日誌

### 2. todo-list-prod
- **數據庫平台**: Supabase
- **URL**: 未在配置中明確指定
- **狀態**: ⚠️ 無法直接訪問

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
| psql 客戶端 | ❌ 未安裝 | 無法直接連接數據庫 |
| Supabase CLI | ❌ 未安裝 | 需要額外安裝 |
| Node.js 環境 | ✅ 可用 | 可嘗試使用 pg 連接 |

---

## 💡 備份建議

### 1. Supabase 項目（MyClawOffice + todo-list）

**推薦備份方法**:

```bash
# 方法 A: 使用 Supabase CLI（推薦）
npx supabase db dump --db-url "postgres://postgres:[PASSWORD]@db.[REF].supabase.co:5432/postgres" > backup.sql

# 方法 B: 手動 SQL 導出
# 1. 登入 https://app.supabase.com
# 2. 进入项目 → SQL Editor
# 3. 執行: SELECT * FROM table_name;
# 4. 導出為 CSV/SQL

# 方法 C: 设置自动备份
# Supabase Pro 计划支持每日自动备份
```

**需要收集的憑證**:
- [ ] Database Host: `db.czolesxhhfiwzubvbmab.supabase.co`
- [ ] Database Password: ❓ 未找到
- [ ] Service Role Key: ❓ 未找到

### 2. Exam System（Zeabur PostgreSQL）

**推薦備份方法**:

```bash
# 使用 pg_dump
pg_dump "postgres://[USER]:[PASSWORD]@[HOST]:5432/[DB]" > exam-system-backup.sql

# 或通过 Zeabur Dashboard
# 1. 登录 Zeabur
# 2. 进入项目 → PostgreSQL → Backups
# 3. 创建手动备份
```

**已知配置位置**: `/home/node/.openclaw/workspace/exam-system-backend/.env.example`
**主機格式**: `xxx.internal` (Zeabur 內部格式)

---

## 📁 已保存的 Schema 文件

所有項目的 Schema 已在此工作區保存:

1. ✅ `/home/node/.openclaw/workspace/anime-office-dashboard/supabase_schema.sql`
2. ✅ `/home/node/.openclaw/workspace/temp_todo_list/supabase-schema.sql`
3. ✅ `/home/node/.openclaw/workspace/exam-system-backend/schema.sql`

---

## 🎯 下一步行動

### 緊急（需要用戶協助）:
1. **提供 Supabase API Key** - 目前無法訪問數據庫
2. **提供 Database Password** - 用於 pg_dump 導出
3. **確認各項目的實際狀態** - 哪些正在使用，哪些已棄用

### 自動化建議:
```bash
# 建議添加 Cron 任務進行定期備份
# supabase db backup --project-ref [REF]
```

---

## 📝 備注

- **exam-system-prod** 不是 Supabase 項目，需要單獨處理
- **temp_todo_list** 可能已棄用（名稱有 "temp_" 前綴）
- 所有項目都是 **測試/開發環境**，建議為生產環境設置自動備份

---

*報告生成時間: 2026-02-20 00:01*
*任務類型: cron:88decc06-28f3-467f-9314-fbcc0e671db2*
