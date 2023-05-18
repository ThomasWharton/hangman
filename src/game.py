import src


def restart_game():
    """
    Creates input to ask user if they would like to play again.
    Restarts game or closes app depending on user input.
    """
    input_valid = False
    while not input_valid:
        restart = input("Play again? (Y/N): ").upper()
        if restart[0] == "Y":
            word = src.get_word()
            start_game(word)
            input_valid = True
        elif restart[0] == "N":
            exit()
        else:
            print("Input is invalid.\nPlease enter Y for yes and N for no.")


def start_game(word):
    """
    Start game and ask user for input.
    """
    word_completion = "_" * len(word)
    guessed_correctly = False
    letters_guessed = []
    words_guessed = []
    lives = 6
    print(src.display_hangman(lives))
    print(f"The word is {len(word)} characters long.\n")
    print(word_completion, "\n")

    while not guessed_correctly and lives > 0:
        guess = input("Guess a letter or a word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in letters_guessed:
                print(f"Sorry! You already guessed the letter {guess}. Please try again.")  # noqa
            elif guess not in word:
                print(f"Unlucky! {guess} is not in the word.")
                lives -= 1
                letters_guessed.append(guess)
            else:
                print(f"Well Done! {guess} is in the word")
                letters_guessed.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]  # noqa
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed_correctly = True

        elif len(guess) == len(word) and guess.isalpha():
            if guess in words_guessed:
                print(f"Sorry! You already guessed the word {guess}. Please try again.")  # noqa
            elif guess != word:
                print(f"Unlucky! {guess} is not the word!")
                lives -= 1
                words_guessed.append(guess)
            else:
                guessed_correctly = True
                word_completion = word

        else:
            print("Your guess is not valid. Please try again.")

        print(src.display_hangman(lives))
        print(f"The word is {len(word)} characters long.\n")
        print(word_completion, "\n")
        print(f"Letters guessed: {letters_guessed}")
        print(f"Words guessed: {words_guessed}", "\n")

    if guessed_correctly:
        print("Congratulations! You guessed the word correctly and saved this poor man's life!\n")  # noqa
    else:
        print(f"Commiserations! You ran out of lives and the poor man has been hanged!\nThe word was {word}!\n")  # noqa

    restart_game()