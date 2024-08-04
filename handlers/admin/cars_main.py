from aiogram import types
from magic_filter import F

from data.config import ADMINS
from filters.private import IsPrivate
from keyboards.default.admin_custom_buttons import admin_uz_main_buttons
from loader import dp


@dp.message_handler(IsPrivate(), F.text == "↩️ Admin menyusiga qaytish", state="*", user_id=ADMINS)
async def admin_cars_main_uz(message: types.Message):
    await message.answer(
        text=message.text, reply_markup=admin_uz_main_buttons
    )
