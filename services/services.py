import random

import requests

from lexicon.lexicon_ru import LEXICON_RU

CATS_URL = 'https://api.thecatapi.com/v1/images/search'
DOGS_URL = 'https://api.thedogapi.com/v1/images/search'

def get_bot_choice() -> str:
    return random.choice(['rock', 'paper', 'scissors'])

def _normalize_user_answer(user_answer: str) -> str:
    for key in LEXICON_RU:
        if LEXICON_RU[key] == user_answer:
            return key
    raise Exception

def get_winner(user_choice: str, bot_choice: str) -> str:
    user_choice = _normalize_user_answer(user_choice)
    rules: dict[str,str] = {'rock': 'scissors',
                            'scissors': 'paper',
                            'paper':'rock'}
    if user_choice == bot_choice:
        return 'nobody_won'
    elif rules[user_choice] == bot_choice:
        return 'user_won'
    else:
        return 'bot_won'


def get_new_image(winner: str) -> str:
    if winner == 'user_won':
        response = requests.get(CATS_URL)
        response = response.json()
        return response[0].get('url')
    elif winner == 'bot_won':
        response = requests.get(DOGS_URL)
        response = response.json()
        return response[0].get('url')
    return 'Никто не победил'


def get_congratulation(winner: str) -> str:
    if winner == 'user_won':
        return random.choice(LEXICON_RU['user_won'])
    elif winner == 'bot_won':
        return random.choice(LEXICON_RU['bot_won'])
    return LEXICON_RU['nobody_won']

