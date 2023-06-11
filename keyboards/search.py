from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

b1 = KeyboardButton("\U00002764")
b2 = KeyboardButton("\U0000274C")
b3 = KeyboardButton("Меню")
search_keys = ReplyKeyboardMarkup(resize_keyboard=True)
search_keys.row(b2, b1).add(b3)


ib1 = InlineKeyboardButton(text="\U0001F4F7", callback_data='all_photos')
ib2 = InlineKeyboardButton(text='\U0001F4DD', callback_data='description')
ib3 = InlineKeyboardButton(text='Пожаловаться', callback_data='complaint')
search_inline_keys = InlineKeyboardMarkup()
search_inline_keys.row(ib1, ib2).add(ib3)

ib1 = InlineKeyboardButton(text="\U0001F4F7", callback_data='all_photos')
ib2 = InlineKeyboardButton(text='\U0001F4DD', callback_data='description')
vk_inline_keys = InlineKeyboardMarkup()
vk_inline_keys.row(ib1, ib2)
