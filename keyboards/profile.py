from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

b1 = KeyboardButton("Назад")
b2 = KeyboardButton("Имя")
b3 = KeyboardButton("Дата рождения")
b4 = KeyboardButton("Пол")
b5 = KeyboardButton("Цели")
b6 = KeyboardButton("Геопозиция")
b7 = KeyboardButton("Описание")
b8 = KeyboardButton("Удал. фото")
b9 = KeyboardButton("Доб. фото")
b10 = KeyboardButton("Дополнительно")
b11 = KeyboardButton("Фильтры")
b12 = KeyboardButton("Удалить профиль")

profile_keys = ReplyKeyboardMarkup(resize_keyboard=True)
profile_keys.add(b1).row(b2, b3).row(b4, b5).row(b6, b7).row(b8, b9).row(b10, b11).add(b12)


b1 = KeyboardButton("Возраст")
b2 = KeyboardButton("Пол")
b3 = KeyboardButton("Расстояние")
b4 = KeyboardButton("Назад")
filter_keys = ReplyKeyboardMarkup(resize_keyboard=True)
filter_keys.row(b1, b2).row(b3, b4)


ib1 = InlineKeyboardButton(text='Рост', callback_data='height')
ib2 = InlineKeyboardButton(text='Хобби', callback_data='hobby')
ib3 = InlineKeyboardButton(text='Занятость', callback_data='busy')
ib4 = InlineKeyboardButton(text='Дети', callback_data='children')
ib5 = InlineKeyboardButton(text='Дом. животные', callback_data='animals')
ib6 = InlineKeyboardButton(text='Вр. привычки', callback_data='habit')
ib7 = InlineKeyboardButton(text='В профиль', callback_data='profile')
profile_inline_keys = InlineKeyboardMarkup()
profile_inline_keys.row(ib1, ib2).row(ib3, ib4).row(ib5, ib6).add(ib7)


ib1 = InlineKeyboardButton(text='Рост', callback_data='height')
ib2 = InlineKeyboardButton(text='Хобби', callback_data='hobby')
ib3 = InlineKeyboardButton(text='Занятость', callback_data='busy')
ib4 = InlineKeyboardButton(text='Дети', callback_data='children')
ib5 = InlineKeyboardButton(text='Дом. животные', callback_data='animals')
ib6 = InlineKeyboardButton(text='Вр. привычки', callback_data='habit')
ib7 = InlineKeyboardButton(text='В профиль', callback_data='profile')
ib8 = InlineKeyboardButton(text='ПЕРЕЙТИ В МЕНЮ', callback_data='menu')
profilereg_inline_keys = InlineKeyboardMarkup()
profilereg_inline_keys.row(ib1, ib2).row(ib3, ib4).row(ib5, ib6).add(ib7).add(ib8)


backkey = InlineKeyboardButton(text='Назад', callback_data='back')
cleankey = InlineKeyboardButton(text='Очистить', callback_data='clean')
backin_keys = InlineKeyboardMarkup()
backin_keys.row(cleankey, backkey)


ib1 = InlineKeyboardButton(text='Имею ребёнка/детей', callback_data='yes')
ib2 = InlineKeyboardButton(text='Планирую', callback_data='plan')
ib3 = InlineKeyboardButton(text='Пока не планирую', callback_data='no')
children_keys = InlineKeyboardMarkup()
children_keys.add(ib1).add(ib2).add(ib3).row(cleankey, backkey)


ib1 = InlineKeyboardButton(text='не учусь/не работаю', callback_data='none')
ib2 = InlineKeyboardButton(text='учусь/не работаю', callback_data='learning')
ib3 = InlineKeyboardButton(text='не учусь/работаю', callback_data='working')
ib4 = InlineKeyboardButton(text='учусь/работаю', callback_data='and')
busy_keys = InlineKeyboardMarkup()
busy_keys.row(ib1, ib2).row(ib3, ib4).row(cleankey, backkey)
