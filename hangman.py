"""
Hangman!

Ways to improve:
    Sanitize the inputs: multiple letters? numbers? What about upper or lower case?
    Use List Comprehension to generate the 'word_to_print'
    Break this code into separate functions so it looks nicer?
    Is there a Python Data Type that we could use instead to store the guessed_letters? Hint, there
        is...

"""

import os

# Rather than having a preset list of words, let's make this a two player game!
secret_word = input("Player 1: Please enter a word for player 2 to guess: ")

os.system('clear')

# For added complexity, we have added difficulty levels
difficulty = input("Player 1: Please enter a difficulty level 1-3: ")

os.system('clear')

if difficulty == "1":
    allowed_guesses = 9
if difficulty == "2":
    allowed_guesses = 7
if difficulty == "3":
    allowed_guesses = 5

# We need to record the guessed letters, as if you guess the same letter twice I don't want you to
# lose a guess.
guessed_letters = []

# We're using a while loop here as we don't know how many guesses the player will need.
while allowed_guesses > 0:

    letter = input("Please enter a single letter: ")

    # Here, we skip the code below if the player enters in a letter they have already used.
    # If it's a new letter though, we add it to the guessed letters list.
    if letter in guessed_letters:
        print("You have already guessed that letter, please enter a different one!")
        continue
    else:
        guessed_letters.append(letter)

    # As I mentioned earlier, we only want to remove a guess if the letter wasn't in the
    # secret_word.
    if letter not in secret_word:
        allowed_guesses = allowed_guesses - 1

    # Here we create the string that contains all the letters of the secret_word we have guessed.
    # If we have guessed the letter, we show that letter, if we haven't, we print an underscore
    # instead.
    word_to_print = ""
    for secret_letter in secret_word:
        if secret_letter in guessed_letters:
            word_to_print = word_to_print + secret_letter
        else:
            word_to_print = word_to_print + "_"

    unknown_letters = word_to_print.count("_")

    print(word_to_print)
    print("Guesses Left: ", allowed_guesses)

    # If there are no underscores, it means that we have guessed every letter in the word, and won!
    if unknown_letters == 0:
        print("You have won! The word was: ", word_to_print)
        break

    # However, if guesses is 0, then we have used all our guesses without getting the word right,
    # so we've lost :(
    if allowed_guesses == 0:
        print("You have run out of guesses! The word was: ", secret_word)
        break


