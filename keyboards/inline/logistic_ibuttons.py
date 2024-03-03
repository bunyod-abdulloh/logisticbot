from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def uz_transport_ibuttons(region: str):
    key = InlineKeyboardMarkup(row_width=1)
    key.add(
        InlineKeyboardButton(
            text='✈️ Avia', callback_data=f'avia_{region}'
        ),
        InlineKeyboardButton(
            text='🚗 Avtomobil', callback_data=f'auto_{region}'
        ),
        InlineKeyboardButton(
            text='🚇 Temir yo\'l', callback_data=f'railway_{region}'
        ),
        InlineKeyboardButton(
            text='⏳ Multimodal', callback_data=f'multimodal_{region}'
        )
    )
    key.add(
        InlineKeyboardButton(
            text='⬅️️ Logistika bo\'limiga qaytish', callback_data='back_logistic_uz'
        )
    )
    return key


def uz_logictic_questions_ikeys(region: str, call_admin: str):
    button = InlineKeyboardMarkup(row_width=1)
    button.add(InlineKeyboardButton(
        text='❔ Savollarga javob berish',
        callback_data=region
    ),
        InlineKeyboardButton(
            text='📞 Operator bilan bog\'lanish',
            callback_data=call_admin
        ),
        InlineKeyboardButton(
            text='⬅️️ Logistika bo\'limiga qaytish',
            callback_data='back_logistic_uz'
        )
    )
    return button
