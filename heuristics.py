import copy
import node
import utils
import math

def pieces_center(board, player):
	return [
			board[3][2], board[3][3], board[3][4],
			board[4][2], board[4][3], board[4][4], board[4][5],
			board[5][2], board[5][3], board[5][4], board[5][5], board[5][6],
			board[6][2], board[6][3], board[6][4], board[6][5],
			board[7][2], board[7][3], board[7][4]
		].count(player)

def win_in_2_verticals(board, player):
	i = 0
	if player == '1':
		enemy = '2'
	else:
		enemy = '1'
	sequence = enemy + enemy + enemy
	
	verticals_index = [
		[[0, 0], [0, 1], [0, 2], [0, 3], [0, 4]],
		[[1, 0], [1, 1], [1, 2], [1, 3], [1, 4], [1, 5]],
		[[2, 0], [2, 1], [2, 2], [2, 3], [2, 4], [2, 5], [2, 6]],
		[[3, 0], [3, 1], [3, 2], [3, 3], [3, 4], [3, 5], [3, 6], [3, 7]],
		[[4, 0], [4, 1], [4, 2], [4, 3], [4, 4], [4, 5], [4, 6], [4, 7], [4, 8]],
		[[5, 0], [5, 1], [5, 2], [5, 3], [5, 4], [5, 5], [5, 6], [5, 7], [5, 8], [5, 9]],
		[[6, 0], [6, 1], [6, 2], [6, 3], [6, 4], [6, 5], [6, 6], [6, 7], [6, 8]],
		[[7, 0], [7, 1], [7, 2], [7, 3], [7, 4], [7, 5], [7, 6], [7, 7]],
		[[8, 0], [8, 1], [8, 2], [8, 3], [8, 4], [8, 5], [8, 6]],
		[[9, 0], [9, 1], [9, 2], [9, 3], [9, 4], [9, 5]],
		[[10, 0], [10, 1], [10, 2], [10, 3], [10, 4]]
	]

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
	
	for row in verticals:
		string = ''.join(str(i) for i in row)
		if sequence in string:
			positions = [pos for pos, char in enumerate(string) if char == '0']

			if (string.index(enemy) - 1) in positions:
				return verticals_index[i][string.index(enemy) - 1]
			if (string.index(enemy) + 3) in positions and (string.index(enemy) - 1) in positions: 
				return verticals_index[i][string.index(enemy) + 3]
			# else:
			# 	return False
		i += 1

	return False

def win_in_2_main_diagonals(board, player):
	i = 0
	if player == '1':
		enemy = '2'
	else:
		enemy = '1'
	sequence = enemy + enemy + enemy
	positions = []

	main_diagonals_index = [
		[[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0]],
		[[0, 1], [1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 0]],
		[[0, 2], [1, 2], [2, 2], [3, 2], [4, 2], [5, 2], [6, 1], [7, 0]],
		[[0, 3], [1, 3], [2, 3], [3, 3], [4, 3], [5, 3], [6, 2], [7, 1], [8, 0]],
		[[0, 4], [1, 4], [2, 4], [3, 4], [4, 4], [5, 4], [6, 3], [7, 2], [8, 1], [9, 0]],
		[[1, 5], [2, 5], [3, 5], [4, 5], [5, 5], [6, 4], [7, 3], [8, 2], [9, 1], [10, 0]],
		[[2, 6], [3, 6], [4, 6], [5, 6], [6, 5], [7, 4], [8, 3], [9, 2], [10, 1]],
		[[3, 7], [4, 7], [5, 7], [6, 6], [7, 5], [8, 4], [9, 3], [10, 2]],
		[[4, 8], [5, 8], [6, 7], [7, 6], [8, 5], [9, 4], [10, 3]],
		[[5, 9], [6, 8], [7, 7], [8, 6], [9, 5], [1, 4]]
	]


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

	
	for row in main_diagonals:
		string = ''.join(str(i) for i in row)
		if sequence in string:
			positions = [pos for pos, char in enumerate(string) if char == '0']

			if (string.index(enemy) - 1) in positions:
				return main_diagonals_index[i][string.index(enemy) - 1]
			if (string.index(enemy) + 3) in positions and (string.index(enemy) - 1) in positions:
				return main_diagonals_index[i][string.index(enemy) + 3]
			# else:
			# 	return False
		i += 1

	return False

def win_in_2_secondary_diagonals(board, player):
	i = 0
	if player == '1':
		enemy = '2'
	else:
		enemy = '1'
	sequence = enemy + enemy + enemy
	positions = []

	secondary_diagonals_index = [
		[[5, 0], [6, 0], [7, 0], [8, 0], [9, 0], [10, 0]],
		[[4, 0], [5, 1], [6, 1], [7, 1], [8, 1], [9, 1], [10, 1]],
		[[3, 0], [4, 1], [5, 2], [6, 2], [7, 2], [8, 2], [9, 2], [10, 2]],
		[[2, 0], [3, 1], [4, 2], [5, 3], [6, 3], [7, 3], [8, 3], [9, 3], [10, 3]],
		[[1, 0], [2, 1], [3, 2], [4, 3], [5, 4], [6, 4], [7, 4], [8, 4], [9, 4], [10, 4]],
		[[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 5], [7, 5], [8, 5], [9, 5]],
		[[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 6], [7, 6], [8, 6]],
		[[0, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 7], [7, 7]],
		[[0, 3], [1, 4], [2, 5], [3, 6], [4, 7], [5, 8], [6, 8]],
		[[0, 4], [1, 5], [2, 6], [3, 7], [4, 8], [5, 9]]
	]


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

	
	for row in secondary_diagonals:
		string = ''.join(str(i) for i in row)
		if sequence in string:
			positions = [pos for pos, char in enumerate(string) if char == '0']

			if (string.index(enemy) - 1) in positions:
				return secondary_diagonals_index[i][string.index(enemy) - 1]
			if (string.index(enemy) + 3) in positions and (string.index(enemy) - 1) in positions:
				return secondary_diagonals_index[i][string.index(enemy) + 3]
			# else:
			# 	return False
		i += 1

	return False


def win_in_1_verticals(board, player):
	i = 0
	sequence = player + player + player + player
	positions = []

	verticals_index = [
		[[0, 0], [0, 1], [0, 2], [0, 3], [0, 4]],
		[[1, 0], [1, 1], [1, 2], [1, 3], [1, 4], [1, 5]],
		[[2, 0], [2, 1], [2, 2], [2, 3], [2, 4], [2, 5], [2, 6]],
		[[3, 0], [3, 1], [3, 2], [3, 3], [3, 4], [3, 5], [3, 6], [3, 7]],
		[[4, 0], [4, 1], [4, 2], [4, 3], [4, 4], [4, 5], [4, 6], [4, 7], [4, 8]],
		[[5, 0], [5, 1], [5, 2], [5, 3], [5, 4], [5, 5], [5, 6], [5, 7], [5, 8], [5, 9]],
		[[6, 0], [6, 1], [6, 2], [6, 3], [6, 4], [6, 5], [6, 6], [6, 7], [6, 8]],
		[[7, 0], [7, 1], [7, 2], [7, 3], [7, 4], [7, 5], [7, 6], [7, 7]],
		[[8, 0], [8, 1], [8, 2], [8, 3], [8, 4], [8, 5], [8, 6]],
		[[9, 0], [9, 1], [9, 2], [9, 3], [9, 4], [9, 5]],
		[[10, 0], [10, 1], [10, 2], [10, 3], [10, 4]]
	]

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
	
	for row in verticals:
		string = ''.join(str(i) for i in row)
		if sequence in string:
			positions = [pos for pos, char in enumerate(string) if char == '0']

			if (string.index(player) - 1) in positions:
				return verticals_index[i][string.index(player) - 1]
			if (string.index(player) + 4) in positions:
				return verticals_index[i][string.index(player) + 4]
			else:
				return False
		i += 1

	return False

def win_in_1_main_diagonals(board, player):
	i = 0
	sequence = player + player + player + player

	main_diagonals_index = [
		[[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0]],
		[[0, 1], [1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 0]],
		[[0, 2], [1, 2], [2, 2], [3, 2], [4, 2], [5, 2], [6, 1], [7, 0]],
		[[0, 3], [1, 3], [2, 3], [3, 3], [4, 3], [5, 3], [6, 2], [7, 1], [8, 0]],
		[[0, 4], [1, 4], [2, 4], [3, 4], [4, 4], [5, 4], [6, 3], [7, 2], [8, 1], [9, 0]],
		[[1, 5], [2, 5], [3, 5], [4, 5], [5, 5], [6, 4], [7, 3], [8, 2], [9, 1], [10, 0]],
		[[2, 6], [3, 6], [4, 6], [5, 6], [6, 5], [7, 4], [8, 3], [9, 2], [10, 1]],
		[[3, 7], [4, 7], [5, 7], [6, 6], [7, 5], [8, 4], [9, 3], [10, 2]],
		[[4, 8], [5, 8], [6, 7], [7, 6], [8, 5], [9, 4], [10, 3]],
		[[5, 9], [6, 8], [7, 7], [8, 6], [9, 5], [1, 4]]
	]


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

	
	for row in main_diagonals:
		string = ''.join(str(i) for i in row)
		if sequence in string:
			positions = [pos for pos, char in enumerate(string) if char == '0']

			if (string.index(player) - 1) in positions:
				return main_diagonals_index[i][string.index(player) - 1]
			if (string.index(player) + 4) in positions:
				return main_diagonals_index[i][string.index(player) + 4]
			else:
				return False
		i += 1

	return False

def win_in_1_secondary_diagonals(board, player):
	i = 0
	sequence = player + player + player + player

	secondary_diagonals_index = [
		[[5, 0], [6, 0], [7, 0], [8, 0], [9, 0], [10, 0]],
		[[4, 0], [5, 1], [6, 1], [7, 1], [8, 1], [9, 1], [10, 1]],
		[[3, 0], [4, 1], [5, 2], [6, 2], [7, 2], [8, 2], [9, 2], [10, 2]],
		[[2, 0], [3, 1], [4, 2], [5, 3], [6, 3], [7, 3], [8, 3], [9, 3], [10, 3]],
		[[1, 0], [2, 1], [3, 2], [4, 3], [5, 4], [6, 4], [7, 4], [8, 4], [9, 4], [10, 4]],
		[[0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 5], [7, 5], [8, 5], [9, 5]],
		[[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 6], [7, 6], [8, 6]],
		[[0, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7], [6, 7], [7, 7]],
		[[0, 3], [1, 4], [2, 5], [3, 6], [4, 7], [5, 8], [6, 8]],
		[[0, 4], [1, 5], [2, 6], [3, 7], [4, 8], [5, 9]]
	]


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

	
	for row in secondary_diagonals:
		string = ''.join(str(i) for i in row)
		if sequence in string:
			positions = [pos for pos, char in enumerate(string) if char == '0']

			if (string.index(player) - 1) in positions:
				return secondary_diagonals_index[i][string.index(player) - 1]
			if (string.index(player) + 4) in positions:
				return secondary_diagonals_index[i][string.index(player) + 4]
			else:
				return False
		i += 1

	return False



