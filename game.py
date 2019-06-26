import os
import sys
import copy
import node
import math
import utils
import minimax
import alpha_beta_pruning as abp
import ABP

def game(player, board, server_moves):
	# minimax
	# if player == 1:
	# 	root = node.Node(-1, board, 0, 2, 0)
	# 	score = minimax.minimax(copy.copy(root), 1)
	# else:
	# 	root = node.Node(-1, board, 0, 1, 0)
	# 	score = minimax.minimax(copy.copy(root), 2)

	# alpha-beta pruning

	abp_class = ABP.ABP()

	removal_move = utils.removal_piece(board, server_moves, player)
	forbidden_moves = utils.forbidden_moves(board, server_moves)
	if removal_move:
		return [removal_move[0]-1, removal_move[1]-1]

	if player == '1':
		root = node.Node(-1, board, 0, 0)
		score = abp.alpha_beta_pruning(root, 1, abp_class, forbidden_moves)
	else:
		root = node.Node(-1, board, 0, 0)
		score = abp.alpha_beta_pruning(root, 2, abp_class, forbidden_moves)

	lowers = root.get_lowers()
	if (len(lowers) > 0):
		best_score = lowers[0].get_score()
		#print('beta: ' + str(abp_class.get_beta()))
		move = lowers[0].get_move()
		#print('move: ' + str(move))

		for lower in lowers:
			#print('score lower: ' + str(lower.get_score()))
			if player == '1':
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
	else:
		print('best move: ' + str(root.get_move()))
		return root.get_move()