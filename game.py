from words import get_word
from display import display_hangman

word = get_word()

def start_game(word):
    word_completion = "_" * len(word)
    guessed_correctly = False
    letters_guessed = []
    words_guessed = []
    lives = 6
    print("Hey name, lets play a game of Hangman!\n")
    print(display_hangman(lives))
    print(word_completion)
    print("\n")

    while not guessed_correctly and lives > 0:
        guess = input("Guess a letter or a word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in letters_guessed:
                print(f"Sorry! You already guessed the letter {guess}. Please try again.")
            elif guess not in word:
                print (f"Unlucky! {guess} is not in the word.")
                lives -= 1
                letters_guessed.append(guess)
            else:
                print (f"Well Done! {guess} is in the word")
                letters_guessed.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed_correctly = True

        elif len(guess) == len(word) and guess.isalpha():
            if guess in words_guessed:
                print(f"Sorry! You already guessed the word {guess}. Please try again.")
            elif guess != word:
                print(f"Unlucky! {guess} is not the word!")
                lives -= 1
                words_guessed.append(guess)
            else:
                guessed_correctly = True
                word_completion = word

        else:
            print("Your guess is not valid. Please try again.")
        print(display_hangman(lives))
        print(word_completion)
        print("\n")
    
    if guessed_correctly:
        print("Congratulations! You guessed the word correctly and saved this poor man's life!")
    else:
        print(f"Commiserations! You ran out of lives and the poor man has been hanged! The word was {word}!")


start_game(word)