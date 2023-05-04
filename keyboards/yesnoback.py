from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

b1 = KeyboardButton("Да")
b2 = KeyboardButton("Нет")
b3 = KeyboardButton("Назад")

yesnoback_keys = ReplyKeyboardMarkup(resize_keyboard=True)
yesnoback_keys.row(b1, b2).add(b3)
