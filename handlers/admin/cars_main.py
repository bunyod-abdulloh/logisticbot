from aiogram import types
from magic_filter import F

from filters.private import IsPrivate
from keyboards.default.admin_custom_buttons import admin_uz_main_buttons
from loader import dp, db


@dp.message_handler(IsPrivate(), F.text == "↩️ Admin menyusiga qaytish", state="*")
async def admin_cars_main_uz(message: types.Message):
    admin = await db.select_admin_sql(
        telegram_id=message.from_user.id
    )
    if admin:
        await message.answer(
            text=message.text, reply_markup=admin_uz_main_buttons
        )
