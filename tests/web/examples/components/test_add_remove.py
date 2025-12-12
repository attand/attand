import pytest
import allure
from playwright.sync_api import Page, expect
from tests.web.pages.examples.components.add_remove_page import AddRemovePage

@allure.feature("Add/Remove Elements")
@pytest.mark.smoke
class TestAddRemove:

    @pytest.fixture(scope="function", autouse=True)
    def page_lifecycle(self, page: Page):
        # Setup: 初始化并导航
        self.page_obj = AddRemovePage(page)
        self.page_obj.navigate_from_home()

        yield

        # Teardown: 模拟数据清理
        # 实际项目中，这里可能会调用 API 删除创建的数据，或者重置页面状态
        print("\n[Teardown] Cleaning up Add/Remove test context...")

    @allure.story("Add and Delete Elements")
    def test_add_remove_elements(self):
        with allure.step("Add two elements"):
            # 对应录制代码中的两次点击 "Add Element"
            self.page_obj.add_element()
            self.page_obj.add_element()

            # 截图
            self.page_obj.take_screenshot("After adding 2 elements")

            # 验证点：此时应该有 2 个删除按钮
            expect(self.page_obj.page.locator(self.page_obj.DELETE_BUTTON)).to_have_count(2)

        with allure.step("Delete one element"):
            # 对应录制代码中的点击 "Delete"
            self.page_obj.delete_element()

            # 截图
            self.page_obj.take_screenshot("After deleting 1 element")

            # 验证点：删除一个后，应该剩 1 个
            expect(self.page_obj.page.locator(self.page_obj.DELETE_BUTTON)).to_have_count(1)
