from aiogram import Router
from aiogram.filters import Command, CommandStart, Text
from aiogram.types import Message
from keyboards.keyboards import game_kb, yes_no_kb
from lexicon.lexicon_ru import LEXICON_RU
from services.services import get_bot_choice, get_winner, get_new_image, get_congratulation
from aiogram.types import CallbackQuery


router: Router = Router()


@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=LEXICON_RU['/start'], reply_markup=yes_no_kb)


@router.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU['/help'], reply_markup=yes_no_kb)


@router.message(Text(text=LEXICON_RU['yes_button']))
async def process_yes_answer(message: Message):
    await message.answer(text=LEXICON_RU['yes'], reply_markup=game_kb)


@router.message(Text(text=LEXICON_RU['no_button']))
async def process_no_answer(message: Message):
    await message.answer(text=LEXICON_RU['no'])


@router.message(Text(text=LEXICON_RU['big_button']))
async def process_big_button(message: Message):
    await message.answer(text=LEXICON_RU['big_button_ans'], reply_markup=game_kb)


@router.message(Text(text=[LEXICON_RU['rock'],
                           LEXICON_RU['paper'],
                           LEXICON_RU['scissors']]))
async def process_game_button(message: Message):
    bot_choice = get_bot_choice()
    await message.answer(text=f"{LEXICON_RU['bot_choice']} "
                              f"{LEXICON_RU[bot_choice]}")
    winner = get_winner(message.text, bot_choice)
    print(winner)
    image = get_new_image(winner)
    congrats = get_congratulation(winner)
    if not winner == 'nobody_won':
        if 'gif' in image:
            await message.answer_animation(animation=image,
                                           caption=congrats,
                                           reply_markup=yes_no_kb)

        # await message.answer(text=LEXICON_RU[winner], reply_markup=yes_no_kb)
        else:
            await message.answer_photo(photo=image,
                                       caption=congrats,
                                       reply_markup=yes_no_kb)
    else:
        await message.answer(text=congrats,
                             reply_markup=yes_no_kb)


@router.callback_query(Text(text=['big_button']))
async def big_button_1_process(callback: CallbackQuery):
    text = LEXICON_RU['big_button_ans']
    if callback.message.text != text:
        await callback.message.edit_text(
            text='Большая кнопка 1 нажата',
            reply_markup=callback.message.reply_markup
        )
        # print(callback.json(indent=4, exclude_none=True))
    await callback.answer(text=text)
