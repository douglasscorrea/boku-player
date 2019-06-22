import copy
import node
import utils
import math

def minimax(curr_node, player):
	score_list = []

	score = utils.calculate_score(curr_node.get_board(), player)

	if score in [math.inf, -math.inf]:
		curr_node.set_score(score)
		print(curr_node.get_board())
		return score
	
	if curr_node.get_depth() == 2:
		print(curr_node.get_board())
		curr_node.set_score(score)
		return score

	moves = utils.get_available_moves(curr_node.get_board())

	if moves == []:
		print(curr_node.get_board())
		curr_node.set_score(score)
		return score

	for move in moves:
		new_board = utils.perform_move(copy.deepcopy(curr_node.get_board()), move, player)
		new_node = node.Node(curr_node, new_board, curr_node.get_depth() + 1, move)
		curr_node.add_lower(new_node)

		if player == 1:
			move_score = minimax(new_node, 2)
		else:
			move_score = minimax(new_node, 1)

		score_list.append(move_score)

	if(player == 1):
		score = max(score_list)
		curr_node.set_score(score)
	else:
		score = min(score_list)
		curr_node.set_score(score)

	return score