import os
import asyncio

from aiogram import Bot, Dispatcher
from dotenv import find_dotenv, load_dotenv

from user_private import user_private_router
import src.config as cfg

load_dotenv(find_dotenv())

dispatcher: Dispatcher = Dispatcher()


class TeleBot:
    def __init__(self):
        self.bot = Bot(token=os.getenv('TOKEN'))
        self.dp = Dispatcher()
        self.dp.include_router(user_private_router)

        async def main():
            await self.dp.start_polling(self.bot, allowed_updates=cfg.ALLOWED_UPDATES)

        # async def send_match(self, match):
        #     await self.send_message(match.get_message())

        asyncio.run(main())
