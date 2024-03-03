from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.default.ru.form_and_main_buttons import ru_get_contact, menu_ru_buttons
from loader import dp, db
from states.ru.users import UserFormsRu


@dp.message_handler(state=UserFormsRu.full_name)
async def forms_ru_first(message: types.Message):
    if message.text.isalpha():
        await db.update_user_fullname(
            full_name=message.text, telegram_id=message.from_user.id
        )
        await message.answer(
            text='Отправьте свой номер с помощью кнопки ниже:',
            reply_markup=ru_get_contact
        )
        await UserFormsRu.phone.set()
    else:
        await message.answer(
            text='Пожалуйста, введите только буквы'
        )


@dp.message_handler(state=UserFormsRu.phone, content_types=['contact'])
async def forms_ru_second(message: types.Message, state: FSMContext):
    telegram_id = message.from_user.id
    username = message.from_user.username
    phone = message.contact.phone_number
    if phone.isdigit():
        phone_ = f"+{phone}"
    else:
        phone_ = phone
    await db.update_user_phone_username(
        phone=phone_, username=f'@{username}', telegram_id=telegram_id
    )
    await message.answer(
        text='Вы успешно зарегистрировались!',
        reply_markup=menu_ru_buttons
    )
    await state.finish()
