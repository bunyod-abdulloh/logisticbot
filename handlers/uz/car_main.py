from aiogram import types

from keyboards.inline.car_ibuttons import get_car_buttons
from keyboards.inline.trucks_cars_main_buttons import trucks_cars_buttons
from loader import dp, bot


@dp.callback_query_handler(text='car_uz', state='*')
async def cars_main_cmd(call: types.CallbackQuery):
    await call.message.delete()
    media = types.MediaGroup()
    media.attach_photo(photo='AgACAgIAAxkBAAEBCldlrlm4LwgJDih6EqGeXVVx44lDlAAC6NQxG2uPcEl0-5SpejC_iwEAAwIAA20AAzQE')
    media.attach_photo(photo='AgACAgIAAxkBAAEBCldlrlm4LwgJDih6EqGeXVVx44lDlAAC6NQxG2uPcEl0-5SpejC_iwEAAwIAA20AAzQE')
    media.attach_photo(photo='AgACAgIAAxkBAAEBCldlrlm4LwgJDih6EqGeXVVx44lDlAAC6NQxG2uPcEl0-5SpejC_iwEAAwIAA20AAzQE')
    media.attach_photo(photo='AgACAgIAAxkBAAEBCldlrlm4LwgJDih6EqGeXVVx44lDlAAC6NQxG2uPcEl0-5SpejC_iwEAAwIAA20AAzQE',
                       )
    await call.message.answer_media_group(
        media=media
    )
    await call.message.answer(
        text='Avtomobil markasini tanlang', reply_markup=await get_car_buttons()
    )
    await call.message.answer_photo(
        photo='AgACAgIAAxkBAAEBCldlrlm4LwgJDih6EqGeXVVx44lDlAAC6NQxG2uPcEl0-5SpejC_iwEAAwIAA20AAzQE',
        caption='Avtomobil markasini tanlang', reply_markup=await get_car_buttons()
    )


@dp.callback_query_handler(text='back_car_uz', state='*')
async def back_car_menu(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer_photo(
        photo='AgACAgIAAxkBAAEBCldlrlm4LwgJDih6EqGeXVVx44lDlAAC6NQxG2uPcEl0-5SpejC_iwEAAwIAA20AAzQE',
        caption='Avtomobil turini tanlang',
        reply_markup=trucks_cars_buttons
    )
