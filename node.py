class Node:
    def __init__(self, arr):
        self.board = arr
        self.spaceIndex = 0
        for i in range(len(arr)):
            if (arr[i] == 0):
                self.spaceIndex = i

    def __str__(self): # string
        return self.board

    def __repr__(self): # in a list or other structure
        return self.board

    def up(self):
        if self.spaceIndex in range(0, 3):
            return None  
        else:
            pass
    
    def down(self):
        if self.spaceIndex in range(6, 9):
            return None  
        else:
            pass

    def left(self):
        if self.spaceIndex == 0 or self.spaceIndex == 3 or self.spaceIndex == 6:
            return None  
        else:
            pass

    def right(self):
        self.spaceIndex == 2 or self.spaceIndex == 5 or self.spaceIndex == 8:
            return None
        else:
            pass
    