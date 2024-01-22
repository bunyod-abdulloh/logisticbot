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

    async def execute(
        self,
        command,
        *args,
        fetch: bool = False,
        fetchval: bool = False,
        fetchrow: bool = False,
        execute: bool = False,
    ):
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
        telegram_id BIGINT NOT NULL UNIQUE,
        full_name VARCHAR(60) NULL,
        username TEXT NULL,        
        phone TEXT NULL,
        language TEXT NULL 
        );
        """
        await self.execute(sql, execute=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join(
            [f"{item} = ${num}" for num, item in enumerate(parameters.keys(), start=1)]
        )
        return sql, tuple(parameters.values())

    async def add_user(self, telegram_id, language):
        sql = "INSERT INTO users (telegram_id, language) VALUES($1, $2) returning *"
        return await self.execute(sql,telegram_id, language, fetchrow=True)

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

    async def delete_users(self):
        await self.execute("DELETE FROM Users WHERE TRUE", execute=True)

    async def drop_users(self):
        await self.execute("DROP TABLE Users", execute=True)

    async def create_table_admin(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Admin (        
        telegram_id BIGINT NOT NULL UNIQUE,
        full_name VARCHAR(60) NULL,        
        description_uz VARCHAR(5000) NULL,
        description_ru VARCHAR(5000) NULL        
        );
        """
        await self.execute(sql, execute=True)

    async def add_admin(self, telegram_id, full_name):
        sql = "INSERT INTO Admin (telegram_id, full_name) VALUES($1, $2) returning *"
        return await self.execute(sql,telegram_id, full_name, fetchrow=True)

    async def update_description_uz(self, description_uz, telegram_id):
        sql = "UPDATE Admin SET description_uz=$1 WHERE telegram_id=$2"
        return await self.execute(sql,  description_uz, telegram_id, execute=True)

    async def select_admins_sql(self):
        sql = f"SELECT telegram_id, full_name FROM Admin "
        return await self.execute(sql, fetch=True)

    async def select_admin_sql(self, telegram_id):
        sql = f"SELECT telegram_id, full_name FROM Admin WHERE telegram_id='{telegram_id}'"
        return await self.execute(sql, fetch=True)

    async def select_desription_uz(self, telegram_id):
        sql = f"SELECT description_uz FROM Admin WHERE telegram_id='{telegram_id}'"
        return await self.execute(sql, fetchrow=True)

    async def delete_admin_sql(self, telegram_id):
        await self.execute(f"DELETE FROM Admin WHERE telegram_id='{telegram_id}'", execute=True)

    async def drop_table_admin(self):
        await self.execute("DROP TABLE Admin", execute=True)
