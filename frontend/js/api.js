const API_BASE_URL = 'http://localhost:8000/api';

export const api = {
    async getTraficoTiempoReal() {
        try {
            const response = await fetch(`${API_BASE_URL}/trafico/tiempo-real`);
            if (!response.ok) throw new Error('Error de red');
            return await response.json();
        } catch (error) {
            console.error('Error obteniendo tráfico:', error);
            // Mock fallback para pruebas sin backend
            return [
                { zona: "Av. San Juan", velocidad_promedio: 15.5, nivel_congestion: "alto", vehiculos_por_minuto: 120 },
                { zona: "Regional", velocidad_promedio: 45.0, nivel_congestion: "medio", vehiculos_por_minuto: 80 }
            ];
        }
    },

    async getZonasCriticas() {
        try {
            const response = await fetch(`${API_BASE_URL}/accidentes/prediccion`);
            return await response.json();
        } catch (error) {
            console.error('Error:', error);
            return { zonas_criticas: [] };
        }
    },

    async getPrediccionCongestion() {
        try {
            const response = await fetch(`${API_BASE_URL}/congestion/prediccion`);
            return await response.json();
        } catch (error) {
            console.error('Error:', error);
            return { predicciones: [] };
        }
    }
};
