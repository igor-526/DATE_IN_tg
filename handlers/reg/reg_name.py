from aiogram import types, Dispatcher
from keyboards import yesnoback_keys
from FSM import Reg
from aiogram.dispatcher import FSMContext
from funcs import start_registration, do_invalid, reg_ask_bdate, reg_ask_name_manual
from validators import valid_name


async def yes(event: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = event.from_user.first_name
    await reg_ask_bdate(event)


async def no(event: types.Message):
    await reg_ask_name_manual(event)


async def back(event: types.Message):
    await start_registration(event)


async def invalid(event: types.Message):
    await do_invalid(event, yesnoback_keys)


async def manual(event: types.Message, state: FSMContext):
    validator = await valid_name(event.text)
    if validator == 'valid':
        async with state.proxy() as data:
            data['name'] = event.text.capitalize()
        await reg_ask_bdate(event)
    elif validator == 'short':
        await event.answer(text="Имя не может состоять из одного символа\nПопробуй ещё раз!")
    elif validator == 'long':
        await event.answer(text="Не устаёшь писать своё имя?\nПопробуй ещё раз!")
    elif validator == 'invalid':
        await event.answer(text='Я не верю в такое имя &#128563;\n'
                                'Попробуй ввести ещё раз',
                           parse_mode=types.ParseMode.HTML)
    elif validator == 'obscene':
        await event.answer(text='И кто же тебя так назвал.. &#128560;\n'
                                'Давай попробуем ещё раз, только нормально &#128514;',
                           parse_mode=types.ParseMode.HTML)


def register_handlers_reg_name(dp: Dispatcher):
    dp.register_message_handler(yes, state=Reg.name_auto, regexp="Да")
    dp.register_message_handler(no, state=Reg.name_auto, regexp="Нет")
    dp.register_message_handler(back, state=Reg.name_auto, regexp="Назад")
    dp.register_message_handler(manual, state=Reg.name_manual)
    dp.register_message_handler(invalid, state=Reg.name_auto)
