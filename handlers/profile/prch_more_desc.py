from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from FSM import Profile, Menu
from create_bot import bot
from funcs import generate_profile_forsettings, f_d_height, f_d_habits, f_d_children, f_d_busy, f_d_hobby, f_d_animals
from keyboards import profile_keys, menu_keys


async def ch_height(event: types.CallbackQuery, state: FSMContext):
    await bot.delete_message(chat_id=event.from_user.id,
                             message_id=event.message.message_id)
    await f_d_height(event, state)


async def ch_habits(event: types.CallbackQuery, state: FSMContext):
    await bot.delete_message(chat_id=event.from_user.id,
                             message_id=event.message.message_id)
    await f_d_habits(event, state)


async def ch_children(event: types.CallbackQuery, state: FSMContext):
    await bot.delete_message(chat_id=event.from_user.id,
                             message_id=event.message.message_id)
    await f_d_children(event, state)


async def ch_busy(event: types.CallbackQuery, state: FSMContext):
    await bot.delete_message(chat_id=event.from_user.id,
                             message_id=event.message.message_id)
    await f_d_busy(event, state)


async def ch_hobby(event: types.CallbackQuery, state: FSMContext):
    await bot.delete_message(chat_id=event.from_user.id,
                             message_id=event.message.message_id)
    await f_d_hobby(event, state)


async def ch_animals(event: types.CallbackQuery, state: FSMContext):
    await bot.delete_message(chat_id=event.from_user.id,
                             message_id=event.message.message_id)
    await f_d_animals(event, state)


async def go_menu(event: types.CallbackQuery, state: FSMContext):
    keyss = await menu_keys(event.from_user.id)
    await bot.send_message(chat_id=event.from_user.id,
                           text="Выберите действие:",
                           reply_markup=keyss)
    await state.finish()
    await Menu.menu.set()


async def go_profile(event: types.CallbackQuery):
    profmsg = await generate_profile_forsettings(event.from_user.id)
    msg1 = 'Вот твой профиль:\n\n' + profmsg['msg1']
    if profmsg['att1']:
        await bot.send_photo(chat_id=event.from_user.id,
                             photo=profmsg['att1'],
                             caption=msg1,
                             parse_mode=types.ParseMode.HTML,
                             reply_markup=profile_keys)
    else:
        await bot.send_message(text=msg1,
                               parse_mode=types.ParseMode.HTML,
                               reply_markup=profile_keys)
    if profmsg['att2']:
        media = types.MediaGroup()
        counter = 1
        for photo in profmsg['att2']:
            if counter == 1:
                media.attach_photo(photo=photo, caption=profmsg['msg2'])
                counter += 1
            else:
                media.attach_photo(photo=photo)
        await bot.send_media_group(chat_id=event.from_user.id,
                                   media=media)
    else:
        if profmsg['msg2']:
            await bot.send_message(text=profmsg['msg2'],
                                   reply_markup=profile_keys)
    await Profile.show.set()


async def invalid(event: types.Message):
    await event.delete()
    await event.answer(text="Я вас не понимаю &#128532;\n"
                            "Пожалуйста, выберите действие на клавиатуре",
                       parse_mode=types.ParseMode.HTML)


def register_handlers_prch_more_desc(dp: Dispatcher):
    dp.register_callback_query_handler(ch_height, state=Profile.desc_more, text='height')
    dp.register_callback_query_handler(ch_hobby, state=Profile.desc_more, text='hobby')
    dp.register_callback_query_handler(ch_busy, state=Profile.desc_more, text='busy')
    dp.register_callback_query_handler(ch_children, state=Profile.desc_more, text='children')
    dp.register_callback_query_handler(ch_animals, state=Profile.desc_more, text='animals')
    dp.register_callback_query_handler(ch_habits, state=Profile.desc_more, text='habit')
    dp.register_callback_query_handler(go_menu, state=Profile.desc_more, text='menu')
    dp.register_callback_query_handler(go_profile, state=Profile.desc_more, text='profile')
    dp.register_message_handler(invalid, state=Profile.desc_more)
