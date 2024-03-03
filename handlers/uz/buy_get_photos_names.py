from aiogram import types
from aiogram.dispatcher import FSMContext
from magic_filter import F

from data.config import BUY_GROUP
from filters.private import IsPrivate
from keyboards.default.buy_cbuttons import buy_main_cbuttons, buy_back_button
from loader import dp, db, bot
from states.user_states import UserBuy


async def del_buy_function(id_: int, message: types.Message, state: FSMContext):
    await db.delete_buy_by_id(
        id_=id_
    )
    await message.answer(
        text='Kerakli bo\'limni tanlang', reply_markup=buy_main_cbuttons()
    )
    await state.finish()


@dp.message_handler(IsPrivate(), F.text == '️↩️ Xarid bo\'limiga qaytish', state='*')
async def back_buy_uz(message: types.Message, state: FSMContext):
    get_state = await state.get_state()
    data = await state.get_data()
    if get_state == 'UserBuy:raw_comment':
        await del_buy_function(
            id_=data['raw_id'], message=message, state=state
        )
    elif get_state == 'UserBuy:equipment_comment':
        await del_buy_function(
            id_=data['equipment_id'], message=message, state=state
        )
    elif get_state == 'UserBuy:small_equipment_comment':
        await del_buy_function(
            id_=data['small_id'], message=message, state=state
        )


@dp.callback_query_handler(F.data == 'back_buy_uz', state='*')
async def back_buy_uz(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    await call.message.answer(
            text='Kerakli bo\'limni tanlang', reply_markup=buy_main_cbuttons()
        )
    await state.finish()


@dp.callback_query_handler(state=UserBuy.equipment)
async def state_equipment_uz(call: types.CallbackQuery):
    if call.data == 'buy_uz_photo':
        await call.message.edit_text(
            text='Sizga aynan qaysi uskuna kerakligini aniqlashtirishimiz uchun uskuna '
                 'rasmini jo\'nating'
        )
        await UserBuy.equipment_photo.set()
    elif call.data == 'buy_uz_comment':
        await call.message.edit_text(
            text='Habaringizni kiriting'
        )
        await UserBuy.equipment_text.set()


@dp.callback_query_handler(state=UserBuy.raw)
async def state_raw_uz(call: types.CallbackQuery):
    if call.data == 'buy_uz_photo':
        await call.message.edit_text(
            text='Sizga aynan qanday xom ashyo kerakligini aniqlashtirishimiz uchun xom ashyo '
                 'rasmini jo\'nating'
        )
        await UserBuy.raw_photo.set()
    elif call.data == 'buy_uz_comment':
        await call.message.edit_text(
            text='Habaringizni kiriting'
        )
        await UserBuy.equipment_text.set()


@dp.callback_query_handler(state=UserBuy.small_equipment)
async def state_small_equipment_uz(call: types.CallbackQuery):
    if call.data == 'buy_uz_photo':
        await call.message.edit_text(
            text='Sizga aynan qanday kichik uskuna kerakligini aniqlashtirishimiz uchun kichik uskuna '
                 'rasmini jo\'nating'
        )
        await UserBuy.small_equipment_photo.set()
    elif call.data == 'buy_uz_comment':
        await call.message.edit_text(
            text='Habaringizni kiriting'
        )
        await UserBuy.equipment_text.set()


@dp.message_handler(state=UserBuy.equipment_photo, content_types=['photo', 'text'])
async def state_equipment_photo(message: types.Message, state: FSMContext):
    if message.content_type == 'photo':
        telegram_id = message.from_user.id
        file_id = message.photo[-1].file_id
        caption = message.caption
        id_ = await db.add_buy_sql(
            telegram_id=telegram_id, type_='Uskuna', photo=file_id, caption=caption, text=None
        )
        await state.update_data(
            equipment_id=id_[0]
        )
        await message.answer_photo(
            photo=file_id, caption=caption
        )
        await message.answer(
            text='\nRasm qabul qilindi!\n\nSavol yoki izohingizni kiriting', reply_markup=buy_back_button
        )
        await UserBuy.equipment_comment.set()
    else:
        await message.answer(
            text='Iltimos, faqat rasm yuboring!'
        )


@dp.message_handler(state=UserBuy.equipment_comment)
async def get_buy_comments(message: types.Message, state: FSMContext):
    telegram_id = message.from_user.id
    data = await state.get_data()
    id_ = data.get('equipment_id')
    await db.update_buy_comments(
        text=message.text, id_=id_
    )
    buy = await db.add_reference_buy(
        telegram_id=telegram_id, buy_type='Uskuna'
    )
    user = await db.select_user(telegram_id=telegram_id)
    user_ = await db.select_buy_by_id(id_=id_)
    await bot.send_photo(
        chat_id=BUY_GROUP,
        photo=user_[4],
        caption=f'ID |{telegram_id}|\n\n{user_[5]}'
                f'\n\n#uskunalar'
                f'\n\n<b>Sana:</b> {buy[1]}'
                f'\n<b>Bo\'lim:</b> 🛍 Xarid qilish > Uskunalar'
                f'\n\n<b>So\'ro\'v raqami:</b> {buy[0]}'
                f'\n<b>Ism:</b> {user[2]}'
                f'\n<b>Username:</b> {user[3]}'
                f'\n<b>Telefon raqam:</b> {user[4]}'
                f'\n<b>Foydalanuvchi habari</b>: {message.text}'
    )
    await state.finish()
    await message.answer(
        text='Ma\'lumotlaringiz qabul qilindi! Tez orada operatorlarimiz Siz bilan bog\'lanishadi!',
        reply_markup=buy_main_cbuttons()
    )


@dp.message_handler(state=UserBuy.equipment_text)
async def equipment_text_uz(message: types.Message, state: FSMContext):
    await state.finish()
    telegram_id = message.from_user.id
    text = message.text
    await db.add_buy_sql(
        telegram_id=telegram_id, type_='Uskuna', photo=None, caption=None, text=text
    )
    user = await db.select_user(
        telegram_id=telegram_id
    )
    buy = await db.add_reference_buy(
        telegram_id=telegram_id, buy_type='Uskuna'
    )
    await bot.send_message(
        chat_id=BUY_GROUP,
        text=f'ID |{telegram_id}|\n\n#uskunalar #xom_ashyo #kichik_uskunalar'
             f'\n\n<b>Sana:</b> {buy[1]}'
             f'\n<b>Bo\'lim:</b> 🛍 Xarid qilish'
             f'\n\n<b>So\'ro\'v raqami:</b> {buy[0]}'
             f'\n<b>Ism:</b> {user[2]}'
             f'\n<b>Username:</b> {user[3]}'
             f'\n<b>Telefon raqam:</b> {user[4]}'
             f'\n<b>Foydalanuvchi habari</b>: {text}'
    )
    await message.answer(
        text='Ma\'lumotlaringiz qabul qilindi! Tez orada operatorlarimiz Siz bilan bog\'lanishadi!',
        reply_markup=buy_main_cbuttons()
    )


@dp.message_handler(state=UserBuy.raw_photo, content_types=['photo', 'text'])
async def state_raw_photo(message: types.Message, state: FSMContext):
    if message.content_type == 'photo':
        telegram_id = message.from_user.id
        file_id = message.photo[-1].file_id
        caption = message.caption
        id_ = await db.add_buy_sql(
            telegram_id=telegram_id, type_='Xom ashyo', photo=file_id, caption=caption, text=None
        )
        await state.update_data(
            raw_id=id_[0]
        )
        await message.answer_photo(
            photo=file_id, caption=caption
        )
        await message.answer(
            text='\nRasm qabul qilindi!\n\nSavol yoki izohingizni kiriting', reply_markup=buy_back_button
        )
        await UserBuy.raw_comment.set()
    else:
        await message.answer(
            text='Iltimos, faqat rasm yuboring!'
        )


@dp.message_handler(state=UserBuy.small_equipment_photo, content_types=['photo', 'text'])
async def state_small_equipment_photo(message: types.Message, state: FSMContext):
    if message.content_type == 'photo':
        telegram_id = message.from_user.id
        file_id = message.photo[-1].file_id
        caption = message.caption
        id_ = await db.add_buy_sql(
            telegram_id=telegram_id, type_='Kichik uskunalar', photo=file_id, caption=caption, text=None
        )
        await state.update_data(
            small_id=id_[0]
        )
        await message.answer_photo(
            photo=file_id, caption=caption
        )
        await message.answer(
            text='\nRasm qabul qilindi!\n\nSavol yoki izohingizni kiriting', reply_markup=buy_back_button
        )
        await UserBuy.small_equipment_comment.set()


@dp.message_handler(state=UserBuy.raw_comment)
async def get_buy_comments(message: types.Message, state: FSMContext):
    telegram_id = message.from_user.id
    data = await state.get_data()
    id_ = data.get('raw_id')
    await db.update_buy_comments(
        text=message.text, id_=id_
    )
    buy_reference = await db.add_reference_buy(
        telegram_id=telegram_id, buy_type='Xom ashyo'
    )
    buy = await db.select_buy_by_id(
        id_=id_
    )
    user = await db.select_user(telegram_id=telegram_id)
    await bot.send_photo(
        chat_id=BUY_GROUP,
        photo=buy[4],
        caption=f'ID |{telegram_id}|\n\n{buy[5]}'
                f'\n\n#xom_ashyo'
                f'\n\n<b>Sana:</b> {buy_reference[1]}'
                f'\n<b>Bo\'lim:</b> 🛍 Xarid qilish > Xom ashyo'
                f'\n\n<b>So\'ro\'v raqami:</b> {buy_reference[0]}'
                f'\n<b>Ism:</b> {user[2]}'
                f'\n<b>Username:</b> {user[3]}'
                f'\n<b>Telefon raqam:</b> {user[4]}'
                f'\n<b>Foydalanuvchi habari</b>: {message.text}'
    )
    await state.finish()
    await message.answer(
        text='Ma\'lumotlaringiz qabul qilindi! Tez orada operatorlarimiz Siz bilan bog\'lanishadi!',
        reply_markup=buy_main_cbuttons()
    )


@dp.message_handler(state=UserBuy.small_equipment_comment)
async def get_buy_comments(message: types.Message, state: FSMContext):
    telegram_id = message.from_user.id
    data = await state.get_data()
    id_ = data.get('small_id')
    await db.update_buy_comments(
        text=message.text, id_=id_
    )
    buy_reference = await db.add_reference_buy(
        telegram_id=telegram_id, buy_type='Kichik uskunalar'
    )
    buy = await db.select_buy_by_id(
        id_=id_
    )
    user = await db.select_user(telegram_id=telegram_id)
    await bot.send_photo(
        chat_id=BUY_GROUP,
        photo=buy[4],
        caption=f'ID |{telegram_id}|\n\n{buy[5]}'
                f'\n\n#kichik_uskunalar'
                f'\n\n<b>Sana:</b> {buy_reference[1]}'
                f'\n<b>Bo\'lim:</b> 🛍 Xarid qilish > Kichik uskunalar'
                f'\n\n<b>So\'ro\'v raqami:</b> {buy_reference[0]}'
                f'\n<b>Ism:</b> {user[2]}'
                f'\n<b>Username:</b> {user[3]}'
                f'\n<b>Telefon raqam:</b> {user[4]}'
                f'\n<b>Foydalanuvchi habari</b>: {message.text}'
    )
    await state.finish()
    await message.answer(
        text='Ma\'lumotlaringiz qabul qilindi! Tez orada operatorlarimiz Siz bilan bog\'lanishadi!',
        reply_markup=buy_main_cbuttons()
    )
