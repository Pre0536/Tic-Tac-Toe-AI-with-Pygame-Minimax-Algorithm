import math
from random import choice
from math import inf as infinity

# Tic-Tac-Toe with Minimax-Algorithm
#
# A Python implementation of Tic-Tac-Toe featuring:
# - Pygame graphical interface
# - Unbeatable AI using Minimax algorithm
# - Alpha-Beta pruning optimization
# - Interactive gameplay with player choice (X/O)
#
# Features:
# - Perfect AI opponent (never loses)
# - Game state tracking
# - Restart capability
#
# Author: Pre0536
# Date: 05.06.2025
# Version: 1.0

X = "X"
O = "O"
EMPTY = None
pl = X
first = True

def initial_state():
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

def player(board):
    global pl
    global first
    NoOfX = 0
    NoOfO = 0

    if first is True:
        first = False
        return pl
    else:
        for i in range(0, len(board)):
            for j in range(0, len(board[0])):
                if board[i][j] == X:
                    NoOfX += 1
                elif board[i][j] == O:
                    NoOfO += 1

        if NoOfX > NoOfO:
            pl = O
        else:
            pl = X
        return pl
    
def actions(board):
    places = []
    if not terminal(board):
        for x, row in enumerate(board):
            for y, cell in enumerate(row):
                if cell == None:
                    places.append([x, y])
        return places
    
def result(board, action):
    b = board
    x, y = action[0], action[1]
    b[x][y] = player(board)
    return b

def winner(board):
    WinState = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[2][0], board[1][1], board[0][2]],
    ]
    if [X, X, X] in WinState:
        return X
    elif [O, O, O] in WinState:
        return O
    else:
        return None
    
def terminal(board):
    if (winner(board) is not None) or (not any(EMPTY in sublist for sublist in board) and winner(board) is None):
        return True
    else:
        return False
    
def utility(board):
    if terminal(board):
        if winner(board) == X:
            score = 1
        elif winner(board) == O:
            score = -1
        else:
            score = 0

        return score
    
def computer_turn(board, length, pl, alpha=-infinity, beta=infinity):
    if pl == X:
        best = [-1, -1, -infinity]
    else:
        best = [-1, -1, +infinity]

    if length == 0 or terminal(board):
        score = utility(board)
        return [-1, -1, score]

    for cell in actions(board):
        x, y = cell[0], cell[1]
        board[x][y] = pl
        score = computer_turn(board, length - 1, player(board), alpha, beta)
        board[x][y] = EMPTY
        score[0], score[1] = x, y

        if pl == X:
            if score[2] > best[2]:
                best = score
                alpha = max(alpha, best[2])
        else:
            if score[2] < best[2]:
                best = score
                beta = min(beta, best[2])
        
        if alpha >= beta:
            break

    return best

def minimax(board):
    length = len(actions(board))
    if length == 0 or terminal(board):
        return None
    
    if length == 9:
        return [choice([0, 1, 2]), choice([0, 1, 2])]
    
    move = computer_turn(board, length, pl)
    return [move[0], move[1]]

