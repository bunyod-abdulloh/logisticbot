from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.default.form_and_main_buttons import menu_uz_buttons
from keyboards.default.ru.form_and_main_buttons import menu_ru_buttons
from keyboards.inline.menu_keyboards import select_language_buttons

from loader import dp, db


@dp.message_handler(CommandStart(), state='*')
async def bot_start(message: types.Message, state: FSMContext):
    await state.finish()
    user = await db.select_user(telegram_id=message.from_user.id)
    if user:
        if user[5] == 'uz':
            await message.answer(
                text='🏡 Bosh sahifa',
                reply_markup=menu_uz_buttons
            )
        elif user[5] == 'ru':
            await message.answer(
                text='Главное меню',
                reply_markup=menu_ru_buttons
            )
    else:
        await message.answer(
            text="Tilni tanlang:"
                 "\n\nВыберите язык:",
            reply_markup=select_language_buttons
        )
