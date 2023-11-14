# %%

import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list 
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = ["_"] * len(self.word)
        self.num_letters = len(set(self.word))
        self.num_letters = len({letters for letters in self.word})
        self.list_of_guesses = []
    
    def check_guess(self, guess):
        guess.lower()
        if guess in self.word:
            print(f"\nGood guess! '{guess}' is in the word.")
            for index, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[index] = letter 
                    print(self.word_guessed)
            self.num_letters = self.num_letters - 1
            print(f"\nYou have {self.num_letters} letters left to guess and {self.num_lives} lives left.")
        else:
            self.num_lives = self.num_lives - 1
            print(f"\nSorry, '{guess}' is not in the word.")
            print(f"You now only have {self.num_lives} lives left.")
        
        
    def ask_for_input(self):
        print(self.word_guessed)
        guess = input("Guess a letter: ")
        while True:
            if len(guess) != 1 or guess.isdigit():
                print("\nInvalid entry. Please, enter a single alphabetical character.")
                break
            elif guess in self.list_of_guesses:
                print("\nYou've already guessed that letter!")
                guess = input("Guess another letter: ")
            elif len(guess) == 1 and guess.isalpha():
                    self.check_guess(guess)
                    self.list_of_guesses.append(guess)
                    break

def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)
    print(f"Welcome to Hangman! You have {num_lives} lives to complete the game.\n")
    print("Here is the word to guess: ")
    while True:
        if game.num_lives == 0:
            print("You lost!")
            user_choice = input(f"\nWould you like to play again? Y or N: ")
            if user_choice == "Y":
                return play_game(word_list)     # calling a function within itself is called recursion
            break
        elif num_lives > 0 and game.num_letters != 0:
            game.ask_for_input()
        else: 
            game.num_lives > 0 and game.num_letters == 0
            print(f"Congratulations!! You've won the game by guessing the word {game.word}, you clever thing.")
            user_choice_1 = input(f"\nWould you like to play again? Y or N: ")
            if user_choice_1 == "Y":
                return play_game(word_list)
            else:
                print("Thanks for playing!")
            break

fruit_list = ['fig', 'cloudberry', 'mango', 'cherry', 'lime']

play_game(fruit_list)

# %%