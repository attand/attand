from core.base_page import BasePage

class QueryPage(BasePage):
    """
    示例：政企业务 > 统计分析 > 综合查询页面
    """
    URL = "/enterprise/analysis/query"

    SEARCH_INPUT = "#search-input"
    SEARCH_BUTTON = "#search-btn"
    RESULT_TABLE = "#result-table"

    def search(self, keyword):
        self.fill(self.SEARCH_INPUT, keyword)
        self.click(self.SEARCH_BUTTON)
