from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from keyboards import yesno_keys
from FSM import Profile
from dbase import upd_deactivate_profile
from funcs import show_myprofile, do_invalid
from datetime import datetime, timedelta


async def yes(event: types.Message, state: FSMContext):
    await event.delete()
    data = await state.get_data()
    await upd_deactivate_profile(data['pr_id'])
    await event.answer(text=f"Профиль успешно деактивирован\n"
                            f"Окончательно он удалится "
                            f"{(datetime.now()+timedelta(days=7)).strftime('%d.%m %H:%M')}\n"
                            f"До этого момента его можно будет только восстановить",
                       reply_markup=types.ReplyKeyboardRemove())
    await state.finish()


async def no(event: types.Message):
    await event.delete()
    await show_myprofile(event)


async def invalid(event: types.Message):
    await do_invalid(event, yesno_keys)


def register_handlers_prch_delprofile(dp: Dispatcher):
    dp.register_message_handler(yes, state=Profile.delete, regexp="Да")
    dp.register_message_handler(no, state=Profile.delete, regexp="Нет")
    dp.register_message_handler(invalid, state=Profile.delete)
