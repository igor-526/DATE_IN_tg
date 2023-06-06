from aiogram import types, Dispatcher
from keyboards import filter_keys, cancel_keys
from FSM import Profile
from aiogram.dispatcher import FSMContext
from dbase import upd_age_f
from validators import valid_age
from funcs import show_myprofile


async def cancel(event: types.Message):
    await event.answer(text="Выбери фильтр:",
                       reply_markup=filter_keys)
    await Profile.filters.set()


async def valid_age_min(event: types.Message, state: FSMContext):
    validator = await valid_age(event.text, None)
    if validator == 'valid':
        await state.set_data({'age_min': int(event.text)})
        await event.answer(text='Отличный выбор! А теперь введи максимальный возраст для поиска!',
                           reply_markup=cancel_keys)
        await Profile.age_max.set()
    elif validator == 'invalid':
        await event.answer(text='Я так не понимаю\n'
                                'Просто напиши циферку',
                           reply_markup=cancel_keys)
    elif validator == 'too_small':
        await event.answer(text='У нас ограничение с 14 лет\n'
                                'Попробуй ввести постарше',
                           reply_markup=cancel_keys)
    elif validator == 'too_old':
        await event.answer(text='Ну тут уже проще будет на кладбище поискать\n'
                                'Попробуй ввести помладше',
                           reply_markup=cancel_keys)


async def valid_age_max(event: types.Message, state: FSMContext):
    async with state.proxy() as data:
        validator = await valid_age(event.text, data['age_min'])
        if validator == 'valid':
            await upd_age_f(event.from_user.id, data['age_min'], int(event.text))
            await event.answer(text="Настройки поиска обновлены!")
            await show_myprofile(event, state)
        elif validator == 'invalid':
            await event.answer(text='Я так не понимаю\n'
                                    'Просто напиши циферку',
                               reply_markup=cancel_keys)
        elif validator == 'more_min':
            await event.answer(text='Максимальный возраст для поиска не может быть меньше минимального\n'
                                    'Попробуй ввести постарше',
                               reply_markup=cancel_keys)
        elif validator == 'too_old':
            await event.answer(text='Ну тут уже проще будет на кладбище поискать\n'
                                    'Попробуй ввести помладше',
                               reply_markup=cancel_keys)


def register_handlers_prch_age_f(dp: Dispatcher):
    dp.register_message_handler(cancel, state=Profile.age_min, regexp="Отмена")
    dp.register_message_handler(cancel, state=Profile.age_max, regexp="Отмена")
    dp.register_message_handler(valid_age_min, state=Profile.age_min)
    dp.register_message_handler(valid_age_max, state=Profile.age_max)
