# %%
import random 

word_list_of_fruits = ['Fig', 'Cloudberry', 'Mango', 'Cherry', 'Lime']
random_word_from_list = random.choice(word_list_of_fruits)


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

# %%