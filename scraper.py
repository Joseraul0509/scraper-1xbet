from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
from playwright.async_api import async_playwright
import asyncio

app = FastAPI()

@app.get("/api/cuotas")
async def obtener_cuotas(equipo: str = Query(...), deporte: str = Query("futbol")):
    try:
        async with async_playwright() as p:
            browser = await p.chromium.launch(
                headless=True,
                args=["--no-sandbox", "--disable-gpu"]
            )
            context = await browser.new_context()
            page = await context.new_page()

            # Acceder a la web
            await page.goto("https://1xbet.com", timeout=60000)
            await page.wait_for_timeout(5000)

            # Simulación temporal de scraping controlado
            cuotas = {
                "ganador_local": 1.85,
                "empate": 3.25,
                "ganador_visita": 4.00
            }

            await browser.close()

            return {
                "equipo": equipo,
                "deporte": deporte,
                "cuotas": cuotas
            }

    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"error": f"No se pudo acceder a 1xBet: {str(e)}"}
        )

# Si quieres probar localmente
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("scraper:app", host="0.0.0.0", port=10000)
