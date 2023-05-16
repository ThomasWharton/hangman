import requests
import random


def get_word():
    """
    Fetches a list of words from api and picks random word from it.
    If fetch from api unsuccessful, uses backup list.
    """
    try:
        response = requests.get('https://random-word-api.herokuapp.com/word?number=100')
        word_list = response.json()
        word = random.choice(word_list).upper()
        return word
    except api_call_failure:
        word_list = [
            'congratulate',
            'triumph',
            'special',
            'pushes',
            'orange',
            'prevent',
            'opening',
            'systems',
            'obliterate',
            'culture',
            'computing',
            'programme',
            'beginning',
            'populate',
            'entertain',
            'transform',
            'apologetic',
            'enormous',
            'competitive',
            'imagine'
            ]
        word = random.choice(word_list).upper()
        return word