from itertools import product
from typing import TypeAlias, TypeVar

Point: TypeAlias = tuple[int, int]
Grid: TypeAlias = list[list[bool]]
T = TypeVar('T')
DEAD: bool = False
ALIVE: bool = True


class ConwaysGameOfLife:
    _size: int
    _state: Grid
    _neighbors: list[list[int]]

    def __init__(self, *, size: int = 0, alive: set[Point] = set()):
        # world is a square
        self._size = size

        def populate_grid(value: T) -> list[list[T]]:
            return [[value] * self._size for _ in range(self._size)]

        # initialize all cells to false (dead)
        self._state = populate_grid(DEAD)

        # initialize neighbor count to zero
        self._neighbors = populate_grid(0)

        def is_out_of_bounds(row: int, col: int, size: int) -> bool:
            return row < 0 or col < 0 or row >= size or col >= size

        for row, col in alive:
            # skip if out of bounds
            if is_out_of_bounds(row, col, self._size):
                continue

            # populate alive cell
            self._state[row][col] = ALIVE

            # increment neighbor counts
            neighbor_cells = product(range(row-1, row+2), range(col-1, col+2))
            for r, c in neighbor_cells:
                # skip if out of bounds
                if is_out_of_bounds(r, c, self._size):
                    continue

                # skip if equal to cell being populated
                if r == row and c == col:
                    continue
                self._neighbors[r][c] += 1

    @property
    def size(self) -> int:
        return self._size

    @property
    def state(self) -> Grid:
        return self._state

    def _will_cell_be_alive(self, index: Point) -> bool:
        row, col = index
        neighbor_count = self._neighbors[row][col]
        if neighbor_count == 2 and self._state[row][col] is ALIVE:
            return True
        if neighbor_count == 3:
            return True
        return False

    def get_next_generation(self):
        cell_indicies = product(range(self._size), repeat=2)
        alive_cells = filter(self._will_cell_be_alive, cell_indicies)
        return ConwaysGameOfLife(size=self._size, alive=alive_cells)
