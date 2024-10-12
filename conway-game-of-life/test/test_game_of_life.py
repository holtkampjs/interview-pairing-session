from src.game_of_life import ConwaysGameOfLife
from itertools import product


def test_initialization():
    game = ConwaysGameOfLife()
    assert game


def test_empty_create_world_three_by_three():
    game = ConwaysGameOfLife(size=3)
    assert game.size == 3
    assert game.state == [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]


def test_populate_world_three_by_three():
    game = ConwaysGameOfLife(size=3, alive=[(0, 0)])
    assert game.state == [
        [1, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]


def test_get_neighbors_three_by_three_population_of_one():
    game = ConwaysGameOfLife(size=3, alive=[(0, 0)])
    assert game.neighbors == [
        [0, 1, 0],
        [1, 1, 0],
        [0, 0, 0]
    ]


def test_get_neighbors_three_by_three_population_of_three():
    game = ConwaysGameOfLife(size=3, alive=[(0, 0), (1, 1), (1, 2)])
    assert game.neighbors == [
        [1, 3, 2],
        [2, 2, 1],
        [1, 2, 2]
    ]


def test_underpopulation_one_lone_cell():
    game = ConwaysGameOfLife(size=3, alive=[(0, 0)])
    next_generation = game.get_next_generation()
    assert next_generation.state == [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ], "All cells should be dead"


def test_underpopulation_one_lone_cell_tiny_board():
    game = ConwaysGameOfLife(size=1, alive=[(0, 0)])
    next_generation = game.get_next_generation()
    assert next_generation.state == [[0]], "All cells should be dead"


def test_cell_living_on_with_two_neighbors():
    game = ConwaysGameOfLife(
        size=3,
        alive=[(0, 0), (0, 1), (0, 2), (2, 0), (2, 1), (2, 2)]
    )
    next_generation = game.get_next_generation()
    assert next_generation.state == [
        [0, 1, 0],
        [0, 0, 0],
        [0, 1, 0]
    ], "The cells at (0, 1) and (2, 1) should be alive"


def test_cell_living_on_with_three_neighbors():
    game = ConwaysGameOfLife(size=3, alive=[(0, 0), (0, 1), (1, 0), (1, 1)])
    next_generation = game.get_next_generation()
    assert next_generation.state == [
        [1, 1, 0],
        [1, 1, 0],
        [0, 0, 0]
    ]


def test_overpopulation_cell_with_more_than_three_neighbors():
    # Expected
    #
    # 1 1 1    1 1 1
    # 0 1 0 -> 0 0 0
    # 1 1 1    1 1 1
    game = ConwaysGameOfLife(
        size=3,
        alive=[(0, 0), (0, 2), (2, 0), (2, 2), (1, 1), (0, 1), (2, 1)]
    )
    next_generation = game.get_next_generation()
    assert next_generation.state == [
        [1, 1, 1],
        [0, 0, 0],
        [1, 1, 1]
    ]


def test_overpopulation_fully_populated():
    game = ConwaysGameOfLife(
        size=3,
        alive=list(product(range(3), repeat=2))
    )
    next_generation = game.get_next_generation()
    assert next_generation.state == [
        [1, 0, 1],
        [0, 0, 0],
        [1, 0, 1]
    ]


def test_reproduction_with_one_cell_in_three_corners_of_three_by_three():
    game = ConwaysGameOfLife(
        size=3,
        alive=[(0, 0), (0, 2), (2, 0)]
    )
    next_generation = game.get_next_generation()
    assert next_generation.state == [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ], "Center cell should be produced, others should perish"
