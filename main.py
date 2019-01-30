from collections import deque
from node import Node
from state import State

def breadthFirstSearch(initialState, finalState):
    def exploreNext(neighbor, move):
        if (neighbor != None and tuple(neighbor) not in explored):
            nextState = State(neighbor)
            nextState.path = currentState.path.copy()
            nextState.path.append(move)
            stateQueue.append(nextState)

    stateQueue = deque([])  # List of States
    explored = set()        # Set of tuples of each visited state of the puzzle

    # Init queue
    stateQueue.append(State(initialState))

    # while queue is not empty
    while stateQueue:
        currentState = stateQueue.popleft()

        # Add an unmodified list to the set, a tuple
        explored.add(tuple(currentState.puzzle))

        if finalState == currentState.puzzle:
            return currentState.path
        
        # Create a node of the current state
        currentNode = Node(currentState.puzzle)

        # Iterate over posible paths
        exploreNext(*currentNode.up())
        exploreNext(*currentNode.down())
        exploreNext(*currentNode.left())
        exploreNext(*currentNode.right())
            
    return None

def main():
    initialState = [1, 5, 4, 2, 7, 6, 0, 3, 8]
    goal = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    
    path = breadthFirstSearch(initialState, goal)
    
    if path != None:
        for move in path:
            print(move)
    else:
        print("It has no solution :(")

main()