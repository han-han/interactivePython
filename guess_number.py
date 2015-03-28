# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random

# global variables
secret_number = 0
secret_number_range = 1
game_left = 0

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    print "New game!"
    global secret_number
    secret_number = random.randrange(0, secret_number_range)

# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global secret_number_range, game_left
    secret_number_range = 100
    game_left = 8
    print "Range is from 0 to " + str(secret_number_range)
    new_game()

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global secret_number_range, game_left
    secret_number_range = 1000
    game_left = 11
    print "Range is from 0 to " + str(secret_number_range)
    new_game()
    
def input_guess(guess):
    # main game logic goes here	
    # remove this when you add your code
    global game_left
    game_left -= 1
    print "Guess is ", guess
    print "Game left ", str(game_left)
    guessint = int(guess)
    if guessint > secret_number:
        print "Larger"
    elif guessint < secret_number:
        print "Smaller"
    elif guessint == secret_number:
        print "Equal! You win~"
    if game_left == 0:
        print "Game over, start again"
        new_game()
        
# create frame
f = simplegui.create_frame("Guess the number",300,300)

# register event handlers for control elements and start frame
f.add_button("Range  100", range100, 100)
f.add_button("Range 1000", range1000, 100)
f.add_input("Guess", input_guess, 100)

# call new_game 
new_game()
range100()

# always remember to check your completed program against the grading rubric
