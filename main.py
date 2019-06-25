import sys
import minimax
import game
import utils
import heuristics as h
import verify_heuristics as vh


def main(board):
	# board = [
	# 	[0, 0, 0, 0, 0], 
	# 	[0, 0, 0, 0, 0, 0], 
	# 	[0, 1, 0, 0, 0, 0, 0], 
	# 	[0, 0, 0, 0, 0, 0, 0, 0], 
	# 	[0, 0, 0, 1, 2, 0, 0, 0, 0], 
	# 	[0, 0, 0, 0, 1, 2, 0, 0, 0, 0], 
	# 	[0, 0, 0, 0, 0, 0, 0, 0, 0], 
	# 	[0, 0, 0, 0, 0, 0, 0, 0], 
	# 	[0, 0, 0, 0, 0, 0, 0], 
	# 	[0, 0, 0, 0, 0, 0], 
	# 	[0, 0, 0, 0, 0]
	# ]

	# board = [
	# 	[0, 0, 0, 0, 0], #0
	# 	[1, 0, 0, 0, 0, 0], #1
	# 	[1, 0, 0, 1, 1, 1, 0], #2
	# 	[1, 0, 0, 0, 0, 0, 0, 0], #3
	# 	[0, 0, 0, 0, 0, 0, 0, 0, 0], #4
	# 	[1, 2, 2, 0, 0, 0, 0, 0, 0, 0], #5
	# 	[1, 0, 0, 0, 0, 0, 0, 0, 0], #6
	# 	[1, 0, 0, 0, 0, 0, 0, 0], #7
	# 	[0, 0, 0, 0, 0, 0, 0], #8
	# 	[0, 0, 0, 0, 0, 0], #9
	# 	[0, 0, 0, 0, 0] #10
	# ]
	# string = ''
	# row = [board[0][0], board[0][1], board[0][2], board[0][3], board[0][4]]
	# string = ''.join(str(i) for i in row)
	# print(string.index('1'))
	#print('move: ' + str(h.win_in_2_secondary_diagonals(board)))
	
	heuristics = vh.verify_heuristics(board, sys.argv[1])
	#heuristics = None
	if heuristics == None:
		return game.game(sys.argv[1], board)
	else:
		print('best move: ' + str(heuristics))
		return heuristics

if __name__ == "__main__":
	main(sys.argv)