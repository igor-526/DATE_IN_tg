from aiogram.dispatcher.filters.state import State, StatesGroup


class Menu(StatesGroup):
    menu = State()
    registration = State()
    return_profile = State()


class Reg(StatesGroup):
    profile = State()
    name_auto = State()
    name_manual = State()
    bdate = State()
    sex = State()
    geo = State()
    photo = State()
    description = State()
    purposes = State()
    f_sex = State()
    f_age_min = State()
    f_age_max = State()
