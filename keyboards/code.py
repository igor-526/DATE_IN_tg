from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

b1 = KeyboardButton("Отправить ещё раз")
b2 = KeyboardButton("Назад")

code_keys = ReplyKeyboardMarkup(resize_keyboard=True)
code_keys.add(b1).add(b2)
