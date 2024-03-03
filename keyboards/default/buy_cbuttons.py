from aiogram.types import ReplyKeyboardMarkup


def buy_main_cbuttons():
    buttons = ReplyKeyboardMarkup(resize_keyboard=True)
    buttons.row('Uskunalar', 'Xom ashyo')
    buttons.row('Kichik uskunalar')
    buttons.row('↩️ Bosh menyuga qaytish')
    return buttons


buy_back_button = ReplyKeyboardMarkup(resize_keyboard=True)
buy_back_button.row('️↩️ Xarid bo\'limiga qaytish')
