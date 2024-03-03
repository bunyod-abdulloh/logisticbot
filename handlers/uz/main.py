from aiogram import types
from aiogram.dispatcher import FSMContext
from magic_filter import F

from filters.private import IsPrivate
from keyboards.default.buy_cbuttons import buy_main_cbuttons
from keyboards.default.logistic_cbuttons import logistic_main_cbuttons
from keyboards.inline.car_ibuttons import get_brand_buttons
from keyboards.inline.feedback_ikeys import feedback_uz_ikeys
from keyboards.inline.profile_ikeys import profile_uz_ikeys
from loader import dp, db
from states.user_states import UserForms, UserCars


@dp.callback_query_handler(text='uz', state='*')
async def get_uz_main(call: types.CallbackQuery):
    telegram_id = call.from_user.id
    await db.add_user(
        telegram_id=telegram_id, language=call.data
    )
    await call.message.edit_text(
        text="Ismingizni kiriting:"
    )
    await UserForms.full_name.set()


@dp.message_handler(IsPrivate(), F.text == '🚙 Avtomobillar', state='*')
async def cars_uz_cmd(message: types.Message):
    await message.answer(
        text='Avtomobil markasini tanlang', reply_markup=await get_brand_buttons()
    )
    await UserCars.main.set()


@dp.message_handler(IsPrivate(), F.text == '📦 Logistika xizmati', state='*')
async def logistic_uz_cmd(message: types.Message, state: FSMContext):
    await message.answer(
        text=message.text, reply_markup=logistic_main_cbuttons()
    )
    await state.finish()


@dp.message_handler(IsPrivate(), F.text == '🛍 Xarid qilish', state='*')
async def buy_uz_cmd(message: types.Message, state: FSMContext):
    await message.answer(
        text='Kerakli bo\'limni tanlang', reply_markup=buy_main_cbuttons()
    )
    await state.finish()


@dp.message_handler(text='🏢 Biz haqimizda', state='*')
async def about_us_uz_main(message: types.Message, state: FSMContext):
    await message.answer(
        text='ℹ️ "At Multimodal Logistics" MCHJ sizning logistika bo\'yicha ishonchli hamkoringizdir. Xalqaro transport'
             ' va bojxona rasmiylashtiruvi bo\'yicha ko\'p yillik tajribaga ega bo\'lgan holda, biz har qanday '
             'o\'lchamdagi yuklarni professional yondashuv bilan tashkil etish va yetkazib berishni kafolatlaymiz. '
             'Bizning global agentlik tarmog\'imiz Janubi-Sharqiy Osiyo va Yevropa mamlakatlaridan havo, dengiz, '
             'avtomobil va temir yo\'l terminallari orqali samarali logistika yechimlarini taqdim etadi. Biz har bir '
             'mijoz uchun keng qamrovli xizmatlar va moslashtirilgan yechimlarni taklif qilish orqali biznesingizni '
             'optimallashtirishga intilamiz.'
             '\n\n📌 Manzil: Bobur ko\'chasi, 34, Toshkent, O\'zbekiston'
             '\n\n☎️ Bog\'lanish uchun:\nㅤㅤ+998931385555\nㅤㅤ+998931395555 '
             '\n\n🌐 Bizning saytimiz:ㅤㅤ\nhttps://atlogisticgroup.com/ru'
    )
    await state.finish()


@dp.message_handler(IsPrivate(), F.text == '👤 Profil', state='*')
async def profile_uz_cmd(message: types.Message):
    user = await db.select_user(telegram_id=message.from_user.id)
    await message.answer(
        text=f'<b>Sizning profilingiz</b>'
             f'\n\nIsm: {user[2]}'
             f'\nTelegram username: {user[3]}'
             f'\nTelefon raqam: {user[4]}',
        reply_markup=profile_uz_ikeys
    )


@dp.message_handler(IsPrivate(), F.text == '🎙 Fikr va mulohazalaringizni yuboring', state='*')
async def feedback_uz_cmd(message: types.Message, state: FSMContext):
    await message.answer(
        text='Savol, taklif, fikr va mulohazalaringizni rasm va matnli ko\'rinishda yuborishingiz mumkin! '
             'Operatorlarimiz tez orada javob beradilar!', reply_markup=feedback_uz_ikeys
    )
    await state.finish()

