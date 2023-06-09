from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from dbase import profile_like, profile_pass, get_photos
from FSM import Search
from funcs import send_menu, search, get_id_from_message, comp_ask_cat, generate_profile_description
from create_bot import bot


async def like_profile(event: types.Message, state: FSMContext):
    await event.delete()
    data = await state.get_data()
    match_status = await profile_like(data['id'], data['offer'])
    if match_status == 'liked':
        await search(event, state)
    elif match_status == 'match':
        await search(event, state)
        await event.answer(text='У тебя новый мэтч!\nПосмотреть контакты можно в меню')
    elif match_status == 'limit':
        await event.answer("Пока что с лайками всё\n"
                           "Я тебе напишу, когда можно будет лайкать дальше")


async def pass_profile(event: types.Message, state: FSMContext):
    await event.delete()
    data = await state.get_data()
    await profile_pass(data['id'], data['offer'])
    await search(event, state)


async def menu(event: types.Message, state: FSMContext):
    await event.delete()
    await send_menu(event, state)


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
    await state.update_data({'compl_to': to_id, 'back_to': 'search'})
    await comp_ask_cat(event.from_user.id)


def register_handlers_search(dp: Dispatcher):
    dp.register_message_handler(like_profile, state=Search.searching, regexp='\U00002764')
    dp.register_message_handler(pass_profile, state=Search.searching, regexp='\U0000274C')
    dp.register_callback_query_handler(all_photos, state="*", text='all_photos')
    dp.register_callback_query_handler(description, state="*", text='description')
    dp.register_callback_query_handler(complaint, state=Search.searching, text='complaint')
    dp.register_message_handler(menu, state=Search.searching, regexp='Меню')
