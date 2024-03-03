from aiogram import types
from aiogram.dispatcher import FSMContext
from magic_filter import F

from filters.private import IsPrivate
from keyboards.default.ru.logistic_cbuttons import logistic_main_cbuttons_ru
from keyboards.inline.ru.logistic_ibuttons import ru_logictic_questions_ikeys
from loader import dp

type_of_transport_ru = 'Какой вид транспорта вы хотите использовать?'


def ru_logistic_text():
    text = (f'Чтобы воспользоваться нашими логистическими услугами, ответьте на наши вопросы ниже или '
            f'оставьте заявку оператору.'
            f'\n\n1. Тип оплаты'
            f'\n2. Место затаможки'
            f'\n3. Место растаможки'
            f'\n4. Место высадки'
            f'\n5. Название груза'
            f'\n6. Вес брутто и нетто'
            f'\n7. Размеры послепакетной загрузки'
            f'\n8. Тип упаковки'
            f'\n9. Вид транспорта'
            f'\n10. Фото груза до и после упаковки')
    return text


def ru_text_china():
    text = ('Чтобы воспользоваться нашими Китайскими логистическими услугами , ответьте на наши вопросы ниже или '
            'оставьте заявку оператору.'
            '\n\n1. Условия поставки'
            '\n2. Место загрузки'
            '\n3. Название груза'
            '\n4. Коды TN VED'
            '\n5. Вес брутто и нетто'
            '\n6. Размеры груза после упаковки'
            '\n7. Тип упаковки'
            '\n8. Инвойс / упаковочный лист'
            '\n9. Фото груза до и после упаковки'
            )
    return text


def ru_text_europe():
    text = ('Чтобы воспользоваться нашими Европейскими логистическими услугами, ответьте на наши вопросы ниже или '
            'operatorga murojaat qoldiring.'
            '\n\n1. Когда груз будет готов?'
            '\n2. Адрес и время работы склада'
            '\n3. Вес груза и дополнительная информация'
            '\n4. Где оформляется экспортная декларация?'
            '\n5. Можно ли его собрать?'
            '\n6. Особые условия (CEMT, ADR и др.)'
            '\n7. Загружается ли ссылочный номер драйвера?'
            '\n8. Счет-фактура продукта'
            )
    return text


@dp.callback_query_handler(F.data == 'back_logistics_ru', state='*')
async def back_logistic_callru(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.delete()
    await call.message.answer(
        text='Логистика', reply_markup=logistic_main_cbuttons_ru()
    )


@dp.message_handler(IsPrivate(), F.text == 'Содружество Независимых Государств (СНГ)', state='*')
async def logistic_ru_main_sng(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer(
        text=ru_logistic_text(),
        reply_markup=ru_logictic_questions_ikeys(
            region='logistic_cis_ru', call_admin='call_cis_ru'
        )
    )


@dp.message_handler(IsPrivate(), F.text == 'Европа', state='*')
async def logistic_ru_main_euro(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer(
        text=ru_text_europe(),
        reply_markup=ru_logictic_questions_ikeys(
            region='logistic_europe_ru', call_admin='call_europe_ru'
        )
    )


@dp.message_handler(IsPrivate(), F.text == 'Азия', state='*')
async def logistic_ru_main_asia(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer(
        text=ru_logistic_text(),
        reply_markup=ru_logictic_questions_ikeys(
            region='logistic_asia_ru', call_admin='call_asia_ru'
        )
    )


@dp.message_handler(IsPrivate(), F.text == 'Соединенные Штаты Америки (США)', state='*')
async def logistic_uz_main_usa(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer(
        text=ru_logistic_text(),
        reply_markup=ru_logictic_questions_ikeys(
            region='logistic_usa_ru', call_admin='call_usa_ru'
        )
    )


@dp.message_handler(IsPrivate(), F.text == 'Китай', state='*')
async def logistic_uz_main_china(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer(
        text=ru_text_china(),
        reply_markup=ru_logictic_questions_ikeys(
            region='logistic_china_ru', call_admin='call_china_ru'
        )
    )
