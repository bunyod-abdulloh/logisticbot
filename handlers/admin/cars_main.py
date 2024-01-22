from aiogram import types

from loader import dp, db
from states.admin_states import Admin


@dp.message_handler(state=Admin.cars_main)
async def cars_main_cmd_(message: types.Message):
    admin = await db.select_admin_sql(
        telegram_id=message.from_user.id
    )
    if admin:
        if message.text == '🚗 Yengil avtomobillar':
            pass
        elif message.text == '🚚 Yuk avtomobillari':
            pass
        elif message.text == '🚜 Qurilish avtomobillari':
            pass
        else:
            pass
