import unittest

from model import cell

class CellTest(unittest.TestCase):
    def test_cell_has_x_position(self):
        a = False;
        myCell = Cell(3,3)
        if myCell.x > 0:
            a = True
        self.assertEqual(True, a)

    def test_cell_has_y_position(self):
        a = False
        myCell = Cell(3, 3)
        if myCell.y > 0:
            a = True
        self.assertEqual(True, a)


if __name__ == '__main__':
    unittest.main()
