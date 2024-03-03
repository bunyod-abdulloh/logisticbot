from aiogram import types
from aiogram.dispatcher import FSMContext
from magic_filter import F

from data.config import LOGISTICS_GROUP
from handlers.ru.logistic_main import type_of_transport_ru
from keyboards.inline.ru.logistic_ibuttons import transport_ibuttons_ru
from loader import dp, db, bot
from states.ru.users import LogisticCISRu


@dp.callback_query_handler(F.data == 'logistic_cis_ru', state='*')
async def logistic_ru_main_cis(call: types.CallbackQuery):
    await call.message.edit_text(
        text='1. Тип оплаты'
    )
    await LogisticCISRu.one.set()


@dp.callback_query_handler(F.data == 'call_cis_ru', state='*')
async def logistic_ru_call_cis(call: types.CallbackQuery):
    telegram_id = call.from_user.id
    id_ = await db.add_reference_logistic(
        telegram_id=telegram_id, logistic_region='MDH', logistic_type='qayta_qongiroq'
    )
    user = await db.select_user(telegram_id=telegram_id)
    text = (f'ID |{telegram_id}|\n\n#logistika_qayta_qongiroq'
            f'\n\nFoydalanuvchi qayta qo\'ng\'iroqni kutmoqda!'
            f'\n\n<b>Sana:</b> {id_[1]}'
            f'\n<b>Bo\'lim:</b> 📦 Logistika xizmati'
            f'\n\n<b>So\'rov raqami:</b> {id_[0]}'
            f'\n<b>Ism:</b> {user[2]}'
            f'\n<b>Username:</b> {user[3]}'
            f'\n<b>Telefon raqam:</b> {user[4]}'
            f'\n<b>Tanlangan davlat:</b> MDH')
    await bot.send_message(
        chat_id=LOGISTICS_GROUP, text=text
    )
    await call.answer(
        text='Ваша заявка принята! Наши операторы скоро свяжутся с вами!',
        show_alert=True
    )
    await call.message.delete()


@dp.message_handler(state=LogisticCISRu.one)
async def cis_ru_one(message: types.Message, state: FSMContext):
    await state.update_data(
        cis_one=message.text
    )
    await message.answer(
        text='2. Место затаможки'
    )
    await LogisticCISRu.two.set()


@dp.message_handler(state=LogisticCISRu.two)
async def cis_ru_two(message: types.Message, state: FSMContext):
    await state.update_data(
        cis_two=message.text
    )
    await message.answer(
        text='3. Место растаможки '
    )
    await LogisticCISRu.three.set()


@dp.message_handler(state=LogisticCISRu.three)
async def cis_ru_three(message: types.Message, state: FSMContext):
    await state.update_data(
        cis_three=message.text
    )
    await message.answer(
        text='4. Место высадки'
    )
    await LogisticCISRu.four.set()


@dp.message_handler(state=LogisticCISRu.four)
async def cis_ru_four(message: types.Message, state: FSMContext):
    await state.update_data(
        cis_four=message.text
    )
    await message.answer(
        text='5. Название груза'
    )
    await LogisticCISRu.five.set()


@dp.message_handler(state=LogisticCISRu.five)
async def cis_ru_five(message: types.Message, state: FSMContext):
    await state.update_data(
        cis_five=message.text
    )
    await message.answer(
        text='6. Вес брутто и нетто'
    )
    await LogisticCISRu.six.set()


@dp.message_handler(state=LogisticCISRu.six)
async def cis_ru_six(message: types.Message, state: FSMContext):
    await state.update_data(
        cis_six=message.text
    )
    await message.answer(
        text='7. Размеры послепакетной загрузки'
    )
    await LogisticCISRu.seven.set()


@dp.message_handler(state=LogisticCISRu.seven)
async def cis_ru_seven(message: types.Message, state: FSMContext):
    await state.update_data(
        cis_seven=message.text
    )
    await message.answer(
        text='8. Тип упаковки'
    )
    await LogisticCISRu.eight.set()


@dp.message_handler(state=LogisticCISRu.eight)
async def cis_ru_eight(message: types.Message, state: FSMContext):
    await state.update_data(
        cis_eight=message.text
    )
    await message.answer(
        text='9. Отправить фото груза перед упаковкой'
    )
    await LogisticCISRu.nine.set()


@dp.message_handler(state=LogisticCISRu.nine, content_types=['photo', 'text'])
async def cis_ru_nine(message: types.Message, state: FSMContext):
    if message.content_type == 'photo':
        await state.update_data(
            cis_first_photo=message.photo[1].file_id
        )
    else:
        pass
    await message.answer(
        text='10. Отправить фото груза перед упаковкой'
    )
    await LogisticCISRu.ten.set()


@dp.message_handler(state=LogisticCISRu.ten, content_types=['photo', 'text'])
async def cis_ru_ten(message: types.Message, state: FSMContext):
    telegram_id = message.from_user.id
    data = await state.get_data()
    one = data['cis_one']
    two = data['cis_two']
    three = data['cis_three']
    four = data['cis_four']
    five = data['cis_five']
    six = data['cis_six']
    seven = data['cis_seven']
    eight = data['cis_eight']
    text_logistic = (f'1. To\'lov turi: {one}'
                     f'\n2. Zatamojka joyi: {two}'
                     f'\n3. Rastamojning nomi: {three}'
                     f'\n4. Tushirish joyi: {four}'
                     f'\n5. Yukning nomi: {five}'
                     f'\n6. Yalpi va sof vazn: {six}'
                     f'\n7. Qadoqdan keyingi yukning o\'lchamlari: {seven}'
                     f'\n8. Qadoq turi: {eight}'
                     )
    if message.content_type == 'photo':
        second_photo = message.photo[-1].file_id
        if 'cis_first_photo' in data.items():
            first_photo = data['cis_first_photo']
            id_ = await db.add_text_logistic(
                telegram_id=telegram_id, region='MDH', text=text_logistic,
                first_photo=first_photo, second_photo=second_photo
            )
        else:
            id_ = await db.add_text_logistic(
                telegram_id=telegram_id, region='MDH', text=text_logistic,
                first_photo=None, second_photo=None
            )
    else:
        id_ = await db.add_text_logistic(
            telegram_id=telegram_id, region='MDH', text=text_logistic, first_photo=None, second_photo=None
        )

    await state.finish()
    await message.answer(
        text=type_of_transport_ru, reply_markup=transport_ibuttons_ru(
            region=f'MDH_{id_[0]}'
        )
    )
