// 基本的なオフラインキャッシュを提供するサービスワーカー
var staticCacheName = "pwa-v" + new Date().getTime();
var filesToCache = [
    '/', // スタートURL
    // ここにキャッシュしたいCSSやJS、主要なページを追加していく
    // 例: '/static/css/style.css', '/static/js/main.js'
];

// インストール処理
self.addEventListener("install", event => {
    this.skipWaiting();
    event.waitUntil(
        caches.open(staticCacheName).then(cache => {
            return cache.addAll(filesToCache);
        })
    )
});

// 古いキャッシュの削除
self.addEventListener('activate', event => {
    event.waitUntil(
        caches.keys().then(cacheNames => {
            return Promise.all(
                cacheNames
                    .filter(cacheName => (cacheName.startsWith("pwa-")))
                    .filter(cacheName => (cacheName !== staticCacheName))
                    .map(cacheName => caches.delete(cacheName))
            );
        })
    );
});

// フェッチイベント（リクエストがあった場合）
self.addEventListener("fetch", event => {
    event.respondWith(
        caches.match(event.request)
            .then(response => {
                return response || fetch(event.request);
            })
    );
});
