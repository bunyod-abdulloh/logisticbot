from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

select_language_buttons = InlineKeyboardMarkup(row_width=2)
select_language_buttons.row(
    InlineKeyboardButton(
        text='O\'zbekcha', callback_data='uz'
    ),
    InlineKeyboardButton(
        text='Русский', callback_data='ru'
    )
)
