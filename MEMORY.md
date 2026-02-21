# Memory - Long-term (Updated 2026-02-21)

## 抗炎早餐公式 (永遠記住！)
**每次記錄飲食必須用呢個公式：**
- 蔬果 + 蛋白粉 + Body Key + 纖維粉 + 卵磷脂粉 + 益生菌 + 薑黃維他命C粉
- **絕對唔好寫錯！**

---

## 健康數據 (2026-02-21)
**尿酸：572 µmol/L** (正常 <420) — 超標，需要戒口 + 睇醫生
**血糖：6.2 mmol/L** (正常空肚 <6.1) — 偏高少少

### 尿酸高既飲食建議
- 戒高嘌呤食物：海鮮、內臟、老火湯、啤酒
- 多飲水：每日2-3公升
- 少食紅肉
- 多食蔬菜水果

---

## ClawDashboard2 Protocol (重要！)

**安裝：** 2026-02-17，運行於 http://localhost:3001

**每次開工/完工必須：**
1. **開工前**：更新 PROJECT.md 既 `## Status` 為 `🔵 working — [任務名]` 或 `🟠 building — [任務名]`
2. **完工後**：更新 status 回 `🟢 idle`，並係 `## Tasks` 打勾 `✅`，係 `## Log` 新增記錄
3. **每週檢查**：確保所有 sub-agents 既 PROJECT.md 都存在

**PROJECT.md 位置：** /home/node/.openclaw/workspace/PROJECT.md

**格式範例：**
```markdown
## Status
🟢 idle

## Tasks
- [x] 2026-02-17 安裝 ClawDashboard2

## Log
- 2026-02-17 19:30 安裝成功
```

---

## User Profile
- **Role**: Junior high school English teacher, English department head, homeroom teacher
- **Location**: Macau (lives and works in Macau)
- **Teaching Focus**: Lesson planning, class management, English education

## System Setup
- **Deployment**: Zeabur (Linux server)
- **Chat**: Telegram
- **AI Model**: MiniMax M2.5
- **GitHub Token**: Configured (for automation)

## GitHub Repos (All Synced)
| Repo | Type | Purpose | Status |
|------|------|---------|--------|
| `ReneTeacher/Coding-Projects` | Public | Student tools | ✅ Synced |
| `ReneTeacher/My-Private-Apps` | Private | Personal apps | ✅ Synced |
| `ReneTeacher/todo-list` | Private | To-Do App | ✅ Synced |
| `ReneTeacher/exam-system` | Private | Exam System | ✅ Synced |

## Completed Projects
1. **Vocabulary Dictation** - dictation.py + Streamlit app
2. **To-Do List** - Private Streamlit app
3. **Exam System** - Streamlit + Supabase (simplified)
4. **Browser Automation** - Zeabur Sandbox (headless Chromium)

## Browser Automation
- **Service**: openclaw-sandbox-browser (Zeabur)
- **Status**: Working
- **URL**: `http://openclaw-sandbox-browser:9222`
- **Capabilities**: Open URLs, fill forms, click buttons, screenshots
- **Limitation**: Cannot send screenshots to Telegram

## Daily News Cron
- **Schedule**: 7:00 AM Hong Kong/Macau time daily
- **Status**: ✅ Fixed and Working
- **Target**: `telegram:8053707596`
- **Skill**: openclaw-news (`/app/skills/openclaw-news/SKILL.md`)

## Preferences
- Communication: Cantonese/Chinese mix, concise
- Likes: Simple solutions, one-time setup for long-term use
- Prefers: Streamlit for quick web apps, Telegram for communication

## Cost Optimization Note
User emphasized: "唔想痴痴講句簡單既嘢都燒好多錢"
- Keep responses concise when possible
- Use memory to avoid repeating explanations
- Optimize heartbeat checks

## Security Note
- ❌ NEVER store passwords or sensitive credentials in memory
- ❌ NEVER save credentials in files
- ✅ Only save project structure and configurations
- ✅ User manages their own passwords externally

## Technology Stack Decision
- **Simple Web Apps**: Streamlit + Supabase (NEW STANDARD)
- **CLI Tools**: Python scripts
- **Browser**: Zeabur Sandbox Browser

## Web Deployment Standard Flow (Streamlit + Supabase)
1. Supabase: New project → Settings > API → Copy URL + anon key
2. Database: SQL Editor > run `supabase-schema.sql`
3. Streamlit Cloud: Deploy > GitHub repo > Add secrets (URL + key)
4. Updates: I write code → push GitHub → Streamlit Redeploy

## Today Summary
- ✅ Fixed daily news cron job (added explicit Telegram delivery)
- ✅ Browser automation working with Zeabur sandbox
- ✅ Created openclaw-news skill with article format template
- ✅ All systems synced and documented
- ✅ User confirmed setup is working

## Key Learnings
1. Zeabur internal URLs require internal hostname, not `.zeabur.app`
2. Cron job delivery needs explicit channel specification
3. User prefers simple solutions over complex ones
4. User wants password/security concerns respected
5. Streamlit + Supabase is the preferred stack for web apps

## Today's Updates (2026-02-15)
### Model Upgrade
- Switched from MiniMax M2.1 to M2.5

### Daily Code Review Cron
- **Schedule**: 6:00 AM Hong Kong time daily (changed from 2:00 AM)
- **Task**: Auto-review all GitHub repos, fix small bugs, report big changes

### Discord Integration
- ✅ Successfully paired!
- **Server**: https://discord.gg/YcJ5ffjD
- **Channel ID**: 1448339661192826961
- **User can now chat via Discord**

### Midjourney Integration
- Created midjourney-api repo on GitHub
- Deployed to Zeabur: mymidjourneyapi.zeabur.app
- ❌ Issue: Library init fails - "Unexpected end of JSON input"
- **Recommendation**: Use Kie.ai API ($0.02/image) instead

### New Cron Jobs Added (Total: 7)
1. GitHub Repo Backup (0:00 daily)
2. Supabase Database Backup (0:00 daily)
3. Website Health Check (every 5 min) - currently paused
4. Weekly Code Summary (Mon 8:00 AM)
5. Weather Reminder (7:00 AM)
6. OpenClaw Daily News (7:00 AM)
7. Daily GitHub Code Review (6:00 AM)

### Multi-Agent Architecture
- Inspired by Threads @levelup.daily_lab: "1 Manager + N Specialist"
- Created improvement report with 10 creative ideas:
  1. Persona Switching
  2. Context Cascade
  3. Visual Dashboard
  4. Randomizer
  5. Task Boxing
  6. Thinking Export
  7. Night Mode
  8. Mobile Commands
  9. Carnival Mode
  10. Voice Memory

### Anime Office Dashboard
- Created anime-office-dashboard repo
- Created sync scripts to read OpenClaw data
- **Supabase**: https://czolesxhhfiwzubvbmab.supabase.co
- **Status**: Waiting for table setup in Supabase SQL Editor

### Tools Added
- Exa MCP (free web search) - replaced Brave Search due to quota limits

### Reports Created
1. multi-agent-improvement-report.md
2. midjourney-troubleshooting-report.md
