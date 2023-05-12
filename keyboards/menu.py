from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

b1 = KeyboardButton("Начать поиск")
b2 = KeyboardButton("Пары (0)")
b3 = KeyboardButton("Обновить геолокацию")
b4 = KeyboardButton("Мой профиль")
b5 = KeyboardButton("Жалоба|Репорт")

menu_keys = ReplyKeyboardMarkup(resize_keyboard=True)
menu_keys.add(b1).add(b2).add(b3).add(b4).add(b5)
