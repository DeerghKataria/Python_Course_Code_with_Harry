# This project is "The Perfect Guess".
# In this game, we have to guess whether a number is higher or lower than our original
# number and if that's the case then we will slowly and steadily guide it towards the
# original number.

import random

def numGuess(num: int):
    userGuess = int(input("Guess the Number: "))

    # In case the guess is correct
    if(userGuess == num):
        print("Hooray! You guessed it right!")
        exit
    # If the guess is higher
    elif(userGuess > num):
        print("Oops! The actual number is lower :)")
        numGuess(num)
    # If the guess is lower
    else:
        print("Oops! The actual number is higher :)")
        numGuess(num)

# Giving the user an option to guess between 1 and 1000.
randNumber = random.randint(1, 1000)
# print(randNumber)
numGuess(randNumber)

# You can also add the functionality of having the high score.
# Just write a file and in that file a history of your records
# will be stored. If you beat the record. Then, your high score
# would be updated.