from aiogram import types
from FSM import Menu
from aiogram.dispatcher import FSMContext
from keyboards import menu_keys
from dbase import get_profile_id


async def send_menu(event: types.Message, state: FSMContext):
    data = await state.get_data()
    if data.get('pr_id'):
        menu_keyss = await menu_keys(data['pr_id'])
        await event.answer(text="Выберите действие:",
                           reply_markup=menu_keyss)
        await Menu.menu.set()
    else:
        try:
            pr_id = await get_profile_id(event.from_user.id)
            await state.update_data({'pr_id': pr_id})
            menu_keyss = await menu_keys(pr_id)
            await event.answer(text="Выберите действие:",
                               reply_markup=menu_keyss)
            await Menu.menu.set()
        except:
            await event.answer(text="Ошибка. Профиль не зарегистрирован")

