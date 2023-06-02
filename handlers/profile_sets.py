from aiogram import types, Dispatcher
from keyboards import profile_keys
from FSM import Profile
from aiogram.dispatcher import FSMContext
from dbase import clean_offerlist, get_profile_id
from funcs import (do_invalid,
                   send_menu,
                   f_ch_name,
                   f_ch_bdate,
                   f_ch_sex,
                   f_ch_geo,
                   f_ch_purposes,
                   f_ch_description,
                   f_ch_add_photos,
                   f_ch_del_photos,
                   f_ch_age_f,
                   f_ch_sex_f,
                   f_ch_delete,
                   f_ch_d)


async def back(event: types.Message, state: FSMContext):
    pr_id = await get_profile_id(event.from_user.id)
    await clean_offerlist(pr_id)
    await send_menu(event, state)


async def ch_name(event: types.Message):
    await f_ch_name(event)


async def ch_bdate(event: types.Message):
    await f_ch_bdate(event)


async def ch_sex(event: types.Message):
    await f_ch_sex(event)


async def ch_purposes(event: types.Message):
    await f_ch_purposes(event)


async def ch_geo(event: types.Message):
    await f_ch_geo(event)


async def ch_description(event: types.Message):
    await f_ch_description(event)


async def del_photos(event: types.Message):
    await f_ch_del_photos(event)


async def add_photos(event: types.Message, state: FSMContext):
    await f_ch_add_photos(event, state)


async def ch_age_f(event: types.Message):
    await f_ch_age_f(event)


async def ch_sex_f(event: types.Message):
    await f_ch_sex_f(event)


async def desc_more(event: types.Message):
    await f_ch_d(event)


async def del_profile(event: types.Message):
    await f_ch_delete(event)


async def profile_invalid(event: types.Message):
    await do_invalid(event, profile_keys)


def register_handlers_profile(dp: Dispatcher):
    dp.register_message_handler(back, state=Profile.show, regexp='Назад')
    dp.register_message_handler(ch_name, state=Profile.show, regexp='Имя')
    dp.register_message_handler(ch_bdate, state=Profile.show, regexp='Дата рождения')
    dp.register_message_handler(ch_sex_f, state=Profile.show, regexp='Изменить пол поиска')
    dp.register_message_handler(desc_more, state=Profile.show, regexp='Дополнительно')
    dp.register_message_handler(ch_sex, state=Profile.show, regexp='Пол')
    dp.register_message_handler(ch_purposes, state=Profile.show, regexp='Цели')
    dp.register_message_handler(ch_geo, state=Profile.show, regexp='Геопозиция')
    dp.register_message_handler(ch_description, state=Profile.show, regexp='Описание')
    dp.register_message_handler(del_photos, state=Profile.show, regexp='Удал. фото')
    dp.register_message_handler(add_photos, state=Profile.show, regexp='Доб. фото')
    dp.register_message_handler(ch_age_f, state=Profile.show, regexp='Изменить возраст поиска')
    dp.register_message_handler(del_profile, state=Profile.show, regexp='Удалить профиль')
    dp.register_message_handler(profile_invalid, state=Profile.show)
