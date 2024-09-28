import pytz
from aiogram import types
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
# from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from handlers.admin.users import download_user_xls

tz = pytz.timezone('Asia/Tashkent')

job_defaults = {
    "misfire_grace_time": 3600
}

jobstores = {
    "default": SQLAlchemyJobStore(url='sqlite:///jobs.sqlite')
}

scheduler = AsyncIOScheduler(
    timezone=tz,
    jobstores=jobstores,
    job_defaults=job_defaults
)


async def jobs():
    await download_user_xls()


scheduler.add_job(jobs, trigger='cron', day_of_week='*', hour=21,
                  minute=31)  # Haftaning barcha kunlari soat 15:26 da ishga tushadi
scheduler.add_job(jobs, trigger='cron', day_of_week='mon-fri', hour=15,
                  minute=26)  # Haftaning dushanbadan jumagacha kunlari soat 15:26 da ishga tushadi
# scheduler.add_job(jobs, trigger='interval', hour=1)  # Har 1 soatda qayta ishni bajaradi
#
# if __name__ == '__main__':
#     scheduler.start()
