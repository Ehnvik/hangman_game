import random
from words import word_list

# imported random word from word_list in words


def get_correct_word(words):
    word = random.choice(words)
    while "-" in word or " " in word:
        word = random.choice(words)

    return word.upper()


def hangman():
    word = get_correct_word(word_list)
    word_letter = set(word)
    used_letter = set()

    user_letter = input("Guess a letter: ").upper()
    if user_letter in used_letter:
        used_letter.add(user_letter)
        if user_letter in word_letter:
            word_letter.remove(user_letter)
    
    elif user_letter in used_letter:
        print("you have already used that word, try again!")
    else:
        print("Wrong word, try again!") 
