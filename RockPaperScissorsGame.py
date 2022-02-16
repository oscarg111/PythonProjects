import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
asciis = [rock, paper, scissors]
compSelection = random.randint(0, 2)
winMsg = "You win!!!"
looseMsg = "Sorry you lost."
userSelection = input("type 0 for rock, 1 for paper, and 2 for scissors")

if compSelection == 0 and int(userSelection) == 1:
    print(asciis[compSelection])
    print("Computer Chose rock")
    print(asciis[int(userSelection)])
    print("You chose paper")
    print(winMsg)
elif compSelection == 1 and int(userSelection) == 0:
    print(asciis[compSelection])
    print("Computer Chose paper")
    print(asciis[int(userSelection)])
    print("You chose rock")
    print(looseMsg)
elif compSelection == 0 and int(userSelection) == 2:
    print(asciis[compSelection])
    print("Computer Chose rock")
    print(asciis[int(userSelection)])
    print("You chose scissors")
    print(looseMsg)
elif compSelection == 1 and int(userSelection) == 2:
    print(asciis[compSelection])
    print("Computer Chose paper")
    print(asciis[int(userSelection)])
    print("You chose scissors")
    print(winMsg)
elif compSelection == 2 and int(userSelection) == 0:
    print(asciis[compSelection])
    print("Computer Chose scissors")
    print(asciis[int(userSelection)])
    print("You chose rock")
    print(winMsg)
elif compSelection == 2 and int(userSelection) == 1:
    print(asciis[compSelection])
    print("Computer Chose scissors")
    print(asciis[int(userSelection)])
    print("You chose paper")
    print(looseMsg)
else:
    print(asciis[compSelection])
    print(asciis[int(userSelection)])
    print("You tied.")