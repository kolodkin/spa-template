"""End-to-end tests for the SPA (Playwright, Chromium)."""
from playwright.sync_api import expect


def _wait_ready(page):
    page.wait_for_function(
        "() => window.__APP && window.__APP.ready === true", timeout=30000
    )


def test_page_loads(server_url, page):
    page.goto(server_url + "/")
    _wait_ready(page)
    expect(page).to_have_title("SPA Template")
    expect(page.locator("h1")).to_have_text("Hello, world!")


def test_app_script_runs(server_url, page):
    # main.js executed: it flips the status line from "Loading…" to "Ready.".
    page.goto(server_url + "/")
    _wait_ready(page)
    expect(page.locator("#status")).to_have_text("Ready.")


def test_no_console_errors(server_url, page):
    errors = []
    page.on("console", lambda msg: errors.append(msg.text) if msg.type == "error" else None)
    page.on("pageerror", lambda exc: errors.append(str(exc)))
    page.goto(server_url + "/")
    _wait_ready(page)
    assert errors == []
