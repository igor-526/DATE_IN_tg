from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from dbase import get_photos
from FSM import Matches
from funcs import send_menu, get_id_from_message, show_new_match
from create_bot import bot


async def next_new(event: types.Message, state: FSMContext):
    await show_new_match(event, state)


async def next_old(event: types.Message, state: FSMContext):
    await show_new_match(event, state)


async def menu(event: types.Message):
    await send_menu(event)


async def all_photos(event: types.CallbackQuery):
    pr_id = await get_id_from_message(event.message.caption)
    photos = await get_photos(pr_id)
    if photos:
        media = types.MediaGroup()
        for photo in photos:
            media.attach_photo(photo=photo)
        await bot.send_media_group(chat_id=event.from_user.id, media=media)
    else:
        await event.answer("У пользователя нет больше фото")


def register_handlers_matches(dp: Dispatcher):
    dp.register_message_handler(next_new, state=Matches.new_matches, regexp='Дальше')
    dp.register_callback_query_handler(all_photos, state=Matches.new_matches, text='all_photos')
    dp.register_message_handler(menu, state=Matches.new_matches, regexp='Меню')
