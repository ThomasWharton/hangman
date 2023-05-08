import requests

def get_words():
    """
    Fetches a list of words from api.
    If fetch from api unsuccessful, uses backup list.
    """
    try:
        response = requests.get('https://random-word-api.herokuapp.com/word?number=100')
        word_list = response.json()
        return word_list
    except:
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
        return word_list


