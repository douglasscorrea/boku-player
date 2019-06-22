import os
import sys
import copy
import node
import math
import utils
import minimax
import alpha_beta_pruning as abp


def game(player, board):
	# if player == 1:
	# 	root = node.Node(-1, board, 0, 2, 0)
	# 	score = minimax.minimax(copy.copy(root), 1)
	# else:
	# 	root = node.Node(-1, board, 0, 1, 0)
	# 	score = minimax.minimax(copy.copy(root), 2)

	if player == 1:
		root = node.Node(-1, board, 0, 2, 0)
		score = abp.alpha_beta_pruning(root, 1, -math.inf, math.inf)
	else:
		root = node.Node(-1, board, 0, 1, 0)
		score = abp.alpha_beta_pruning(root, 2, -math.inf, math.inf)

	lowers = root.get_lowers()
	best_score = lowers[0].get_score()
	move = lowers[0].get_move()

	for lower in lowers:
		if lower.get_score() == -math.inf:
			print("move: " + str(lower.get_move()))
		if player == 1:
			if(lower.get_score() > best_score):
				best_score = lower.get_score()
				move = lower.get_move()
		else:
			if(lower.get_score() < best_score):
				best_score = lower.get_score()
				move = lower.get_move()

	print('final score: ' + str(best_score))
	print('best move: ' + str(move))
	#utils.show_tree([root])
	return move