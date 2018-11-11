class Cell:
    NO_NEARBY_MINES = "~"
    FLAG = "$"
    INIT = " "

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.status = self.INIT

    def __str__(self):
        return str(self.status)

    def __repr__(self):
        return f"Cell: '{self.status}' @ ({self.x}, {self.y})"


class Grid:
    def __init__(self, size_x, size_y):
        self.size_x = size_x
        self.size_y = size_y

        # access with self.cells[Y][X]
        self.cells = []
        for y in range(self.size_y):
            cell_row = [Cell(x, y) for x in range(self.size_x)]
            self.cells.append(cell_row)

    def __str__(self):
        """
        print the minesweeper grid
        """

        lines = []

        horizontal_break = "+".join("-" for _ in range(self.size_x))
        horizontal_break = "+" + horizontal_break + "+"
        lines.append(horizontal_break)

        for row in self.cells:
            row_string = "|".join(str(cell) for cell in row)
            lines.append("|" + row_string + "|")
            lines.append(horizontal_break)

        return "\n".join(lines)
