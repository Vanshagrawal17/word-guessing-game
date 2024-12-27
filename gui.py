import random
import nltk
from nltk.corpus import words
import tkinter as tk
from tkinter import messagebox

# Download the words corpus if you haven't already
nltk.download('words')

# Initialize word list from the NLTK corpus
word_list = words.words()

# Function to start the game
def start_game():
    global word, guesses, turns
    guesses = ''
    word = random.choice(word_list).lower()  # randomly choose a word
    turns = len(word)
    word_label.config(text="_ " * len(word))  # display underscores representing the word
    guess_entry.delete(0, tk.END)  # clear the input field

# Function to process the user's guess
def guess_char():
    global turns, guesses

    guess = guess_entry.get().lower()
    guess_entry.delete(0, tk.END)  # clear the input field

    if len(guess) == 0:
        messagebox.showinfo("Error", "Please enter a character.")
        return

    if guess in guesses:
        messagebox.showinfo("Error", "You have already guessed this character.")
        return

    guesses += guess
    failed = 0
    display_word = ""

    # Build the display for the word
    for char in word:
        if char in guesses:
            display_word += char + " "
        else:
            display_word += "_ "
            failed += 1

    word_label.config(text=display_word.strip())

    if failed == 0:
        messagebox.showinfo("Congratulations!", "You Win! The word is: " + word)
        start_game()

    if guess not in word:
        turns -= 1
        attempts_label.config(text="Attempts left: " + str(turns))
        if turns == 0:
            messagebox.showinfo("Game Over", "You Lose! The word was: " + word)
            start_game()

# GUI Setup
root = tk.Tk()
root.title("WORD GUESS")

# Add the UI elements
title_label = tk.Label(root, text="Hangman Game", font=("Helvetica", 20))
title_label.pack(pady=10)

word_label = tk.Label(root, text="_ _ _ _ _", font=("Helvetica", 18))
word_label.pack(pady=20)

attempts_label = tk.Label(root, text="Attempts left: 0", font=("Helvetica", 14))
attempts_label.pack(pady=10)

guess_entry = tk.Entry(root, font=("Helvetica", 14))
guess_entry.pack(pady=10)

guess_button = tk.Button(root, text="Guess", command=guess_char, font=("Helvetica", 14))
guess_button.pack(pady=10)

# Start the game
start_game()

root.mainloop()
