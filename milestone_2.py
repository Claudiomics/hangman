# %%
import random 

word_list_of_fruits = ['Fig', 'Cloudberry', 'Mango', 'Cherry', 'Lime']

print(word_list_of_fruits)
word = random.choice(word_list_of_fruits)
print(word)

user_guess = input("Guess letter:")

if len(user_guess) == 1 and user_guess.isalpha():
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")

# %%