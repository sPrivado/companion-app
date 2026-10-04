from fastapi import FastAPI
from pydantic import BaseModel
from cerebro import responder

class MensajeEntrada(BaseModel):
    texto: str

app = FastAPI()

@app.get("/")
async def root():
    return {"mensaje": "Hola, soy el backend del companion"}

@app.get("/health")
async def health():
    return {"ok": True}

@app.post("/chat")
async def chat(mensaje: MensajeEntrada):
    return {"respuesta": responder(mensaje.texto)}