from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

b1 = KeyboardButton("Регистрируюсь первый раз")
b2 = KeyboardButton("Вход через VK")

reg_profile_keys = ReplyKeyboardMarkup(resize_keyboard=True)
reg_profile_keys.add(b1).add(b2)
