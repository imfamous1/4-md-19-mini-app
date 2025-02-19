import json
import os

import telebot
from telebot.types import ReplyKeyboardMarkup, WebAppInfo, KeyboardButton


TOKEN="7864680268:AAGhWs_yX17s58VxaZaT8ccmTqimI7OV5vo"
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

        # Формируем текст и путь к изображению
        text = f"{data['title']}\n\n{data['description']}"
        photo_path = data['image']  # Локальный путь к изображению, например '2.png'

        # Проверяем, существует ли файл
        if not os.path.exists(photo_path):
            raise FileNotFoundError(f"Файл {photo_path} не найден")

        # Открываем изображение как файл и отправляем
        with open(photo_path, 'rb') as photo:
            bot.send_photo(message.from_user.id, photo=photo, caption=text)
    except Exception as e:
        print(f"Ошибка: {e}")
        bot.send_message(message.from_user.id, "Произошла ошибка при обработке данных. Попробуйте еще раз.")

bot.polling()