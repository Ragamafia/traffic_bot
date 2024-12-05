from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def links():
    link_list = [
        [InlineKeyboardButton(text='Запросить траффик ✈', callback_data='request')],
        [InlineKeyboardButton(text='Связаться с разработчиком', url='https://t.me/raga_mafia')],
        [InlineKeyboardButton(text='Перейти на канал мастерской KARBAN', url='https://t.me/karban_flo')]
    ]
    return InlineKeyboardMarkup(inline_keyboard=link_list, resize_keyboard=True)

