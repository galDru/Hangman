def choose_word(file_path, index):
    with open(file_path, 'r') as file:
        secret_word = file.read().split()
        chosen = secret_word[index]
        return chosen


def check_valid_input(letter_guessed, old_letters_guessed):
    if (not (letter_guessed.isalpha())) and len(letter_guessed) > 1:
        return False
    elif not (letter_guessed.isalpha()):
        return False
    elif (len(letter_guessed)) > 1:
        return False
    elif letter_guessed.lower() in old_letters_guessed:
        return False
    else:
        return True


def show_hidden_word(secret_word, old_letters_guessed):
    word = ''
    for char in secret_word:
        if char in old_letters_guessed:
            word += char + ' '
        else:
            word += '_ '
    return word


def check_win(secret_word, old_letters_guessed):
    if any(char not in old_letters_guessed for char in secret_word):
        return False
    else:
        return True


HANGMAN = (
    """
 ------
 |    |
 |
 |
 |
 |
 |
 |
 |
----------
""",
    """
 ------
 |    |
 |    O
 |
 |
 |
 |
 |
 |
----------
""",
    """
 ------
 |    |
 |    O
 |   -+-
 | 
 |   
 |   
 |   
 |   
----------
""",
    """
 ------
 |    |
 |    O
 |  /-+-
 |   
 |   
 |   
 |   
 |   
----------
""",
    """
 ------
 |    |
 |    O
 |  /-+-/
 |   
 |   
 |   
 |   
 |   
----------
""",
    """
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |   
 |   
 |   
 |   
----------
""",
    """
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |    |
 |   | 
 |   | 
 |   
----------
""",
    """
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |    |
 |   | |
 |   | |
 |  
----------
""")

MAX_TRIES = 8

HANGMAN_ASCII_ART = ("""Welcome to the game Hangman \n
    _    _
   | |  | |
   | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
   |  __  |/ _' | '_ \ / _' | '_ ' _ \ / _' | '_ 
   | |  | | (_| | | | | (_| | | | | | | (_| | | | |
   |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                        __/ |
                       |___/""")
print(HANGMAN_ASCII_ART, "\n", MAX_TRIES)
wrong = 0
fileName = r"C:\Users\gald1\OneDrive\שולחן העבודה\New Text Document.txt"
print("please enter a number for the index word in the file path")
wordIndex = int(input())
secret = choose_word(fileName, wordIndex)
old_letters = []
while wrong < MAX_TRIES and not check_win(secret, old_letters):
    print(HANGMAN[wrong])
    print(show_hidden_word(secret, old_letters))
    print("Guess a letter:")
    letter = input()
    while not check_valid_input(letter, old_letters):
        print("You already guessed the letter:\t", letter)
        letter = input("Guess again:\t")
    old_letters.append(letter)

    if letter in secret:
        print("The letter, ", letter, "is in the word")
    else:
        print("\nSorry,", letter, "isn't in word")
        wrong += 1

    if wrong == MAX_TRIES:
        print(HANGMAN[wrong])
        print(show_hidden_word(secret, old_letters))
        print("I would tell you, that you've been hanged. \n\ But you're dead, so.......RIP?")
    else:
        print("\nYou guessed it!")
