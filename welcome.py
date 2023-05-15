def welcome():
    accepted_username = False
    print(
        """
        =======================================================================================================
        ||Welcome to hangman!                                                                                ||
        ||Try to guess the word to save this poor man from being hanged.                                     ||
        ||Simply guess a letter or the entire word.                                                          ||
        ||For every incorrect guess, you will lose a life and the man will be one step closer to his demise! ||
        ||Guesses must be made up of letters contained in the standard English alphabet.                     ||
        ||If guessing a word, it must be of equal length to the chosen word.                                 ||
        ||Please enter your username to begin!                                                               ||
        =======================================================================================================
        """
    )
    
    while not accepted_username:
        print("Username must be between 1 and 10 characters and only contain letters from the English Alphabet.")
        username = input("Please enter a username: ")

        if len(username) in range(1,11) and username.isalpha():
            accepted_username = True
            return username
        else:
            print("The username entered does not meet requirements. Please try again.")
