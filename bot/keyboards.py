from aiogram import types, Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup


router = Router()


@router.message(CommandStart())
async def start_cmd(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text='Запросить траффик'),
            types.KeyboardButton(text='Чат с разработчиком', url='https://t.me/raga_mafia')
        ],
        [types.KeyboardButton(text='Перейти на канал мастерской KARBAN 🌸', url='https://t.me/karban_flo')]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)

    await message.answer('Привет! Я помогу вам оценить обстановку с траффиком у аэропорта ✈️ \nЧто вы хотите сделать?',
                         reply_markup=keyboard,)


@router.message(F.text.lower() == "запросить траффик")
async def call_parser(message: types.Message):
    await message.reply('Должна залететь инфа от парсера')


#@router.message(Command('Запросить траффик'))
# async def call_parser(message: types.Message):
#     await message.reply('test1')

# @router.message(Command('traffic'))
# async def get_inline_btn_link(message: types.Message):
#     await message.answer('Что вас интересует? Выберите команду?)')

# @user_private_router.message(Command('request'))
# async def get_request(message: types.Message):
#     await message.answer('Нажата инлайн кнопка')

# def links():
#     link_list = [
#         [InlineKeyboardButton(text='Ширямова к Аэропорту ', )],
#         [InlineKeyboardButton(text='Чат с разработчиком', url='https://t.me/raga_mafia')],
#         [InlineKeyboardButton(text='Хочу перейти на канал мастерской KARBAN 🌸', url='https://t.me/karban_flo')]
#     ]
#     return InlineKeyboardMarkup(inline_keyboard=link_list)
