from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

get_contact = ReplyKeyboardMarkup(resize_keyboard=True)
get_contact.add(
    KeyboardButton(
        text='📍 Telefon raqam yuborish', request_contact=True
    )
)

menu_uz_buttons = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
menu_uz_buttons.row('🚙 Avtomobillar')
menu_uz_buttons.row('📦 Logistika xizmati')
menu_uz_buttons.add('🏢 Biz haqimizda', '👤 Profil')
menu_uz_buttons.add('🎙 Fikr va mulohazalaringizni yuboring')
