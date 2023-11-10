# %%
import random

word_list_of_fruits = ['fig', 'cloudberry', 'mango', 'cherry', 'lime']
random_word_from_list = random.choice(word_list_of_fruits)

class Hangman:
    def __init__(self, random_word_from_list, num_lives=5):
        self.random_word_from_list = random_word_from_list

        #word_guessed = len(random_word_from_list.split())
        word_guessed = [list(letter) for letter in random_word_from_list]
        #word_guessed = [list(letter) as '_' for letter in random_word_from_list] invalid syntax
        #word_guessed = [list(letter.split()) as _ for letter in random_word_from_list]

    #def print_guess(self, random_word_from_list, num_lives=5):
     #   print(self.word_guessed)

def check_guess(guess):
    guess.lower()
    if guess in random_word_from_list:
        print(f"Good guess! '{guess}' is in the word.")
    else:
        print(f"Sorry, '{guess}' is not in the word. Try again.")

def ask_for_input():
    check_guess(guess)
    while True:
        if len(guess) == 1 and guess.isalpha():
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")

guess = input("Guess letter: ")

ask_for_input()

guess_1 = Hangman('a')

print(guess_1.word_guessed())


# %%