from config_data.config import api_key
import requests
import string
import random
import logging


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def my_password(length: int) -> str:
    """Генерирует случайный пароль заданной длины."""

    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))


def get_request(length: int) -> str:
    """Генерирует случайный пароль"""

    url = f'https://api.api-ninjas.com/v1/passwordgenerator?length={length}'
    try:
        response = requests.get(url, headers={'X-Api-Key': api_key})
        response.raise_for_status()
        data = response.json()
        return data.get('random_password', '')
    except requests.RequestException as e:
        logger.error(f'Ошибка при генерации пароля через API: {e}')
        # В случае ошибки запроса используем функцию my_password для генерации пароля
        logger.info('Используем функцию my_password для генерации случайного пароля.')
        return my_password(length)
