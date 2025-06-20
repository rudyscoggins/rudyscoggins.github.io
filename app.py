from fastapi import FastAPI, Request, Response
from fastapi.staticfiles import StaticFiles

app = FastAPI()

@app.middleware("http")
async def add_no_cache_headers(request: Request, call_next):
    response: Response = await call_next(request)
    response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"
    return response

# Serve static files from the repository root
app.mount("/", StaticFiles(directory=".", html=True), name="static")

