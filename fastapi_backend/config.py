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
    DB_NAME : str = os.getenv("DB_NAME","test")

    # mysql connection
    # DB_URL=f'mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_SERVER}:{DB_PORT}/{DB_NAME}'

    # mssql connection
    server = "N7\MSSQL"
    database = "test"
    driver = "ODBC+Driver+17+for+SQL+Server"
    DB_URL = f"mssql+pyodbc://{server}/{database}?trusted_connection=yes&driver={driver}"

settings = Settings()


