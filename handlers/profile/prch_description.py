from aiogram import types, Dispatcher
from keyboards import profile_keys
from FSM import Profile
from dbase import upd_description
from validators import valid_description
from funcs import show_myprofile


async def cancel(event: types.Message):
    await event.answer(text="Выберите действие:",
                       reply_markup=profile_keys)
    await Profile.show.set()


async def valid(event: types.Message):
    validator = await valid_description(event.text)
    if validator == 'valid':
        await upd_description(event.from_user.id, event.text)
        await event.answer(text='Описание успешно обновлено!')
        await show_myprofile(event)
    elif validator == 'obscene':
        await event.answer(text="Мы против нецензурной лексики\n"
                                "фильтр мог сработать ошибочно, пока что оставим так, но твоё описание бует отправлено "
                                "на модерацию")
        await upd_description(event.from_user.id, event.text)
        await show_myprofile(event)
    elif validator == 'long':
        await event.answer(text="Слишком длинное описание\n"
                                "К сожалению, это не наше ограничение, а мессенджеров")


def register_handlers_prch_description(dp: Dispatcher):
    dp.register_message_handler(cancel, state=Profile.description, regexp="Отмена")
    dp.register_message_handler(valid, state=Profile.description)
