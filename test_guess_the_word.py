# Natalia Sanchez-Garcia
# # CIS256 Fall 2024
# # Programming Assignment 4 (PA 4)
import pytest 
from game import the_word, words, guess_word_game

def test_guess_word_game():
    word = the_word()
    assert word in ["today", "tomorrow", "yesterday"] #checking selection from original list

def test_words():
    word = "today" # making sure selected word is from list
    guessed_letter = set()

    guessed_letter, guess = word(words, 't', guessed_letter) #testing correct guess
    assert correct == True
    assert message == "Right, the letter 't' is part of the word."
    assert guessed_letter == {'t'}

    guessed_letter, guess == word(words, 'e', guessed_letter) # testing incorrect guess
    assert correct == False
    assert message == "Wrong"
    assert guessed_letter == {'t', 'e'}
