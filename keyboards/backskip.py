from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

b1 = KeyboardButton("Пропустить")
b2 = KeyboardButton("Назад")

backskip_keys = ReplyKeyboardMarkup(resize_keyboard=True)
backskip_keys.add(b1).add(b2)
