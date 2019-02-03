class State:
    """The data about the current puzzle state and the paths taken so far.

    Args:
        arr: The array of integers that represent the positions of the puzzle.

    Attributes:
        puzzle: Human readable string describing the exception.
        path: The current path taken form the original state to the current.

    """
    def __init__(self, arr):
        self.puzzle = arr
        self.path = []
        self.g_heuristic = 0

    def __str__(self):
        return str(self.puzzle) + " : " + str(self.g_heuristic)

    def __lt__(self, other):
        return self.g_heuristic < other.g_heuristic

