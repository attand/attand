from core.base_page import BasePage
from config.settings import settings

class LoginPage(BasePage):
    URL = f"{settings.BASE_URL}/login"

    # Selectors
    USERNAME_INPUT = "#username"
    PASSWORD_INPUT = "#password"
    LOGIN_BUTTON = "button[type='submit']"
    FLASH_MESSAGE = "#flash"
    LOGOUT_BUTTON = "a[href='/logout']"

    def navigate_to(self):
        self.navigate(self.URL)

    def login(self, username, password):
        self.fill(self.USERNAME_INPUT, username)
        self.fill(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

    def get_flash_message_text(self):
        self.wait_for_selector(self.FLASH_MESSAGE)
        return self.get_text(self.FLASH_MESSAGE)

    def is_logout_button_visible(self):
        return self.is_visible(self.LOGOUT_BUTTON)
