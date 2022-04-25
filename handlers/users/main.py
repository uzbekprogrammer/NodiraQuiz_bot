from aiogram import types
from pprint import pprint
from data.config import ADMINS
from data.text import question
from loader import dp, bot


@dp.message_handler(commands="quiz")
async def poll(msg: types.Message):
    json1 = question
    quest = json1['question']
    options = json1['answer']
    correct = json1['explanation'] - 1
    message = await msg.answer_poll(question=quest,
                                    options=options,
                                    type='quiz',
                                    correct_option_id=correct,
                                    explanation=f'To\'g\'ri javob: {options[correct]}'
                                    )


@dp.poll_answer_handler()
async def some_poll_answer_handler(poll_answer: types.PollAnswer):

    print(poll_answer['poll_id'])
