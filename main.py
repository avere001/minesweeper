import itertools

from grid import Grid


def validate(user_input, max_x, max_y):
    try:
        x, y = user_input.split()
    except ValueError:
        raise ValueError("please separate your x and y values with a space")

    try:
        x, y = int(x), int(y)
    except ValueError:
        raise ValueError("x and y must be integers")

    if 1 <= x <= max_x and 1 <= y <= max_y:
        return x - 1, y - 1
    else:
        raise ValueError(f"{x} {y} is not a valid cell")


if __name__ == "__main__":

    grid = Grid(10, 10, num_mines=10)

    while True:
        print(grid)
        response = input("select a cell to reveal (format: x y): ")
        try:
            x, y = validate(response, 10, 10)
        except ValueError as e:
            input(f"oops: {e}. (press enter)")
            continue

        grid.cells[y][x].reveal()
