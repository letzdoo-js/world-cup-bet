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
@app.get("/api/hello/William")
async def hello_william():
    return {"message": "Salut William !"}
