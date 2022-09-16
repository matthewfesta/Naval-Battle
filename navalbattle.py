"""
This module creates a naval game to be played by a single player in the command
line / console similar to the game Battleship.

Author: Matthew Festa

"""

import random

"""
    -------NAVAL BATTLE-------

    How it will work:
    1. A 10x10 grid will have 5 ships randomly placed about
    2. You can choose a row and column to indicate where to shoot
    3. For every shot that hits or misses it will show up in the grid
    4. If all ships are shot, game over

    Legend:
    1. "." = water
    2. "S" = ship position
    3. "O" = a miss
    4. "X" = a hit 
"""

# Global variable for grid size
grid_size = 10
# Global variable for grid
user_grid = [[''] * grid_size for i in range(grid_size)]
computer_grid = [[''] * grid_size for i in range(grid_size)]
# Global variable for number of ships to place
num_of_ships = 5


def draw_board(my_board):
	"""
	This function prints the game board that has already been set up.
	:param my_board:
	:return: Void
	"""
	print("+---" * 11 + "+")
	print("|   | ", end="")
	for col in range(len(my_board)):
		print(str(col), end=" | ")
	print()
	for row in range(len(my_board)):
		print("+---" * 11 + "+")
		print("| " + str(row) + " |", end="")
		for col in range(len(my_board)):
			print(my_board[row][col] + '|', end="")
		print()
	print("+---" * 11 + "+")


def setup_board(my_board):
	"""
	This function sets up the 2D board and fills each of the matrices with
	'.' if empty space and 'S' if there is a ship.
	:param my_board:
	:return: my_board 2D list object
	"""

	# Initialize all grid[row][col] = '.'
	for row in range(grid_size):
		for col in range(grid_size):
			my_board[row][col] = ' . '

	# Place the ships
	for i in range(num_of_ships):
		randomRow = random.randint(0, grid_size - 1)
		randomCol = random.randint(0, grid_size - 1)
		my_board[randomRow][randomCol] = ' S '
	return my_board


def hit_or_miss(my_board, row, col):
	"""
	The hit or miss takes the values inputted by the user as parameters for
	the location of the ship and checks if it is a hit or miss.
	:param my_board:
	:param row:
	:param col:
	:return: check - HIT if is ship, MISS if is empty
	"""
	space = my_board[row][col]
	if space == ' S ' or space == ' X ':
		my_board[row][col] = ' X '
		check = 'HIT'
		draw_board(my_board)
		return check
	else:
		my_board[row][col] = ' O '
		check = 'MISSED'
		draw_board(my_board)
		return check


def hit_or_miss_computer(my_board, row, col):
	"""
	The hit or miss takes the values inputted by the computer as parameters for
	the location of the ship and checks if it is a hit or miss.
	:param my_board:
	:param row:
	:param col:
	:return: check - HIT if is ship, MISS if is empty
	"""
	space = my_board[row][col]
	if space == ' S ' or space == ' X ':
		my_board[row][col] = ' X '
		check = 'HIT'
		return check
	else:
		my_board[row][col] = ' O '
		check = 'MISSED'
		return check


def is_game_over(my_board):
	"""
	This function returns a boolean value to check if the prerequisites of
	ending the game are met.
	:param my_board:
	:return: True if all ships are sunk, False if ships remain
	"""
	for row in range(grid_size):
		for column in range(grid_size):
			if my_board[row][column] == ' S ':
				return False
	return True


def main(user_board, computer_board):
	"""
	This function defines how the code in the main function will execute.
	:param user_board, computer_board:
	:return:
	"""
	round = 1
	user_name = input('Enter Name: \n')
	try:
		user_name = str(user_name)
	except:
		print('Invalid name')
	print(f'Hello {user_name}! Welcome to the game!')
	print(f'**** Drawing Boards ~ Round {round} ****')
	setup_board(user_board)
	setup_board(computer_board)
	print(f'{user_name}\'s board:')
	draw_board(user_board)
	print('Legend:')
	print('1. . = water \n'
	      '2. S = ship position \n'
	      '3. O = a miss \n'
	      '4. X = a hit')
	while not is_game_over(user_board):
		row = input('Enter a row (X): \n')
		try:
			row = int(row)
			if int(row) < 0 or int(row) >= 10:
				raise ValueError('Invalid row')
		except ValueError as e:
			print(e)
			continue
		col = input('Enter a column (Y): \n')
		try:
			col = int(col)
			if int(col) < 0 or int(col) >= 10:
				raise ValueError('Invalid column')
		except ValueError as e:
			print(e)
			continue
		else:
			# Computer's random row and column
			comp_row = random.randint(0, grid_size - 1)
			comp_col = random.randint(0, grid_size - 1)
			# Check each board for hit or miss
			check_user = hit_or_miss_computer(computer_board, row, col)
			check_computer = hit_or_miss(user_board, comp_row,
			                             comp_col)
			# Print out
			print(f'Your torpedo {check_user} one of the computer\'s ships!')
			print(f'The computer\'s torpedo {check_computer} one'
			      f' of {user_name}\'s ships')
			# Check if game is over
			is_game_over(user_board)
			is_game_over(computer_board)
			# If over, print out Game over
			if is_game_over(user_board):
				print('Game over! Computer wins!')
				print(f'{user_name}\'s final board:')
				draw_board(user_board)
				print('Computer\'s final board:')
				draw_board(computer_board)
				break
			elif is_game_over(computer_board):
				print(f'Game over! {user_name} wins!')
				print(f'{user_name}\'s final board:')
				draw_board(user_board)
				print('Computer\'s final board:')
				draw_board(computer_board)
				break
			else:
				round += 1
				print(f'Round: {round}')
	# Ask if you want to play again
	yes_no = input('Do you want to play again Y / N ?')
	try:
		yes_no = yes_no.upper()
	except:
		print('Something went wrong')
	else:
		if yes_no == 'Y':
			main(user_board, computer_board)
		elif yes_no == 'N':
			quit()
		else:
			print('Something went wrong.')


if __name__ == '__main__':
	main(user_grid, computer_grid)
