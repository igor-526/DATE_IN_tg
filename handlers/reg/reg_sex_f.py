from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from FSM import Reg
from funcs import reg_ask_purposes, reg_ask_age_min, do_invalid
from keyboards import sex_f_keys


async def back(event: types.Message):
    await reg_ask_purposes(event)


async def male(event: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['sex_f'] = [2]
    await reg_ask_age_min(event)


async def female(event: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['sex_f'] = [1]
    await reg_ask_age_min(event)


async def all(event: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['sex_f'] = [1, 2]
    await reg_ask_age_min(event)


async def invalid(event: types.Message):
    await do_invalid(event, sex_f_keys)


def register_handlers_reg_sex_f(dp: Dispatcher):
    dp.register_message_handler(back, state=Reg.f_sex, regexp="Назад")
    dp.register_message_handler(male, state=Reg.f_sex, regexp="Мужчин")
    dp.register_message_handler(female, state=Reg.f_sex, regexp="Девушек")
    dp.register_message_handler(all, state=Reg.f_sex, regexp="Всех")
    dp.register_message_handler(invalid, state=Reg.f_sex)
