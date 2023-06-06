from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from dbase import chk_reg, get_profile_id, dates_info, upd_activate_profile, del_profile
from keyboards import registration_keys, search_keys, match_keys, return_keys, menu_keys, geo_keys
from FSM import Menu, Search
from funcs import start_registration, do_invalid, send_menu, show_myprofile, search, show_new_match
from datetime import datetime, timedelta, timezone


async def startmessage(event: types.Message, state: FSMContext):
    check = await chk_reg(event.from_user.id)
    if check:
        pr_id = check.id
        await state.update_data({'pr_id': pr_id})
        if check.status == 'active':
            await event.answer(f'Добро пожаловать, {check.name}')
            await send_menu(event, state)
        if check.status == 'deactivated':
            datesinfo = await dates_info(pr_id)
            if datesinfo['deactivated'] + timedelta(days=7) <= datetime.now(tz=timezone.utc):
                await del_profile(pr_id)
                await event.answer(text="Добро пожаловать в DATE IN!\n"
                                        "Для начала использования необходимо зарегистрироваться",
                                   reply_markup=registration_keys)
                await Menu.registration.set()
            else:
                await event.answer(text=f"Профиль был деактивирован "
                                        f"{datesinfo['deactivated'].strftime('%d.%m %H:%M')}\n"
                                        f"Окончательно удалён он будет "
                                        f"{(datesinfo['deactivated'] + timedelta(days=7)).strftime('%d.%m %H:%M')}\n"
                                        f"Сейчас его можно только восстановить",
                                   reply_markup=return_keys)
        if check.status == 'freeze':
            await event.answer(text='Ваш профиль был временно заморожен администрацией, так как нарушал правила '
                                    'использования сервиса\n'
                                    'Если Вы с этим не согласны, напишите в /report')
    else:
        await event.answer(text="Добро пожаловать в DATE IN!\n"
                                "Для начала использования необходимо зарегистрироваться",
                           reply_markup=registration_keys)
        await Menu.registration.set()


async def activateprofile(event: types.Message, state: FSMContext):
    try:
        data = await state.get_data()
        await upd_activate_profile(data['pr_id'])
        await event.delete()
        keys = await menu_keys(data['pr_id'])
        await event.answer(text="Профиль успешно восстановлен\nВыберите действие:",
                           reply_markup=keys)
        await Menu.menu.set()
    except Exception:
        await startmessage(event, state)


async def start_search(event: types.Message, state: FSMContext):
    check = await chk_reg(event.from_user.id)
    if check.status == 'active':
        await Search.searching.set()
        await event.answer(text="Уже ищу..", reply_markup=search_keys)
        await search(event, state)
    elif check.status == 'freeze':
        await event.answer(text='Ваш профиль был временно заморожен администрацией, так как нарушал правила '
                                'использования сервиса\n'
                                'Если Вы с этим не согласны, напишите в /report')
        await send_menu(event, state)


async def go_matches(event: types.Message, state: FSMContext):
    pr_id = await get_profile_id(event.from_user.id)
    await event.answer(text='Секунду..', reply_markup=match_keys)
    await state.update_data({'pr_id': pr_id})
    await show_new_match(event, state)


async def updgeo(event: types.Message, state: FSMContext):
    data = await state.get_data()
    if not data.get("pr_id"):
        pr_id = await get_profile_id(event.from_user.id)
        await state.update_data({'pr_id': pr_id})
    await event.delete()
    await event.answer(text="Отправьте мне своё местоположение, чтобы я смог подбирать профили сначала поближе!\n"
                            "Ты можешь вложением отправить примерное местоположение, если не хочешь делиться настоящим\n"
                            "В любом случае, эти данные останутся исключительно между нами!",
                       reply_markup=geo_keys)
    await Menu.updgeo.set()


async def profile(event: types.Message, state: FSMContext):
    await show_myprofile(event, state)


async def registration(event: types.Message):
    await start_registration(event)


async def registration_invalid(event: types.Message):
    await do_invalid(event, registration_keys)


async def menu_invalid(event: types.Message):
    await event.delete()
    await event.answer(text="Я вас не понимаю &#128532;\n"
                            "Пожалуйста, выберите действие на клавиатуре\n"
                            "Если её нет, используйте /menu для выхода в главное меню",
                       parse_mode=types.ParseMode.HTML)


def register_handlers_menu(dp: Dispatcher):
    dp.register_message_handler(activateprofile, regexp='Восстановить')
    dp.register_message_handler(startmessage)
    dp.register_message_handler(profile, state=Menu.menu, regexp='Профиль')
    dp.register_message_handler(start_search, state=Menu.menu, regexp='Поиск')
    dp.register_message_handler(go_matches, state=Menu.menu, regexp='Пары')
    dp.register_message_handler(updgeo, state=Menu.menu, regexp="Обновить \U0001F4CD")
    dp.register_message_handler(registration, state=Menu.registration, regexp='Регистрация')
    dp.register_message_handler(menu_invalid, state=Menu.menu)
    dp.register_message_handler(registration_invalid, state=Menu.registration)
