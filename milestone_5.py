# %%

import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list 
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = "_" * len(self.word)
        #  int - The number of UNIQUE letters in the word that have not been guessed yet
        self.num_letters = [len(set(letter)) for letter in self.word] 
        self.list_of_guesses = []
    
    def check_guess(self, guess):
        guess.lower()
        if guess in self.word:
            print(f"Good guess! '{guess}' is in the word.")
            #for letter in self.word:
             #   if letter == guess:
              #      correct = self.word_guessed[guess]  # string indices must be integers, not 'str'.
               #     correct.replace(letter) # needs enumerate

            for index, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed.replace(letter)
                    print(self.word_guessed)
                    if self.word > 1
                self.num_letters - 1 # what happens if the guess fills more than 1 letter in the word? len(letters)?
            
        else:
            self.num_lives - 1 # this doesn't decrease
            print(f"Sorry, '{guess}' is not in the word.")
            print(f"You have {self.num_lives} guesses left.")


    def ask_for_input(self):
        print(self.word_guessed)
        guess = input("Guess a letter: ")
        while True:
            if len(guess) != 1 and guess.isdigit():
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You've already guessed that letter!") # this always prints
                break
            else:
                if len(guess) == 1 and guess.isalpha():
                    self.check_guess(guess)
                    self.list_of_guesses.append(guess)


def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)
    while True:
        if num_lives == 0:
            print("You lost!")
        elif num_lives > 0:
            ask_for_input()
        elif num_lives > 0 and num_letters != 0:
            print("Congratulations!! You've won the game, you clever thing you.")

fruit_list = ['fig', 'cloudberry', 'mango', 'cherry', 'lime']

play_game(fruit_list)


# %%