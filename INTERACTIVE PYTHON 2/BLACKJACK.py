# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
msg = ""
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.hand=[]
        

    def __str__(self):
        
        i=""
        for a in self.hand:
            i+=a.__str__()+" "
            
        return i	
       
    
    def add_card(self, card):
        self.hand.append(card)	# add a card object to a hand

    def get_value(self):
        value=0
        for i in range(len(self.hand)):
            index=self.hand[i].rank
            value+=VALUES[index]
            
            if 'A' in self.hand[i].rank:
                if value+10<=21:
                     value+=10
                
        
        return int(value)
   
    def draw(self, canvas, pos):
        self.hand.draw() 	# draw a hand on the canvas, use the draw method for cards
 
        
# define deck class 
class Deck:
    def __init__(self):
        self.deck=[]
       
        for i in range(len(SUITS)):
            for j in range(len(RANKS)):
                self.deck.append(Card(SUITS[i],RANKS[j]))

        
        
    def shuffle(self):
        # shuffle the deck 
        random.shuffle(self.deck)

    def deal_card(self):
       
        return self.deck.pop(0)# deal a card object from the deck
    
    def __str__(self):
        s=""
        
        for i in range(len(self.deck)):
             
            s+=str(self.deck[i])+" "
        return str(s)		# return a string representing the deck



#define event handlers for buttons
def deal():
    global in_play,deck,player,dealer,msg,score
    if in_play :
        msg="YOU LOST!!!"
        score-=1
        in_play=False
    else:
        deck = Deck()
        deck.shuffle()


        player = Hand()
        player.add_card(deck.deal_card())
        player.add_card(deck.deal_card())

        dealer = Hand()
        dealer.add_card(deck.deal_card())
        dealer.add_card(deck.deal_card())

        msg=""
        in_play = True

def hit():
    global player,score,in_play,msg
    if in_play == True:
        
        player.add_card(deck.deal_card())
        
        if player.get_value() > 21:   

            msg= "You have Busted!!!"
            in_play = False
            score-=1
           
 
    # if the hand is in play, hit the player
   
    # if busted, assign a message to outcome, update in_play and score
       
def stand():
    global dealer ,player,score,in_play,msg
    if in_play==True:
        
       
        while dealer.get_value() < 17:
            dealer.add_card(deck.deal_card())

       
        if dealer.get_value() > 21:
                msg= "DEALER BUSTED!!! YOU WIN"
                
                score+=1
        elif dealer.get_value() <  player.get_value() :
            msg= " YOU WIN !!!"
            score+=1

        else:
            msg= " YOU LOST !!!"
            score-=1
        in_play = False
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more

    # assign a message to outcome, update in_play and score

# draw handler    
def draw(canvas):
 # @  global
    j=80
    if in_play== True:
        card_loc = (CARD_CENTER[0] , CARD_CENTER[1] ) 

        canvas.draw_image(card_back, card_loc, CARD_SIZE, [70 + CARD_CENTER[0], 190 + CARD_CENTER[1]], CARD_SIZE)
    else:
        card = Card(dealer.hand[0].suit,dealer.hand[0].rank)
        card.draw(canvas, [70, 190])
    for i in range(1,len(dealer.hand)):
        
        card = Card(dealer.hand[i].suit,dealer.hand[i].rank)
        card.draw(canvas, [70+j, 190])
        j+= 80
        
    j=0    
    for i in range(len(player.hand)):
        
        card = Card(player.hand[i].suit,player.hand[i].rank)
        card.draw(canvas, [70+j, 430])
        j+= 80
    if in_play == True:
        canvas.draw_text('HIT OR STAND ??', (380, 200), 20, 'White','sans-serif')
    else:
        canvas.draw_text('NEW DEAL ??', (390, 200), 20, 'Orange','sans-serif')
   

    canvas.draw_text(msg, (200, 150), 20, 'White')
               
    canvas.draw_text('BLACKJACK', (180, 40), 40, 'White','sans-serif')
    canvas.draw_line((0, 50), (600, 50), 4, 'White')
    canvas.draw_line((0, 168), (600, 168), 2, 'White')
    canvas.draw_line((0, 408), (600, 408), 2, 'White')
    canvas.draw_line((0, 128), (600, 128), 2, 'White')
    canvas.draw_line((0, 368), (600, 368), 2, 'White')
    canvas.draw_text('Score: ', (390, 100), 40, 'White')
    canvas.draw_text(str(score), (500, 100), 40, 'White')
    
    canvas.draw_text('Dealer', (50, 160), 30, 'Black')
    canvas.draw_text('Player', (50, 400), 30, 'Black')
    

# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Teal")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()

# remember to review the gradic rubric