import random
from words import word_list
import string

# imported random word from word_list in words


def get_correct_word(words):
    word = random.choice(word_list)
    while "-" in word or " " in word:
        word = random.choice(words)

    return word.upper()


def main():
    word = get_correct_word(word_list)
    word_letter = set(word)
    main_words = set(string.ascii_uppercase)
    used_letter = set()

    while len(word_letter) > 0:
        print("You have used these letters: ", " ".join(used_letter))
    
        lists = [letter if letter in used_letter else '-' for letter in word]

        print("current word: ", " ".join(lists))

        user_letter = input("Guess a letter: ""\n").upper()
        if user_letter in main_words - used_letter:
            used_letter.add(user_letter)
            if user_letter in word_letter:
                word_letter.remove(user_letter)
                print(f"Correct! You typed in {user_letter}.""\n")
            else:
                print(f"Wrong! {user_letter} is not in the word.""\n")
            
        elif user_letter in used_letter:
            print(f"you have already used {user_letter}. Try again!""\n")
        
        else:
            print(f"{user_letter} is not a letter, try again!" "\n")


main()