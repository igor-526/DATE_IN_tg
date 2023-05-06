from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from FSM import Reg
from funcs import reg_ask_photos, reg_ask_purposes
from validators import valid_description
from keyboards import back_keys


async def back(event: types.Message, state: FSMContext):
    await reg_ask_photos(event, state)


async def skip(event: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['description'] = None
    await reg_ask_purposes(event)


async def valid(event: types.Message, state: FSMContext):
    validator = await valid_description(event.text)
    if validator == 'valid':
        async with state.proxy() as data:
            data['description'] = event.text
        await reg_ask_purposes(event)
    elif validator == 'obscene':
        await event.answer(text="Мы против нецензурной лексики\n"
                                "Попробуй переписать так, чтобы её там не было",
                           reply_markup=back_keys)
    elif validator == 'long':
        await event.answer(text="Слишком длинное описание\n"
                                "К сожалению, это не наше ограничение, а мессенджеров",
                           reply_markup=back_keys)


def register_handlers_reg_description(dp: Dispatcher):
    dp.register_message_handler(back, state=Reg.description, regexp="Назад")
    dp.register_message_handler(skip, state=Reg.description, regexp="Пропустить")
    dp.register_message_handler(valid, state=Reg.description)
