from aiogram import types
from FSM import Menu
from keyboards import menu_keys


async def send_menu(event: types.Message):
    menu_keyss = await menu_keys(event.from_user.id)
    await event.answer(text="Выберите действие:",
                       reply_markup=menu_keyss)
    await Menu.menu.set()
