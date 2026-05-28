from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from core.database import engine, Base
from api import accidentes, trafico, congestion, clima_rutas

# Caché
from fastapi_cache import FastAPICache
from fastapi_cache.backends.inmemory import InMemoryBackend

# Crear las tablas en la base de datos
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="moviliDATA - Backend API",
    description="API REST para la plataforma inteligente de movilidad urbana",
    version="1.0.0"
)

@app.on_event("startup")
async def startup():
    FastAPICache.init(InMemoryBackend(), prefix="fastapi-cache")


# Configurar CORS para permitir peticiones desde el Frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # En producción cambiar esto por el dominio real
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Registrar Routers
app.include_router(accidentes.router, prefix="/api/accidentes", tags=["Accidentes"])
app.include_router(trafico.router, prefix="/api/trafico", tags=["Tráfico"])
app.include_router(congestion.router, prefix="/api/congestion", tags=["Congestión"])
app.include_router(clima_rutas.router, prefix="/api/rutas", tags=["Rutas y Clima"])

@app.get("/")
def read_root():
    return {"message": "Bienvenido a la API de moviliDATA. Visita /docs para ver la documentación interactiva."}
