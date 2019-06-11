import copy
import node
import utils


def minimax(curr_node, player):
	score_list = []
	id = curr_node.get_id()

	score = utils.calculate_score(curr_node.get_board(), player)
	moves = utils.get_available_moves(curr_node.get_board())

	if (score in [-1, 0, 1]):
		curr_node.set_score(score)
		return score

	for move in moves:
		id += 1
		new_board = utils.perform_move(copy.copy(curr_node.get_board()), move, player)
		new_node = node.Node(curr_node, new_board, curr_node.get_depth() + 1, player, move, id)
		curr_node.add_lower(new_node)

		move_score = minimax(new_node, -1*player)

		score_list.append(move_score)
		
	if(player == 1):	# MAXIMIZING
		score = max(score_list)
		curr_node.set_score(score)
	else:	# MINIMIZING
		score = min(score_list)
		curr_node.set_score(score)

	return score