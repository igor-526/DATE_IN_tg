from aiogram import types
from aiogram.dispatcher import FSMContext
from dbase import get_search_profile, get_profile_id
from funcs.profile import generate_profile_forview
from funcs.menu import send_menu
from FSM import Search


async def search(event: types.Message, state: FSMContext):
    pr_id = await get_profile_id(event.from_user.id)
    offer = await get_search_profile(pr_id)
    if offer != 'no_profiles':
        print(offer)
        await state.update_data({'id': pr_id, 'offer': offer['id']})
        await Search.searching.set()
        profmsg = await generate_profile_forview(offer['id'], offer['dist'])
        if profmsg['m_ph']:
            await event.answer_photo(photo=profmsg['m_ph'], caption=profmsg['msg1'], parse_mode=types.ParseMode.HTML)
        else:
            await event.answer(text=profmsg['msg1'], parse_mode=types.ParseMode.HTML)
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
    else:
        await event.answer(text="Никого не нашли для тебя\n"
                                "Не расстраивайся, попробуй поменять настройки поиска")
        await send_menu(event)
