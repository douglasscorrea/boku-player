import sys
import minimax
import game
import utils
import heuristics as h
import verify_heuristics as vh


def main(board, server_moves):
	# board = [
	# 	[0, 0, 0, 0, 0], 
	# 	[0, 0, 0, 0, 0, 0], 
	# 	[0, 1, 0, 0, 0, 0, 0], 
	# 	[0, 0, 0, 0, 0, 0, 0, 0], 
	# 	[0, 0, 0, 1, 2, 0, 0, 0, 0], 
	# 	[0, 0, 0, 0, 1, 2, 0, 0, 0, 0], 
	# 	[1, 0, 0, 0, 0, 0, 0, 0, 0], 
	# 	[1, 0, 0, 0, 0, 0, 0, 0], 
	# 	[1, 0, 0, 0, 0, 0, 0], 
	# 	[0, 0, 0, 0, 0, 0], 
	# 	[0, 0, 0, 0, 0]
	# ]

	#board = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 2, 2, 2, 0, 0, 0], [0, 0, 1, 1, 2, 0, 0, 0], [0, 0, 1, 1, 2, 2, 1, 0, 0], [0, 0, 1, 1, 1, 2, 2, 0, 0, 0], [0, 0, 1, 0, 1, 2, 0, 0, 0], [0, 0, 0, 0, 2, 1, 0, 0], [0, 0, 0, 2, 0, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0]]

	#print(h.win_in_2_secondary_diagonals(board, 1))
	# string = ''
	# row = [board[0][0], board[0][1], board[0][2], board[0][3], board[0][4]]
	# string = ''.join(str(i) for i in row)
	# print(string.index('1'))
	#print('score: ' + str(utils.calculate_score(board, 1)))
	#return 
	heuristics = vh.verify_heuristics(board, sys.argv[1])
	#heuristics = None
	print('heuristics: ' + str(heuristics))

	if heuristics == None:
		return game.game(sys.argv[1], board, server_moves)
	elif (heuristics[0]+1, heuristics[1]+1) not in server_moves:
		return game.game(sys.argv[1], board, server_moves)
	else:
		print('best move: ' + str(heuristics))
		return heuristics

if __name__ == "__main__":
	main(sys.argv)