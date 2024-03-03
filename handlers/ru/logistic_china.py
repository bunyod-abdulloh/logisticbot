from aiogram import types
from aiogram.dispatcher import FSMContext
from magic_filter import F

from data.config import CHINA_GROUP
from handlers.ru.logistic_main import type_of_transport_ru
from keyboards.inline.ru.logistic_ibuttons import transport_ibuttons_ru
from loader import dp, db, bot
from states.ru.users import LogisticChinaRu


@dp.callback_query_handler(F.data == 'logistic_china_ru', state='*')
async def logistic_ru_main_china(call: types.CallbackQuery):
    await call.message.edit_text(
        text='1. Условия поставки'
    )
    await LogisticChinaRu.one.set()


@dp.callback_query_handler(F.data == 'call_china_ru', state='*')
async def logistic_ru_call_china(call: types.CallbackQuery):
    telegram_id = call.from_user.id
    id_ = await db.add_reference_logistic(
        telegram_id=telegram_id, logistic_type='qayta_qongiroq', logistic_region='Xitoy'
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
            f'\n<b>Tanlangan davlat:</b> Xitoy')
    await bot.send_message(
        chat_id=CHINA_GROUP, text=text
    )
    await call.answer(
        text='Ваша заявка принята! Наши операторы скоро свяжутся с вами!',
        show_alert=True
    )
    await call.message.delete()


@dp.message_handler(state=LogisticChinaRu.one)
async def china_ru_one(message: types.Message, state: FSMContext):
    await state.update_data(
        china_one=message.text
    )
    await message.answer(
        text='2. Место загрузки'
    )
    await LogisticChinaRu.two.set()


@dp.message_handler(state=LogisticChinaRu.two)
async def china_ru_two(message: types.Message, state: FSMContext):
    await state.update_data(
        china_two=message.text
    )
    await message.answer(
        text='3. Название груза'
    )
    await LogisticChinaRu.three.set()


@dp.message_handler(state=LogisticChinaRu.three)
async def china_ru_three(message: types.Message, state: FSMContext):
    await state.update_data(
        china_three=message.text
    )
    await message.answer(
        text='4. Код ТН ВЕД'
    )
    await LogisticChinaRu.four.set()


@dp.message_handler(state=LogisticChinaRu.four)
async def china_ru_four(message: types.Message, state: FSMContext):
    await state.update_data(
        china_four=message.text
    )
    await message.answer(
        text='5. Вес брутто и нетто'
    )
    await LogisticChinaRu.five.set()


@dp.message_handler(state=LogisticChinaRu.five)
async def china_ru_five(message: types.Message, state: FSMContext):
    await state.update_data(
        china_five=message.text
    )
    await message.answer(
        text='6. Размеры груза после упаковки'
    )
    await LogisticChinaRu.six.set()


@dp.message_handler(state=LogisticChinaRu.six)
async def china_ru_six(message: types.Message, state: FSMContext):
    await state.update_data(
        china_six=message.text
    )
    await message.answer(
        text='7. Тип упаковки'
    )
    await LogisticChinaRu.seven.set()


@dp.message_handler(state=LogisticChinaRu.seven)
async def china_ru_seven(message: types.Message, state: FSMContext):
    await state.update_data(
        china_seven=message.text
    )
    await message.answer(
        text='8. Инвойс / упаковочный лист'
    )
    await LogisticChinaRu.eight.set()


@dp.message_handler(state=LogisticChinaRu.eight)
async def china_ru_eight(message: types.Message, state: FSMContext):
    await state.update_data(
        china_eight=message.text
    )
    await message.answer(
        text='9. Отправить фото груза перед упаковкой'
    )
    await LogisticChinaRu.nine.set()


@dp.message_handler(state=LogisticChinaRu.nine, content_types=['photo', 'text'])
async def china_ru_nine(message: types.Message, state: FSMContext):
    if message.content_type == 'photo':
        await state.update_data(
            china_first_photo=message.photo[1].file_id
        )
    else:
        pass
    await message.answer(
        text='10. Отправить фотографию груза после упаковки'
    )
    await LogisticChinaRu.ten.set()


@dp.message_handler(state=LogisticChinaRu.ten, content_types=['photo', 'text'])
async def china_ru_ten(message: types.Message, state: FSMContext):
    telegram_id = message.from_user.id
    data = await state.get_data()
    one = data['china_one']
    two = data['china_two']
    three = data['china_three']
    four = data['china_four']
    five = data['china_five']
    six = data['china_six']
    seven = data['china_seven']
    eight = data['china_eight']
    text_logistic = (f'1. Yetkazib berish shartlari: {one}'
                     f'\n2. Yuklash joyi: {two}'
                     f'\n3. Yukning nomi: {three}'
                     f'\n4. TN VED KODI: {four}'
                     f'\n5. Yalpi va sof vazni: {five}'
                     f'\n6. Qadoqlashdan keyin yukning o\'lchamlari: {six}'
                     f'\n7. Qadoq turi: {seven}'
                     f'\n8. Invoys / qadoqlash ro\'yxati: {eight}'
                     )
    if message.content_type == 'photo':
        second_photo = message.photo[-1].file_id
        if 'china_first_photo' in data.items():
            first_photo = data['china_first_photo']
            id_ = await db.add_text_logistic(
                telegram_id=telegram_id, region='Xitoy', text=text_logistic,
                first_photo=first_photo, second_photo=second_photo
            )
        else:
            id_ = await db.add_text_logistic(
                telegram_id=telegram_id, region='Xitoy', text=text_logistic, first_photo=None, second_photo=None
            )
    else:
        id_ = await db.add_text_logistic(
            telegram_id=telegram_id, region='Xitoy', text=text_logistic, first_photo=None, second_photo=None
        )
    await state.finish()
    await message.answer(
        text=type_of_transport_ru, reply_markup=transport_ibuttons_ru(
            region=f'Xitoy_{id_[0]}'
        )
    )
