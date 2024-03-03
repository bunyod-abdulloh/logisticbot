from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

feedback_uz_ikeys = InlineKeyboardMarkup(row_width=1)
feedback_uz_ikeys.add(
    InlineKeyboardButton(
        text='📸 Rasmli habar yuborish',
        callback_data='feedback_uz_photo'
    ),
    InlineKeyboardButton(
        text='💬 Matnli habar yuborish',
        callback_data='feedback_uz_comment'
    ),
    InlineKeyboardButton(
        text='↩️ Bosh menyuga qaytish',
        callback_data='back_main_uz'
    )
)
