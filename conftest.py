from playwright.sync_api import sync_playwright
import pytest


@pytest.fixture(scope="function", autouse=False)
def page():
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    yield page
    browser.close()
    playwright.stop()