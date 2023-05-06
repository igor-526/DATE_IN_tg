from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

b1 = KeyboardButton("Начать поиск")
b2 = KeyboardButton("Профиль")

menu_keys = ReplyKeyboardMarkup(resize_keyboard=True)
menu_keys.add(b1).add(b2)
