from aiogram import types
from aiogram.dispatcher import FSMContext
from magic_filter import F

from data.config import LOGISTICS_GROUP
from handlers.ru.logistic_main import type_of_transport_ru
from keyboards.inline.ru.logistic_ibuttons import transport_ibuttons_ru
from loader import dp, db, bot
from states.ru.users import LogisticEuropeRu


@dp.callback_query_handler(F.data == 'logistic_europe_ru', state='*')
async def logistic_ru_main_europe(call: types.CallbackQuery):
    await call.message.edit_text(
        text='1. Когда груз будет готов?'
    )
    await LogisticEuropeRu.one.set()


@dp.callback_query_handler(F.data == 'call_europe_ru', state='*')
async def logistic_ru_call_europe(call: types.CallbackQuery):
    telegram_id = call.from_user.id
    id_ = await db.add_reference_logistic(
        telegram_id=telegram_id, logistic_type='qayta_qongiroq', logistic_region='Yevropa'
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
            f'\n<b>Tanlangan davlat:</b> Yevropa')
    await bot.send_message(
        chat_id=LOGISTICS_GROUP, text=text
    )
    await call.answer(
        text='Ваша заявка принята! Наши операторы скоро свяжутся с вами!',
        show_alert=True
    )
    await call.message.delete()


@dp.message_handler(state=LogisticEuropeRu.one)
async def europe_ru_one(message: types.Message, state: FSMContext):
    await state.update_data(
        europe_one=message.text
    )
    await message.answer(
        text='2. Адрес и время работы склада'
    )
    await LogisticEuropeRu.two.set()


@dp.message_handler(state=LogisticEuropeRu.two)
async def europe_ru_two(message: types.Message, state: FSMContext):
    await state.update_data(
        europe_two=message.text
    )
    await message.answer(
        text='3. Вес груза и дополнительная информация'
    )
    await LogisticEuropeRu.three.set()


@dp.message_handler(state=LogisticEuropeRu.three)
async def europe_ru_three(message: types.Message, state: FSMContext):
    await state.update_data(
        europe_three=message.text
    )
    await message.answer(
        text='4. Где оформляется экспортная декларация?'
    )
    await LogisticEuropeRu.four.set()


@dp.message_handler(state=LogisticEuropeRu.four)
async def europe_ru_four(message: types.Message, state: FSMContext):
    await state.update_data(
        europe_four=message.text
    )
    await message.answer(
        text='5. Можно ли его собрать?'
    )
    await LogisticEuropeRu.five.set()


@dp.message_handler(state=LogisticEuropeRu.five)
async def europe_ru_five(message: types.Message, state: FSMContext):
    await state.update_data(
        europe_five=message.text
    )
    await message.answer(
        text='6. Особые условия (CEMT, ADR и др.)'
    )
    await LogisticEuropeRu.six.set()


@dp.message_handler(state=LogisticEuropeRu.six)
async def europe_ru_six(message: types.Message, state: FSMContext):
    await state.update_data(
        europe_six=message.text
    )
    await message.answer(
        text='7. Загружается ли ссылочный номер драйвера?'
    )
    await LogisticEuropeRu.seven.set()


@dp.message_handler(state=LogisticEuropeRu.seven)
async def europe_ru_seven(message: types.Message, state: FSMContext):
    await state.update_data(
        europe_seven=message.text
    )
    await message.answer(
        text='8. Счет-фактура продукта'
    )
    await LogisticEuropeRu.eight.set()


@dp.message_handler(state=LogisticEuropeRu.eight)
async def europe_ru_eight(message: types.Message, state: FSMContext):
    data = await state.get_data()
    one = data['europe_one']
    two = data['europe_two']
    three = data['europe_three']
    four = data['europe_four']
    five = data['europe_five']
    six = data['europe_six']
    seven = data['europe_seven']
    eight = message.text
    text_logistic = (f'1. Yuk qachon tayyor bo\'ladi? {one}'
                     f'\n2. Omborning manzili va ish vaqti: {two}'
                     f'\n3. Yukning og\'irligi va qo\'shimcha ma\'lumotlari: {three}'
                     f'\n4. Eksport deklaratsiyasi qayerda beriladi? {four}'
                     f'\n5. Uni yig\'ish mumkinmi? {five}'
                     f'\n6. Maxsus shartlar (CEMT, ADR va boshqalar.): {six}'
                     f'\n7. Haydovchi uchun mos yozuvlar raqami yuklanadimi? {seven}'
                     f'\n8. Mahsulot schyot-fakturasi: {eight}'
                     )
    id_ = await db.add_text_logistic(
        telegram_id=message.from_user.id, text=text_logistic, region='Yevropa', first_photo=None, second_photo=None
    )
    await state.finish()
    await message.answer(
        text=type_of_transport_ru, reply_markup=transport_ibuttons_ru(
            region=f'Yevropa_{id_[0]}'
        )
    )
