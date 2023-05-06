import config
from aiogram import types
from FSM import ViaVK
from keyboards import back_keys, code_keys
from dbase import add_tg_id
import requests
import random


async def vk_ask_id(event: types.Message):
    await event.answer(text='Пожалуйста, введи id твоего профиля\n'
                            'Найти его можно в настройках профиля',
                       reply_markup=back_keys)
    await ViaVK.id.set()


async def send_code(vk_id):
    code = random.randint(10000, 99999)
    msg = f'Одноразовый код для входа в DATE IN через Telegram: {code}'
    url = "https://api.vk.com/method/messages.send"
    params = {
        "access_token": config.vk_token,
        "v": "5.131",
        "user_id": vk_id,
        "random_id": random.randint(2000000000, 2147483647),
        "message": msg
    }
    response = requests.get(url, params=params)
    return code if response.status_code == 200 else None


async def ask_code(event: types.Message):
        await event.answer(text='Отправил тебе в ВК пятизначный код! Введи его здесь',
                           reply_markup=code_keys)
        await ViaVK.code.set()


async def vk_finish(event: types.Message, id):
    await add_tg_id(prof_id=id,
                    tg_id=event.from_user.id,
                    tg_nick=event.from_user.username,
                    tg_url=event.from_user.url)
    await event.answer(text="Готово. Успешный вход через ВК!")
