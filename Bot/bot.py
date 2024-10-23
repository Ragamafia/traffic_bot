import os
import asyncio

from aiogram import types
from aiogram import Bot, Dispatcher

#import config as cfg
from user_private import user_private_router
#from bot_cmd_list import private

from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv())

ALLOWED_UPDATES = ['message, edited_message']

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher()

dp.include_router(user_private_router)

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    #await bot.set_my_commands(commands=private, scope=types.BotCommandScopeAllPrivateChats())
    await dp.start_polling(bot, allowed_updates=ALLOWED_UPDATES)

asyncio.run(main())
