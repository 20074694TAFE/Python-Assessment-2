#!/usr/bin/env python3
"""Guess-My-Word is a game where the player has to guess a word.
<your description> 
Author: <name>
Company: <company>
Copyright: <year>

"""
# Your code must use PEP8
# Your code must be compatible with Python 3.1x
# You cannot use any libraries outside the python standard library without the explicit permission of your lecturer.

# This code uses terms and symbols adopted from the following source:
# See https://github.com/3b1b/videos/blob/68ca9cfa8cf5a41c965b2015ec8aa5f2aa288f26/_2022/wordle/simulations.py#L104


from random import choice
from sys import stdout


MISS = 0  # _-.: letter not found ⬜
MISSPLACED = 1  # O, ?: letter in wrong place 🟨
EXACT = 2  # X, +: right letter, right place 🟩

MAX_ATTEMPTS = 6
WORD_LENGTH = 5

ALL_WORDS = 'word-bank/all_words.txt'
TARGET_WORDS = 'word-bank/target_words.txt'
# TODO: Add linebreak after each guess
# TODO: Add guesses after each guess

def play():
    """Code that controls the interactive game play"""
    # select a word of the day:
    word_of_the_day = get_target_word()
    # build a list of valid words (words that can be entered in the UI):
    valid_words = get_valid_words()
    # do the following in an iteration construct
    guesses = 0
    while True:
        guess = ask_for_guess(valid_words)
        score = score_guess(guess, word_of_the_day)
        print("Result of your guess:")  # Put some of your own personality into this!
        print(format_score(guess, score))
        guesses += 1
        if is_correct(score):
            print("Winner: You guessed a total of " + str(guesses) + " times")
            return True
        if guesses >= MAX_ATTEMPTS:
            print("You've ran out of guesses")
            return False
    # end iteration
    # return True


def is_correct(score):
    """Checks if the score is entirely correct and returns True if it is
    Examples:
    >>> is_correct((1,1,1,1,1))
    False
    >>> is_correct((2,2,2,2,1))
    False
    >>> is_correct((0,0,0,0,0))
    False
    >>> is_correct((2,2,2,2,2))
    True"""
    if score == (2,2,2,2,2):
        return True
    return False


def get_valid_words(file_path=ALL_WORDS):
    """returns a list containing all valid words.
    Note to test that the file is read correctly, use:
    >>> get_valid_words()[0]
    'aahed'
    >>> get_valid_words()[-1]
    'zymic'
    >>> get_valid_words()[10:15]
    ['abamp', 'aband', 'abase', 'abash', 'abask']

    """
    # read words from files and return a list containing all words that can be entered as guesses
    file = open(file_path, "r")
    word_list = file.read().splitlines()
    file.close()
    return word_list
    # return ['wibble', 'wobble', 'wubble', 'wabble']


def get_target_word(file_path=TARGET_WORDS, seed=None):
    """Picks a random word from a file of words

    Args:
        file_path (str): the path to the file containing the words

    Returns:
        str: a random word from the file

    How do you test that a random word chooser is choosing the correct words??
    Discuss in class!
    >>> get_target_word()
    'aback'
    >>> get_target_word()
    'zonal'

    """
    # read words from a file and return a random word (word of the day)
    file = open(file_path,'r')
    list_words = file.read().splitlines()
    file.close()
    return choice(list_words)
    # return 'woble'


def ask_for_guess(valid_words):
    """Requests a guess from the user directly from stdout/in
    Returns:
        str: the guess chosen by the user. Ensures guess is a valid word of correct length in lowercase
    """
    while True:
        user_input = input("Please input a 5 letter word: ")
        if user_input.lower() in valid_words:
            break
        else:
            print(user_input + " is not a valid input")
    return user_input
    # return 'wibble'


def score_guess(guess, target_word):
    """given two strings of equal length, returns a tuple of ints representing the score of the guess
    against the target word (MISS, MISPLACED, or EXACT)
    Here are some example (will run as doctest):

    >>> score_guess('hello', 'hello')
    (2, 2, 2, 2, 2)
    >>> score_guess('drain', 'float')
    (0, 0, 1, 0, 0)
    >>> score_guess('hello', 'spams')
    (0, 0, 0, 0, 0)

    Try and pass the first few tests in the doctest before passing these tests.
    >>> score_guess('gauge', 'range')
    (0, 2, 0, 2, 2)
    >>> score_guess('melee', 'erect')
    (0, 1, 0, 1, 0)
    >>> score_guess('array', 'spray')
    (0, 0, 2, 2, 2)
    >>> score_guess('train', 'tenor')
    (2, 1, 0, 0, 1)
        """
    # You must use this convention as test automation will be validating your scorer

    # num_list = [0, 0, 0, 0, 0]
    # for index, char in enumerate(guess):
    #     if char == target_word[index]:
    #         num_list[index] = 2
    #     elif char in target_word:
    #         num_list[index] = 1
    #     else:
    #         num_list[index] = 0
    # return tuple(num_list)

    num_list = [0, 0, 0, 0, 0]
    char_correct = []
    for index, char in enumerate(guess):
        if char == target_word[index]:
            num_list[index] = 2
            char_correct += char
    for index, char in enumerate(guess):
        if char in target_word and char not in char_correct:
            num_list[index] = 1
    return tuple(num_list)
    # return 0, 0, 0, 0, 0


def help():
    """Provides help for the game"""
    pass


def format_score(guess, score):
    """Formats a guess with a given score as output to the terminal.
    The following is an example output (you can change it to meet your own creative ideas, 
    but be sure to update these examples)
    >>> print(format_score('hello', (0,0,0,0,0)))
    H E L L O
    _ _ _ _ _
    >>> print(format_score('hello', (0,0,0,1,1)))
    H E L L O
    _ _ _ ? ?
    >>> print(format_score('hello', (1,0,0,2,1)))
    H E L L O
    ? _ _ + ?
    >>> print(format_score('hello', (2,2,2,2,2)))
    H E L L O
    + + + + +"""
    
    string_guess = ""
    for char in guess:
        string_guess += char.upper() + " "
    string_guess.strip()
    string_score = ""
    for num in score:
        if num == 2:
            string_score += "+ "
        elif num == 1:
            string_score += "? "
        else:
            string_score += "_ "
    string_score.strip()
    return string_guess + "\n" + string_score


def main(test=False):
    if test:
        import doctest
        return doctest.testmod()
    play()


if __name__ == '__main__':
    print(main(test=True))
