from aiogram import types, Dispatcher
from create_bot import bot
from keyboards import yesno_keys, search_keys, match_keys
from FSM import Complaints, Search
from aiogram.dispatcher import FSMContext
from funcs import do_invalid, comp_send, show_new_match


async def cancel(event: types.Message, state: FSMContext):
    await event.delete()
    data = await state.get_data()
    if data['back_to'] == 'search':
        await Search.searching.set()
        await bot.send_message(chat_id=event.from_user.id,
                               text="Жалоба отменена",
                               reply_markup=search_keys)
    elif data['back_to'] == 'matches':
        await bot.send_message(chat_id=event.from_user.id,
                               text="Жалоба отменена")
        await event.answer(text='Секунду..', reply_markup=match_keys)
        await show_new_match(event, state)


async def yes(event: types.Message, state: FSMContext):
    await comp_send(event, state)


async def invalid(event: types.Message):
    await do_invalid(event, yesno_keys)


def register_handlers_comp_confirm(dp: Dispatcher):
    dp.register_message_handler(cancel, state=Complaints.confirm, regexp="Нет")
    dp.register_message_handler(yes, state=Complaints.confirm, regexp="Да")
    dp.register_message_handler(invalid, state=Complaints.confirm)
