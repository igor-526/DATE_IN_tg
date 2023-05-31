from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from dbase import chk_reg, get_profile_id
from keyboards import registration_keys, search_keys, match_keys
from FSM import Menu, Search
from funcs import start_registration, do_invalid, send_menu, show_myprofile, search, show_new_match


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


async def go_matches(event: types.Message, state: FSMContext):
    pr_id = await get_profile_id(event.from_user.id)
    await event.answer(text='Секунду..', reply_markup=match_keys)
    await state.update_data({'pr_id': pr_id})
    await show_new_match(event, state)


async def profile(event: types.Message, state: FSMContext):
    pr_id = await get_profile_id(event.from_user.id)
    await state.update_data({'pr_id': pr_id})
    await show_myprofile(event)


async def registration(event: types.Message):
    await start_registration(event)


async def registration_invalid(event: types.Message):
    await do_invalid(event, registration_keys)


async def menu_invalid(event: types.Message):
    await event.answer(text="Я вас не понимаю &#128532;\n"
                            "Пожалуйста, выберите действие на клавиатуре\n"
                            "Если её нет, используйте /menu для выхода в главное меню",
                       parse_mode=types.ParseMode.HTML)


def register_handlers_menu(dp: Dispatcher):
    dp.register_message_handler(startmessage)
    dp.register_message_handler(profile, state=Menu.menu, regexp='Профиль')
    dp.register_message_handler(start_search, state=Menu.menu, regexp='Поиск')
    dp.register_message_handler(go_matches, state=Menu.menu, regexp='Пары')
    dp.register_message_handler(registration, state=Menu.registration, regexp='Регистрация')
    dp.register_message_handler(menu_invalid, state=Menu.menu)
    dp.register_message_handler(registration_invalid, state=Menu.registration)
