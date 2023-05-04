from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from FSM import Reg
from funcs import reg_ask_name, reg_ask_sex
from validators import valid_bdate


async def back(event: types.Message):
    await reg_ask_name(event)


async def valid(event: types.Message, state: FSMContext):
    validator = await valid_bdate(event.text)
    if validator == 'valid':
        async with state.proxy() as data:
            data['bdate'] = event.text
        await reg_ask_sex(event)
    elif validator == 'invalid':
        await event.answer(text='Не смог ничего сделать с этим сообщением\n'
                                'Пожалуйста, введи дату рождения в формате ДД.ММ.ГГГГ')
    elif validator == 'interval':
        await event.answer(text='У нас ограничение от 14 до 60 лет :(')


def register_handlers_reg_bdate(dp: Dispatcher):
    dp.register_message_handler(back, state=Reg.bdate, regexp="Назад")
    dp.register_message_handler(valid, state=Reg.bdate)
