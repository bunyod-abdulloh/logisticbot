from typing import Union

import asyncpg
from asyncpg import Connection
from asyncpg.pool import Pool

from data import config


class Database:
    def __init__(self):
        self.pool: Union[Pool, None] = None

    async def create(self):
        self.pool = await asyncpg.create_pool(
            user=config.DB_USER,
            password=config.DB_PASS,
            host=config.DB_HOST,
            database=config.DB_NAME,
        )

    async def execute(self, command, *args, fetch: bool = False, fetchval: bool = False, fetchrow: bool = False,
                      execute: bool = False):
        async with self.pool.acquire() as connection:
            connection: Connection
            async with connection.transaction():
                if fetch:
                    result = await connection.fetch(command, *args)
                elif fetchval:
                    result = await connection.fetchval(command, *args)
                elif fetchrow:
                    result = await connection.fetchrow(command, *args)
                elif execute:
                    result = await connection.execute(command, *args)
            return result

    async def create_table_users(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Users (
        id SERIAL PRIMARY KEY,
        telegram_id BIGINT NOT NULL,
        full_name VARCHAR(60) NULL,
        username TEXT NULL,        
        phone TEXT NULL,
        language TEXT NULL               
        );
        """
        await self.execute(sql, execute=True)

    async def add_user(self, telegram_id, language):
        sql = "INSERT INTO Users (telegram_id, language) VALUES($1, $2) returning *"
        return await self.execute(sql, telegram_id, language, fetchrow=True)

    async def select_all_users(self):
        sql = "SELECT * FROM Users"
        return await self.execute(sql, fetch=True)

    async def select_user(self, telegram_id):
        sql = f"SELECT * FROM Users WHERE telegram_id='{telegram_id}'"
        return await self.execute(sql, fetchrow=True)

    async def count_users(self):
        sql = "SELECT COUNT(*) FROM Users"
        return await self.execute(sql, fetchval=True)

    async def update_user_fullname(self, full_name, telegram_id):
        sql = "UPDATE Users SET full_name=$1 WHERE telegram_id=$2"
        return await self.execute(sql, full_name, telegram_id, execute=True)

    async def update_user_phone_username(self, phone, username, telegram_id):
        sql = "UPDATE Users SET phone=$1, username=$2 WHERE telegram_id=$3"
        return await self.execute(sql, phone, username, telegram_id, execute=True)

    async def update_user_language(self, language, telegram_id):
        sql = f"UPDATE Users SET language='{language}' WHERE telegram_id='{telegram_id}'"
        return await self.execute(sql, execute=True)

    async def update_user_username(self, username, telegram_id):
        sql = f"UPDATE Users SET username='{username}' WHERE telegram_id='{telegram_id}'"
        return await self.execute(sql, execute=True)

    async def update_user_phone(self, phone, telegram_id):
        sql = f"UPDATE Users SET phone='{phone}' WHERE telegram_id='{telegram_id}'"
        return await self.execute(sql, execute=True)

    async def update_user_blocks(self, blocked_user, telegram_none, telegram_id):
        sql = (f"UPDATE Users SET blocks='{blocked_user}', telegram_id='{telegram_none}' "
               f"WHERE telegram_id='{telegram_id}'")
        return await self.execute(sql, execute=True)

    async def update_user_unblock(self, unblock, telegram_id, blocked_user):
        sql = (f"UPDATE Users SET blocks='{unblock}', telegram_id='{telegram_id}' "
               f"WHERE blocks='{blocked_user}'")
        return await self.execute(sql, execute=True)

    async def alter_add_column_blocks(self):
        sql = "ALTER TABLE Users ADD COLUMN blocks BIGINT NULL"
        return await self.execute(sql, fetch=True)

    async def alter_drop_column_blocks(self):
        await self.execute("ALTER TABLE Users DROP COLUMN blocks", execute=True)

    async def delete_user(self, telegram_id):
        await self.execute(f"DELETE FROM Users WHERE telegram_id='{telegram_id}'", execute=True)

    async def delete_users(self):
        await self.execute("DELETE FROM Users", execute=True)

    async def drop_users(self):
        await self.execute("DROP TABLE Users", execute=True)

    # ====================TABLE CARS============================================
    async def create_table_cars(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Cars (        
        id SERIAL PRIMARY KEY,        
        main_photo VARCHAR(200) NULL,
        brand VARCHAR(100) NULL,
        model VARCHAR(100) NULL,        
        price VARCHAR(100) NULL,
        file_id VARCHAR(500) NULL                        
        );
        """
        await self.execute(sql, execute=True)

    async def add_car(self, main_photo, brand, model, price, file_id):
        sql = ("INSERT INTO Cars (main_photo, brand, model, price, file_id) "
               "VALUES($1, $2, $3, $4, $5) returning *")
        return await self.execute(sql, main_photo, brand, model, price, file_id, fetchrow=True)

    async def select_cars(self):
        sql = f"SELECT DISTINCT brand FROM Cars ORDER BY brand"
        return await self.execute(sql, fetch=True)

    async def select_cars_model(self, brand):
        sql = f"SELECT id, model, main_photo FROM Cars WHERE brand='{brand}'"
        return await self.execute(sql, fetch=True)

    async def select_by_id_car(self, id_):
        sql = f"SELECT * FROM Cars WHERE id='{id_}'"
        return await self.execute(sql, fetchrow=True)

    async def update_car_photo(self, file_id, brand):
        sql = "UPDATE Cars SET file_id=$1 WHERE brand=$2"
        return await self.execute(sql, file_id, brand, execute=True)

    async def update_brand_photo(self, main_photo, brand):
        sql = "UPDATE Cars SET main_photo=$1 WHERE brand=$2"
        return await self.execute(sql, main_photo, brand, execute=True)

    async def update_car_by_id(self, file_id, id_):
        sql = "UPDATE Cars SET main_photo=$1 WHERE id=$2"
        return await self.execute(sql, file_id, id_, execute=True)

    async def delete_cars(self):
        await self.execute(f"DELETE FROM Cars", execute=True)

    async def drop_table_cars(self):
        await self.execute("DROP TABLE Cars", execute=True)

    async def create_table_logistics(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Logistics (
        id SERIAL PRIMARY KEY,
        checked_date DATE DEFAULT CURRENT_DATE,        
        telegram_id BIGINT NULL,
        region TEXT NULL,
        type TEXT NULL,
        text VARCHAR(4000),
        first_photo VARCHAR(200) NULL,
        second_photo VARCHAR(200) NULL
        );
        """
        await self.execute(sql, execute=True)

    async def add_text_logistic(self, telegram_id, region, text, first_photo, second_photo):
        sql = ("INSERT INTO Logistics (telegram_id, region, text, first_photo, second_photo) "
               "VALUES($1, $2, $3, $4, $5) returning id")
        return await self.execute(sql, telegram_id, region, text, first_photo, second_photo, fetchrow=True)

    async def update_type_logistic(self, type_, id_):
        sql = f"UPDATE Logistics SET type='{type_}' WHERE id='{id_}'"
        return await self.execute(sql, execute=True)

    async def select_by_id_logistic(self, id_):
        sql = f"SELECT * FROM Logistics WHERE id='{id_}'"
        return await self.execute(sql, fetchrow=True)

    async def delete_logistic_id(self, id_):
        await self.execute(f"DELETE FROM Logistics WHERE id='{id_}'", execute=True)

    async def drop_table_logistics(self):
        await self.execute("DROP TABLE Logistics", execute=True)

    async def create_table_buy(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Buy (
        id SERIAL PRIMARY KEY,
        checked_date DATE DEFAULT CURRENT_DATE,        
        telegram_id BIGINT NULL,        
        type TEXT NULL,
        photo VARCHAR(200) NULL,
        caption VARCHAR(4000) NULL,
        text VARCHAR(4000)        
        );
        """
        await self.execute(sql, execute=True)

    async def add_buy_sql(self, telegram_id, type_, photo, caption, text):
        sql = ("INSERT INTO Buy (telegram_id, type, photo, caption, text) "
               "VALUES($1, $2, $3, $4, $5) returning id")
        return await self.execute(sql, telegram_id, type_, photo, caption, text, fetchrow=True)

    async def update_buy_comments(self, text, id_):
        sql = f"UPDATE Buy SET text=$1 WHERE id=$2"
        return await self.execute(sql, text, id_, execute=True)

    async def select_buy_by_id(self, id_):
        sql = f"SELECT * FROM Buy WHERE id='{id_}'"
        return await self.execute(sql, fetchrow=True)

    async def delete_buy_by_id(self, id_):
        await self.execute(f"DELETE FROM Buy WHERE id='{id_}'", execute=True)

    async def drop_table_buy(self):
        await self.execute("DROP TABLE Buy", execute=True)

    async def create_table_reports(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Reports (
        id SERIAL PRIMARY KEY,
        checked_date DATE DEFAULT CURRENT_DATE,
        telegram_id BIGINT NULL,
        car_brand TEXT NULL,
        car_model TEXT NULL,
        logistic_region TEXT NULL,
        logistic_type TEXT NULL,
        buy_type TEXT NULL
        );
        """
        await self.execute(sql, execute=True)

    async def add_reference_car(self, telegram_id, car_brand, car_model):
        sql = "INSERT INTO Reports (telegram_id, car_brand, car_model) VALUES($1, $2, $3) returning id, checked_date"
        return await self.execute(sql, telegram_id, car_brand, car_model, fetchrow=True)

    async def add_reference_logistic(self, telegram_id, logistic_region, logistic_type):
        sql = ("INSERT INTO Reports (telegram_id, logistic_region, logistic_type) "
               "VALUES($1, $2, $3) returning id, checked_date")
        return await self.execute(sql, telegram_id, logistic_region, logistic_type, fetchrow=True)

    async def add_reference_buy(self, telegram_id, buy_type):
        sql = "INSERT INTO Reports (telegram_id, buy_type) VALUES($1, $2) returning id, checked_date"
        return await self.execute(sql, telegram_id, buy_type, fetchrow=True)

    async def select_dates_cars(self):
        sql = f"SELECT DISTINCT checked_date FROM Reports WHERE car_brand IS NOT NULL"
        return await self.execute(sql, fetch=True)

    async def select_dates_logistics(self):
        sql = f"SELECT DISTINCT checked_date FROM Reports WHERE logistic_region IS NOT NULL"
        return await self.execute(sql, fetch=True)

    async def select_cars_date(self, date):
        sql = f"SELECT car_brand, car_model FROM Reports WHERE checked_date='{date}' AND car_brand IS NOT NULL"
        return await self.execute(sql, fetch=True)

    async def select_logistics_date(self, date):
        sql = (f"SELECT logistic_region, logistic_type FROM Reports WHERE checked_date='{date}' "
               f"AND logistic_region IS NOT NULL")
        return await self.execute(sql, fetch=True)

    async def select_cars_months(self):
        sql = 'SELECT * FROM Reports WHERE car_brand IS NOT NULL'
        return await self.execute(sql, fetch=True)

    # sql = ('SELECT checked_date, car_brand, car_model FROM Reports WHERE EXTRACT(MONTH FROM checked_date) = '
    #        'EXTRACT(MONTH FROM CURRENT_DATE) AND EXTRACT(YEAR FROM checked_date) = EXTRACT(YEAR FROM CURRENT_DATE)'
    #        ' AND car_brand IS NOT NULL')
    async def select_logistics_months(self):
        sql = 'SELECT * FROM Reports WHERE logistic_region IS NOT NULL'
        return await self.execute(sql, fetch=True)

    async def select_buy_months(self):
        sql = 'SELECT * FROM Reports WHERE buy_type IS NOT NULL'
        return await self.execute(sql, fetch=True)

    async def select_all_report(self):
        sql = f"SELECT * FROM Reports"
        return await self.execute(sql, fetch=True)

    async def delete_report_by_id(self, id_):
        await self.execute(f"DELETE FROM Report WHERE id='{id_}'", execute=True)

    async def drop_table_reports(self):
        await self.execute("DROP TABLE Reports", execute=True)

    async def create_table_feedback(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Feedback (
        id SERIAL PRIMARY KEY,        
        checked_date DATE DEFAULT CURRENT_DATE,
        telegram_id BIGINT NULL,        
        photo_id VARCHAR(200) NULL,
        caption VARCHAR(5000) NULL,
        text VARCHAR(4000) NULL     
        );
        """
        await self.execute(sql, execute=True)

    async def add_feedback(self, telegram_id, photo_id, caption, text):
        sql = ("INSERT INTO Feedback (telegram_id, photo_id, caption, text) "
               "VALUES($1, $2, $3, $4) returning id, checked_date")
        return await self.execute(sql, telegram_id, photo_id, caption, text, fetchrow=True)

    async def select_feedback_by_id(self, id_):
        sql = f"SELECT * FROM Feedback WHERE id='{id_}'"
        return await self.execute(sql, fetchrow=True)

    async def update_feedback_text(self, text, id_):
        sql = f"UPDATE Feedback SET text=$1 WHERE id=$2"
        return await self.execute(sql, text, id_, execute=True)

    async def delete_feedback_by_id(self, id_):
        await self.execute(f"DELETE FROM Feedback WHERE id='{id_}'", execute=True)

    async def drop_table_feedback(self):
        await self.execute("DROP TABLE Feedback", execute=True)
