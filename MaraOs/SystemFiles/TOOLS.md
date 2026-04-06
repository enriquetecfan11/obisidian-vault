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

Add whatever helps you do your job. This is your cheat sheet.

## Current Ops Routing (Discord + Telegram)

- Discord channel → agent bindings (guild `413791825607000067`):
  - `tecnofanaticos` (`1484990924676268145`) → `main`
  - `#mara-os` (`1484934389228566802`) → `atlas`
  - `#mara-os` (`1484934357767684096`) → `arvis`
  - `#warren` (`1484934434674311288`) → `scout` (Warren)
  - `#mara-os` (`1484934172010217763`) → `main`

- Delivery policy requested by Quique:
  - Keep Telegram daily summaries.
  - Also post each agent’s Obsidian/output summaries in its Discord channel.

- Specific override:
  - `Mara changelog diario Obsidian (Discord)` must post to `1484997198084182186` (NOT `tecnofanaticos`).

- Known issue to remember:
  - Some cron jobs can fail if OpenAI Codex OAuth token needs refresh.
