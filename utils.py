import node
import numpy as np
import math 
import heuristics as h

def create_board():
	board = [	
		[0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0],		
	]

	board = np.array(board,dtype=object)
	return board


def get_available_moves(board):
	moves = []
	column_counter = 0

	for i in range(0, len(board)):
		for j in range(0, len(board[column_counter])):
			if board[i][j] == 0:
				moves.append([i, j])
		column_counter += 1

	return moves


def perform_move(board, move, player):
	board[int(move[0])][int(move[1])] = player

	return board


def calculate_score(board, player):
	if player == 1:
		return calculate_score_player1(board)
	else:
		return calculate_score_player2(board)


def calculate_score_player1(board):
	sequence = '11'
	sequence_enemy = '22'

	score = []
	score_enemy = []
	pieces_center = h.pieces_center(board, 1)
	pieces_center_enemy = h.pieces_center(board, 2)

	for _ in range(0, 6):
		score.append(verify_verticals(board, sequence) + pieces_center)
		score.append(verify_main_diagonals(board, sequence) + pieces_center)
		score.append(verify_secondary_diagonals(board, sequence) + pieces_center)
		score_enemy.append(verify_verticals(board, sequence_enemy) + pieces_center_enemy)
		score_enemy.append(verify_main_diagonals(board, sequence_enemy) + pieces_center_enemy)
		score_enemy.append(verify_secondary_diagonals(board, sequence_enemy) + pieces_center_enemy)
		sequence += '1'
		sequence_enemy += '2'

	if max(score_enemy) == math.inf:
		return -math.inf
	elif max(score) == math.inf:
		return math.inf

	return max(score) - max(score_enemy)


def calculate_score_player2(board): 
	sequence = '22'
	sequence_enemy = '11'
	score = []
	score_enemy = []

	pieces_center = h.pieces_center(board, 2)
	pieces_center_enemy = h.pieces_center(board, 1)
	for _ in range(0, 6):
		score.append(verify_verticals(board, sequence) + pieces_center)
		score.append(verify_main_diagonals(board, sequence) + pieces_center)
		score.append(verify_secondary_diagonals(board, sequence) + pieces_center)
		score_enemy.append(verify_verticals(board, sequence_enemy) + pieces_center_enemy)
		score_enemy.append(verify_main_diagonals(board, sequence_enemy) + pieces_center_enemy)
		score_enemy.append(verify_secondary_diagonals(board, sequence_enemy) + pieces_center_enemy)
		sequence += '2'
		sequence_enemy += '1'

	if max(score_enemy) == math.inf:
			return math.inf
	elif max(score) == math.inf:
		return -math.inf

	return max(score_enemy) - max(score)


def verify_main_diagonals(board, sequence):
	#print('main diagonals')
	main_diagonals = [
		[board[0][0], board[1][0], board[2][0], board[3][0], board[4][0], board[5][0]],
		[board[0][1], board[1][1], board[2][1], board[3][1], board[4][1], board[5][1], board[6][0]],
		[board[0][2], board[1][2], board[2][2], board[3][2], board[4][2], board[5][2], board[6][1], board[7][0]],
		[board[0][3], board[1][3], board[2][3], board[3][3], board[4][3], board[5][3], board[6][2], board[7][1], board[8][0]],
		[board[0][4], board[1][4], board[2][4], board[3][4], board[4][4], board[5][4], board[6][3], board[7][2], board[8][1], board[9][0]],
		[board[1][5], board[2][5], board[3][5], board[4][5], board[5][5], board[6][4], board[7][3], board[8][2], board[9][1], board[10][0]],
		[board[2][6], board[3][6], board[4][6], board[5][6], board[6][5], board[7][4], board[8][3], board[9][2], board[10][1]],
		[board[3][7], board[4][7], board[5][7], board[6][6], board[7][5], board[8][4], board[9][3], board[10][2]],
		[board[4][8], board[5][8], board[6][7], board[7][6], board[8][5], board[9][4], board[10][3]],
		[board[5][9], board[6][8], board[7][7], board[8][6], board[9][5], board[1][4]]
	]

	length = len(sequence)
	for row in main_diagonals:	
		if sequence in ''.join(str(i) for i in row):
			if length == 5:
				#print('5')
				return math.inf
			elif length == 4:
				#print('4')
				return 1350
			elif length == 3:
				#print('3')
				return 450
			elif length == 2:
				#print('2')
				return 150
	
	return 0


def verify_secondary_diagonals(board, sequence):
	secondary_diagonals = [
		[board[5][0], board[6][0], board[7][0], board[8][0], board[9][0], board[10][0]],
		[board[4][0], board[5][1], board[6][1], board[7][1], board[8][1], board[9][1], board[10][1]],
		[board[3][0], board[4][1], board[5][2], board[6][2], board[7][2], board[8][2], board[9][2], board[10][2]],
		[board[2][0], board[3][1], board[4][2], board[5][3], board[6][3], board[7][3], board[8][3], board[9][3], board[10][3]],
		[board[1][0], board[2][1], board[3][2], board[4][3], board[5][4], board[6][4], board[7][4], board[8][4], board[9][4], board[10][4]],
		[board[0][0], board[1][1], board[2][2], board[3][3], board[4][4], board[5][5], board[6][5], board[7][5], board[8][5], board[9][5]],
		[board[0][1], board[1][2], board[2][3], board[3][4], board[4][5], board[5][6], board[6][6], board[7][6], board[8][6]],
		[board[0][2], board[1][3], board[2][4], board[3][5], board[4][6], board[5][7], board[6][7], board[7][7]],
		[board[0][3], board[1][4], board[2][5], board[3][6], board[4][7], board[5][8], board[6][8]],
		[board[0][4], board[1][5], board[2][6], board[3][7], board[4][8], board[5][9]]
	]

	length = len(sequence)
	for row in secondary_diagonals:
		if sequence in ''.join(str(i) for i in row):
			if length == 5:
				return math.inf
			elif length == 4:
				return 1350
			elif length == 3:
				return 450
			elif length == 2:
				return 150
	
	return 0


def verify_verticals(board, sequence):
	verticals = [
		[board[0][0], board[0][1], board[0][2], board[0][3], board[0][4]],
		[board[1][0], board[1][1], board[1][2], board[1][3], board[1][4], board[1][5]],
		[board[2][0], board[2][1], board[2][2], board[2][3], board[2][4], board[2][5], board[2][6]],
		[board[3][0], board[3][1], board[3][2], board[3][3], board[3][4], board[3][5], board[3][6], board[3][7]],
		[board[4][0], board[4][1], board[4][2], board[4][3], board[4][4], board[4][5], board[4][6], board[4][7], board[4][8]],
		[board[5][0], board[5][1], board[5][2], board[5][3], board[5][4], board[5][5], board[5][6], board[5][7], board[5][8], board[5][9]],
		[board[6][0], board[6][1], board[6][2], board[6][3], board[6][4], board[6][5], board[6][6], board[6][7], board[6][8]],
		[board[7][0], board[7][1], board[7][2], board[7][3], board[7][4], board[7][5], board[7][6], board[7][7]],
		[board[8][0], board[8][1], board[8][2], board[8][3], board[8][4], board[8][5], board[8][6]],
		[board[9][0], board[9][1], board[9][2], board[9][3], board[9][4], board[9][5]],
		[board[10][0], board[10][1], board[10][2], board[10][3], board[10][4]]
	]
	
	length = len(sequence)
	for row in verticals:
		if sequence in ''.join(str(i) for i in row):
			if length == 5:
				return math.inf
			elif length == 4:
				return 1350
			elif length == 3:
				return 450
			elif length == 2:
				return 150
	
	return 0


def removal_piece(board, server_moves, player):
	if player == '1':
		for move in server_moves:
			if board[move[0]-1][move[1]-1] == 2:
				return move
	else:
		for move in server_moves:
			if board[move[0]-1][move[1]-1] == 1:
				return move
	
	return False


def forbidden_moves(board, server_moves):
	forbidden_moves = []
	moves = get_available_moves(board)

	for move in moves:
		if (move[0]+1, move[1]+1) not in server_moves:
			forbidden_moves.append([move[0]+1, move[1]+1])
	
	return forbidden_moves

def show_tree(nodes):
	while(len(nodes) > 0):
		node = nodes.pop(0)
		
		print(node.get_board())
		print(node.get_score())

		new_nodes = node.get_lowers()
		for lower in new_nodes:
			nodes.append(lower)