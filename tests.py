import io
import sys
import unittest
from grid import Grid, Cell


class TestGridPrinting(unittest.TestCase):
    def test_grid_print_1_1(self):
        grid = Grid(1, 1, 0)
        self.assertEqual(str(grid), "\n".join(["+-+", "|?|", "+-+"]))

    def test_grid_print_3_3(self):
        grid = Grid(3, 3, 0)

        grid.cells[2][1].reveal(0)
        self.assertEqual(
            str(grid),
            "\n".join(
                [
                    "+-+-+-+",
                    "|?|?|?|",
                    "+-+-+-+",
                    "|?|?|?|",
                    "+-+-+-+",
                    "|?| |?|",
                    "+-+-+-+",
                ]
            ),
        )
