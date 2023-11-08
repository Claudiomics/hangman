# %%
import random 

word_list_of_fruits = ['Fig', 'Cloudberry', 'Mango', 'Cherry', 'Lime']

#print(word_list_of_fruits)
random_word_from_list = random.choice(word_list_of_fruits)
#print(random_word_from_list)

#user_guess = input("Guess letter:")

#if len(user_guess) == 1 and user_guess.isalpha():
 #   print("Good guess!")
#else:
  #  print("Oops! That is not a valid input.")


#while user_guess in random_word_from_list:
while True:
    user_guess = input("Guess letter: ") 
    if len(user_guess) == 1 and user_guess.isalpha():
        break
    else:
        print("Invalid letter. Please, enter a single alphabetical character.")

# while True:    
#    if len(user_guess) == 1 and user_guess.isalpha():
#    print("Good guess!")  
#        if user_guess in random_word_from_list:
#            print("Good guess!")
#        elif user_guess not in random_word_from_list:
#            break
#            print("Wrong. Try again, fool.")
#    else:
#        print("Oops! That is not a valid input.")



# %%