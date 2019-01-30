class Node:
    # The puzzleState atribute is the array of integers that represents the state of the puzzle
    # [0, 1, 2
    #  3, 4, 5
    #  6, 7, 8]
    def __init__(self, arr):
        self.puzzleState = arr
        self.spaceIndex = 0         # index where the zero value is. The space of the puzzle
        for i in range(len(arr)):
            if (arr[i] == 0):
                self.spaceIndex = i
        self.__verticalDistance = 3 # Distance to simulate moving the space of the puzzle up or down

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
        if self.__onUpperBound(self.spaceIndex):
            return None  
        else:
            return self.__moveSpace(self.spaceIndex - self.__verticalDistance)
    
    def down(self):
        if self.__onLowerBound(self.spaceIndex):
            return None  
        else:
            return self.__moveSpace(self.spaceIndex + self.__verticalDistance)

    def left(self):
        if self.__onLeftBound(self.spaceIndex):
            return None  
        else:
            return self.__moveSpace(self.spaceIndex - 1)

    def right(self):
        if self.__onRightBound(self.spaceIndex):
            return None
        else:
            return self.__moveSpace(self.spaceIndex + 1)

    def posiblePaths(self):
        paths = []
        state = self.up()
        if (state != None):
            paths.append(state)
        
        state = self.down()
        if (state != None):
            paths.append(state)

        state = self.left()
        if (state != None):
            paths.append(state)

        state = self.right()
        if (state != None):
            paths.append(state)
        
        return paths
    
def debugMethods():
    x = Node([0, 1, 2, 3, 4, 5, 6 ,7 ,8])
    print(x.right())
    print(x.down())
    print(x.left())
    print(x.up())
    print("_________")
    print(x.posiblePaths())

if __name__ == "__main__":
    debugMethods()