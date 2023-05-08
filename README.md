# Hangman
Hangman is a Python terminal game, which is run in the Code Institute mock terminal and hosted on Heroku.

Users will be asked to guess a random word by typing in letters or words. The challenge is to guess the word before the poor man is hanged.

## How to play
Firstly, the user will be asked for their name and once submitted, the game will begin.

The user will be given a random word with each letter being represented by the **_** symbol. This will give the user the total length of the word.

They will then be prompted to input a letter or a word as their guess.

Letters guessed must be from within the standard English alphabet. Guessed words must be the same length as the randomly generated word and only contain characters from the standard English alphabet.

For each correct letter guessed, the **_** symbols will be replaced with the correctly guessed letter. For each incorrect guess (letter or word), the user will lose a life and the man will move one step closer to being hanged.

If the user correctly guesses the word, they will be presented with a congratulatory message and asked if they would like to play again.

If the user runs out of lives, the man will unfortunately be hanged, the user will be presente with a commiseratory message and asked if they would like to play again.

The user will be warned if they have already guessed a letter and told to guess again. This will not result in the loss of a life.

## Features

### Welcome Message

Upon loading, the user will be presented with a welcome message, detailing the game and how to begin.

### Username Prompt

The user will be prompted to submit a username and once provided, the game will begin.

### Hangman Gallows

Once the game begins, the empty gallows will be displayed and updated with each incorrect guess. Once the user is out of tries, the fully hanged man will be displayed.

### Word

A random word will be selected from an API or if unsuccessful in loading from the API, a word will be selected from a prewritten backup list.

The word will be displayed with each letter represented by the **_** symbol. With each correct letter guess, the correctly guessed letter(s) will then replace the underscore at the correct position in the word. 

### List of incorrect letters

The user will be presented a list of their already guessed letters which were incorrect. This will allow the user to keep track of what they have already tried.

### List of incorrect words

If the user incorrectly guesses a word, this word will be added to a list of incorrect word guesses and displayed for the user.

### Play again

Once the game is complete, whether that resulted in a win or a loss for the user, a prompt will appear for the user to start again by typing either y for yes and n for no.




