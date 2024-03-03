from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

profile_uz_ikeys = InlineKeyboardMarkup(row_width=1)
profile_uz_ikeys.add(InlineKeyboardButton(text='📝 Tilni o\'zgartirish', callback_data='language_uz'),
                     InlineKeyboardButton(text='😎 Ismni o\'zgartirish', callback_data='name_uz'),
                     InlineKeyboardButton(text='👤 Username o\'zgartirish', callback_data='username_uz'),
                     InlineKeyboardButton(text='📱 Telefon raqamni o\'zgartirish', callback_data='phone_uz'),
                     InlineKeyboardButton(text='↩️ Bosh menyuga qaytish', callback_data='back_main_uz'))
