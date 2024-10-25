import os
import asyncio

from aiogram import Bot, Dispatcher
from dotenv import find_dotenv, load_dotenv

from user_private import user_private_router
import config as cfg

load_dotenv(find_dotenv())

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher()

dp.include_router(user_private_router)

async def main():
    await dp.start_polling(bot, allowed_updates=cfg.ALLOWED_UPDATES)

asyncio.run(main())
