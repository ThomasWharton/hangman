from src.utilities.words import get_word
from src.game import start_game

def restart_game():
    input_valid = False
    while not input_valid:
        restart = input("Play again? (Y/N): ").upper()
        if restart[0] == "Y":
            word = get_word()
            start_game(word)
            input_valid = True
        elif restart[0] == "N":
            input_valid = True
            exit()
        else:
            print("Input is invalid.\nPlease enter Y for yes and N for no.")