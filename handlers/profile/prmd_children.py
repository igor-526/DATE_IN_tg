from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from create_bot import bot
from FSM import Profile
from keyboards import profile_inline_keys
from dbase import upd_d_children


async def yes(event: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    await upd_d_children(data['pr_id'], "имею ребёнка/детей")
    await bot.send_message(chat_id=event.from_user.id,
                           text="Записал!\n"
                                "Какую дополнительную информацию хочешь указать?",
                           reply_markup=profile_inline_keys)
    await bot.delete_message(chat_id=event.from_user.id,
                             message_id=data['msg'])
    await Profile.desc_more.set()


async def plan(event: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    await upd_d_children(data['pr_id'], "планирую")
    await bot.send_message(chat_id=event.from_user.id,
                           text="Записал!\n"
                                "Какую дополнительную информацию хочешь указать?",
                           reply_markup=profile_inline_keys)
    await bot.delete_message(chat_id=event.from_user.id,
                             message_id=data['msg'])
    await Profile.desc_more.set()


async def no(event: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    await upd_d_children(data['pr_id'], "пока не планирую")
    await bot.send_message(chat_id=event.from_user.id,
                           text="Записал!\n"
                                "Какую дополнительную информацию хочешь указать?",
                           reply_markup=profile_inline_keys)
    await bot.delete_message(chat_id=event.from_user.id,
                             message_id=data['msg'])
    await Profile.desc_more.set()


async def clean(event: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    await upd_d_children(data['pr_id'])
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


def register_handlers_prmd_children(dp: Dispatcher):
    dp.register_callback_query_handler(yes, state=Profile.d_m_children, text='yes')
    dp.register_callback_query_handler(plan, state=Profile.d_m_children, text='plan')
    dp.register_callback_query_handler(no, state=Profile.d_m_children, text='no')
    dp.register_callback_query_handler(clean, state=Profile.d_m_children, text='clean')
    dp.register_callback_query_handler(back, state=Profile.d_m_children, text='back')
    dp.register_message_handler(invalid, state=Profile.d_m_children)
