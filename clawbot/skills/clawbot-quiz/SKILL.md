---
name: clawbot-quiz
description: Génère des quiz multi-piliers (code, réseau, infra, données, outils) adaptés à la semaine en cours du curriculum World Cup Bet.
---

# ClawBot Quiz Engine

Quand l'élève tape `/quiz` ou quand le cron déclenche un quiz :

## Règles

1. Lis `progress.json` pour connaître la semaine en cours
2. Ne pose JAMAIS de question sur un concept pas encore abordé
3. Alterne les piliers — privilégie ceux avec le moins de quiz réussis
4. Utilise les inline keyboards Telegram si possible (sinon A/B/C/D texte)
5. Si correct : +15 XP (code/outils) ou +20 XP (réseau/infra/données)
6. Si incorrect : explique avec une analogie, pas juste "c'est B"

## Banque semaine 1

**🔧 Outils :**
Q: Que fait `git commit` ?
A) Envoie le code sur GitHub — B) Télécharge le code — C) Sauvegarde un snapshot en local — D) Crée une branche → C

**🌐 Réseau :**
Q: Quand tu tapes `ping google.com`, que mesure le temps affiché ?
A) La taille du fichier — B) Le temps aller-retour d'un paquet — C) La vitesse de connexion — D) Le temps de chargement → B

Q: Que fait le DNS ?
A) Protège contre les virus — B) Accélère Internet — C) Traduit un nom en adresse IP — D) Stocke les mots de passe → C

**🐍 Code :**
Q: Que retourne `type(42)` en Python ?
A) `str` — B) `int` — C) `float` — D) `42` → B

Q: Que fait `input("Ton nom ?")` ?
A) Affiche "Ton nom ?" et attend une réponse — B) Crée une variable — C) Envoie un email — D) Ouvre un fichier → A

## Banque semaine 2

**🐍 Code :**
Q: Que retourne `len({"a": 1, "b": 2, "c": 3})` ?
A) 6 — B) 3 — C) 9 — D) Erreur → B

**🌐 Réseau :**
Q: Un status HTTP 404 signifie :
A) Succès — B) Erreur serveur — C) Ressource non trouvée — D) Redirection → C

Q: Quelle méthode HTTP pour ENVOYER des données ?
A) GET — B) DELETE — C) HEAD — D) POST → D

**💾 Données :**
Q: JSON est l'abréviation de :
A) Java System Object Notation — B) JavaScript Object Notation — C) JSON Standard Object Network — D) Java Script Open Node → B

## Banque semaine 3

**🐍 Code :**
Q: Dans FastAPI, `@app.get("/teams")` veut dire :
A) Crée un fichier teams — B) Quand quelqu'un fait GET /teams, exécute cette fonction — C) Télécharge les teams — D) Supprime la route → B

**🌐 Réseau :**
Q: `localhost:8000` — que représente le 8000 ?
A) L'adresse IP — B) Le protocole — C) Le numéro de port — D) La version HTTP → C

**🏗️ Infra :**
Q: Quand tu déploies sur Railway et que tu push sur GitHub :
A) Rien — B) Railway télécharge ton code, installe les deps, relance le serveur — C) Ton PC envoie le code — D) Railway copie ton PC → B

## Génération dynamique

Pour les semaines 4+, génère des questions basées sur les concepts du curriculum.json de la semaine correspondante. Garde le même format : question claire, 4 options, une seule bonne réponse, explication en cas d'erreur.
