from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from loader import db


async def get_brand_buttons_ru():
    cars = await db.select_cars()
    keyboard = InlineKeyboardMarkup(row_width=2)
    for car in cars:
        keyboard.insert(
            InlineKeyboardButton(
                text=f'{car[0]}', callback_data=f'{car[0]}')
        )
    keyboard.add(
        InlineKeyboardButton(text='↩️ Назад в Главное меню', callback_data='back_main_ru'
                             )
    )
    return keyboard


def key_returner_ru(items, current_page, all_pages):
    keys = InlineKeyboardMarkup(
        row_width=5
    )
    for text, value in enumerate(items):
        keys.insert(
            InlineKeyboardButton(
                text=f"{text + 1}",
                callback_data=f"{value[0]}"
            )
        )
    keys.row(
        InlineKeyboardButton(
            text="⬅️ Предыдущий",
            callback_data="prevru"
        ),
        InlineKeyboardButton(
            text=f"{current_page}/{all_pages}",
            callback_data=f"alertru_{current_page}"
        ),
        InlineKeyboardButton(
            text="Следующий ➡️",
            callback_data="nextru"
        )
    )
    keys.add(
        InlineKeyboardButton(
            text="↩️ Назад в меню Бренды",
            callback_data="car_menu_ru"
        )
    )
    return keys


def back_models_ibutton_ru(car_id):
    key = InlineKeyboardMarkup(row_width=1)
    key.add(
        InlineKeyboardButton(
            text='📞 Связаться с оператором',
            callback_data=f'carru_{car_id}'
        ),
        InlineKeyboardButton(
            text='⬅️ Назад',
            callback_data="backmodelsru"
        )
    )
    return key
