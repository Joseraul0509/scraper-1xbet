from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from playwright.sync_api import sync_playwright

app = FastAPI()

# CORS para permitir peticiones externas (ej. desde Hostinger)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"mensaje": "Microservicio 1xBet activo"}

@app.get("/api/cuotas")
def obtener_cuotas(equipo: str = Query(...)):
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            url = f"https://1xbet.com/es/search/?query={equipo}"
            page.goto(url, timeout=15000)
            page.wait_for_timeout(5000)  # esperar carga de cuotas

            html = page.content()
            browser.close()

            # Aquí simulas resultados (puedes luego extraer datos reales del HTML con BeautifulSoup)
            cuotas = {
                "ganador_local": 1.85,
                "empate": 3.25,
                "ganador_visita": 4.00
            }

            return {"equipo": equipo, "cuotas": cuotas}

    except Exception as e:
        return {"error": f"No se pudo acceder a 1xBet: {str(e)}"}
