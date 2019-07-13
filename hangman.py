"""
Helper module for the hangman game. Contains all the functions needed ot run the game smoothly.
"""
import random
from string import ascii_lowercase as lowercase

import os
my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "words.txt")

def get_word(word_length):
    returned_word = None
    with open(path) as w:
        while (returned_word is None):
            for word in w:
                word = word.strip()
                if len(word) != word_length:
                    continue
                if random.randint(1,100) == 55:                 
                    returned_word = word
    return returned_word

def get_num_letters():
    """
    Get the number of letters the word contains.
    """
    while True:
        word_length = input("How many letters do you want the word to have? (4 <= Word Length <= 12) \n")
        try:
            word_length = int(word_length)
            if (4 <= word_length <= 12):
                return word_length
            else:
                print("Word length must be a number between 4 and 12")
        except:
            print("Word length must be a number between 4 and 12")
        print()

def get_num_tries(word_length):
    """
    Gets the number of wrong attempts the player is allowed.
    """
    message = "How many chances do you want? Enter an integer between 8 and " + str(26 - word_length) + '\n'
    error_message = "Invalid input. Please enter an integer between 8 and " + str(26 - word_length) + '\n'
    while True:
        num_chances = input(message)
        try:
            num_chances = int(num_chances)
            if (7 < num_chances <= (26 - word_length)):
                return num_chances
            else:
                print(error_message)
        except:
            print(error_message)

def convert_to_list(word):
    """
    Converts the word to a list of letters
    """
    split_word = []
    for letter in word:
        split_word.append(letter)
    return split_word

def convert_to_string(charlist):
    """
    Converts a list of chars to a string.
    pre: list must be a list of one character strings
    """
    string = ""
    for x in charlist:
        string += x
    return string

def readable_letters(list_of_letters):
    """
    A function to handle converting the list of remaining letters to a more readable form.
    """
    string = ''
    for i in range(len(list_of_letters) - 1):
        string += (list_of_letters[i] + ',')
    string += list_of_letters[len(list_of_letters) - 1]
    return string

def play_game(word_length, letter_list, num_chances):
    """
    Main function that handles gameplay and determines whether the user won/lost this round.
    """
    hidden_list = []
    for i in range(word_length):
        hidden_list.append('*')
    letters = convert_to_list(lowercase)
    already_input = []
    chances = num_chances

    while(chances > 0):
        if not('*' in hidden_list):
            return True
        print('\nThe word:   ' + convert_to_string(hidden_list))
        print("Letters remaining = " + readable_letters(letters))
        print("Wrong attempts remaining: " + str(chances))
        given_letter = str(input("Enter a letter: "))
        if not(given_letter in letters):
            if not(given_letter in already_input):
                print("Invalid input. You must input a letter from the English Alphabet.")
            else:
                print("You've already input " + repr(given_letter) + ". Input a letter you haven't already used.")
            continue
        else:
            letters.remove(given_letter)
            already_input.append(given_letter)
            if given_letter in letter_list:
                for i in range(len(letter_list)):
                    if letter_list[i] == given_letter:
                        hidden_list[i] = given_letter
                print("Correct. Well done.")
            else:
                print(repr(given_letter) + " isn't in the word.")
                chances -= 1
    else:
        return False
