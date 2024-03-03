from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from magic_filter import F

from data.config import ALL_GROUPS
from filters.private import IsPrivate
from keyboards.default.form_and_main_buttons import menu_uz_buttons
from loader import dp, bot, db


@dp.message_handler(IsPrivate(), F.text == '↩️ Bosh menyuga qaytish', state='*')
async def back_to_main_menu(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer(
        text='Bosh menyu',
        reply_markup=menu_uz_buttons
    )


@dp.message_handler(Command('block'), state='*', chat_id=ALL_GROUPS)
async def menu_uz_(message: types.Message):
    user_id = str()
    try:
        content_type = message.reply_to_message.content_type
        if content_type == 'text':
            user_id = message.reply_to_message.text.split('|')[1]
        elif content_type == 'photo':
            user_id = message.reply_to_message.caption.split('|')[1]
        await bot.send_message(
            chat_id=user_id,
            text='Sizga botdan foydalanish bo\'yicha cheklov qo\'yildi!',
            reply_markup=types.ReplyKeyboardRemove()
        )
        await db.update_user_blocks(
            blocked_user=user_id, telegram_none=None, telegram_id=user_id
        )
        await message.answer(
            text=f'{user_id} ID raqamli foydalanuvchi bloklandi!'
        )
    except Exception:
        pass
