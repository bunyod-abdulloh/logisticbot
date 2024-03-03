from aiogram import types
from aiogram.dispatcher import FSMContext
from magic_filter import F

from filters.private import IsPrivate
from keyboards.inline.buy_ibuttons import buy_uz_ikeys
from loader import dp
from states.user_states import UserBuy


@dp.message_handler(IsPrivate(), F.text == 'Uskunalar', state='*')
async def buy_uz_main_equipment(message: types.Message):
    await message.answer(
        text='Tugmalardan birini tanlang', reply_markup=buy_uz_ikeys
    )
    await UserBuy.equipment.set()


@dp.message_handler(IsPrivate(), F.text == 'Xom ashyo', state='*')
async def buy_uz_main_raw(message: types.Message):
    await message.answer(
        text='Tugmalardan birini tanlang', reply_markup=buy_uz_ikeys
    )
    await UserBuy.raw.set()


@dp.message_handler(IsPrivate(), F.text == 'Kichik uskunalar', state='*')
async def buy_uz_main_sequipment(message: types.Message):
    await message.answer(
        text='Tugmalardan birini tanlang', reply_markup=buy_uz_ikeys
    )
    await UserBuy.small_equipment.set()
