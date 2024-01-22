from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.default.admin_custom_buttons import admin_uz_main_buttons
from loader import dp, db
from states.admin_states import Admin


@dp.message_handler(state=Admin.add_admin_name)
async def admin_add_admin(message: types.Message, state: FSMContext):
    await state.update_data(
        admin_name=message.text
    )
    await message.answer(
        text='Admin ID raqamini kiriting:'
    )
    await Admin.add_admin_id.set()


@dp.message_handler(state=Admin.add_admin_id)
async def add_admin_id(message: types.Message, state: FSMContext):
    data = await state.get_data()
    full_name = data.get('admin_name')
    admin_id = int(message.text)

    await db.add_admin(telegram_id=admin_id, full_name=full_name)
    await message.answer(
        text='Adminlar ro\'yxatiga yangi admin qo\'shildi!'
    )
    await state.finish()


@dp.callback_query_handler(text_contains='admindelete_')
async def delete_admin_cmd_(call: types.CallbackQuery):
    admin_id = call.data.split('_')[1]
    await db.delete_admin_sql(
        telegram_id=admin_id
    )
    await call.answer(
        text='Admin ma\'lumotlar omboridan o\'chirildi!', show_alert=True
    )
    await call.message.delete()


@dp.callback_query_handler(text='', state='*')
async def back_admin_menu(call: types.CallbackQuery):
    await call.message.edit_text(
        text='Admin bosh sahifasi', reply_markup=admin_uz_main_buttons
    )
