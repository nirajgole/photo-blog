import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    PROJECT_NAME:str = "Ngx🔥"
    PROJECT_VERSION: str = "1.0.0"

    DB_USER : str = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_SERVER : str = os.getenv("DB_SERVER","localhost")
    DB_PORT : str = os.getenv("DB_PORT","5432")
    DB_NAME : str = os.getenv("DB_NAME","tdd")
    DB_URL=f'mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_SERVER}:{DB_PORT}/{DB_NAME}'

settings = Settings()

