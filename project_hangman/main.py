import random
import string
from words import words


def is_vaiable_word(words):
    chosen_word = random.choice(words)
    while (' ' in chosen_word) or ('-' in chosen_word):
        chosen_word = random.choice(words)

    return chosen_word.lower()


def play_hangman():
    word = is_vaiable_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_lowercase)
    used_letters = set()
    lives = 6

    while len(word_letters) > 0 and lives > 0:
        print(f'\nYou have {lives} lives. \n Used letters: ', ' '.join(used_letters))

        word_list =[letter if letter in used_letters else '_' for letter in word]
        print('Current word: ',' '.join(word_list))

        user_letter = ''
        while user_letter not in alphabet:
            user_letter = input("Guess a letter: ").lower()

        if user_letter in used_letters:
            print('\nYou have already used this letter!')
        elif user_letter in word_letters:
            word_letters.remove(user_letter)
        else:
            print(f'\nTheres no letter "{user_letter}" in the word!')
            lives -=1

        used_letters.add(user_letter)

    if lives==0:
        return f'\nYou lost! The word was "{word}".'

    return f'\nYou won! The word was "{word}".'



print(play_hangman())

