from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from config.settings import settings
from core.utils.logger import get_logger

logger = get_logger("DBManager")

class DBManager:
    def __init__(self):
        self.connection_string = (
            f"mysql+pymysql://{settings.DB_USER}:{settings.DB_PASSWORD}"
            f"@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}"
        )
        self.engine = None
        self.Session = None

    def connect(self):
        try:
            self.engine = create_engine(self.connection_string)
            self.Session = sessionmaker(bind=self.engine)
            logger.info("Connected to database successfully")
        except Exception as e:
            logger.error(f"Failed to connect to database: {e}")
            raise

    def execute_query(self, query: str, params=None):
        if not self.engine:
            self.connect()

        with self.engine.connect() as conn:
            result = conn.execute(text(query), params or {})
            # Convert Row objects to dictionaries to ensure compatibility with MockDBManager
            # and allow .get() access in tests.
            return [row._mapping for row in result]

class MockDBManager:
    """Mock Database Manager for local testing without real DB"""
    def __init__(self):
        logger.info("Using MockDBManager")

    def connect(self):
        pass

    def execute_query(self, query: str, params=None):
        logger.info(f"Mock Executing query: {query}")
        # Return mock data based on query content
        if "users" in query.lower():
            return [
                {"username": "tomsmith", "password": "SuperSecretPassword!", "expected": "success"},
                {"username": "invalid", "password": "wrong", "expected": "failure"}
            ]
        return []

def get_db_manager():
    if settings.USE_MOCK_DB:
        return MockDBManager()
    return DBManager()
