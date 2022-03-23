from tkinter import *
import pandas as pd
import random as rd

to_learn = {}
try:
    flashcard_words = pd.read_csv("words_to_learn.csv")
except FileNotFoundError:
    og_flashcard_words = pd.read_csv("Day 31 FINAL data Capstone.csv")
    to_learn = og_flashcard_words.to_dict(orient="records")
else:
    to_learn = flashcard_words.to_dict(orient="records")
current_card = {}


# commands
def new_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = rd.choice(to_learn)
    canvas.itemconfig(language_txt, text="Italian", fill="black")
    canvas.itemconfig(word_txt, text=current_card["Italian"], fill="black")
    canvas.itemconfig(card, image=front_img)
    flip_timer = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(language_txt, text="English", fill="white")
    canvas.itemconfig(word_txt, text=current_card["English"], fill="white")
    canvas.itemconfig(card, image=back_img)


def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    unknown_data = pd.DataFrame(to_learn)
    unknown_data.to_csv("words_to_learn.csv", index=False)
    new_word()


# window
window = Tk()
window.title("Flashcards")
window.config(padx=20, pady=0, bg="#B1DDC6")
flip_timer = window.after(3000, func=flip_card)

# canvas
canvas = Canvas(width=800, height=526, highlightthickness=0, bg="#B1DDC6")
front_img = PhotoImage(file="card_front.png")
back_img = PhotoImage(file="card_back.png")
card = canvas.create_image(400, 263, image=front_img)
language_txt = canvas.create_text(400, 150, text="", fill="Black", font=("Ariel", 40, "italic"))
word_txt = canvas.create_text(400, 263, text="", fill="Black", font=("Ariel", 60, "bold"))
canvas.grid(row=1, column=1, columnspan=3)

# buttons
right_img = PhotoImage(file="right.png")
wrong_img = PhotoImage(file="wrong.png")
right_button = Button(image=right_img, highlightthickness=0, command=is_known)
wrong_button = Button(image=wrong_img, highlightthickness=0, command=new_word)
right_button.grid(row=2, column=3)
wrong_button.grid(row=2, column=1)

new_word()

window.mainloop()
