import os
import allure
import re
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

    def assert_text_contains(self, selector: str, text: str):
        """Assert that the element contains the specified text."""
        self.logger.info(f"Asserting element {selector} contains text: {text}")
        expect(self.page.locator(selector)).to_contain_text(text)

    def assert_element_visible(self, selector: str):
        """Assert that the element is visible."""
        self.logger.info(f"Asserting element {selector} is visible")
        expect(self.page.locator(selector)).to_be_visible()

    def assert_url_contains(self, text: str):
        """Assert that the URL contains the specified text."""
        self.logger.info(f"Asserting URL contains text: {text}")
        expect(self.page).to_have_url(re.compile(text))

    def take_screenshot(self, name: str):
        """Taking screenshot and attach to allure report"""
        self.logger.info(f"Taking screenshot: {name}")
        png_bytes = self.page.screenshot()

        # 1. Attach to Allure Report
        allure.attach(
            png_bytes,
            name=name,
            attachment_type=allure.attachment_type.PNG
        )

        # 2. Save to loose file if SCREENSHOT_DIR is set
        screenshot_dir = os.getenv("SCREENSHOT_DIR")
        if screenshot_dir:
            # Sanitize name to be safe filename
            safe_name = "".join([c if c.isalnum() else "_" for c in name])
            file_path = os.path.join(screenshot_dir, f"{safe_name}.png")
            try:
                with open(file_path, "wb") as f:
                    f.write(png_bytes)
                self.logger.info(f"Saved screenshot to: {file_path}")
            except Exception as e:
                self.logger.error(f"Failed to save screenshot file: {e}")
