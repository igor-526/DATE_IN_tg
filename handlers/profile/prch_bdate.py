import datetime
from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from keyboards import profile_keys
from FSM import Profile
from dbase import upd_bdate
from validators import valid_bdate
from funcs import show_myprofile


async def cancel(event: types.Message):
    await event.answer(text="Выберите действие:",
                       reply_markup=profile_keys)
    await Profile.show.set()


async def valid(event: types.Message, state: FSMContext):
    validator = await valid_bdate(event.text)
    if validator == 'valid':
        datelist = event.text.split('.')
        bdate = datetime.date(year=int(datelist[2]), month=int(datelist[1]), day=int(datelist[0]))
        await upd_bdate(event.from_user.id, bdate)
        await event.answer(text='Поменял успешно!')
        await show_myprofile(event, state)
    elif validator == 'invalid':
        await event.answer(text='Не смог ничего сделать с этим сообщением\n'
                                'Пожалуйста, введи дату рождения в формате ДД.ММ.ГГГГ')
    elif validator == 'interval':
        await event.answer(text='У нас ограничение от 14 до 60 лет :(')


def register_handlers_prch_bdate(dp: Dispatcher):
    dp.register_message_handler(cancel, state=Profile.bdate, regexp="Отмена")
    dp.register_message_handler(valid, state=Profile.bdate)
