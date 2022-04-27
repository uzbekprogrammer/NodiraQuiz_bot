from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove

from data.config import ADMINS
from data.text import question, test
from keyboards.default.Cancel import cancel
from keyboards.default.Quiz import main
from loader import dp, bot
from states.createquiz import CreateQuiz


@dp.message_handler(commands='new_quiz', chat_id=ADMINS)
async def quiz(msg: types.Message, state: FSMContext):
    await msg.reply('Savol kiritishingiz mumkin', reply_markup=cancel)
    await CreateQuiz.Question.set()


@dp.message_handler(state=CreateQuiz.Question)
async def qufh(msg: types.Message, state: FSMContext):
    message = msg.text
    test.update({
        'question': message
    })
    await msg.answer('Javoblarni kiriting', reply_markup=cancel)
    await CreateQuiz.Answer.set()


@dp.message_handler(state=CreateQuiz.Answer)
async def answers(msg: types.Message, state: FSMContext):
    message = msg.text

    list1 = list(message.split('\n'))
    test.update({
        'answer': list1
    })
    await msg.answer('Qaysi tartib raqamli javob to\'gri', reply_markup=cancel)
    await CreateQuiz.Tartib.set()


@dp.message_handler(state=CreateQuiz.Tartib)
async def tartibi(msg: types.Message, state: FSMContext):
    message = msg.text

    test.update({
        'explanation': int(message)
    })
    await msg.answer('Bajarildi', reply_markup=main)

    if question['explanation'] != test['explanation']:
        json1 = test.copy()
    else:
        json1 = question.copy()
    quest = json1['question']
    options = json1['answer']
    correct = json1['explanation'] - 1
    target_channel = ['@opencv_uzb']
    for i in target_channel:
        message = await bot.send_poll(chat_id=i,
                                      question=quest,
                                      options=options,
                                      type='quiz',
                                      correct_option_id=correct,
                                      explanation=f'To\'g\'ri javob: {options[correct]}'
                                      )

    await state.finish()
