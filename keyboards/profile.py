from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

b1 = KeyboardButton("Назад")
b2 = KeyboardButton("Имя")
b3 = KeyboardButton("Дата рождения")
b4 = KeyboardButton("Пол")
b5 = KeyboardButton("Цели")
b6 = KeyboardButton("Геопозиция")
b7 = KeyboardButton("Описание")
b8 = KeyboardButton("Удал. фото")
b9 = KeyboardButton("Доб. фото")
b10 = KeyboardButton("Изменить возраст поиска")
b11 = KeyboardButton("Изменить пол поиска")
b12 = KeyboardButton("Удалить профиль")

profile_keys = ReplyKeyboardMarkup(resize_keyboard=True)
profile_keys.add(b1).row(b2, b3).row(b4, b5).row(b6, b7).row(b8, b9).add(b10).add(b11).add(b12)
