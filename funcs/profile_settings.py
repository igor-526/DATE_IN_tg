from aiogram import types
from FSM import Profile
from aiogram.dispatcher import FSMContext
from create_bot import bot
from keyboards import (profile_keys,
                       cancel_keys,
                       sex_keys,
                       geo_keys,
                       yesno_keys,
                       sex_f_keys,
                       readyback_keys,
                       profile_inline_keys,
                       backin_keys,
                       children_keys,
                       busy_keys)
from funcs.purposes import gen_purposes
from dbase import dates_info, upd_c_photos
from funcs.profile import generate_profile_forsettings


async def do_invalid(event: types.Message, keys):
    await event.delete()
    await event.answer(text="Я вас не понимаю &#128532;\n"
                            "Пожалуйста, выберите действие на клавиатуре",
                       reply_markup=keys,
                       parse_mode=types.ParseMode.HTML)


async def show_myprofile(event: types.Message):
    profmsg = await generate_profile_forsettings(event.from_user.id)
    msg1 = 'Вот твой профиль:\n\n' + profmsg['msg1']
    if profmsg['att1']:
        await event.answer_photo(photo=profmsg['att1'], caption=msg1, parse_mode=types.ParseMode.HTML,
                                 reply_markup=profile_keys)
    else:
        await event.answer(text=msg1, parse_mode=types.ParseMode.HTML, reply_markup=profile_keys)
    if profmsg['att2']:
        media = types.MediaGroup()
        counter = 1
        for photo in profmsg['att2']:
            if counter == 1:
                media.attach_photo(photo=photo, caption=profmsg['msg2'])
                counter += 1
            else:
                media.attach_photo(photo=photo)
        await event.answer_media_group(media=media)
    else:
        if profmsg['msg2']:
            await event.answer(profmsg['msg2'], reply_markup=profile_keys)
    await Profile.show.set()


async def f_ch_name(event: types.Message, state: FSMContext):
    await event.delete()
    data = await state.get_data()
    ch_date = await dates_info(data['pr_id'])
    if not ch_date['name']:
        await event.answer(text='Введи имя, на которое хочешь поменять\n'
                                'Но учти, что делать это можно только один раз!',
                           reply_markup=cancel_keys)
        await Profile.name.set()
    else:
        await event.answer(text=f'Вы уже меняли имя {ch_date["name"].strftime("%d.%m")}\n'
                                f'Если есть необходимость всё-таки его поменять, обратитесь через /report')


async def f_ch_bdate(event: types.Message, state: FSMContext):
    await event.delete()
    data = await state.get_data()
    ch_date = await dates_info(data['pr_id'])
    if not ch_date['bdate']:
        await event.answer(text='Введи свою дату рождения в формате ДД.ММ.ГГГГ\n'
                                'Но учти, что делать это можно только один раз!',
                           reply_markup=cancel_keys)
        await Profile.bdate.set()
    else:
        await event.answer(text=f'Вы уже меняли дату рождения {ch_date["name"].strftime("%d.%m")}\n'
                                f'Если есть необходимость всё-таки её поменять, обратитесь через /report')


async def f_ch_sex(event: types.Message, state: FSMContext):
    await event.delete()
    data = await state.get_data()
    ch_date = await dates_info(data['pr_id'])
    if not ch_date['sex']:
        await event.answer(text='Кто ты?\n'
                                'Но учти, что делать это можно только один раз!',
                           reply_markup=sex_keys)
        await Profile.sex.set()
    else:
        await event.answer(text=f'Вы уже меняли пол {ch_date["sex"].strftime("%d.%m")}\n'
                                f'Если есть необходимость всё-таки поменять пол, обратитесь через /report')


async def f_ch_purposes(event: types.Message):
    await event.delete()
    msg = 'Пожалуйста, перечислите через запятую или пробел номера целей\n' \
          'Менять их можно сколько угодно раз!\n\n'
    msg += await gen_purposes()
    await event.answer(text=msg, reply_markup=cancel_keys, parse_mode=types.ParseMode.HTML)
    await Profile.purposes.set()


async def f_ch_geo(event: types.Message):
    await event.delete()
    await event.answer(text="Отправьте мне своё местоположение, чтобы я смог подбирать профили сначала поближе!\n"
                            "Можно отправить гео через вложения, если хочется отправить приерное местоположение",
                       reply_markup=geo_keys)
    await Profile.geo.set()


async def f_ch_description(event: types.Message):
    await event.delete()
    await event.answer(text="Напиши мне самое лучшее описание профиля на свете!",
                       reply_markup=cancel_keys)
    await Profile.description.set()


async def f_ch_del_photos(event: types.Message):
    await event.delete()
    await event.answer(text="Функция удалит все твои фотографии профиля, но ты потом сможешь добавить их снова!\n"
                            "Уверены?",
                       reply_markup=yesno_keys)
    await Profile.del_photos.set()


async def f_ch_add_photos(event: types.Message, state: FSMContext):
    await event.delete()
    count = await upd_c_photos(event.from_user.id)
    if count == 11:
        await event.answer(text='У тебя уже 11 фотографий!\n'
                                'К сожалению, больше нельзя. Для начала нужно удалить фотографии')
    else:
        await event.answer(text=f'Отправь мне свои самые лучшие фотографии!\n'
                                f'(Макс. {11-count}. остальные не смогу добавить :( )',
                           reply_markup=readyback_keys)
        await Profile.add_photos.set()
        await state.set_data({'photos': []})


async def f_ch_age_f(event: types.Message):
    await event.delete()
    await event.answer(text="Введите минимальный возраст для поиска:",
                       reply_markup=cancel_keys)
    await Profile.age_min.set()


async def f_ch_sex_f(event: types.Message):
    await event.delete()
    await event.answer(text="Кого будем искать?",
                       reply_markup=sex_f_keys)
    await Profile.sex_f.set()


async def f_ch_delete(event: types.Message):
    await event.delete()
    await event.answer(text="В течение недели ты сможешь восстановить профиль, после чего он будет окончательно "
                            "удалён. Продолжить?",
                       reply_markup=yesno_keys)
    await Profile.delete.set()


async def f_ch_d(event: types.Message):
    await event.delete()
    await event.answer(text='Чем больше информации - тем лучше!',
                       reply_markup=types.ReplyKeyboardRemove())
    await event.answer(text="Какую дополнительную информацию хочешь указать?",
                       reply_markup=profile_inline_keys)
    await Profile.desc_more.set()


async def f_d_height(event: types.CallbackQuery, state: FSMContext):
    msg = await bot.send_message(chat_id=event.from_user.id,
                                 text="Напиши мне свой рост:",
                                 reply_markup=backin_keys)
    await state.update_data({'msg': msg.message_id})
    await Profile.d_m_height.set()


async def f_d_habits(event: types.CallbackQuery, state: FSMContext):
    msg = await bot.send_message(chat_id=event.from_user.id,
                                 text="Расскажи мне о своих вредных привычках (100 символов):",
                                 reply_markup=backin_keys)
    await state.update_data({'msg': msg.message_id})
    await Profile.d_m_habits.set()


async def f_d_children(event: types.CallbackQuery, state: FSMContext):
    msg = await bot.send_message(chat_id=event.from_user.id,
                                 text="Что у тебя по детям?",
                                 reply_markup=children_keys)
    await state.update_data({'msg': msg.message_id})
    await Profile.d_m_children.set()


async def f_d_busy(event: types.CallbackQuery, state: FSMContext):
    msg = await bot.send_message(chat_id=event.from_user.id,
                                 text="Выбери соответствующий вариант:",
                                 reply_markup=busy_keys)
    await state.update_data({'msg': msg.message_id})
    await Profile.d_m_busy.set()


async def f_d_hobby(event: types.CallbackQuery, state: FSMContext):
    msg = await bot.send_message(chat_id=event.from_user.id,
                                 text="Напиши мне в кратце о своих хобби (200 символов):",
                                 reply_markup=backin_keys)
    await state.update_data({'msg': msg.message_id})
    await Profile.d_m_hobby.set()


async def f_d_animals(event: types.CallbackQuery, state: FSMContext):
    msg = await bot.send_message(chat_id=event.from_user.id,
                                 text="У тебя есть домашние животные?\n"
                                      "Может, планируешь завести?\n"
                                      "Или негативно к ним относишься?\n"
                                      "(150 символов)",
                                 reply_markup=backin_keys)
    await state.update_data({'msg': msg.message_id})
    await Profile.d_m_animals.set()
