import itertools
from random import sample


class Cell:
    EMPTY = " "
    NOT_REVEALED = "?"

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self._display_character = self.NOT_REVEALED
        self._is_revealed = False
        self.is_mine = False
        self.siblings = []

    @property
    def is_revealed(self):
        return self._is_revealed

    def reveal(self):
        if self._is_revealed:
            return

        self._is_revealed = True

        if len(self.nearby_mines) == 0:
            self._display_character = " "
            for sibling in self.siblings:
                sibling.reveal()
        else:
            self._display_character = str(len(self.nearby_mines))

    @property
    def nearby_mines(self):
        return [x for x in self.siblings if x.is_mine]

    def populate_siblings(self, grid):
        """populate this cells list of siblings"""
        for dx, dy in itertools.product((-1, 0, 1), repeat=2):
            try:
                if dx == dy == 0:
                    # I am not my own sibling.
                    continue

                sibling = grid.cells[self.y + dy][self.x + dx]
                # we need this check because of negative indexing
                if sibling.x - dx == self.x and sibling.y - dy == self.y:
                    self.siblings.append(sibling)
            except IndexError:
                pass

    def __str__(self):
        return str(self._display_character)

    def __repr__(self):
        return f"Cell: '{self._display_character}' @ ({self.x}, {self.y})"


class Grid:
    def __init__(self, size_x, size_y, num_mines):

        assert size_x > 0
        assert size_y > 0
        assert num_mines < size_x * size_y

        self.num_mines = num_mines
        self.size_x = size_x
        self.size_y = size_y

        # access with self.cells[Y][X]
        self.cells = []
        for y in range(self.size_y):
            cell_row = [Cell(x, y) for x in range(self.size_x)]
            self.cells.append(cell_row)

        for y, cell_row in enumerate(self.cells):
            for x, cell in enumerate(cell_row):
                cell.populate_siblings(self)

        flattened_cells = list(itertools.chain.from_iterable(self.cells))

        mines = sample(flattened_cells, self.num_mines)
        for mine in mines:
            mine.is_mine = True

    def __str__(self):

        lines = []

        horizontal_break = "+".join("-" for _ in range(self.size_x))
        horizontal_break = "+" + horizontal_break + "+"
        lines.append(horizontal_break)

        for row in self.cells:
            row_string = "|".join(str(cell) for cell in row)
            lines.append("|" + row_string + "|")
            lines.append(horizontal_break)

        return "\n".join(lines)
