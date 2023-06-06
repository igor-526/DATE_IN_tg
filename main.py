from aiogram.utils import executor
import urllib3
from models import db_bind, db_close
from create_bot import dp, bot


async def on_startup(_):
    print("Connecting to database...")
    await db_bind()
    print("Bot started succesfully!")
    urllib3.disable_warnings()
    await bot.set_webhook(WEBHOOK_DOMAIN, drop_pending_updates=True)


async def on_shutdown(_):
    await db_close()
    await bot.delete_webhook()

if __name__ == "__main__":
    from handlers import (register_handlers_menu,
                          register_handlers_profile,
                          register_handlers_reg_profile,
                          register_handlers_reg_name,
                          register_handlers_reg_bdate,
                          register_handlers_reg_sex,
                          register_handlers_reg_geo,
                          register_handlers_reg_photo,
                          register_handlers_reg_description,
                          register_handlers_reg_purposes,
                          register_handlers_reg_sex_f,
                          register_handlers_reg_f_age,
                          register_handlers_viavk_id,
                          register_handlers_viavk_confirm,
                          register_handlers_viavk_code,
                          register_handlers_prch_name,
                          register_handlers_prch_bdate,
                          register_handlers_prch_sex,
                          register_handlers_prch_purposes,
                          register_handlers_prch_geo,
                          register_handlers_prch_description,
                          register_handlers_prch_photos,
                          register_handlers_prch_age_f,
                          register_handlers_prch_sex_f,
                          register_handlers_prch_delprofile,
                          register_handlers_search,
                          register_handlers_matches,
                          register_handlers_comp_category,
                          register_handlers_comp_description,
                          register_handlers_comp_confirm,
                          register_handlers_prch_more_desc,
                          register_handlers_prmd_height,
                          register_handlers_prmd_habits,
                          register_handlers_prmd_children,
                          register_handlers_prmd_busy,
                          register_handlers_prmd_hobby,
                          register_handlers_prmd_animals,
                          register_handlers_commands,
                          register_handlers_updgeo,
                          register_handlers_report,
                          register_handlers_prch_dist)
    register_handlers_commands(dp)
    register_handlers_report(dp)
    register_handlers_menu(dp)
    register_handlers_search(dp)
    register_handlers_matches(dp)
    register_handlers_updgeo(dp)
    register_handlers_profile(dp)
    register_handlers_comp_category(dp)
    register_handlers_comp_description(dp)
    register_handlers_comp_confirm(dp)
    register_handlers_prch_name(dp)
    register_handlers_prch_bdate(dp)
    register_handlers_prch_sex(dp)
    register_handlers_prch_geo(dp)
    register_handlers_prch_purposes(dp)
    register_handlers_prch_description(dp)
    register_handlers_prch_age_f(dp)
    register_handlers_prch_photos(dp)
    register_handlers_prch_sex_f(dp)
    register_handlers_prch_more_desc(dp)
    register_handlers_prch_delprofile(dp)
    register_handlers_prch_dist(dp)
    register_handlers_prmd_height(dp)
    register_handlers_prmd_habits(dp)
    register_handlers_prmd_children(dp)
    register_handlers_prmd_busy(dp)
    register_handlers_prmd_hobby(dp)
    register_handlers_prmd_animals(dp)
    register_handlers_reg_profile(dp)
    register_handlers_reg_name(dp)
    register_handlers_reg_bdate(dp)
    register_handlers_reg_sex(dp)
    register_handlers_reg_geo(dp)
    register_handlers_reg_photo(dp)
    register_handlers_reg_description(dp)
    register_handlers_reg_purposes(dp)
    register_handlers_reg_sex_f(dp)
    register_handlers_reg_f_age(dp)
    register_handlers_viavk_id(dp)
    register_handlers_viavk_confirm(dp)
    register_handlers_viavk_code(dp)
    WEBHOOK_DOMAIN = 'https://datein.ru/tgbot'
    WEBAPP_HOST = '127.0.0.1'
    WEBAPP_PORT = '3001'
    # executor.start_polling(dp, on_startup=on_startup, on_shutdown=on_shutdown)
    executor.start_webhook(dispatcher=dp,
                           webhook_path='',
                           on_startup=on_startup,
                           on_shutdown=on_shutdown,
                           skip_updates=True,
                           host=WEBAPP_HOST,
                           port=WEBAPP_PORT)


