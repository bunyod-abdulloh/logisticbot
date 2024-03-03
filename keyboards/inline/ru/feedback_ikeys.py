from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

feedback_ru_ikeys = InlineKeyboardMarkup(row_width=1)
feedback_ru_ikeys.add(
    InlineKeyboardButton(
        text='📸 Отправить в виде Фото',
        callback_data='feedback_ru_photo'
    ),
    InlineKeyboardButton(
        text='💬 Отправить в виде Текста',
        callback_data='feedback_ru_comment'
    ),
    InlineKeyboardButton(
        text='↩️ Назад в Главное меню',
        callback_data='back_main_ru'
    )
)
