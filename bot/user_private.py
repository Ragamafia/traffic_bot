from aiogram import types, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


user_private_router = Router()

@user_private_router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer('Привет! Я могу рассказать тебе про траффик возле Аэропорта! Для продолжения, нажми "МЕНЮ"✈️'
    )


@user_private_router.message(Command('traffic'))
async def get_inline_btn_link(message: types.Message):
    await message.answer('Какой район вас интересует?)', reply_markup=links())


def links():
    link_list = [
        [InlineKeyboardButton(text='Ширямова к Аэропорту ', url='https://t.me/karban_flo')],
        [InlineKeyboardButton(text='Плотина ГЭС в Солнечный', url='https://t.me/karban_flo')],
        [InlineKeyboardButton(text='Плотина ГЭС к Мухиной', url='https://t.me/karban_flo')]
    ]
    return InlineKeyboardMarkup(inline_keyboard=link_list)
