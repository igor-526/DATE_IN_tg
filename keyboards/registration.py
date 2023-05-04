from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

b1 = KeyboardButton("Регистрация")

registration_keys = ReplyKeyboardMarkup(resize_keyboard=True)
registration_keys.add(b1)
