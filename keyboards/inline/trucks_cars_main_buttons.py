from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

trucks_cars_buttons = InlineKeyboardMarkup(row_width=2)
trucks_cars_buttons.add(InlineKeyboardButton(
    text='🚗 Yengil avtomobillar', callback_data='car_uz')
)
trucks_cars_buttons.add(InlineKeyboardButton(
    text='🚚 Yuk avtomobillari', callback_data='trucks_uz')
)
trucks_cars_buttons.add(InlineKeyboardButton(
    text='🚜 Qurilish avtomobillari', callback_data='construction_machines_uz')
)
trucks_cars_buttons.add(InlineKeyboardButton(
    text='↩️ Bosh menyuga qaytish', callback_data='construction_machines_uz')
)
