from aiogram import types
from aiogram.dispatcher import FSMContext
from magic_filter import F

from filters.private import IsPrivate
from keyboards.default.logistic_cbuttons import logistic_main_cbuttons
from keyboards.inline.logistic_ibuttons import uz_logictic_questions_ikeys
from loader import dp

type_of_transport = 'Qaysi transport turidan foydalanmoqchisiz?'


def uz_logistic_text(region: str):
    text = (f'{region} logistika hizmatimizdan foydalanish uchun quyidagi savollarimizga javob bering yoki '
            f'operatorga murojaat qoldiring.'
            f'\n\n1. To\'lov turi'
            f'\n2. Zatamojka joyi'
            f'\n3. Rastamojning joyi'
            f'\n4. Tushirish joyi'
            f'\n5. Yukning nomi'
            f'\n6. Yalpi va sof vazn'
            f'\n7. Qadoqdan keyingi yukning o\'lchamlari'
            f'\n8. Qadoq turi'
            f'\n9. Transport turi'
            f'\n10. Qadoqlashdan oldin va keyin yukning fotosurati')
    return text


def uz_text_china():
    text = ('Xitoy logistika hizmatimizdan foydalanish uchun quyidagi savollarimizga javob bering yoki '
            'operatorga murojaat qoldiring.'
            '\n\n1. Yetkazib berish shartlari'
            '\n2. Yuklash joyi'
            '\n3. Yukning nomi'
            '\n4. TN VED KODI'
            '\n5. Yalpi va sof vazni'
            '\n6. Qadoqlashdan keyin yukning o\'lchamlari'
            '\n7. Qadoq turi'
            '\n8. Invoys / qadoqlash ro\'yxati'
            '\n9. Qadoqlashdan oldin va keyin yukning fotosurati'
            )
    return text


def uz_text_europe():
    text = ('Yevropa logistika hizmatimizdan foydalanish uchun quyidagi savollarimizga javob bering yoki '
            'operatorga murojaat qoldiring.'
            '\n\n1. Yuk qachon tayyor bo\'ladi?'
            '\n2. Omborning manzili va ish vaqti'
            '\n3. Yukning og\'irligi va qo\'shimcha ma\'lumotlari'
            '\n4. Eksport deklaratsiyasi qayerda beriladi?'
            '\n5. Uni yig\'ish mumkinmi?'
            '\n6. Maxsus shartlar (CEMT, ADR va boshqalar.)'
            '\n7. Haydovchi uchun mos yozuvlar raqami yuklanadimi?'
            '\n8. Mahsulot schyot-fakturasi'
            )
    return text


@dp.callback_query_handler(F.data == 'back_logistics', state='*')
async def back_logistic_callback(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.delete()
    await call.message.answer(
        text='Logistika bo\'limi', reply_markup=logistic_main_cbuttons()
    )


@dp.message_handler(IsPrivate(), F.text == 'Mustaqil Davlatlar Hamdo\'stiligi (MDH)', state='*')
async def logistic_uz_main_mdh(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer(
        text=uz_logistic_text(region='MDH'),
        reply_markup=uz_logictic_questions_ikeys(
            region='logistic_cis', call_admin='call_cis'
        )
    )


@dp.message_handler(IsPrivate(), F.text == 'Yevropa', state='*')
async def logistic_uz_main_euro(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer(
        text=uz_text_europe(),
        reply_markup=uz_logictic_questions_ikeys(
            region='logistic_europe', call_admin='call_europe'
        )
    )


@dp.message_handler(IsPrivate(), F.text == 'Osiyo', state='*')
async def logistic_uz_main_asia(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer(
        text=uz_logistic_text(region='Osiyo'),
        reply_markup=uz_logictic_questions_ikeys(
            region='logistic_asia', call_admin='call_asia'
        )
    )


@dp.message_handler(IsPrivate(), F.text == 'Amerika Qo\'shma Shtatlari (AQSH)', state='*')
async def logistic_uz_main_usa(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer(
        text=uz_logistic_text(region='AQSH'),
        reply_markup=uz_logictic_questions_ikeys(
            region='logistic_usa', call_admin='call_usa'
        )
    )


@dp.message_handler(IsPrivate(), F.text == 'Xitoy', state='*')
async def logistic_uz_main_china(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer(
        text=uz_text_china(),
        reply_markup=uz_logictic_questions_ikeys(
            region='logistic_china', call_admin='call_china'
        )
    )
