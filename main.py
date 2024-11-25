from typing import final

import pandas

# read csv file
nato_alphabets = pandas.read_csv("nato_phonetic_alphabet.csv")

# create a dictionary variable for the read file
nato_dictionary = {value.letter:value.code for (key, value) in nato_alphabets.iterrows()}

on = True

while on:
# getting user input
    user_input = input("Enter a word: ").upper()

    try:
        answer = [nato_dictionary[word] for word in user_input]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
    else:
        print(answer)
        on = False

# I could've defined a function instead of a loop and used recursion on the...
# except block to get the code to repeat.
