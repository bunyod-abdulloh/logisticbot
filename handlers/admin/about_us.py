from aiogram import types
from aiogram.dispatcher import FSMContext

from data.config import ADMINS
from keyboards.inline.admin_inline_buttons import admin_check_buttons_uz
from loader import dp, db
from states.admin_states import Admin


@dp.message_handler(state=Admin.about_us_uz)
async def add_about_us_uz(message: types.Message, state: FSMContext):
    await state.update_data(
        about_us_uz=message.text
    )
    await message.answer(
        text='Matn qabul qilindi!\n\nTasdiqlaysizmi?',
        reply_markup=admin_check_buttons_uz
    )


@dp.callback_query_handler(text='again_uz', state='*', user_id=ADMINS[0])
async def admin_again_uz(call: types.CallbackQuery):
    await call.message.edit_text(
        text='Faoliyat matnini qayta kiriting:'
    )
    await Admin.about_us_uz.set()


@dp.callback_query_handler(text='check_uz', state='*', user_id=ADMINS[0])
async def admin_check_uz(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    about_text = data.get('about_us_uz')
    await db.update_description_uz(
        description_uz=about_text, telegram_id=call.from_user.id
    )
    user = await db.select_desription_uz(telegram_id=call.from_user.id)
    print(user)
    await call.message.edit_text(
        text='Matn qabul qilindi!'
    )
    await state.finish()
