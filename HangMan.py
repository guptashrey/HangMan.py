def HangMan(c):
    print "\n\n!!!!!!!!!! HANGMAN !!!!!!!!!! \n"
    if c == 8:
        print " _________________ \n"

    elif c == 7:
        print " _________________ \n"
        print "        |          \n"
        print "        |          \n"
        print "        |          \n"

    elif c == 6:
        print " _________________ \n"
        print "        |          \n"
        print "        |          \n"
        print "        |          \n"
        print "      /. .\         \n"
        print "      \ - /         \n"

    elif c == 5:
        print " _________________ \n"
        print "        |          \n"
        print "        |          \n"
        print "        |          \n"
        print "      /. .\         \n"
        print "      \ - /         \n"
        print "        |         \n"
        print "        |         \n"

    elif c == 4:
        print " _________________ \n"
        print "        |          \n"
        print "        |          \n"
        print "        |          \n"
        print "      /. .\         \n"
        print "      \ - /         \n"
        print "        |         \n"
        print "        |         \n"
        print "        |        \n"
        print "        |         \n"
        print "        |         \n"
        print "        |         \n"

    elif c == 3:
        print " _________________ \n"
        print "        |          \n"
        print "        |          \n"
        print "        |          \n"
        print "      /. .\         \n"
        print "      \ - /         \n"
        print "        |         \n"
        print "        |         \n"
        print "       /|        \n"
        print "      / |         \n"
        print "        |         \n"
        print "        |         \n"

    elif c == 2:
        print " _________________ \n"
        print "        |          \n"
        print "        |          \n"
        print "        |          \n"
        print "      /. .\         \n"
        print "      \ - /         \n"
        print "        |         \n"
        print "        |         \n"
        print "       /|\        \n"
        print "      / | \        \n"
        print "        |         \n"
        print "        |         \n"

    elif c == 1:
        print " _________________ \n"
        print "        |          \n"
        print "        |          \n"
        print "        |          \n"
        print "      /. .\         \n"
        print "      \ - /         \n"
        print "        |         \n"
        print "        |         \n"
        print "       /|\        \n"
        print "      / | \        \n"
        print "        |         \n"
        print "        |         \n"
        print "       /        \n "
        print "      /         \n "

    elif c == 0:
        print " _________________ \n"
        print "        |          \n"
        print "        |          \n"
        print "        |          \n"
        print "      /. .\         \n"
        print "      \ - /         \n"
        print "        |         \n"
        print "        |         \n"
        print "       /|\        \n"
        print "      / | \        \n"
        print "        |         \n"
        print "        |         \n"
        print "       / \        \n "
        print "      /   \       \n "


import os
print "******************** Hangman Game ********************"


word = raw_input("Enter Word: ")
word = word.upper()
word1 = list(word)
word2 = list(word)


for i in range(len(word1)):
    if word1[i] == 'A' or word1[i] == 'E' or word1[i] == 'I' or word1[i] == 'O' or word1[i] == 'U' or word1[i] == ' ':
        continue
    else:
        word1[i] = '_'


os.system('clear')
print "********** Hangman Game **********"
print "Guess the word: ", word1

j = 0
chances = 9
while(1):
    j = j + 1
    letter = raw_input("Enter Letter: ")
    letter1 = letter.upper()

    if letter1 in word2:

        for i in range(len(word2)):
            if word2[i] == letter1:
                word1[i] = letter1

    else:
        chances = chances - 1
        HangMan(chances)

    if ''.join(word1) == word or chances == 0:
        break

    print "********** Hangman Game **********"
    print "Word guessed so far: %s , Chances Left: %d" % (word1, chances)


if ''.join(word1) == word:
    os.system('clear')
    print "********** Hangman Game **********"
    print "You guessed the correct word %s." % ''.join(word1)
    print "You Win!"

else:
    print "********** Hangman Game **********"
    print "The Correct Word is:", word
    print "You Lose!"
