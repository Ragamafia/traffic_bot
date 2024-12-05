from aiogram import types, Router, F
from aiogram.filters import CommandStart, Command

from src.bot.keyboards import links
from src.parser import create_message


router = Router()


@router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer('Пожалуйста, выберите что вас интересует?', reply_markup=links())


@router.callback_query(F.data == 'request')
async def get_request(callback: types.CallbackQuery):
    await callback.message.answer(create_message())
    await callback.answer(text='Для повторного выбора нажмите "Меню"', show_alert=True)

@router.message(Command('traffic'))
async def repeat_call(message: types.Message):
    await message.answer('Пожалуйста, выберите что вас интересует?', reply_markup=links())
