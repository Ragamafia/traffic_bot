from aiogram import types, Router
from aiogram.filters import CommandStart, Command

from keyboards import links


router = Router()


@router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer('Пожалуйста, выберите что вас интересует?', reply_markup=links())


# @router.message(Command('traffic'))
# async def get_inline_btn_link(message: types.Message):
#     await message.answer('Пожалуйста, выберите что вас интересует?', reply_markup=links())
