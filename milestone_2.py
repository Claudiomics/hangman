# %%
import random 

word_list = ['Fig', 'Cloudberry', 'Mango', 'Cherry', 'Lime']

#print(word_list)
#word = random.choice(word_list)
#print(word)

guess = input("Guess letter:")

if len(guess) == 1 and guess.isalpha():
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")

# %%