from aiogram import types, Dispatcher
from create_bot import bot
from keyboards import search_keys
from FSM import Complaints, Search
from aiogram.dispatcher import FSMContext
from funcs import comp_confirm


async def cancel(event: types.Message):
    await event.delete()
    await Search.searching.set()
    await bot.send_message(chat_id=event.from_user.id,
                           text="Жалоба отменена",
                           reply_markup=search_keys)


async def get_photos(event: types.PhotoSize, state: FSMContext):
    async with state.proxy() as data:
        if event['photo']:
            file_id = event['photo'][-1]['file_id']
            data['comp_media'].append(file_id)
            if event['caption']:
                data['comp_description'] += f"{event['caption']}\n"
        if event['document']:
            file_id = event['document']["thumbnail"]["file_id"]
            data['comp_media'].append(file_id)
            if event['caption']:
                data['comp_description'] += f"{event['caption']}\n"


async def get_text(event: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comp_description'] += f"{event.text}\n"


async def ready(event: types.Message, state: FSMContext):
    await comp_confirm(event, state)


def register_handlers_comp_description(dp: Dispatcher):
    dp.register_message_handler(cancel, state=Complaints.description, regexp="Назад")
    dp.register_message_handler(ready, state=Complaints.description, regexp="Готово!")
    dp.register_message_handler(get_photos, state=Complaints.description, content_types=types.ContentType.PHOTO)
    dp.register_message_handler(get_photos, state=Complaints.description, content_types=types.ContentType.DOCUMENT)
    dp.register_message_handler(get_text, state=Complaints.description)
