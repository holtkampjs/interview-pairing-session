from collections import namedtuple
from copy import deepcopy
from enum import Enum

Offset = namedtuple('Offset', ['row', 'col'])


class Cell(Enum):
    DEAD = 0
    ALIVE = 1


# TODO: Create base class for initializing board
# TODO: Create class for playing game state
# TODO: Create class for static state
class ConwaysGameOfLife:
    """An instance of Conway's Game of Life"""
    _neighbors = None
    _neighbor_index_offsets: tuple[Offset] = (
        Offset(row=-1, col=-1),
        Offset(row=-1, col=0),
        Offset(row=-1, col=1),
        Offset(row=0, col=-1),
        Offset(row=0, col=1),
        Offset(row=1, col=-1),
        Offset(row=1, col=0),
        Offset(row=1, col=1),
    )

    def __init__(self, state: list[list[Cell]]):
        """Initializer"""
        self._state = state
        self._row_count = len(state)
        self._col_count = len(state[0])

    def _filter_out_of_bounds(self, coordinate: Offset) -> bool:
        out_of_bounds: bool = (
            coordinate.row < 0
            or coordinate.col < 0
            or coordinate.row > self._row_count-1
            or coordinate.col > self._col_count-1
        )
        return not out_of_bounds

    def _get_neigbor_count(self, row_idx: int, col_idx: int) -> int:
        neighbor_indicies: tuple[Offset] = (
            Offset(row=row_idx+offset.row, col=col_idx+offset.col)
            for offset
            in self._neighbor_index_offsets
        )
        neighbor_indicies: tuple[Offset] = tuple(
            filter(self._filter_out_of_bounds, neighbor_indicies)
        )
        return sum([
            self._state[index.row][index.col].value
            for index in neighbor_indicies
        ])

    @property
    def neighbors(self):
        if not self._neighbors:
            self._neighbors = [
                [
                    self._get_neigbor_count(row_idx, col_idx)
                    for col_idx in range(len(self._state[row_idx]))
                ]
                for row_idx in range(len(self._state))
            ]
        return self._neighbors

    # def _convert_neighbors_to_status(self, row: list[int]) -> list[Cell]:
    #     pass

    # def get_next_generation(self):
    #     """Perform 1 cycle of the game"""
    #     neigbor_map: list[list] = deepcopy(self.neighbors)
    #     for row in x

    #     for row_idx in range(self._row_count):
    #         next_generation.append(list())
    #         for col_idx in range(self._col_count):
    #             next_generation[row_idx].append(Cell.DEAD)
    #             neighbor_count = self.neighbors[row_idx][col_idx]
    #             if neighbor_count == 2:
    #                 next_generation[row_idx][col_idx] = self._state[row_idx][col_idx]
    #     return next_generation

    def get_next_generation(self):
        """Perform 1 cycle of the game"""
        next_generation: list = list()
        for row_idx in range(self._row_count):
            next_generation.append(list())
            for col_idx in range(self._col_count):
                next_generation[row_idx].append(Cell.DEAD)
                neighbor_count = self.neighbors[row_idx][col_idx]
                if neighbor_count == 2:
                    next_generation[row_idx][col_idx] = self._state[row_idx][col_idx]
        return next_generation
