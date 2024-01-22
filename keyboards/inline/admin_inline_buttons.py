from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

admin_check_buttons_uz = InlineKeyboardMarkup(row_width=2)
admin_check_buttons_uz.add(
    InlineKeyboardButton(
        text='🔄 Qayta kiritish', callback_data='again_uz'
    ),
    InlineKeyboardButton(
        text='✅ Tasdiqlash', callback_data='check_uz'
    )
)


async def admin_delete_button(telegram_id):
    key = InlineKeyboardMarkup(row_width=1)
    key.add(
        InlineKeyboardButton(
            text='⛔️ O\'chirish', callback_data=f'admindelete_{telegram_id}'
        ),
        InlineKeyboardButton(
            text='⬅️ Ortga', callback_data='admin_back'
        )
    )
    return key
