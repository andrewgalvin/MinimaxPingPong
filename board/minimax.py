player, opponent = 'O', 'X'

def can_play(board) :
	for i in range(3) :
		for j in range(3) :
			if (board[i][j] == '_') :
				return True
	return False

def check_if_someone_won(b) :

	# Checking for Rows for X or O victory.
	for row in range(3) :	
		if (b[row][0] == b[row][1] and b[row][1] == b[row][2]) :	
			if (b[row][0] == player) :
				return 10
			elif (b[row][0] == opponent) :
				return -10

	# Checking for Columns for X or O victory.
	for col in range(3) :
	
		if (b[0][col] == b[1][col] and b[1][col] == b[2][col]) :
		
			if (b[0][col] == player) :
				return 10
			elif (b[0][col] == opponent) :
				return -10

	# Checking for Diagonals for X or O victory.
	if (b[0][0] == b[1][1] and b[1][1] == b[2][2]) :
	
		if (b[0][0] == player) :
			return 10
		elif (b[0][0] == opponent) :
			return -10

	if (b[0][2] == b[1][1] and b[1][1] == b[2][0]) :
	
		if (b[0][2] == player) :
			return 10
		elif (b[0][2] == opponent) :
			return -10

	# Else if none of them have won then return 0
	return 0

def minimax(board, depth, isMax) :
	score = check_if_someone_won(board)

	# maximizer won
	if (score == 10) :
		return score

	# minimizer won
	if (score == -10) :
		return score

	# tie
	if (can_play(board) == False) :
		return 0

	# maximizers move
	if (isMax) :	
		best = -1000

		# Traverse all cells
		for i in range(3) :		
			for j in range(3) :
			
				# Check if cell is empty
				if (board[i][j]=='_') :
				
					# Make the move
					board[i][j] = player

					# Call minimax recursively and choose
					# the maximum value
					best = max( best, minimax(board,
											depth + 1,
											not isMax) )

					# Undo the move
					board[i][j] = '_'
		return best

	# minimizers move
	else :
		best = 1000

		# Traverse all cells
		for i in range(3) :		
			for j in range(3) :
			
				# Check if cell is empty
				if (board[i][j] == '_') :
				
					# Make the move
					board[i][j] = opponent

					# Call minimax recursively and choose
					# the minimum value
					best = min(best, minimax(board, depth + 1, not isMax))

					# Undo the move
					board[i][j] = '_'
		return best

# This will return the best possible move for the player
def search_for_best_move(board) :
	bestVal = -1000
	bestMove = (-1, -1)

	# check all of board
	for i in range(3) :	
		for j in range(3) :
		
			# Check if cell is empty
			if (board[i][j] == '_') :
			
				# Make the move
				board[i][j] = player

				# compute evaluation function for this
				# move.
				moveVal = minimax(board, 0, False)

				# Undo the move
				board[i][j] = '_'

				if (moveVal > bestVal) :			
					bestMove = (i, j)
					bestVal = moveVal

	return bestMove