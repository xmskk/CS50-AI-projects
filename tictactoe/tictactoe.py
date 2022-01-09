"""
Tic Tac Toe Player
"""

import math, copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    PX = 0
    PO = 0

    if terminal(board):
        return "Game is already over"

    for row in board:
        for cell in row:
            if cell is X:
                PX += 1
            elif cell is O:
                PO += 1
    
    if PX > PO:
        return O
    else:
        return X



def actions(board):
    actionSet = set()

    if terminal(board):
        return "Game is already over"

    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if cell is EMPTY:
                actionSet.add((i, j))
    
    return actionSet


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board = copy.deepcopy(board)
    if new_board[action[0]][action[1]] is not EMPTY:
        raise Exception("Invalid action")
    new_board[action[0]][action[1]] = player(board)

    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    #print(board)
    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if cell is not EMPTY:
                if i-1 >= 0 and i+1 < 3:
                    if board[i+1][j] is cell and board[i-1][j] is cell:
                        return cell
                if j-1 >= 0 and j+1 < 3:
                    if board[i][j+1] is cell and board[i][j-1] is cell:
                        return cell
                if i-1 >= 0 and j-1 >= 0 and i+1 < 3 and j+1 < 3:
                    if board[i-1][j-1] is cell and board[i+1][j+1] is cell:
                        return cell
                    elif board[i-1][j+1] is cell and board[i+1][j-1] is cell:
                        return cell
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True

    for row in board:
        for cell in row:
            if cell is EMPTY:
                return False
    
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) is X:
        return 1
    elif winner(board) is O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    vmax = -math.inf
    vmin = math.inf
    if player(board) is X:
        v = -math.inf
        for action in actions(board):
            minn = minimum(result(board, action), vmax, vmin)
            if minn > v:
                v = minn
                va = action
        return va
    if player(board) is O:
        v = math.inf
        for action in actions(board):
            maxx = maximum(result(board, action), vmax, vmin)
            if maxx < v:
                v = maxx
                va = action
        return va


def maximum(board, vmax, vmin):
    """
    Returns the maximum possible utility for the current board
    """
    if terminal(board):
        return utility(board)
    v = -math.inf
    for action in actions(board):
        v = max(v, minimum(result(board, action), vmax, vmin))
        vmax = max(vmax, v)
        if vmin <= vmax:
            break 
    return v
    

def minimum(board, vmax, vmin):
    """
    Returns the minimum possible utility for the current board
    """
    if terminal(board):
        return utility(board)
    v = math.inf
    for action in actions(board):
        v = min(v, maximum(result(board, action), vmax, vmin))
        vmin = min(vmin, v)
        if vmin <= vmax:
            break
    return v