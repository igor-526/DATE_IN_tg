from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from FSM import Reg
from funcs import reg_ask_sex
from keyboards import geo_keys


async def back(event: types.Message):
    await reg_ask_sex(event)


async def valid(event: types.Location, state: FSMContext):
    async with state.proxy() as data:
        data['latitude'] = event['location']['latitude']
        data['longitude'] = event['location']['longitude']
        print(data)


async def invalid(event: types.Message):
    await event.answer(text='Я не знаю, что делать с этим сообщением &#128532;\n'
                            'Пожалуйста, отправь мне геопозицию (можно примерную)',
                       reply_markup=geo_keys,
                       parse_mode=types.ParseMode.HTML)


def register_handlers_reg_geo(dp: Dispatcher):
    dp.register_message_handler(back, state=Reg.geo, regexp="Назад")
    dp.register_message_handler(valid, state=Reg.geo, content_types=types.ContentType.LOCATION)
    dp.register_message_handler(invalid, state=Reg.geo)
