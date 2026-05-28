// Service Worker básico para PWA
self.addEventListener('install', event => {
  self.skipWaiting();
});

self.addEventListener('activate', event => {
  // Limpieza o migración de cachés si es necesario
});

self.addEventListener('fetch', event => {
  // Puedes personalizar la estrategia de caché aquí
});