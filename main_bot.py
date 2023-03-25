from aiogram import types , executor
from help_for_bot import dp
from handlers import user 
import logging
from sql import sql

logging.basicConfig(level=logging.INFO)

async def start(_):
    await sql.sql_start()
    print('Бот вышел на связь')

user.handlers_client(dp)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True , on_startup=start)