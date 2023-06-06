from aiogram import types, Dispatcher
from keyboards import code_keys
from FSM import ViaVK
from aiogram.dispatcher import FSMContext
from funcs import start_registration, vk_ask_id, send_code, ask_code, send_menu, vk_finish


async def again(event: types.Message, state: FSMContext):
    data = await state.get_data()
    code = await send_code(data["vk_id"])
    if code:
        await state.update_data(data={'code': code})
        await ask_code(event)
    else:
        await event.answer(text="Что-то пошло не так\n"
                                "Попробуйте ещё раз позже")
        await start_registration(event)


async def back(event: types.Message):
    await vk_ask_id(event)


async def valid(event: types.Message, state: FSMContext):
    data = await state.get_data()
    try:
        if int(event.text) == data['code']:
            await vk_finish(event, data['prof_id'])
            await send_menu(event, state)
        else:
            await event.answer(text="Код неверный!\n"
                                    "Попробуй ещё раз",
                               reply_markup=code_keys)
    except:
        await event.answer(text="Пожалуйста, введи только 5 цифр, которые я отправил тебе в ВК",
                           reply_markup=code_keys)


def register_handlers_viavk_code(dp: Dispatcher):
    dp.register_message_handler(again, state=ViaVK.code, regexp="Отправить ещё раз")
    dp.register_message_handler(back, state=ViaVK.code, regexp="Назад")
    dp.register_message_handler(valid, state=ViaVK.code)
