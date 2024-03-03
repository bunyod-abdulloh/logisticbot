from aiogram.types import ReplyKeyboardMarkup


def buy_main_cbuttons_ru():
    buttons = ReplyKeyboardMarkup(resize_keyboard=True)
    buttons.row('Оборудование', 'Сырьё')
    buttons.row('Малые оборудование')
    buttons.row('↩️ назад в Главное меню')
    return buttons


ru_buy_back_button = ReplyKeyboardMarkup(resize_keyboard=True)
ru_buy_back_button.row('️↩️ Назад в меню Закуп')
