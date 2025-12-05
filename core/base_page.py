import allure
from playwright.sync_api import Page, Locator, expect
from core.utils.logger import get_logger

class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.logger = get_logger(self.__class__.__name__)

    def navigate(self, url: str):
        self.logger.info(f"Navigating to {url}")
        self.page.goto(url)

    def click(self, selector: str):
        self.logger.info(f"Clicking element: {selector}")
        self.page.click(selector)

    def fill(self, selector: str, text: str):
        self.logger.info(f"Filling element {selector} with text: {text}")
        self.page.fill(selector, text)

    def get_text(self, selector: str) -> str:
        self.logger.info(f"Getting text from element: {selector}")
        return self.page.inner_text(selector)

    def is_visible(self, selector: str) -> bool:
        return self.page.is_visible(selector)

    def wait_for_selector(self, selector: str, timeout: int = 5000):
        self.logger.info(f"Waiting for selector: {selector}")
        self.page.wait_for_selector(selector, timeout=timeout)

    def take_screenshot(self, name: str):
        """Taking screenshot and attach to allure report"""
        self.logger.info(f"Taking screenshot: {name}")
        png_bytes = self.page.screenshot()
        allure.attach(
            png_bytes,
            name=name,
            attachment_type=allure.attachment_type.PNG
        )
