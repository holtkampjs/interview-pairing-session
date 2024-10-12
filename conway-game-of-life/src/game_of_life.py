from itertools import product
from typing import Generator


class ConwaysGameOfLife:
    def __init__(self, *, size: int = 0, alive: list[tuple[int, int]] = []):
        # world is a square
        self._size: int = size

        # initialize all cells to zero (dead)
        self._state: list[list[int]] = [
            [0] * self._size for _ in range(self._size)
        ]

        # initialize neighbor count to zero
        self._neighbors: list[list[int]] = [
            [0] * self._size for _ in range(self._size)
        ]

        # populate alive cells and neighbor count
        for row, col in alive:
            self._state[row][col] = 1
            for r, c in self._get_neighbors(row, col):
                self._neighbors[r][c] += 1

    def _get_neighbors(
        self,
        row: int,
        col: int
    ) -> Generator[tuple[int, int], None, None]:
        for r, c in product(range(row-1, row+2), range(col-1, col+2)):
            # skip if the cell for neighbor calculation
            if r == row and c == col:
                continue

            # skip if out of bounds
            if r < 0 or c < 0 or r >= self._size or c >= self._size:
                continue

            yield (r, c)

    @property
    def size(self) -> int:
        return self._size

    @property
    def state(self) -> list[list[int]]:
        return self._state

    @property
    def neighbors(self) -> list[list[int]]:
        return self._neighbors

    def _will_cell_be_alive(self, index: tuple[int, int]) -> bool:
        row, col = index
        neighbor_count = self._neighbors[row][col]
        if neighbor_count == 2 and self._state[row][col] == 1:
            return True
        if neighbor_count == 3:
            return True
        return False

    def get_next_generation(self):
        cell_indicies = product(range(self._size), repeat=2)
        alive_cells = filter(self._will_cell_be_alive, cell_indicies)
        return ConwaysGameOfLife(size=self._size, alive=alive_cells)
