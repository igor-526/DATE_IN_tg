from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

b1 = KeyboardButton("Готово!")
b2 = KeyboardButton("Назад")

readyback_keys = ReplyKeyboardMarkup(resize_keyboard=True)
readyback_keys.add(b1).add(b2)
