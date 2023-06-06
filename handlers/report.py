from aiogram import types, Dispatcher
from FSM import Menu
from aiogram.dispatcher import FSMContext
from funcs import send_menu, do_invalid
from keyboards import yesno_keys
from dbase import send_complaint


async def cancel(event: types.Message, state: FSMContext):
    await event.delete()
    await event.answer("Репорт отменён")
    await send_menu(event, state)


async def get_photos(event: types.PhotoSize, state: FSMContext):
    async with state.proxy() as data:
        if event['photo']:
            file_id = event['photo'][-1]['file_id']
            data['comp_media'].append(file_id)
            if event['caption']:
                data['comp_description'] += f"{event['caption']}\n"
        if event['document']:
            file_id = event['document']["thumbnail"]["file_id"]
            data['comp_media'].append(file_id)
            if event['caption']:
                data['comp_description'] += f"{event['caption']}\n"


async def get_text(event: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['comp_description'] += f"{event.text}\n"


async def ready(event: types.Message, state: FSMContext):
    data = await state.get_data()
    print(data)
    if data['comp_description'] == '' and not data['comp_media']:
        await event.delete()
        await event.answer("Репорт не может быть пустым. Сначала отправь мне текст репорта или картинку, "
                           "затем ещё раз нажми эту кнопку")
    else:
        await event.delete()
        await event.answer(f'{data["comp_description"]}\n'
                           f'+ {len(data["comp_media"])} вложений\n'
                           f'Всё верно?',
                           reply_markup=yesno_keys)
        await Menu.report_confirm.set()


async def readyreport(event: types.Message, state: FSMContext):
    data = await state.get_data()
    await send_complaint(data['pr_id'], None, 'report', data['comp_description'], data['comp_media'])
    await event.answer("Репорт успешно отправлен!")
    await send_menu(event,state)


async def inval(event: types.Message):
    await do_invalid(event, yesno_keys)


def register_handlers_report(dp: Dispatcher):
    dp.register_message_handler(cancel, state=Menu.report, regexp="Назад")
    dp.register_message_handler(ready, state=Menu.report, regexp="Готово!")
    dp.register_message_handler(get_photos, state=Menu.report, content_types=types.ContentType.PHOTO)
    dp.register_message_handler(get_photos, state=Menu.report, content_types=types.ContentType.DOCUMENT)
    dp.register_message_handler(get_text, state=Menu.report)
    dp.register_message_handler(cancel, state=Menu.report_confirm, regexp="Нет")
    dp.register_message_handler(readyreport, state=Menu.report_confirm, regexp="Да")
    dp.register_message_handler(inval, state=Menu.report_confirm)
