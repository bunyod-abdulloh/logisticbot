from aiogram import types
from aiogram.dispatcher import FSMContext
from magic_filter import F

from data.config import LOGISTICS_GROUP
from handlers.ru.logistic_main import type_of_transport_ru
from keyboards.inline.ru.logistic_ibuttons import transport_ibuttons_ru
from loader import dp, db, bot
from states.ru.users import LogisticAsiaRu


@dp.callback_query_handler(F.data == 'logistic_asia_ru', state='*')
async def logistic_ru_main_asia(call: types.CallbackQuery):
    await call.message.edit_text(
        text='1. Тип оплаты'
    )
    await LogisticAsiaRu.one.set()


@dp.callback_query_handler(F.data == 'call_asia_ru', state='*')
async def logistic_ru_call_asia(call: types.CallbackQuery):
    telegram_id = call.from_user.id
    id_ = await db.add_reference_logistic(
        telegram_id=telegram_id, logistic_region='Osiyo', logistic_type='qayta_qongiroq'
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
            f'\n<b>Tanlangan davlat:</b> Osiyo')
    await bot.send_message(
        chat_id=LOGISTICS_GROUP, text=text
    )
    await call.answer(
        text='Ваша заявка принята! Наши операторы скоро свяжутся с вами!',
        show_alert=True
    )
    await call.message.delete()


@dp.message_handler(state=LogisticAsiaRu.one)
async def logistic_first_ru(message: types.Message, state: FSMContext):
    await state.update_data(
        asia_one=message.text
    )
    await message.answer(
        text='2. Место затаможки'
    )
    await LogisticAsiaRu.two.set()


@dp.message_handler(state=LogisticAsiaRu.two)
async def logistic_second_ru(message: types.Message, state: FSMContext):
    await state.update_data(
        asia_two=message.text
    )
    await message.answer(
        text='3. Место растаможки '
    )
    await LogisticAsiaRu.three.set()


@dp.message_handler(state=LogisticAsiaRu.three)
async def logistic_three_ru(message: types.Message, state: FSMContext):
    await state.update_data(
        asia_three=message.text
    )
    await message.answer(
        text='4. Место высадки'
    )
    await LogisticAsiaRu.four.set()


@dp.message_handler(state=LogisticAsiaRu.four)
async def logistic_four_ru(message: types.Message, state: FSMContext):
    await state.update_data(
        asia_four=message.text
    )
    await message.answer(
        text='5. Название груза'
    )
    await LogisticAsiaRu.five.set()


@dp.message_handler(state=LogisticAsiaRu.five)
async def logistic_five_ru(message: types.Message, state: FSMContext):
    await state.update_data(
        asia_five=message.text
    )
    await message.answer(
        text='6. Вес брутто и нетто'
    )
    await LogisticAsiaRu.six.set()


@dp.message_handler(state=LogisticAsiaRu.six)
async def logistic_six_ru(message: types.Message, state: FSMContext):
    await state.update_data(
        asia_six=message.text
    )
    await message.answer(
        text='7. Размеры послепакетной загрузки'
    )
    await LogisticAsiaRu.seven.set()


@dp.message_handler(state=LogisticAsiaRu.seven)
async def logistic_seven_ru(message: types.Message, state: FSMContext):
    await state.update_data(
        asia_seven=message.text
    )
    await message.answer(
        text='8. Тип упаковки'
    )
    await LogisticAsiaRu.eight.set()


@dp.message_handler(state=LogisticAsiaRu.eight)
async def logistic_eight_ru(message: types.Message, state: FSMContext):
    await state.update_data(
        asia_eight=message.text
    )
    await message.answer(
        text='9. Отправить фото груза перед упаковкой'
    )
    await LogisticAsiaRu.nine.set()


@dp.message_handler(state=LogisticAsiaRu.nine, content_types=['photo', 'text'])
async def logistic_nine_ru(message: types.Message, state: FSMContext):
    if message.content_type == 'photo':
        await state.update_data(
            asia_first_photo=message.photo[1].file_id
        )
    else:
        pass
    await message.answer(
        text='10. Отправить фотографию груза после упаковки'
    )
    await LogisticAsiaRu.ten.set()


@dp.message_handler(state=LogisticAsiaRu.ten, content_types=['photo', 'text'])
async def logistic_ten_ru(message: types.Message, state: FSMContext):
    telegram_id = message.from_user.id
    data = await state.get_data()
    one = data['asia_one']
    two = data['asia_two']
    three = data['asia_three']
    four = data['asia_four']
    five = data['asia_five']
    six = data['asia_six']
    seven = data['asia_seven']
    eight = data['asia_eight']
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
        if 'asia_first_photo' in data.items():
            first_photo = data['asia_first_photo']
            id_ = await db.add_text_logistic(
                telegram_id=telegram_id, region='Osiyo', text=text_logistic,
                first_photo=first_photo, second_photo=second_photo
            )
        else:
            id_ = await db.add_text_logistic(
                telegram_id=telegram_id, region='Osiyo', text=text_logistic, first_photo=None, second_photo=None
            )
    else:
        id_ = await db.add_text_logistic(
            telegram_id=telegram_id, region='Osiyo', text=text_logistic, first_photo=None, second_photo=None
        )
    await state.finish()
    await message.answer(
        text=type_of_transport_ru, reply_markup=transport_ibuttons_ru(
            region=f'Osiyo_{id_[0]}'
        )
    )
