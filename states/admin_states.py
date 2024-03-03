from aiogram.dispatcher.filters.state import StatesGroup, State


class Admin(StatesGroup):
    add_admin_name = State()
    add_admin_id = State()
    send_to_users = State()
    check_send = State()
    get_id = State()
    delete_user = State()
    unblock_user = State()
    add_cars_catalog = State()
