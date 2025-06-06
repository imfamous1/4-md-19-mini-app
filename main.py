import json
import os
import telebot
from telebot.types import ReplyKeyboardMarkup, WebAppInfo, KeyboardButton


TOKEN="" # Здесь нужно указать токен вашего бота
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def welcome_message(message):

    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    web_app = WebAppInfo("https://imfamous1.github.io/4-md-19-mini-app/")
    button = KeyboardButton(text="Открыть Mini App", web_app=web_app)
    keyboard.add(button)
    bot.send_message(message.from_user.id, "Запустить приложение",
                     reply_markup=keyboard)


@bot.message_handler(content_types=['web_app_data'])
def web_app_data_handler(message):
    try:
        # Получаем данные из Mini App
        data = json.loads(message.web_app_data.data)
        print(f"Получены данные с Mini App: {data}")

    except Exception as e:
        print(f"Ошибка: {e}")
        bot.send_message(message.from_user.id, "Произошла ошибка при обработке данных. Попробуйте еще раз.")

bot.polling()