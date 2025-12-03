import os
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseModel):
    BASE_URL: str = os.getenv("BASE_URL", "https://the-internet.herokuapp.com")
    DB_HOST: str = os.getenv("DB_HOST", "localhost")
    DB_PORT: int = int(os.getenv("DB_PORT", 3306))
    DB_USER: str = os.getenv("DB_USER", "root")
    DB_PASSWORD: str = os.getenv("DB_PASSWORD", "")
    DB_NAME: str = os.getenv("DB_NAME", "testdb")
    USE_MOCK_DB: bool = os.getenv("USE_MOCK_DB", "true").lower() == "true"
    HEADLESS: bool = os.getenv("HEADLESS", "true").lower() == "true"

settings = Settings()
