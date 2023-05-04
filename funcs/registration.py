from aiogram import types
from FSM import Reg
from keyboards import reg_profile_keys, yesnoback_keys, sex_keys, back_keys, geo_keys


async def do_invalid(event: types.Message, keys):
    await event.answer(text="Я вас не понимаю &#128532;\n"
                            "Пожалуйста, выберите действие на клавиатуре",
                       reply_markup=keys,
                       parse_mode=types.ParseMode.HTML)


async def start_registration(event: types.Message):
    await event.answer(text="Подскажите, у Вас уже есть профиль на сайте или в TG?",
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
