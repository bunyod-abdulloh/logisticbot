from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


buy_ru_ikeys = InlineKeyboardMarkup(row_width=1)
buy_ru_ikeys.add(
    InlineKeyboardButton(
        text='📸 Отправить сообщение с рисунком',
        callback_data='buy_ru_photo'
    ),
    InlineKeyboardButton(
        text='💬 Отправить сообщение с текстом',
        callback_data='buy_ru_comment'
    ),
    InlineKeyboardButton(
        text='↩️ назад в меню Закуп',
        callback_data='back_buy_ru'
    )
)
