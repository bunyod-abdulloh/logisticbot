from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def type_transport_ibuttons(region: str):
    key = InlineKeyboardMarkup(row_width=1)
    key.add(
        InlineKeyboardButton(
            text='Avia', callback_data=f'avia_{region}'
        ),
        InlineKeyboardButton(
            text='Avtomobil', callback_data=f'auto_{region}'
        ),
        InlineKeyboardButton(
            text='Temir yo\'l', callback_data=f'railway_{region}'
        ),
        InlineKeyboardButton(
            text='Kutilmoqda', callback_data=f'expected_{region}'
        )
    )
    return key
