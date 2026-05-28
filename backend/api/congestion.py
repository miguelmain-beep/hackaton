from fastapi import APIRouter

router = APIRouter()

@router.get("/prediccion")
def predict_congestion():
    """
    Pronóstico de congestión para las próximas 2-4 horas (Módulo 3).
    """
    return {
        "predicciones": [
            {"hora": "14:00", "zona": "Av. Oriental", "probabilidad_congestion": 0.9, "nivel": "critico"},
            {"hora": "15:00", "zona": "Calle San Juan", "probabilidad_congestion": 0.75, "nivel": "alto"}
        ]
    }
