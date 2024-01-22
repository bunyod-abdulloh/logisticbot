from aiogram.dispatcher.filters.state import StatesGroup, State


class UserForms(StatesGroup):
    full_name = State()
    phone = State()
