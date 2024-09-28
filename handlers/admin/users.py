import datetime
import os

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from magic_filter import F

from data.config import DATABASE_GROUP, ADMINS
from filters.private import IsPrivate
from handlers.admin.export_to_xls import export_to_excel
from keyboards.default.admin_custom_buttons import admin_users_button
from loader import dp, db, bot
from states.admin_states import Admin


@dp.message_handler(IsPrivate(), F.text == 'Foydalanuvchilar', state='*')
async def view_all_users_menu(message: types.Message):
    await message.answer(
        text='Foydalanuvchilar bo\'limi', reply_markup=admin_users_button
    )


@dp.message_handler(F.text == "users", user_id=ADMINS)
async def download_user_xls(message: types.Message = None):
    users = await db.select_all_users()
    current_date = datetime.date.today()
    filepath = f"downloads/userslogistic_{current_date}.xlsx"
    await export_to_excel(
        data=users, headings=["ID", "TELEGRAM_ID", "FULL_NAME", "USERNAME", "PHONE", "LANGUAGE"], filepath=filepath
    )
    await bot.send_document(
        chat_id=DATABASE_GROUP,
        document=types.input_file.InputFile(path_or_bytesio=filepath),
        caption=f"#logisticAT #users\n\n{current_date}\n\nFOYDALANUVCHILAR JADVALI"
    )
    os.remove(filepath)


@dp.message_handler(IsPrivate(), F.text == 'Block user', state='*')
async def block_user_menu(message: types.Message):
    await message.answer(
        text='Foydalanuvchi ID raqamini kiriting'
    )
    await Admin.delete_user.set()


@dp.message_handler(state=Admin.delete_user)
async def delete_user_menu(message: types.Message, state: FSMContext):
    await state.finish()
    telegram_id = int(message.text)
    await db.update_user_blocks(
        blocked_user=telegram_id, telegram_none=None, telegram_id=telegram_id
    )
    await message.answer(
        text='Foydalanuvchi bloklandi!'
    )
    try:
        await bot.send_message(
            chat_id=telegram_id,
            text='Sizga botdan foydalanish bo\'yicha cheklov qo\'yildi!',
            reply_markup=types.ReplyKeyboardRemove()
        )
    except Exception:
        pass


@dp.message_handler(IsPrivate(), F.text == 'Unblock user', state='*')
async def edit_blocked_user_menu(message: types.Message):
    await message.answer(
        text='Foydalanuvchi ID raqamini kiriting'
    )
    await Admin.unblock_user.set()


@dp.message_handler(state=Admin.unblock_user)
async def unblock_user_menu(message: types.Message, state: FSMContext):
    await state.finish()
    telegram_id = int(message.text)
    await db.update_user_unblock(
        unblock=None, telegram_id=telegram_id, blocked_user=telegram_id
    )
    await message.answer(
        text='Foydalanuvchi blokdan chiqarildi!'
    )
    try:
        await bot.send_message(
            chat_id=telegram_id,
            text='Sizga botdan qayta foydalanish imkoniyati ochildi! /start buyrug\'ini kiritib botdan '
                 'foydalanishingiz foydalanishingiz mumkin!'
        )
    except Exception:
        pass


@dp.message_handler(IsPrivate(), Command('id'), state='*')
async def get_id_user(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer(
        text=f'ID: <code>{message.from_user.id}</code>'
    )
