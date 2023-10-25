import telebot

from config.settings import TELEGRAM_API_TOKEN, TELEGRAM_URL_BOT

URL = TELEGRAM_URL_BOT
TOKEN = TELEGRAM_API_TOKEN

bot = telebot.TeleBot(f'{TELEGRAM_API_TOKEN}')


@bot.message_handler(commands=['info'])
def main(message):
    bot.send_message(message.chat.id, f'Ваш ID чата: {message.chat.id}.'
                                      f'\n\nПросьба сохранить его в базе данных для вашей учетной записи.')


bot.polling(none_stop=True)
