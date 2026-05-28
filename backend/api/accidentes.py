from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from core.database import get_db
from models.accidentes import Accidente
from typing import List
from pydantic import BaseModel
from datetime import datetime
import json
import os
from fastapi_cache.decorator import cache

router = APIRouter()

# Schema para Pydantic
class AccidenteOut(BaseModel):
    id: int
    fecha: datetime
    latitud: float
    longitud: float
    gravedad: str
    tipo: str
    zona: str
    clima: str

    class Config:
        orm_mode = True
        from_attributes = True

@router.get("/historico")
@cache(expire=60)
def get_historico_accidentes(db: Session = Depends(get_db)):
    """
    Retorna el histórico de accidentes (útil para el Módulo 1).
    Usa caché (60s) para evitar sobrecarga y lee desde JSON local si la DB está vacía.
    """
    accidentes = db.query(Accidente).limit(100).all()
    # Si la base de datos está vacía, devolvemos datos locales descargados
    if not accidentes:
        data_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "incidentes.json")
        try:
            with open(data_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return data[:100] # Devolver solo 100 para no saturar
        except FileNotFoundError:
            return {"error": "No se encontraron datos locales ni en la base de datos."}
    return accidentes

@router.get("/prediccion")
@cache(expire=60)
def predict_zonas_criticas():
    """
    Simulación de la predicción de zonas críticas (Módulo 1)
    Aquí integraremos el modelo de Machine Learning
    """
    return {
        "zonas_criticas": [
            {"zona": "Laureles", "probabilidad_accidente": 0.85, "motivo": "Alto flujo + Lluvia"},
            {"zona": "Poblado", "probabilidad_accidente": 0.65, "motivo": "Congestión extrema"}
        ]
    }
