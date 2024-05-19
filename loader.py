from telebot import TeleBot
from telebot.storage import StateMemoryStorage
from config_data.config import SiteSettings

site = SiteSettings()

storage = StateMemoryStorage()
bot = TeleBot(token=site.bot_token, state_storage=storage)
