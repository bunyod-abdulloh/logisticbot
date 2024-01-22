from aiogram import types

from loader import dp, db
from states.user_states import UserForms


@dp.callback_query_handler(text='uz', state='*')
async def get_uz_main(call: types.CallbackQuery):
    telegram_id = call.from_user.id
    await db.add_user(
        telegram_id=telegram_id, language=call.data
    )
    await call.message.edit_text(
        text="Ismingizni kiriting:"
    )
    await UserForms.full_name.set()
