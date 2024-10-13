from itertools import product
from typing import TypeAlias

Point: TypeAlias = tuple[int, int]
Grid: TypeAlias = list[list[bool]]
DEAD: bool = False
ALIVE: bool = True


class ConwaysGameOfLife:
    def __init__(self, *, size: int = 0, alive: list[Point] = []):
        # world is a square
        self._size: int = size

        # initialize all cells to false (dead)
        self._state: Grid = [
            [DEAD] * self._size for _ in range(self._size)
        ]

        # initialize neighbor count to zero
        self._neighbors: list[list[int]] = [
            [0] * self._size for _ in range(self._size)
        ]

        for row, col in alive:
            # populate alive cell
            self._state[row][col] = ALIVE

            # increment neighbor counts
            for r, c in product(range(row-1, row+2), range(col-1, col+2)):
                # skip if out of bounds
                if r < 0 or c < 0 or r >= self._size or c >= self._size:
                    continue
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
