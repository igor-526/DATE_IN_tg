from aiogram import types
from FSM import Menu
from keyboards import menu_keys


async def send_menu(event: types.Message):
    await event.answer(text="Выберите действие:",
                       reply_markup=menu_keys)
    await Menu.menu.set()
