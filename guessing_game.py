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
    
   # When the program starts, we want to:
   # ------------------------------------
    #1. Display an intro/welcome message to the player.
    print("Hello, Welcome to the random number game the game is simple alll you have to do is pick a number from 1-10")
    #2. Store a random number as the answer/solution.
    random_number = random.randint(1,10)
    #3. Continuously prompt the player for a guess.
    attempt = 1
    guess=input(" please pick a number from 1-10  ")
    guess=int(guess)
   #   a. If the guess greater than the solution, display to the player "It's lower".
    while random_number != guess:
        if guess < random_number:
                print("It's Lower")
                guess = input("try again:  ")
                int(guess)
                attempt+=1
                continue
            #  b. If the guess is less than the solution, display to the player "It's higher".
        elif guess > random_number:
                print("It's Higher")
                guess = input("try again:  ")
                int(guess)
                attempt += 1
                continue
            #4. Once the guess is correct, stop looping, inform the user they "Got it"
        elif guess == random_number:
                print("Got it")
                # and show how many attempts it took them to get the correct number.
                print("it took you {} tries".format(attempt))
                
            #5. Let the player know the game is ending, or something that indicates the game is over.
        again=input("Would you like to play again ? yes/no  " )
        if again == 'yes':
                print("nice alright the HighScore is {}".format(attempt))
                continue
        else:
                break
                
        
        
    
    #( You can add more features/enhancements if you'd like to. )
    
    # write your code inside this function.



# Kick off the program by calling the start_game function.
start_game()
