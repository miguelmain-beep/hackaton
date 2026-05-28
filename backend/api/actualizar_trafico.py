import requests
import mysql.connector
from mysql.connector import Error
from datetime import datetime

# 1. CONFIGURACIÓN DE LA BASE DE DATOS MARIADB
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',       # Cambia por tu usuario
    'password': '',       # Cambia por tu contraseña
    'database': 'movilidata_db'
}

# 2. URL DE LA API DE DATOS ABIERTOS (Ejemplo simulado de Datos Abiertos Medellín / SIATA)
# Nota: Las APIs de datos.gov.co usan un identificador único (Token de recurso)
API_URL = "https://datos.gov.co/resource/xxxx-xxxx.json?$limit=10" 

def consultar_api_alcaldia():
    """Consume la API externa y retorna los datos en formato JSON"""
    try:
        response = requests.get(API_URL, timeout=10)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"[{datetime.now()}] Error API: Código de estado {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"[{datetime.now()}] Error de conexión con la API: {e}")
        return None

def insertar_datos_mariadb(datos_transito):
    """Procesa e inserta los datos en la base de datos MariaDB"""
    if not datos_transito:
        return

    connection = None
    cursor = None
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        if connection.is_connected():
            cursor = connection.cursor()
            
            # Consulta SQL coincidente con tu tabla creada previamente
            query = """
                INSERT INTO registro_flujo_vehicular 
                (id_sensor, fecha_hora, conteo_vehiculos, velocidad_promedio, nivel_congestion) 
                VALUES (%s, %s, %s, %s, %s)
            """
            
            registros_insertados = 0
            
            for dato in datos_transito:
                # MAPEO DE DATOS: Traducir lo que envía la API a los campos de tu DB
                # Nota: Cambia las llaves ['id_sensor_api'], etc., por los nombres reales de la API de la alcaldía
                id_sensor = int(dato.get('id_sensor_api', 1)) 
                fecha_hora = dato.get('fecha_medicion', datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
                conteo = int(dato.get('vehiculos_conteo', 45))
                velocidad = int(dato.get('velocidad_promedio', 35))
                
                # Clasificación automática basada en velocidad
                if velocidad > 50: nivel = "Fluido"
                elif velocidad > 30: nivel = "Moderado"
                elif velocidad > 15: nivel = "Pesado"
                else: nivel = "Embotellado"

                valores = (id_sensor, fecha_hora, conteo, velocidad, nivel)
                
                # Ejecutar inserción
                cursor.execute(query, valores)
                registros_insertados += 1
            
            connection.commit()
            print(f"[{datetime.now()}] Éxito: Se insertaron {registros_insertados} nuevos registros de tráfico.")

    except Error as e:
        print(f"[{datetime.now()}] Error al insertar en MariaDB: {e}")
    finally:
        if cursor: cursor.close()
        if connection and connection.is_connected(): connection.close()

# Ejecución principal del flujo ETL
if __name__ == "__main__":
    print(f"[{datetime.now()}] Iniciando actualización de datos...")
    datos = consultar_api_alcaldia()
    if datos:
        insertar_datos_mariadb(datos)
        
        
import schedule
import time

def ejecutar_tarea_completa():
    print(f"\n[{datetime.now()}] Ejecutando ciclo de actualización...")
    datos = consultar_api_alcaldia()
    insertar_datos_mariadb(datos)

# Programar para que corra estrictamente cada 5 minutos
schedule.every(5).minutes.do(ejecutar_tarea_completa)

# También puedes probarlo cada 10 segundos para ver si funciona rápido:
# schedule.every(10).seconds.do(ejecutar_tarea_completa)

print("Servicio de automatización de tráfico iniciado. Presiona Ctrl+C para salir.")
while True:
    schedule.run_pending()
    time.sleep(1)