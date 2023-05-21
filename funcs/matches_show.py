from aiogram import types
from aiogram.dispatcher import FSMContext
from dbase import new_match, old_match
from funcs.profile import generate_profile_forview
from funcs.menu import send_menu
from FSM import Matches
from keyboards import match_inline_keys, nomatch_keys


async def show_new_match(event: types.Message, state: FSMContext):
    async with state.proxy() as data:
        match = await new_match(data['pr_id'])
        if match:
            profmsg = await generate_profile_forview(match)
            keyss = await match_inline_keys(profmsg['contacts'])
            if profmsg['m_ph']:
                await event.answer_photo(photo=profmsg['m_ph'], caption=profmsg['msg1'],
                                         parse_mode=types.ParseMode.HTML,
                                         reply_markup=keyss)
            else:
                await event.answer(text=profmsg['msg1'], parse_mode=types.ParseMode.HTML,
                                   reply_markup=keyss)
        else:
            await event.answer(text='Новых мэтчей пока нет\n'
                                    'Но ты можешь отправиться на поиски за новыми или посмотреть старые!',
                               reply_markup=nomatch_keys)
        await Matches.new_matches.set()


async def show_old_match(event: types.Message, state: FSMContext):
    async with state.proxy() as data:
        match = await old_match(data['pr_id'])
        if match:
            profmsg = await generate_profile_forview(match)
            if profmsg['m_ph']:
                await event.answer_photo(photo=profmsg['m_ph'], caption=profmsg['msg1'],
                                         parse_mode=types.ParseMode.HTML,
                                         reply_markup=match_inline_keys)
            else:
                await event.answer(text=profmsg['msg1'], parse_mode=types.ParseMode.HTML,
                                   reply_markup=match_inline_keys)
            await Matches.old_matches.set()
        else:
            await event.answer(text='Мэтчей пока нет\n'
                                    'Но ты можешь отправиться на поиски за новыми!')
            await send_menu(event)
