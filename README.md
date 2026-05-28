<<<<<<< HEAD
# moviliDATA

Repositorio para el proyecto de hackatón: Sistema de información y predicción de movilidad para Medellín.

## Estructura

- backend/: Lógica de backend y APIs
- frontend/: Interfaz de usuario y recursos web
- data/: Archivos de respaldo (CSV/JSON)
- docs/: Documentación técnica y manual de usuario

## Instalación y uso

(Agrega aquí instrucciones para correr el backend y frontend)
=======
# 🚗 moviliDATA
## Plataforma Unificada de Movilidad Inteligente para Medellín
Proyecto desarrollado para HackData CTGI SENA 2026.

---

## 📌 Descripción
**moviliDATA** es una plataforma *full stack* inteligente diseñada para solucionar los cuatro grandes desafíos interconectados de la movilidad urbana en Medellín: accidentalidad vial, congestión vehicular, predicción de tráfico y rutas inseguras en temporada de lluvias. 

Utilizando analítica de datos, modelos predictivos y monitoreo en tiempo real, transformamos la movilidad reactiva en una experiencia predictiva y segura.

---

## 🎯 Objetivo
Construir una plataforma tipo *startup* que procese múltiples fuentes de datos abiertos (APIs, CSV, modelos estadísticos) para proporcionar a las autoridades y a los ciudadanos dashboards interactivos, heatmaps de probabilidad de congestión y predicciones de accidentes basadas en datos climáticos e históricos.

---
# 🚗 moviliDATA
## Plataforma Unificada de Movilidad Inteligente para Medellín
Proyecto desarrollado para HackData CTGI SENA 2026.

---

## 📌 Descripción
**moviliDATA** es una plataforma *full stack* inteligente diseñada para solucionar los cuatro grandes desafíos interconectados de la movilidad urbana en Medellín: accidentalidad vial, congestión vehicular, predicción de tráfico y rutas inseguras en temporada de lluvias. 

Utilizando analítica de datos, modelos predictivos y monitoreo en tiempo real, transformamos la movilidad reactiva en una experiencia predictiva y segura.

---

## 🎯 Objetivo
Construir una plataforma tipo *startup* que procese múltiples fuentes de datos abiertos (APIs, CSV, modelos estadísticos) para proporcionar a las autoridades y a los ciudadanos dashboards interactivos, heatmaps de probabilidad de congestión y predicciones de accidentes basadas en datos climáticos e históricos.

---

## 🚀 Tecnologías Usadas
### Frontend
- HTML5, CSS3, JavaScript Vanilla
- **Chart.js** (Visualización estadística)
- **Leaflet.js** (Mapas geoespaciales interactivos)
### Backend & Machine Learning
- **Python 3.10+**
- **FastAPI** (Desarrollo ágil de APIs REST)
- **SQLAlchemy & MySQL** (Base de Datos)
- **Pandas & Scikit-learn** (Análisis estadístico y Modelos Predictivos - *Integración lista*)

---

## 📂 Estructura del Sistema
El código fuente está organizado profesionalmente separando responsabilidades:

```text
moviliDATA/
├── backend/                  # Servidor y API REST (FastAPI)
│   ├── api/                  # Endpoints (Accidentes, Tráfico, Rutas)
│   ├── core/                 # Configuración de BD (MySQL)
│   ├── models/               # Modelos SQLAlchemy
│   └── services/             # Integración con Machine Learning
├── frontend/                 # Interfaz Web (Dashboard)
│   ├── css/                  # Sistema de diseño moderno (Dark Mode)
│   ├── js/                   # Lógica e integración API (Fetch)
│   └── index.html            # Dashboard Central
├── data/                     # Archivos de respaldo (CSV/JSON)
├── docs/                     # Documentación técnica y manual de usuario
```

---

## 🌐 APIs y Datasets Consumidos (Fuentes de Datos)
La arquitectura está preparada para consumir las siguientes fuentes públicas de Medellín:
- [Observatorio de Movilidad de Medellín (Víctimas e Incidentes)](#)
- [Sistema Inteligente de Movilidad de Medellín (SIM)](#)
- Integración climática en tiempo real (SIATA).

---

## ⚙️ Cómo Ejecutar el Proyecto

### 1. Levantar la Base de Datos (MySQL)
Crea una base de datos local llamada `hackathon_db` y ajusta tus credenciales en el archivo `backend/.env`.

### 2. Levantar el Backend (FastAPI)
Abre una terminal en la carpeta `/backend` y ejecuta:
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```
La API estará documentada de manera interactiva en: [http://localhost:8000/docs](http://localhost:8000/docs)

### 3. Levantar el Frontend (Dashboard)
El frontend no requiere de Node.js ni compilación. Solo debes abrir el archivo `frontend/index.html` en tu navegador, o utilizar extensiones como *Live Server* en tu editor de código.

---

## 👥 Integrantes y Roles
- **[Tu Nombre]**: Desarrollo Full Stack, Analítica de Datos y Arquitectura de IA.
- *(Añadir más integrantes si aplica)*

---
