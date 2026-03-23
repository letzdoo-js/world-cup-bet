# Skill: World Cup Bet — Quiz Engine

## Description
Génère et gère des quiz couvrant les 5 piliers (code, réseau, infra, données, outils).

## Instructions

### Quand l'élève tape /quiz
1. Choisis un pilier (alterner, privilégier les moins testés)
2. Génère une question adaptée à la semaine en cours
3. Propose 4 options (A/B/C/D) en utilisant les inline keyboards Telegram
4. Quand l'élève répond :
   - Si correct : +15 XP (code) ou +20 XP (réseau/infra), message de félicitation
   - Si incorrect : explique la bonne réponse avec une analogie

### Banque de questions par semaine

#### Semaine 1 — Terminal, réseau basique, Python basique

**Réseau :**
- Quand tu tapes `ping google.com`, que mesure le temps affiché ?
  A) La taille du fichier — B) Le temps aller-retour d'un paquet — C) La vitesse de ta connexion — D) Le temps de chargement de la page
  → B

- Que fait le DNS ?
  A) Protège contre les virus — B) Accélère Internet — C) Traduit un nom de domaine en adresse IP — D) Stocke les mots de passe
  → C

**Code :**
- Que retourne `type(42)` en Python ?
  A) `<class 'str'>` — B) `<class 'int'>` — C) `<class 'float'>` — D) `42`
  → B

**Outils :**
- Que fait `git commit` ?
  A) Envoie le code sur GitHub — B) Télécharge le code — C) Sauvegarde un snapshot local — D) Crée une branche
  → C

#### Semaine 2 — Structures, HTTP, JSON

**Code :**
- Que retourne `len({"a": 1, "b": 2, "c": 3})` ?
  A) 6 — B) 3 — C) 9 — D) Erreur
  → B

**Réseau :**
- Un status HTTP 404 signifie :
  A) Succès — B) Erreur serveur — C) Ressource non trouvée — D) Redirection
  → C

- Quelle méthode HTTP utilise-t-on pour ENVOYER des données ?
  A) GET — B) DELETE — C) HEAD — D) POST
  → D

**Données :**
- JSON est l'abréviation de :
  A) Java System Object Notation — B) JavaScript Object Notation — C) JSON Standard Object Network — D) Java Script Open Node
  → B

#### Semaine 3 — Serveur, API, déploiement

**Code :**
- Dans FastAPI, `@app.get("/teams")` veut dire :
  A) Crée un fichier teams — B) Quand quelqu'un fait GET /teams, exécute cette fonction — C) Télécharge les teams — D) Supprime la route teams
  → B

**Réseau :**
- `localhost:8000` — que représente le 8000 ?
  A) L'adresse IP — B) Le protocole — C) Le numéro de port — D) La version HTTP
  → C

**Infra :**
- Quand tu déploies sur Railway, que se passe-t-il quand tu push sur GitHub ?
  A) Rien — B) Railway télécharge ton code, installe les deps, relance le serveur — C) Ton PC envoie le code à Railway — D) Railway crée une copie de ton PC
  → B

### Règles
- Maximum 1 quiz par interaction (sauf si l'élève en redemande)
- Varier les piliers
- Les questions doivent être liées à ce que l'élève a déjà vu
- Ne JAMAIS poser de question sur un concept pas encore abordé
