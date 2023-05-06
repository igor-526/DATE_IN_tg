from aiogram import types, Dispatcher
from dbase import chk_reg
from keyboards import reg_profile_keys
from FSM import Reg
from funcs import do_invalid, reg_ask_name, vk_ask_id


async def first_time(event: types.Message):
    await reg_ask_name(event)


async def via_vk(event: types.Message):
    await vk_ask_id(event)


async def invalid(event: types.Message):
    await do_invalid(event, reg_profile_keys)


def register_handlers_reg_profile(dp: Dispatcher):
    dp.register_message_handler(first_time, state=Reg.profile, regexp="Регистрируюсь первый раз")
    dp.register_message_handler(via_vk, state=Reg.profile, regexp="Вход через VK")
    dp.register_message_handler(invalid, state=Reg.profile)
