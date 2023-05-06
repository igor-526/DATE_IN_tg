from aiogram import types, Dispatcher
from keyboards import yesno_keys
from FSM import ViaVK
from aiogram.dispatcher import FSMContext
from funcs import start_registration, vk_ask_id, do_invalid, send_code, ask_code


async def yes(event: types.Message, state: FSMContext):
    data = await state.get_data()
    code = await send_code(data["vk_id"])
    if code:
        await state.update_data(data={'code': code})
        await ask_code(event)
    else:
        await event.answer(text="Что-то пошло не так\n"
                                "Попробуйте ещё раз позже")
        await start_registration(event)


async def no(event: types.Message):
    await vk_ask_id(event)


async def invalid(event: types.Message):
    await do_invalid(event, yesno_keys)


def register_handlers_viavk_confirm(dp: Dispatcher):
    dp.register_message_handler(yes, state=ViaVK.confirm, regexp="Да")
    dp.register_message_handler(no, state=ViaVK.confirm, regexp="Нет")
    dp.register_message_handler(invalid, state=ViaVK.confirm)
