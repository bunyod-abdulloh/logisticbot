from aiogram import types
from magic_filter import F

from keyboards.default.logistic_cbuttons import logistic_main_cbuttons
from keyboards.inline.logistic_ibuttons import type_transport_ibuttons
from loader import dp

type_of_transport = 'Qaysi transport turidan foydalanmoqchisiz?'


@dp.message_handler(F.text == '📦 Logistika xizmati', state='*')
async def logistic_uz_main_cmd(message: types.Message):
    await message.answer(
        text=message.text, reply_markup=logistic_main_cbuttons()
    )


@dp.message_handler(F.text == 'Mustaqil Davlatlar Hamdo\'stiligi (MDH)', state='*')
async def logistic_uz_main_cmd(message: types.Message):
    await message.answer(
        text=type_of_transport, reply_markup=type_transport_ibuttons(
            region='MDH'
        )
    )


@dp.message_handler(F.text == 'Yevropa', state='*')
async def logistic_uz_main_cmd(message: types.Message):
    await message.answer(
        text=type_of_transport, reply_markup=logistic_main_cbuttons()
    )


@dp.message_handler(F.text == 'Osiyo', state='*')
async def logistic_uz_main_cmd(message: types.Message):
    await message.answer(
        text=type_of_transport, reply_markup=logistic_main_cbuttons()
    )


@dp.message_handler(F.text == 'Xitoy', state='*')
async def logistic_uz_main_cmd(message: types.Message):
    await message.answer(
        text=type_of_transport, reply_markup=logistic_main_cbuttons()
    )
