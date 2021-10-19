import random
from words import word_list

# imported random word from word_list in words


def get_correct_word(words):
    word = random.choice(word_list)
    while "-" in word or " " in word:
        word = random.choice(words)

    return word


def hangman():
    word = get_correct_word(word_list)
    word_letter = set(word)
    used_letter = set()

    while len(word_letter) > 0:
        print("You have used these letters: ", " ".join(used_letter))

        list = [letter if letter in used_letter else '-' for letter in word]

        print("current word: ", " ".join(list))

        user_letter = input("Guess a letter: ")
        if user_letter in used_letter:
            used_letter.add(user_letter)
        if user_letter in word_letter:
            word_letter.remove(user_letter)
    
        elif user_letter in used_letter:
            print("you have already used that letter, try again!c")
        else:
            print("Wrong letter, try again!") 


hangman()