from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from dbase import chk_reg
from dbase.fakeprofile import add_fake_profile
from keyboards import registration_keys, search_keys
from FSM import Menu, Search
from funcs import start_registration, do_invalid, send_menu, show_myprofile, search


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


async def start_search(event: types.Message, state: FSMContext):
    await Search.searching.set()
    await event.answer(text="Уже ищу..", reply_markup=search_keys)
    await search(event, state)


async def profile(event: types.Message):
    await show_myprofile(event)


async def registration(event: types.Message):
    await start_registration(event)


async def registration_invalid(event: types.Message):
    await do_invalid(event, registration_keys)


async def reg_fake(event: types.Message):
    for _ in range(0, 10):
        await add_fake_profile()


def register_handlers_menu(dp: Dispatcher):
    dp.register_message_handler(startmessage)
    dp.register_message_handler(profile, state=Menu.menu, regexp='Мой профиль')
    dp.register_message_handler(start_search, state=Menu.menu, regexp='Начать поиск')
    dp.register_message_handler(reg_fake, state=Menu.menu, regexp='Фейк')
    dp.register_message_handler(registration, state=Menu.registration, regexp='Регистрация')
    dp.register_message_handler(registration_invalid, state=Menu.registration)
