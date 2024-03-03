from aiogram import types
from aiogram.dispatcher import FSMContext
from magic_filter import F

from data.config import ADMINS
from loader import dp, db, bot
from states.ru.users import UserFeedbackRu


@dp.callback_query_handler(F.data == 'feedback_ru_photo')
async def feedback_first_ru(call: types.CallbackQuery):
    await call.message.edit_text(
        text='Отправьте фото'
    )
    await UserFeedbackRu.photo.set()


@dp.callback_query_handler(F.data == 'feedback_ru_comment')
async def feedback_second_ru(call: types.CallbackQuery):
    await call.message.edit_text(
        text='Введите свое сообщение'
    )
    await UserFeedbackRu.text.set()


@dp.message_handler(state=UserFeedbackRu.photo, content_types=['photo'])
async def feedback_ru_get_photo(message: types.Message, state: FSMContext):
    telegram_id = message.from_user.id
    file_id = message.photo[-1].file_id
    caption = message.caption
    id_ = await db.add_feedback(
        telegram_id=telegram_id, photo_id=file_id, caption=caption, text=None
    )
    await state.update_data(
        feedback_id=id_[0]
    )
    await message.answer_photo(
        photo=file_id, caption=caption
    )
    await message.answer(
        text='Введите свой комментарий к изображению'
    )
    await UserFeedbackRu.photo_text.set()


@dp.message_handler(state=UserFeedbackRu.photo_text, content_types=['text'])
async def feedback_ru_get_text(message: types.Message, state: FSMContext):
    data = await state.get_data()
    id_ = data['feedback_id']
    telegram_id = message.from_user.id
    user = await db.select_user(
        telegram_id=telegram_id
    )
    feedback = await db.select_feedback_by_id(
        id_=id_
    )
    await db.update_feedback_text(
        text=message.text, id_=id_
    )
    for admin in ADMINS:
        await bot.send_photo(
            chat_id=admin,
            photo=feedback[3],
            caption=f'ID |{message.from_user.id}|\n\n{feedback[4]}'
                    f'\n\n#fikr_va_mulohazalar'
                    f'\n\n<b>Sana:</b> {feedback[1]}'
                    f'\n<b>Bo\'lim:</b> 🎙 Fikr va mulohazalar'
                    f'\n\n<b>Ism:</b> {user[2]}'
                    f'\n<b>Username:</b> {user[3]}'
                    f'\n<b>Telefon raqam:</b> {user[4]}'
                    f'\n<b>Foydalanuvchi izohi:</b> {message.text}'
        )
    await message.answer(
        text='✅ Ваше сообщение принято!'
    )
    await state.finish()


@dp.message_handler(state=UserFeedbackRu.text)
async def user_feedback_uz(message: types.Message, state: FSMContext):
    telegram_id = message.from_user.id
    feedback = await db.add_feedback(
        telegram_id=telegram_id, photo_id=None, caption=None, text=message.text
    )
    user = await db.select_user(
        telegram_id=telegram_id
    )
    for admin in ADMINS:
        await bot.send_message(
                chat_id=admin,
                text=f'ID |{message.from_user.id}|\n\n#fikr_va_mulohazalar'
                     f'\n\n<b>Sana:</b> {feedback[1]}'
                     f'\n<b>Bo\'lim:</b> 🎙 Fikr va mulohazalar'
                     f'\n\n<b>Ism:</b> {user[2]}'
                     f'\n<b>Username:</b> {user[3]}'
                     f'\n<b>Telefon raqam:</b> {user[4]}'
                     f'\n<b>Foydalanuvchi savoli:</b> {message.text}'
            )
    await message.answer(
        text='✅ Ваше сообщение принято!'
    )
    await state.finish()
