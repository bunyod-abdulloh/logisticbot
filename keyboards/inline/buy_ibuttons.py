from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


buy_uz_ikeys = InlineKeyboardMarkup(row_width=1)
buy_uz_ikeys.add(
    InlineKeyboardButton(
        text='📸 Rasmli habar yuborish',
        callback_data='buy_uz_photo'
    ),
    InlineKeyboardButton(
        text='💬 Matnli habar yuborish',
        callback_data='buy_uz_comment'
    ),
    InlineKeyboardButton(
        text='↩️ Xarid bo\'limiga qaytish',
        callback_data='back_buy_uz'
    )
)

# https://onmap.uz/tel/paste_phone_number
