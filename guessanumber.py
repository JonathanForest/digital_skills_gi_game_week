#/usr/bin/python3

"""
Guess a Number!

The aim here is to write a short program that will create a random number that the user (person
playing the game) will have to guess.

We've chosen to guess any number between 0 and 100, but to make it easier on the user we'll add
some functionality that will tell the user whether their guess was too high or too low.

Because of that, we'll have to make our program allow as many guesses as the user needs.

Skills we need to use:
    Data Types: ints and strings
    Variables
    Ifs
    Loops
"""


# Import the modules that will create the random numbers
import random

# This is the number that the users will try to guess
random_number = random.randrange(0, 100)

# Display a welcome message to the user
print("Hello! Welcome to the Guess a Number game!")

# We use a while loop because we don't know how many guesses the user will need
while True:

    # This get's the users guest, and saves it as a string
    guess = input("Enter your guess, between 0 and 100: ")

    # This converts the user's guess into an integer, which allows us to check whether it's higher,
    # lower or equal to our random_number.
    guess_number = int(guess)

    # Here we check whether it was too high, low or spot on!
    if guess_number > random_number:
        print("Your guess was too high! Try again...")
    if guess_number < random_number:
        print("Your guess was too low! Try again...")
    if guess_number == random_number:
        print("You guessed the number correctly! Well Done!")
        break

print("Thank you for playing!")



# Ways to improve?
#   - Sanitize the user inputs
#   - Keep track of how many guesses the user needed
#   - Save the scores to a file

