from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

b1 = KeyboardButton("Отправить геопозицию!", request_location=True)
b2 = KeyboardButton("Назад")

geo_keys = ReplyKeyboardMarkup(resize_keyboard=True)
geo_keys.add(b1).add(b2)
