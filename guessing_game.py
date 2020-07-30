"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random


def start_game():
    #"""Psuedo-code Hints
    
    #When the program starts, we want to:
    #------------------------------------
    #1. Display an intro/welcome message to the player.
    print("Hello and welcome to the random number game")
    #2. Store a random number as the answer/solution.
    randoms=random.randint(1,10)
    attempt = 1
    # 3. Continuously prompt the player for a guess.
    while True:
        try:
            guess =input("Please pick a number between 1-10: ")
            my_guess=int(guess)

        except:
            print("Sorry wrong Value please pick a number between 1 and 10")
        else:
    #  a. If the guess greater than the solution, display to the player "It's lower"
            if randoms < my_guess:
                print("It's lower")
                attempt += 1
                continue
        #     b. If the guess is less than the solution, display to the player "It's higher".
            elif randoms > my_guess:
                print("It's Higher")
                attempt+= 1
                continue
        
        #4. Once the guess is correct, stop looping, inform the user they "Got it"
            elif my_guess == randoms:
                print("Got it")
                print("It took you {} tries to get it right".format(attempt))
                print("Till next time bye ")
                break
        #    and show how many attempts it took them to get the correct number.
    #5. Let the player know the game is ending, or something that indicates the game is over.
    
    #( You can add more features/enhancements if you'd like to. )
    #"""
    # write your code inside this function.



# Kick off the program by calling the start_game function.
start_game()
