from words import get_word
from display import display_hangman

word = get_word()

def start_game(word):
    word_completion = "_" * len(word)
    guessed_correctly = False
    letters_guessed = []
    words_guessed = []
    lives = 6
    print("Hey name, lets play a game of Hangman!")
    print(display_hangman(lives))
    print(word_completion)

start_game(word)