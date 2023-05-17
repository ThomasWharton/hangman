# Hangman
Hangman is a Python terminal game, which is run in the Code Institute mock terminal and hosted on Heroku.

Users will be asked to guess a random word by typing in letters or words. The challenge is to guess the word before the poor man is hanged.

![Responsive Mockup](docs/screenshots/amiresponsive.png)

## How to play
Firstly, the user will be asked for their name and once submitted, the game will begin.

The user will be given a random word with each letter being represented by the **_** symbol. This will give the user the total length of the word.

They will then be prompted to input a letter or a word as their guess.

Letters guessed must be from within the standard English alphabet. Guessed words must be the same length as the randomly generated word and only contain characters from the standard English alphabet.

For each correct letter guessed, the **_** symbols will be replaced with the correctly guessed letter. For each incorrect guess (letter or word), the user will lose a life and the man will move one step closer to being hanged.

If the user correctly guesses the word, they will be presented with a congratulatory message and asked if they would like to play again.

If the user runs out of lives, the man will unfortunately be hanged, the user will be presented with a commiseratory message and asked if they would like to play again.

The user will be warned if they have already guessed a letter and told to guess again. This will not result in the loss of a life.

## Features

### Welcome Message

Upon loading, the user will be presented with a welcome message, detailing the game and how to begin.

![Welcome Message](docs/screenshots/welcome.png)

### Username Prompt

The user will be prompted to submit a username and once provided, the game will begin. The user is notified that their username must be between 1 and 10 characters and only contain letters included in the standard English alphabet. If the username does not meet the requirements, the user will be notified that it is not valid and to try again. Once a valid username has been entered, the game will begin.

*Username Input*<br>
![Username Input](docs/screenshots/username-prompt.png)

*Username Validation*<br>
![Username Validation](docs/screenshots/username_validation.png)

### Hangman Gallows

Once the game begins, the empty gallows will be displayed and updated with each incorrect guess. Once the user is out of tries, the fully hanged man will be displayed.

*Start of Game*<br>
![Start of Game](docs/screenshots/start_of_game.png)

*Incorrect Guess*<br>
![Incorrect Guess](docs/screenshots/incorrect_letter.png)

### Word

A random word will be selected from an API or if unsuccessful in loading from the API, a word will be selected from a prewritten backup list. The API used is from [random-word-api](http://random-word-api.herokuapp.com/home "random-word-api") and creates a list of 100 words to select from.

The word will be displayed with each letter represented by the **_** symbol. With each correct letter guess, the correctly guessed letter(s) will then replace the underscore at the correct position in the word.

*Letters Guessed Correctly*<br>
![Letters Guessed Correctly](docs/screenshots/correct_letters.png)

### List of guessed letters

The user will be presented a list of their already guessed letters. This will allow the user to keep track of what they have already tried.

### List of guessed words

If the user incorrectly guesses a word, this word will be added to a list of incorrect word guesses and displayed for the user.

*Word Guessed*<br>
![Word Guessed](docs/screenshots/word_guessed.png)

### Guess Validation

If the user tries to guess multiple letters which is not equal to the length of the word, an error will occur and the user will be notified that their guess is not valid. The same will happen if the user tries to submit a character not within the standard English alphabet.

*Invalid Word Length Validation*<br>
![Invalid Length Guess](docs/screenshots/guess_validation.png)

*Invalid Character Guess*<br>
![Invalid Character Guess](docs/screenshots/guess_validation2.png)

### Completion Message

The user will receive either a congratulatory or commiseratory message depending on whether they were successful or not.

*Congratulatory Message*<br>
![Congratulatory Message](docs/screenshots/success_message.png)

*Commiseratory Message*<br>
![Commiseratory Message](docs/screenshots/failure_message.png)

### Play again

Once the game is complete, whether that resulted in a win or a loss for the user, a prompt will appear for the user to start again by typing either Y for yes and N for no. If the user inputs a character other than Y or N, a validation error will occur. The user can also submit a lowercase Y or N and yes or no as validation is done by splicing the first letter and converting to uppercase.

*Play Again Validation*<br>
![Play Again Validation](docs/screenshots/play_again_validation.png)

## Testing

Thorough testing has been completed throughout the project's development. Upon completion, testing has been carried out to ensure all features work correctly and all user inputs go through validation. All information regarding feature testing is displayed in the table below.

| Feature Tested        | Feature Description                                                                                                           | Testing Completed                                                                                                                              | Expected Outcome                                                                                                                                                                                                                                                                                      | Result       |
|-----------------------|-------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|
| Welcome Message       | Welcome message and username <br>input field displayed.                                                                       | Run program.                                                                                                                                   | Welcome message and username<br>should be displayed.                                                                                                                                                                                                                                                  | As expected. |
| Username Input        | User can input username adhering<br>to requirements.                                                                          | Input invalid and valid<br>username.                                                                                                           | Upon invalid username input,<br>user will be notified that it<br>is not valid and to try again.<br>Upon valid input, game will start.                                                                                                                                                                 | As expected. |
| Get Word              | Random word pulled from API list<br>or backup list.                                                                           | Fetch word from API and<br>from backup list. Tested via<br>printing fetched word. To test<br>backup list, API URL was made to<br>be incorrect. | Word should be selected at random from<br>API fetched list or from backup list if<br>API fetch fails.                                                                                                                                                                                                 | As expected. |
| Start Game Message    | Message appears at game start with<br>given username.                                                                         | Input username to initiate game<br>start.                                                                                                      | Message should appear at game start<br>which includes username given by user.                                                                                                                                                                                                                         | As expected. |
| Display Hangman       | Display hangman at different stages.                                                                                          | Start game to initiate display of<br>first stage and intentionally lose<br>lives to display further stages of <br>hangman gallows.             | Hangman gallows should first display<br>empty and update with every life lost.                                                                                                                                                                                                                        | As expected. |
| Word length Message   | User notified of the length of word.                                                                                          | Start game to initiate display if<br>word length message.                                                                                      | Message with length of word should be<br>displayed.                                                                                                                                                                                                                                                   | As expected. |
| Display Word          | Word displayed with every letter<br>initially replaced with underscore.                                                       | Start game to initiate display of<br>hidden word.                                                                                              | Hidden word should be displayed as a <br>number of underscores equal to length<br>of word.                                                                                                                                                                                                            | As expected. |
| Guess Input           | Input field for user to submit guess                                                                                          | Start game to initiate guess input<br>field.                                                                                                   | Guess input field should appear at bottom<br>of game.                                                                                                                                                                                                                                                 | As expected. |
| Guess Validation      | Validates user guesses.                                                                                                       | Try valid and invalid guesses.                                                                                                                 | Upon invalid guess, user should be notified<br>that guess and told to guess again. User <br>should not lose life for invalid guess. <br>If guess has already been tried, user should<br>be notified and not lose a life. If valid,<br>user should be notified whether or not it<br>guess was correct. | As expected. |
| Update Word           | Upon successful letter guess, hidden<br>word will update to display correct<br>letter guessed at correct position in<br>word. | Guess letter correctly.                                                                                                                        | If letter guessed is correct, hidden word<br>should update to replace underscores with<br>correct letter at correct position.                                                                                                                                                                         | As expected. |
| Letters Guessed List  | Any letters guessed will be added to <br>list and displayed for user.                                                         | Guess letters.                                                                                                                                 | When a letter is guessed by user, letters<br>guessed list should update and be displayed<br>for user.                                                                                                                                                                                                 | As expected. |
| Words Guessed List    | Incorrect words guessed will be<br>added to list and displayed for user.<br>If correct word guessed, game will end.           | Guess words.                                                                                                                                   | When an incorrect word is guessed, words<br>guessed list updated and displayed for user.<br>If correct word is guessed, game will end.                                                                                                                                                                | As expected. |
| Completion Message    | Upon game completion, message will be<br>displayed congratulating or commiserating<br>user.                                   | Complete game by failing and<br>winning.                                                                                                       | When user wins, congratulatory message<br>should display and commiseratory message<br>when user loses.                                                                                                                                                                                                | As expected. |
| Play Again Prompt     | Upon game completion, user is asked if<br>they would like to play again.                                                      | Complete game.                                                                                                                                 | When game completed, prompt should appear<br>to allow user to close game or start again.<br>Game should restart if user input yes and<br>program should exit if input is no.                                                                                                                          | As expected. |
| Play Again Validation | Validate play again input from user.                                                                                          | Invalid input given to play again<br>prompt.                                                                                                   | If user gives invalid input to play again <br>prompt they should be notified and allowed<br>to try again.                                                                                                                                                                                             | As expected. |




