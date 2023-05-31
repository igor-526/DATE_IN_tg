from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

b1 = KeyboardButton("Да")
b2 = KeyboardButton("Нет")

yesno_keys = ReplyKeyboardMarkup(resize_keyboard=True)
yesno_keys.row(b1, b2)
