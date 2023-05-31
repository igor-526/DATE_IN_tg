from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


ib1 = InlineKeyboardButton(text='Фейковый профиль/данные', callback_data='fake')
ib2 = InlineKeyboardButton(text='Откровенный контент', callback_data='sex_content')
ib3 = InlineKeyboardButton(text='Коммерческая деятельность', callback_data='commercial')
ib4 = InlineKeyboardButton(text='Мошенничество', callback_data='faking')
ib5 = InlineKeyboardButton(text='Призывы к незаконным действиям', callback_data='illegal')
ib6 = InlineKeyboardButton(text='Неадекватное поведение/оскорбление', callback_data='abuse')
ib7 = InlineKeyboardButton(text='Младше 14 лет', callback_data='age')
ib8 = InlineKeyboardButton(text='Другое', callback_data='other')
complaint_keys = InlineKeyboardMarkup()
complaint_keys.add(ib1).add(ib2).add(ib3).add(ib4).add(ib5).add(ib6).add(ib7).add(ib8)
