from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.default.form_and_main_buttons import get_contact, menu_uz_buttons
from loader import dp, db
from states.user_states import UserForms


@dp.message_handler(state=UserForms.full_name)
async def get_full_name_forms(message: types.Message):
    if message.text.isalpha():
        await db.update_user_fullname(
            full_name=message.text, telegram_id=message.from_user.id
        )
        await message.answer(
            text='Raqamingizni habar bilan <b>998XXXXXXXXX</b> shaklda yoki quyidagi tugma orqali yuboring:',
            reply_markup=get_contact
        )
        await UserForms.phone.set()
    else:
        await message.answer(
            text='Iltimos, faqat harf kiriting'
        )


@dp.message_handler(state=UserForms.phone, content_types=['contact', 'text'])
async def get_phone_forms(message: types.Message, state: FSMContext):
    telegram_id = message.from_user.id
    username = message.from_user.username
    if message.content_type == 'contact':
        await db.update_user_phone_username(
            phone=message.contact.phone_number, username=f'@{username}', telegram_id=telegram_id
        )
        await message.answer(
            text='Siz ro\'yxatdan muvaffaqqiyatli o\'tdingiz!',
            reply_markup=menu_uz_buttons
        )
        await state.finish()
    elif message.text.isdigit():
        await db.update_user_phone_username(
            phone=f'+{message.text}', username=f'@{username}', telegram_id=telegram_id
        )
        await message.answer(
            text='Siz ro\'yxatdan muvaffaqqiyatli o\'tdingiz!',
            reply_markup=menu_uz_buttons
        )
        await state.finish()
    else:
        await message.answer(
            text='Iltimos, faqat raqam kiriting!'
        )
