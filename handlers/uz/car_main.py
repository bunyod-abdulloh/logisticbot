from aiogram import types
from aiogram.dispatcher import FSMContext
from magic_filter import F

from data.config import AUTO_GROUP
from keyboards.inline.car_ibuttons import key_returner, get_brand_buttons, back_models_ibutton
from loader import dp, db, bot
from states.user_states import UserCars

PAGE_COUNT = 10


@dp.callback_query_handler(F.data == 'car_menu_uz', state='*')
async def car_menu_uz(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.answer(
        text='Avtomobil markasini tanlang', reply_markup=await get_brand_buttons()
    )
    await UserCars.main.set()


@dp.callback_query_handler(F.data.contains('uzcar_'), state='*')
async def car_model_uz_cmd(call: types.CallbackQuery):
    telegram_id = call.from_user.id
    car_id = call.data.split('_')[1]
    user = await db.select_user(telegram_id=telegram_id)
    car = await db.select_by_id_car(car_id)
    reference_id = await db.add_reference_car(
        telegram_id=telegram_id, car_brand=car[2], car_model=car[3])
    await bot.send_message(
        chat_id=AUTO_GROUP,
        text=f'ID |{telegram_id}|\n\n#avtomobillar'
             f'\n\nFoydalanuvchi qayta qo\'ng\'iroqni kutmoqda!'
             f'\n\n<b>Sana:</b> {reference_id[1]}'
             f'\n<b>Bo\'lim:</b> 🚗 Avtomobillar'
             f'\n\n<b>So\'rov raqami:</b> {reference_id[0]}'
             f'\n<b>Foydalanuvchi:</b> {user[2]}'
             f'\n<b>Username:</b> {user[3]}'
             f'\n<b>Telefon raqam:</b> {user[4]}'
             f'\n<b>Tanlangan brand/marka:</b> {car[2]} | {car[3]}'
    )
    await call.answer(
        text='Habaringiz qabul qilindi! Operatorlarimiz Siz bilan bog\'lanishadi!',
        show_alert=True
    )


@dp.callback_query_handler(text_contains="alertmessage_", state="*")
async def alert_message(call: types.CallbackQuery):
    current_page = call.data.split("_")[1]
    await call.answer(
        text=f"Siz {current_page} - sahifadasiz!",
        show_alert=True
    )


@dp.callback_query_handler(state=UserCars.main)
async def car_models_uz(call: types.CallbackQuery, state: FSMContext):
    models = await db.select_cars_model(brand=call.data)

    current_page = 1

    if len(models) % PAGE_COUNT == 0:
        all_pages = len(models) // PAGE_COUNT
    else:
        all_pages = len(models) // PAGE_COUNT + 1

    key = key_returner(models[:PAGE_COUNT], current_page=current_page, all_pages=all_pages)

    model = ' '
    c = 0
    for i in models[:PAGE_COUNT]:
        c += 1
        model += f'{c}. {i[1]}\n'

    await call.message.answer_photo(
        photo=models[0][2],
        caption=f'{model}\nYuqoridagi ketma ketlik bo\'yicha kerakli markani tanlang', reply_markup=key
    )
    await state.update_data(
        current_page=current_page, all_pages=all_pages, brand=call.data
    )
    await UserCars.first.set()


@dp.callback_query_handler(state=UserCars.first)
async def car_models_uz_(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    current_page = data['current_page']
    all_pages = data['all_pages']
    brand = data['brand']
    models = await db.select_cars_model(brand=brand)
    if call.data.isalpha():
        if call.data == "prev":
            if current_page == 1:
                current_page = all_pages
            else:
                current_page -= 1
        elif call.data == 'next':
            if current_page == all_pages:
                current_page = 1
            else:
                current_page += 1
        all_messages = models[(current_page - 1) * PAGE_COUNT: current_page * PAGE_COUNT]
        key = key_returner(all_messages, current_page, all_pages)

        model = str()
        c = 0
        for i in all_messages:
            c += 1
            model += f'{c}. {i[1]}\n'
        await call.message.answer_photo(
            photo=all_messages[0][2],
            caption=f'{model}\nRasmdagi ketma ketlik bo\'yicha kerakli markani tanlang', reply_markup=key
        )
        await state.update_data(
            current_page=current_page, all_pages=all_pages, brand=brand
        )
    else:
        car = await db.select_by_id_car(id_=call.data)
        await call.message.answer_photo(
            photo=car[-1],
            caption=f'🚘 {car[2]}'
                    f'\n🕹{car[3]}'
                    f'\n💰 ${car[4]}',
            reply_markup=back_models_ibutton(
                car_id=car[0]
            )
        )
