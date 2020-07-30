"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random


def start_game():
  #  """Psuedo-code Hints
    
  #  When the program starts, we want to:
 #   ------------------------------------
  #  1. Display an intro/welcome message to the player.
    print("Hello Welcome to my number guessing game !")
   # 2. Store a random number as the answer/solution.
    random_number= random.randint(1,10)
   # 3. Continuously prompt the player for a guess.
    guess = int(input("Pick a number between 1-10  "))
    attempt = 1
    while guess != random_number:
        
        
     # a. If the guess greater than the solution, display to the player "It's lower".
        if guess == random_number:
            print("You got it ! congrats" )
            print("it took you {} to get it not bad".format(attempt))
            print("until next time")
    #  b. If the guess is less than the solution, display to the player "It's higher".
        elif guess<random_number:
            print("its higher")
            guess = int(input("please try again:  "))
            attempt += 1
    
   # 4. Once the guess is correct, stop looping, inform the user they "Got it"
        elif guess >random_number:
            print("its lower" )
            guess = int(input("please try again:  "))
            attempt += 1
            
    #     and show how many attempts it took them to get the correct number.
   # 5. Let the player know the game is ending, or something that indicates the game is over.
    
   # ( You can add more features/enhancements if you'd like to. )
 #   """
#    # write your code inside this function.



# Kick off the program by calling the start_game function.
start_game()


# Kick off the program by calling the start_game function.
start_game()
