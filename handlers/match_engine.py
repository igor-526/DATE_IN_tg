from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from dbase import get_photos
from FSM import Matches, Search
from funcs import (send_menu,
                   get_id_from_message,
                   show_new_match,
                   show_old_match,
                   next_old_match,
                   search,
                   prev_old_match,
                   comp_ask_cat,
                   generate_profile_description)
from keyboards import search_keys
from create_bot import bot


async def next_new(event: types.Message, state: FSMContext):
    await event.delete()
    await show_new_match(event, state)


async def show_old(event: types.Message, state: FSMContext):
    await event.delete()
    await show_old_match(event, state)


async def next_old(event: types.Message, state: FSMContext):
    await event.delete()
    await next_old_match(event, state)


async def prev_old(event: types.Message, state: FSMContext):
    await event.delete()
    await prev_old_match(event, state)


async def menu(event: types.Message, state: FSMContext):
    await event.delete()
    await send_menu(event, state)


async def searching(event: types.Message, state: FSMContext):
    await Search.searching.set()
    await event.answer(text="Уже ищу..", reply_markup=search_keys)
    await search(event, state)


async def all_photos(event: types.CallbackQuery):
    texttoid = event.message.caption if event.message.caption else event.message.text
    pr_id = await get_id_from_message(texttoid)
    photos = await get_photos(pr_id)
    if photos:
        media = types.MediaGroup()
        for photo in photos:
            media.attach_photo(photo=photo)
        await bot.send_media_group(chat_id=event.from_user.id, media=media)
    else:
        await event.answer("У пользователя нет больше фото")


async def description(event: types.CallbackQuery):
    texttoid = event.message.caption if event.message.caption else event.message.text
    pr_id = await get_id_from_message(texttoid)
    desc = await generate_profile_description(pr_id)
    await bot.send_message(chat_id=event.from_user.id,
                           text=desc,
                           parse_mode=types.ParseMode.HTML)


async def complaint(event: types.CallbackQuery, state: FSMContext):
    texttoid = event.message.caption if event.message.caption else event.message.text
    to_id = await get_id_from_message(texttoid)
    await state.update_data({'compl_to': to_id, 'back_to': 'matches'})
    await comp_ask_cat(event.from_user.id)


def register_handlers_matches(dp: Dispatcher):
    dp.register_message_handler(next_new, state=Matches.new_matches, regexp='\U000025B6')
    dp.register_message_handler(show_old, state=Matches.new_matches, regexp='Просмотренные')
    dp.register_callback_query_handler(complaint, state=Matches.new_matches, text='complaint')
    dp.register_callback_query_handler(complaint, state=Matches.old_matches, text='complaint')
    dp.register_message_handler(menu, state=Matches.new_matches, regexp='Меню')
    dp.register_message_handler(menu, state=Matches.old_matches, regexp='Меню')
    dp.register_message_handler(searching, state=Matches.new_matches, regexp='Начать поиск')
    dp.register_message_handler(searching, state=Matches.new_matches, regexp='Начать поиск')
    dp.register_message_handler(next_old, state=Matches.old_matches, regexp="\U000025B6")
    dp.register_message_handler(prev_old, state=Matches.old_matches, regexp="\U000025C0")
