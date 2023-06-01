from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from create_bot import bot
from FSM import Profile
from keyboards import profile_inline_keys
from dbase import upd_d_height


async def valid(event: types.Message, state: FSMContext):
    try:
        if 120 < int(event.text) < 240:
            data = await state.get_data()
            await upd_d_height(data['pr_id'], int(event.text))
            await event.answer(text="Записал!\n"
                                    "Какую дополнительную информацию хочешь указать?",
                               reply_markup=profile_inline_keys)
            await event.delete()
            await bot.delete_message(chat_id=event.from_user.id,
                                     message_id=data['msg'])
            await Profile.desc_more.set()
        else:
            await event.answer("Я не могу поверить в такой рост")
            await event.delete()
    except ValueError:
        await event.delete()
        await event.answer("Пожалуйста, напиши мне только цифру.\n"
                           "Сколько твой рост в сантиметрах?")


async def clean(event: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    await upd_d_height(data['pr_id'])
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


def register_handlers_prmd_height(dp: Dispatcher):
    dp.register_callback_query_handler(clean, state=Profile.d_m_height, text='clean')
    dp.register_callback_query_handler(back, state=Profile.d_m_height, text='back')
    dp.register_message_handler(valid, state=Profile.d_m_height)
