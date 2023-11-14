# %%

import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list 
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = ["_"] * len(self.word)
        self.num_letters = len(set(self.word)) # You have -35013 letters left to guess. 
        self.num_letters = len({letters for letters in self.word})
        self.list_of_guesses = []
    
    def check_guess(self, guess):
        guess.lower()
        if guess in self.word:
            print(f"Good guess! '{guess}' is in the word.")
            print(self.word)
            print(self.word_guessed)
            for index, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[index] = letter 
                    print(self.word_guessed)
                break
        else:
            self.num_lives = self.num_lives - 1
            print(f"Sorry, '{guess}' is not in the word.")
            print(f"You have {self.num_lives} lives left.")
        self.num_letters = self.num_letters - 1
        print(f"You have {self.num_letters} letters left to guess.")
        
        

    def ask_for_input(self):
        print(self.word_guessed)
        guess = input("Guess a letter: ")
        while True:
            if len(guess) != 1 and guess.isdigit():
                print("Invalid letter. Please, enter a single alphabetical character.")
            #elif guess in self.list_of_guesses:
            #    print("You've already guessed that letter!") # this always prints...
            #    guess = input("Guess another letter: ")
            elif len(guess) == 1 and guess.isalpha():
                    self.check_guess(guess)
                    self.list_of_guesses.append(guess)
            else:
                guess in self.list_of_guesses
                print("You've already guessed that letter!") # this always prints...
                guess = input("Guess another letter: ")


def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)
    print(f"Welcome to Hangman! You have {num_lives} lives to complete the game.")
    print("Here is the word to guess: ")
    while True:
        if game.num_lives == 0:
            print("You lost!")
        elif num_lives > 0:
            game.ask_for_input()
        elif game.num_lives > 0 and game.num_letters != 0:
            print("Congratulations!! You've won the game, you clever thing you.")

fruit_list = ['fig', 'cloudberry', 'mango', 'cherry', 'lime']

play_game(fruit_list)

# %%