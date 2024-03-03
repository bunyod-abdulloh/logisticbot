from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

profile_ru_ikeys = InlineKeyboardMarkup(row_width=1)
profile_ru_ikeys.add(InlineKeyboardButton(text='📝 Изменить язык', callback_data='language_ru'),
                     InlineKeyboardButton(text='😎 Изменить имя', callback_data='name_ru'),
                     InlineKeyboardButton(text='👤 Изменить username', callback_data='username_ru'),
                     InlineKeyboardButton(text='📱 Изменить номер телефона', callback_data='phone_ru'),
                     InlineKeyboardButton(text='↩️ вернуться в Главное меню', callback_data='back_main_ru'))
