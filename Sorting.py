word = input("Type the word you wish to put in the game(type done to finish): ")
print('\n')
while (word != "done"):
    if (len(word)<=5):
        WordLibray = open("Level1Words.txt", 'a')
        WordLibray.write(word.lower() +'\n')
        WordLibray.close()
    elif (6<=len(word)<=8):
        WordLibray = open("Level2Words.txt",'a')
        WordLibray.write(word.lower() +'\n')
        WordLibray.close()
    else:
        WordLibray = open("Level3Words.txt",'a')
        WordLibray.write(word.lower() + '\n')
        WordLibray.close()
    word = input("Type the word you wish to put in the game(type done to finish): ")
    print('\n')