import sys
import argparse
from random import randint
from minimax import search_for_best_move
import os
import numpy as np


def cls():
    os.system("cls" if os.name == "nt" else "clear")


def printBoard(board):
    for row in board:
        print(row)


def findIndex(move):
    move -= 1
    return (move // 3, move % 3)


def pickSpace():
    row = int(input("Select a row: "))
    column = int(input("Select a column: "))
    # if not 1 <= space <= 9:
    #     raise ValueError
    return row, column


def markMove(move, x, board):
    i, j = move
    if board[i][j] == "_":
        board[i][j] = "X" if x else "O"
    else:
        raise ValueError


def checkDraw(board):
    for row in board:
        for ele in row:
            if ele == "_":
                return False
    print("\nThe game is a draw")
    printBoard(board)
    return True

    # def checkWin(board):
    # winner = None
    # for i in range(3):
    #     # horizontal win
    #     if board[i][0] == board[i][1] == board[i][2] and board[i][0] != "_":
    #         winner = board[i][0]
    #         break
    #     # vertical win
    #     if board[0][i] == board[1][i] == board[2][i] and board[0][i] != "_":
    #         winner = board[0][i]
    #         break
    # # diagonal win
    # if board[1][1] != "_":
    #     if (
    #         board[0][0] == board[1][1] == board[2][2]
    #         or board[0][2] == board[1][1] == board[2][0]
    #     ):
    #         winner = board[1][1]
    # if winner is not None:
    #     print("\n\n\n")
    #     printBoard(board)
    #     print(winner + " is the winner of the game!")
    #     return True
    # return False


def checkRows(board):
    for row in board:
        if "_" not in row:
            if len(set(row)) == 1:
                return row[0]
    return 0


def checkDiagonals(board):
    if len(set([board[i][i] for i in range(len(board))])) == 1:
        if board[0][0] != "_":
            return board[0][0]
    if len(set([board[i][len(board) - i - 1] for i in range(len(board))])) == 1:
        if board[0][len(board) - 1] != "_":
            return board[0][len(board) - 1]
    return 0


def checkWin(board):
    # transposition to check rows, then columns
    for newBoard in [board, np.transpose(board)]:
        result = checkRows(newBoard)
        if result:
            return result
    return checkDiagonals(board)


def create_board(n):
    return [["_" for _ in range(n)] for _n in range(n)]


def main():

    print("Please enter a NxN game you would like to play:\n")
    N = int(input("N: "))
    # print(checkWin(create_board(N)))

    board = create_board(N)
    x = True
    goal = False
    err = False
    count = 0

    while not goal:

        if x == False:
            # have ai play
            print(f"\nCurrent Board [{count}]:")
            printBoard(board)
            move = search_for_best_move(board, N, "O", "X")
            markMove(move, x, board)
        else:
            # cls()
            print(f"\nCurrent Board [{count}]:")
            printBoard(board)
            # Uncomment out below code to play manually
            # try:
            #     move = pickSpace()
            #     markMove(move, x, board)
            # except ValueError:
            #     print("Must select an unoccupied square 1-9")
            #     continue

            # BELOW CODE IS FOR AI TO PLAY AGAINST ITSELF
            if count == 0:
                move = randint(0, N - 1), randint(0, N - 1)
            else:
                move = search_for_best_move(board, N, "X", "O")
            markMove(move, x, board)
        goal = checkDraw(board)
        winner = checkWin(board)
        if winner != 0:
            print(winner, "has won!")
            printBoard(board)
            goal = True
        x = not x
        count += 1


if __name__ == "__main__":
    main()
