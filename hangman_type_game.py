import random

# Set initial variables
word = []
hide = []
hidden = ""
show_word = ""
final = ""
correct = 0
i = 0

# Opens a file with words and creates
# a list object containing the words
# returns an exception if the word file is not present
try:
    f = open("words.txt", "r")
    words = f.readlines()
    f.close()
except IOError:
    print("Word list file not found.")

# Randomly chooses a word from the list
# and creates a new list containing the letters
for letter in words[random.randint(-1, len(words))].strip("\n"):
    word.append(letter)
    show_word += letter

# Creates a list based on the length of the word
# and adds dashes representing hidden letters.
# It then adds those dashes to a string object for printing
while i < len(word):
    hide.append("-")
    i += 1
for letter in hide:
    hidden += letter

# Sets number of tries based on word length
tries = len(word) * 2

# Main game loop
while True:
    if correct == len(word):
        print("Word: " + show_word.upper(), '\n')
        word.clear()
        hide.clear()    # If player reveals word this section resets
        hidden = ""     # game variables and adds new word from list.
        show_word = ""  # Same as above. Also asks if player wants continue game
        i = 0
        correct = 0

        for letter in words[random.randint(-1, len(words))]:
            word.append(letter)
            show_word += letter

        while i < len(word):
            hide.append("-")
            i += 1
        for letter in hide:
            hidden += letter

        tries = len(word) * 2

        print("          WORD REVEALED!!!", '\n')

        resume = input("Keep playing? (y/n): ")

        if resume == "n":
            break
        elif resume == "y":
            continue
            print('\n')

# If player runs out of tries game ends and displays hidden word
    if tries == 0:
        print("         ATTEMPTS WASTED!!!", '\n')
        print("Word:", show_word.upper())
        break

# Prints out user interface
    print("         HANGMAN TYPE GAME", '\n\n')

    print("Hidden Word: ", hidden.upper(), '\n')

    print("Attempts:", tries, '\n')

    print("Type \'!\' to guess complete word,", '\n' + "all attempts will be lost", '\n')

    print("Type \'exit\' to quit", '\n')

    guess = input("Type a letter: ")

    print('\n')


# Game logic, if user enters correct letter, a dash
# in the hidden word list is replaced with the letter.
# The hidden word string object is updated for printing
# A turn is removed per guess attempt
    if guess == "exit":
        break
    elif len(guess) > 1:
        print("     ONE LETTER AT A TIME, WTF?!", '\n')
    elif guess in word:
        for letter in word:
            if letter == guess:
                hide[word.index(guess)] = guess
                correct += 1
                word[word.index(letter)] = "@"
        hidden = ""

        for letter in hide:
            hidden += letter

        tries -= 1
    elif guess == "!":
        final = input("Enter word: ")
        if final == show_word:
            correct = len(word)
            guess = ""
            print('\n')
        elif final != show_word:
            tries = 0
            print('\n')
    else:
        if guess != "":
            print("   THAT LETTER IS NOT IN THE WORD", '\n')
            tries -= 1



