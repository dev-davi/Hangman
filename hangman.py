from ntpath import join
from re import S
import sys
import random
import time
from urllib.request import urlopen


# Pulls a list of words from the specified url and puts them into a list.
word_site = "https://www.mit.edu/~ecprice/wordlist.10000"
response = urlopen(word_site)
txt = response.read()
WORDS = txt.splitlines()


def main() -> None:
    global count
    global display
    global word
    global already_guessed
    global length
    global play_game
    global limit
    # choose a random word from WORDS and decodes it from a type bytes to str.
    word = random.choice(WORDS).decode('UTF-8')
    length = len(word)
    count = 0
    display = '_' * length
    already_guessed = []
    play_game = ""
    limit = 9
    print(word)
    check_valid_input()


# Initializing all the conditions required for the game:
def check_valid_input():
    guess = input("This is what you have so far: " + display +
        ", Enter a letter: \n").strip()
    if len(guess) == 0 or len(guess) >= 2 or guess <= "9":
        print("Invalid Input, Try a letter\n")
        check_valid_input()
    else:
        hangman(guess)

# Update display to account for the correctly guessed letter. 
def update_display(guess: str) -> None:
    global display
    global word
    display_alias = display
    # iterate over word and find the relevent index of the guessed letter, 
    # then replace "_" with the letter at that index
    for i in range(len(word)):
        if word[i] == guess and display[i] == '_':
            display = display[:i] + guess + display[i+1:]
            break
    # if it desn't break before the last position of word, then all available positions of the gussed letter 
    # are filled, then it counts as a wrong guess.
    if display_alias == display:
        wrong_guess()

def update_alreay_guessed(guess: str) -> None:
    global already_guessed
    if guess not in already_guessed:
        already_guessed.append(guess)

def hangman(guess):
    global count
    global display
    global word
    global already_guessed
    global play_game
    global limit
    if guess in word:
        update_alreay_guessed(guess)
        update_display(guess)
        print(display)
    else:
        wrong_guess()
    if display == word:
        print("Congrats! You have guessed the word correctly!")
        play_loop()
    elif count != limit:
        check_valid_input()


def wrong_guess():
    global count
    global word
    global already_guessed
    count += 1
    if count == 1:
        time.sleep(1)
        print("   _____ \n"
            "  |      \n"
            "  |      \n"
            "  |      \n"
            "  |      \n"
            "  |      \n"
            "  |      \n"
            "__|__\n")
        print("Wrong guess. " + str(limit - count) + " guesses remaining")
    elif count == 2:
        time.sleep(1)
        print("   _____ \n"
            "  |     | \n"
            "  |     |\n"
            "  |      \n"
            "  |      \n"
            "  |      \n"
            "  |      \n"
            "__|__\n")
        print("Wrong guess. " + str(limit - count) + " guesses remaining")
    elif count == 3:
        time.sleep(1)
        print("   _____ \n"
            "  |     | \n"
            "  |     |\n"
            "  |     | \n"
            "  |      \n"
            "  |      \n"
            "  |      \n"
            "__|__\n")
        print("Wrong guess. " + str(limit - count) + " guesses remaining")
    elif count == 4:
        time.sleep(1)
        print("   _____ \n"
            "  |     | \n"
            "  |     |\n"
            "  |     | \n"
            "  |     O \n"
            "  |      \n"
            "  |      \n"
            "__|__\n")
        print("Wrong guess. " + str(limit - count) + " guesses remaining")
    elif count == 5:
        time.sleep(1)
        print("   _____ \n"
            "  |     | \n"
            "  |     |\n"
            "  |     | \n"
            "  |     O \n"
            "  |     | \n"
            "  |      \n"
            "__|__\n")
        print("Wrong guess. " + str(limit - count) + " guesses remaining")
    elif count == 6:
        time.sleep(1)
        print("   _____ \n"
            "  |     | \n"
            "  |     |\n"
            "  |     | \n"
            "  |     O \n"
            "  |    /| \n"
            "  |     \n"
            "__|__\n")
        print("Wrong guess. " + str(limit - count) + " guesses remaining")
    elif count == 7:
        time.sleep(1)
        print("   _____ \n"
            "  |     | \n"
            "  |     |\n"
            "  |     | \n"
            "  |     O \n"
            "  |    /|\  \n"
            "  |      \n"
            "__|__\n")
        print("Wrong guess. " + str(limit - count) + " guesses remaining")
    elif count == 8:
        time.sleep(1)
        print("   _____ \n"
            "  |     | \n"
            "  |     |\n"
            "  |     | \n"
            "  |     O \n"
            "  |    /|\  \n"
            "  |    /  \n"
            "__|__\n")
        print("Wrong guess. " + str(limit - count) + " last guess remaining")
    elif count == 9:
        time.sleep(1)
        print("   _____ \n"
            "  |     | \n"
            "  |     |\n"
            "  |     | \n"
            "  |     O \n"
            "  |    /|\ \n"
            "  |    / \ \n"
            "__|__\n")
        print("Wrong guess. You are hanged!!!")
        print("The word was:", word)
        print("your correct guesses:", already_guessed)
        play_loop()

def play_loop():
    play_game = input("Would you like to play again? y = yes, n = no \n")
    # following while loop forces player to provide an appropriate answer.
    while play_game not in ["y", "n"]:
        play_game = input("Would you like to play again? y = yes, n = no \n")
    if play_game == "y":
        time.sleep(1)
        print("Get ready...")
        time.sleep(2)
        main()
    else:
        print("Thanks For Playing! Come again!")
        sys.exit()


if __name__ == "__main__":
    # Initial steps to invite in the game:
    print('Welcome to hangman.')

    # capitalized first letter of player's input incase the player didn't.
    name = input('please enter your name: ').capitalize()
    print('Hello ' + name +
        ', I hope you have a great time playing our game, good Luck!!')

    # halt the game for a few seconds to add suspense.
    time.sleep(3)
    print('lets begin the game.....')
    time.sleep(3)
    print("you have 9 wrong attempts.")
    main()
