# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
PAD1_POS=[HALF_PAD_WIDTH, HEIGHT/2-HALF_PAD_HEIGHT]
PAD2_POS=[WIDTH-HALF_PAD_WIDTH, HEIGHT/2-HALF_PAD_HEIGHT]
paddle1_vel=0
paddle2_vel=0
ball_pos=[]
ball_vel=[4,2]
flag='a'
score_l=0
score_r=0
RIGHT=True
LEFT=False


def spawn_ball(direction):
    global ball_pos, ball_vel
    ball_pos=[WIDTH/2,HEIGHT/2]
    if direction == RIGHT:
        ball_vel=[4,-2]
    elif direction == LEFT:
         ball_vel=[-4,-2]


            
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel,PAD1_POS,PAD2_POS  # these are numbers
    global score_l, score_r  # these are ints
    score_l=0
    score_r=0
    ball_pos=[WIDTH/2,HEIGHT/2]
    PAD1_POS=[HALF_PAD_WIDTH, HEIGHT/2-HALF_PAD_HEIGHT]
    PAD2_POS=[WIDTH-HALF_PAD_WIDTH, HEIGHT/2-HALF_PAD_HEIGHT]
    spawn_ball(RIGHT)
    flag='a'
    
    
   

def draw(canvas):
    global score_l, score_r, paddle1_pos, paddle2_pos, ball_pos, ball_vel,paddle1_vel, paddle2_vel
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball_pos[0] += ball_vel[0]  
    ball_pos[1] += ball_vel[1] 
    
    
    if ball_pos[1]<= BALL_RADIUS or ball_pos[1]>= HEIGHT-BALL_RADIUS:
        ball_vel[1]= -ball_vel[1]
    # draw ball
    canvas.draw_circle(ball_pos,BALL_RADIUS,1,'White','White')
    
 
   

    canvas.draw_line((PAD1_POS), (PAD1_POS[0], PAD1_POS[1]+PAD_HEIGHT), PAD_WIDTH, 'White') 
    canvas.draw_line((PAD2_POS), (PAD2_POS[0], PAD2_POS[1]+PAD_HEIGHT), PAD_WIDTH, 'White')
    # determine whether paddle and ball collide    
    
    if ball_pos[0]<= BALL_RADIUS+PAD_WIDTH: # or ball_pos[0]>= WIDTH-BALL_RADIUS-PAD_WIDTH:
        if ball_pos[1]>= PAD1_POS[1] and ball_pos[1]<= PAD1_POS[1]+PAD_HEIGHT :
            ball_vel[0]= -ball_vel[0]
        else:
            score_r+=1
            spawn_ball(RIGHT)
        ball_vel[0]+= 0.1*ball_vel[0]    
    if ball_pos[0]>= WIDTH-BALL_RADIUS-PAD_WIDTH:
        if ball_pos[1]>= PAD2_POS[1] and ball_pos[1]<= PAD2_POS[1]+PAD_HEIGHT :
            ball_vel[0]= -ball_vel[0]
        else:
            score_l+=1
            spawn_ball(LEFT)
        ball_vel[0]+= 0.1*ball_vel[0]
        
   
    if PAD1_POS[1]<=3 and flag==87:
         paddle1_vel=0
    elif PAD1_POS[1]>=HEIGHT-PAD_HEIGHT and flag==83:
           paddle1_vel=0    
    
   
    if PAD2_POS[1]<=3 and flag==38:
         paddle2_vel=0
    elif PAD2_POS[1]>=HEIGHT-PAD_HEIGHT and flag==40:
           paddle2_vel=0  
            
            
    PAD1_POS[1]+=paddle1_vel
    
    PAD2_POS[1]+=paddle2_vel 
    
    
    canvas.draw_text(str(score_l), (150, 50), 30, 'White')
    canvas.draw_text(str(score_r), [450, 50], 30, 'White')
    
    
        
def keydown(key):
    global paddle1_vel, paddle2_vel,flag
    flag=key
    
    if key==simplegui.KEY_MAP["up"]:
        paddle2_vel-=6
       
        
    elif key==simplegui.KEY_MAP["down"]:
         paddle2_vel+=6 
    
    if key==simplegui.KEY_MAP["W"]:
        
        
            paddle1_vel-=6
        
    elif key==simplegui.KEY_MAP["S"]:
         paddle1_vel+=6 

            
def keyup(key):
    global paddle1_vel, paddle2_vel
    paddle1_vel=0
    paddle2_vel=0

# create frame


frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
button1 = frame.add_button('RESTART', new_game)

# start frame
new_game()
frame.start()
