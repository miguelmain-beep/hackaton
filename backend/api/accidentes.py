from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from core.database import get_db
from models.accidentes import Accidente
from typing import List
from pydantic import BaseModel
from datetime import datetime

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

@router.get("/historico", response_model=List[AccidenteOut])
def get_historico_accidentes(db: Session = Depends(get_db)):
    """
    Retorna el histórico de accidentes (útil para el Módulo 1).
    """
    accidentes = db.query(Accidente).limit(100).all()
    # Si la base de datos está vacía, devolvemos datos mock
    if not accidentes:
        return [
            AccidenteOut(id=1, fecha=datetime.now(), latitud=6.2442, longitud=-75.5812, gravedad="alta", tipo="choque", zona="Centro", clima="lluvioso"),
            AccidenteOut(id=2, fecha=datetime.now(), latitud=6.2518, longitud=-75.5636, gravedad="media", tipo="atropello", zona="Aranjuez", clima="despejado")
        ]
    return accidentes

@router.get("/prediccion")
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
