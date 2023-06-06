from aiogram import types, Dispatcher
from keyboards import filter_keys, cancel_keys
from FSM import Profile
from aiogram.dispatcher import FSMContext
from dbase import upd_dist
from funcs import show_myprofile


async def cancel(event: types.Message):
    await event.answer(text="Выбери фильтр:",
                       reply_markup=filter_keys)
    await Profile.filters.set()


async def valid(event: types.Message, state: FSMContext):
    data = await state.get_data()
    try:
        dist = int(event.text)
        if dist < 5:
            await event.delete()
            await event.answer(text="Это слишком мало, мне пока что будет сложно найти профили так близко\n"
                                    "Минимум 5 км",
                               reply_markup=cancel_keys)
        elif dist > 60:
            await event.delete()
            await event.answer(text="Это слишком далеко\n"
                                    "Давай поищем ближе 60км. Если нужен другой город, просто обнови геолокацию",
                               reply_markup=cancel_keys)
        else:
            await event.delete()
            await upd_dist(data['pr_id'], dist)
            await event.answer(text="Успешно обновил!")
            await show_myprofile(event, state)
    except:
        await event.delete()
        await event.answer(text="Я не знаю, что делать с этим сообщением\n"
                                "Мне нужна только циферка, в радиусе скольки километров будем искать другие профили",
                           reply_markup=cancel_keys)


def register_handlers_prch_dist(dp: Dispatcher):
    dp.register_message_handler(cancel, state=Profile.km_f, regexp="Отмена")
    dp.register_message_handler(valid, state=Profile.km_f)
