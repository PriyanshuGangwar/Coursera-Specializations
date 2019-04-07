"""
Mini-max Tic-Tac-Toe Player
"""

import poc_ttt_gui
import poc_ttt_provided as provided

# Set timeout, as mini-max can take a long time
import codeskulptor
codeskulptor.set_timeout(60)

# SCORING VALUES - DO NOT MODIFY
SCORES = {provided.PLAYERX: 1,
          provided.DRAW: 0,
          provided.PLAYERO: -1}

    
            

def mm_move(board, player):
    """
    Make a move on the board.
    
    Returns a tuple with two elements.  The first element is the score
    of the given board and the second element is the desired move as a
    tuple, (row, col).
    """
    res = board.check_win()
    if res:
        return SCORES[res],(-1,-1)
    if len(board.get_empty_squares())==board.get_dim() ** 2:
        return SCORES[player],(0,0)
    res = {0:[],1:[],-1:[]}
    for r,c in board.get_empty_squares():
        clone = board.clone()
        clone.move(r,c,player)
        player_1 = provided.switch_player(player)
        score,move=mm_move(clone,player_1)
        res[score].append((r,c))
    
        if res[SCORES[player]]:
            return SCORES[player],res[SCORES[player]][0]
    t=provided.switch_player(player)
    if res[0]:
        return 0,res[0][0]
    
    elif res[SCORES[t]]:
        return SCORES[t],res[SCORES[t]][0]
    
    return 0,(-1, -1)

def move_wrapper(board, player, trials):
    """
    Wrapper to allow the use of the same infrastructure that was used
    for Monte Carlo Tic-Tac-Toe.
    """
    move = mm_move(board, player)
    assert move[1] != (-1, -1), "returned illegal move (-1, -1)"
    return move[1]



provided.play_game(move_wrapper, 1, False)        
poc_ttt_gui.run_gui(3, provided.PLAYERO, move_wrapper, 1, False)

