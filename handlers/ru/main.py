from aiogram import types
from aiogram.dispatcher import FSMContext
from magic_filter import F

from filters.private import IsPrivate
from keyboards.default.ru.buy_cbuttons import buy_main_cbuttons_ru
from keyboards.default.ru.logistic_cbuttons import logistic_main_cbuttons_ru
from keyboards.inline.ru.car_ibuttons import get_brand_buttons_ru
from keyboards.inline.ru.feedback_ikeys import feedback_ru_ikeys
from keyboards.inline.ru.profile_ikeys import profile_ru_ikeys
from loader import dp, db
from states.ru.users import UserFormsRu, UserCarsRu


@dp.callback_query_handler(text='ru', state='*')
async def get_uz_main(call: types.CallbackQuery):
    telegram_id = call.from_user.id
    await db.add_user(
        telegram_id=telegram_id, language=call.data
    )
    await call.message.edit_text(
        text="Введите свое имя:"
    )
    await UserFormsRu.full_name.set()


@dp.message_handler(IsPrivate(), F.text == '🚙 Автомобили', state='*')
async def cars_uz_cmd(message: types.Message):
    await message.answer(
        text='Выберите марку автомобиля', reply_markup=await get_brand_buttons_ru()
    )
    await UserCarsRu.main.set()


@dp.message_handler(IsPrivate(), F.text == '📦 Услуга логистики', state='*')
async def logistic_uz_cmd(message: types.Message, state: FSMContext):
    await message.answer(
        text=message.text, reply_markup=logistic_main_cbuttons_ru()
    )
    await state.finish()


@dp.message_handler(IsPrivate(), F.text == '🛍 Закуп', state='*')
async def buy_uz_cmd(message: types.Message, state: FSMContext):
    await message.answer(
        text='Выберите нужный раздел', reply_markup=buy_main_cbuttons_ru()
    )
    await state.finish()


@dp.message_handler(text='🏢 О нас', state='*')
async def about_us_uz_main(message: types.Message, state: FSMContext):
    await message.answer(
        text='ℹ️ Компания ООО "AT Multimodal Logistics" предлагает клиентам полный комплекс логистических услуг. '
             'За многолетний опыт работы на транспортно-логистическом рынке в качестве международного перевозчика и '
             'зарегистрированного таможенного представителя, ООО "AT Multimodal Logistics" заработала имидж '
             'организованной и надежной компании, которая серьезно и профессионально подходит к решению любых '
             'логистических задач. Предлагая своим клиентам услуги в комплексе, мы стремимся оптимизировать все '
             'бизнес-процессы, связанные с организацией и доставкой крупногабаритных, тяжеловесных и сборных грузов. '
             'Развитая география присутствия и обширная международная агентская сеть во всех странах мира позволяют нам'
             ' предлагать клиентам максимально эффективные варианты логистических схем и маршрутов доставки груза из '
             'стран Юго-Восточной Азии и Европы. С учетом таможенного оформления на основных воздушных, морских, '
             'автомобильных и железнодорожных терминалах.'
             '\n\n📌 Адрес: Улица Бабура, 34, Ташкент, Узбекистан '
             '\n\n☎️ Наши контакты:\nㅤㅤ+998931385555\nㅤㅤ+998931395555'
             '\n\n🌐 Наш сайт:\nhttps://atlogisticgroup.com/ru'
    )
    await state.finish()


@dp.message_handler(IsPrivate(), F.text == '👤 Профиль', state='*')
async def profile_uz_cmd(message: types.Message):
    user = await db.select_user(telegram_id=message.from_user.id)
    await message.answer(
        text=f'<b>Ваш профиль</b>'
             f'\n\nИмя: {user[2]}'
             f'\nИмя пользователя Telegram: {user[3]}'
             f'\nНомер телефона: {user[4]}',
        reply_markup=profile_ru_ikeys
    )


@dp.message_handler(IsPrivate(), F.text == '🎙 Написать отзыв', state='*')
async def feedback_uz_cmd(message: types.Message, state: FSMContext):
    await message.answer(
        text='Вы можете присылать свои вопросы, предложения, отзывы и комментарии в виде изображений и текста! '
             'Наши операторы ответят в ближайшее время!', reply_markup=feedback_ru_ikeys
    )
    await state.finish()
