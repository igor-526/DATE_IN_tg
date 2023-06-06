from aiogram import types
from aiogram.dispatcher import FSMContext
from dbase import get_search_profile, get_profile_id
from funcs.profile import generate_profile_forview
from funcs.menu import send_menu
from FSM import Search
from keyboards import search_inline_keys


async def search(event: types.Message, state: FSMContext):
    pr_id = await get_profile_id(event.from_user.id)
    offer = await get_search_profile(pr_id)
    if offer != 'no_profiles':
        await state.update_data({'id': pr_id, 'offer': offer['id']})
        await Search.searching.set()
        profmsg = await generate_profile_forview(offer['id'], offer['dist'])
        if profmsg['m_ph']:
            await event.answer_photo(photo=profmsg['m_ph'], caption=profmsg['msg1'], parse_mode=types.ParseMode.HTML,
                                     reply_markup=search_inline_keys)
        else:
            await event.answer(text=profmsg['msg1'], parse_mode=types.ParseMode.HTML, reply_markup=search_inline_keys)
    else:
        await event.answer(text="Никого не нашли для тебя\n"
                                "Не расстраивайся, попробуй поменять настройки поиска")
        await send_menu(event, state)
