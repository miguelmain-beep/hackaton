from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# IMPORTANTE: Aquí importamos tu archivo .py como un módulo de Python
from backend.api.clima_rutas import router as rutas_gubernamentales

app = FastAPI()

# Habilitar CORS para que tu HTML pueda leer la API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(rutas_gubernamentales, prefix="/api/rutas")