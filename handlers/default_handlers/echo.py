from loader import bot


@bot.message_handler(func=lambda message: True)
def message_handler(message):
    bot.send_message(message.chat.id, message.text)


if __name__ == '__main__':
    bot.infinity_polling()
