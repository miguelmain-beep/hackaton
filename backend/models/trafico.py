from sqlalchemy import Column, Integer, String, Float, DateTime
from core.database import Base
from datetime import datetime

class FlujoTrafico(Base):
    __tablename__ = "flujo_trafico"

    id = Column(Integer, primary_key=True, index=True)
    fecha = Column(DateTime, default=datetime.utcnow)
    zona = Column(String(100), nullable=False)
    velocidad_promedio = Column(Float) # km/h
    nivel_congestion = Column(String(50)) # "bajo", "medio", "alto"
    vehiculos_por_minuto = Column(Integer)
