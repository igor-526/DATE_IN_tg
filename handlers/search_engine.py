from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from dbase import profile_like, profile_pass
from FSM import Search
from funcs import send_menu, search


async def like_profile(event: types.Message, state: FSMContext):
    data = await state.get_data()
    await profile_like(data['id'], data['offer'])
    await search(event, state)


async def pass_profile(event: types.Message, state: FSMContext):
    data = await state.get_data()
    await profile_pass(data['id'], data['offer'])
    await search(event, state)


async def menu(event: types.Message):
    await send_menu(event)


def register_handlers_search(dp: Dispatcher):
    dp.register_message_handler(like_profile, state=Search.searching, regexp='ЛАЙК')
    dp.register_message_handler(pass_profile, state=Search.searching, regexp='Далее')
    dp.register_message_handler(menu, state=Search.searching, regexp='Меню')