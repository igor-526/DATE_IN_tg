from aiogram import types, Dispatcher
from keyboards import back_keys, yesno_keys, vk_inline_keys
from FSM import ViaVK
from aiogram.dispatcher import FSMContext
from funcs import start_registration, generate_profile_forview
from dbase import chk_vk_reg


async def back(event: types.Message):
    await start_registration(event)


async def valid(event: types.Message, state: FSMContext):
    try:
        prof = await chk_vk_reg(int(event.text))
        vk_id = prof.vk_id
        if not vk_id:
            raise
        await state.update_data(data={'prof_id': int(event.text), 'vk_id': vk_id})
        profmsg = await generate_profile_forview(int(event.text), 0)
        await event.answer(text='Нашёл! Это твой профиль?',
                           reply_markup=yesno_keys)
        if profmsg['m_ph']:
            await event.answer_photo(photo=profmsg['m_ph'], caption=profmsg['msg1'], parse_mode=types.ParseMode.HTML,
                                     reply_markup=vk_inline_keys)
        else:
            await event.answer(text=profmsg['msg1'], parse_mode=types.ParseMode.HTML, reply_markup=vk_inline_keys)
        await ViaVK.confirm.set()
    except:
        await event.answer_photo(caption="К сожеланию, профиль с таким id не найден\n"
                                         "Убедись, что вводишь id профиля DATE IN, а не ВК",
                                 reply_markup=back_keys,
                                 photo='AgACAgIAAxkBAAJPJmSQUDxJ0uU83tjOghw2CZ1eahMHAAJ3zTEbbC-JSPjB9EA8v07yAQADAgADeQADLwQ')


def register_handlers_viavk_id(dp: Dispatcher):
    dp.register_message_handler(back, state=ViaVK.id, regexp="Назад")
    dp.register_message_handler(valid, state=ViaVK.id)
