"""
This module tests a naval game to be played by a single player in the command
line / console similar to the game Battleship.

"""


import unittest
import navalbattle


class TestNavalBattle(unittest.TestCase):
	def test_setup_board_ships(self):
		test_ships = 0
		test_board = Battleship.setup_board(Battleship.grid)
		for row in range(len(test_board)):
			for column in range(len(test_board)):
				if test_board[row][column] == ' S ':
					test_ships += 1
				else:
					continue
		self.assertEqual(test_ships, 5)

	def test_setup_board_empty_space(self):
		test_empty = 0
		test_board = Battleship.setup_board(Battleship.grid)
		for row in range(len(test_board)):
			for column in range(len(test_board)):
				if test_board[row][column] == ' . ':
					test_empty += 1
				else:
					continue
		self.assertEqual(test_empty, 95)

	def test_hit(self):
		test_hit = ""
		test_board = Battleship.setup_board(Battleship.grid)
		for row in range(len(test_board)):
			for column in range(len(test_board)):
				if test_board[row][column] == ' S ':
					test_hit = Battleship.hit_or_miss(test_board, row, column)
				else:
					continue
		self.assertEqual(test_hit, 'HIT!')

	def test_miss(self):
		test_miss = ""
		test_board = Battleship.setup_board(Battleship.grid)
		for row in range(len(test_board)):
			for column in range(len(test_board)):
				if test_board[row][column] == ' . ':
					test_miss = Battleship.hit_or_miss(test_board, row, column)
				else:
					continue
		self.assertEqual(test_miss, 'MISS!')

	def test_is_game_over_true(self):
		test_board = Battleship.setup_board(Battleship.grid)
		for row in range(len(test_board)):
			for column in range(len(test_board)):
				if test_board[row][column] == ' S ':
					test_board[row][column] = ' X '
				else:
					continue
		result = Battleship.is_game_over(test_board)
		self.assertEqual(result, True)

	def test_is_game_over_false(self):
		test_board = Battleship.setup_board(Battleship.grid)
		result = Battleship.is_game_over(test_board)
		self.assertEqual(result, False)


if __name__ == '__main__':
	unittest.main()
