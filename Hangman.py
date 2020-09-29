import random

def easy():
    global word
    wordlibray = open('Level1Words.txt', 'r')
    for line in wordlibray:
        words.append(line)
    wordlibray.close()
    word = random.choice(words)
    word = list(word)
    word.remove('\n')
    return len(word)

def medium():
    global word
    wordlibrary = open('Level2Words.txt', 'r')
    for line in wordlibrary:
        words.append(line)
    wordlibrary.close()
    word = random.choice(words)
    word = list(word)
    word.remove('\n')
    return len(word)

def hard():
    global word
    wordlibrary = open('Level3Words.txt', 'r')
    for line in wordlibrary:
        words.append(line)
    wordlibrary.close()
    word = random.choice(words)
    word = list(word)
    word.remove('\n')
    return len(word)

def check(word, emptyword, user_input):
    global misses
    global Guessed_Letters
    correct = 0
    for count in range(len(word)):
        if (user_input == word[count]):
            emptyword[count] = user_input
            correct = 1
    if (user_input == "stop"):
        return "Game Over"
    if (correct == 0):
        misses += 1
        print("Number of misses: " + str(misses))
    Guessed_Letters.append(user_input)
    return emptyword

def win(blankword):
    for count in range(len(blankword)):
        if blankword[count] == '_':
            return False
    return True

def check_letter(user_input,letters_guessed):
    for count in range(len(letters_guessed)):
        if (user_input == letters_guessed[count]):
            return False
    return True

# *********MAIN**********#
print("Let's play hangman(you can enter stop at anytime to end that round).")
restart = "yes"
while (restart.lower() == "yes"):
    words = []
    word = []
    difficulty = int(input("enter a difficulty level from 1-3: "))
    while (True):
        if (difficulty == 1):
            print("The word is " + str(easy()) + " letters long.")
            break
        elif (difficulty == 2):
            print("The word is " + str(medium()) + " letters long.")
            break
        elif (difficulty == 3):
            print("The word is " + str(hard()) + " letters long.")
            break
        else:
            difficulty = int(input("You entered an invalid level.\nEnter a difficulty level from 1-3: "))

    # setup for starting game

    blankword = []
    for count in range(len(word)):
        blankword.append('_')
    print(blankword)
    misses = 0
    Guessed_Letters = []

    # game
    while (True):
        print('\n')
        guess = input('guess a letter(lowercase): ')
        if check_letter(guess,Guessed_Letters):
            print(check(word, blankword, guess))
            print("Letters used: "+str(Guessed_Letters))
            if (win(blankword)):
                print("You were able to guess the word!")
                break
            if (misses == 10):
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