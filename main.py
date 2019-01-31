import sys

from timeit import default_timer as timer
from collections import deque

from node import Node
from state import State

def breadthFirstSearch(initialState, finalState):
    """Search by width algorithm"""

    def exploreNext(neighbor, move):
        """Finds out if the neighbor is withinf the boundaries and explore it.
        `explored` is the set used in the BFS function.
        `stateQueue` is the queue inside the BFS function.
        `currentState` is each visited node inside the loop of the BFS function.

        """
        if (neighbor != None and tuple(neighbor) not in explored):
            nextState = State(neighbor)
            nextState.path = currentState.path.copy()
            nextState.path.append(move)
            stateQueue.append(nextState)

    stateQueue = deque([])  # List of States
    explored = set()        # Set of tuples of each visited state of the puzzle
    sizeBytesCounter = 0

    # Init queue
    stateQueue.append(State(initialState))

    # while queue is not empty
    while stateQueue:
        currentState = stateQueue.popleft()
        sizeBytesCounter += sys.getsizeof(currentState)

        # Add an unmodified list to the set, a tuple
        explored.add(tuple(currentState.puzzle))

        if finalState == currentState.puzzle:
            return currentState, explored, sizeBytesCounter
        
        # Create a node of the current state
        currentNode = Node(currentState.puzzle)

        # Iterate over posible paths
        exploreNext(*currentNode.up())
        exploreNext(*currentNode.down())
        exploreNext(*currentNode.left())
        exploreNext(*currentNode.right())
            
    return None

def main():
    initialState = []
    goal = [0, 1, 2, 3, 4, 5, 6, 7, 8]

    with open("puzzle.txt", "r") as file:
        line = file.readline()
        for val in line.split(" "):
            initialState.append(int(val))
    
    start = timer()
    finalState, exploredSet, size = breadthFirstSearch(initialState, goal)
    end = timer()
    
    if finalState.path != None:
        print("=" * 20)
        print("Solution depth or cost: %d" % len(finalState.path))
        print("=" * 20)
        print("Number of visited nodes: %d" % len(exploredSet))
        print("=" * 20)
        print("Running time: %f" % (end - start))
        print("=" * 20)
        print("Used memory: %d bytes" % size)
        print("=" * 20)
        print("This are the movements to solve the puzzle:")
        print("-" * 20)

        for move in finalState.path:
            print(move)
    else:
        print("It has no solution :(")

main()