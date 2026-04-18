"""
🏆 World Cup Bet — Backend API

C'est le point d'entrée de ton serveur.

Pour lancer :
    uvicorn main:app --reload

Puis ouvre http://localhost:8000 dans ton navigateur.
"""

from fastapi import FastAPI

app = FastAPI(
    title="World Cup Bet API",
    version="0.1.0",
)


@app.get("/")
async def root():
    return {"message": "🏆 World Cup Bet API", "status": "online"}


@app.get("/health")
async def health():
    return {"status": "ok"}


# ----- À TOI DE JOUER ! -----
#
# Semaine 1, Mission 4 :
#   Ajoute GET /api/hello/{name} → {"message": "Salut {name} !"}
#
# Semaine 2, Mission 1 :
#   Ajoute GET /api/teams → retourne la liste des équipes
#
# Semaine 3, Mission 2 :
#   Ajoute GET /api/teams/{group} → équipes d'un groupe
# ----- À TOI DE JOUER ! -----
@app.get("/api/hello/{name}")
async def hello_name(name: str):
    return {"message": f"Salut name"}
# Données des groupes Coupe du Monde 2026
groups = {
    "A": ["Mexique", "Afrique du Sud", "Corée du Sud", "Tchéquie"],
    "B": ["Canada", "Bosnie-Herzégovine", "Qatar", "Suisse"],
    "C": ["Brésil", "Maroc", "Haïti", "Écosse"],
    "D": ["Etas Unis", "Paraguay", "Australie", "Turquie"],
    "E": ["France", "Italie", "Japon", "Nouvelle-Zélande"],
    "F": ["Espagne", "Allemagne", "Croatie", "Costa Rica"],
    "G": ["Argentine", "Angleterre", "Belgique", "Colombie"],
    "H": ["Portugal", "Pays-Bas", "Pologne", "Mexique"],
    "I": ["Uruguay", "Danemark", "Suède", "Norvège"],
    "J": ["Pérou", "Chili", "Équateur", "Venezuela"],
    "K": ["Nigeria", "Ghana", "Sénégal", "Cameroun"],
    "L": ["Arabie Saoudite", "Iran", "Irak", "Jordanie"]}


@app.get("/api/teams/{group}")
async def afficher_groupe(group: str):
    return {"teams": groups[group]}
