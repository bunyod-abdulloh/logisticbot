from aiogram import types
from aiogram.dispatcher import FSMContext
from magic_filter import F

from data.config import LOGISTICS_GROUP
from handlers.uz.logistic_main import type_of_transport
from keyboards.inline.logistic_ibuttons import uz_transport_ibuttons
from loader import dp, db, bot
from states.user_states import LogisticCIS


@dp.callback_query_handler(F.data == 'logistic_cis', state='*')
async def logistic_uz_main_cis(call: types.CallbackQuery):
    await call.message.edit_text(
        text='1. To\'lov turi'
    )
    await LogisticCIS.one.set()


@dp.callback_query_handler(F.data == 'call_cis', state='*')
async def logistic_uz_call_cis(call: types.CallbackQuery):
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
        text='So\'rovingiz qabul qilindi! Operatorlarimiz Siz bilan bog\'lanishadi!',
        show_alert=True
    )
    await call.message.delete()


@dp.message_handler(state=LogisticCIS.one)
async def uz_logistic_cis_one(message: types.Message, state: FSMContext):
    await state.update_data(
        cis_one=message.text
    )
    await message.answer(
        text='2. Zatamojka joyi'
    )
    await LogisticCIS.two.set()


@dp.message_handler(state=LogisticCIS.two)
async def uz_logistic_cis_two(message: types.Message, state: FSMContext):
    await state.update_data(
        cis_two=message.text
    )
    await message.answer(
        text='3. Rastamojning joyi '
    )
    await LogisticCIS.three.set()


@dp.message_handler(state=LogisticCIS.three)
async def uz_logistic_cis_three(message: types.Message, state: FSMContext):
    await state.update_data(
        cis_three=message.text
    )
    await message.answer(
        text='4. Tushirish joyi'
    )
    await LogisticCIS.four.set()


@dp.message_handler(state=LogisticCIS.four)
async def uz_logistic_cis_four(message: types.Message, state: FSMContext):
    await state.update_data(
        cis_four=message.text
    )
    await message.answer(
        text='5. Yukning nomi'
    )
    await LogisticCIS.five.set()


@dp.message_handler(state=LogisticCIS.five)
async def uz_logistic_cis_five(message: types.Message, state: FSMContext):
    await state.update_data(
        cis_five=message.text
    )
    await message.answer(
        text='6. Yalpi va sof vazn'
    )
    await LogisticCIS.six.set()


@dp.message_handler(state=LogisticCIS.six)
async def uz_logistic_cis_six(message: types.Message, state: FSMContext):
    await state.update_data(
        cis_six=message.text
    )
    await message.answer(
        text='7. Qadoqdan keyingi yukning o\'lchamlari'
    )
    await LogisticCIS.seven.set()


@dp.message_handler(state=LogisticCIS.seven)
async def uz_logistic_cis_seven(message: types.Message, state: FSMContext):
    await state.update_data(
        cis_seven=message.text
    )
    await message.answer(
        text='8. Qadoq turi'
    )
    await LogisticCIS.eight.set()


@dp.message_handler(state=LogisticCIS.eight)
async def uz_logistic_cis_eight(message: types.Message, state: FSMContext):
    await state.update_data(
        cis_eight=message.text
    )
    await message.answer(
        text='9. Yukning qadoqlashdan oldingi fotosuratini yuboring'
    )
    await LogisticCIS.nine.set()


@dp.message_handler(state=LogisticCIS.nine, content_types=['photo', 'text'])
async def uz_logistic_cis_nine(message: types.Message, state: FSMContext):
    if message.content_type == 'photo':
        await state.update_data(
            cis_first_photo=message.photo[1].file_id
        )
    else:
        pass
    await message.answer(
        text='10. Yukning qadoqlashdan keyingi fotosuratini yuboring'
    )
    await LogisticCIS.ten.set()


@dp.message_handler(state=LogisticCIS.ten, content_types=['photo', 'text'])
async def uz_logistic_cis_ten(message: types.Message, state: FSMContext):
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
        text=type_of_transport, reply_markup=uz_transport_ibuttons(
            region=f'MDH_{id_[0]}'
        )
    )
