from aiogram import types
from aiogram.dispatcher import FSMContext
from magic_filter import F

from data.config import CHINA_GROUP
from handlers.uz.logistic_main import type_of_transport
from keyboards.inline.logistic_ibuttons import uz_transport_ibuttons
from loader import dp, db, bot
from states.user_states import LogisticChina


@dp.callback_query_handler(F.data == 'logistic_china', state='*')
async def logistic_uz_main_china(call: types.CallbackQuery):
    await call.message.edit_text(
        text='1. Yetkazib berish shartlari'
    )
    await LogisticChina.one.set()


@dp.callback_query_handler(F.data == 'call_china', state='*')
async def logistic_uz_call_china(call: types.CallbackQuery):
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
        text='So\'rovingiz qabul qilindi! Operatorlarimiz Siz bilan bog\'lanishadi!',
        show_alert=True
    )
    await call.message.delete()


@dp.message_handler(state=LogisticChina.one)
async def uz_logistic_china_one(message: types.Message, state: FSMContext):
    await state.update_data(
        china_one=message.text
    )
    await message.answer(
        text='2. Yuklash joyi'
    )
    await LogisticChina.two.set()


@dp.message_handler(state=LogisticChina.two)
async def uz_logistic_china_two(message: types.Message, state: FSMContext):
    await state.update_data(
        china_two=message.text
    )
    await message.answer(
        text='3. Yukning nomi'
    )
    await LogisticChina.three.set()


@dp.message_handler(state=LogisticChina.three)
async def uz_logistic_china_three(message: types.Message, state: FSMContext):
    await state.update_data(
        china_three=message.text
    )
    await message.answer(
        text='4. TN VED KODI'
    )
    await LogisticChina.four.set()


@dp.message_handler(state=LogisticChina.four)
async def uz_logistic_china_four(message: types.Message, state: FSMContext):
    await state.update_data(
        china_four=message.text
    )
    await message.answer(
        text='5. Yalpi va sof vazni'
    )
    await LogisticChina.five.set()


@dp.message_handler(state=LogisticChina.five)
async def uz_logistic_china_five(message: types.Message, state: FSMContext):
    await state.update_data(
        china_five=message.text
    )
    await message.answer(
        text='6. Qadoqlashdan keyin yukning o\'lchamlari'
    )
    await LogisticChina.six.set()


@dp.message_handler(state=LogisticChina.six)
async def uz_logistic_china_six(message: types.Message, state: FSMContext):
    await state.update_data(
        china_six=message.text
    )
    await message.answer(
        text='7. Qadoq turi'
    )
    await LogisticChina.seven.set()


@dp.message_handler(state=LogisticChina.seven)
async def uz_logistic_china_seven(message: types.Message, state: FSMContext):
    await state.update_data(
        china_seven=message.text
    )
    await message.answer(
        text='8. Invoys / qadoqlash ro\'yxati'
    )
    await LogisticChina.eight.set()


@dp.message_handler(state=LogisticChina.eight)
async def uz_logistic_china_eight(message: types.Message, state: FSMContext):
    await state.update_data(
        china_eight=message.text
    )
    await message.answer(
        text='9. Yukning qadoqlashdan oldingi fotosuratini yuboring'
    )
    await LogisticChina.nine.set()


@dp.message_handler(state=LogisticChina.nine, content_types=['photo', 'text'])
async def uz_logistic_china_nine(message: types.Message, state: FSMContext):
    if message.content_type == 'photo':
        await state.update_data(
            china_first_photo=message.photo[1].file_id
        )
    else:
        pass
    await message.answer(
        text='10. Yukning qadoqlashdan keyingi fotosuratini yuboring'
    )
    await LogisticChina.ten.set()


@dp.message_handler(state=LogisticChina.ten, content_types=['photo', 'text'])
async def uz_logistic_china_ten(message: types.Message, state: FSMContext):
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
        text=type_of_transport, reply_markup=uz_transport_ibuttons(
            region=f'Xitoy_{id_[0]}'
        )
    )
