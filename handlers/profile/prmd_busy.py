from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from create_bot import bot
from FSM import Profile
from keyboards import profile_inline_keys
from dbase import upd_d_busy


async def no(event: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    await upd_d_busy(data['pr_id'], "не учусь и не работаю")
    await bot.send_message(chat_id=event.from_user.id,
                           text="Записал!\n"
                                "Какую дополнительную информацию хочешь указать?",
                           reply_markup=profile_inline_keys)
    await bot.delete_message(chat_id=event.from_user.id,
                             message_id=data['msg'])
    await Profile.desc_more.set()


async def learning(event: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    await upd_d_busy(data['pr_id'], "только учусь")
    await bot.send_message(chat_id=event.from_user.id,
                           text="Записал!\n"
                                "Какую дополнительную информацию хочешь указать?",
                           reply_markup=profile_inline_keys)
    await bot.delete_message(chat_id=event.from_user.id,
                             message_id=data['msg'])
    await Profile.desc_more.set()


async def working(event: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    await upd_d_busy(data['pr_id'], "только работаю")
    await bot.send_message(chat_id=event.from_user.id,
                           text="Записал!\n"
                                "Какую дополнительную информацию хочешь указать?",
                           reply_markup=profile_inline_keys)
    await bot.delete_message(chat_id=event.from_user.id,
                             message_id=data['msg'])
    await Profile.desc_more.set()


async def landw(event: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    await upd_d_busy(data['pr_id'], "учусь и работаю")
    await bot.send_message(chat_id=event.from_user.id,
                           text="Записал!\n"
                                "Какую дополнительную информацию хочешь указать?",
                           reply_markup=profile_inline_keys)
    await bot.delete_message(chat_id=event.from_user.id,
                             message_id=data['msg'])
    await Profile.desc_more.set()


async def clean(event: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    await upd_d_busy(data['pr_id'])
    await bot.delete_message(chat_id=event.from_user.id,
                             message_id=event.message.message_id)
    await bot.send_message(chat_id=event.from_user.id,
                           text="Успешно очистил!\n"
                                "Какую дополнительную информацию хочешь указать?",
                           reply_markup=profile_inline_keys)
    await Profile.desc_more.set()


async def back(event: types.CallbackQuery):
    await bot.delete_message(chat_id=event.from_user.id,
                             message_id=event.message.message_id)
    await bot.send_message(chat_id=event.from_user.id,
                           text="Какую дополнительную информацию хочешь указать?",
                           reply_markup=profile_inline_keys)
    await Profile.desc_more.set()


async def invalid(event: types.Message):
    await event.delete()
    await event.answer(text="Я вас не понимаю &#128532;\n"
                            "Пожалуйста, выберите действие на клавиатуре",
                       parse_mode=types.ParseMode.HTML)


def register_handlers_prmd_busy(dp: Dispatcher):
    dp.register_callback_query_handler(no, state=Profile.d_m_busy, text='none')
    dp.register_callback_query_handler(learning, state=Profile.d_m_busy, text='learning')
    dp.register_callback_query_handler(working, state=Profile.d_m_busy, text='working')
    dp.register_callback_query_handler(landw, state=Profile.d_m_busy, text='and')
    dp.register_callback_query_handler(clean, state=Profile.d_m_busy, text='clean')
    dp.register_callback_query_handler(back, state=Profile.d_m_busy, text='back')
    dp.register_message_handler(invalid, state=Profile.d_m_busy)
