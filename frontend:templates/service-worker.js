const CACHE_NAME = "nbkpay-pwa-v1";
const ASSETS = [
  "/",
  "/static/style.css",
  "/static/icons/icon-192x192.png",
  "/static/icons/icon-512x512.png",
  // ...add other asset paths here
];

self.addEventListener("install", event => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => cache.addAll(ASSETS))
  );
});

self.addEventListener("fetch", event => {
  event.respondWith(
    caches.match(event.request)
      .then(response => response || fetch(event.request))
  );
});