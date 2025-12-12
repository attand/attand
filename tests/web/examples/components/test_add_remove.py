import pytest
import allure
from playwright.sync_api import Page, expect
from tests.web.pages.examples.components.add_remove_page import AddRemovePage

@allure.feature("Add/Remove Elements")
@pytest.mark.smoke
class TestAddRemove:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, page: Page):
        # 初始化页面对象
        self.page_obj = AddRemovePage(page)
        # 导航到目标页面 (这里我们演示从首页点击进去的流程，还原你的录制)
        self.page_obj.navigate_from_home()

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
