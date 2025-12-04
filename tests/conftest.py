import pytest  # Импортируем pytest
from playwright.sync_api import sync_playwright, Playwright, Page  # Имопртируем класс страницы, будем использовать его для аннотации типов


@pytest.fixture
def chromium_page(playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    yield browser.new_page()
    browser.close()