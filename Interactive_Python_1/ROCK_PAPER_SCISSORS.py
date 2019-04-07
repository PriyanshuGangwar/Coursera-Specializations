# 0=rock
# 1=spock
# 2=paper
# 3=lizard
# 4=scissors

import random

def name_to_number(name):
    if name == "rock":
          return 0
    if name == "spock":
          return 1
    if name == "paper":
          return 2
    if name == "lizard":
          return 3
    if name == "scissors":
          return 4	
def number_to_name(number):
    if number == 0 :
          return "rock"
    if number == 1:
          return "spock"
    if number == 2:
          return "paper"
    if number == 3:
          return "lizard"
    if number == 4:
          return "scissors"

def rpsls(name):
    num1= name_to_number(name)
    num2= random.randint(0,4)	
    print "Player choose ",name
    print "Computer choose ",number_to_name(num2)	 
    difference=num2-num1
    
    if(difference==1) or (difference==2) or (difference==-3) or (difference==-4):
        print "Computer wins "
    elif(difference==3) or (difference==4) or (difference==-1) or (difference==-2):
        print "Player wins"
    elif difference==0:
        print "Player and Computer tie!!"	 
         
rpsls("rock")
rpsls("spock")		 
rpsls("paper")
rpsls("lizard")
rpsls("scissors")		 