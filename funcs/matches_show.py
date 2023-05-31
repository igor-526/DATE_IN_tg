from aiogram import types
from aiogram.dispatcher import FSMContext
from dbase import new_match, old_match
from funcs.profile import generate_profile_forview
from FSM import Matches
from keyboards import match_inline_keys, nomatch_keys, oldmatch_keys


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


async def next_old_match(event: types.Message, state: FSMContext):
    try:
        async with state.proxy() as data:
            data['old_matches']['cursor'] += 1
            cursor = data['old_matches']['cursor']
            profmsg = await generate_profile_forview(data['old_matches']['matches'][cursor])
            keyss = await match_inline_keys(profmsg['contacts'])
            if profmsg['m_ph']:
                await event.answer_photo(photo=profmsg['m_ph'], caption=profmsg['msg1'],
                                         parse_mode=types.ParseMode.HTML,
                                         reply_markup=keyss)
            else:
                await event.answer(text=profmsg['msg1'], parse_mode=types.ParseMode.HTML,
                                   reply_markup=keyss)
    except IndexError:
        await event.answer(text='Больше нет\n'
                                'Давайте лучше отправимся за поиском новых пар!')


async def prev_old_match(event: types.Message, state: FSMContext):
    try:
        async with state.proxy() as data:
            data['old_matches']['cursor'] -= 1
            cursor = data['old_matches']['cursor']
            profmsg = await generate_profile_forview(data['old_matches']['matches'][cursor])
            keyss = await match_inline_keys(profmsg['contacts'])
            if profmsg['m_ph']:
                await event.answer_photo(photo=profmsg['m_ph'], caption=profmsg['msg1'],
                                         parse_mode=types.ParseMode.HTML,
                                         reply_markup=keyss)
            else:
                await event.answer(text=profmsg['msg1'], parse_mode=types.ParseMode.HTML,
                                   reply_markup=keyss)
    except IndexError:
        await event.answer(text='Больше нет\n'
                                'Давайте лучше отправимся за поиском новых пар!')


async def show_old_match(event: types.Message, state: FSMContext):
    async with state.proxy() as data:
        matches = await old_match(data['pr_id'])
        if len(matches) == 0:
            await event.answer(text='У вас пока нет ни одной пары. Отправляйтесь скорее за новыми!')
        else:
            await state.update_data({'old_matches': {'matches': matches, 'cursor': -1}})
            await event.answer(text='Секунду..',
                               reply_markup=oldmatch_keys)
            await Matches.old_matches.set()
            await next_old_match(event, state)
