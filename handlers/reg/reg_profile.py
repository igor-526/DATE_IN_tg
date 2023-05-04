from aiogram import types, Dispatcher
from dbase import chk_reg
from keyboards import reg_profile_keys
from FSM import Reg
from funcs import start_registration, do_invalid, reg_ask_name


async def first_time(event: types.Message):
    await reg_ask_name(event)


async def via_vk(event: types.Message):
    await event.answer(text='Функционал пока не поддерживается')


async def invalid(event: types.Message):
    await do_invalid(event, reg_profile_keys)


def register_handlers_reg_profile(dp: Dispatcher):
    dp.register_message_handler(first_time, state=Reg.profile, regexp="Регистрируюсь первый раз")
    dp.register_message_handler(via_vk, state=Reg.profile, regexp="Вход через VK")
    dp.register_message_handler(invalid, state=Reg.profile)
