# %%
import random

class Hangman:
    '''
    This class is used to represent Hangman.

    Attributes:
        word_list (list) : the list of words to choose a random word from.
        num_lives (int) : the number of lives the player has at the start of the game.
        word (str) : the word to be guessed, picked randomly from the word_list.
        word_guessed (list) : a list of the letters of the word, with _ for each letter not yet guessed.
        num_letters (int) : the number of unique letters in the word that have not been guessed yet.
        list_of_guesses (list) : a list of the guesses that have already been tried.
    '''
    def __init__(self, word_list, num_lives=5):
        '''
        See help(Hangman) for accurate signature.
        '''
        self.word_list = word_list 
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = ["_"] * len(self.word)
        self.num_letters = len(set(self.word))
        self.num_letters = len({letters for letters in self.word})
        self.list_of_guesses = []
    
    def _check_guess(self, guess):
        '''
        This function is used to check the users guess is within the random word or not.

        Args:
            guess (str) : the users input to guess a letter.
        
        Returns:
            list: the ammended letters within self.word_guessed as a list if the guess is in the word.   
            str: a formatted string showing the numer or letters left to guess and lives available.
        '''
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
        '''
        This function is used to ask the user for an input and ensure it is a valid input.

        Returns:
            str: string statements describing what is wrong if the input is invalid.
            list: updated list of all user guesses if the input is valid.

        '''
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
    '''
    This function is used to play the Hangman game using attributes and methods defined in the Hangman class.
    
    Args:
        word_list (list) : the list of words to be randomly selected from.
    
    Returns:
        str: string explaining to the user they have lost if they run out of lives.
        func: play_game() if the user chooses to play again.
        func: game.ask_for_input() if the user still has lives and letters to guess.
        str: string congratulating the user if they have guessed all the letters in the word.
        str: string thanking the user for playing if they choose not to play again.
    '''
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
            else:
                print("Thanks for playing!")
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