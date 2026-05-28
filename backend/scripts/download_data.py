import json
import os
import random
from datetime import datetime, timedelta

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")
OUTPUT_FILE = os.path.join(DATA_DIR, "incidentes.json")

def generate_local_data():
    zonas_medellin = ["Poblado", "Laureles", "Centro", "Belen", "Robledo", "Aranjuez", "Manrique", "Buenos Aires"]
    tipos = ["choque", "atropello", "caida_ocupante", "volcamiento"]
    gravedad = ["baja", "media", "alta"]
    climas = ["despejado", "lluvioso", "nublado"]

    data = []
    now = datetime.now()
    
    for i in range(1, 1001):
        # Generar coordenadas simuladas alrededor de Medellín (Lat: ~6.24, Lon: ~-75.58)
        lat = 6.24 + random.uniform(-0.05, 0.05)
        lon = -75.58 + random.uniform(-0.05, 0.05)
        
        incidente = {
            "id": i,
            "fecha": (now - timedelta(hours=random.randint(0, 720))).isoformat(),
            "latitud": round(lat, 6),
            "longitud": round(lon, 6),
            "gravedad": random.choice(gravedad),
            "tipo": random.choice(tipos),
            "zona": random.choice(zonas_medellin),
            "clima": random.choice(climas)
        }
        data.append(incidente)
        
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)
        
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        
    print(f"✅ ¡Éxito! {len(data)} incidentes generados y guardados en {OUTPUT_FILE} de manera local.")

if __name__ == "__main__":
    generate_local_data()
