import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    PROJECT_NAME:str = os.getenv("PROJECT_NAME")
    PROJECT_VERSION: str = os.getenv("PROJECT_VERSION")


settings = Settings()