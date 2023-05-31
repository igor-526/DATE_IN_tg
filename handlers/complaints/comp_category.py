from aiogram import types, Dispatcher
from create_bot import bot
from keyboards import cancel_keys, search_keys
from FSM import Complaints, Search
from aiogram.dispatcher import FSMContext
from funcs import do_invalid, comp_ask_desc


async def cancel(event: types.Message):
    await event.delete()
    await Search.searching.set()
    await bot.send_message(chat_id=event.from_user.id,
                           text="Жалоба отменена",
                           reply_markup=search_keys)


async def category(event: types.CallbackQuery, state: FSMContext):
    await state.update_data({'comp_cat': event.data, 'comp_media': [], 'comp_description': ''})
    await comp_ask_desc(event.from_user.id)


async def invalid(event: types.Message):
    await do_invalid(event, cancel_keys)


def register_handlers_comp_category(dp: Dispatcher):
    dp.register_message_handler(cancel, state=Complaints.category, regexp="Отмена")
    dp.register_callback_query_handler(category, state=Complaints.category, text='fake')
    dp.register_callback_query_handler(category, state=Complaints.category, text='sex_content')
    dp.register_callback_query_handler(category, state=Complaints.category, text='commercial')
    dp.register_callback_query_handler(category, state=Complaints.category, text='faking')
    dp.register_callback_query_handler(category, state=Complaints.category, text='illegal')
    dp.register_callback_query_handler(category, state=Complaints.category, text='abuse')
    dp.register_callback_query_handler(category, state=Complaints.category, text='age')
    dp.register_callback_query_handler(category, state=Complaints.category, text='other')
    dp.register_message_handler(invalid, state=Complaints.category)
