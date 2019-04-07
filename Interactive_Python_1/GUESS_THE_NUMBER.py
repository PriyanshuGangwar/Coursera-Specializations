
import simplegui
import random

g1=0
# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global num1,num2,g1,g
   

def reset(): 
    global g,g1
    if g1==7:
        range100()
    if g1==10:
        range1000()
   

# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global num1,g,g1
    print "NEW GAME.  Range is (0,100)"
    g=7
    g1=7
   
    num1= random.randrange(0,100)
 
    
    

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global num1,g,g1
    print "NEW GAME.  Range is (0,1000)"
    g=10
    g1=10
    num1= random.randrange(0,1000)

    
    
def input_guess(guess):
    # main game logic goes here	
    global num2,g
    
    num2=int(guess)
    
    print "Guess was : ",guess
    print 'Number of remaining guesses is: ',g
    
    if g==0 and num2!=num1:
        print "You loose!!"
        exit()
   
    
    if num2==num1:
        print "Correct!"
        new_game()
        reset()
        
        
    elif num2<num1:
        print "Higher!"
        
    elif num2>num1:
        print "Lower!"
        
    g = g-1
    print
    
# create frame

frame=simplegui.create_frame("Guess the number",200,200)

# register event handlers for control elements and start frame
frame.add_button("Range (0-100)",range100,200)
frame.add_button("Range (0-1000)",range1000,200)
frame.add_input("Enter the Guess", input_guess,200)
frame.start()
# call new_game 
new_game()