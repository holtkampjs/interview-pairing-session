from src.game_of_life import ConwaysGameOfLife, Cell


def test_initialization():
    game = ConwaysGameOfLife([[]])
    assert game


def test_empty_board_of_one_by_one():
    board = [[Cell.DEAD]]
    game = ConwaysGameOfLife(board)
    result = game.get_next_generation()
    assert result == [[Cell.DEAD]], "expects all cells to be dead"


def test_one_alive_cell_with_less_than_two_neigbors():
    board = [[Cell.DEAD, Cell.ALIVE]]
    game = ConwaysGameOfLife(board)
    result = game.get_next_generation()
    assert result == [[Cell.DEAD, Cell.DEAD]], "expects all cells to be dead"


def test_live_cell_with_two_live_neighbors():
    state = [[Cell.ALIVE, Cell.ALIVE, Cell.ALIVE]]
    game = ConwaysGameOfLife(state)
    result = game.get_next_generation()

    # Center cell should be alive
    assert result[0][0] == Cell.DEAD, "expects cell 0, 0 to be dead"
    assert result[0][1] == Cell.ALIVE, "expects cell 0, 1 to be alive"
    assert result[0][2] == Cell.DEAD, "expects cell 0, 2 to be dead"


def test_neighbor_count_trivial():
    state = [[Cell.DEAD]]
    game = ConwaysGameOfLife(state)
    result = game.neighbors

    assert result == [[0]], "should contain 1 cell indicating no neighbors"


def test_neighbor_count_trivial_alive():
    state = [[Cell.ALIVE]]
    game = ConwaysGameOfLife(state)
    result = game.neighbors

    assert result == [[0]], "should contain 1 cell indicating no neighbors"
    

def test_neighbor_count_one():
    state = [[Cell.ALIVE, Cell.DEAD]]
    game = ConwaysGameOfLife(state)
    result = game.neighbors

    assert result == [[0, 1]], "should contain [0, 1] indicating 1 neighbor to cell 0, 1"
