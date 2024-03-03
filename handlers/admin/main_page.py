from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from magic_filter import F

from filters.private import IsPrivate
from keyboards.default.admin_custom_buttons import admin_uz_main_buttons, cars_cbuttons, stats_main
from keyboards.inline.admin_inline_buttons import admin_delete_button
from loader import dp, db
from states.admin_states import Admin


@dp.message_handler(Command(['admins']), state='*')
async def admin_page_main(message: types.Message, state: FSMContext):
    await state.finish()
    admin = await db.select_admin_sql(
        telegram_id=message.from_user.id
    )
    if admin:
        await message.answer(
            text=message.text,
            reply_markup=admin_uz_main_buttons
        )


@dp.message_handler(IsPrivate(), F.text == '😎 Adminlarni ko\'rish', state='*')
async def view_admins_cmd(message: types.Message, state: FSMContext):
    await state.finish()
    admins = await db.select_admins_sql()
    if admins:
        for admin in admins:
            await message.answer(
                text=f'Admin: {admin[1]}\nID raqam: {admin[0]}',
                reply_markup=await admin_delete_button(
                    telegram_id=admin[0]
                )
            )
    else:
        await message.answer(
            text='Hozircha Sizdan boshqa admin yo\'q!'
        )


@dp.message_handler(IsPrivate(), F.text == '➕ Admin qo\'shish', state='*')
async def add_admin_cmd(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer(
        text='Admin ismini kiriting:'
    )
    await Admin.add_admin_name.set()


@dp.message_handler(IsPrivate(), F.text == '🚙 Avtomobillar bo\'limi', state='*')
async def cars_main_admin(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer(
        text=message.text, reply_markup=cars_cbuttons
    )
    await Admin.cars_main.set()


@dp.message_handler(IsPrivate(), F.text == '📊 Hisobot', state='*')
async def stats_cmd(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer(
        text=message.text, reply_markup=stats_main
    )


@dp.message_handler(IsPrivate(), F.text == '👥 Foydalanuvchilar soni', state='*')
async def count_users_cmd(message: types.Message, state: FSMContext):
    await state.finish()
    users = await db.count_users()
    await message.answer(
        text=f'Foydalanuvchilar soni: {users}'
    )


@dp.message_handler(IsPrivate(), F.text == '🗣 Foydalanuvchilarga habar yuborish', state='*')
async def send_to_users(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer(
        text='Yubormoqchi bo\'lgan habaringizni kiriting \n(faqat matnli habar yuboriladi!)'
    )
    await Admin.send_to_users.set()


@dp.message_handler(IsPrivate(), F.text == 'ID olish', state='*')
async def get_id_cmd(message: types.Message):
    admin = await db.select_admin_sql(telegram_id=message.from_user.id)
    if admin:
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
