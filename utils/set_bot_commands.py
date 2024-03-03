from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Botni ishga tushurish"),
            types.BotCommand("id", "ID olish"),
            types.BotCommand("admins", "Adminlar bo'limi"),
            types.BotCommand("block", "Botdan foydalanish bo'yicha cheklov qo'yish")
        ]
    )
