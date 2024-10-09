from enum import Enum


class Cell(Enum):
    DEAD = 0
    ALIVE = 1


class ConwaysGameOfLife:
    """An instance of Conway's Game of Life"""
    def __init__(self, state: list[list[Cell]]):
        """Initializer"""
        self._state = state
        self._row_count = len(state)
        self._col_count = len(state[0])

    def get_neighbor_count(self, row_idx: int, col_idx: int) -> list[list[Cell]]:
        row_slice = slice(max(0, row_idx-1), row_idx+2)
        col_slice = slice(max(0, col_idx-1), col_idx+2)
        count_by_row = [
            row[col_slice].count(Cell.ALIVE)
            for row in
            self._state[row_slice]
        ]
        count = sum(count_by_row) - self._state[row_idx][col_idx].value
        return count

    def get_next_generation(self):
        """Perform 1 cycle of the game"""
        next_generation: list = list()
        for row_idx in range(self._row_count):
            next_generation.append(list())
            for col_idx in range(self._col_count):
                next_generation[row_idx].append(Cell.DEAD)
                neighbor_count = self.get_neighbor_count(row_idx, col_idx)
                if neighbor_count == 2:
                    next_generation[row_idx][col_idx] = self._state[row_idx][col_idx]
        return next_generation
