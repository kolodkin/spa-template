// Minimal SPA entry point. Replace with your app.
//
// window.__APP mirrors the pattern the e2e tests rely on: tests wait for
// `__APP.ready` instead of sleeping, so they stay fast and deterministic.

const status = document.getElementById("status");
status.textContent = "Ready.";

window.__APP = { ready: true };
