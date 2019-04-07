"""
Clone of 2048 game.
"""

import poc_2048_gui
import random
# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}

def merge(lines):
    """
    Helper function that merges a single row or column in 2048
    """
    

    flag=0
    lst=[]
    check=[]
    
    line=[index_1 for index_1 in lines]
    for index_3 in range(1,12):
        check.append(pow(2,index_3))
    
    if len(line)==1:
        return line
      
           
    for index_2 in range(0,len(line)-1):
        for index_1 in range(0,len(line)-1):
            if line[index_1]==0:
                tmp=line[index_1]
                line[index_1]=line[index_1+1]
                line[index_1+1]=tmp
    index_1=0  
       
    while index_1 < len(line):
        flag=0
        if index_1==len(line)-1:
            lst.append(line[index_1])
            break
        else:
            
            number=line[index_1]+line[index_1+1]
            for index_2 in range(0,11):
                if number==check[index_2] :
                    flag=1
                    break
            if(flag==1):
                lst.append(number)
                line[index_1+1]=0
                index_1=index_1+2
            else:
                lst.append(line[index_1])
                index_1=index_1+1
        
            
        
            
    
    if len(lst)!=len(line):
        for index_1 in range(0,len(line)-len(lst)):
            lst.append(0)
            
            
    return lst



class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        self._grid_height = grid_height
        self._grid_width = grid_width
        
#        self.i_tiles = { UP: [(0,i) for i in range(0,self._grid_width)],
#                         DOWN: [(self._grid_height-1,i) for i in range(self._grid_width)],
#                         LEFT: [(i,0) for i in range(0,self._grid_height)],
#                         RIGHT: [(i,self._grid_width-1) for i in range(self._grid_height)]
#                       }
        
#        print self.i_tiles.items()
        self.reset()
#        print self.__str__()

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        self._grid = [ [0 for _ in range(self._grid_width)] for __ in range(self._grid_height)]
        
        self.new_tile() 
        self.new_tile()
        

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        # replace with your code
        return str(self._grid)

    def get_grid_height(self):
        """
        Get the height of the board.
        """
       
        return self._grid_height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        
        return self._grid_width 
    
    
    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        
        
        
        if direction == UP:
            for col in range(self._grid_width):
                lst=[]
                for row in range(self._grid_height):
                    print "row= ",row,"  ",col
                    lst.append(self._grid[row][col])
              
                flist=merge(lst)
           
                for row in range(self._grid_height):
                    self._grid[row][col] = flist[row]
            self.new_tile() 
            
            
        elif direction == DOWN:
                for col in range(self._grid_width-1,-1,-1):
                    lst=[]
                    for row in range(self._grid_height-1,-1,-1):
                        lst.append(self._grid[row][col])
                    flist=merge(lst)
                     
                    row1=0
                    for row in range(self._grid_height-1,-1,-1):
                        self._grid[row][col] = flist[row1]
                        row1+=1
                self.new_tile() 
                
        elif direction == LEFT:
                for row in range(self._grid_height):
                    lst=[]
                    for col in range(self._grid_width):
                        lst.append(self._grid[row][col])
                      
                    flist=merge(lst)
                    
                    
                    
                    for col in range(self._grid_width):
                        
                        self._grid[row][col] = flist[col]
                        
                self.new_tile() 
                
                
        elif direction == RIGHT:
                for row in range(self._grid_height):
                    lst=[]
                    for col in range(self._grid_width-1,-1,-1):
                        lst.append(self._grid[row][col])
    
                    flist=merge(lst)

                    row1=0
                    
                    for col in range(self._grid_width-1,-1,-1):
                        
                        self._grid[row][col] = flist[row1]
                        row1+=1      
                self.new_tile()    
        #print self._grid         
        
        

    
    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        
        count=0
        for col in range(self._grid_width):
            for row in range(self._grid_height):
                if self._grid[row][col]==0:
                    count+=1
        if count==0:
            return
        
        
        r_row = random.randrange(0,self._grid_height) 
        r_col = random.randrange(0,self._grid_width) 
        if self._grid[r_row][r_col] == 0:
            if int(random.random() *100) < 90:
                 self.set_tile( r_row, r_col, 2)
            else:
                 self.set_tile( r_row, r_col, 4)
        else:
            self.new_tile()

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self._grid[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """    
    
        return self._grid[row][col]


poc_2048_gui.run_gui(TwentyFortyEight(4, 4))
