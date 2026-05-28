from fastapi import APIRouter

router = APIRouter()

@router.get("/seguras")
def get_rutas_seguras(origen: str = "Centro", destino: str = "Poblado"):
    """
    Rutas seguras en temporada de lluvias (Módulo 4).
    """
    return {
        "origen": origen,
        "destino": destino,
        "clima_actual": "Lluvia intensa",
        "rutas_recomendadas": [
            {
                "via": "Av. Las Vegas",
                "motivo": "Menor riesgo de inundación",
                "tiempo_estimado_min": 25
            },
            {
                "via": "Av. El Poblado",
                "motivo": "Vía alterna segura",
                "tiempo_estimado_min": 35
            }
        ],
        "vias_evitar": ["Soterrado Parques del Río", "Depresión La 10"]
    }
