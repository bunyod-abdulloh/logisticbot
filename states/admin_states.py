from aiogram.dispatcher.filters.state import StatesGroup, State


class Admin(StatesGroup):
    about_us_uz = State()
    about_us_ru = State()
    add_admin_name = State()
    add_admin_id = State()
    cars_main = State()
    