from aiogram import types, Dispatcher
from keyboards import profile_keys, yesno_keys, readyback_keys
from FSM import Profile
from dbase import upd_del_photos, upd_add_photos, upd_c_photos, get_profile_id
from funcs import show_myprofile, do_invalid, upload_to_vk
from aiogram.dispatcher import FSMContext
from threading import Thread


async def no(event: types.Message):
    await event.answer(text="Выберите действие:",
                       reply_markup=profile_keys)
    await Profile.show.set()


async def yes(event: types.Message):
    await upd_del_photos(event.from_user.id)
    await event.answer(text="Удалил. Теперь ты можешь добавить 11 фотографий для профиля!")
    await show_myprofile(event)


async def get_photos(event: types.PhotoSize, state: FSMContext):
    file_id = event['photo'][-1]['file_id']
    async with state.proxy() as data:
        if len(data['photos']) < 11:
            data['photos'].append(file_id)


async def ready(event: types.Message, state: FSMContext):
    count = await upd_c_photos(event.from_user.id)
    pr_id = await get_profile_id(event.from_user.id)
    max_count = 11 - count
    async with state.proxy() as data:
        await upd_add_photos(event.from_user.id, data['photos'][:max_count])
    upl = Thread(target=upload_to_vk, args=(pr_id,), daemon=True)
    upl.start()
    upl.join(0.0)
    await event.answer(text='Прекрасные фотографии! Добавил!')
    await show_myprofile(event)


async def invalid_del(event: types.Message):
    await do_invalid(event, yesno_keys)


async def invalid_add(event: types.Message):
    await event.answer(text="К сожалению, я не знаю, что мне сделать с этим сообщением :(\n"
                            "Пожалуйста, отправь мне свои фотографии, после чего нажми 'Готово!'",
                       reply_markup=readyback_keys)


def register_handlers_prch_photos(dp: Dispatcher):
    dp.register_message_handler(no, state=Profile.del_photos, regexp="Нет")
    dp.register_message_handler(no, state=Profile.add_photos, regexp="Назад")
    dp.register_message_handler(yes, state=Profile.del_photos, regexp="Да")
    dp.register_message_handler(get_photos, state=Profile.add_photos, content_types=types.ContentType.PHOTO)
    dp.register_message_handler(ready, state=Profile.add_photos, regexp="Готово!")
    dp.register_message_handler(invalid_del, state=Profile.del_photos)
    dp.register_message_handler(invalid_add, state=Profile.add_photos)
