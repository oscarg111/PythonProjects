from art import GuessTheNumberLogo
import random

print(GuessTheNumberLogo)

"""
The aim of the challenge is to create a guess the number game in which users will start
out by selecting easy or hard difficulty.  If easy is selected, they have 10 opportunities
to guess the number, and if hard is selected, they have 5 opportunities to select the number. 
while guessing, the console displays if the number guessed is too high or too low.
"""

# user inputs their chosen difficulty
difficulty = input("Welcome to guess the number! pick a difficulty:\n"
                   "either \"easy\" or \"hard\".").lower()
print("I am thinking of a number between 1 and 100")

# picks a random number within the constraints and assigns a user guess so the
# initial while loop is able to execute.
random_number = random.randint(1, 100)
user_guess = 0

# by default, guesses is equal to 10.  if the user decides on hard, it will be lowered to 5
guesses = 10

if difficulty == "hard":
    guesses = 5

# counter for attempts the user has made
attempts = guesses

while attempts > 0 and user_guess != random_number:
    print(f"You have {attempts} attempts remaining.")
    user_guess = int(input("Guess your number:\n"))
    attempts -= 1
    if user_guess > random_number:
        print("Too high!")
    elif user_guess < random_number:
        print("Too low!")

if user_guess == random_number:
    print(f"The number was {random_number}.")
    print("Congratulations! you have won the game!")
else:
    print(f"The number was {random_number}.")
    print("Sorry, you have lost the game.")