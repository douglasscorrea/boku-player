import copy
import node
import utils
import math
import math

def alpha_beta_pruning(curr_node, player, alpha, beta):
	score = utils.calculate_score(curr_node.get_board(), player)
	
	if score in [math.inf, -math.inf]:
		curr_node.set_score(score)
		return score
	
	if curr_node.get_depth() == 3:
		curr_node.set_score(score)
		return score

	moves = utils.get_available_moves(curr_node.get_board())

	if moves == []:
		curr_node.set_score(score)
		return score

	if player == 1:
		best_score = -math.inf

		for move in moves:
			new_board = utils.perform_move(copy.deepcopy(curr_node.get_board()), move, player)
			new_node = node.Node(curr_node, new_board, curr_node.get_depth() + 1, move)
			curr_node.add_lower(new_node)
		
			move_score = alpha_beta_pruning(new_node, 2, alpha, beta)
			best_score = max(best_score, move_score)
			alpha = max(alpha, best_score)
			if alpha >= beta:
				break

		curr_node.set_score(move_score)
		return move_score
	else:
		best_score = math.inf

		for move in moves:
			new_board = utils.perform_move(copy.deepcopy(curr_node.get_board()), move, player)
			new_node = node.Node(curr_node, new_board, curr_node.get_depth() + 1, move)
			curr_node.add_lower(new_node)

			move_score = alpha_beta_pruning(new_node, 1, alpha, beta)
			best_score = min(best_score, move_score)
			beta = min(beta, best_score)
			if alpha >= beta:
				break

		curr_node.set_score(move_score)
		return move_score

	