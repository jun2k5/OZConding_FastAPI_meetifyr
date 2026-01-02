import os
from enum import StrEnum

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()
mysql_password = os.getenv("MYSQL_PASSWORD")


class Env(StrEnum):
    LOCAL = "local"
    STAGE = "stage"
    PROD = "prod"


class Config(BaseSettings):
    ENV: Env = Env.LOCAL

    MYSQL_HOST: str = "localhost"
    MYSQL_PORT: int = 3306
    MYSQL_USER: str = "root"
    MYSQL_PASSWORD: str | None = mysql_password
    MYSQL_DB: str = "meetifyr"
    MYSQL_CONNECT_TIMEOUT: int = 5
    CONNECTION_POOL_MAXSIZE: int = 30
