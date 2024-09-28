from aiogram import executor

from handlers.admin.apscheduler import scheduler
from loader import dp, db
import middlewares, filters, handlers
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands


async def on_startup(dispatcher):
    await db.create()
    # await db.drop_users()
    # await db.drop_table_logistics()
    # await db.drop_table_feedback()
    # await db.drop_table_admin()
    await db.create_table_users()
    await db.create_table_logistics()
    await db.create_table_buy()
    await db.create_table_feedback()
    await db.create_table_cars()
    await db.create_table_reports()
    await set_default_commands(dispatcher)
    await on_startup_notify(dispatcher)
    scheduler.start()

if __name__ == "__main__":
    executor.start_polling(dp, on_startup=on_startup)
