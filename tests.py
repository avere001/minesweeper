import io
import sys
import unittest
from main import Grid, Cell


class TestGridPrinting(unittest.TestCase):
    def test_grid_print_1_1(self):
        grid = Grid(1, 1)

        self.assertEqual(str(grid), "\n".join(["+-+", "| |", "+-+"]))

        grid.cells[0][0].status = Cell.FLAG
        self.assertEqual(str(grid), "\n".join(["+-+", "|$|", "+-+"]))

    def test_grid_print_3_3(self):
        grid = Grid(3, 3)

        grid.cells[2][1].status = Cell.FLAG
        self.assertEqual(
            str(grid),
            "\n".join(
                [
                    "+-+-+-+",
                    "| | | |",
                    "+-+-+-+",
                    "| | | |",
                    "+-+-+-+",
                    "| |$| |",
                    "+-+-+-+",
                ]
            ),
        )
