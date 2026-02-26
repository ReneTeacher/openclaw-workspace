# Supabase 數據庫備份報告
**日期**: 2026年2月25日 上午12:00 (Asia/Hong_Kong)
**狀態**: 自動備份任務

---

## 📋 項目概覽

### 1. MyClawOffice (anime-office-dashboard)
- **數據庫平台**: ~~Supabase~~ → **Zeabur** (已遷移)
- **Supabase URL**: https://czolesxhhfiwzubvbmab.supabase.co
- **狀態**: ❌ **無法訪問** - DNS 解析失敗，Supabase 項目可能已刪除
- **Zeabur 部署**: ✅ 正常運行中

**已知 Schema 表結構** (保存在 `/anime-office-dashboard/supabase_schema.sql`):
- `agent_status` - Agent 狀態追蹤
- `cron_jobs` - Cron 任務配置  
- `system_metrics` - 系統指標
- `activity_log` - 活動日誌

**Zeabur 數據庫**: 表不存在於當前 Zeabur PostgreSQL

### 2. todo-list-prod
- **數據庫平台**: Supabase  
- **狀態**: ❌ 無法訪問
- **項目位置**: `/temp_todo_list/` (前綴 temp，可能已棄用)

**已知 Schema 表結構** (保存在 `/temp_todo_list/supabase-schema.sql`):
- `public.todos` - 待辦事項 (id, title, completed, created_at)

### 3. exam-system-prod
- **數據庫平台**: ~~Supabase~~ → **Zeabur PostgreSQL**
- **狀態**: ⚠️ 數據庫表不存在於當前服務器

**預期 Schema 表結構** (保存在 `/exam-system-backend/schema.sql`):
- `users` - 用戶 (student/teacher)
- `exams` - 考試
- `questions` - 問題
- `submissions` - 提交記錄

---

## 🔍 訪問測試結果

| 項目 | 結果 | 備註 |
|------|------|------|
| Supabase URL DNS 解析 | ❌ 失敗 | czolesxhhfiwzubvbmab.supabase.co 無法解析 |
| Zeabur PostgreSQL 連接 | ✅ 成功 | 可連接至 service-698d6557d47fc6c4e5b9e122 |
| anime-office 表 | ❌ 不存在 | Zeabur DB 中無 agent_status, cron_jobs 等表 |
| exam-system 表 | ❌ 不存在 | Zeabur DB 中無 users, exams, questions, submissions 表 |
| todo-list 表 | ❌ 不存在 | Zeabur DB 中無 todos 表 |

### Zeabur PostgreSQL 當前表 (部分):
```
users, project, workflow_entity, execution_entity, 
solid_queue_jobs, settings, variables, etc.
```
這看起來是 OpenClaw 系統自身的數據庫，不是項目數據庫。

---

## 📁 已保存的 Schema 文件

1. ✅ `/home/node/.openclaw/workspace/anime-office-dashboard/supabase_schema.sql`
2. ✅ `/home/node/.openclaw/workspace/temp_todo_list/supabase-schema.sql`
3. ✅ `/home/node/.openclaw/workspace/exam-system-backend/schema.sql`

---

## ⚠️ 重要發現

### Supabase 項目狀態
- **所有 Supabase 項目 URL 無法訪問** - 項目可能已被刪除或帳戶問題
- 需要登入 Supabase Dashboard 確認項目狀態

### Zeabur 數據庫
- 當前 Zeabur PostgreSQL 包含 OpenClaw 系統表
- **項目數據庫未找到** - 可能需要個別的數據庫實例

### 建議行動
1. 確認 Supabase 帳戶和項目狀態
2. 如果項目已遷移到 Zeabur，確認數據庫連接資訊
3. 考慮為每個項目建立獨立的 Zeabur PostgreSQL 數據庫

---

## 💡 備份建議

### 1. 確認項目位置 (立即行動)
```bash
# 登入 Supabase Dashboard
https://app.supabase.com

# 檢查項目是否仍存在
# 如果不存在，需要重建或從備份恢復
```

### 2. 如果使用 Zeabur 托管數據庫:
```bash
# 透過 Zeabur Dashboard 備份
# 1. 登入 https://zeabur.com
# 2. 進入 PostgreSQL 服務 → Backups
# 3. 創建手動備份

# 或使用 pg_dump
pg_dump "postgresql://root:[PASSWORD]@host:5432/database" > backup.sql
```

### 3. 對於空缺數據庫:
- 項目可能尚未配置數據庫
- 或數據庫已刪除/遷移
- 建議檢查項目配置

---

## 🎯 結論

**無法完成自動備份** - 目標數據庫不存在或無法訪問

### 需要用戶協助:
1. **登入 Supabase Dashboard** 確認 MyClawOffice 等項目是否仍存在
2. **確認項目數據庫位置** - 是否已遷移至 Zeabur 或其他地方
3. **提供正確的數據庫連接資訊** - 如果項目數據庫在其他位置
4. **檢查 Zeabur 帳戶** - 確認每個項目是否有獨立數據庫

### 現有資源:
- ✅ 所有預期 Schema 定義已保存為 SQL 文件
- ⚠️ 需要用戶確認項目數據庫狀態

---

*報告生成時間: 2026-02-25 00:00*
*任務類型: cron:88decc06-28f3-467f-9314-fbcc0e671db2*
