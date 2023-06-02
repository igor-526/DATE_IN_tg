from aiogram import types, Dispatcher
from keyboards import back_keys
from FSM import Reg
from aiogram.dispatcher import FSMContext
from funcs import reg_ask_description, reg_ask_f_sex
from validators import valid_purpose


async def back(event: types.Message):
    await reg_ask_description(event)


async def valid(event: types.Message, state: FSMContext):
    validator = await valid_purpose(event.text)
    if validator == 'invalid':
        await event.answer(text='Я так не понял\n'
                                'Пожалуйста, введите только номера целей, отделяя их запятой или пробелом',
                           reply_markup=back_keys)
    else:
        async with state.proxy() as data:
            data['purposes'] = validator
        await reg_ask_f_sex(event)


def register_handlers_reg_purposes(dp: Dispatcher):
    dp.register_message_handler(back, state=Reg.purposes, regexp="Назад")
    dp.register_message_handler(valid, state=Reg.purposes)
