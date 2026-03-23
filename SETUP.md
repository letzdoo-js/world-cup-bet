# 🚀 Guide de setup — Sprint 0

Tout ce qu'il faut faire pour que le projet soit prêt au lancement.

---

## 1. Bot Telegram via @BotFather (5 min)

1. Ouvre Telegram, cherche `@BotFather`
2. Envoie `/newbot`
3. Nom du bot : `World Cup Bet Coach`
4. Username : `worldcupbet_coach_bot` (ou un nom dispo)
5. **Copie le token** → tu en auras besoin pour nanobot
6. Configure les commandes : envoie à @BotFather :
```
/setcommands
```
Puis sélectionne ton bot et colle :
```
mission - 🎯 Mission du jour
hint - 💡 Indice pour la mission en cours
done - ✅ Marquer la mission comme terminée
quiz - 🧠 Quiz code/réseau/infra
whatis - 📡 Explique un concept (ex: /whatis DNS)
debug - 🔍 Aide au debugging
progress - 📊 Ma progression
code - 📝 Soumettre du code pour review
```

7. Récupère le Telegram ID de ton fils :
   - Il doit envoyer un message à `@userinfobot`
   - Et le tien aussi

---

## 2. Repo GitHub (5 min)

1. Va sur https://github.com/new
2. Nom : `worldcup-bet`
3. Public (les amis doivent pouvoir voir)
4. **Ne coche PAS** "Add a README" (on a le nôtre)
5. Crée le repo

Puis push le code du Sprint 0 :
```bash
cd worldcup-bet/
git init
git add .
git commit -m "Sprint 0 : structure du projet"
git branch -M main
git remote add origin https://github.com/TON_USERNAME/worldcup-bet.git
git push -u origin main
```

6. **Active GitHub Codespaces** :
   - Settings → Codespaces → Active
   - Ton fils ouvrira VS Code en ligne via : `github.com/TON_USERNAME/worldcup-bet` → bouton "Code" → "Codespaces" → "Create codespace"

---

## 3. Vercel (5 min)

1. Va sur https://vercel.com
2. Connecte avec GitHub
3. "Import Project" → sélectionne `worldcup-bet`
4. Framework : **Other**
5. Root Directory : `frontend`
6. Deploy

Tu auras une URL type `worldcup-bet-xxxxx.vercel.app`
La page "Coming Soon" sera visible immédiatement.

Chaque push sur `main` redéploiera automatiquement.

---

## 4. Nanobot sur ton lab (15 min)

Sur ta machine lab :

```bash
# Installe nanobot
pip install nanobot-ai

# OU depuis les sources (recommandé vu que tu contribues)
git clone https://github.com/HKUDS/nanobot.git
cd nanobot
pip install -e .

# Initialise
nanobot onboard
```

Copie la config dans `~/.nanobot/config.json` :
```json
{
  "providers": {
    "openrouter": {
      "apiKey": "sk-or-v1-TA_CLE_OPENROUTER"
    }
  },
  "agents": {
    "defaults": {
      "model": "anthropic/claude-sonnet-4"
    }
  },
  "channels": {
    "telegram": {
      "enabled": true,
      "token": "LE_TOKEN_BOTFATHER",
      "allowFrom": [
        "ID_TELEGRAM_FILS",
        "ID_TELEGRAM_JEROME"
      ]
    }
  },
  "tools": {
    "web": {
      "search": {
        "apiKey": "TA_CLE_BRAVE_SEARCH"
      }
    }
  }
}
```

Copie les skills et le workspace :
```bash
# Copie les skills custom dans nanobot
cp -r worldcup-bet/clawbot/skills/* ~/.nanobot/skills/
cp -r worldcup-bet/clawbot/workspace/* ~/.nanobot/workspace/
```

Lance le bot :
```bash
nanobot gateway
```

Teste : envoie `/start` au bot sur Telegram.

### Cron pour la mission quotidienne (17h)
```bash
nanobot cron add \
  --name "daily_mission" \
  --message "Envoie la mission du jour à l'élève. Lis progress.json pour savoir où il en est, puis lis curriculum.json pour trouver la bonne mission. Commence par un message motivant lié au foot." \
  --cron "0 17 * * *"
```

### Cron pour le rappel (si inactif 48h)
```bash
nanobot cron add \
  --name "inactivity_reminder" \
  --message "Vérifie progress.json. Si last_active date de plus de 48h, envoie un message d'encouragement sympa à l'élève. Style : 'Hé ! Le match commence bientôt, ta feature aussi ?'" \
  --cron "0 18 * * *"
```

### Cron pour le quiz (mardi et vendredi)
```bash
nanobot cron add \
  --name "quiz" \
  --message "Envoie un quiz à l'élève. Alterne les piliers (code, réseau, infra, données, outils). Adapte la difficulté à la semaine en cours dans progress.json." \
  --cron "0 16 * 2,5"
```

---

## 5. Vérification finale

- [ ] Bot Telegram répond à `/start`
- [ ] Repo GitHub accessible et contient le Sprint 0
- [ ] GitHub Codespaces lance un VS Code fonctionnel
- [ ] Page "Coming Soon" visible sur Vercel
- [ ] Nanobot tourne sur le lab, connecté au bot Telegram
- [ ] Cron de mission quotidienne configuré
- [ ] Clé API Claude/OpenRouter fonctionnelle

---

## 6. Session de lancement avec ton fils (1h)

### Déroulé suggéré

**10 min — Le projet**
"Tu vas construire une app que tes amis vont utiliser pour parier
sur la Coupe du Monde. De zéro. Toi, le code, et moi pour t'aider."

**10 min — Les outils**
Montre-lui GitHub, Vercel, le terminal, le bot Telegram.
"Tout ça, tu vas comprendre comment ça marche, pas juste l'utiliser."

**10 min — Codespaces**
Ouvre GitHub Codespaces ensemble. "C'est ton VS Code, dans le cloud."

**15 min — Premier contact avec ClawBot**
Il envoie `/start` au bot. Puis `/mission` pour sa première mission.

**15 min — Première mission ensemble**
Faites la mission `w1m1` (terminal) ensemble. Il tape, tu expliques.
Il envoie `/done` quand c'est fini. Première dose de XP ! 🎉

---

*Quand tout est prêt, envoie "c'est bon" à ClawBot et on démarre !*
