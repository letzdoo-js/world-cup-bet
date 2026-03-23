# 🏆 World Cup Bet

Application de pronostics pour la Coupe du Monde 2026.

**Construit de zéro par un dev de 14 ans.** 💪

## C'est quoi ?

Une app web où toi et tes amis pouvez :
- 📝 Parier sur les matchs de la Coupe du Monde
- 🏅 Voir le classement en temps réel
- 🎖️ Gagner des badges
- 📊 Suivre vos stats

## Stack technique

| Quoi | Techno |
|------|--------|
| Backend | Python + FastAPI |
| Frontend | React |
| Base de données | SQLite → Turso |
| Hébergement backend | Railway |
| Hébergement frontend | Vercel |
| Bot Telegram | nanobot |
| IA | Claude (Anthropic) |

## Lancer en local

```bash
# Backend
cd backend
uv sync
uvicorn main:app --reload

# Frontend
cd frontend
npm install
npm run dev
```

## Structure

```
worldcup-bet/
├── backend/         ← API Python/FastAPI
├── frontend/        ← App React
├── clawbot/         ← Bot Telegram (nanobot) — hébergé séparément
└── .devcontainer/   ← Config VS Code en ligne
```

## Journal de bord

> _Semaine 1 : ..._
> _À remplir au fur et à mesure !_
