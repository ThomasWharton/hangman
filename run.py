from src/utilities/welcome import welcome
from src/utilities/words import get_word
from src/utilities/display import display_hangman
from src/game import start_game

def main():
    username = welcome()
    print(f"Hey {username}, lets play a game of Hangman!\n")
    word = get_word()
    start_game(word)

main()