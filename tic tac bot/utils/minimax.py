from calcscore import *
import math

def finish(board):
    if "" in board:
        return False
    return True

def minimax(board, depth, maxMode):
    value = score(board)
    if value == 10 or value == -10:
        return value

    if finish(board) == True:
        return 0

    if maxMode:
        bestVal = -math.inf
        for i in range(len(board)):
            if board[i] == "":
                board[i] = "O"
                value = minimax(board, depth+1, False)
                bestVal = max(bestVal, value)
                board[i] = ""

        return bestVal

    else:
        bestVal = math.inf
        for i in range(len(board)):
            if board[i] == "":
                board[i] = "X"
                value = minimax(board, depth+1, True)
                bestVal = min(bestVal, value)
                board[i] = ""

        return bestVal

def bestMove(board):
    bestVal = -math.inf
    bestMove = -1
    moveVal = -math.inf

    for i in range(len(board)):
        if board[i] == "":
            board[i] = "O"
            moveVal = minimax(board, 0, False)
            board[i] = ""

        if moveVal > bestVal:
            bestVal = moveVal
            bestMove = i

    print("Best Move is to Position {}".format(bestMove))
    print("Value = {}".format(bestMove))

bestMove(["X", "", "O", "", "X", "", "", "", ""])


