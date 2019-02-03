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

def main(arg):
    initialState = []
    goal = [0, 1, 2, 3, 4, 5, 6, 7, 8]

    with open(arg, "r") as file:
        line = file.readline()
        for val in line.split(" "):
            initialState.append(int(val))

    if set(goal) != set(initialState):
        sys.exit("ERROR: input is not valid, it must have numbers from 0 to 8")
    elif len(goal) != len(initialState):
        sys.exit("ERROR: invalid input, it must have nine numbers, from 0 to 8")
    
    start = timer()
    finalState, exploredSet, size = breadthFirstSearch(initialState, goal)
    end = timer()
    
    if finalState != None:
        print("=" * 20)
        print("Solution depth or cost: %d" % len(finalState.path))
        print("=" * 20)
        print("Number of visited nodes: %d" % len(exploredSet))
        print("=" * 20)
        print("Running time: %f sec" % (end - start))
        print("=" * 20)
        print("Bytes per node: %d" % sys.getsizeof(State(goal)))
        print("Used memory: %d bytes" % size)
        print("=" * 20)
        print("This are the movements to solve the puzzle:")
        print("-" * 20)
        print(*finalState.path, sep=' => ')
    else:
        print("It has no solution :(")

if len(sys.argv) < 2:
    sys.exit("ERROR: The program needs the name of the file with the initial state of the puzzle as an argument when executing")
elif len(sys.argv) > 2:
    sys.exit("ERROR: too many arguments")

main(sys.argv[1])