# template for "Stopwatch: The Game"
import simplegui
# define global variables
A=0
B=0
C=0
D=0
time=0
x=0
y=0
flag=1

def format(time):
    global A,B,C,D
    
    A=time/600
    num=time%600
    
    D=num%10
    num/=10
    
    C=num%10
    num/=10
    
    B=num%10
    return str(A)+':'+str(B)+str(C)+'.'+str(D)
    

def start():
    global flag
    flag =1

    timer.start()
    
    

def stop():
    global x,y,flag
    
    timer.stop()
    if flag==1:
        y=y+1
        if D == 0:
            x=x+1
     
    flag=0

def reset():
    global time,x,y
    time=0
    x=0
    y=0
    
                                            
def time_handler():
    global time
    
    time+=1 
    
                 

def draw(canvas):
    canvas.draw_text(format(time), (90, 150), 50, 'White')                                        
    canvas.draw_text(str(x)+"/"+str(y), (260, 30), 30, 'Red')               
   
        
        
        
timer=simplegui.create_timer(100,time_handler)

    

frame=simplegui.create_frame("STOPWATCH",300,300)


button1 = frame.add_button("Start",start,100)
button2 = frame.add_button("Stop",stop,100)
button3 = frame.add_button("Reset",reset,100)


frame.set_draw_handler(draw)
frame.start()

