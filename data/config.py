from environs import Env

env = Env()
env.read_env()


BOT_TOKEN = env.str("BOT_TOKEN")
ADMINS = env.list("ADMINS")
AUTO_GROUP = env.int("AUTO_GROUP")
BUY_GROUP = env.int("BUY_GROUP")
LOGISTICS_GROUP = env.int("LOGISTICS_GROUP")
CHINA_GROUP = env.int("CHINA_GROUP")
DATABASE_GROUP = env.int("DATABASE_GROUP")
ALL_GROUPS = AUTO_GROUP, BUY_GROUP, LOGISTICS_GROUP, CHINA_GROUP
IP = env.str("IP")

DB_USER = env.str("DB_USER")
DB_PASS = env.str("DB_PASS")
DB_NAME = env.str("DB_NAME")
DB_HOST = env.str("DB_HOST")
