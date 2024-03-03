from aiogram import types
from aiogram.dispatcher import FSMContext
from magic_filter import F

from keyboards.default.form_and_main_buttons import menu_uz_buttons
from loader import dp, db
from states.ru.users import UserProfileRu


@dp.callback_query_handler(F.data == 'language_ru', state='*')
async def change_language_ru(call: types.CallbackQuery):
    await db.update_user_language(language='uz', telegram_id=call.from_user.id)
    await call.message.answer(
        text=f'O\'zbek tili tanlandi',
        reply_markup=menu_uz_buttons
    )


@dp.callback_query_handler(F.data == 'name_ru', state='*')
async def change_name_ru(call: types.CallbackQuery):
    await call.message.edit_text(
        text='Введите имя,на которое хотите изменить'
    )
    await UserProfileRu.edit_name.set()


@dp.callback_query_handler(F.data == 'username_ru', state='*')
async def change_username_ru(call: types.CallbackQuery):
    await call.message.edit_text(
        text='Введите имя пользователя, на которое хотите изменить'
    )
    await UserProfileRu.edit_username.set()


@dp.callback_query_handler(F.data == 'phone_ru', state='*')
async def change_phone_ru(call: types.CallbackQuery):
    await call.message.edit_text(
        text='Введите номер телефона, который вы хотите изменить, в форму 998XXXXXXXXX'
    )
    await UserProfileRu.edit_phone.set()


@dp.message_handler(state=UserProfileRu.edit_name)
async def edit_name_ru(message: types.Message, state: FSMContext):
    await state.finish()
    await db.update_user_fullname(full_name=message.text, telegram_id=message.from_user.id)
    await message.answer(
        text=f'Имя изменено'
    )


@dp.message_handler(state=UserProfileRu.edit_phone)
async def edit_phone_ru(message: types.Message, state: FSMContext):
    if message.text.isdigit():
        phone = f'+{message.text}'
        await db.update_user_phone(phone=phone, telegram_id=message.from_user.id)
        await state.finish()
        await message.answer(
            text=f'Номер телефона изменен'
        )
    else:
        await message.answer(
            text='Пожалуйста, введите число!'
        )


@dp.message_handler(state=UserProfileRu.edit_username)
async def edit_username_ru(message: types.Message, state: FSMContext):
    link_prefixes = ['@', 'http://', 'https://', 't.me']

    if any(prefix in message.text for prefix in link_prefixes):
        await message.answer(
            text='Пожалуйста, не введите текст, в котором есть ссылка!'
        )
    else:
        username = f'@{message.text}'
        await db.update_user_username(username=username, telegram_id=message.from_user.id)
        await state.finish()
        await message.answer(
            text=f'Имя пользователя изменено'
        )
