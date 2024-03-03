from aiogram import types
from magic_filter import F

from data.config import LOGISTICS_GROUP
from loader import dp, bot, db


async def latest_logistic_message_ru(call: types.CallbackQuery):
    await call.answer(
        text='Ваша заявка принята! Наши операторы скоро свяжутся с вами!',
        show_alert=True
    )    
    await call.message.delete()


@dp.callback_query_handler(F.data.contains('aviaru_'), state='*')
async def get_avia_ru(call: types.CallbackQuery):
    album = types.MediaGroup()
    telegram_id = call.from_user.id
    region = call.data.split('_')[1]
    id_ = call.data.split('_')[2]
    await db.update_type_logistic(
        type_='avia', id_=id_
    )
    user = await db.select_user(
        telegram_id=telegram_id
    )
    user_ = await db.select_by_id_logistic(
        id_=id_
    )
    reference_id = await db.add_reference_logistic(
        telegram_id=telegram_id, logistic_region=region, logistic_type='avia'
    )
    caption = (f'ID |{telegram_id}|\n\n#logistika_avia'
               f'\n\n<b>Sana:</b> {reference_id[1]}'
               f'\n<b>Bo\'lim:</b> 📦 Logistika xizmati'
               f'\n\n<b>So\'rov raqami:</b> {reference_id[0]}'
               f'\n<b>Ism:</b> {user[2]}'
               f'\n<b>Username:</b> {user[3]}'
               f'\n<b>Telefon raqam:</b> {user[4]}'
               f'\n<b>Tanlangan davlat:</b> {region}'
               f'\n<b>Logistika turi:</b> Avia'
               f'\n\n<b>So\'rovnomaga javob:</b>'
               f'\n{user_[5]}')
    if user_[-1] is None:
        await bot.send_message(
            chat_id=LOGISTICS_GROUP,
            text=caption
        )
    else:
        photo1 = user_[-2]
        photo2 = user_[-1]
        album.attach_photo(photo=photo1)
        album.attach_photo(photo=photo2, caption=caption)
        await bot.send_media_group(
            chat_id=LOGISTICS_GROUP,
            media=album
        )
    await latest_logistic_message_ru(call=call)


@dp.callback_query_handler(F.data.contains('autoru_'), state='*')
async def get_auto_ru(call: types.CallbackQuery):
    album = types.MediaGroup()
    telegram_id = call.from_user.id
    region = call.data.split('_')[1]
    id_ = call.data.split('_')[2]
    await db.update_type_logistic(
        type_='avto', id_=id_
    )
    user = await db.select_user(
        telegram_id=telegram_id
    )
    user_ = await db.select_by_id_logistic(
        id_=id_
    )
    reference_id = await db.add_reference_logistic(
        telegram_id=telegram_id, logistic_region=region, logistic_type='avia'
    )
    caption = (f'ID |{telegram_id}|\n\n#logistika_avto'
               f'\n\n<b>Sana:</b> {reference_id[1]}'
               f'\n<b>Bo\'lim:</b> 📦 Logistika xizmati'
               f'\n\n<b>So\'rov raqami:</b> {reference_id[0]}'
               f'\n<b>Ism:</b> {user[2]}'
               f'\n<b>Username:</b> {user[3]}'
               f'\n<b>Telefon raqam:</b> {user[4]}'
               f'\n<b>Tanlangan davlat:</b> {region}'
               f'\n<b>Logistika turi:</b> Avto'
               f'\n\n<b>So\'rovnomaga javob:</b>'
               f'\n{user_[5]}')
    if user_[-1] is None:
        await bot.send_message(
            chat_id=LOGISTICS_GROUP,
            text=caption
        )
    else:
        photo1 = user_[-2]
        photo2 = user_[-1]
        album.attach_photo(photo=photo1)
        album.attach_photo(photo=photo2, caption=caption)
        await bot.send_media_group(
            chat_id=LOGISTICS_GROUP,
            media=album
        )
    await latest_logistic_message_ru(call=call)


@dp.callback_query_handler(F.data.contains('railwayru_'), state='*')
async def get_railway_ru(call: types.CallbackQuery):
    album = types.MediaGroup()
    telegram_id = call.from_user.id
    region = call.data.split('_')[1]
    id_ = call.data.split('_')[2]
    await db.update_type_logistic(
        type_='temir_yol', id_=id_
    )
    user = await db.select_user(
        telegram_id=telegram_id
    )
    user_ = await db.select_by_id_logistic(
        id_=id_
    )
    reference_id = await db.add_reference_logistic(
        telegram_id=telegram_id, logistic_region=region, logistic_type='temir_yol'
    )
    caption = (f'ID |{telegram_id}|\n\n#logistika_temir_yol'
               f'\n\n<b>Sana:</b> {reference_id[1]}'
               f'\n<b>Bo\'lim:</b> 📦 Logistika xizmati'
               f'\n\n<b>So\'rov raqami:</b> {reference_id[0]}'
               f'\n<b>Ism:</b> {user[2]}'
               f'\n<b>Username:</b> {user[3]}'
               f'\n<b>Telefon raqam:</b> {user[4]}'
               f'\n<b>Tanlangan davlat:</b> {region}'
               f'\n<b>Logistika turi:</b> Temir yo\'l'
               f'\n\n<b>So\'rovnomaga javob:</b>'
               f'\n{user_[5]}')
    if user_[-1] is None:
        await bot.send_message(
            chat_id=LOGISTICS_GROUP,
            text=caption
        )
    else:
        photo1 = user_[-2]
        photo2 = user_[-1]
        album.attach_photo(photo=photo1)
        album.attach_photo(photo=photo2, caption=caption)
        await bot.send_media_group(
            chat_id=LOGISTICS_GROUP,
            media=album
        )
    await latest_logistic_message_ru(call=call)


@dp.callback_query_handler(F.data.contains('multimodalru_'), state='*')
async def get_multimodal_ru(call: types.CallbackQuery):
    album = types.MediaGroup()
    telegram_id = call.from_user.id
    region = call.data.split('_')[1]
    id_ = call.data.split('_')[2]
    await db.update_type_logistic(
        type_='multimodal', id_=id_
    )
    user = await db.select_user(
        telegram_id=telegram_id
    )
    user_ = await db.select_by_id_logistic(
        id_=id_
    )
    reference_id = await db.add_reference_logistic(
        telegram_id=telegram_id, logistic_region=region, logistic_type='multimodal'
    )
    caption = (f'ID |{telegram_id}|\n\n#logistika_multimodal'
               f'\n\n<b>Sana:</b> {reference_id[1]}'
               f'\n<b>Bo\'lim:</b> 📦 Logistika xizmati'
               f'\n\n<b>So\'rov raqami:</b> {reference_id[0]}'
               f'\n<b>Ism:</b> {user[2]}'
               f'\n<b>Username:</b> {user[3]}'
               f'\n<b>Telefon raqam:</b> {user[4]}'
               f'\n<b>Tanlangan davlat:</b> {region}'
               f'\n<b>Logistika turi:</b> Multimodal'
               f'\n\n<b>So\'rovnomaga javob:</b>'
               f'\n{user_[5]}')
    if user_[-1] is None:
        await bot.send_message(
            chat_id=LOGISTICS_GROUP,
            text=caption
        )
    else:
        photo1 = user_[-2]
        photo2 = user_[-1]
        album.attach_photo(photo=photo1)
        album.attach_photo(photo=photo2, caption=caption)
        await bot.send_media_group(
            chat_id=LOGISTICS_GROUP,
            media=album
        )
    await latest_logistic_message_ru(call=call)
