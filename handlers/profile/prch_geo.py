from aiogram import types, Dispatcher
from keyboards import profile_keys, geo_keys
from FSM import Profile
from dbase import upd_geo
from funcs import do_invalid, get_city
from create_bot import bot


async def cancel(event: types.Message):
    await event.answer(text="Выберите действие:",
                       reply_markup=profile_keys)
    await Profile.show.set()


async def valid(event: types.Location):
    geo = {}
    geo['latitude'] = event['location']['latitude']
    geo['longitude'] = event['location']['longitude']
    geo['city'] = await get_city(event['location']['latitude'], event['location']['longitude'])
    await upd_geo(event['from']['id'], geo)
    await bot.send_message(event['from']['id'], text="Успешно обновил!\n"
                                                     "Выберите действие:",
                           reply_markup=profile_keys)
    await Profile.show.set()


async def invalid(event: types.Message):
    await do_invalid(event, geo_keys)


def register_handlers_prch_geo(dp: Dispatcher):
    dp.register_message_handler(cancel, state=Profile.geo, regexp="Назад")
    dp.register_message_handler(valid, state=Profile.geo, content_types=types.ContentType.LOCATION)
    dp.register_message_handler(invalid, state=Profile.geo)
