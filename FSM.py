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


class ViaVK(StatesGroup):
    id = State()
    confirm = State()
    code = State()


class Profile(StatesGroup):
    show = State()
    name = State()
    bdate = State()
    sex = State()
    purposes = State()
    geo = State()
    description = State()
    del_photos = State()
    add_photos = State()
    age_min = State()
    age_max = State()
    sex_f = State()
    delete = State()
    desc_more = State()
    d_m_height = State()
    d_m_habits = State()
    d_m_hobby = State()
    d_m_children = State()
    d_m_animals = State()
    d_m_busy = State()


class Search(StatesGroup):
    searching = State()
    complaint_cat = State()
    complaint_desc = State()


class Matches(StatesGroup):
    new_matches = State()
    old_matches = State()


class Complaints(StatesGroup):
    category = State()
    description = State()
    confirm = State()
