from aiogram import types
from aiogram.dispatcher import FSMContext

from data.config import ADMINS
from keyboards.default.admin_custom_buttons import admin_uz_main_buttons, cars_cbuttons
from keyboards.inline.admin_inline_buttons import admin_delete_button
from keyboards.inline.menu_keyboards import select_language_buttons
from loader import dp, db
from states.admin_states import Admin


@dp.message_handler(text='/admins', state='*')
async def admin_page_main(message: types.Message):
    # await message.answer(
    #     text="Tilni tanlang:"
    #          "\n\nВыберите язык:",
    #     reply_markup=admin_language_buttons_
    # )
    admin = await db.select_admin_sql(
        telegram_id=message.from_user.id
    )
    if admin:
        await message.answer(
            text=message.text,
            reply_markup=admin_uz_main_buttons
        )


@dp.message_handler(text='😎 Adminlarni ko\'rish', state='*')
async def view_admins_cmd(message: types.Message):
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


@dp.message_handler(text='➕ Admin qo\'shish', state='*')
async def add_admin_cmd(message: types.Message):
    await message.answer(
        text='Admin ismini kiriting:'
    )
    await Admin.add_admin_name.set()


@dp.message_handler(text='🚙 Avtomobillar bo\'limi', state='*')
async def cars_main_admin(message: types.Message):
    await message.answer(
        text=message.text, reply_markup=cars_cbuttons
    )
    await Admin.cars_main.set()
    
    
@dp.message_handler(text='🏢 Biz haqimizda bo\'limiga matn', state='*')
async def about_us_cmd(message: types.Message):
    telegram_id = message.from_user.id
    about_us_uz = await db.select_desription_uz(
        telegram_id=telegram_id
    )
    if about_us_uz:
        pass
    else:
        await message.answer(
            text='Faoliyat to\'g\'risidagi ma\'lumotlarni kiriting:'
        )
        await Admin.about_us_uz.set()
