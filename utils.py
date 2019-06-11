import node
import numpy as np


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
			if board[i][j] == 1:
				moves.append([i, j])
		column_counter += 1

	return moves


def perform_move(board, move, player):
	board[int(move[0])][int(move[1])] = player

	return board


def calculate_score(board, player):
	win_states = [
		[board[0][0], board[0][1], board[0][2]],
		[board[1][0], board[1][1], board[1][2]],
		[board[2][0], board[2][1], board[2][2]],
		[board[0][0], board[1][0], board[2][0]],
		[board[0][1], board[1][1], board[2][1]],
		[board[0][2], board[1][2], board[2][2]],
		[board[0][0], board[1][1], board[2][2]],
		[board[2][0], board[1][1], board[0][2]],
	]
	
	if [player, player, player] in win_states:
		return player
	elif (len(get_available_moves(board)) == 0):
		return 0
	else:
		return -2

def verify_end_game(board, player):
	win_states = [
		[board[0][0], board[0][1], board[0][2]],
		[board[1][0], board[1][1], board[1][2]],
		[board[2][0], board[2][1], board[2][2]],
		[board[0][0], board[1][0], board[2][0]],
		[board[0][1], board[1][1], board[2][1]],
		[board[0][2], board[1][2], board[2][2]],
		[board[0][0], board[1][1], board[2][2]],
		[board[2][0], board[1][1], board[0][2]],
	]

	if [player, player, player] in win_states:
		return player
	elif [-1*player, -1*player, -1*player] in win_states:
		return -1*player
	elif any(0 in i for i in win_states):
		return -2
	else:
		return 0