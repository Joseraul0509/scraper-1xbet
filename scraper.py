from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
from playwright.async_api import async_playwright
import asyncio

app = FastAPI()

@app.get("/api/cuotas")
async def obtener_cuotas(equipo: str = Query(...), deporte: str = Query("futbol")):
    try:
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            context = await browser.new_context()
            page = await context.new_page()

            # Aquí usarías una URL real de 1xBet
            await page.goto("https://1xbet.com")

            await page.wait_for_timeout(2000)  # Espera 2 segundos (ajusta si es necesario)

            # Simulación de búsqueda (ajustar a lo real si scrapeas)
            cuotas = {
                "ganador_local": 1.85,
                "empate": 3.25,
                "ganador_visita": 4.00
            }

            await browser.close()
            return {"equipo": equipo, "cuotas": cuotas}

    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"error": f"No se pudo acceder a 1xBet: {str(e)}"}
        )
