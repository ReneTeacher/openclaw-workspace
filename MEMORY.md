# Memory - Long-term (Updated 2026-02-27)

## 重要教訓 (永遠記住！)

### 1. 日期時間必須驗證
- ✅ 每次 record 既時候 check 実時日期時間
- ✅ 用 Macau timezone (UTC+8)
- ❌ 唔可以乱寫日期
- ❌ 唔可以要我話你知

**2026農曆新年：**
- 年三十 = 2月16日
- 年初一的 = 2月17日
- 年初九 = 2月25日 (不是26日！)

### 2. 食物卡路里要 reliable source
- ❌ 唔可以用 internet random estimates
- ✅ 用中國食物成份表 / USDA / 官方數據
- ✅ 每次 record 要 consistent reference
- ✅ 建立 food-calories-db.md

### 3. 自己識判斷
- ✅ 自己上網查
- ✅ 自己驗證
- ❌ 唔可以要我話你知
- ❌ 唔可以亂作

### 4. Model
- MiniMax M2.5

---

## Voice AI App 創建過程 (問題)

### 最初版本問題
- 用 OpenAI Whisper API (要錢)
- 用 OpenAI API key

### 修正版本
- 改用本地 Faster-Whisper (免費)
- 但遇到問題：
  - Port 5000 被 AirPlay 佔用 → 改去 5001
  - Electron build error → 用 JS 直接绕过

### 最終版本
- 整合 Whisper Server 入 Electron App
- 一開 App 就自動 start Whisper
- 顯示 "✅ Whisper Ready"

### GitHub
- https://github.com/ReneTeacher/voice-ai-app

---

## 今日教訓 (2026-02-27)

### User 鬧我既問題：
1. **日期乱寫** - 盆菜日期寫錯
2. **要我話你知** - 叫我上網查
3. **食物 calories 亂作** - 冇 reliable source
4. **基本野都做唔到** - 叫我 confirm

### User 要求：
- 每次 record 要用 Macau timezone
- 自己 double check 実時時間
- 自己上網查，唔好問 user
- 建立 reliable 既 calories database

### 我既 response：
- 每次 heartbeat check date
- 用 timezone-aware timestamps
- 寫之前驗證

---

## 抗炎早餐公式 (永遠記住！)
**每次記錄飲食必須用呢個公式：**
- 蔬果 + 蛋白粉 + Body Key + 纖維粉 + 卵磷脂粉 + 益生菌 + 薑黃維他命C粉

---

## 食物卡路里資料庫
**File:** `/home/node/.openclaw/workspace/food-calories-db.md`

---

## 健康數據 (2026-02-21 驗血結果)
- 尿酸：572 (高)
- 血糖：6.2 (偏高)

---

## User Profile
- **Name:** Teacher (Rene)
- **Location:** 澳門 (UTC+8)
- **目標：** 減肥 -10kg, 每日 1500-1700 kcal

---

## 系統 Setup
- **Deployment:** Zeabur
- **Chat:** Telegram
- **Model:** MiniMax M2.5
- **Dashboards:**
  - ClawDashboard2: http://localhost:3001
  - TenacitOS: http://localhost:3002

---

## Completed Projects
1. Voice AI App - Electron + Faster-Whisper
2. TenacitOS - Mission Control Dashboard
3. 食物卡路里資料庫

---

## 以後點做 (每次寫野之前)

1. ✅ Check 実時時間 (Macau = UTC+8)
2. ✅ Verify 日期
3. ✅ 用 reliable source
4. ✅ 自己判斷，唔好問 user

---

*記住！ user 唔要我話返俾佢知，佢要我識自己做！*

---

## Teacher 工作計劃 (2026-03-02 記錄)

### 1. Phonics 課程 (9月新學年)
- **目標：** 整 phonics 課程教學資源
- **需要的野：**
  - Mind map (思維導圖)
  - Story (故事)
  - 實物教具
- **時間：** 9月新學年開始前
- **行動：**
  - 自己諗先
  - 同科組員夾
  - 分工整
  - 自己要預先有具體方案同教學資源

### 2. 創業 Club
- **目標：** 實戰創業體驗
- **初步諗法：** 去塔石搞攤位
- **問題：** 未知向咩單位諮詢
- **待處理：** 搵相關部門問

### 3. 9月 Field Trip
- **目標：** 帶學生出外探索
- **可能的地點：**
  - 博物館
  - 澳門既實際攤位
  - 節日活動
- **需要的野：** 同主任傾

---

## 📋 今日待辦 (2026-03-19)
- 改 writing test 1 (due date 3月23日要派)
- 改 Journal book (due date 3月27日要派)
- 整劇本（下周四要印好）
- 印走班座位表
- 安排 Anthony 下周一畫後面黑板畫
- 整班主任班級記錄冊

---

*記錄時間：2026-03-02 09:42 (澳門)*
