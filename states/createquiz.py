from aiogram.dispatcher.filters.state import StatesGroup, State


class CreateQuiz(StatesGroup):
    Question = State()
    Answer = State()
    Tartib = State()
