import sys
import argparse




def printBoard(board):
    for row in board:
        print(row)

def findIndex(move):
    move -= 1
    return (move // 3, move % 3)

def pickSpace():
    space = int(input("Select a square: "))
    if not 1 <= space <= 9:
        raise ValueError
    return space

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
    printBoard(board)
    print("The game is a draw")
    return True

def checkWin(board):
    winner = None
    for i in range(3):
        #horizontal win
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != "_":
            winner = board[i][0]
            break
        #vertical win
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != "_":
            winner = board[0][i]
            break
    #diagonal win
    if board[1][1] != "_":
        if (board[0][0] == board[1][1] == board[2][2] or board[0][2] == board[1][1] == board[2][0]):
            winner = board[1][1]
    if winner is not None:
        printBoard(board)
        print(winner + " is the winner of the game!")
        return True
    return False


def main():
    board = [["_" for _ in range(3)] for _ in range(3)]
    x = True
    goal = False
    while not goal:
        printBoard(board)
        try:
            move = findIndex(pickSpace())
            markMove(move, x, board)
        except ValueError:
            print("Must select an unoccupied square 1-9")
            continue
        goal = checkWin(board) or checkDraw(board)
        x = not x


if __name__ == "__main__":
    main()
