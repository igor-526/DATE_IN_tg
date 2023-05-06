from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from FSM import Reg
from funcs import reg_ask_geo, reg_ask_description
from keyboards import readyback_keys


async def back(event: types.Message):
    await reg_ask_geo(event)


async def ready(event: types.Message):
    await reg_ask_description(event)


async def get_photos(event: types.PhotoSize, state: FSMContext):
    file_id = event['photo'][-1]['file_id']
    async with state.proxy() as data:
        if len(data['photos']) < 11:
            data['photos'].append(file_id)


async def invalid(event: types.Message):
    await event.answer(text='Я не знаю, что делать с этим сообщением &#128532;\n'
                            'Пожалуйста, отправь мне свои фотографии',
                       reply_markup=readyback_keys,
                       parse_mode=types.ParseMode.HTML)


def register_handlers_reg_photo(dp: Dispatcher):
    dp.register_message_handler(ready, state=Reg.photo, regexp="Готово!")
    dp.register_message_handler(back, state=Reg.photo, regexp="Пропустить")
    dp.register_message_handler(get_photos, state=Reg.photo, content_types=types.ContentType.PHOTO)
    dp.register_message_handler(invalid, state=Reg.photo)
