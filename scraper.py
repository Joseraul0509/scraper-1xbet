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

            await page.goto("https://1xbet.com")
            await page.wait_for_timeout(2000)

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

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("scraper:app", host="0.0.0.0", port=10000)
