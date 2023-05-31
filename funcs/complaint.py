from aiogram import types
from FSM import Complaints
from create_bot import bot
from aiogram.dispatcher import FSMContext
from keyboards import (cancel_keys,
                       complaint_keys,
                       readyback_keys,
                       yesno_keys,
                       search_keys)
from funcs.profile import generate_profile_forview
from funcs.searching import search
from dbase import send_complaint


async def comp_ask_cat(from_id):
    await bot.send_message(chat_id=from_id,
                           text="Вы собираетесь оформить жалобу на профиль",
                           reply_markup=cancel_keys)
    await bot.send_message(chat_id=from_id,
                           text="Выберите категорию жалобы:",
                           reply_markup=complaint_keys)
    await Complaints.category.set()


async def comp_ask_desc(from_id):
    await bot.send_message(chat_id=from_id,
                           text="Опиши, пожалуйста, что произошло. Можно приложить фотографии или отправить их "
                                "отдельным сообщением. После чего нажми 'Готово'",
                           reply_markup=readyback_keys)
    await Complaints.description.set()


async def comp_confirm(event: types.Message, state: FSMContext):
    data = await state.get_data()
    profmsg = await generate_profile_forview(data['compl_to'])
    msg = profmsg['msg1']
    compl_files = len(data['comp_media'])
    compl_desc = data['comp_description']
    msg += f'\n\nЖалоба: {compl_desc}\n+ принято {compl_files} вложения\nОтправить жалобу?'
    if profmsg['m_ph']:
        await event.answer_photo(photo=profmsg['m_ph'], caption=msg, parse_mode=types.ParseMode.HTML,
                                 reply_markup=yesno_keys)
    else:
        await event.answer(text=msg, parse_mode=types.ParseMode.HTML, reply_markup=yesno_keys)
    await Complaints.confirm.set()


async def comp_send(event: types.Message, state: FSMContext):
    data = await state.get_data()
    await send_complaint(pr_id=data['id'],
                         to_id=data['compl_to'],
                         cat=data['comp_cat'],
                         description=data['comp_description'],
                         images=data['comp_media'])
    await event.delete()
    await event.answer(text='Жалоба успешно отправлена',
                       reply_markup=search_keys)
    await state.finish()
    await search(event, state)
