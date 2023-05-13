from aiogram import types, Dispatcher
from keyboards import profile_keys, sex_f_keys
from FSM import Profile
from dbase import upd_sex_f
from funcs import show_myprofile, do_invalid


async def cancel(event: types.Message):
    await event.answer(text="Выберите действие:",
                       reply_markup=profile_keys)
    await Profile.show.set()


async def set_male(event: types.Message):
    await upd_sex_f(event.from_user.id, [2])
    await event.answer(text='Настройки поиска обновлены')
    await show_myprofile(event)


async def set_female(event: types.Message):
    await upd_sex_f(event.from_user.id, [1])
    await event.answer(text='Настройки поиска обновлены')
    await show_myprofile(event)


async def set_all(event: types.Message):
    await upd_sex_f(event.from_user.id, [1, 2])
    await event.answer(text='Настройки поиска обновлены')
    await show_myprofile(event)


async def invalid(event: types.Message):
    await do_invalid(event, sex_f_keys)


def register_handlers_prch_sex_f(dp: Dispatcher):
    dp.register_message_handler(cancel, state=Profile.sex_f, regexp="Назад")
    dp.register_message_handler(set_male, state=Profile.sex_f, regexp="Мужчин")
    dp.register_message_handler(set_female, state=Profile.sex_f, regexp="Девушек")
    dp.register_message_handler(set_all, state=Profile.sex_f, regexp="Всех")
    dp.register_message_handler(invalid, state=Profile.sex_f)
