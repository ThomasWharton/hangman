from src.utilities.words import get_word
from src.game import start_game

def restart_game():
    """
    Creates input to ask user if they would like to play again.
    Restarts game or closes app depending on user input.
    """
    input_valid = False
    while not input_valid:
        restart = input("Play again? (Y/N): ").upper()
        if restart[0] == "Y":
            word = get_word()
            start_game(word)
            input_valid = True
        elif restart[0] == "N":
            exit()
        else:
            print("Input is invalid.\nPlease enter Y for yes and N for no.")