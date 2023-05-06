from aiogram import types, Dispatcher
from keyboards import back_keys, yesno_keys
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
        msg1 = 'Нашёл! Это твой профиль?\n\n' + profmsg['msg1']
        if profmsg['m_ph']:
            await event.answer_photo(photo=profmsg['m_ph'], caption=msg1, parse_mode=types.ParseMode.HTML,
                                     reply_markup=yesno_keys)
        else:
            await event.answer(text=msg1, parse_mode=types.ParseMode.HTML, reply_markup=yesno_keys)
        if profmsg['o_ph']:
            media = types.MediaGroup()
            counter = 1
            for photo in profmsg['o_ph']:
                if counter == 1:
                    media.attach_photo(photo=photo, caption=profmsg['msg2'])
                    counter += 1
                else:
                    media.attach_photo(photo=photo)
            await event.answer_media_group(media=media)
        else:
            if profmsg['msg2']:
                await event.answer(profmsg['msg2'])
        await ViaVK.confirm.set()
    except:
        await event.answer(text="К сожеланию, профиль с таким id не найден\n"
                                "Убедитесь, что вы вводите id профиля DATE IN, а не ВК",
                           reply_markup=back_keys)


def register_handlers_viavk_id(dp: Dispatcher):
    dp.register_message_handler(back, state=ViaVK.id, regexp="Назад")
    dp.register_message_handler(valid, state=ViaVK.id)
