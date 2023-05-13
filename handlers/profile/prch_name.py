from aiogram import types, Dispatcher
from keyboards import profile_keys
from FSM import Profile
from dbase import upd_name
from validators import valid_name
from funcs import show_myprofile


async def cancel(event: types.Message):
    await event.answer(text="Выберите действие:",
                       reply_markup=profile_keys)
    await Profile.show.set()


async def valid(event: types.Message):
    validator = await valid_name(event.text)
    if validator == 'valid':
        await upd_name(event.from_user.id, event.text)
        await event.answer(text="Успешно!")
        await show_myprofile(event)
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


def register_handlers_prch_name(dp: Dispatcher):
    dp.register_message_handler(cancel, state=Profile.name, regexp="Отмена")
    dp.register_message_handler(valid, state=Profile.name)
