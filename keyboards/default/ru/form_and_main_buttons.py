from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

ru_get_contact = ReplyKeyboardMarkup(resize_keyboard=True)
ru_get_contact.add(
    KeyboardButton(
        text='📍 Отправить номер телефона', request_contact=True
    )
)

menu_ru_buttons = ReplyKeyboardMarkup(resize_keyboard=True)
menu_ru_buttons.row('🚙 Автомобили')
menu_ru_buttons.row('📦 Услуга логистики')
menu_ru_buttons.add('🛍 Закуп', '🏢 О нас')
menu_ru_buttons.add('👤 Профиль')
menu_ru_buttons.add('🎙 Написать отзыв')
