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
	
	heuristics = vh.verify_heuristics(board, sys.argv[1])
	#heuristics = None

	if heuristics == None:
		return game.game(sys.argv[1], board, server_moves)
	elif (heuristics[0]+1, heuristics[1]+1) not in server_moves:
		return game.game(sys.argv[1], board, server_moves)
	else:
		print('best move: ' + str(heuristics))
		return heuristics

if __name__ == "__main__":
	main(sys.argv, [])