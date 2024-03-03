from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp, db, bot
from states.admin_states import Admin


@dp.message_handler(state=Admin.send_to_users)
async def send_message_to_users(message: types.Message, state: FSMContext):
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(types.InlineKeyboardButton(text='Yuborish', callback_data='admin_send_message'),
                 types.InlineKeyboardButton(text='Qayta kiritish', callback_data='admin_re_enter'))
    await state.update_data(
        admin_text=message.text
    )
    await message.answer(
        text='Habaringiz qabul qilindi! Yuborasizmi?', reply_markup=keyboard
    )
    await Admin.check_send.set()


@dp.callback_query_handler(state=Admin.check_send)
async def admin_check_send(call: types.CallbackQuery, state: FSMContext):
    message = await db.select_admins_sql()
    if message[0][2] is True:
        await call.message.answer(
            text='Habar yuborilmoqda!'
        )
    else:
        if call.data == 'admin_send_message':
            await db.update_send_message(send_message=True)
            data = await state.get_data()
            text = data['admin_text']
            all_users = await db.select_all_users()
            c = 0
            d = 0
            for user in all_users:
                try:
                    c += 1
                    await bot.send_message(
                        chat_id=user[1],
                        text=text
                    )
                except Exception:
                    d += 1
                    await db.delete_user(telegram_id=user[1])
            await call.message.answer(
                text=f'Habar {c} ta foydalanuvchiga yuborildi!'
                     f'\n\nACTIVE: {c}\nBLOCK: {d}'
            )
            # await db.delete_users()
            await state.finish()
            await db.update_send_message(send_message=False)
        elif call.data == 'admin_re_enter':
            await call.message.answer(
                text='Habaringizni qayta kiriting!'
            )
            await Admin.send_to_users.set()
