from telebot.types import BotCommand
from config_data import config


def set_default_commands(bot):
    bot.set_my_commands(
        [BotCommand(*i) for i in config.DEFAULT_COMMANDS]
    )
