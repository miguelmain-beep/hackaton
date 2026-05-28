# Backend moviliDATA

Backend desarrollado con **FastAPI**, **Pandas**, **Scikit-learn** y conectado a **MySQL** (mediante SQLAlchemy). Provee las APIs requeridas para los 4 módulos del hackathon.

## Requisitos Previos
1. Tener instalado **Python 3.10+**.
2. Tener instalado **MySQL Server** (y que esté ejecutándose).

## Configuración Inicial

1. **Crear la Base de Datos:**
   Abre tu consola de MySQL o herramienta como phpMyAdmin y crea la base de datos:
   ```sql
   CREATE DATABASE hackathon_db;
   ```

2. **Configurar Variables de Entorno:**
   Edita el archivo `.env` ubicado en esta misma carpeta y asegúrate de poner las credenciales correctas de tu MySQL (`DB_USER`, `DB_PASSWORD`, `DB_HOST`, etc.). Si la contraseña de tu usuario root está vacía, puedes dejarlo como está.

3. **Activar Entorno Virtual e Instalar Dependencias:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # En Windows usa: venv\Scripts\activate
   pip install -r requirements.txt
   ```

## Ejecución del Servidor

Para arrancar el backend en modo desarrollo (se reinicia al hacer cambios en el código):

```bash
uvicorn main:app --reload
```

## Documentación Interactiva

Una vez que el servidor esté corriendo, puedes ver y probar todas las APIs (Swagger UI) ingresando en tu navegador a:
👉 **[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)**

## Estructura
- `/core`: Configuración de base de datos MySQL y variables.
- `/models`: Modelos SQLAlchemy que crearán las tablas en MySQL automáticamente.
- `/api`: Rutas y endpoints para Accidentes, Tráfico, Congestión y Rutas/Clima.
- `/services`: Lógica de integración con los modelos de Machine Learning (Scikit-learn/Pandas).
- `/data`: Carpeta para alojar archivos CSV o JSON en crudo.
