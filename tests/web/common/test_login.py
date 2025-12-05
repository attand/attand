import pytest
from playwright.sync_api import Page
from tests.web.pages.common.login_page import LoginPage
from core.database.db_manager import get_db_manager
import allure

# Fetch data from DB (or Mock)
db = get_db_manager()
try:
    # In a real scenario, this query fetches test cases
    test_data = db.execute_query("SELECT username, password, expected FROM users")
except Exception:
    test_data = []

@allure.feature("Login")
class TestLogin:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, page: Page):
        self.login_page = LoginPage(page)
        self.login_page.navigate_to()

    @pytest.mark.parametrize("data", test_data)
    @allure.story("Login Data Driven Test")
    def test_login_ddt(self, data):
        username = data.get("username") or data[0] # Handle dict or tuple
        password = data.get("password") or data[1]
        expected = data.get("expected") or data[2]

        with allure.step(f"Login with {username}"):
            self.login_page.login(username, password)

        if expected == "success":
            with allure.step("Verify login success"):
                assert "You logged into a secure area!" in self.login_page.get_flash_message_text()
                assert self.login_page.is_logout_button_visible()
        else:
            with allure.step("Verify login failure"):
                assert "Your username is invalid!" in self.login_page.get_flash_message_text()
