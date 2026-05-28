from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from core.database import get_db
from models.trafico import FlujoTrafico
from pydantic import BaseModel
from typing import List
from datetime import datetime

router = APIRouter()

class FlujoTraficoOut(BaseModel):
    id: int
    fecha: datetime
    zona: str
    velocidad_promedio: float
    nivel_congestion: str
    vehiculos_por_minuto: int

    class Config:
        orm_mode = True
        from_attributes = True

@router.get("/tiempo-real", response_model=List[FlujoTraficoOut])
def get_trafico_tiempo_real(db: Session = Depends(get_db)):
    """
    Simula la obtención de tráfico en tiempo real (Módulo 2).
    """
    flujo = db.query(FlujoTrafico).order_by(FlujoTrafico.fecha.desc()).limit(10).all()
    if not flujo:
        return [
            FlujoTraficoOut(id=1, fecha=datetime.now(), zona="Av. San Juan", velocidad_promedio=15.5, nivel_congestion="alto", vehiculos_por_minuto=120),
            FlujoTraficoOut(id=2, fecha=datetime.now(), zona="Regional", velocidad_promedio=45.0, nivel_congestion="medio", vehiculos_por_minuto=80)
        ]
    return flujo
