from aiogram import types
from magic_filter import F

from filters.private import IsPrivate
from keyboards.inline.ru.buy_ibuttons import buy_ru_ikeys
from loader import dp
from states.ru.users import UserBuyRu


@dp.message_handler(IsPrivate(), F.text == 'Оборудование', state='*')
async def buy_ru_main_equipment(message: types.Message):
    await message.answer(
        text='Выберите одну из кнопок', reply_markup=buy_ru_ikeys
    )
    await UserBuyRu.equipment.set()


@dp.message_handler(IsPrivate(), F.text == 'Сырьё', state='*')
async def buy_ru_main_raw(message: types.Message):
    await message.answer(
        text='Выберите одну из кнопок', reply_markup=buy_ru_ikeys
    )
    await UserBuyRu.raw.set()


@dp.message_handler(IsPrivate(), F.text == 'Малые оборудование', state='*')
async def buy_ru_main_equipment(message: types.Message):
    await message.answer(
        text='Выберите одну из кнопок', reply_markup=buy_ru_ikeys
    )
    await UserBuyRu.small_equipment.set()
