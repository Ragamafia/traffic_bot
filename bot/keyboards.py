from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Запросить траффик'),
            KeyboardButton(text='Связаться с разработчиком'),
        ],
        [
            KeyboardButton(text='Канал мастерской KARBAN'),
        ],
    ],
    resize_keyboard=True,
    input_field_placeholder='Выберите раздел',
)
