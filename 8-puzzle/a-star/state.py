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
