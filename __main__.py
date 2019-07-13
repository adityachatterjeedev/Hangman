"""
This is a simple text-based version of the popular game Hangman I decided to write because I had two hours of 
free time.

Author: Aditya Chatterjee
Date: July 9, 2019
"""

from hangman import get_word, get_num_letters, get_num_tries, convert_to_list, play_game
from string import ascii_lowercase as lowercase 

def new_game():
    """
    An instance of a game. Keeps playing the game until the player decides to stop.
    """
    start_string = 'New Game'.center(60, '*')
    print(start_string)
    print("Welcome to a new game of Hangman.")
    word_length = get_num_letters()
    num_chances = get_num_tries(word_length)
    word = get_word(word_length)
    letter_list = convert_to_list(word)
    if play_game(word_length, letter_list, num_chances):
        print("Well done. You've won this round.")
    else:
        print("The word was: " + word)
        print("Hard luck. I'm sure you'll do better next time.")
    cont = str(input("Do you want to play again? (y/n) "))
    cont = cont.strip().lower()
    if cont == 'y':
        return True
    else:
        print("Thanks for playing. See you next time!")
        return False

if __name__ == '__main__':
    while new_game():
        print()