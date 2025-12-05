from core.base_page import BasePage
from config.settings import settings

class AddRemovePage(BasePage):
    # 1. 定义页面 URL
    URL = f"{settings.BASE_URL}/add_remove_elements/"

    # 2. 定义页面元素 (Selectors)
    # 首页上的入口链接
    ENTRY_LINK = "a[href='/add_remove_elements/']"

    # "Add Element" 按钮
    ADD_BUTTON = "button[onclick='addElement()']"

    # "Delete" 按钮 (新增出来的元素)
    DELETE_BUTTON = ".added-manually"

    def navigate_from_home(self):
        """从首页导航进入该模块"""
        self.navigate(settings.BASE_URL)
        self.click(self.ENTRY_LINK)

    def add_element(self):
        """点击添加元素按钮"""
        self.click(self.ADD_BUTTON)

    def delete_element(self):
        """点击删除按钮（删除第一个）"""
        # 注意：如果有多个，click() 默认点击第一个可见的
        self.click(self.DELETE_BUTTON)

    def get_delete_buttons_count(self) -> int:
        """获取当前页面上 Delete 按钮的数量（用于验证）"""
        return self.page.locator(self.DELETE_BUTTON).count()
