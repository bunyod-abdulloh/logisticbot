from aiogram import types
from aiogram.dispatcher import FSMContext
from magic_filter import F

from filters.private import IsPrivate
from keyboards.default.ru.form_and_main_buttons import menu_ru_buttons
from keyboards.default.ru.logistic_cbuttons import logistic_main_cbuttons_ru
from loader import dp


@dp.callback_query_handler(F.data == 'back_main_ru', state='*')
async def back_main_ru_cmd(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    await call.message.answer(
        text='Главное меню', reply_markup=menu_ru_buttons
    )
    await state.finish()


@dp.callback_query_handler(F.data == 'back_logistic_ru', state='*')
async def back_logistic_ru(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    await call.message.answer(
        text='Логистические услуги', reply_markup=logistic_main_cbuttons_ru()
    )
    await state.finish()


@dp.message_handler(IsPrivate(), F.text == '↩️ назад в Главное меню', state='*')
async def back_main_ru_custom(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer(
        text='Главное меню', reply_markup=menu_ru_buttons
    )
