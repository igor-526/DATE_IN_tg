from aiogram import types, Dispatcher
from keyboards import profile_keys
from FSM import Profile
from dbase import upd_purposes
from validators import valid_purpose
from funcs import show_myprofile


async def cancel(event: types.Message):
    await event.answer(text="Выберите действие:",
                       reply_markup=profile_keys)
    await Profile.show.set()


async def valid(event: types.Message):
    validator = await valid_purpose(event.text)
    if validator == 'invalid':
        await event.answer(text='Я так не понял\n'
                                'Пожалуйста, введите только номера целей, отделяя их запятой или пробелом')
    else:
        await upd_purposes(event.from_user.id, validator)
        await event.answer(text="Успешно поменял!")
        await show_myprofile(event)


def register_handlers_prch_purposes(dp: Dispatcher):
    dp.register_message_handler(cancel, state=Profile.purposes, regexp="Отмена")
    dp.register_message_handler(valid, state=Profile.purposes)
