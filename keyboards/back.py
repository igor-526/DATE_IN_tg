from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

b1 = KeyboardButton("Назад")

back_keys = ReplyKeyboardMarkup(resize_keyboard=True)
back_keys.add(b1)
