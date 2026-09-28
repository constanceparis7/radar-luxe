/* Service worker ConstanceParis7 (28/09/2026).
   Le site reste consultable hors connexion : chaque page visitée est gardée en copie,
   le réseau passe toujours en premier (le contenu change chaque jour), la copie ne sert
   qu'en secours, et une page dédiée s'affiche s'il n'existe aucune copie.
   Jamais de ressource tierce en cache (GoatCounter reste hors de ce fichier). */
var VERSION = 'cp7-2026-09-28';
var SOCLE = ['/hors-connexion.html', '/manifest.webmanifest', '/favicon.svg', '/icone-192.png'];
var MAX_ENTREES = 90;

self.addEventListener('install', function (e) {
  e.waitUntil(caches.open(VERSION).then(function (c) { return c.addAll(SOCLE); }).then(function () { return self.skipWaiting(); }));
});

self.addEventListener('activate', function (e) {
  e.waitUntil((function () {
    var p = [];
    if (self.registration.navigationPreload) { p.push(self.registration.navigationPreload.enable().catch(function () {})); }
    p.push(caches.keys().then(function (ks) {
      return Promise.all(ks.filter(function (k) { return k.indexOf('cp7-') === 0 && k !== VERSION; }).map(function (k) { return caches.delete(k); }));
    }));
    return Promise.all(p).then(function () { return self.clients.claim(); }).then(function () {
      // Les pages déjà ouvertes (dont celle qui vient d'installer ce worker) n'ont pas
      // transité par lui : on en prend copie maintenant. Le cache HTTP du navigateur
      // répond, donc aucun nouveau téléchargement.
      return self.clients.matchAll({ type: 'window', includeUncontrolled: true }).then(function (cs) {
        return caches.open(VERSION).then(function (c) {
          return Promise.all(cs.map(function (cl) {
            var u = new URL(cl.url);
            if (u.origin !== self.location.origin) { return null; }
            return fetch(cl.url).then(function (r) {
              if (r && r.ok && r.type === 'basic' && !r.redirected) { return c.put(cl.url, r); }
            }).catch(function () {});
          }));
        });
      });
    });
  })());
});

function borner(c) {
  return c.keys().then(function (keys) {
    var surplus = keys.length - MAX_ENTREES;
    if (surplus <= 0) { return; }
    var candidats = keys.filter(function (r) { return SOCLE.indexOf(new URL(r.url).pathname) === -1; }).slice(0, surplus);
    return Promise.all(candidats.map(function (r) { return c.delete(r); }));
  });
}

self.addEventListener('fetch', function (e) {
  var req = e.request;
  if (req.method !== 'GET') { return; }
  var url = new URL(req.url);
  if (url.origin !== self.location.origin || url.pathname === '/sw.js') { return; }
  e.respondWith((function () {
    return caches.open(VERSION).then(function (c) {
      return Promise.resolve(e.preloadResponse).then(function (pre) { return pre || fetch(req); })
        .then(function (res) {
          if (res && res.ok && res.type === 'basic' && !res.redirected) {
            c.put(req, res.clone()).then(function () { return borner(c); }).catch(function () {});
          }
          return res;
        })
        .catch(function (err) {
          return c.match(req, { ignoreSearch: true }).then(function (hit) {
            if (hit) { return hit; }
            if (req.mode === 'navigate') { return c.match('/hors-connexion.html'); }
            throw err;
          });
        });
    });
  })());
});
