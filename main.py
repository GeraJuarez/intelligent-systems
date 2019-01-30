import sys

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

    # Init queue
    stateQueue.append(State(initialState))

    # while queue is not empty
    while stateQueue:
        currentState = stateQueue.popleft()

        # Add an unmodified list to the set, a tuple
        explored.add(tuple(currentState.puzzle))

        if finalState == currentState.puzzle:
            return currentState, explored
        
        # Create a node of the current state
        currentNode = Node(currentState.puzzle)
        
        # Iterate over posible paths
        exploreNext(*currentNode.up())
        exploreNext(*currentNode.down())
        exploreNext(*currentNode.left())
        exploreNext(*currentNode.right())
            
    return None

def main():
    #with open("hola.txt", "r") as file:

    initialState = [1,2,5,3,4,0,6,7,8] # read from textfile
    goal = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    
    finalState, exploredSet = breadthFirstSearch(initialState, goal)
    
    if finalState.path != None:
        print("=" * 20)
        print("Solution depth or cost: %d" % len(finalState.path))
        print("=" * 20)
        print("Number of visited nodes: %d" % len(exploredSet))
        print("=" * 20)
        print("Running time:")
        print("=" * 20)
        print("Used memory:")
        print("=" * 20)
        print("This are the movements to solve the puzzle")
        print("-" * 20)

        for move in finalState.path:
            print(move)
    else:
        print("It has no solution :(")

main()