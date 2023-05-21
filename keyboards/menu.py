from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from dbase import count_matches


async def menu_keys(tg_id):
    match_count = await count_matches(tg_id)
    b1 = KeyboardButton("Начать поиск")
    b2 = KeyboardButton(f"Пары ({match_count})")
    b3 = KeyboardButton("Обновить геолокацию")
    b4 = KeyboardButton("Мой профиль")
    b5 = KeyboardButton("Жалоба|Репорт")
    keys = ReplyKeyboardMarkup(resize_keyboard=True)
    keys.add(b1).add(b2).add(b3).add(b4).add(b5)
    return keys
