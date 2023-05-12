from aiogram import types, Dispatcher
from dbase import chk_reg
from keyboards import registration_keys
from FSM import Menu
from funcs import start_registration, do_invalid, send_menu, show_myprofile


async def startmessage(event: types.Message):
    check = await chk_reg(event.from_user.id)
    if check:
        if check.status == 'active':
            await event.answer(f'Добро пожаловать, {check.name}')
            await send_menu(event)
    else:
        await event.answer(text="Добро пожаловать в DATE IN!\n"
                                "Для начала использования необходимо зарегистрироваться",
                           reply_markup=registration_keys)
        await Menu.registration.set()


async def profile(event: types.Message):
    await show_myprofile(event)


async def registration(event: types.Message):
    await start_registration(event)


async def registration_invalid(event: types.Message):
    await do_invalid(event, registration_keys)


def register_handlers_menu(dp: Dispatcher):
    dp.register_message_handler(startmessage)
    dp.register_message_handler(profile, state=Menu.menu, regexp='Мой профиль')
    dp.register_message_handler(registration, state=Menu.registration, regexp='Регистрация')
    dp.register_message_handler(registration_invalid, state=Menu.registration)
