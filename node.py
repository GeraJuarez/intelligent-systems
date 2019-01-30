class Node:
    # The board atribute is the array of integers that represents the state of the puzzle
    # [0, 1, 2
    #  3, 4, 5
    #  6, 7, 8]
    def __init__(self, arr):
        self.board = arr
        self.spaceIndex = 0
        for i in range(len(arr)):
            if (arr[i] == 0):
                self.spaceIndex = i
        self.__verticalDistance = 3 # Distance to simulate moving the space of the puzzle up or down

    def __repr__(self): # in a list or other structure
        return self.board

    def __onUpperBound(self, index):
        return index in range(0, 3)

    def __onLowerBound(self, index):
        return index in range(6, 9)

    def __onLeftBound(self, index):
        return index == 0 or index == 3 or index == 6

    def __onRightBound(self, index):
        return index == 2 or index == 5 or index == 8

    def __swapValues(self, newIndex):
        self.board[self.spaceIndex] = self.board[newIndex]
        self.board[newIndex] = 0
        self.spaceIndex = newIndex

    def up(self):
        if self.__onUpperBound(self.spaceIndex):
            return None  
        else:
            self.__swapValues(self.spaceIndex - self.__verticalDistance)
            return self.board
    
    def down(self):
        if self.__onLowerBound(self.spaceIndex):
            return None  
        else:
            self.__swapValues(self.spaceIndex + self.__verticalDistance)
            return self.board

    def left(self):
        if self.__onLeftBound(self.spaceIndex):
            return None  
        else:
            self.__swapValues(self.spaceIndex - 1)
            return self.board

    def right(self):
        if self.__onRightBound(self.spaceIndex):
            return None
        else:
            self.__swapValues(self.spaceIndex + 1)
            return self.board
    
def debugMethods():
    x = Node([0, 1, 2, 3, 4, 5, 6 ,7 ,8])
    print(x.right())
    print(x.down())
    print(x.left())
    print(x.up())

if __name__ == "__main__":
    debugMethods()