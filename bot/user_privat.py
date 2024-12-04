from aiogram import types, Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards import start_kb

router = Router()


@router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer('Привет! Я помогу вам оценить обстановку с траффиком у аэропорта ✈️ \nЧто вас интересует?',
                         reply_markup=start_kb)


@router.message(F.text.lower() == "запросить траффик")
async def call_parser(message: types.Message):
    await message.reply('Ответ')


@router.callback_query(lambda call: call.data == 'Cвязаться с разработчиком')
async def chat_with_dev(callback_query: types.CallbackQuery):
    await callback_query.message.answer('test')


# def links():
#     link_list = [
#         [InlineKeyboardButton(text='Ширямова к Аэропорту ', )],
#         [InlineKeyboardButton(text='Чат с разработчиком', url='https://t.me/raga_mafia')],
#         [InlineKeyboardButton(text='Хочу перейти на канал мастерской KARBAN 🌸', url='https://t.me/karban_flo')]
#     ]
#     return InlineKeyboardMarkup(inline_keyboard=link_list)
