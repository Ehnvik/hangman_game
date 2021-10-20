import random
from words import word_list
from hangman_guy import lives_hangman_guy
import string
import sys


# imported random word from word_list in words

# Choose a random word from the word list
def get_correct_word(words):
    word = random.choice(word_list)
    while "-" in word or " " in word:
        word = random.choice(words)

    return word.upper()


# Defined varibales that later used in the game
def main():
    lives = 7
    word = get_correct_word(word_list)
    word_letter = set(word)
    main_words = set(string.ascii_uppercase)
    used_letter = set()

    while len(word_letter) > 0 and lives > 0:
        print("Game started!\n""You have", lives, "lives left")
        print("You have used these letters: ", " ".join(used_letter))
        # What letters used
        lists = [letter if letter in used_letter else '-' for letter in word]
        print(lives_hangman_guy[lives])
        print("Current word: ", " ".join(lists))
        print("\n")

        # Let the user guess a letter
        user_letter = input("Guess a letter: ").upper()
        print("")
        if user_letter in main_words - used_letter:
            used_letter.add(user_letter)
            if user_letter in word_letter:
                word_letter.remove(user_letter)
                print(f"Correct! You typed in {user_letter}.""\n")
            else:
                lives = lives - 1  # Takes a life for every wrong answer
                print(f"Wrong! {user_letter} is not in the word.""\n")

        elif user_letter in used_letter:
            print(f"You have already used {user_letter}. Try again!""\n")

        else:
            print(f"{user_letter} is not a letter, try again!" "\n")

    if lives == 0:  # Stating that the game is over when lives == 0
        print(lives_hangman_guy[lives])
        print(f"You lost! The word was {word}.")
    else:
        print(f"Congratulations! You have completed the word {word}.")


# Let the user to choose between starting the game or exit the game
def start_game():
    while True:
        user_input = input("Hangman! Type 'yes' to play or 'no' to exit'\n\n")

        if user_input == "yes":
            print("\n\n")
            print(main())

        elif user_input == "no":
            print("\n\n")
            print("See you next time!")
            sys.exit()
        else:
            print("\n")
            print("Please choose 'yes' or 'no'\n\n")


start_game()


main()
