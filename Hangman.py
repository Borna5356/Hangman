"""
Author: Borna Eshraghi
File: Hangaman.py
Description: Uses the random module
and words from text files to play 
hangman

"""
import random

def easy_word():
    """
    Gets a word from the Level1Words.txt
    and returns the length

    """
    global word
    wordlibray = open('Level1Words.txt', 'r')
    for line in wordlibray:
        words.append(line)
    wordlibray.close()
    word = random.choice(words)
    word = list(word)
    word.remove('\n')
    return len(word)

def medium_word():
    """
    Gets a word from the Level2Words.txt
    and returns the length

    """
    global word
    wordlibrary = open('Level2Words.txt', 'r')
    for line in wordlibrary:
        words.append(line)
    wordlibrary.close()
    word = random.choice(words)
    word = list(word)
    word.remove('\n')
    return len(word)

def hard_word():
    """
    Gets a word from the Level3Words.txt
    and returns the length

    """
    global word
    wordlibrary = open('Level3Words.txt', 'r')
    for line in wordlibrary:
        words.append(line)
    wordlibrary.close()
    word = random.choice(words)
    word = list(word)
    word.remove('\n')
    return len(word)

def check_letter(word, emptyword, user_input):
    """
    Checks to see if the letter the 
    user guessed is in the word

    """
    global guesses
    global Guessed_Letters
    correct = 0
    for count in range(len(word)):
        if (user_input == word[count]):
            emptyword[count] = user_input
            correct = 1
    if (user_input == "stop"):
        return "Game Over"
    if (correct == 0):
        guesses -= 1
        print("You have", guesses, "guesses left")
    Guessed_Letters.append(user_input)
    return emptyword

def win(blankword):
    """
    checks to see if the word has been guessed
    
    """
    for count in range(len(blankword)):
        if blankword[count] == '_':
            return False
    return True

def check_guessed_letter(user_input,letters_guessed):
    """
    checks to see if the user has already 
    guessed the inputed letter
    
    """
    for count in range(len(letters_guessed)):
        if (user_input == letters_guessed[count]):
            return False
    return True

def invalid_input(guess):
    """
    checks to make sure the guess is 
    1 character long

    """
    if (len(guess) > 1) or (guess == ''):
        return True
    else:
        return False

def num_input(guess):
    """
    checks to make sure the 
    guess is not a number
    
    
    """
    try:
        int(guess)
        return True
    except ValueError:
        return False

# *********MAIN**********#
print("Let's play hangman(you can enter stop at anytime to end that round).")
restart = "yes"
while (restart.lower() == "yes"):
    words = []
    word = []
    difficulty = int(input("enter a difficulty level from 1-3: "))
    while (True):
        if (difficulty == 1):
            print("The word is " + str(easy_word()) + " letters long.")
            break
        elif (difficulty == 2):
            print("The word is " + str(medium_word()) + " letters long.")
            break
        elif (difficulty == 3):
            print("The word is " + str(hard_word()) + " letters long.")
            break
        else:
            difficulty = int(input("You entered an invalid level.\nEnter a difficulty level from 1-3: "))

    # setup for starting game

    blankword = []
    for count in range(len(word)):
        blankword.append('_')
    print(blankword)
    guesses = 10
    Guessed_Letters = []

    # game
    while (True):
        print('')
        guess = input('guess a letter(lowercase): ')
        while (invalid_input(guess)) and (guess != "stop") or (num_input(guess)):
            print("")
            if (invalid_input(guess)):
                print("You can use one character for your guess")
            
            elif (num_input(guess)):
                print("you can only use letters")
            guess = input('guess a letter(lowercase): ')

        if check_guessed_letter(guess,Guessed_Letters):
            print(check_letter(word, blankword, guess))
            print("Letters used: "+str(Guessed_Letters))
            if (win(blankword)):
                print("You were able to guess the word!")
                break
            if (guesses == 0):
                print("You lost!\nThe word is: " + str(word))
                break
            elif (guess == "stop"):
                print("you gave up.\nThe word is "+str(word))
                break
        else:
            print("This letter has already been used")
            print(blankword)
            print("Letters used: "+str(Guessed_Letters))

    #asking to restart game
    print('\n')
    restart = input('do you want to play again: ')
    print('\n')
print("Thank you for playing")