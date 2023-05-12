from aiogram import types
from aiogram.dispatcher import FSMContext
from FSM import Menu, Profile
from keyboards import (profile_keys)
from funcs.purposes import gen_purposes
from dbase import add_profile, add_settings, add_profile_photos
from datetime import date
from funcs.profile import generate_profile_forsettings
from funcs.menu import send_menu
from pprint import pprint


async def do_invalid(event: types.Message, keys):
    await event.answer(text="Я вас не понимаю &#128532;\n"
                            "Пожалуйста, выберите действие на клавиатуре",
                       reply_markup=keys,
                       parse_mode=types.ParseMode.HTML)


async def show_myprofile(event: types.Message):
    profmsg = await generate_profile_forsettings(event.from_user.id)
    msg1 = 'Вот твой профиль:\n\n' + profmsg['msg1']
    if profmsg['att1']:
        await event.answer_photo(photo=profmsg['att1'], caption=msg1, parse_mode=types.ParseMode.HTML,
                                 reply_markup=profile_keys)
    else:
        await event.answer(text=msg1, parse_mode=types.ParseMode.HTML, reply_markup=profile_keys)
    if profmsg['att2']:
        media = types.MediaGroup()
        counter = 1
        for photo in profmsg['att2']:
            if counter == 1:
                media.attach_photo(photo=photo, caption=profmsg['msg2'])
                counter += 1
            else:
                media.attach_photo(photo=photo)
        await event.answer_media_group(media=media)
    else:
        if profmsg['msg2']:
            await event.answer(profmsg['msg2'], reply_markup=profile_keys)
