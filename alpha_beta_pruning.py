import copy
import node
import utils
import math
import heuristics as h

def alpha_beta_pruning(curr_node, player, abp_class, forbidden_moves):
	alpha = abp_class.get_alpha()
	beta = abp_class.get_beta()
	score = utils.calculate_score(curr_node.get_board(), player)

	if score in [math.inf, -math.inf]:
		curr_node.set_score(score)
		return score
	
	if curr_node.get_depth() == 2:
		curr_node.set_score(score)
		return score

	moves = utils.get_available_moves(curr_node.get_board())
	for move in moves:
		if [move[0]+1, move[1]+1] in forbidden_moves:
			moves.remove(move)
		
	if moves == []:
		curr_node.set_score(score)
		return score

	if len(moves) in [80, 79]:
		if [5, 4] in moves:
			curr_node.set_score(score)
			curr_node.set_move([5, 4])
			return score
		elif [5, 5] in moves:
			curr_node.set_score(score)
			curr_node.set_move([5, 5])
			return score
		elif [4, 3] in moves:
			curr_node.set_score(score)
			curr_node.set_move([4, 3])
			return score
		elif [6, 3] in moves:
			curr_node.set_score(score)
			curr_node.set_move([6, 3])
			return score

	if player == 1:
		best_score = -math.inf

		for move in moves:
			new_board = utils.perform_move(copy.deepcopy(curr_node.get_board()), move, player)
			new_node = node.Node(curr_node, new_board, curr_node.get_depth() + 1, move)
			curr_node.add_lower(new_node)
		
			move_score = alpha_beta_pruning(new_node, 2, abp_class, forbidden_moves)

			best_score = max(best_score, move_score)
			abp_class.set_alpha(max(alpha, best_score))
			if abp_class.get_alpha() >= beta:
				break

		curr_node.set_score(best_score)
		return best_score
	else:
		best_score = math.inf

		for move in moves:
			new_board = utils.perform_move(copy.deepcopy(curr_node.get_board()), move, player)
			new_node = node.Node(curr_node, new_board, curr_node.get_depth() + 1, move)
			curr_node.add_lower(new_node)

			move_score = alpha_beta_pruning(new_node, 1, abp_class, forbidden_moves)

			best_score = min(best_score, move_score)
			abp_class.set_beta(min(beta, best_score))
			if alpha >= abp_class.get_beta():
				break

		curr_node.set_score(best_score)
		return best_score

	