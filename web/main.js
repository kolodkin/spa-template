// Minimal SPA entry module. Replace with your app.
//
// index.html maps the bare specifier "app" to this file and calls init().
// window.__APP mirrors the pattern the e2e tests rely on: tests wait for
// `__APP.ready` instead of sleeping, so they stay fast and deterministic.

export function init() {
  const status = document.getElementById("status");
  status.textContent = "Ready.";

  window.__APP = { ready: true };
}
