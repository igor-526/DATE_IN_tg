from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

b1 = KeyboardButton("\U00002764")
b2 = KeyboardButton("\U0001F494")
b3 = KeyboardButton("Пожаловаться")
b4 = KeyboardButton("Меню")
search_keys = ReplyKeyboardMarkup(resize_keyboard=True)
search_keys.row(b2, b1).add(b3).add(b4)


ib1 = InlineKeyboardButton(text="Фото", callback_data='all_photos')
ib2 = InlineKeyboardButton(text='Инфо', callback_data='x')
ib3 = InlineKeyboardButton(text='Пожаловаться', callback_data='x')
search_inline_keys = InlineKeyboardMarkup()
search_inline_keys.row(ib1, ib2).add(ib3)
