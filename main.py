from aiogram.utils import executor

import config
from models import db_bind
from create_bot import dp


async def on_startup(_):
    print("Connecting to database...")
    await db_bind()
    print("Connected to database succesfully!\n")
    print("Bot started succesfully!")

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
                          register_handlers_search)
    register_handlers_menu(dp)
    register_handlers_search(dp)
    register_handlers_profile(dp)
    register_handlers_prch_name(dp)
    register_handlers_prch_bdate(dp)
    register_handlers_prch_sex(dp)
    register_handlers_prch_geo(dp)
    register_handlers_prch_purposes(dp)
    register_handlers_prch_description(dp)
    register_handlers_prch_age_f(dp)
    register_handlers_prch_photos(dp)
    register_handlers_prch_sex_f(dp)
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
    executor.start_polling(dp, on_startup=on_startup)
