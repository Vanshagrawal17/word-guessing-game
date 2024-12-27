import random
import nltk
from nltk.corpus import words

# Download the words corpus if you haven't already
nltk.download('words')

# Input from the user for their name
name = input("What is your name? ")

print("Good Luck!", name)

# Use a large collection of words from the nltk corpus
word_list = words.words()

# Randomly choose a word from the list
word = random.choice(word_list)

print("Guess the characters")

# String to store the user's guesses
guesses = ''

# Set the number of turns
turns = len(word)

# Main game loop
while turns > 0:
    # Variable to track the number of failed guesses
    failed = 0

    # Loop through each character in the word
    for char in word:
        # If the character is guessed, print it
        if char in guesses:
            print(char, end=" ")
        else:
            # If the character is not guessed, print a blank space
            print("_", end=" ")
            failed += 1

    # If there are no failed attempts, the player has guessed the word
    if failed == 0:
        print("\nYou Win!")
        print("The word is:", word)
        break

    # Ask the user to guess a character
    guess = input("\nGuess a character: ").lower()

    # Add the guessed character to the guesses string
    guesses += guess

    # If the guess is not in the word
    if guess not in word:
        # Reduce the number of turns by 1
        turns -= 1
        print("Wrong")
        print("You have", turns, 'more guesses')

    # If the player runs out of turns
    if turns == 0:
        print("You Lose! The word was:", word)
