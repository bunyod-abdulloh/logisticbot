from aiogram import types
from aiogram.dispatcher import FSMContext
from magic_filter import F

from data.config import LOGISTICS_GROUP
from handlers.ru.logistic_main import type_of_transport_ru
from keyboards.inline.ru.logistic_ibuttons import transport_ibuttons_ru
from loader import dp, db, bot
from states.ru.users import LogisticUSARu


@dp.callback_query_handler(F.data == 'logistic_usa_ru', state='*')
async def logistic_uz_main_usa(call: types.CallbackQuery):
    await call.message.edit_text(
        text='1. Тип оплаты'
    )
    await LogisticUSARu.one.set()


@dp.callback_query_handler(F.data == 'call_usa_ru', state='*')
async def logistic_uz_call_usa(call: types.CallbackQuery):
    telegram_id = call.from_user.id
    id_ = await db.add_reference_logistic(
        telegram_id=telegram_id, logistic_type='qayta_qongiroq', logistic_region='AQSH'
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
            f'\n<b>Tanlangan davlat:</b> AQSH')
    await bot.send_message(
        chat_id=LOGISTICS_GROUP, text=text
    )
    await call.answer(
        text='Ваша заявка принята! Наши операторы скоро свяжутся с вами!',
        show_alert=True
    )
    await call.message.delete()


@dp.message_handler(state=LogisticUSARu.one)
async def uz_logistic_usa_one(message: types.Message, state: FSMContext):
    await state.update_data(
        usa_one=message.text
    )
    await message.answer(
        text='2. Место затаможки'
    )
    await LogisticUSARu.two.set()


@dp.message_handler(state=LogisticUSARu.two)
async def uz_logistic_usa_two(message: types.Message, state: FSMContext):
    await state.update_data(
        usa_two=message.text
    )
    await message.answer(
        text='3. Место растаможки '
    )
    await LogisticUSARu.three.set()


@dp.message_handler(state=LogisticUSARu.three)
async def uz_logistic_usa_three(message: types.Message, state: FSMContext):
    await state.update_data(
        usa_three=message.text
    )
    await message.answer(
        text='4. Место высадки'
    )
    await LogisticUSARu.four.set()


@dp.message_handler(state=LogisticUSARu.four)
async def uz_logistic_usa_four(message: types.Message, state: FSMContext):
    await state.update_data(
        usa_four=message.text
    )
    await message.answer(
        text='5. Название груза'
    )
    await LogisticUSARu.five.set()


@dp.message_handler(state=LogisticUSARu.five)
async def uz_logistic_usa_five(message: types.Message, state: FSMContext):
    await state.update_data(
        usa_five=message.text
    )
    await message.answer(
        text='6. Вес брутто и нетто'
    )
    await LogisticUSARu.six.set()


@dp.message_handler(state=LogisticUSARu.six)
async def uz_logistic_usa_six(message: types.Message, state: FSMContext):
    await state.update_data(
        usa_six=message.text
    )
    await message.answer(
        text='7. Размеры послепакетной загрузки'
    )
    await LogisticUSARu.seven.set()


@dp.message_handler(state=LogisticUSARu.seven)
async def uz_logistic_usa_seven(message: types.Message, state: FSMContext):
    await state.update_data(
        usa_seven=message.text
    )
    await message.answer(
        text='8. Тип упаковки'
    )
    await LogisticUSARu.eight.set()


@dp.message_handler(state=LogisticUSARu.eight)
async def uz_logistic_usa_eight(message: types.Message, state: FSMContext):
    await state.update_data(
        usa_eight=message.text
    )
    await message.answer(
        text='9. Отправить фото груза перед упаковкой'
    )
    await LogisticUSARu.nine.set()


@dp.message_handler(state=LogisticUSARu.nine, content_types=['photo', 'text'])
async def uz_logistic_usa_nine(message: types.Message, state: FSMContext):
    if message.content_type == 'photo':
        await state.update_data(
            usa_first_photo=message.photo[1].file_id
        )
    else:
        pass
    await message.answer(
        text='10. Отправить фотографию груза после упаковки'
    )
    await LogisticUSARu.ten.set()


@dp.message_handler(state=LogisticUSARu.ten, content_types=['photo', 'text'])
async def uz_logistic_usa_ten(message: types.Message, state: FSMContext):
    telegram_id = message.from_user.id
    data = await state.get_data()
    one = data['usa_one']
    two = data['usa_two']
    three = data['usa_three']
    four = data['usa_four']
    five = data['usa_five']
    six = data['usa_six']
    seven = data['usa_seven']
    eight = data['usa_eight']
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
        if 'usa_first_photo' in data.items():
            first_photo = data['usa_first_photo']
            id_ = await db.add_text_logistic(
                telegram_id=telegram_id, region='AQSH', text=text_logistic,
                first_photo=first_photo, second_photo=second_photo
            )
        else:
            id_ = await db.add_text_logistic(
                telegram_id=telegram_id, region='AQSH', text=text_logistic, first_photo=None, second_photo=None
            )
    else:
        id_ = await db.add_text_logistic(
            telegram_id=telegram_id, region='AQSH', text=text_logistic, first_photo=None, second_photo=None
        )
    await state.finish()
    await message.answer(
        text=type_of_transport_ru, reply_markup=transport_ibuttons_ru(
            region=f'AQSH_{id_[0]}'
        )
    )
