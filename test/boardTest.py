import unittest

from model.board import Board 

class BoardTest(unittest.TestCase):
    def test_board_x_position(self):
        myBoard = Board(4, 4)
        myBoard.x = 4
        expected = 4
        assert expected == myBoard.x

    def test_board_cell(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())


if __name__ == '__main__':
    unittest.main()
