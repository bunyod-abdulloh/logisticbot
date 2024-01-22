from aiogram import types
from aiogram.dispatcher import FSMContext
from keyboards.default.form_and_main_buttons import menu_uz_buttons
from keyboards.inline.trucks_cars_main_buttons import trucks_cars_buttons
from loader import dp


@dp.message_handler(state='*', content_types=['photo'])
async def get_photo_id(message: types.Message):
    await message.answer(
        text=f"<code>{message.photo[-1].file_id}</code>"
    )


@dp.message_handler(text='🚙 Avtomobillar', state='*')
async def cars_uz_main(message: types.Message):
    await message.answer_photo(
        photo='AgACAgIAAxkBAAEBCldlrlm4LwgJDih6EqGeXVVx44lDlAAC6NQxG2uPcEl0-5SpejC_iwEAAwIAA20AAzQE',
        caption='Avtomobil turini tanlang',
        reply_markup=trucks_cars_buttons
    )


@dp.message_handler(text='🏡 Bosh sahifa', state='*')
async def main_menu_uz(message: types.Message, state: FSMContext):
    await message.answer(
        text=message.text,
        reply_markup=menu_uz_buttons
    )
    await state.finish()
