from aiogram import types
from aiogram.dispatcher import FSMContext
from magic_filter import F

from keyboards.default.form_and_main_buttons import menu_uz_buttons
from keyboards.default.logistic_cbuttons import logistic_main_cbuttons
from loader import dp


@dp.callback_query_handler(F.data == 'back_main_uz', state='*')
async def back_main_uz_cmd(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    await call.message.answer(
        text='Bosh sahifa', reply_markup=menu_uz_buttons
    )
    await state.finish()


@dp.callback_query_handler(F.data == 'back_logistic_uz', state='*')
async def back_logistic_uz(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    await call.message.answer(
        text='Logistika hizmati bo\'limi', reply_markup=logistic_main_cbuttons()
    )
    await state.finish()
