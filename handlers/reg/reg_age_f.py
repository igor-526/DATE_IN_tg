from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from FSM import Reg
from funcs import reg_ask_f_sex, reg_ask_age_min, reg_ask_age_max, reg_finish
from validators import valid_age
from keyboards import back_keys


async def back_to_sex(event: types.Message):
    await reg_ask_f_sex(event)


async def back_to_age_min(event: types.Message):
    await reg_ask_age_min(event)


async def valid_age_min(event: types.Message, state: FSMContext):
    validator = await valid_age(event.text, None)
    if validator == 'valid':
        await state.update_data(data={'age_min': int(event.text)})
        await reg_ask_age_max(event)
    elif validator == 'invalid':
        await event.answer(text='Я так не понимаю\n'
                                'Просто напиши циферку',
                           reply_markup=back_keys)
    elif validator == 'too_small':
        await event.answer(text='У нас ограничение с 14 лет\n'
                                'Попробуй ввести постарше',
                           reply_markup=back_keys)
    elif validator == 'too_old':
        await event.answer(text='Ну тут уже проще будет на кладбище поискать\n'
                                'Попробуй ввести помладше',
                           reply_markup=back_keys)


async def valid_age_max(event: types.Message, state: FSMContext):
    async with state.proxy() as data:
        validator = await valid_age(event.text, data['age_min'])
        if validator == 'valid':
            await state.update_data(data={'age_max': int(event.text)})
            await reg_finish(event, state)
        elif validator == 'invalid':
            await event.answer(text='Я так не понимаю\n'
                                    'Просто напиши циферку',
                               reply_markup=back_keys)
        elif validator == 'more_min':
            await event.answer(text='Максимальный возраст для поиска не может быть меньше минимального\n'
                                    'Попробуй ввести постарше',
                               reply_markup=back_keys)
        elif validator == 'too_old':
            await event.answer(text='Ну тут уже проще будет на кладбище поискать\n'
                                    'Попробуй ввести помладше',
                               reply_markup=back_keys)


def register_handlers_reg_f_age(dp: Dispatcher):
    dp.register_message_handler(back_to_sex, state=Reg.f_age_min, regexp="Назад")
    dp.register_message_handler(back_to_age_min, state=Reg.f_age_max, regexp="Назад")
    dp.register_message_handler(valid_age_min, state=Reg.f_age_min)
    dp.register_message_handler(valid_age_max, state=Reg.f_age_max)
