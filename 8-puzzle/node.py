class Node:
    """Node calculates the available paths of the state it obtains as parameter
    [0, 1, 2
     3, 4, 5
     6, 7, 8]

    Args:
        arr: The array of integers that represent the positions of the puzzle.

    Attributes:
        puzzleState: The current positions of the puzzle
        spaceIndex: the index where the zero value or space is located inside the array

    """
    def __init__(self, arr):
        self.puzzleState = arr
        self.spaceIndex = 0             # index where the zero value is. The space of the puzzle
        for i in range(len(arr)):
            if (arr[i] == 0):
                self.spaceIndex = i
        self.__verticalDistance = 3     # Distance to simulate moving the space of the puzzle up or down
        self.__horizontalDistance = 1   # Distance to simulate moving the space of the pussle left or right

    def __onUpperBound(self, index):
        return index in range(0, 3)

    def __onLowerBound(self, index):
        return index in range(6, 9)

    def __onLeftBound(self, index):
        return index == 0 or index == 3 or index == 6

    def __onRightBound(self, index):
        return index == 2 or index == 5 or index == 8

    def __moveSpace(self, newIndex):
        newState = self.puzzleState.copy()
        newState[self.spaceIndex] = newState[newIndex]
        newState[newIndex] = 0
        return newState

    def up(self):
        """Changes to a state where the space is moved upwards in the puzzle

        Return:
            An array of integers that represent the next state of the puzzle

        """
        if self.__onUpperBound(self.spaceIndex):
            return None, None
        else:
            return self.__moveSpace(self.spaceIndex - self.__verticalDistance), "UP"
    
    def down(self):
        """Changes to a state where the space is moved downwards in the puzzle

        Return:
            An array of integers that represent the next state of the puzzle

        """
        if self.__onLowerBound(self.spaceIndex):
            return None, None
        else:
            return self.__moveSpace(self.spaceIndex + self.__verticalDistance), "DOWN"

    def left(self):
        """Changes to a state where the space is moved to the left in the puzzle

        Return:
            An array of integers that represent the next state of the puzzle

        """
        if self.__onLeftBound(self.spaceIndex):
            return None, None
        else:
            return self.__moveSpace(self.spaceIndex - self.__horizontalDistance), "LEFT"

    def right(self):
        """Changes to a state where the space is moved to the right in the puzzle

        Return:
            An array of integers that represent the next state of the puzzle

        """
        if self.__onRightBound(self.spaceIndex):
            return None, None
        else:
            return self.__moveSpace(self.spaceIndex + self.__horizontalDistance), "RIGHT"
    
def debugMethods():
    x = Node([0, 1, 2, 3, 4, 5, 6 ,7 ,8])
    print(x.right())
    print(x.down())
    print(x.left())
    print(x.up())

if __name__ == "__main__":
    debugMethods()