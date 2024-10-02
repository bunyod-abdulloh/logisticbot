import os

import pandas as pd
from aiogram import types
from aiogram.dispatcher import FSMContext
from magic_filter import F

from filters.private import IsPrivate
from loader import dp, db, bot

from states.admin_states import Admin

SAVE_PATH = 'downloads/'


async def download_and_save_file(file_id: str, save_path: str):
    file_info = await bot.get_file(file_id)
    file_path = os.path.join(save_path, file_info.file_path)
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    await bot.download_file(file_info.file_path, file_path)
    return file_path


@dp.message_handler(F.photo)
async def get_photo_id_rtr(message: types.Message):
    await message.answer(
        text=f"<code>{message.photo[-1].file_id}</code>"
    )


@dp.message_handler(IsPrivate(), F.text == "Excel shaklda qo\'shish", state="*")
async def add_cars_main_uz(message: types.Message):
    await message.answer(
        text='Excel hujjatni yuboring:'
    )
    await Admin.add_cars_catalog.set()


@dp.message_handler(state=Admin.add_cars_catalog, content_types=['document'])
async def get_document(message: types.Message):
    file_path = await download_and_save_file(message.document.file_id, SAVE_PATH)
    try:
        df = pd.read_excel(file_path, sheet_name=0)
        c = 0
        cars_table = df.values[0:]
        for n in cars_table:
            c += 1
            await db.add_car(
                main_photo=n[0], brand=n[1], model=n[2], price=n[3], file_id=n[4]
            )
        await message.answer(
            text=f'Jami {c} ta mashina ma\'lumotlari bot bazasiga yuklandi!'
        )
    except Exception as e:
        await db.delete_cars()
        await message.answer(
            text=f'{e}'
        )
    os.remove(file_path)


@dp.message_handler(IsPrivate(), F.text == "🔙 Ortga", state="*")
async def a_a_s_back(message: types.Message, state: FSMContext):
    await message.answer(
        text=message.text
    )
    await state.finish()
