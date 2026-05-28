import { api } from './api.js';

// Inicialización del Mapa de Medellín
const map = L.map('map').setView([6.2442, -75.5812], 13); // Coordenadas de Medellín

L.tileLayer('https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png', {
    attribution: '&copy; <a href="https://carto.com/attributions">CARTO</a>'
}).addTo(map);

// Variables Globales
let trafficChartInstance = null;

// Función para actualizar los KPIs
function updateKPIs(traficoData) {
    if (!traficoData || traficoData.length === 0) return;
    
    // Calcular promedio
    const avgSpeed = traficoData.reduce((acc, curr) => acc + curr.velocidad_promedio, 0) / traficoData.length;
    document.getElementById('kpi-velocidad').textContent = `${avgSpeed.toFixed(1)} km/h`;
    
    // Contar alertas (congestión alta)
    const alertas = traficoData.filter(t => t.nivel_congestion === 'alto').length;
    document.getElementById('kpi-alertas').textContent = alertas;
}

// Función para actualizar Tabla
function updateTable(traficoData) {
    const tbody = document.getElementById('traffic-table-body');
    tbody.innerHTML = ''; // Limpiar
    
    traficoData.forEach(item => {
        const tr = document.createElement('tr');
        
        // Asignar clase de badge según nivel
        let badgeClass = 'bajo';
        if(item.nivel_congestion === 'alto') badgeClass = 'alto';
        else if(item.nivel_congestion === 'medio') badgeClass = 'medio';

        tr.innerHTML = `
            <td>${item.zona}</td>
            <td>${item.velocidad_promedio} km/h</td>
            <td><span class="badge ${badgeClass}">${item.nivel_congestion.toUpperCase()}</span></td>
        `;
        tbody.appendChild(tr);
    });
}

// Función para actualizar Gráfica Chart.js
function updateChart(traficoData) {
    const ctx = document.getElementById('trafficChart').getContext('2d');
    
    const labels = traficoData.map(t => t.zona);
    const data = traficoData.map(t => t.vehiculos_por_minuto);

    if (trafficChartInstance) {
        trafficChartInstance.destroy(); // Destruir instancia anterior
    }

    trafficChartInstance = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: labels,
            datasets: [{
                label: 'Vehículos por minuto',
                data: data,
                backgroundColor: 'rgba(59, 130, 246, 0.8)',
                borderRadius: 5
            }]
        },
        options: {
            responsive: true,
            scales: {
                y: {
                    beginAtZero: true,
                    grid: { color: 'rgba(255, 255, 255, 0.1)' },
                    ticks: { color: '#94a3b8' }
                },
                x: {
                    grid: { display: false },
                    ticks: { color: '#94a3b8' }
                }
            },
            plugins: {
                legend: { labels: { color: '#f8fafc' } }
            }
        }
    });
}

// Agregar marcadores dummy al mapa
function addMapMarkers(traficoData) {
    // Coordenadas dummy de ejemplo para las zonas de la respuesta
    const coordsMock = {
        "Av. San Juan": [6.248, -75.578],
        "Regional": [6.240, -75.575]
    };

    traficoData.forEach(item => {
        if(coordsMock[item.zona]) {
            const color = item.nivel_congestion === 'alto' ? 'red' : item.nivel_congestion === 'medio' ? 'orange' : 'green';
            
            const circle = L.circleMarker(coordsMock[item.zona], {
                color: color,
                fillColor: color,
                fillOpacity: 0.5,
                radius: 15
            }).addTo(map);
            
            circle.bindPopup(`<b>${item.zona}</b><br>Velocidad: ${item.velocidad_promedio} km/h`);
        }
    });
}

// Main loader
async function initDashboard() {
    // 1. Obtener datos de la API FastAPI
    const traficoData = await api.getTraficoTiempoReal();
    
    // 2. Renderizar UI
    updateKPIs(traficoData);
    updateTable(traficoData);
    updateChart(traficoData);
    addMapMarkers(traficoData);
}

// Iniciar al cargar
document.addEventListener('DOMContentLoaded', initDashboard);
