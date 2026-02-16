# TOOLS.md - Local Notes

Skills define _how_ tools work. This file is for _your_ specifics — the stuff that's unique to your setup.

## What Goes Here

Things like:

- Camera names and locations
- SSH hosts and aliases
- Preferred voices for TTS
- Speaker/room names
- Device nicknames
- Anything environment-specific

## Examples

```markdown
### Cameras

- living-room → Main area, 180° wide angle
- front-door → Entrance, motion-triggered

### SSH

- home-server → 192.168.1.100, user: admin

### TTS

- Preferred voice: "Nova" (warm, slightly British)
- Default speaker: Kitchen HomePod
```

## Why Separate?

Skills are shared. Your setup is yours. Keeping them apart means you can update skills without losing your notes, and share skills without leaking your infrastructure.

---

### Cloudflare Markdown for Agents

- **Skill**: `/app/skills/cloudflare-markdown-agents/SKILL.md`
- **Purpose**: Reduce token usage by ~80% when fetching web content
- **Usage**: Add `Accept: text/markdown` header to HTTP requests
- **Benefit**: Direct Markdown response instead of parsing HTML

```bash
# Example
node /app/skills/cloudflare-markdown-agents/cloudflare-markdown.js <url>
```

---

### API Connections Reference

- **Full Documentation**: `/home/node/.openclaw/workspace/skills/api-connections/SKILL.md`

**Quick Reference:**

| Service | Key Info |
|---------|----------|
| Supabase | URL: https://czolesxhhfiwzubvbmab.supabase.co |
| Midjourney API | https://mymidjourneyapi.zeabur.app/imagine |
| Discord Server | https://discord.gg/YcJ5ffjD |

---

### 3D Game Development

- **Three.js Skill**: `/home/node/.openclaw/workspace/skills/threejs-game-dev/SKILL.md`
- **3D Character Pipeline**: `/home/node/.openclaw/workspace/skills/3d-character-pipeline/SKILL.md`

**Resources:**
- Ready Player Me: https://readyplayer.me/
- Three.js Examples: https://threejs.org/examples/
- Midjourney API: https://mymidjourneyapi.zeabur.app

---

### Installed MCPs

| MCP | Status | 用途 |
|-----|--------|------|
| exa | ✅ Working | Web Search |
| context7 | ❌ Offline | Context Search |
