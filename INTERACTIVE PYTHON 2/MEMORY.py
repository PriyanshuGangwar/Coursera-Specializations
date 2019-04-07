# implementation of card game - Memory

import simplegui
import random
state=0
colour= 'Red'
lst=range(0,8)+range(0,8)
index=0
exposed=[]
ref1=0
ref2=0
turns=0

# helper function to initialize globals
def new_game():
    global exposed
    global state,turns
    turns=0
    state=0
    exposed =[False]*16
    
    random.shuffle(lst)
    random.shuffle(exposed)
    
    label.set_text("Turns = 0")
# define event handlers
def mouseclick(pos):
    
    i=0
    
    global index,turns
    global state,ref1,ref2
    
    index=0
    while(i<=800):
        if pos[0]>=i and pos[0]<=i+49:
            
            break
        else:
            index+=1
        i=i+50    
    
    if exposed[index]==False:
        exposed[index]=True
        if state == 0:
            state=1
            ref1=index
            turns+=1
        
        elif state == 1:
            state=2
            ref2=index
            
            
        
        else:
           
            if lst[ref1]==lst[ref2]:
                pass
            else:
                exposed[ref1]=False
                exposed[ref2]=False   
            state=1
            ref1 = index
            turns+=1
    label.set_text("Turns = "+str(turns))
      
        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    j=13
    k=25
    for i in range(0,len(lst)):
        if exposed[i]==True:
            canvas.draw_text(str(lst[i]), (j, 75), 68, 'White')
        else:
            canvas.draw_line([k, 0],[k, 100], 49, 'Green')
        j=j+50    
        k=k+50


frame = simplegui.create_frame("Memory", 800, 100)

frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")


frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)


new_game()
frame.start()


