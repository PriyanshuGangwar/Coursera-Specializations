"""
Loyd's Fifteen puzzle - solver and visualizer
Note that solved configuration has the blank (zero) tile in upper left
Use the arrows key to swap this tile with its neighbors
"""

import poc_fifteen_gui

class Puzzle:
    """
    Class representation for the Fifteen puzzle
    """

    def __init__(self, puzzle_height, puzzle_width, initial_grid=None):
        """
        Initialize puzzle with default height and width
        Returns a Puzzle object
        """
        self._height = puzzle_height
        self._width = puzzle_width
        self._grid = [[col + puzzle_width * row
                       for col in range(self._width)]
                      for row in range(self._height)]

        if initial_grid != None:
            for row in range(puzzle_height):
                for col in range(puzzle_width):
                    self._grid[row][col] = initial_grid[row][col]

    def __str__(self):
        """
        Generate string representaion for puzzle
        Returns a string
        """
        ans = ""
        for row in range(self._height):
            ans += str(self._grid[row])
            ans += "\n"
        return ans

    #####################################
    # GUI methods

    def get_height(self):
        """
        Getter for puzzle height
        Returns an integer
        """
        return self._height

    def get_width(self):
        """
        Getter for puzzle width
        Returns an integer
        """
        return self._width

    def get_number(self, row, col):
        """
        Getter for the number at tile position pos
        Returns an integer
        """
        return self._grid[row][col]

    def set_number(self, row, col, value):
        """
        Setter for the number at tile position pos
        """
        self._grid[row][col] = value

    def clone(self):
        """
        Make a copy of the puzzle to update during solving
        Returns a Puzzle object
        """
        new_puzzle = Puzzle(self._height, self._width, self._grid)
        return new_puzzle

    ########################################################
    # Core puzzle methods

    def current_position(self, solved_row, solved_col):
        """
        Locate the current position of the tile that will be at
        position (solved_row, solved_col) when the puzzle is solved
        Returns a tuple of two integers        
        """
        solved_value = (solved_col + self._width * solved_row)

        for row in range(self._height):
            for col in range(self._width):
                if self._grid[row][col] == solved_value:
                    return (row, col)
        assert False, "Value " + str(solved_value) + " not found"

    def update_puzzle(self, move_string):
        """
        Updates the puzzle state based on the provided move string
        """
        zero_row, zero_col = self.current_position(0, 0)
        for direction in move_string:
            if direction == "l":
                assert zero_col > 0, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row][zero_col - 1]
                self._grid[zero_row][zero_col - 1] = 0
                zero_col -= 1
            elif direction == "r":
                assert zero_col < self._width - 1, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row][zero_col + 1]
                self._grid[zero_row][zero_col + 1] = 0
                zero_col += 1
            elif direction == "u":
                assert zero_row > 0, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row - 1][zero_col]
                self._grid[zero_row - 1][zero_col] = 0
                zero_row -= 1
            elif direction == "d":
                assert zero_row < self._height - 1, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row + 1][zero_col]
                self._grid[zero_row + 1][zero_col] = 0
                zero_row += 1
            else:
                assert False, "invalid direction: " + direction

    ##################################################################
    # Phase one methods

    def lower_row_invariant(self, target_row, target_col):
        """
        Check whether the puzzle satisfies the specified invariant
        at the given position in the bottom rows of the puzzle (target_row > 1)
        Returns a boolean
        """
        dummy_row=0
        dummy_col=0
        if(self.get_number(target_row,target_col)==0):
            array_0=[]
            array_1=[]
            row=self.get_height()
            col=self.get_width()
            if target_row==row-1 and target_col==col-1:
                return True
            for dummy_row in range(target_row,row):
                for dummy_col in range(target_col,col):
                    target_col=0
                    array_0.append(self.get_number(dummy_row,dummy_col))
            for dummy_row in range(row):
                for dummy_col in range(col):
                    array_1.append(self.get_number(dummy_row,dummy_col))
         
            array_0.pop(0)
            if(len(array_0)==1):
                if(array_0[0]==max(array_1)):
                    return True
                return False
            
            dummy_col=array_0.pop(0)
            for dummy_row in array_0:
                if(dummy_row==dummy_col+1):
                    dummy_col=dummy_row
                else:
                    return False
            return True    
        return False

    def solve_interior_tile(self, target_row, target_col):
        """
        Place correct tile at target position
        Updates puzzle and returns a move string
        """
        dummy_row=0
        dummy_col=0
        move=""
        row=self.get_height()
        col=self.get_width()
        if target_col==col-1 and target_row==row-1:
            ele=(row*col)
            
        elif target_col==col-1 and target_row!=row-1:
            ele=self.get_number(target_row+1,0)
        else:
            ele=self.get_number(target_row,target_col+1)
        for dummy_row in range(row):
            for dummy_col in range(col):
                
                if self.get_number(dummy_row,dummy_col)==ele-1:
                    break
            else:
                continue  
            break         
                    
                 
        #case 1:  
        for _ in range(target_row,dummy_row,-1):
                move+='u'
        if target_col==dummy_col:
           
            for _ in range(target_row-dummy_row-1):
                move+="lddru"
            move+="ld"
            
        elif target_col <dummy_col:
            
            for _ in range(target_col,dummy_col):
                move+="r"
            for _ in range(dummy_col-target_col-1):
                move+="dllur"
            move+="dlu"    
            for _ in range(target_row-dummy_row-1):
                move+="lddru"
            move+="ld" 
            
        elif target_col > dummy_col:
            if target_row==dummy_row:
                for _ in range(dummy_col,target_col):
                    move+="l"
            else:    
                
                for _ in range(target_col-dummy_col):
                    move+="l"
                for _ in range(target_col-dummy_col-1):

                    move+="drrul"
                move+="dru"    
                for _ in range(target_row-dummy_row-1):
                    move+="lddru"
                move+="ld"     
            
#        br=[]        
#        for i in range(row):
#                for j in range(col):
#                    br.append(self.get_number(i,j))
#        print br,move         
        self.update_puzzle(move)        
        return move

    def solve_col0_tile(self, target_row):
        """
        Solve tile in column zero on specified row (> 1)
        Updates puzzle and returns a move string
        """
        dummy_row=0
        dummy_col=0
        move=""
        row=self.get_height()
        col=self.get_width()
        ele=self.get_number(target_row,1)
        
        for dummy_row in range(row):
            for dummy_col in range(col):
                
                if self.get_number(dummy_row,dummy_col)==ele-1:
                    break
            else:
                continue  
            break
            
        for _ in range(target_row-dummy_row):
                move+='u'    
        if dummy_col!=0:
            for _ in range(dummy_col):
                move+="r"
            for _ in range(dummy_col-1):
                move+="dllur"
            move+="dlu"    
        for _ in range(target_row-dummy_row-2):
                move+="rddlu"
        if dummy_row!= target_row-1:        
            move+="rdl"
            move+="ruldrdlurdluurddlur"
        else:
            move+='r'
        for _ in range(1,col-1):
                move+="r"
        
        self.update_puzzle(move) 
#        br=[]        
#        for i in range(row):
#                for j in range(col):
#                    br.append(self.get_number(i,j))
#        print br
        return move

    #############################################################
    # Phase two methods
    def move(self, target_row, target_col, row, column):
        '''
        place a tile at target position;
        target tile's current position must be either above the target position
        (k < i) or on the same row to the left (i = k and l < j);
        returns a move string
        '''
        move_it = ''
        combo = 'druld'

        column_delta = target_col - column
        row_delta = target_row - row

        
        move_it += row_delta * 'u'
        
        if column_delta == 0:
            move_it += 'ld' + (row_delta - 1) * combo
        else:
            
            if column_delta > 0:
                move_it += column_delta * 'l'
                if row == 0:
                    move_it += (abs(column_delta) - 1) * 'drrul'
                else:
                    move_it += (abs(column_delta) - 1) * 'urrdl'
            
            elif column_delta < 0:
                move_it += (abs(column_delta) - 1)  * 'r'
                if row == 0:
                    move_it += abs(column_delta) * 'rdllu'
                else:
                    move_it += abs(column_delta) * 'rulld'
            
            move_it += row_delta * combo

        return move_it

    def row0_invariant(self, target_col):
        """
        Check whether the puzzle satisfies the row zero invariant
        at the given column (col > 1)
        Returns a boolean
        """
        row=self.get_height()
        col=self.get_width()
        if self.get_number(0,target_col)!=0:
            return False
        #for row0&1
        for tmp in range(target_col+1,col):
            if self.get_number(0,tmp)!=tmp:
                return False
        for tmp in range(target_col,col):    
            if self.get_number(1,tmp)!=tmp+col:
                return False
        for dummy_row in range(2,row):
            for dummy_col in range(col):
                if self.get_number(dummy_row,dummy_col)!=dummy_row*col+dummy_col:
                    return False
                
        return True

    def row1_invariant(self, target_col):
        """
        Check whether the puzzle satisfies the row one invariant
        at the given column (col > 1)
        Returns a boolean
        """
        row=self.get_height()
        col=self.get_width()
        if self.get_number(1,target_col)!=0:
            return False
        for tmp in range(target_col+1,col):
            if self.get_number(0,tmp)!=tmp:
                return False
        
            
            if self.get_number(1,tmp)!=tmp+col:
                return False
        for dummy_row in range(2,row):
            for dummy_col in range(col):
                if self.get_number(dummy_row,dummy_col)!=dummy_row*col+dummy_col:
                    return False
                
        return True

    def solve_row0_tile(self, target_col):
        """
        Solve the tile in row zero at the specified column
        Updates puzzle and returns a move string
        """
        assert self.row0_invariant(target_col)
        move_it = 'ld'       
        self.update_puzzle(move_it)

        
        row, column = self.current_position(0, target_col)
        
        if row == 0 and column == target_col:
            return move_it
        else:
            
            step = self.move(1, target_col - 1, row, column)
            
            step += 'urdlurrdluldrruld'
            self.update_puzzle(step)
            move_it += step

        
        return move_it

    def solve_row1_tile(self, target_col):
        """
        Solve the tile in row one at the specified column
        Updates puzzle and returns a move string
        """
        row, column = self.current_position(1, target_col)
        move_it = self.move(1, target_col, row, column)
        move_it += 'ur'

        self.update_puzzle(move_it)
        return move_it


    ###########################################################
    # Phase 3 methods

    def solve_2x2(self):
        """
        Solve the upper left 2x2 part of the puzzle
        Updates the puzzle and returns a move string
        """
        move_it = ''
        first_step = ''

        if self.get_number(1, 1) == 0:
            first_step += 'ul'
            self.update_puzzle(first_step)
            
            if (0, 1) == self.current_position(0, 1) and (1, 1) == self.current_position(1, 1):
                return first_step

            
            if self.get_number(0, 1) < self.get_number(1, 0):
                move_it += 'rdlu'
            else:
                move_it += 'drul'        
            self.update_puzzle(move_it)

        return first_step + move_it

    def solve_puzzle(self):
        """
        Generate a solution string for a puzzle
        Updates the puzzle and returns a move string
        """
        move_it = ''

        
        row = self.get_height() - 1
        column = self.get_width() - 1
        
        row_current, column_current = self.current_position(0, 0)
        
        column_delta = column_current - column
        row_delta = row_current - row
        step = abs(column_delta) * 'r' + abs(row_delta) * 'd'
        self.update_puzzle(step)
        move_it += step

        
        for dummy_row in range(row, 1, -1):
            for dummy_column in range(column, 0, -1):
                move_it += self.solve_interior_tile(dummy_row, dummy_column)
            move_it += self.solve_col0_tile(dummy_row)

        
        for dummy_column in range(column, 1, -1):
            move_it += self.solve_row1_tile(dummy_column)
            move_it += self.solve_row0_tile(dummy_column)

         
        move_it += self.solve_2x2()
        return move_it


poc_fifteen_gui.FifteenGUI(Puzzle(4, 4))



