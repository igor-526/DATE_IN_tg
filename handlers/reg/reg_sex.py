from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from FSM import Reg
from funcs import reg_ask_bdate, do_invalid, reg_ask_geo
from keyboards import sex_keys


async def back(event: types.Message):
    await reg_ask_bdate(event)


async def male(event: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['sex'] = 2
    await reg_ask_geo(event)


async def female(event: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['sex'] = 1
    await reg_ask_geo(event)


async def invalid(event: types.Message):
    await do_invalid(event, sex_keys)


def register_handlers_reg_sex(dp: Dispatcher):
    dp.register_message_handler(back, state=Reg.sex, regexp="Назад")
    dp.register_message_handler(male, state=Reg.sex, regexp="Мужчина")
    dp.register_message_handler(male, state=Reg.sex, regexp="Девушка")
    dp.register_message_handler(invalid, state=Reg.sex)
