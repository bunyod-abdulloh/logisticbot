from aiogram import types
from aiogram.dispatcher import FSMContext
from magic_filter import F

from keyboards.default.ru.form_and_main_buttons import menu_ru_buttons
from loader import dp, db
from states.user_states import UserProfile


@dp.callback_query_handler(F.data == 'language_uz', state='*')
async def change_language_uz(call: types.CallbackQuery):
    await db.update_user_language(language='ru', telegram_id=call.from_user.id)
    await call.message.answer(
        text=f'Выбран русский язык', reply_markup=menu_ru_buttons
    )


@dp.callback_query_handler(F.data == 'name_uz', state='*')
async def change_name_uz(call: types.CallbackQuery):
    await call.message.edit_text(
        text='O\'zgartirmoqchi bo\'lgan ismni kiriting'
    )
    await UserProfile.edit_name.set()


@dp.callback_query_handler(F.data == 'username_uz', state='*')
async def change_username_uz(call: types.CallbackQuery):
    await call.message.edit_text(
        text='O\'zgartirmoqchi bo\'lgan usernameni kiriting'
    )
    await UserProfile.edit_username.set()


@dp.callback_query_handler(F.data == 'phone_uz', state='*')
async def change_phone_uz(call: types.CallbackQuery):
    await call.message.edit_text(
        text='O\'zgartirmoqchi bo\'lgan telefon raqamingizni 998XXXXXXXXX shaklida kiriting'
    )
    await UserProfile.edit_phone.set()


@dp.message_handler(state=UserProfile.edit_name)
async def edit_name_uz(message: types.Message, state: FSMContext):
    await db.update_user_fullname(full_name=message.text, telegram_id=message.from_user.id)
    await state.finish()
    await message.answer(
        text=f'Ism o\'zgartirildi'
    )


@dp.message_handler(state=UserProfile.edit_phone)
async def edit_phone_uz(message: types.Message, state: FSMContext):
    if message.text.isdigit():
        phone = f'+{message.text}'
        await db.update_user_phone(phone=phone, telegram_id=message.from_user.id)
        await state.finish()
        await message.answer(
            text=f'Telefon raqami o\'zgartirildi'
        )
    else:
        await message.answer(
            text=f'Iltimos, faqat namunada ko\'rsatilganidek raqam kiriting!'
        )


@dp.message_handler(state=UserProfile.edit_username)
async def edit_username_uz(message: types.Message, state: FSMContext):
    link_prefixes = ['@', 'http://', 'https://', 't.me']

    if any(prefix in message.text for prefix in link_prefixes):
        await message.answer(
            text='Iltimos, link bor matn kiritmang!'
        )
    else:
        username = f'@{message.text}'
        await db.update_user_username(username=username, telegram_id=message.from_user.id)
        await state.finish()
        await message.answer(
            text=f'Username o\'zgartirildi'
        )
