from aiogram import types
from aiogram.dispatcher import FSMContext
from FSM import Reg, Profile
from keyboards import (reg_profile_keys,
                       yesnoback_keys,
                       sex_keys,
                       back_keys,
                       geo_keys,
                       backskip_keys,
                       readyback_keys,
                       sex_f_keys,
                       profilereg_inline_keys)
from funcs.purposes import gen_purposes
from dbase import add_profile, add_settings, add_profile_photos
from datetime import date
import requests
import config
from threading import Thread


async def do_invalid(event: types.Message, keys):
    await event.answer(text="Я вас не понимаю &#128532;\n"
                            "Пожалуйста, выберите действие на клавиатуре",
                       reply_markup=keys,
                       parse_mode=types.ParseMode.HTML)


async def start_registration(event: types.Message):
    await event.answer(text="Подскажите, у Вас уже есть профиль на сайте или в ВК?",
                       reply_markup=reg_profile_keys)
    await Reg.profile.set()


async def reg_ask_name(event: types.Message):
    await event.answer(text=f"Тогда начнём &#128521;\n"
                            f"Тебя зовут {event.from_user.first_name}?",
                       reply_markup=yesnoback_keys,
                       parse_mode=types.ParseMode.HTML)
    await Reg.name_auto.set()


async def reg_ask_name_manual(event: types.Message):
    await event.answer(text=f'Как же тогда тебя зовут? &#128527;\n'
                            f'Учти, что имя после регистрации можно будет поменять только 1 раз!',
                       reply_markup=types.ReplyKeyboardRemove(),
                       parse_mode=types.ParseMode.HTML)
    await Reg.name_manual.set()


async def reg_ask_bdate(event: types.Message):
    await event.answer(text="Записал &#128521;\n"
                            "Мне нужна твоя дата рождения. Напиши мне её, пожалуйста, в формате ДД.ММ.ГГГГ",
                       reply_markup=back_keys,
                       parse_mode=types.ParseMode.HTML)
    await Reg.bdate.set()


async def reg_ask_sex(event: types.Message):
    await event.answer(text="Супер!\n"
                            "Теперь нужно определиться, кто же ты?&#128104;&#128105;",
                       reply_markup=sex_keys,
                       parse_mode=types.ParseMode.HTML)
    await Reg.sex.set()


async def reg_ask_geo(event: types.Message):
    await event.answer(text='Мне нужно знать твоё местоположение (можно примерное)\n'
                            'Это необходимо для того, чтобы подбирать тебе анкеты поближе',
                       reply_markup=geo_keys)
    await Reg.geo.set()


async def reg_ask_photos(event: types, state: FSMContext):
    async with state.proxy() as data:
        data['photos'] = []
    await event.answer(text='Супер! Отправь мне фотографии (Не более 11), которые '
                            'будешь гордо демонстрировать другим пользователям сервиса, после чего нажми "Готово"\n'
                            'Если хочется пользоваться без фотографий (что мы очень не рекомендуем) или '
                            'отправить их потом, нажми кнопку "Готово"',
                       reply_markup=readyback_keys)
    await Reg.photo.set()


async def reg_ask_description(event: types.Message):
    await event.answer(text="Готово! Почти последний шаг - напиши мне какой-нибудь текст, который заинтересует любого "
                            "и заставит нажать кнопку лайка!\n"
                            "Если хочется придумать позже, или вообще не добавлять (что мы так же не рекомендуем!),"
                            " просто нажми кнопку 'Пропустить'",
                       reply_markup=backskip_keys)
    await Reg.description.set()


async def reg_ask_purposes(event: types.Message):
    msg = 'Последний шаг - определиться с целями!\nПожалуйста, через запятую или пробел ' \
          'перечислите номера целей\n\n'
    msg += await gen_purposes()
    await event.answer(text=msg,
                       reply_markup=back_keys,
                       parse_mode=types.ParseMode.HTML)
    await Reg.purposes.set()


async def reg_ask_f_sex(event: types.Message):
    await event.answer(text='С твоим профилем всё!\nОсталось определиться с настройками поиска\n'
                            'Тут гораздо меньше. Детальнее потом можно будет настроить в меню')
    await event.answer(text='Кого мы будем искать?',
                       reply_markup=sex_f_keys)
    await Reg.f_sex.set()


async def reg_ask_age_min(event: types.Message):
    await event.answer(text='С этим определились!\n'
                            'Осталось понять, какой будет минимальный возраст для поиска',
                       reply_markup=back_keys)
    await Reg.f_age_min.set()


async def reg_ask_age_max(event: types.Message):
    await event.answer(text='Прекрасный выбор!\n'
                            'А максимальный?',
                       reply_markup=back_keys)
    await Reg.f_age_max.set()


def upload_to_vk(pr_id):
    requrl = f'{config.api_url}/vkphoto/'
    params = {"id": pr_id,
              "auth_token": config.api_token}
    resp = requests.post(url=requrl, json=params, verify=False)
    print(resp.text)


async def reg_finish(event: types.Message, state: FSMContext):
    await event.answer("Завершение регистрации..")
    try:
        async with state.proxy() as data:
            datelist = data['bdate'].split('.')
            pr_id = await add_profile(tg_id=event.from_user.id,
                                      tg_url=event.from_user.url,
                                      tg_nick=event.from_user.username,
                                      name=data['name'],
                                      bdate=date(year=int(datelist[2]), month=int(datelist[1]), day=int(datelist[0])),
                                      sex=data['sex'],
                                      city=data['city'],
                                      geo_lat=data['latitude'],
                                      geo_long=data['longitude'],
                                      description=data['description'])
            find_f = 1 if 1 in data['sex_f'] else 0
            find_m = 1 if 2 in data['sex_f'] else 0
            purp1 = 1 if 1 in data['purposes'] else 0
            purp2 = 1 if 2 in data['purposes'] else 0
            purp3 = 1 if 3 in data['purposes'] else 0
            purp4 = 1 if 4 in data['purposes'] else 0
            purp5 = 1 if 5 in data['purposes'] else 0
            await add_settings(tg_id=event.from_user.id,
                               age_min=data['age_min'],
                               age_max=data['age_max'],
                               find_f=find_f,
                               find_m=find_m,
                               purp1=purp1,
                               purp2=purp2,
                               purp3=purp3,
                               purp4=purp4,
                               purp5=purp5
                               )
        await add_profile_photos(event.from_user.id, data['photos'])

        upl = Thread(target=upload_to_vk, args=(pr_id, ), daemon=True)
        upl.start()
        upl.join(0.0)
        await event.answer(text="Ура! Всё получилось!\n"
                                "Ты так же можешь добавить следующие данные о себе:",
                           reply_markup=profilereg_inline_keys)
        await state.update_data({'pr_id': pr_id})
        await Profile.desc_more.set()
    except Exception as exx:
        await event.answer("Что-то пошло не так\n"
                           "Пожалуйста, попробуйте позже")
        await state.finish()
        print(exx)
