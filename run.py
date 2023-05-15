# from src.utilities.welcome import welcome
# from src.utilities.words import get_word
# from src.game import start_game

import src

def main():
    username = src.welcome()
    print(f"Hey {username}, lets play a game of Hangman!\n")
    word = src.get_word()
    src.start_game(word)  

main()
