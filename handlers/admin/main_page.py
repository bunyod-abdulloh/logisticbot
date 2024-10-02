from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from magic_filter import F

from data.config import ADMINS
from filters.private import IsPrivate
from keyboards.default.admin_custom_buttons import admin_uz_main_buttons, cars_cbuttons, stats_main
from loader import dp, db
from states.admin_states import Admin


@dp.message_handler(Command(['admin']), state='*', user_id=ADMINS)
async def admin_page_main(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer(
        text=message.text,
        reply_markup=admin_uz_main_buttons
    )


@dp.message_handler(IsPrivate(), F.text == '🚙 Avtomobillar bo\'limi', state='*', user_id=ADMINS)
async def cars_main_admin(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer(
        text=message.text, reply_markup=cars_cbuttons
    )


@dp.message_handler(IsPrivate(), F.text == '📊 Hisobot', state='*', user_id=ADMINS)
async def stats_cmd(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer(
        text=message.text, reply_markup=stats_main
    )


@dp.message_handler(IsPrivate(), F.text == '👥 Foydalanuvchilar soni', state='*', user_id=ADMINS)
async def count_users_cmd(message: types.Message, state: FSMContext):
    await state.finish()
    users = await db.count_users()
    await message.answer(
        text=f'Foydalanuvchilar soni: {users}'
    )


@dp.message_handler(IsPrivate(), F.text == '🗣 Foydalanuvchilarga habar yuborish', state='*', user_id=ADMINS)
async def send_to_users(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer(
        text='Yubormoqchi bo\'lgan habaringizni kiriting \n(faqat matnli habar yuboriladi!)'
    )
    await Admin.send_to_users.set()


@dp.message_handler(IsPrivate(), F.text == 'ID olish', state='*', user_id=ADMINS)
async def get_id_cmd(message: types.Message):
    await message.answer(
        text=f'ID olish bo\'limi yoqildi!\n\nRasmlarni yuborib ID raqamlarini olishingiz mumkin!'
             f'\n\nMarhamat, rasm yuboring'
    )
    await Admin.get_id.set()


@dp.message_handler(state=Admin.get_id, content_types=['photo'])
async def get_id_photo(message: types.Message):
    await message.answer(
        text=f'RASM ID RAQAMI: \n\n<code>{message.photo[-1].file_id}</code>'
    )


@dp.message_handler(IsPrivate(), F.text == 'ID o\'chirish', state='*')
async def delete_id_cmd(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer(
        text='ID olish o\'chirildi!'
    )
