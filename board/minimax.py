import numpy as np


def can_play(board, N):
    for i in range(N):
        for j in range(N):
            if board[i][j] == "_":
                return True
    return False


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


def check_if_someone_won(board, player, opponent):
    for newBoard in [board, np.transpose(board)]:
        result = checkRows(newBoard)
        if result:
            if result == player:
                return 10
            elif result == opponent:
                return -10
    diagonals = checkDiagonals(board)
    if diagonals == player:
        return 10
    elif diagonals == opponent:
        return -10
    else:
        return 0


def minimax(board, depth, isMax, N, player, opponent):
    score = check_if_someone_won(board, player, opponent)
    # maximizer won
    if score == 10:
        return score

    # minimizer won
    if score == -10:
        return score

    # tie
    if can_play(board, N) == False:
        return 0

    # maximizers move
    if isMax:
        best = -1000

        # Traverse all cells
        for i in range(N):
            for j in range(N):

                # Check if cell is empty
                if board[i][j] == "_":

                    # Make the move
                    board[i][j] = player

                    # Call minimax recursively and choose
                    # the maximum value
                    best = max(
                        best, minimax(board, depth + 1, not isMax, N, player, opponent)
                    )

                    # Undo the move
                    board[i][j] = "_"
        return best

    # minimizers move
    else:
        best = 1000

        # Traverse all cells
        for i in range(N):
            for j in range(N):

                # Check if cell is empty
                if board[i][j] == "_":

                    # Make the move
                    board[i][j] = opponent

                    # Call minimax recursively and choose
                    # the minimum value
                    best = min(
                        best, minimax(board, depth + 1, not isMax, N, player, opponent)
                    )

                    # Undo the move
                    board[i][j] = "_"
        return best


# This will return the best possible move for the player
def search_for_best_move(board, N, p, o):
    bestVal = -1000
    bestMove = (-1, -1)

    # check all of board
    for i in range(N):
        for j in range(N):

            # Check if cell is empty
            if board[i][j] == "_":

                # Make the move
                board[i][j] = p

                # compute evaluation function for this
                # move.
                moveVal = minimax(board, 0, False, N, p, o)

                # Undo the move
                board[i][j] = "_"

                if moveVal > bestVal:
                    bestMove = (i, j)
                    bestVal = moveVal

    return bestMove
