from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

b1 = KeyboardButton("ЛАЙК")
b2 = KeyboardButton("Далее")
b3 = KeyboardButton("Пожаловаться")
b4 = KeyboardButton("Меню")

search_keys = ReplyKeyboardMarkup(resize_keyboard=True)
search_keys.row(b1, b2).add(b3).add(b4)
