import copy
import node
import utils
import math
import heuristics as h

def verify_heuristics(board, player):
	if player == '1':
		vw = verify_win_in_1(board, player)
		print('vw: ' + str(vw))
		if vw == None:
			vw = verify_lose_in_1(board, '2')
			print('vw2: ' + str(vw))
			if vw != None:
				return vw
		else:
			return vw
	else:
		vw = verify_win_in_1(board, player)
		print('vw: ' + str(vw))
		if vw == None:
			vw = verify_lose_in_1(board, '1')
			print('vw2: ' + str(vw))
			if vw != None:
				return vw
		else:
			return vw


	w2 = h.win_in_2_verticals(board, player)
	if w2 != False:
		print('verticals')
		return w2

	w2 = h.win_in_2_main_diagonals(board, player)
	if w2 != False:
		print('md')
		return w2

	w2 = h.win_in_2_secondary_diagonals(board, player)
	if w2 != False:
		print('sd')
		return w2
	
	return None

def verify_win_in_1(board, player):
	w1 = h.win_in_1_verticals(board, player)
	if w1 != False:
		print('1')
		return w1

	w1 = h.win_in_1_main_diagonals(board, player)
	if w1 != False:
		print('2')
		return w1

	w1 = h.win_in_1_secondary_diagonals(board, player)
	if w1 != False:
		print('3')
		return w1
	
	return None

def verify_lose_in_1(board, player):
	w1 = h.win_in_1_verticals(board, player)
	if w1 != False:
		print('1')
		return w1

	w1 = h.win_in_1_main_diagonals(board, player)
	if w1 != False:
		print('2')
		return w1

	w1 = h.win_in_1_secondary_diagonals(board, player)
	if w1 != False:
		print('3')
		return w1
	
	return None