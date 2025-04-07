from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from bs4 import BeautifulSoup
import requests
import uvicorn

app = FastAPI()

# CORS habilitado
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

HEADERS = {
    "User-Agent": "Mozilla/5.0",
    "Accept-Language": "es-ES,es;q=0.9",
    "Referer": "https://1xbet.com/"
}

@app.get("/")
def root():
    return {"mensaje": "Microservicio de cuotas 1xBet activo"}

@app.get("/api/cuotas")
def obtener_cuotas(equipo: str = Query(...), deporte: str = Query("futbol")):
    try:
        # Simulación de URL (esto cambia según el deporte real)
        url = f"https://1xbet.com/es/search/?query={equipo}"

        response = requests.get(url, headers=HEADERS, timeout=10)
        if response.status_code != 200:
            return {"error": "No se pudo acceder a 1xBet"}

        soup = BeautifulSoup(response.text, "html.parser")
        
        # Aquí debes ajustar el scraping a la estructura real de 1xBet
        # Esto es un ejemplo representativo:
        cuotas = {
            "ganador_local": 1.75,
            "empate": 3.20,
            "ganador_visita": 4.10,
            "over_2.5": 1.95,
            "under_2.5": 1.80,
            "handicap_local_-1": 2.50
        }

        return {"equipo": equipo, "cuotas": cuotas}

    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    uvicorn.run("scraper:app", host="0.0.0.0", port=3000)
