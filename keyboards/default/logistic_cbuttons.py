from aiogram.types import ReplyKeyboardMarkup


def logistic_main_cbuttons():
    buttons = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    buttons.add('Mustaqil Davlatlar Hamdo\'stiligi (MDH)')
    buttons.row('Yevropa', 'Osiyo')
    buttons.row('Amerika Qo\'shma Shtatlari (AQSH)')
    buttons.add('Xitoy')
    buttons.row('↩️ Bosh menyuga qaytish')
    return buttons
