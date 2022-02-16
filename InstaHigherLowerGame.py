import random
from art import HigherLowerVs, HigherLowerLogo
from HigherLowerData import data

print(HigherLowerLogo)

"""
'Game' function:
    I will start off by printing two instagram accounts separated by 'vs', then I will ask the user 
    to guess which account has the higher number of followers. 
     
'Compare' function:
    I will input two instagram accounts and the user guess, then return True if the user guess is 
    correct, and False if the user guess is incorrect. 
    
'Description' function:
    Will put the random celebrity into string form.

Note: I must implement a way in which the higher celebrity stays on the board
'Stay' function:
    returns the higher follower celebrity
"""

print("Welcome to the Higher Lower game!\n\n")

# global variable that declares the amount of points attained throughout the game and first account
points = 0
account1 = random.choice(data)

def game():
    global points
    global account1

    # gets random accounts from data import
    account2 = random.choice(data)

    # returns which account is greater
    higher_follow_count = more_followers(acc1=account1, acc2=account2)

    # prints the status of the game
    print(f"You have {points} points.")

    # prints the accounts that will be compared
    print("Compare A: " + description(account1))
    print(HigherLowerVs)
    print("Against B: " + description(account2))

    # gets user input
    user_a_or_b = input("\n\nChoose either A or B:\n").upper()

    # if account1 is not the highest follower count, sets account1 to the higher follower count
    if account1.get('follower_count') < higher_follow_count.get('follower_count'):
        account1 = higher_follow_count

    # adds one to points based on the accuracy of the user guess
    if compare_the_celebrities(acc1=account1, acc2=account2, user_guess=user_a_or_b):
        points+=1
        game()
    else:
        print(f"You have guessed incorrectly, the game is now over.\n"
              f"You finished with {points} points.")

def description(account):
    return account.get('name') + ", a " + account.get('description') + ", from " + account.get("country") + "."

def compare_the_celebrities(acc1, acc2, user_guess):
    # compares the follower amount of account 1 to that of account 2
    acc1_greater_than_acc2 = acc1.get('follower_count') > acc2.get('follower_count')

    # returns boolean value based on user guess and previous boolean value
    if acc1_greater_than_acc2 and user_guess == 'A':
        return True
    elif not acc1_greater_than_acc2 and user_guess == 'B':
        return True
    else:
        return False

def more_followers(acc1, acc2):
    if acc1.get('follower_count') > acc2.get('follower_count'):
        return acc1
    else:
        return acc2

game()
