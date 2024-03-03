from aiogram import types
from aiogram.dispatcher import FSMContext
from magic_filter import F

from data.config import LOGISTICS_GROUP
from handlers.uz.logistic_main import type_of_transport
from keyboards.inline.logistic_ibuttons import uz_transport_ibuttons
from loader import dp, db, bot
from states.user_states import LogisticAsia


@dp.callback_query_handler(F.data == 'logistic_asia', state='*')
async def logistic_uz_main_asia(call: types.CallbackQuery):
    await call.message.edit_text(
        text='1. To\'lov turi'
    )
    await LogisticAsia.one.set()


@dp.callback_query_handler(F.data == 'call_asia', state='*')
async def logistic_uz_call_asia(call: types.CallbackQuery):
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
        text='So\'rovingiz qabul qilindi! Operatorlarimiz Siz bilan bog\'lanishadi!',
        show_alert=True
    )
    await call.message.delete()


@dp.message_handler(state=LogisticAsia.one)
async def uz_logistic_asia_one(message: types.Message, state: FSMContext):
    await state.update_data(
        asia_one=message.text
    )
    await message.answer(
        text='2. Zatamojka joyi'
    )
    await LogisticAsia.two.set()


@dp.message_handler(state=LogisticAsia.two)
async def uz_logistic_asia_two(message: types.Message, state: FSMContext):
    await state.update_data(
        asia_two=message.text
    )
    await message.answer(
        text='3. Rastamojning joyi '
    )
    await LogisticAsia.three.set()


@dp.message_handler(state=LogisticAsia.three)
async def uz_logistic_asia_three(message: types.Message, state: FSMContext):
    await state.update_data(
        asia_three=message.text
    )
    await message.answer(
        text='4. Tushirish joyi'
    )
    await LogisticAsia.four.set()


@dp.message_handler(state=LogisticAsia.four)
async def uz_logistic_asia_four(message: types.Message, state: FSMContext):
    await state.update_data(
        asia_four=message.text
    )
    await message.answer(
        text='5. Yukning nomi'
    )
    await LogisticAsia.five.set()


@dp.message_handler(state=LogisticAsia.five)
async def uz_logistic_asia_five(message: types.Message, state: FSMContext):
    await state.update_data(
        asia_five=message.text
    )
    await message.answer(
        text='6. Yalpi va sof vazn'
    )
    await LogisticAsia.six.set()


@dp.message_handler(state=LogisticAsia.six)
async def uz_logistic_asia_six(message: types.Message, state: FSMContext):
    await state.update_data(
        asia_six=message.text
    )
    await message.answer(
        text='7. Qadoqdan keyingi yukning o\'lchamlari'
    )
    await LogisticAsia.seven.set()


@dp.message_handler(state=LogisticAsia.seven)
async def uz_logistic_asia_seven(message: types.Message, state: FSMContext):
    await state.update_data(
        asia_seven=message.text
    )
    await message.answer(
        text='8. Qadoq turi'
    )
    await LogisticAsia.eight.set()


@dp.message_handler(state=LogisticAsia.eight)
async def uz_logistic_asia_eight(message: types.Message, state: FSMContext):
    await state.update_data(
        asia_eight=message.text
    )
    await message.answer(
        text='9. Yukning qadoqlashdan oldingi fotosuratini yuboring'
    )
    await LogisticAsia.nine.set()


@dp.message_handler(state=LogisticAsia.nine, content_types=['photo', 'text'])
async def uz_logistic_asia_nine(message: types.Message, state: FSMContext):
    if message.content_type == 'photo':
        await state.update_data(
            asia_first_photo=message.photo[1].file_id
        )
    else:
        pass
    await message.answer(
        text='10. Yukning qadoqlashdan keyingi fotosuratini yuboring'
    )
    await LogisticAsia.ten.set()


@dp.message_handler(state=LogisticAsia.ten, content_types=['photo', 'text'])
async def uz_logistic_asia_ten(message: types.Message, state: FSMContext):
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
        text=type_of_transport, reply_markup=uz_transport_ibuttons(
            region=f'Osiyo_{id_[0]}'
        )
    )
