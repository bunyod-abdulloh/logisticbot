from aiogram.types import ReplyKeyboardMarkup


def buy_main_cbuttons():
    buttons = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    buttons.row('Uskunalar', 'Xom ashyo')
    buttons.row('Kichik uskunalar')
    buttons.row('◀️ Ortga')
    return buttons
