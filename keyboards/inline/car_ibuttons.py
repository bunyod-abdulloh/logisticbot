from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from loader import db


async def get_brand_buttons():
    cars = await db.select_cars()
    keyboard = InlineKeyboardMarkup(row_width=2)
    for car in cars:
        keyboard.insert(
            InlineKeyboardButton(
                text=f'{car[0]}', callback_data=f'{car[0]}')
        )
    keyboard.add(
        InlineKeyboardButton(text='↩️ Bosh menyuga qaytish', callback_data='back_main_uz'
                             )
    )
    return keyboard


def key_returner(items, current_page, all_pages):
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
            text="⬅️ Ortga",
            callback_data="prev"
        ),
        InlineKeyboardButton(
            text=f"{current_page}/{all_pages}",
            callback_data=f"alertmessage_{current_page}"
        ),
        InlineKeyboardButton(
            text="Oldinga ➡️",
            callback_data="next"
        )
    )
    keys.add(
        InlineKeyboardButton(
            text="↩️ Brendlar bo'limiga qaytish",
            callback_data="car_menu_uz"
        )
    )
    return keys


def back_models_ibutton(car_id):
    key = InlineKeyboardMarkup(row_width=1)
    key.add(
        InlineKeyboardButton(
            text='📞 Operator bilan bog\'lanish',
            callback_data=f'uzcar_{car_id}'
        ),
        InlineKeyboardButton(
            text='⬅️ Ortga',
            callback_data="backmodelsuz"
        )
    )
    return key
