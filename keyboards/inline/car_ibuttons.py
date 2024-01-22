from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def get_car_buttons():
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(
        InlineKeyboardButton(
            text='1', callback_data='1'),
        InlineKeyboardButton(
            text='2', callback_data='2'
        )
    )
    keyboard.add(
        InlineKeyboardButton(
            text='3', callback_data='3'),
        InlineKeyboardButton(
            text='4', callback_data='4'
        )
    )
    keyboard.add(
        InlineKeyboardButton(
            text='⬅️ Orqaga', callback_data='back_car_uz'
        )
    )
    # InlineKeyboardButton(
    #             text='Keyingi ➡️', callback_data='next_car'
    #         )
    return keyboard
