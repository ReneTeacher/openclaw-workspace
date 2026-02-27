# Memory - Long-term (Updated 2026-02-27)

## 抗炎早餐公式 (永遠記住！)
**每次記錄飲食必須用呢個公式：**
- 蔬果 + 蛋白粉 + Body Key + 纖維粉 + 卵磷脂粉 + 益生菌 + 薑黃維他命C粉
- **絕對唔好寫錯！**

---

## 健康數據 (2026-02-21 驗血結果)
**尿酸：572 µmol/L** (正常 <420) — 超標，需要戒口 + 睇醫生
**血糖：6.2 mmol/L** (正常空肚 <6.1) — 偏高少少

### 尿酸高既飲食建議
- 戒高嘌呤食物：海鮮、內臟、老火湯、啤酒
- 多飲水：每日2-3公升
- 少食紅肉
- 多食蔬菜水果

---

## 食物卡路里資料庫
**File:** `/home/node/.openclaw/workspace/food-calories-db.md`

**用途：** 記錄所有食物既 calories，以後 record 飲食可以 reference

### 常見食物 Reference
| 食物 | 份量 | kcal |
|------|------|------|
| 白飯 | 100g | 130 |
| 牛腩 (瘦) | 100g | ~200 |
| 牛腩麵 | 1碗 | ~500-600 |
| 豉油雞 | 100g | ~200 |
| 炸雞柳 | 100g | ~200 |
| 炸雞軟骨 | 10粒 | ~150 |
| 炸魷魚 | 100g | ~300 |
| Healthy Mix | 1份 | ~346 |
| 椰菜 (煮) | 100g | ~30 |
| 青瓜 | 100g | ~15 |

**更新記錄：**
- 2026-02-27: 初始化，由 user feedback 修正

---

## ClawDashboard2 Protocol (重要！)

**安裝：** 2026-02-17，運行於 http://localhost:3001

**每次開工/完工必須：**
1. **開工前**：更新 PROJECT.md 既 `## Status` 為 `🔵 working — [任務名]` 或 `🟠 building — [任務名]`
2. **完工後**：更新 status 回 `🟢 idle`，並係 `## Tasks` 打勾 `✅`，係 `## Log` 新增記錄
3. **每週檢查**：確保所有 sub-agents 既 PROJECT.md 都存在

**PROJECT.md 位置：** /home/node/.openclaw/workspace/PROJECT.md

---

## Voice AI App (最重要！)

**Purpose:** 整一個 Typeless 既 Voice Dictation App — 用本地 Whisper，免費！

**GitHub:** https://github.com/ReneTeacher/voice-ai-app

**Tech Stack:**
- Electron (Desktop App)
- React + TypeScript
- Vite
- Faster-Whisper (本地運行，免費！)

**Features:**
- 🎙️ Voice Recording - Click to record, click again to stop
- 🆓 100% Free - 用本地 Whisper，唔洗 API key
- ✨ AI Polishing (Optional) - 可以加 OpenAI key
- 📋 One-click Copy
- ⌨️ Global Shortcut: Ctrl+Shift+V

**最重要既 Feature — 整合 Whisper Server：**
- Electron App 會自動 spawn Whisper server
- 一開 App 就會自動 start，唔洗另外開 Terminal
- 顯示 "✅ Whisper Ready" 先可以錄音

**Setup 教學 (Mac):**
```bash
# 1. Install
cd ~/Desktop/voice-ai-app
git pull
npm install
npm run dist

# 2. Install DMG
open release/Voice*.dmg

# 3. 一開就用到！
```

**Build 問題解決：**
- Port 5000 被 AirPlay 佔用 → 改去 5001
- Electron build 需要 tsc compile → 直接用 JS 绕过

---

## TenacitOS (Mission Control Dashboard)

**Purpose:** OpenClaw 既靚 dashboard，有 3D Office！

**GitHub:** https://github.com/ReneTeacher/tenacitOS

**Status:** 
- ✅ Code 已 push
- ❌ Zeabur version 讀取唔到 data (因為係另一部 server)

**解決方案：**
1. 用本地 version (localhost:3002) — 但要用 VPN
2. Deploy 去 Zeabur — 要改 code 去讀取 GitHub

---

## OpenWork (Open Source Claude Cowork 替代品)

**User 想搵既野：**
- OpenSource 既 Claude Cowork 替代品
- 數據要 privacy (local-first)

**發現既 Solution：**
- **OpenCode** - Open source AI coding agent
- **OpenWork** - OpenCode 既 Desktop GUI
- **官網:** https://openwork.software

**佢既 Features:**
- ✅ Desktop GUI
- ✅ Support Claude, GPT, Gemini, Ollama
- ✅ Local-first (數據唔出門)
- ✅ Workflows & Skills
- ✅ 免費！

**未來 Action:** 等 user 想 setup 先

---

## User Profile

- **Name:** Teacher (Rene)
- **Role:** 中學英文老師，英文科主任，班主任
- **Location:** 澳門 (NOT 香港)
- **Teaching Focus:** Lesson planning, class management, English education

**健康狀況 (2026-02-21):**
- 尿酸：572 (高)
- 血糖：6.2 (偏高)

**目標：**
- 減肥：-10kg
- 每日熱量：1500-1700 kcal

---

## 飲食記錄 (2026-02-27)

**目標：** 1500-1700 kcal | 蛋白質 80-100g | 碳水 150-200g | 脂肪 45-60g

### 2026-02-27
- 早餐：Healthy mix (~346 kcal) ✅
- 午餐：學校飯盒 — 豉油雞 + 椰菜 + 青瓜炒鯪魚肉 + 白飯 (~525 kcal) ✅
- 晚餐：牛記 — 牛腩撈麵 + 炸雞柳 + 炸雞軟骨 + 炸魷魚 (~1200 kcal)
- **總計：** ~2071 kcal ⚠️

### 2026-02-26
- 早餐：Healthy mix (~346 kcal) ✅
- 午餐：學校飯盒 — 平菇炒肉片 + 椰菜 + 飯 + 南瓜蒸排骨 (~515 kcal) ✅
- 晚餐：自己煮 — 西蘭花炒雞胸 + 瑤柱炒雞蛋 + 烚小白菜 + 紫薯 (~710 kcal) ✅
- **總計：** ~1571 kcal ✅ (達標！)

---

## System Setup

- **Deployment:** Zeabur (Linux server)
- **Chat:** Telegram
- **AI Model:** MiniMax M2.5
- **GitHub Token:** [CONFIGURED - REDACTED]

### Dashboards
- **ClawDashboard2:** http://localhost:3001 (經常崩潰，需手動重啟)
- **TenacitOS:** http://localhost:3002 (密碼: teacher2026)

### Cron Jobs (7個)
1. GitHub Repo Backup (0:00 daily)
2. Supabase Database Backup (0:00 daily) — **壞咗 (Supabase project 被刪)**
3. Website Health Check (every 5 min) — paused
4. Weekly Code Summary (Mon 8:00 AM)
5. Weather Reminder (7:00 AM)
6. OpenClaw Daily News (7:00 AM)
7. Daily GitHub Code Review (6:00 AM) — **壞咗 (GitHub token issue)**

### Supabase
- **URL:** https://czolesxhhfiwzubvbmab.supabase.co
- **Status:** DNS 解析失敗，可能已被刪除
- **受影響既 projects:**
  - anime-office-dashboard
  - todo-list-prod
  - exam-system-prod

---

## GitHub Repos

| Repo | Type | Purpose |
|------|------|---------|
| ReneTeacher/Coding-Projects | Public | Student tools |
| ReneTeacher/My-Private-Apps | Private | Personal apps |
| ReneTeacher/todo-list | Private | To-Do App |
| ReneTeacher/exam-system | Private | Exam System |
| ReneTeacher/tenacitOS | Public | Mission Control Dashboard |
| ReneTeacher/voice-ai-app | Public | Voice AI App (Typeless clone) |

---

## Completed Projects

1. **Vocabulary Dictation** - dictation.py + Streamlit app
2. **To-Do List** - Private Streamlit app
3. **Exam System** - Streamlit + Supabase
4. **Browser Automation** - Zeabur Sandbox
5. **Voice AI App** - Electron + Faster-Whisper ⭐ (最新！)
6. **TenacitOS** - Mission Control Dashboard

---

## User 既 Preferences

- **Communication:** Cantonese/中文 mix，簡潔
- **Likes:** 簡單既 solution，一次 setup 可以用好耐
- **Prefers:** Streamlit for quick web apps，Telegram for communication
- **Concerns:** 
  - 唔想燒太多錢 ("痴痴講句簡單既嘢都燒好多錢")
  - 要 privacy (唔放心將 data 放上 cloud)
  - 想學啲有技術性既野 (vibe coding)

---

## 重要教訓 (永遠記住！)

1. **Memory 既重要性：** User 鬧咗好多次「乜你唔記得㗎喇」，以後一定要將所有野寫低！
2. **營養資料：** 中國居民膳食指南得原則，唔係食物既 calories
3. **食物 calories 要 consistently reference 同一個 source**
4. **OpenClaw data location：** OpenClaw data 係 server 度，Zeabur deploy 既嘢讀取唔到
5. **Port 5000 被 AirPlay 佔用：** Mac 既問題，要用 5001

---

## 今日總結 (2026-02-27)

✅ **完成既野：**
- Voice AI App 整咗出嚟 — 第一個自己寫既 Desktop App！
- TenacitOS Setup 完成
- 食物卡路里資料庫建立
- 每日飲食繼續 record

⚠️ **問題：**
- Supabase 壞咗 (project 被刪)
- GitHub Code Review cron 壞咗
- Dashboard 經常崩潰

🎯 **下一步：**
- 等 user 想 setup OpenWork
- 繼續優化 Voice AI App
- 修補 cron jobs

---

*呢個 Memory file 會不斷更新，以後所有重要既野都會寫低曬！*
