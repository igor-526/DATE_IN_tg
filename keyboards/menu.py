from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from dbase import count_matches


async def menu_keys(tg_id):
    match_count = await count_matches(tg_id)
    b1 = KeyboardButton("Поиск")
    b2 = KeyboardButton(f"Пары ({match_count})")
    b3 = KeyboardButton("Обновить гео")
    b4 = KeyboardButton("Профиль")
    keys = ReplyKeyboardMarkup(resize_keyboard=True)
    keys.row(b1, b2).row(b3, b4)
    return keys
