from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

b1 = KeyboardButton("Мужчин")
b2 = KeyboardButton("Девушек")
b3 = KeyboardButton("Всех")
b4 = KeyboardButton("Назад")

sex_f_keys = ReplyKeyboardMarkup(resize_keyboard=True)
sex_f_keys.row(b1, b2).add(b3).add(b4)
