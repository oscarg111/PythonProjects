import pandas as pd

nato_data = pd.read_csv("nato_phonetic_alphabet.csv")
nato_data_dict = {row.letter: row.code for (index, row) in nato_data.iterrows()}


def generate_nato():
    user_input = input("What do you want to convert to nato alphabet?\n").upper()
    try:
        user_array = [nato_data_dict[letter] for letter in user_input]
    except KeyError:
        print("sorry, only letters")
        generate_nato()
    else:
        print(user_array)


generate_nato()
