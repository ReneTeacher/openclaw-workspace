# Calendar Templates for OpenClaw Memory System

## Folder Structure

```
memory/
├── calendar/
│   ├── 2026-02.md
│   └── 2026-03.md
├── templates/
│   ├── daily-note-template.md
│   └── monthly-note-template.md
└── daily/
    ├── 2026-02-12.md
    └── 2026-02-13.md
```

## Usage in Obsidian

### Option 1: Templater Plugin (Recommended)
1. Install **Templater** plugin
2. Set template folder to `memory/templates`
3. Create new notes with templates

### Option 2: Daily Notes Plugin
1. Enable **Daily Notes** plugin
2. Set format: `YYYY-MM-DD`
3. Set template: `memory/templates/daily-note-template.md`

### Option 3: Manual
1. Copy template file
2. Rename to date
3. Fill in content

## Integration with OpenClaw

OpenClaw automatically reads files in this folder and uses them to:
- Check your schedule
- Remind you of upcoming events
- Generate context-aware responses

## Sync

This folder syncs with:
- GitHub: ReneTeacher/openclaw-memory
- OpenClaw (Zeabur): Automatically pulls changes
