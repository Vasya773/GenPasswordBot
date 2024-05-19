import os
from dotenv import load_dotenv, find_dotenv
from pydantic import SecretStr, StrictStr
from pydantic_settings import BaseSettings


if not find_dotenv():
    exit('Переменные окружения не загружены, так как отсутствует файл .env')
else:
    load_dotenv()


class SiteSettings(BaseSettings):
    api_key: SecretStr = os.getenv('API_KEY', None)
    host_api: StrictStr = os.getenv('HOST_API', None)
    bot_token: str = os.getenv('BOT_TOKEN', None)
