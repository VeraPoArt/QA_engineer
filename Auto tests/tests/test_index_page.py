import pytest
import pages
import time
from playwright.sync_api import sync_playwright
from playwright.sync_api import Playwright, sync_playwright, expect


class TestFooter:

    def test_run(self):
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=False)
            time.sleep(5)
            context = browser.new_context(viewport={"width": 1920, "height": 1080})
            time.sleep(5)
            page = context.new_page()
            time.sleep(2.5)
            page.goto("https://dev.devselink.ru/")
            time.sleep(2.5)
            page.get_by_role("button", name="").click()
            time.sleep(2.5)
            page.locator("input[type=\"text\"]").click()
            time.sleep(2.5)
            page.locator("input[type=\"text\"]").fill("forfront@mail.ru")
            time.sleep(2.5)
            page.locator("input[type=\"password\"]").click()
            time.sleep(2.5)
            page.locator("input[type=\"password\"]").fill("123Qwerty")
            time.sleep(2.5)
            page.get_by_role("button", name="Войти в систему").click()
            time.sleep(2.5)
            expect(page.get_by_text("Личные данные")).to_be_visible()  # Замените "selector" на ваш селектор
            context.close()
            browser.close()