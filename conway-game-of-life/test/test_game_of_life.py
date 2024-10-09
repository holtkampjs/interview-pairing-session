from src.game_of_life import ConwaysGameOfLife


def test_initialization():
    game = ConwaysGameOfLife()
    assert game


def test_empty_board_of_one_by_one():
    game = ConwaysGameOfLife([0])
    result = game.get_next_generation()
    assert result == [0]


def test_one_alive_cell_with_less_than_two_neigbors():
    game = ConwaysGameOfLife([0, 1])
    result = game.get_next_generation()
    assert result == [0, 0]


def test_live_cell_with_two_live_neighbors():
    game = ConwaysGameOfLife([1, 1, 1])
    result = game.get_next_generation()

    # Center cell should be alive
    assert result[1] == 1
