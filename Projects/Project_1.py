# WAP using Python Programming language to make a rock, paper & scisssor game
# Using 'Random' for computer's input.

import random

def RPS(comp, player):
    # In case two values are equal then declare a tie
    if player == comp:
        return None
    
    # All the possible combinations
    # When computer choose Rock
    elif player == "R":
        if comp == "P":
            return False
        elif comp == "S":
            return True
    
    # When computer choose Paper
    elif player == "P":
        if comp == "S":
            return False
        elif comp == "R":
            return True
        
    # When computer choose Scissor
    elif player == "S":
        if comp == "P":
            return False
        elif comp == "R":
            return True
        
print("Computer's Turn: Rock(R), Paper(P) or Scissors(S)")
randNo = random.randint(1, 3)
if randNo == 1:
    comp = "R"
elif randNo == 2:
    comp = "P"
elif randNo == 3:
    comp = "S"
    
player = input("Your Turn: Rock(R), Paper(P) or Scissors(S)?")
game = RPS(comp, player)

print(f"Computer chose {comp}")
print(f"You chose {player}")


# This is in case the User enters an invalid input.
if game == None:
    print("The Game is a Tie!")
# elif game:
#     print("You win!")
# else:
#     print("You Lose!")