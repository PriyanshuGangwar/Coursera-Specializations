"""
MC TIC TAC TOE
"""

import random
import poc_ttt_gui
import poc_ttt_provided as provided

# Constants for Monte Carlo simulator
# You may change the values of these constants as desired, but
#  do not change their names.
NTRIALS = 5000        # Number of trials to run
SCORE_CURRENT = 1.0 # Score for squares played by the current player
SCORE_OTHER = 1.0   # Score for squares played by the other player
#scores=[]    
# Add your functions here.
def mc_trial(board,player):
    """
    trials
    """
    while board.check_win() == None:
        empty = board.get_empty_squares()
        rsquare = empty[random.randrange(len(empty))]
        board.move(rsquare[0], rsquare[1], player)
        player = provided.switch_player(player)

def mc_update_scores(scores, board, player):
    """
    updates scores
    """
    
    if board.check_win() == provided.DRAW:
        return
    winner = board.check_win()
    for row in range(board.get_dim()):
        for col in range(board.get_dim()):
            square = board.square(row, col)
            if square == winner:
                if winner==player:
                    scores[row][col] += SCORE_CURRENT
                else:
                    scores[row][col] += SCORE_OTHER
            elif square == provided.EMPTY:
                continue
            else:
                if winner == player:
                    scores[row][col] -= SCORE_CURRENT
                else:
                    scores[row][col] -= SCORE_OTHER

                    
def get_best_move(board,scores):
    """
    detrmining best move
    """
    print board
    print scores
    esquares=board.get_empty_squares()
    
    maxx = -10000
    
    result=[]
    for empty in esquares:
        if maxx<= scores[empty[0]][empty[1]]:
            maxx=scores[empty[0]][empty[1]]
    for empty in esquares:
        if maxx== scores[empty[0]][empty[1]]:
            result.append(empty)
    
    return random.choice(result)      


def mc_move(board,player,trials):
    """
    for playing trials
    """
    global scores
    scores=[[0 for a0 in range(board.get_dim())] for a0 in range(board.get_dim())] 
    tboard=board.clone()
    while trials>0:
        mc_trial(tboard,player)
        
        mc_update_scores(scores, tboard, player)
        trials-=1
    best=  get_best_move(board,scores) 
    return best


provided.play_game(mc_move, NTRIALS, False)        
poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)
