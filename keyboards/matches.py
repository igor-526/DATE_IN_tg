from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.exceptions import BadRequest

b1 = KeyboardButton("Меню")
b2 = KeyboardButton("\U000025B6")
b3 = KeyboardButton("Просмотренные")
match_keys = ReplyKeyboardMarkup(resize_keyboard=True)
match_keys.row(b1, b2).add(b3)


b1 = KeyboardButton("Начать поиск")
b2 = KeyboardButton("Меню")
b3 = KeyboardButton("Просмотренные")
nomatch_keys = ReplyKeyboardMarkup(resize_keyboard=True)
nomatch_keys.add(b1).row(b2, b3)


b1 = KeyboardButton("\U000025C0")
b2 = KeyboardButton("\U000025B6")
b3 = KeyboardButton("Меню")
b4 = KeyboardButton("Начать поиск")
oldmatch_keys = ReplyKeyboardMarkup(resize_keyboard=True)
oldmatch_keys.row(b1, b2).add(b3)


b1 = KeyboardButton("Начать поиск")
b2 = KeyboardButton("Меню")
oldnomatch_keys = ReplyKeyboardMarkup(resize_keyboard=True)
oldnomatch_keys.add(b1).add(b2)


async def match_inline_keys(contacts):
    ib1 = InlineKeyboardButton(text="\U0001F4F7", callback_data='all_photos')
    ib2 = InlineKeyboardButton(text='\U0001F4DD', callback_data='description')
    ib3 = InlineKeyboardButton(text='Пожаловаться', callback_data='complaint')
    keys = InlineKeyboardMarkup()
    keys.row(ib1, ib2)
    if contacts['cont_tg']:
        keys.add(InlineKeyboardButton(text='TG', url=contacts['cont_tg']))
    if contacts['cont_vk']:
        keys.add(InlineKeyboardButton(text='ВК', url=contacts['cont_vk']))
    keys.add(ib3)
    return keys