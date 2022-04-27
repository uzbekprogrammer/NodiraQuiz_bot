from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


main = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='ℹKutubxona xaqida'),
            KeyboardButton(text='📈Statistika')
        ],
        [
            KeyboardButton(text="📝Test bajarish"),
        ],
    ],
    resize_keyboard=True
)
