from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from keyboards import profile_keys, sex_keys
from FSM import Profile
from dbase import upd_sex
from funcs import show_myprofile, do_invalid


async def cancel(event: types.Message):
    await event.answer(text="Выберите действие:",
                       reply_markup=profile_keys)
    await Profile.show.set()


async def set_male(event: types.Message, state: FSMContext):
    await upd_sex(event.from_user.id, 2)
    await event.answer(text='Успешно поменяли!')
    await show_myprofile(event, state)


async def set_female(event: types.Message, state: FSMContext):
    await upd_sex(event.from_user.id, 1)
    await event.answer(text='Успешно поменяли!')
    await show_myprofile(event, state)


async def invalid(event: types.Message):
    await do_invalid(event, sex_keys)


def register_handlers_prch_sex(dp: Dispatcher):
    dp.register_message_handler(cancel, state=Profile.sex, regexp="Назад")
    dp.register_message_handler(set_male, state=Profile.sex, regexp="Мужчина")
    dp.register_message_handler(set_female, state=Profile.sex, regexp="Девушка")
    dp.register_message_handler(invalid, state=Profile.sex)
