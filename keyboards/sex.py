from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

b1 = KeyboardButton("Парень")
b2 = KeyboardButton("Девушка")
b3 = KeyboardButton("Назад")

sex_keys = ReplyKeyboardMarkup(resize_keyboard=True)
sex_keys.row(b1, b2).add(b3)
