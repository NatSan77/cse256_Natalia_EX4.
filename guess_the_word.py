# Natalia Sanchez-Garcia
# # CIS256 Fall 2024
# # Programming Assignment 4 (PA 4)
import random #for assigning random words
words = ["today", "tomorrow", "yesterday"] #my chosen list of words

def the_word():
    return random.choice(words) # program selecting random word

def display_word(word, guessed_letter):
    return ' '.join([letter if letter in guessed_letter else '_' for letter in word])
def guess_word_game(): #starting the game
    word = the_word()
    guessed_letter = set()
    
    print("Guess the Word Game")

    while word != words: #while words are not complete the code below runs
        guess = input("Guess a letter").lower() #prompting user

        if len(guess) !=1:
            print ("Only enter one letter") # only lets one letter
            continue
        if guess in guessed_letter:
            print("Already guessed") #doesn't let repeats
            continue

        guessed_letter.add(guess)

        if guess in word:
            print(f"Right, the letter '{guess} is in this word.") #reveals the right letter
        else:
            print("Wrong, try again") # user can guess as many times as they want

        if all(letter in guessed_letter for letter in word):
            print(f"Congrats, your guessed right '{word}") #displays the congratulatory message when word guessed
            break

if __name__ == "__main__":
    guess_word_game() 