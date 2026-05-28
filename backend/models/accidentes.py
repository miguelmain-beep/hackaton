from sqlalchemy import Column, Integer, String, Float, DateTime
from core.database import Base
from datetime import datetime

class Accidente(Base):
    __tablename__ = "accidentes"

    id = Column(Integer, primary_key=True, index=True)
    fecha = Column(DateTime, default=datetime.utcnow)
    latitud = Column(Float, nullable=False)
    longitud = Column(Float, nullable=False)
    gravedad = Column(String(50), nullable=False)  # ej. "alta", "media", "baja"
    tipo = Column(String(50)) # ej. "choque", "atropello"
    zona = Column(String(100)) # ej. "Centro", "Poblado"
    clima = Column(String(50)) # ej. "lluvioso", "despejado"
