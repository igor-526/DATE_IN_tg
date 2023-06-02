from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from dbase import chk_reg, get_profile_id, del_profile
from funcs import send_menu


async def rules(event: types.Message):
    with open(file='fixtures/rules.txt', mode='r') as file:
        await event.answer(text=file.read())


async def deleteprofile(event: types.Message):
    pr_id = await get_profile_id(event.from_user.id)
    await del_profile(pr_id)


async def reset(event: types.Message, state: FSMContext):
    await state.finish()
    await event.answer("Успешно. Напишите что-нибудь")


async def smenu(event: types.Message, state: FSMContext):
    check = await chk_reg(event.from_user.id)
    if check.status == 'active':
        await state.update_data({'pr_id': check.id})
        await send_menu(event, state)
    elif check.status == 'deactivated':
        await event.answer(text="Ошибка\n"
                                "Ваш профиль дактивирован, команда недоступна")
    elif check.status == 'freeze':
        await event.answer(text='Ваш профиль был временно заморожен администрацией, так как нарушал правила '
                                'использования сервиса\n'
                                'Если Вы с этим не согласны, напишите в /report')


async def help(event: types.Message):
    with open(file='fixtures/help.txt', mode='r') as file:
        await event.answer(text=file.read())


def register_handlers_commands(dp: Dispatcher):
    dp.register_message_handler(deleteprofile, commands=['deleteprofile'], state='*')
    dp.register_message_handler(rules, commands=['rules'], state='*')
    dp.register_message_handler(reset, commands=['reset'], state='*')
    dp.register_message_handler(smenu, commands=['menu'], state='*')
    dp.register_message_handler(help, commands=['help', 'info'], state='*')
