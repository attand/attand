import pytest
from core.utils.logger import get_logger
from config.settings import settings

logger = get_logger("GlobalFixture")

@pytest.fixture(scope="session", autouse=True)
def global_lifecycle():
    """
    全局生命周期管理：
    Setup: 测试会话开始前执行（如初始化DB连接池、检查环境）
    Teardown: 测试会话结束后执行（如生成统计报告、清理临时文件）
    """
    logger.info("========== [Global Setup] Test Session Started ==========")
    logger.info(f"Environment: {settings.BASE_URL}")
    logger.info(f"Database Mode: {'Mock' if settings.USE_MOCK_DB else 'Real'}")

    yield

    logger.info("========== [Global Teardown] Test Session Finished ==========")
