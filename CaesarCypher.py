alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
from art import caesarCypherLogo
"""
make it keep running if user enters yes and stop if user enters no

if massive number entered, make it so that application still works
"""
print(caesarCypherLogo)
def caesar(text, shift, direction):
    result = ""
    if direction == "decode":
        shift *= -1
    for letter in text:
        if letter in alphabet:
            index = alphabet.index(letter)
            index += shift
            if index > 25:
                index -= 26
            result += alphabet[index]
        else:
            result += letter
    print(result)

userInput = "yes"
while userInput == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if shift > 26:
        shift %= 26
    caesar(text, shift, direction)
    userInput = input("Do you want to continue? (yes or no)\n").lower()

