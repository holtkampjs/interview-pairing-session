class ConwaysGameOfLife:
    """An instance of Conway's Game of Life"""
    def __init__(self, state=None):
        """Initializer"""
        self._state = state

    def get_next_generation(self):
        """Perform 1 cycle of the game"""
        return [0 for cell in self._state]
