from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def transport_ibuttons_ru(region: str):
    key = InlineKeyboardMarkup(row_width=1)
    key.add(
        InlineKeyboardButton(
            text='✈️ Авиа', callback_data=f'aviaru_{region}'
        ),
        InlineKeyboardButton(
            text='🚗 Автомобиль', callback_data=f'autoru_{region}'
        ),
        InlineKeyboardButton(
            text='🚇 Железнодорожная', callback_data=f'railwayru_{region}'
        ),
        InlineKeyboardButton(
            text='⏳ Мультимодальный', callback_data=f'multimodalru_{region}'
        )
    )
    key.add(
        InlineKeyboardButton(
            text='⬅️️ Назад в меню Логистика', callback_data='back_logistic_ru'
        )
    )
    return key


def ru_logictic_questions_ikeys(region: str, call_admin: str):
    button = InlineKeyboardMarkup(row_width=1)
    button.add(InlineKeyboardButton(
        text='❔ Ответить на вопросы',
        callback_data=region
    ),
        InlineKeyboardButton(
            text='📞 Связаться с оператором',
            callback_data=call_admin
        ),
        InlineKeyboardButton(
            text='⬅️️ Назад в меню Логистика',
            callback_data='back_logistic_ru'
        )
    )
    return button
