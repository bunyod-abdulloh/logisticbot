from aiogram.types import ReplyKeyboardMarkup


def logistic_main_cbuttons_ru():
    buttons = ReplyKeyboardMarkup(resize_keyboard=True)
    buttons.add('Содружество Независимых Государств (СНГ)')
    buttons.row('Европа', 'Азия')
    buttons.row('Соединенные Штаты Америки (США)')
    buttons.add('Китай')
    buttons.row('↩️ назад в Главное меню')
    return buttons
