# 🤖 ClawBot — Bot Telegram nanobot pour World Cup Bet

Coach de coding IA sur Telegram, propulsé par [nanobot](https://github.com/HKUDS/nanobot) + Claude.

## Qu'est-ce que c'est

Un bot Telegram qui guide un ado de 14 ans dans la construction d'une app de pronostics.
Il envoie des missions quotidiennes, des quiz, aide au debugging, et track la progression.

Le bot ne donne jamais la réponse — il guide avec des questions.

## Structure

```
clawbot/
├── setup.sh                  ← Script d'installation (lance ça)
├── config.json.template      ← Template de config nanobot
├── skills/
│   ├── clawbot-tutor/
│   │   └── SKILL.md          ← Personnalité + logique pédagogique
│   └── clawbot-quiz/
│       └── SKILL.md          ← Quiz multi-piliers
└── workspace/
    ├── curriculum.json        ← Toutes les missions (3 semaines)
    └── progress.json          ← Tracking progression élève
```

## Setup rapide

```bash
# 1. Clone ou copie ce dossier sur ton lab
# 2. Lance le setup
chmod +x setup.sh
./setup.sh

# 3. Édite la config
nano ~/.nanobot/config.json
# Remplace les REPLACE_... avec tes vraies clés

# 4. Lance
nanobot gateway

# 5. Teste : envoie /start au bot sur Telegram
```

## Pré-requis

1. **Token Telegram** : crée un bot via @BotFather, copie le token
2. **Clé OpenRouter** : https://openrouter.ai/keys (pour Claude)
3. **IDs Telegram** : envoie un message à @userinfobot pour avoir les IDs
4. **Python 3.11+** sur ton lab

## Commandes du bot

| Commande | Action |
|----------|--------|
| `/start` | Bienvenue + première mission |
| `/mission` | Mission du jour |
| `/done` | Valider la mission en cours |
| `/hint` | Indice sans donner la réponse |
| `/quiz` | Quiz code/réseau/infra |
| `/whatis <x>` | Explique un concept |
| `/debug <err>` | Aide au debugging guidé |
| `/progress` | XP, niveau, stats |
| `/code` | Soumettre du code pour review |

## Configurer les crons

```bash
# Mission quotidienne 17h
nanobot cron add --name "daily_mission" \
  --message "Envoie la mission du jour. Lis progress.json et curriculum.json." \
  --cron "0 17 * * *"

# Quiz mardi et vendredi 16h
nanobot cron add --name "quiz" \
  --message "Lance un quiz adapté à la semaine en cours." \
  --cron "0 16 * * 2,5"

# Rappel si inactif
nanobot cron add --name "reminder" \
  --message "Si last_active > 48h, envoie un encouragement foot+code." \
  --cron "0 18 * * *"
```

## Ajouter des semaines au curriculum

Édite `~/.nanobot/workspace/curriculum.json` et ajoute un bloc `week` en suivant le même format.
Le bot s'adapte automatiquement.
