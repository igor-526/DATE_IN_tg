from aiogram.utils import executor

import config
from models import db_bind, db_reset
from create_bot import dp


async def on_startup(_):
    print("Connecting to database...")
    await db_bind()
    print("Connected to database succesfully!\n")
    if config.reset_db == 1:
        await db_reset()
        print("DATABASE WAS RESETED\n")
    print("Bot started succesfully!")

if __name__ == "__main__":
    from handlers import (register_handlers_menu,
                          register_handlers_reg_profile,
                          register_handlers_reg_name,
                          register_handlers_reg_bdate,
                          register_handlers_reg_sex,
                          register_handlers_reg_geo)
    register_handlers_menu(dp)
    register_handlers_reg_profile(dp)
    register_handlers_reg_name(dp)
    register_handlers_reg_bdate(dp)
    register_handlers_reg_sex(dp)
    register_handlers_reg_geo(dp)
    executor.start_polling(dp, on_startup=on_startup)
