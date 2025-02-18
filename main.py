import telebot
from telebot.types import ReplyKeyboardMarkup, WebAppInfo, KeyboardButton


TOKEN="7864680268:AAGhWs_yX17s58VxaZaT8ccmTqimI7OV5vo"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def welcome_message(message):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    web_app = WebAppInfo("https://www.ya.ru")
    button = KeyboardButton(text="Открыть Mini App", web_app=web_app)
    keyboard.add(button)
    bot.send_message(message.from_user.id, "Запустить приложение",
                     reply_markup=keyboard)




bot.polling()