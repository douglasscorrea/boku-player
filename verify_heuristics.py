import copy
import node
import utils
import math
import heuristics as h

def verify_heuristics(board, player):
	w2 = h.win_in_2_verticals(board, player)
	if w2 != False:
		return w2

	w2 = h.win_in_2_main_diagonals(board, player)
	if w2 != False:
		return w2

	w2 = h.win_in_2_secondary_diagonals(board, player)
	if w2 != False:
		return w2
	
	return None