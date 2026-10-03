from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"mensaje": "Hola, soy el backend del companion"}

@app.get("/health")
async def health():
    return {"ok": True}