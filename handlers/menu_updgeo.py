from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from keyboards import menu_keys, geo_keys
from FSM import Menu
from dbase import upd_geo
from funcs import do_invalid, get_city, send_menu
from create_bot import bot


async def cancel(event: types.Message, state: FSMContext):
    await send_menu(event, state)


async def valid(event: types.Location, state: FSMContext):
    try:
        geo = {}
        geo['latitude'] = event['location']['latitude']
        geo['longitude'] = event['location']['longitude']
        geo['city'] = await get_city(event['location']['latitude'], event['location']['longitude'])
        await upd_geo(event['from']['id'], geo)
        data = await state.get_data()
        keyss = await menu_keys(data['pr_id'])
        await bot.send_message(event['from']['id'], text="Успешно обновил!\n"
                                                         "Выберите действие:",
                               reply_markup=keyss)
        await Menu.menu.set()
    except:
        await invalid(event)


async def invalid(event: types.Message):
    await do_invalid(event, geo_keys)


def register_handlers_updgeo(dp: Dispatcher):
    dp.register_message_handler(cancel, state=Menu.updgeo, regexp="Назад")
    dp.register_message_handler(valid, state=Menu.updgeo, content_types=types.ContentType.ANY)
    dp.register_message_handler(invalid, state=Menu.updgeo)
