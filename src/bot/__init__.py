import os

import asyncio
import logging

from aiogram import Bot, Dispatcher
from dotenv import find_dotenv, load_dotenv

from src.bot.user_private import router


load_dotenv(find_dotenv())
logging.basicConfig(level=logging.INFO)


class TeleBot:
    def __init__(self):
        self.bot = Bot(token=os.getenv('TOKEN'))
        self.dp = Dispatcher()
        self.dp.include_router(router)

        async def main():
            await self.dp.start_polling(self.bot)

        asyncio.run(main())
